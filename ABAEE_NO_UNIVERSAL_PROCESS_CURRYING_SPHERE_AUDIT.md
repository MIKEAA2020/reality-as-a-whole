# Abaee's process-currying preprint and the internal sphere

**Related subsequent preprint:** [additive-dynamics and compression audit](ABAEE_ADDITIVE_DYNAMICS_AND_EXACT_DIAMOND_RADIUS.md) treats the universal continuous compression floor, distinguishes it from restricted sphere programming, and corrects the geometric in-radius remark without challenging the stated floor.

**Finite-reference continuation:** [the tetrahedral construction](FINITE_SPHERE_ZERO_REFERENCE_AND_SYMMETRIC_RECORDS.md) shows that continuous rotational invariance of a particular finite joint state does not entail exact universal programming of all measurement directions. A tailored invariant state-preparing Hamiltonian is likewise distinct from a universal processor.

## Source and scope

The supplied [DOI](https://doi.org/10.5281/zenodo.21795780) resolves to Amin Abaee, *No Universal Process Currying: The Intercept Principle, Environmental Currying, and Finite-Dimensional Obstructions to Exact Process Storage, Evaluation, and Recovery*, Zenodo preprint, version 4, published 4 August 2026. The record lists a manuscript and a supplementary verification archive.

I inspected the abstract, selected definitions and proofs of the finite-dimensional channel and programmable-evaluation results, the recoverability section, and parts of the discussion. The archive preview lists a README, output and script, but their contents were not retrieved or run in this environment. **This is a focused analysis, not a complete proof audit or an independent verification of every claim in the paper.** The record calls it a preprint; the record alone does not establish peer review.

## 1. The result in ordinary language

Abaee studies whether adding a fixed environment to a system can be represented by a universal, natural transformation that turns processes with that environment input into processes whose output is an ordinary finite quantum memory. In the category of finite-dimensional quantum channels, the proposed right adjoint would require natural correspondences of the form

```text
Chan(A ⊗ E, B)  ≅  Chan(A, M_B)
```

for every `A,B`, with `E` fixed. The paper proves that no such right adjoint exists for a nontrivial finite-dimensional `E`. Its corresponding left-adjoint result has a separate argument. Similar claims are developed for specifically defined stochastic and instrument categories. An adjoint here is a **universal representation of process spaces**, not simply an inverse for discarding an environment or a claim that no particular process is reversible.

A related operational theorem states that a **single fixed deterministic processor**, fed a state of a **finite-dimensional program memory**, cannot exactly implement every unitary channel on a nontrivial system. The paper explicitly connects this with the existing no-programming theorem; its categorical non-adjoint result is related but logically distinct. Approximate processors, restricted process families, probabilistic schemes, classical descriptions, and other categories are not ruled out by that exact statement.

A simple checked special case illustrates the dimension obstruction. For a qubit `E`, the affine dimension of all qubit channels is `2²(2²−1)=12`; the affine dimension of *all* density matrices on an `m`-dimensional system is `m²−1`. An affine isomorphism would require `m²=13`, impossible for integer `m`. More generally, for `e>1`,

```text
(e²−1)² < e⁴−e²+1 < (e²)².
```

This rules out that full-state-space affine isomorphism, not every useful embedding of channels in states. Choi states, for example, embed channels in a constrained subset of a larger state space; a description of a process is not automatically a universal deterministic evaluator of it. The preprint addresses this distinction explicitly.

## 2. A necessary clarification to our sphere model

The most relevant connection is to [our full-support spherical reference](ZERO_SPHERICAL_PLENITUDE_AND_BRANCHWISE_RECORD_BALANCE.md). There we used

```text
H_C=L²(S²,dμ),        c(n)=1,
```

and a fixed direction-controlled interaction. For each direction `n`, the corresponding mathematical fiber produces opposite correlated records. The constant wavefunction is normalized, and its support covers the sphere. The resulting full quantum state and the exact record-sum identity are valid within the model.

But **full support is not the same as a normalizable program that chooses an exact arbitrary direction on demand**. The formal `|n⟩` notation refers to generalized direction eigenvectors. A singleton on the sphere has measure zero, and a delta function at `n` is not an `L²` wavefunction. Conditioning a continuous-outcome experiment on an exact direction is expressed by an operator-valued density/regular conditional description, defined almost everywhere; it is not preparation of a normalized, exact-direction quantum state. Our prior report should not be read as providing a finite-dimensional universal sharp-measurement processor, or as establishing a separately actual event for every point.

This **does not invalidate** its pointwise fiber identity: a superposition with any normalizable reference wavefunction still lies in the kernel of the opposite-record sum when both record interactions use the same reference. It does constrain an additional interpretation—exactly selecting any one of uncountably many distinct sharp measurements using an ordinary physical program state. The preprint's finite-memory theorem concerns universal unitary-channel evaluation; the more specific measurement claim below has its own short argument and assumptions.

## 3. Why exact sharp directions need distinguishable programs

Suppose a fixed deterministic quantum processor takes a program state and a qubit, and outputs a fixed-labelled binary sharp measurement `P_±(n)=(I±n·σ)/2`. It must implement the specified measurement **exactly for every input state**. For two distinct oriented directions `n,m`, input `|+_n⟩` with program `n` gives outcome `+` with certainty, while input `|−_m⟩` with program `m` gives outcome `−` with certainty. Their input-qubit overlap obeys

```text
|⟨+_n|−_m⟩|² = (1−n·m)/2 > 0       when n≠m.
```

A Stinespring isometry for the fixed processor preserves input inner products, while the two certain output records occupy orthogonal outcome subspaces. Thus the two program states must be orthogonal. The same conclusion for mixed programs follows by applying the deterministic outcome constraints to every vector in their supports.

Consequently an `m`-dimensional program can exactly implement at most `m` **distinct fixed-labelled** sharp directions under these assumptions. A separable Hilbert space cannot contain uncountably many pairwise orthogonal normalizable programs either. The statement does not cover arbitrary approximate, probabilistic or measurement-assisted schemes with additional program-dependent classical processing, and it does not show that reality itself must be a programmable processor.

Conversely, a finite family of directions is straightforward: use mutually orthogonal program labels and a fixed controlled measurement. Our tests build the four-direction tetrahedral example. It gives exact balance and selected projective measurements for that family, but does not cover a continuum of selectable directions.

## 4. A normalizable approximation—and what survives exactly

Take a normalized reference wavepacket with constant amplitude inside a spherical cap of opening angle `δ>0` centered on `m`, and zero outside. If the direction is not read and one applies the previous controlled measurement, its effective `+` effect on the logical qubit is

```text
E_+ = ½(I+c m·σ),      c=(1+cos δ)/2.
```

The target sharp effect is `P_+(m)=½(I+m·σ)`. The maximum difference in the `+` outcome probability over input states is

```text
(1−c)/2 = (1−cos δ)/4.
```

For example, `δ=π/3` gives `c=3/4` and maximum probability error `1/8`. Every positive-width cap gives an unsharp effective measurement; shrinking it makes the error tend to zero, but the limiting delta state is not a normalized vector in this reference Hilbert space. A full-sphere uniform reference, when its direction is ignored, gives `E_+=I/2`. These are probability errors for this particular measurement construction, not a general optimal memory-size bound or the preprint's diamond-norm theorem.

The important positive result is that **opposite matched records survive the finite resolution**. For each fiber `n`, the record-sum operator annihilates the two-record state. Therefore it also annihilates any normalizable superposition of those fibers, including a finite-width cap. The model can retain exact internal cancellation without an exactly selected direction. What changes is the sharpness of the effective measurement relative to a separately specified target `m`.

This is a promising way to separate two ideas that had become conflated: all-direction symmetry of the whole need not mean every subject has an exact, independently selectable direction. It still does not show which records are actual subjects or how their felt characters are constituted.

## 5. Reversing a whole interaction is not recovering a reduced record

Abaee also contrasts universal process representation with recovery of **one specified channel**. For a finite-dimensional channel, exact recovery of all input states by a CPTP left inverse is equivalent to its complementary channel being constant on those inputs: the environment must carry no input-dependent information about the full input. The paper presents this as a standard recoverability result, not its novel theorem.

Our record model makes the distinction concrete. For a logical controlled-copy operation,

```text
|0⟩_S|0⟩_R → |0⟩_S|0⟩_R,
|1⟩_S|0⟩_R → |1⟩_S|1⟩_R.
```

The full `S+R` operation is unitary and can be undone if the coherent joint system remains accessible. But if `R` is discarded, the system channel dephases: `|+⟩` and `|−⟩` produce the same reduced output, so no recovery on `S` alone can recover every input. The complementary record distinguishes the `|0⟩` and `|1⟩` inputs. Recovery on a restricted set of basis states, or recovery with access to the full dilation, is a different claim.

The paper's ordered-instrument no-inverse result has another specific scope: outcome number is part of the morphism, so composing graded instruments multiplies the number of formally retained outcome labels. That should not be misread as proving that a premeasurement unitary on a closed system cannot be reversed. A classical outcome retained as a separate instrument label, a discarded environment, and a coherent pointer available to a global unitary are distinct operational situations.

## 6. Implication for the user's programme

The preprint does **not** show that a self-sufficient zero whole cannot contain its internal relations, nor that all genuine possibilities cannot be actual. Its results concern particular finite-dimensional process categories and exact, universal, deterministic processor assumptions. They do, however, expose a real obligation for the point–sphere proposal:

> Distinguish the whole's complete relational structure from a finite subsystem's ability to encode and exactly evaluate every possible process or choose every exact direction.

Our spherical reference currently represents the former only as a specified mathematical structure; it has not been derived from zero's own constitution. Neither its full support nor the preprint's obstruction settles actual subjectivity, signed felt valence, incidence, global energy zero or necessity. The finite-width calculation gives a constructive next target: develop internally realized finite-resolution records while preserving the exact matched-record balance, then justify the subjects, felt qualities and actual measure without postulating them merely to make the sum vanish.

## Verification and limitations

```text
python -m unittest verification.abaee_sphere_program_recovery_test -v
```

Ten standard-library checks cover the qubit affine-dimension obstruction, its integer inequality, the overlap used in the sharp-measurement argument, a finite-family projector processor, spherical-cap integration and error, exact matched records for a finite coherent reference superposition, and the distinction between global reversal and reduced dephasing. Continuous-sphere results and the general programming proof are analytical; numerical spot checks are not a proof of all of Abaee's results, nor a run of the supplied supplementary verifier.
