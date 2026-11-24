# An autonomous detector inside the sphere–cosmology constraint

**Continuation:** [the interacting clock spectrum and bound states](ZERO_SPHERE_INTERACTING_CLOCK_SPECTRUM_AND_BOUND_STATES.md) proves sector-specific bound modes, constructs an asymptotic scattering representation, and tests full pointer transport.

## The new construction

The preceding [finite-clock-instrument result](ZERO_SPHERE_QUANTUM_COSMOLOGY_FINITE_CLOCK_INSTRUMENTS.md) specified operations on a physical Hilbert space but did not derive a detector interaction. Here a two-state detector is added **to the same minisuperspace constraint as the geometry, scalar clock and encoded sphere–record qubit**. The detector's pointer changes under a fixed, scalar-independent coupling as a geometry wavepacket passes an interaction region; there is no externally scheduled switching in the model.

For the selected wavepacket and couplings, the numerical detector-one probability rises from zero to approximately **0.9589**, whereas a control packet initially on the opposite side and mainly moving away produces approximately **0.00076** at the same scalar reading. These are model-dependent discrimination probabilities for two preparations, not a claim that quantum paths are individually definite or that every other preparation is equally well detected. A second pointer readout, conditioned on the pointer being 1 at scalar reading 80, finds a flip probability of about `4×10⁻⁵` at reading 120 in this model. The first readout is a specified ideal projection; an independent observer or readout device is not simulated.

The interaction modifies the geometry momentum and enters the constraint's balance. A conserved scalar momentum and a positive-frequency physical inner product are explicit. The detector is autonomous **only in this limited sense**: it is a finite degree of freedom governed by a time-independent constrained Hamiltonian, rather than a POVM inserted by hand at a scheduled time. The band-projected interaction is nonlocal in geometry momentum, the spin pointer has no realistic microscopic realization, and neither an irreversible memory nor a local gravitational detector has been obtained. The total constraint is not automatically an objective total energy of the whole.

All formulas are defined in the continuous band model; numerical checks discretize the momentum band and approximate the square-root propagator. The 14 standard-library tests are in [verification/zero_sphere_autonomous_detector_constraint_test.py](verification/zero_sphere_autonomous_detector_constraint_test.py).

## 1. A single constraint with the pointer included

Use the flat, compact FLRW model, scalar φ, logarithmic scale factor α and encoded sphere–record clock `h=0,1` from the [normalizable cosmology](ZERO_SPHERE_NORMALIZABLE_QUANTUM_COSMOLOGY_CLOCK.md). Set `κ=ℏ=1`, `p=p_α`, restrict to `−7<p<−6`, and add a pointer D with basis `|0_z⟩,|1_z⟩`. Its bare Hamiltonian is chosen to be zero. Let E be the previous Gaussian-smeared α-window effect, with window `[-2,2]` and resolution `σ=1`:

```text
E(p,q) = exp[−(p−q)²/2] sin[2(p−q)] / [π(p−q)],
E(p,p) = 2/π,               0 ≤ E ≤ I.
```

This is the compression of multiplication by a bounded window-response function in α to the selected momentum band. Its parameter values, the band, and the two-level pointer are assumptions. In an α representation before compression, the response is localized near the chosen window; spectral projection makes it nonlocal on the unrestricted α Hilbert space. It is **not** a detector localized in a region of three-dimensional spacetime.

Introduce the rescaled constraint operator

```text
C̃ = −p²/12 + p_φ²/2 + h + λ E ⊗ σ_y^D = 0,
λ = 0.4.
```

The complete tensor product is geometry ⊗ logical sphere–record sector ⊗ pointer; identity factors are suppressed. This is a new, explicitly prescribed interaction. Before the usual positive `a³` rescaling, the added term is `λ E σ_y^D/a³` in the constraint. The added coupling may have either sign; it is not asserted to be a positive local energy density. The detector is idealized and degenerate, so one cannot infer its material cost from its bare Hamiltonian.

Define

```text
Θ = p²/6 − 2h − 2λ E ⊗ σ_y^D,       C̃ = (p_φ²−Θ)/2.
```

The operators p², h and E are bounded self-adjoint on the selected band. Since `0≤E≤I` and `h≤1`,

```text
3.2 = 6−2−2|λ| ≤ Θ ≤ 49/6+2|λ| < ∞.
```

Consequently `Ω=√Θ` is a well-defined bounded positive self-adjoint operator for the declared sector. This remains true although E and p² **do not commute**. The square root is taken of the full interacting operator, not of each term separately.

