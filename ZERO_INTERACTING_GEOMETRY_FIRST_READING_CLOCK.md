# Interacting geometry clock: first reading, records and no reading

## What is new here

Relational/emergent time is already the idea that physical changes are described relative to other physical changes rather than a fundamental external time. That premise is not a new solution. The task here is to make a **specific clock comparison** work in the interacting constrained model, without silently discarding missed readings, repeated readings, measurement disturbance or the interacting bound states.

We construct a finite, operational **first-geometry-reading instrument**. It yields the probability that a finite-resolution geometry window is first registered at each chosen scalar-clock checkpoint, jointly with the detector-pointer value at that checkpoint, plus a no-reading outcome. We also construct all repeated-reading histories. The instrument is exact on the stated physical Hilbert space; examples use converging finite momentum grids. It makes progress on the concrete question “what does the detector read when the geometry window is first registered?” but it is **not** an instantaneous α-clock deparametrization, an autonomously triggered measurement, or a full solution to the multiple-choice problem.

Code: [verification/zero_interacting_relational_first_reading_test.py](verification/zero_interacting_relational_first_reading_test.py). Background and the analytic bound-state transition proof: [interacting clock transitions](ZERO_INTERACTING_CLOCK_TRANSITIONS_AND_PROBLEM_OF_TIME.md).

## 1. One interacting constrained system and a defined protocol

Use the previously chosen positive-frequency physical sector

```text
H_phys = L²((-7,−6),dp) ⊗ C²_h ⊗ C²_d,
Θ_(h,d)=p²/6−2h−0.8d E,     Ω_(h,d)=√Θ_(h,d),
U(φ)=exp(i Ω φ),              h=0,1, d=±1.
```

h is the sphere–record logical index, d the pointer σ_y eigenvalue, and E the compressed Gaussian-smeared `α=ln(a)` window of half-width 2 and smearing 1, centered on α=0. Its kernel and the operator bounds are specified in the [preceding note](ZERO_INTERACTING_CLOCK_TRANSITIONS_AND_PROBLEM_OF_TIME.md). Both logical levels and both pointer channels are retained. The chosen α window is an interval with finite resolution, not a sharp surface or a statement that a crossing occurred.

At scalar values `φ₁=30, φ₂=40, φ₃=50`, apply the instrument

```text
Y=E,      N=√(I−E²),      Y†Y+N†N=I.
```

Yes has effect E²; no has effect I−E². These are **specified measurement operations**, not an asserted unique or passive geometry observation. Let `U_k=U(φ_k−φ_(k−1))`, with φ₀=0. The unnormalized first-yes output operators and no-yes operator, in the scalar representation, are

```text
B₁ = Y U₁,
B₂ = Y U₂ N U₁,
B₃ = Y U₃ N U₂ N U₁,
B⊥ = N U₃ N U₂ N U₁.
```

For pointer projectors `P_z` onto z=0,1, define the physical effects

```text
F_(k,z) = B_k† P_z B_k,      F⊥ = B⊥† B⊥,
Pr(k,z) = Tr(ρ F_(k,z)),     Pr(⊥) = Tr(ρ F⊥).
```

Each effect is positive, and telescoping completeness of N,Y and unitarity gives the **exact identity**

```text
Σ_(k=1..3) Σ_(z=0,1) F_(k,z) + F⊥ = I.
```

Thus these effects define a normalized joint POVM for any state on the declared sector, including bound states and coherent superpositions with their complements. The output instrument is `ρ → P_z B_k ρ B_k† P_z` for each `(k,z)` and `ρ → B⊥ρB⊥†` for no yes. Pointer z is measured at the first yes; the protocol then stops. The outcome ⊥ means **no yes at these three attempts**, not an eternal failure to cross.

Alternatively continue the yes/no operation through all three checkpoints. The eight ordered outcome strings form a normalized history instrument; coarse-graining strings with their first 1 at k reproduces `Pr(k)`. Repeated yeses are allowed and are not automatically multiple geometrical crossings—an extended window and measurement backaction can cause repeated registrations.

There is a unitary measurement dilation: with a fresh two-level memory initialized to 0, and in the memory basis,

```text
W_mem = [[N, −Y], [Y, N]].
```

It is unitary because N and Y commute and N²+Y²=I; its two memory amplitudes are Nψ and Yψ. Three memories and the intermediate interacting U's give a reversible circuit that records the history. This is a **formal circuit on the physical sector**; its checkpoint timing and memory couplings are externally specified in the protocol. We have not constructed a local clock-controlled Hamiltonian, shown a spatially local interaction, derived irreversible records, or solved a total constraint including this memory apparatus.

## 2. A concrete comparison with the prior packet and detector

Take the earlier normalized packet `f(p)=√30 (p+7)(−6−p)` multiplied by `exp(15 i p)`, the logical state `(|0⟩+i|1⟩)/√2`, and the detector pointer initially in z=0. This is the same incident-packet preparation as the prior interacting-pointer calculation. At N=80 momentum samples:

| First yes at scalar reading | Joint `Pr(first yes)` | `Pr(pointer z=1 | first yes)` |
|---:|---:|---:|
| 30 | 0.1778760 | 0.35956 |
| 40 | 0.1033579 | 0.46657 |
| 50 | 0.0149717 | 0.57235 |
| No yes at these three attempts | 0.7037944 | not queried |

