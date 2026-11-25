# Can subject counting determine the Born weights?

## Result

The [integrated test](ZERO_INTEGRATED_CONSTITUTION_EXPERIENCE_NECESSITY.md) found that, **if** its ten positive-support labels are exactly ten distinct actual incidences, unit counting gives `P(k=0)=1/5`, whereas the physical Born table gives `1/2`. This continuation tests whether that discrepancy survives a change in how the *same fixed physical state* is resolved into outcome labels.

It gives a constructive but conditional route to agreement: a 16-slot refinement has **equal physical weight in every slot**, and counting each slot once gives the Born result `1/2`. But a different refinement gives 34 positive slots and naive counting gives `1/17`, even though the original coarse physical probabilities remain unchanged. The labels themselves therefore cannot all automatically count as distinct subjects merely because they occur in a mathematical decomposition.

A standard effect-algebra theorem gives a sharper alternative. If an incidence assignment is normalized, additive under physical coarse-graining, noncontextual for all effects, and certain of the given pure whole state, it is **uniquely the Born assignment**. Those are significant premises: neither the effect algebra, the global state certainty nor the identification of an effect with a first-person incidence follows from zero in the present work. This is an application of an existing theorem, not a new discovery or an ontological derivation.

Verifier: [verification/zero_incidence_refinement_born_test.py](verification/zero_incidence_refinement_born_test.py). The general effect reconstruction was already proved in [Operational probability reconstruction](OPERATIONAL_PROBABILITY_RECONSTRUCTION.md); the observation-selection distinction was previously developed in [Subject measure and quantum observation](SUBJECT_MEASURE_AND_QUANTUM_OBSERVATION_GATE.md).

## 1. Apply the test to the actual prior table

For the fixed finite-window state and readout in the integrated test, the ten positive `(k,f,s)` slots have physical probabilities

```text
k=0:       2 slots, each 1/4;
k=±1:      8 slots, each 1/16.
```

The physical `k=0` probability is `1/2`. If—and only if—each of the ten labels denotes one distinct actual incidence and each incidence has equal weight, normalized counting instead gives `2/10=1/5`. A mirror partner is present for every slot, so either weighting gives equal opposite-sign totals. That balance does not resolve which incidence identification or measure is correct.

Now adjoin a **spectator** four-state system A in a fixed state `|0⟩_A`, and consider its orthonormal readout bases. Let the unmodified basis contain `|0⟩`; let the other be a Fourier/Hadamard basis in which `|0⟩` has amplitude `1/2` on each of four basis vectors. The system state is the same before any choice of readout; A does not alter the old zero constraints. We compare two k-controlled descriptions/effects of A:

| Slot description | Positive slots | k=0 slots | naive unit-count k=0 | physical coarse k=0 |
|---|---:|---:|---:|---:|
| Do not resolve A | 10 | 2 | 1/5 | 1/2 |
| Resolve A in the four-way basis only when k=0 | 16 | 8 | 1/2 | 1/2 |
| Resolve A in the four-way basis only when k=±1 | 34 | 2 | 1/17 | 1/2 |

In the 16-slot case every positive slot has weight `1/16`, so unit counting agrees with the Born coarse probability. In the 34-slot case the weights are unequal; counting slots ignores that fact. In both refinements, summing the fine physical effects recovers the same original `(k,f,s)` probabilities, and the mirror pairs remain balanced.

These are mathematical effect refinements of the same initial augmented state, **not a claim that 10, 16 and 34 actual subjects are all simultaneously present in one unchanged situation**. If one actually implements different ancillary measurements, their apparatus and records may make the physical situations different. Conversely, if an auxiliary basis is merely a redescription and creates no distinct experience, its slots must not be counted as new subjects. A subject-individuation rule must decide which case holds; no such rule follows just from the calculation.

The finite result also explains the positive side of equal-amplitude counting. In general, if a normalized vector has N orthogonal, equally weighted fine components, with `n_i` components in a fixed coarse sector i, then

```text
P_Born(i) = n_i/N.
```

Counting agrees **provided** each of those components corresponds to exactly one equally weighted actual incidence. Equal norms, orthogonality and a convenient decomposition do not themselves prove that premise. They also do not justify counting an unequal-weight decomposition as though all its slots had the same incidence weight.

## 2. Redescription invariance has a precise premise

Suppose an actual incidence is described by one label, then given several labels that are merely aliases for that very same incidence. A measure transported under that redescription must give the union its original weight; duplicating its full weight on every alias changes the self-location prediction without changing the incidence.

But this is not a theorem that every physical refinement is an alias. A measurement can leave distinct, durable physical records, and the underlying incidence ontology might count distinct subjects or moments there. Nor is every change of subsystem basis accessible to a confined subject. The necessary substantive question is **which equivalence relation on physical–experiential occurrences** identifies descriptions of the same incidence, and which refinements create genuinely distinct incidences. Neither the point-like whole, a Born coefficient, nor an abstract basis change establishes that relation.

