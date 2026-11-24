# Can time arise in a timeless whole? An interacting clock result

## Answer and constructive proposal

Yes, a **timeless constrained whole can have genuine internal change** in a mathematically precise model: its physical state solves a constraint, while correlations between internal variables depend on the reading of a physical clock. We have constructed this for a positive-frequency, homogeneous FLRW sector coupled to the sphere–record logical system and an interacting pointer. Neither an external time nor a fundamental preferred foliation is introduced. This is a solution to the *frozen-dynamics aspect within that model*, not a solution of the entire problem of time in quantum gravity or a derivation of time, subjects and all physics from zero.

The next gap was concrete: the detector interaction produces bound states, and the free geometry-clock switch cannot simply be reused. Here we define an exact finite-region geometry-reading **instrument on the interacting physical Hilbert space**, including its bound states, and prove that this reading necessarily transfers some amplitude out of an individual bound eigenstate. A reciprocal preparation transfers amplitude back. This shows precisely how a stationary sector can support change *after an intervention*, and how clock readout can mix sectors that asymptotic clock constructions treat separately. The calculation does not supply an autonomous local detector or an instantaneous geometry-clock switch.

Previous work: [interacting spectrum and asymptotic clock](ZERO_SPHERE_INTERACTING_CLOCK_SPECTRUM_AND_BOUND_STATES.md), [autonomous detector](ZERO_SPHERE_AUTONOMOUS_CONSTRAINED_DETECTOR.md), [domain/sector distinction](ZERO_DOMAIN_SECTOR_CLOCK_RECOVERABILITY.md). Standard-library checks: [verification/zero_interacting_clock_bound_transition_test.py](verification/zero_interacting_clock_bound_transition_test.py).

## 1. A physical finite-region clock instrument

Use the previously specified physical Hilbert space

```text
H_phys = L²((-7,−6), dp) ⊗ C²_h ⊗ C²_d,
Θ_(h,d) = p²/6 − 2h − 2λ d E,      Ω_(h,d) = √Θ_(h,d),
h=0,1;  d=±1;  λ=0.4;            U(φ) = exp(+i Ω φ).
```

E is the Gaussian-smeared α=ln(a) window, compressed to the momentum band, with window half-width 2 and width σ=1. Its kernel in p-space is

```text
E(p,q) = exp[−(p−q)²/2] sin[2(p−q)]/[π(p−q)],
E(p,p) = 2/π;        0 ≤ E ≤ I.
```

It acts as the identity on the h and d registers. The square root Ω exists because Θ≥3.2 in this selected sector. These are the earlier interaction, geometry, encoding and physical inner product; none is derived from the zero point. Scalar φ is an internal reading, not external time.

At a specified scalar reading φ₀ define the **two-outcome instrument**

```text
K_yes = E,             K_no = √(I−E²),
K_yes† K_yes + K_no† K_no = I.
```

It is a legitimate completely positive trace-preserving operation when its outcome is ignored, on the full interacting physical space including bound states. Its yes *effect is E²*, not E. In particular it is a filtered window reading, not the Lüders instrument for E and not the only possible readout. In the reduced representation, the unnormalized post-yes data are `E χ(φ₀)`; subsequent evolution is `U(φ−φ₀)Eχ(φ₀)` and remains on the selected constraint branch. It can be transported as an operator and instrument to any unitarily equivalent physical representation. That is representation independence for the **same operation**, not proof that another natural clock reading is equivalent or that an interacting instantaneous α clock has been constructed.

Repeated-readout probabilities are well defined. With the first reading at φ₀=0, the second at φ=t, and initial normalized data ψ,

```text
Pr(yes₀,yes_t) = || E U(t) E ψ ||².
```

This formula includes the apparatus backaction represented by the chosen Kraus operator. It requires no distribution uniform in scalar φ. It is not the probability of a first arrival, nor is it a standalone experiment without a specified preparation and readout mechanism. The operation is a physical-Hilbert-space instrument, not yet a local, autonomous apparatus or an operator shown to commute strongly with the full off-shell constraint.

## 2. Exact bound-to-complement transition

Work in h=0, d=+1 and write `T(p)=p²/6`, so `Θ=T−0.8E`. The previous report proves there is a normalized eigenvector b of Θ below the free band's bottom 6. Let `P=|b⟩⟨b|` and `Q=I−P`. Since E is self-adjoint,

```text
Pr(yes and Q after | initial b) = ||Q E b||²
                               = ⟨b|E²|b⟩ − |⟨b|E|b⟩|².
```