Choose the `p_φ>0` branch and physical solution

```text
χ(φ) = exp(+i Ω φ) χ₀,
Ψ(φ) = (2Ω)^(−1/2) exp(+i Ω φ) χ₀.
```

The second expression is the generalized covariant solution, with the positive-branch Klein–Gordon product normalized so its norm equals `||χ₀||²`. It obeys `(p̂_φ²−Θ)Ψ=0` and `p̂_φΨ=ΩΨ`. The physical state is normalizable in its specified physical inner product, not as a uniform wavefunction over the entire real φ axis. Because the interaction is φ-independent, `p_φ` is conserved. The earlier full-gravity, other-branch and physical-measure qualifications still apply.

## 2. The detector's Kraus operators emerge from its unitary dynamics

In the pointer `σ_y` eigenbasis `d=±1`, the squared root decomposes into

```text
Θ_(h,d) = p²/6 − 2h − 2λ d E,
U_(h,d)(φ) = exp[iφ√Θ_(h,d)].
```

Initialize the pointer in `|0_z⟩`. At a selected scalar reading its components in the z basis are generated by the **actual coupled evolution**:

```text
M_0,h(φ) = [U_(h,+)(φ)+U_(h,−)(φ)]/2,
M_1,h(φ) = i[U_(h,+)(φ)−U_(h,−)(φ)]/2.
```

As operators on geometry plus the logical clock, the `M_r` are block diagonal in h. For every physical input,

```text
M_0†M_0 + M_1†M_1 = I,
Pr(r at φ) = ||M_r(φ) χ_geometry,logical||².
```

The identity follows from unitarity of the two `U_(h,d)`, even though they need not commute. Reading D is a proposed physical record observable; its probabilities are calculated from the coupled history. The positive-root constraint is obeyed by the history before and after a specified pointer projection because each reduced state defines a solution of this same branch. The projection is an idealized further operation; a second autonomous device to read the pointer has not been modeled.

Importantly, the resulting pointer effect `M_1†M_1` is generally **not** the E² effect of the prior abstract instrument. E is used as an interaction profile here; that choice does not make it the actual detector POVM. For example, at φ=0 the detector has probability zero to be 1 for every initial geometry state, while E² has nonzero probability on a packet centered in the interaction region. A proper comparison must derive and calibrate the actual effect at the relevant reading, not identify it by name.

## 3. Finite detection and a control

Use the earlier normalized band packet `f(p)=√30(p+7)(−6−p)` and logical state `( |0⟩+i|1⟩ )/√2`. Translate the initial geometry wavefunction by `α₀=−15`, by multiplying f(p) by `e^(−ipα₀)`. In the free branch its mean geometry coordinate moves toward the interaction window as φ increases. This is a quantum wavepacket, not a sharply defined classical trajectory.

With N=80 midpoint samples and the specified square-root propagation, we obtain:

| Scalar reading φ | `Pr(D=1)` | `⟨E⟩` |
|---:|---:|---:|
| 0 | 0.000000 | 0.000768 |
| 40 | 0.779419 | 0.236828 |
| 80 | 0.958826 | 0.000078 |
| 100 | 0.958879 | 0.000062 |
| 120 | 0.958883 | 0.000055 |

The pointer has largely flipped after the packet has largely left the interaction region. In an otherwise identical preparation centered at `α₀=+15`, whose free mean moves away from the window, the pointer-one probability at φ=100 is approximately `0.000761`. The packets have tails, and the interacting dynamics is quantum: these numbers calibrate **these two preparations**, not an error rate for a perfect binary event of crossing versus not crossing.

The zero-coupling control leaves D in `|0⟩` and reproduces the earlier free sphere–cosmology evolution. Reducing λ also reduces the response for this preparation: the N=40 calculation at φ=100 gives pointer-one probabilities about `0.0336` at λ=0.05, `0.1291` at λ=0.1 and `0.4389` at λ=0.2. These are examples, not a universal detector response curve.

For a more meaningful memory check than merely comparing marginals, the test projects D onto `|1_z⟩` at φ=80, then evolves the resulting conditional physical state for 40 more scalar units. It calculates `Pr(D=0 at 120 | D=1 at 80)` as approximately `4.4×10⁻⁵` at N=40 and `3.9×10⁻⁵` at N=80. This shows high **finite-interval repeatability under the specified ideal first readout**, not indefinite stability, irreversible recording, or a record that has actually been experienced. The full unitary evolution is reversible, as the tests verify.