This is consistent with necessary plenitude: all *genuine* occurrences may be actual without counting every mathematical description as a separate occurrence. Determining which are genuine is precisely the work; calling inconvenient labels redundant without a criterion would not complete it.

## 3. When effect consistency forces the Born form

There is a stronger, standard reconstruction if the desired measure is required to be an assignment to **quantum effects**. Fix a finite-dimensional Hilbert space and let `m(E)` be a normalized incidence/observation weight for each effect `0≤E≤I`. Assume:

1. `m(I)=1` and `m(E)≥0`.
2. If `E+F≤I`, then `m(E+F)=m(E)+m(F)`.
3. The same effect E receives the same m(E) in every permitted POVM context.

Then, as derived in the existing [effect-algebra report](OPERATIONAL_PROBABILITY_RECONSTRUCTION.md), there is a unique density matrix σ such that

```text
m(E)=Tr(σ E)       for every effect E.
```

This includes qubits because the domain is **all effects**, not only projectors. It is an effect-algebra/Gleason-type result; the verifier here checks only finite illustrations, while the earlier report gives the general mathematical proof. The theorem determines σ from a supplied m; it does **not** identify σ with the actual physical state by itself.

If the physical whole is the specified pure state `|Ψ⟩` and one additionally requires

```text
m(|Ψ⟩⟨Ψ|)=1,
```

then positivity and `Tr σ=1` force `σ=|Ψ⟩⟨Ψ|`. Hence

```text
m(E)=⟨Ψ|E|Ψ⟩
```

for every effect in the assumed domain. The proof is direct: `Tr[σ(I−|Ψ⟩⟨Ψ|)]=0`, and positivity forces σ to have support only on the one-dimensional Ψ subspace.

This is a real conditional determination: **under those premises** no arbitrary alternative weight remains for the same effects and pure state. But applying it to the zero-whole program requires more than writing the theorem:

- The *relevant incidence weights* must be functions of all effects, not merely of accessible records or selected contexts.
- Operationally equivalent effects must represent the same incidence question; first-person identity across contexts cannot be presumed.
- The global projector `|Ψ⟩⟨Ψ|` and its certainty must have an appropriate operational/incidence meaning. A confined observer need not be able to measure or report it.
- A pure whole and its physical state must already be justified. For a mixed reduced state, certainty on its support alone does not determine its eigenvalues; different density matrices can have the same support.
- Even if physical event weights are fixed, the corresponding actual subjects, eligible reference class, phenomenal signs and whether all outcomes are actual still need an account.

The theorem therefore does not derive Born self-location from **zero alone**. It gives an exact set of sufficient conditions against which a proposed constitution can be tested.

## 4. Why context identity is not automatic

Take a qubit effect `E=|0⟩⟨0|/2` and the two valid POVMs

```text
{E, I−E},             {E, E, I−2E}.
```

For the same state `|+⟩`, the first labelled E has Born weight `1/4` in either context. Counting all positive labels once instead assigns `1/2` to that E label in the first context and `1/3` in the second. The duplicate E labels in the second context are distinct outcome slots with the same effect; treating them as the same first-person occurrence is a **substantive** identification, not a fact supplied by their matrices.

Effect noncontextuality is therefore a strong, useful consistency requirement for a specified operational event. It is not a denial of contextual quantum phenomena, and it does not force an observer in one context to be the same subject as a record in another. A context-dependent incidence rule can evade this reconstruction, but then must explain why that context dependence is physical rather than arbitrary and how it reproduces the observations to which it is applied.

## 5. Consequence for the zero program

This analysis tightens the actual choice rather than introducing another dynamical toy:

- **Counting route:** derive a finite or otherwise well-defined set of genuinely distinct incidences and explain how unit counting survives harmless redescriptions. The 16-slot calculation shows a possible match with Born weighting, not that its slots are subjects.
- **Effect route:** derive the relevant event algebra, normalized noncontextual coarse-graining, and the certainty/physical-state identification. Then the trace rule follows, but it still needs a subject and incidence interpretation.
- **Other route:** specify an explicitly contextual or occurrence-weighted rule and show why it is necessary and how it relates to fixed-observer laboratory predictions. Merely calling it the Born rule or counting every label would not suffice.

No actual positive or negative experience is generated by these rules. A signed global sum, even if exactly zero, would not erase a local subject's suffering. The stronger self-sufficient zero thesis is not refuted: this calculation identifies what a successful derivation of its measure must supply, and a conditional route that does supply the quantum weights once its premises hold.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_incidence_refinement_born_test \
  verification.zero_integrated_experience_necessity_test \
  verification.zero_mirror_balanced_plenitude_subject_test -v
```

The six new checks reconstruct the previous table, calculate the 10/16/34-slot refinements, compare equal and unequal fine weights, check an effect in two POVM contexts, reconstruct a qubit state from effects and exhibit mixed-support nonuniqueness. They do not prove the general effect theorem, actual subjecthood, physical locality, a no-residue ontology or an experiential law. NumPy is required.