**This quantity is strictly positive in the continuum model.** Suppose instead `Q E b=0`. Then `E b=c b` for some real c. From `(T−0.8E)b=θ_b b` it follows that `T b=(θ_b+0.8c)b`. But multiplication by p²/6 has no nonzero L² eigenvectors on the band: each level set has measure zero. Contradiction. Thus the selected finite-region instrument necessarily creates a component orthogonal to b when it reports yes. This is an analytic statement, not a conclusion drawn solely from matrix diagonalization.

The reverse transition is equally explicit. Define

```text
χ = Q E b / ||Q E b||.
```

It is a normalized physical state orthogonal to b, and the joint probability of yes and subsequent projection onto b is

```text
|⟨b|E|χ⟩|² = ||Q E b||² > 0.
```

This `Q` is the complement of **one** bound vector. It may include other bound or singular-continuous states as well as scattering states. Therefore the proof is **not** a proof of transition specifically to or from the absolutely continuous scattering subspace. The latter needs a separate spectral analysis.

## 3. Numerical check, not a continuum scattering calculation

A Nyström midpoint discretization and symmetric Jacobi eigensolver give the following for the lowest d=+, h=0 eigenvector; the continuum b exists independently of this discretization:

| Band samples N | `Pr(yes)` | `Pr(yes and b)` | `Pr(yes and Q)` |
|---:|---:|---:|---:|
| 40  | 0.0611431 | 0.0182209 | 0.0429221 |
| 80  | 0.0571100 | 0.0159450 | 0.0411650 |
| 160 | 0.0555968 | 0.0151251 | 0.0404718 |

At N=80, about 0.7208 of the *yes-conditioned* output weight is in Q. Finite-N Q consists of other discrete eigenvectors; those interior grid modes are not automatically continuum bound or scattering states. The trend is a numerical consistency check, not a rigorously estimated continuum error.

A bound eigenstate alone has stationary E² reading probabilities under scalar evolution. But after a yes operation it contains different spectral components and subsequent readings can change. For the same N=80 example, the joint probabilities `Pr(yes₀,yes_t)` are approximately 0.0158877, 0.00109738 and 0.00074862 at t=0, 40 and 100. These describe two specified interventions, not spontaneous passage in the initial eigenstate. Direct p-basis evaluation agrees with evaluation in the full interacting eigenbasis when the instrument is transported, including all off-diagonal matrix elements.

## 4. What this says about the whole and experienced time

This supports a constructive picture: a whole can be described without an external clock, while physical substructures register correlations and alter one another. Stationarity of a particular state is not the absence of all relational descriptions; nor does registering an event require every sector to possess a single global clock. In this specific model an eigenstate rules out a normalized real-valued POVM covariant under scalar evolution on the whole interacting sector, as proved in the preceding report. Our finite-region instrument is **not** such a covariant global clock and does not evade that theorem: it refers to a chosen scalar reading and an operation there.

The distinction between the surface and room still matters: the traveler is the player, not a surface inhabitant. The surface-restricted traveler's position remains A during the room journey and becomes B on return; the richer trajectory is not automatically experienced by a confined inhabitant. Nothing in this instrument establishes an inhabitant, subjective passage, or a communication channel across domains.

The zero-point/sphere proposal goes beyond this model: it asks how zero's own constitution necessitates physical differentiation and actual subjectivity without unexplained residue. Constraint-zero dynamics with nonzero internal changes is a useful constructive example, but neither the constraint nor the selected action and state establish objective whole energy or a signed experiential total. Local suffering remains real; no experiential cancellation is inferred from the mathematical transition.

## 5. The next decisive step

Construct a **finite-interaction-region relational geometry-clock instrument**, not just a geometry-window operation conditioned on a scalar clock. It must specify what “the scalar and pointer read X when geometry reads α” means, treat multiple crossings and no-crossing outcomes, include bound and scattering components, and compare the *same instrument* in alternative representations. Prove when that construction exists and how its probabilities change under a different clock. The present transition proof says why splitting the spectrum first and neglecting measurement-induced mixing would be unjustified.

Beyond this model, a solution would also need consistent inhomogeneous constraints or an emergent equivalent; recovery of local causal structure, clock rates and empirical relativity; a justified physical inner product and treatment of clock domains; an account of records and outcomes; and, for the user's stronger programme, a derivation of the structure and experiential incidence from zero. These are connected obligations, not assertions that a preferred external time must be restored. Established relational approaches provide essential prior art, e.g. [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580) on conditional states and Dirac observables. The present bound-transition observation is conditional on our particular operator and instrument; no general novelty claim is made.