## 4. Backaction and zero balance with the detector present

The pointer interaction changes geometry momentum because `[E,p²]≠0`; the test checks this explicitly. With the incident packet, at N=80 the expectation of the rescaled gravitational term changes from approximately `−3.523810` initially to `−3.519212` at φ=40. At the same reading the interaction term contributes about `−0.004597`; the scalar contribution is approximately `3.023810` and the bare logical contribution is `0.5`. Their sum is zero to numerical accuracy:

```text
−3.519212 + 3.023810 + 0.500000 − 0.004597 ≈ 0.
```

The separate terms are expectations of a chosen rescaled constraint; they are not uniquely localized energies. Scalar momentum is conserved because the interaction has no φ dependence. Pointer populations and geometry distributions can change without violating the model's constraint. No energy conservation statement about a separately omitted laboratory, and no autonomous erasure or thermodynamic cost, is established.

The pointer is correlated with the logical sphere sector as well as geometry. A pointer readout can change the conditional logical state; the joint state and pointer dynamics depend on the h-sector roots. The five-ray model's full confined candidate-subsystem density is nevertheless independent of the logical density matrix: the four polarization controls established in the preceding round are checked again here. Hence both pointer outcomes and their mixture leave that specified confined density and record table unchanged. Pair and triple receiver-state equality is also checked for those polarizations. These results apply to this encoded common interaction and do not amount to general no-signalling in a local gravitational field theory.

This is an exact version of the domain distinction only **within the model**: richer correlations can change while the declared confined state stays fixed. The player is not a chess piece, and the traveler is not a surface inhabitant. The surface-restricted position remains A during the room journey, changing to B on return; the room position traverses the chord. No holding interaction or guaranteed access from the confined realm follows.

## 5. A consequential clock-switch obstruction

The free model's scalar-to-geometry clock map used the pointwise dispersion relation `p_φ=ω_h(p)` and a Jacobian. **That map cannot simply be reused with this detector coupling**: the interacting `Ω=√(p²/6−2h−2λEσ_y)` is not a multiplication operator in p. The test finds a nonzero `[E,p²]` on the packet. Treating the free Jacobian as the interacting transformation would discard the very backaction now being studied.

A genuine interacting clock change would need an appropriate spectral or scattering representation of Ω and physical flux, and a separately justified geometry-clock treatment of the α-dependent interaction. It must transform the pointer, instrument, effects and measure as well as the state, and handle possible failure of α to be a global clock. The existence of the scalar-branch solution does not establish interacting clock equivalence, a self-adjoint global α clock, or refoliation invariance in inhomogeneous gravity. No fundamental preferred foliation is assumed.

## 6. What this does and does not contribute to the whole

A nonzero detector response, changing internal correlations and finite record persistence now coexist in one selected zero-constraint model without an externally scheduled interaction. That is a concrete advance from inserting an instrument after the fact. It shows how an internal scalar can organize measurable relations while the whole history satisfies a constraint, and it gives a precise target for comparing better detector models.

It does not follow that the point–sphere constitution uniquely demands the band, rotor, interaction, initial packet or physical inner product. The constraint's zero is not thereby the proposed objective whole-level energy zero. Neither the pointer nor its conditional correlations establish an actual subject, lived duration, a valence law or experiential cancellation. Local suffering would remain real even if an appropriate signed whole-level quantity were eventually shown to balance. Nor do the computed conditional probabilities select outcomes or prove the thesis that all genuine possibilities are necessary and actual.

The next concrete steps are to (1) construct and verify the *interacting* clock switch and its physical measure; (2) build a spatially local detector with a nondegenerate record and energy/resource accounting, preferably with environmental persistence rather than declaring reversibility to be memory; (3) extend from homogeneity to local constraints and demonstrate consistent slicing-independent observables; and (4) connect physical records to independently tested subject-incidence and valence laws. A derivation from zero must explain the inputs rather than merely label them acceptable residues.

## Reproduction and numerical scope

```sh
python -m unittest verification.zero_sphere_autonomous_detector_constraint_test -v
```

The continuum operator inequalities and instrument completeness are analytic. Tests use midpoint Nyström matrices and Chebyshev propagation, check two polynomial degrees at readings 100 and 120, compare N=40 and N=80, verify the no-coupling limit, conservation/constraint terms, reversible evolution, a control preparation and the two-readout persistence estimate. These checks do not establish convergence for all states, all times or removal of the band restriction, and do not establish full quantum gravity or empirical confirmation.