The four first-reading/no-reading probabilities sum to 1. If attempts continue after a yes, the probability of **two or more** yeses is approximately 0.0201346. At N=160 the first-yes probabilities are approximately 0.1778585, 0.1033548 and 0.0149755, with no yes 0.7038112 and two-or-more yeses 0.0201300. These are checks of grid convergence, not rigorously bounded errors or physical forecasts. The rather large no-yes probability is a property of this particular finite set of filtered attempts, not a statement that the packet never moves through the window.

A useful backaction control: measuring only at φ=40 gives yes probability 0.1159256 at N=80. In the *first-yes protocol* the joint probability for no at 30 and yes at 40 is 0.1033579. The difference is not a disagreement between clocks: these are different experimental questions, and the earlier no-result operation changes the state. Normalizing by the probability of no at 30 would give a different conditional probability again.

## 3. Bound-sector coherence is retained

The existing proof gives at least one normalizable bound eigenstate in the interacting d=+ channel. The present formulas act on the **entire** Hilbert space and do not apply a bound/scattering projection before a reading. For the N=80 d=+, h=0 grid, write the incident packet `f=P_b f+Q_b f` using the numerical lowest eigenvector. At φ=40, the single-yes probability is approximately 0.1629901. If one instead dephases between the b and Q_b components before evolution, the sum of their separate yes probabilities is 0.1646813. Their difference is an explicit interference term that the full operation retains.

This check refers to one pointer channel rather than the full pointer-prepared state in the table; its probabilities therefore should not be added to the table. Q_b is the complement of a single bound vector and cannot automatically be called the continuum scattering subspace. Neither the finite grid nor this comparison proves a bound-to-absolutely-continuous transition.

## 4. Two representations, and what has *not* been switched

We evaluate every first-reading and repeated-history probability twice:

1. in the original momentum p representation;
2. in the interacting spectral representation, using the eigenbasis of each pointer channel for the finite-grid check.

The effects, updates and pointer projectors must all be transported. In particular, the two d channels have different eigenbases: the pointer z operator connects them using their **cross-Gram matrix**, not by identifying equal eigenvalue indices. In the no-yes branch at N=80, the correct *joint* probability for no yes and final pointer z=1 is about 0.6607054. Naively subtracting equal coefficients in the two unrelated eigenbases gives about 0.3017477 in one arbitrary eigenvector phase convention. The naive number itself changes when eigenvector signs change and has no invariant significance. The proper p- and spectral-representation results agree across all checked outcomes.

This is a valid **representation change within the same scalar-clock description**, not a switch from scalar time to geometry time. It proves neither the equivalence of independently quantized clock theories nor a finite-interaction-region α-clock reduction. Constructing the latter remains the important unresolved step: it must reproduce the same concrete joint effects on whatever common domain exists, and account for failures of geometry to furnish a good clock. The protocol above can serve as a target for such a comparison; it does not supply the answer in advance.

The broad first-detection method is established prior art, including repeated measurements with non-detection backaction ([Dhar et al.](https://arxiv.org/abs/1312.5923)) and first-click memory schemes in relational-time settings ([arXiv:2603.28623](https://arxiv.org/abs/2603.28623)). Physical-clock perspective changes and their domain limitations have also been studied by [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580). Our contribution here is the explicitly specified instrument and calculation **for this existing interacting sphere–record FLRW sector**, not invention of the first-detection or relational-time framework.

## 5. Consequence and next test

The interacting example now gives an explicit relational *operational question*, with no-reading and repeated-reading alternatives and the measurement's disturbance included. The idealized scalar readings are still the checkpoints of the deparametrized description; they are not measured by a finite-resolution autonomous scalar apparatus in this protocol. The controlled memory operations are scheduled rather than dynamically triggered. The model is homogeneous and band-projected, not a proof of refoliation invariance or of GR's local constraint algebra.

The decisive next construction is an independently specified **geometry-clock perspective in the interaction region**: define its physical inner product, instrument, overlap domain and failure/multiple-reading outcomes; show whether it reproduces the effects `F_(k,z)` on the common domain, rather than assuming a unitary map. It must confront the previously proved global covariant-clock obstruction and the window's nonlocality. If it cannot reproduce these effects, determine whether the cause is unequal experimental protocols, incompatible domains, or genuinely inequivalent quantizations.

The point–sphere programme demands more than the existence of such relational descriptions: it asks how zero's own constitution determines internal differentiation, subjectivity and their relationship. This calculation assumes the constraint, state, physical measure, measurements and logical encoding. It does not derive objective whole energy, actual experience, felt time, or experiential cancellation; local suffering is not erased by a global zero. No real subject, observer outcome or lived record follows merely from a pointer correlation.

## Reproduce

```sh
python -m unittest verification.zero_interacting_relational_first_reading_test -v
```

The code checks completeness, all eight histories, pointer-at-first-yes, distinct no-hit backaction, bound/complement interference, a finite memory-unitary dilation, agreement between p and interacting eigenbases including pointer transport, and N=40/80 refinement. Its grid computations do not prove continuum spectral type, autonomous realization, or a switch of physical clocks.
