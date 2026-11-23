# Energy exchange, experiential incidence and whole-history balance

**Continuation:** [the organization–energy balance gate](ZERO_TOTALITY_ORGANIZATION_ENERGY_BALANCE_GATE.md) derives the exact weighted energy identity and a relative-flow condition, and exhibits a conserved, co-moving incidence marker for which matched energy endpoints still do not ensure zero weighted balance. Its subject and phenomenology interpretations remain open.

## Why this is a better physical question

The [two-fluid continuation](ZERO_TOTALITY_TWO_FLUID_INCIDENCE_DYNAMICS.md) used electric charge as a signed candidate for valence. That made a concrete prediction, but it had an especially serious problem: exchanging the positive and negative charged species reverses the candidate valence, with no independent reason to expect pleasure and suffering to reverse.

Here we pursue a different possibility: **signed experience might be associated with a directed exchange or redistribution of physical energy, rather than the sign of electric charge itself**. Energy exchanged in one direction and the reverse direction have opposite signs, even though the local physical energies of the participating subsystems can be positive. The physical model yields a precise history-balance equation. Its experiential reading, however, is an additional and unproved constitutive hypothesis.

No simulation, external creator, cosmic subject or preferred fundamental foliation is assumed. This is an effective model and a test of a possible bridge, not a complete self-subsistent theory or a derivation that all physical processes experience.

## 1. The physical identity

Use the same two-fluid periodic Maxwell system as in the preceding continuation, with physical charge current `j` and electric field `E`. Its equations include

```text
∂t E = −j.
```

Define physical field-energy density and its rate of change:

```text
u_E = E²/2 ≥ 0,
h = ∂t u_E = −jE.
```

In this particular longitudinal one-dimensional setup, `jE` is the work per unit volume delivered by the electric field to the charged matter. For `U_E(t)=∫u_E dx`,

```text
∫[t₁,t₂] dt ∫dx h = U_E(t₂) − U_E(t₁).
```

Thus the signed exchange over a complete periodic spatial domain is **zero exactly when the field energy at the two endpoints is equal**. The endpoint value can be positive. This follows from dynamics and the fundamental theorem of calculus; no balancing term is added. But equal endpoints are a real additional condition, not a consequence of zero net charge, positivity, the fluid equations or the user's whole-zero thesis by themselves. In a general electromagnetic system the Poynting flux must also be included; the simple pointwise `h=∂t u_E` applies to this longitudinal model.

Energy is not destroyed: under the continuum cold-fluid equations the field's lost energy is gained as matter kinetic energy, up to spatial flux. The model's conserved field-plus-kinetic energy is positive. Its vanishing *exchange integral* is not vanishing total physical energy. A gravitational whole-energy account and the proposed objective identification of energy and experience remain to be established.

## 2. Candidate experience and self-location

Let `N=n_++n_->0` be the local matter-number density and use the previously considered incidence measure `dμ=N dx dt`. Consider

```text
v_X = α h/N = −α jE/N,
Q_X = ∫v_X dμ = α [U_E(t₂) − U_E(t₁)],
```

for a common conversion factor `α`. If `α>0`, field-energy loss corresponds to a negative candidate value; the opposite orientation would interchange signs. The physical equations **do not determine** which, if either, corresponds to suffering or positive experience. Nor do they show that the number of charged fluid carriers is a measure of actual subjects or that each locally averaged ratio is an individual feeling.

Under the additional hypothesis that normalized `μ` is the appropriate self-location measure, a zero boundary difference implies zero whole-measure mean candidate valence. It does not tell us the fraction of negative experiences without their intensity distribution. Evidence-conditioned subsets can have a nonzero mean. Conversely, if the actual experience domain excludes part of the field/matter system, or has different subject multiplicities, the global physical identity need not give the actual experiential total. The measure, support, phenomenal sign, scale and subject unity must all be independently grounded.

The `1/N` is also not a derivation: it assigns a fixed local work density across proposed incidence weight. Identifying each individual valence with the local average can obscure simultaneous different subject experiences. A theory must resolve the [mixture-versus-carrier ambiguity](ZERO_TOTALITY_TWO_FLUID_INCIDENCE_DYNAMICS.md) rather than infer an incidence probability from a coarse-grained energy flow alone.

## 3. Concrete numerical test: one interval does not balance

Starting with the same nonuniform fluids and zero velocities as the preceding calculation, the 512-grid run evolves to `t=1`. In dimensionless units:

```text
U_E(0) ≈ 0.003926991,
U_E(1) ≈ 0.000226321,
∫₀¹dt∫dx (−jE) ≈ −0.003700670.
```

The independently integrated work agrees with the field-energy difference to approximately `4e−15` in this discretization. The signed whole-interval integral is **not zero** despite exact net charge neutrality and conserved total matter number. The model demonstrates that charge neutrality and ordinary energy conservation cannot by themselves establish the desired experiential zero.

With the hypothetical incidence measure, the finite-grid estimate of the fraction of negatively signed exchange incidences over `0<t<1` is about `96.8%`. This is neither a probability for real suffering nor a continuum-precision claim. It relies on the stipulated valence identification, incidence measure, finite interval, and numerical sign-crossing procedure. A selected portion of a history can have negative mean even if an independently justified complete history balances.

