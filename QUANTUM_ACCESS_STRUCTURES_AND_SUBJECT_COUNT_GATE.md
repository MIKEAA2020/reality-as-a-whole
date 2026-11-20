# Quantum access is not a subject count

## Result

The same quantum information can be recoverable from several overlapping physical regions without being several independent copies. Conversely, the same yes/no pattern of which regions can recover information can describe different amounts of independent quantum information. Therefore a proposed subject selector cannot count **recovering regions** as subjects, or use a bare recoverability pattern as a sufficient subject count, without extra rules.

This is a precise **physical bookkeeping constraint**, not a theory of consciousness. It does not say that quantum information is experience, that a logical qutrit is a subject, or that actual observers use a quantum code. The existing [weak-record gate](WEAK_RECORD_COHERENCE_AND_PERSPECTIVE_GATE.md) distinguished history amplitudes from access to records. Here we sharpen the next step: **even full quantum recoverability, stronger than recovery of one classical record, is not a rule for individuating subjects.**

The mathematical machinery and the three-qutrit code are established, not new. We apply them to a subject-counting criterion and provide an exact verifier. The principal source is Cleve, Gottesman and Lo, [*How to Share a Quantum Secret*](https://arxiv.org/html/quant-ph/9901025), including their `((2,3))` code and no-cloning argument. The [Error Correction Zoo entry](https://errorcorrectionzoo.org/c/stab_3_1_2) discusses multiple physical representations of the same logical operator. For the broader operator-algebra context, see Pastawski and Preskill, [*Code Properties from Holographic Geometries*](https://arxiv.org/html/1612.00017v2). Source-reading limits appear below.

## 1. What access means here

Take a specified isometric encoding `V` of a logical state into physical parties `A`, `B`, `C`. A set `S` is **authorized** if there is a quantum channel acting on its shares that recovers *every* input state, including arbitrary entanglement with an untouched reference. It is not enough to guess one basis label, obtain a correlation, or recover just one known state. A set is **blind** if its reduced state is independent of the logical input, including the corresponding reference correlations.

These definitions describe a controlled physical communication or storage task. They require the input family, encoding, accessible parties, permitted recovery operations and reference system to be specified. They do not assume that any party is a person. Recovery is a possible operation, not evidence that it was actually performed or that the same information was simultaneously recovered in multiple places.

## 2. An exact overlapping-access example

All arithmetic below is modulo 3. The known code maps a qutrit basis state as

`V|s⟩ = (1/√3) Σ_{r=0}² |r, r+s, r+2s⟩_ABC`, for `s=0,1,2`,

and extends linearly to arbitrary states. An individual share is maximally mixed and independent of the input. Any two shares can recover the entire quantum input. Thus the *minimal* authorized sets are

`{A,B}`, `{A,C}`, `{B,C}`.

They overlap pairwise; their intersections `{A}`, `{B}`, `{C}` are blind. This is not a partition into disjoint supports and there is no unique minimal region. Counting the three pairs as three separate recovered qutrits would mistake three alternative recovery procedures for three independent copies of the one encoded qutrit. Nor can the overlap be identified as the information-bearing subsystem: each singleton is blind.

A concrete pair decoder shows what this means. Let the two accessible positions be `i,j ∈ {0,1,2}` and the missing one `k`; let their basis labels be `x_i,x_j`. Apply the reversible basis permutation

`(x_i,x_j) ↦ (s,q)` where `s=(x_j−x_i)/(j−i)` and `q=x_i+(k−i)s`.

Since `j−i` is nonzero modulo 3, its inverse exists. After this pair-only unitary, the global state is

`|ψ⟩_decoded ⊗ (1/√3) Σ_q |q⟩_aux |q⟩_missing`

for any input `|ψ⟩`, including when it is entangled with a reference. The leftover state is independent of `|ψ⟩`. The decoder does not measure the shares individually. Once one recovery has acted on a pair, one must account for its action before discussing a different recovery; the overlapping procedures are not simultaneous independent readouts.

For arbitrary unknown quantum states, disjoint sets cannot each recover a perfect copy: applying both recoveries would violate no-cloning, as Cleve et al. explain. This restriction does **not** prevent redundancy of a fixed classical observable or known orthogonal states. It also does not assert that conscious experiences are unknown quantum states or that subjects cannot be duplicated.

## 3. Same Boolean access pattern, different information capacity

Use two independent copies of the same encoder `V⊗V`, grouping each pair of local qutrits as one party. Each of `A`, `B`, and `C` now has the same physical Hilbert-space dimension `9` in both cases below; the physical encoder is also the same.

| Declared input family | Logical space | Singleton access | Any pair access |
|---|---:|---|---|
| First logical qutrit arbitrary, second fixed to `|0⟩` | dimension 3 | blind to the varying input | exact recovery |
| Both logical qutrits arbitrary, possibly jointly entangled with a reference | dimension 9 | blind to both | exact recovery of both jointly |

The Boolean authorized-set family is identical: the three pairs and their superset. Yet the two specified input families support different quantum information capacity, `log₂3` versus `log₂9` qubits. Their accessible variation is genuinely different: allowing the second input to vary supplies additional operational tests. In fact, on the common preparation `|0⟩⊗|0⟩` the physical encoded state and circuit can be identical. A single actual state plus the coarse yes/no access table does not fix the intended input family or independently varying content.

The dimension distinction is physical and testable **if** the different inputs and reference-sensitive recoveries can be prepared and assessed. It is not a count of independent minds. Even decomposing a nine-dimensional logical algebra into two qutrit factors requires a specified tensor-factor structure; mathematical factor choices alone do not constitute autonomous experiential subjects. More generally, an `n`-fold tensor power has the same three-party threshold pattern for its full `3ⁿ`-dimensional logical input. Our verifier checks `n=1,2`, while the tensor-product extension follows from the cited code and factorwise decoding.

## 4. A constructive interface for plural perspectives

This suggests a more careful candidate interface, without claiming that it solves subject constitution:

1. **Declare the physical task:** code/input family, state preparations including reference correlations, region partition, permitted operations and local relational ordering. Access here concerns a tested channel, not an inferred phenomenal fact.
2. **Identify represented content, not merely supports.** For a fixed encoding and logical operator `O`, two physical operators `O_AB`, `O_AC` represent the same logical action when `O_AB V=V O` and `O_AC V=V O` on the same code. They can differ outside it. This is a code-dependent equivalence of implementations, not proof they are the same person. Merely noting that two algebras are abstractly isomorphic is insufficient: independent copies can be isomorphic too.
3. **Keep independently varying content distinct.** Specify compatible logical algebras or operational input–output channels, their allowed joint preparations, and which physical resources they share. Do not identify separate inputs just because their access sets coincide. Conversely, avoid multiplying one content because its implementations have different supports.
4. **Add an occurrence/maintenance condition.** Perfect recoverability is a counterfactual capability and can exist in a static encoded state. A candidate subject rule must specify the realized processes, interaction structure, interval and how they map to experiential occurrences. It must not treat a decoder someone *could* perform as a process that *did* occur.
5. **Add a phenomenal and identity rule.** Specify what makes the process an experience, what binds contents into one subject, and how subjects persist or diverge. These are not fixed by code equivalence, distinguishable classical records, or a count of logical factors. Investigate symmetry, fission and overlap with the prior [ties and persistence gate](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md).
6. **State the scope of invariance.** Transport the encoding, admissible states, regions and interventions together under a genuine redescription. Arbitrary repartitioning can change which operations are physically local. A quotient by code-equivalent implementations is appropriate only under the stated task; it is not a general proof of substrate independence or a substitute for mapping physically admissible interventions.

A quantum code may help describe how one information-bearing structure is multiply accessible without being multiply instantiated. Equally, the proposal of a timeless experiential whole may contain multiple genuine subjects—but neither follows from the other. Interpersonal comparison of classical records requires an additional physical account. For background on operational notions of shared classical information, Le and Olaya-Castro's [*Strong Quantum Darwinism and Strong Independence is equivalent to Spectrum Broadcast Structure*](https://arxiv.org/html/1803.08936v2) distinguishes different definitions of objectivity; their notion does not itself establish phenomenal subjecthood.

## 5. Boundaries and next test

The example is an ideal finite code, not an empirical model of a human, a brain, or quantum gravity. It supplies no cosmological boundary, fundamental time, self-subsistence, experiential quality, or measure over subjects. The operational ordering used in encoding and recovery is internal to the task, not a universal external clock. Nor does a code-space equality prove two mathematical descriptions are physically equivalent in a concrete setting.

The next useful test is **not** to count code regions or logical factors as subjects. It is to compare two explicit process-and-constitution proposals on the same independently specified physical organization, including (i) overlapping recovery supports, (ii) two independently controlled logical inputs, (iii) actual versus merely possible recovery, and (iv) an independently justified experiential incidence assay. Until such an assay and constitution bridge are supplied, the test can reject bad physical bookkeeping but cannot decide how many genuine perspectives exist.

## Reproduction and source scope

Run `python verification/quantum_access_subject_count_gate.py`. Integer arithmetic checks all logical matrix units of the reduced singleton channel, bijectivity of all three pair-decoder permutations, and decoded basis terms for one and two qutrits; the restricted input case is checked within the same dimension-nine shares. Off-diagonal matrix units and the fixed decoded remainder support the arbitrary-reference claim, not merely basis-state guessing. The adjacent JSON records the finite checks.

- Cleve, Gottesman and Lo, [*How to Share a Quantum Secret*](https://arxiv.org/html/quant-ph/9901025): all five HTML text chunks and references read; no independent journal-version comparison or full proof audit.
- [*Three-qutrit code*, Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_3_1_2): substantive opening chunk read; remaining hierarchy material not audited.
- Pastawski and Preskill, [*Code Properties from Holographic Geometries*](https://arxiv.org/html/1612.00017v2): opening chunk of the available full preprint only; remaining sections, proofs and figures not audited. No holographic claim is needed for this finite result.
- Le and Olaya-Castro, [*Strong Quantum Darwinism and Strong Independence is equivalent to Spectrum Broadcast Structure*](https://arxiv.org/html/1803.08936v2): opening chunk of the available revised preprint only; the rest, proofs, figures and journal version were not audited. We do not assert their conclusions beyond their stated operational definitions.