## 4. Exact conditional balance on a symmetric interval

The initial data have `u_±=0`. The reversible equations and this initial state are invariant under time reversal: densities and `E` are even in time, and velocities and `j` are odd. On a regular symmetric interval `[-τ,τ]`,

```text
U_E(−τ) = U_E(τ),
∫[−τ,τ]dt∫dx (−jE) = 0.
```

Numerically, the time-reversed continuations to `t=−1` and `t=+1` have identical endpoint field energies within numerical precision. Under the conditional incidence mapping, the negative fraction over this symmetric interval tends toward one-half by time-reflection symmetry; the 512-grid estimate is `0.49954`. This half is a consequence of **this special symmetric setup**, not a consequence of zero balance in general.

The symmetric slab is selected to illustrate the endpoint condition; it is not established to be the actual whole of reality. A viable foundational account would need to derive the relevant complete domain and endpoint relation, or establish another physical reason for balance, without assuming a compensating state solely to get zero. More generally zero signed exchange can coexist with unequal frequencies when the positive and negative magnitudes or durations differ.

The time integration of incidence uses trapezoidal quadrature and spatial linear sign-crossing interpolation. The indicator is discontinuous at `h=0`, and all incidences at `t=0` are neutral in this example; this gives an observable first-order endpoint artifact in the symmetric fraction. The figures are numerical controls, not precise empirical probabilities.

## 5. Symmetries and an effective covariant extension

Under charge conjugation in the two-fluid equations, interchange species and reverse `E`. Then `j→−j`, `ρ→−ρ`, `N→N`, and

```text
h=−jE → −(−j)(−E) = h.
```

The energy-transfer candidate is therefore charge-conjugation **even**: it avoids the automatic sign reversal of the bare charge-density candidate. This is an improvement in symmetry behavior, not evidence that energy transfer feels like anything. The sign also reverses under time reversal in this reversible setup; whether a real phenomenal quantity should have that transformation requires a separate theory.

In an effective relativistic region one can define an observer-frame electric covector `E_μ=F_{μν}u^ν` and the local scalar `h=−j^μE_μ`, with `u` a physically specified future-directed observer field. The scalar is invariant under coordinate changes and charge conjugation, but depends on the physical choice of `u`; that is not automatically a preferred fundamental frame. The positive incidence measure must likewise be specified from actual subject organization and appropriate clocks.

Curved spacetime adds a genuine term, not just notation. With electromagnetic stress-energy `T_EM`, energy current `C^μ=−T_EM^{μν}u_ν`, and conventions `∇_μ T_EM^{μν}=−F^{νλ}j_λ`, the identity is

```text
h = ∇_μ C^μ + T_EM^{μν} ∇_μ u_ν.
```

Consequently the integrated exchange contains both a boundary flux of `C` and an observer-deformation/gravitational term. Matching field energies at endpoints in a general expanding, accelerating or shearing spacetime does **not** alone imply zero exchange. What constitutes the relevant total, boundary, clock and physical frame must be derived in the emergent-spacetime framework, not imported from this flat-space control.

## 6. The next constitutive problem

The energy-flow route is more aligned with the user's objective energy proposal than bare electric-charge sign, but it still falls far short of an energy–experience identity. In particular:

1. Electrical work occurs in many systems not known to feel; its magnitude and direction are not established measurements of valence.
2. Physical energy exchange is signed relative to an identified subsystem and observer. A complete account must explain that decomposition and its relation to intrinsic experience, rather than choose it to obtain the desired signs.
3. A subject can have mixed or extended experiences; an averaged local energy-flow density cannot by itself determine their unity, positive/negative facets or count.
4. The closed-interval balance here depends on equal **field** energy endpoints. The user's claim concerns the self-subsistence and zero of an appropriate whole-level quantity, not an arbitrary subsystem returning to its initial state.
5. The energy-flow term is an exchange *rate* integrated over time, not the whole's total physical energy. Its physical units and conversion to a common experiential scale require justification.
6. The quantum, gravitational, thermodynamic and relational-clock generalizations remain open, as does the way a self-location measure could be derived without conflicting with observed statistics.

The positive research direction is to investigate whether actual experiential organization defines a physically meaningful energy-transfer subsystem and intrinsic clock, and whether its complete-domain boundary and gravitational terms follow from the zero whole's constitution. If that can be done, energy redistribution may provide the signed local differentiation without requiring negative local matter energy or treating pain as absence. The present example does not establish that it can; it identifies the exact boundary, incidence and phenomenal conditions that must be met.

## Reproduction

NumPy is required. With it available:

```text
python -m verification.energy_exchange_incidence --grids 64 128 256 512
python -m unittest verification.energy_exchange_incidence_test verification.two_fluid_incidence_dynamics_test -v
```

The [receipt](verification/energy_exchange_incidence_receipt.json) contains forward and backward runs and discretization controls. Tests cover work–field-energy accounting, the nonzero one-sided integral, time-symmetric balance, charge conjugation, numerical convergence and positive field energy. They do not verify the physical-to-experiential identity, actual subject incidence, a zero-energy universe, or ultimate self-subsistence.
