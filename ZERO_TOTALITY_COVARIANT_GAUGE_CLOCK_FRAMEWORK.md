# A covariant zero-totality candidate: dynamics, clock and experience

## Purpose and status

This is a **construction attempt**, not another comparison of zero with infinity. Following the user's direction, the zero-totality programme takes the case against infinity as settled for this work and moves on to building the actual account. The aim is one candidate connecting a real physical field, exact whole-level zero, local positive and negative contributions, relational time and a proposed experiential interpretation.

The concrete starting point is generally covariant gravity coupled to a U(1) gauge field, charged matter and a scalar clock. On a compact boundaryless spatial slice, its Gauss constraint forces the gauge charge to sum to zero while allowing nonzero local charges. We construct explicit nontrivial initial data satisfying **all three** classical Einstein–matter constraint classes, and separately calculate the energy and local evolution of a related matter-field configuration. A scalar clock gives a local relational-time reduction on an explicitly stated branch. We then make a **specific, falsifiable candidate bridge** from signed charge density to felt valence.

This is a physically specified *effective candidate*, not a derivation of quantum gravity or a claim that experience actually is electric charge. General relativity and spacetime here are recovery targets, not presumed ultimate. The experiential bridge, actual incidence and the derivation of this action from zero's self-subsistent nature are not yet established. The exact calculations are genuine consequences of the declared theory, but do not solve physics as a whole.

**Continuations:** [Nonlinear gravity–clock evolution](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) evolves these initial data, checks numerical constraint convergence and compares gravity with a fixed-metric control at the same clock reading. [Covariant clock–current history balance](ZERO_TOTALITY_COVARIANT_CLOCK_HISTORY_BRIDGE.md) derives a conditional zero spacetime integral and tests clock-slice fluxes and subject-weighting controls.

## 1. A single covariant candidate

In a classical regime where a smooth four-dimensional Lorentzian description is valid, consider

```text
S = integral d⁴x sqrt(-g) [ R/(2κ)
      - (1/4) F_{μν}F^{μν}
      - (1/2) (D_μ χ)·(D^μ χ) - (m²/2) χ·χ
      - (1/2) (∂_μ T)(∂^μ T) ],

F=dA,    D_μχ=∂_μχ-e A_μ Jχ,    J(χ₁,χ₂)=(-χ₂,χ₁).
```

Here χ has two real components, A is an Abelian gauge field, T is a real massless scalar clock, `κ=8πG>0`, and `e,m` are specified effective parameters. The metric signature is `(-,+,+,+)`. The sign conventions below use `E^i` and ρ such that `∂_i E^i=ρ` in flat-space coordinates. This is the familiar form of a charged scalar coupled to a gauge field and gravity, supplemented with a scalar clock; the proposed **experiential use** is new to this candidate, not a claim that standard scalar electrodynamics is new.

A local rotation `χ -> exp(-e λ J)χ`, with `A_μ -> A_μ-∂_μ λ`, is a gauge redescription. The field strength, gauge-invariant current and geometry are physical candidates; the phase convention itself is not a subject or a sensation. The action is local and generally covariant in this effective regime. That does not derive it, its constants, its fields, its actual state or spacetime from zero's nature.

We work on a specified globally hyperbolic region with compact, orientable Cauchy surfaces Σ without spatial boundary, and sufficiently regular fields. Compactness is an assumption of this realization—not a claim the actual universe has been observed to be compact, and not a general consequence of the user's zero proposal. There may be nontrivial gauge bundles or global flux sectors; the integrated result below uses a globally defined electric field density and no electric boundary/source term.

## 2. Physical local differences and whole-level zero

In canonical variables, let `π` be the momentum conjugate to χ and let `E^i` be the canonical electric field **density**. The gauge constraint is

```text
G(x) = ∂_i E^i - ρ = 0,       ρ = e π·Jχ.
```

Integrating on boundaryless Σ gives

```text
Q_gauge = integral_Σ ρ d³x = integral_Σ ∂_i E^i d³x = 0.
```

This is not imposed by matching each positive event to a negative event: it follows from the stated local Gauss constraint and global boundary condition. With matter and gauge field in the same action, no external balancer or external charge reservoir is introduced. Different subregions can carry nonzero signed charges, with their flux accounted for across internal boundaries. The same derivation applies on any admissible compact Cauchy slice of the stated theory; it is not a preferred fundamental foliation.

The physical content is **a zero gauge charge**, not yet the user's global energy or the total of all experiences. Zero energy, zero gauge charge and the vanishing Hamiltonian constraint are distinct claims. An infinite or boundary-bearing space, additional sources, modified Gauss law, or nonstandard boundary conditions require a separate calculation. This does not assert that the world fails the user's demand for a well-defined global quantity.

For background on ordinary Gauss constraints and boundary issues, I consulted the introduction of Bachlechner, [*Testing Hamiltonian Reduced QED*](https://arxiv.org/html/1910.08080v1), arXiv:1910.08080, and did not adopt that paper's nonstandard boundary-theory conclusions. For relational clocks, I consulted the abstract and introduction of Calcinari et al., [*Gauge versus (hidden) physical symmetries of FLRW cosmologies*](https://arxiv.org/html/2607.27351), arXiv:2607.27351; their minisuperspace analysis is not a proof of the full field-theory reduction below.

## 3. A nontrivial initial state in the actual field equations

To make this calculable, temporarily hold the effective spacetime metric fixed and flat on a cubic spatial three-torus of side L and volume `V=L³`. Use standard temporal gauge `A₀=0`; set `k=2πn/L`, `n>=1`, and initial data

```text
χ₁=v,              χ₂=b sin(kx),
π₁=0,              π₂=P cos(kx),
A_i=0,             E_x=(e v P/k) sin(kx),   E_y=E_z=0,
```

with real nonzero e, v, P and b. The fields are periodic. They are dynamical charged matter and gauge-field initial data, not a preassigned external current. At the initial time,

```text
ρ = e v P cos(kx),             ∂_i E^i = e v P cos(kx),
Q_gauge = 0.
```

The pointwise Gauss constraint is satisfied, and there are positive and negative regions if `e v P != 0`. For the current convention `j_i = -e (D_iχ)·Jχ`, initially

```text
j_x = -e v b k cos(kx),
∂_t ρ = -e v b k² sin(kx) = -∂_x j_x.
```

The time derivative follows from the coupled equations at that initial instant; it is not an assertion that the initial sine/cosine profile remains a solution at all later times. Standard constraint propagation keeps Gauss's law satisfied under the classical equations, for as long as a regular solution exists. Thus the specified initial configuration supports changing local contributions without violating the global neutrality condition.

The ordinary positive matter-plus-gauge Hamiltonian at that instant is

```text
H_matter+gauge = V [ P²/4 + b²k²/4
                     + m²v²/2 + m²b²/4 + (e v P)²/(4k²) ].
```

The final term is the positive longitudinal electric-field energy. For fixed charge amplitude `rho0=e v P`, its value is `V rho0²/(4k²)`: different wavelengths give a definite energetic cost, independent of assigning a phenomenal interpretation. The scalar gradient and mass costs are included above. A zero gauge charge emphatically does **not** make the state, its local fields, or its ordinary physical energy zero.

This first calculation holds the metric fixed; it is **not** itself a solution of the Einstein constraints with this stress tensor. The next section supplies a different, explicitly constraint-satisfying initial configuration for the full coupled theory. Neither choice says that a torus is the observed cosmological topology.

### A constraint-satisfying Einstein–gauge–clock initial configuration

We can do more than postpone gravity. In the *same action*, choose a second set of initial data on a three-torus with side `2π`. Work in normalized units with `e=1`, `m=0`, and set

```text
h_ij = δ_ij,              K_ij = (K/3) δ_ij,       K² = 15κ/2,
χ=(1, cos x),             π=(0, cos x),
A_i=0,                    E^i=(sin x,0,0).
```

Here `h` is the spatial metric, K the trace of extrinsic curvature, and the matter momenta and E are the canonical densities. In these coordinates `sqrt(h)=1`. Define the clock initial data by

```text
f(x) = sin x cos x,
S(x) = 4 - sin² x,
p_T(x) = sqrt([S(x)+sqrt(S(x)²-4 f(x)²)]/2),
∂_x T = f(x)/p_T(x),     ∂_y T=∂_z T=0.
```

The radicand is strictly positive: `S>=3` and `4f²<=1`. The derivative of T integrates to zero around the x-circle by reflection symmetry, so a smooth periodic T exists; its additive constant is immaterial to this free clock. Moreover `p_T²>(∂_x T)²` everywhere, so its four-gradient is timelike on the initial slice. This is a specifically constructed initial state, not a derivation that the whole must select it.

All three classes of constraint now hold **pointwise**:

- **Gauss:** `ρ=π·Jχ=cos x=∂_x E^x`; its integral on the torus is zero, although it is nonzero locally.
- **Momentum:** the gravitational momentum term vanishes because the spatial metric and K are constant. With `A=0` and `F_ij=0`, the matter term is `π·∂_xχ+p_T∂_xT= -sin x cos x+f(x)=0`; the other components vanish.
- **Hamiltonian:** the positive normal-frame matter-plus-clock energy density is

```text
rho_energy = 1/2 [cos² x + sin² x + sin² x + p_T² + (T')²]
           = 1/2 [1+sin² x + S(x)] = 5/2.
```

The equality `p_T²+(T')²=S` follows from the displayed quadratic root. Since the intrinsic spatial curvature is zero and `K_ij K^ij=K²/3`, the gravitational constraint is

```text
(1/(2κ)) (K_ij K^ij-K²-R^(3)) + rho_energy
    = -K²/(3κ)+5/2 = 0.
```

The first two sine-squared terms in the energy are respectively the χ gradient and electric field; π contributes cosine squared. No physical energy has been set to zero: positive matter/clock energy balances the gravitational term **in the constraint**. Nor is a vanishing constraint automatically the whole's observable physical energy.

This is a smooth, nontrivial, fully coupled **classical initial-data solution** to the stated Gauss, Einstein Hamiltonian and momentum constraints, not a numerical fit or an external-source profile. Standard local Einstein–matter Cauchy evolution, under an appropriate gauge and regularity assumptions, provides a local development; [a later computation](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) evolves it numerically in planar symmetry, but does not establish global existence, its quantum state, or its cosmological predictions. The inhomogeneous clock was deliberately constructed to satisfy the constraints, so its selected form and the action are not derived from zero. At the initial slice, with unit lapse and zero shift at that instant, the matter equations also give `j_x=sin x` and `∂_tρ=-cos x`, preserving global charge while changing local values. The clock is timelike there, but it is **not spatially constant on this initial slice**; the gauge `T=t` below is a local clock-coordinate choice on a suitable patch, not a claim that this very slice already is a T-constant slice.

## 4. Relational time in the coupled candidate

In the full gravity-plus-matter action, the local Hamiltonian constraint includes the scalar clock contribution

```text
C = C_rest + p_T²/(2 sqrt(h))
             + (sqrt(h)/2) h^ij ∂_i T ∂_j T = 0,
```

where `h_ij` is the induced spatial metric and `C_rest` includes gravity, gauge field and χ. The theory also has spatial-diffeomorphism and Gauss constraints. These are constraints of a specified covariant theory, not an established globally measurable energy of all reality.

On a region where T has an admissible timelike gradient and can serve as a clock, choose the **local gauge** `T=t`, so `∂_i T=0`. On the patch where the square root is real,

```text
p_T = ± sqrt(-2 sqrt(h) C_rest).
```

Selecting one branch and substituting into the canonical action yields the corresponding local relational Hamiltonian density `-p_T`, with remaining spatial-diffeomorphism and Gauss constraints. Its sign and clock orientation depend on the branch; this formula is not a proof of a globally positive Hamiltonian. The clock gauge requires nonzero p_T and a suitable lapse, and can fail at turning points or outside its patch. It selects a useful description, not a preferred **fundamental** foliation; the underlying displayed action is covariant. A full reduced phase-space construction and quantum treatment are still needed.

In particular, the gauge-charge zero, the local Hamiltonian constraint `C=0`, and the actual total energy of the whole are not identified merely because the first two vanish. A fundamental theory might make such an identification, but this effective calculation does not.

## 5. A concrete experiential bridge—and its physics prediction

Let `j^μ` be the gauge-invariant current in this model and `u^μ` an independently specified future-pointing physical observer/experience congruence where such a congruence exists. Define the charge density measured in that frame by `rho_u=-u_μ j^μ`. The proposed bridge is:

> **B:** on actual experiential incidences, signed felt valence per unit of the relevant local measure is `v_X=α rho_u`, with a single independently fixed nonzero conversion α. The actual subject-incidence rule identifies where this applies and avoids double counting.

This is a **hypothesis to test**, not a definition that turns χ into experience. A field may be physically present without any felt experience, and a signed scalar does not supply qualitative richness, phenomenal unity or subject identity. Taking B literally for all regions would also require explaining non-experiential charge and neutral or mixed experience. The gauge field could only be a *candidate hidden sector* until independently connected to actual measurements; it is not asserted to be the ordinary electromagnetic charge of brains.

The bridge has a sharp physical consequence. On a flat-background region R at rest in the chosen frame, let `V_R=integral_R v_X d³x`. Current conservation implies

```text
dV_R/dt = -α integral_(boundary R) j·n dA.
```

For a fixed region whose boundary current vanishes throughout an interval, the **spatially integrated signed valence in this specific candidate cannot change**. Local valence may change while its regional total stays fixed. Therefore a robust observed change in a properly calibrated regional total, together with an independently established bound excluding the necessary boundary flux and other missing terms, would challenge B and its domain. Merely observing changing feelings does not establish that the needed physical flux is absent. Conversely, an unconstrained unobservable flux introduced after the fact would make the proposal difficult to test.

The field energy above supplies a second discriminating prediction: a neutral sinusoidal charge pattern of fixed amplitude has a positive longitudinal energy proportional to `1/k²`. If B, α, the relevant fields and couplings were independently determined, changing spatial scale would constrain the associated physical cost. No numerical experimental bound or claim of already detecting the field is supplied. A realistic proposal must specify the coupling to known matter, operational observable, controls and existing constraints before experimental agreement can be assessed.

## 6. The actual-history total is not automatic

Gauss's law gives zero `integral_Σ ρ` on each admissible compact slice. The user's proposed total might instead sum **felt intensity over actual subject-history durations**. These are not automatically the same quantity.

For example, on a clock slice with normal `u=n`, canonical density `ρ=sqrt(h) rho_n`, and a vanishing shift in the chosen patch, a spacetime-volume-weighted integral of B over a finite slab is

```text
integral_slab v_X sqrt(-g) d⁴x = α integral dt integral_Σ N ρ d³x.
```

`integral_Σ ρ=0` does not force `integral_Σ Nρ=0` if the lapse varies spatially. In the flat illustrative profile, at the initial time `ρ=rho0 cos(kx)` and positive lapse `N=1+epsilon cos(kx)`, `|epsilon|<1`, give

```text
integral_Σ ρ d³x = 0,      integral_Σ Nρ d³x = epsilon rho0 V/2.
```

This is a **kinematic counterexample** comparing a slice charge with a spacetime-weighted quantity, not a demonstrated full coupled solution with this particular clock gauge and lapse, nor an observable effect of changing coordinates. Changing the lapse changes the slab bounded by the next clock slice; it must not be interpreted as physically changing a fixed four-dimensional region. It shows why specifying the actual domain, observer field and measure matters. An independently justified uniform lapse, alternative incidence measure, conserved-current flux definition or non-additive account could alter the conclusion; none is derived here.

The slice quantity may itself be the relevant global experiential invariant **if** B, subject incidence and that definition are established. If the user instead means a duration-weighted total over all actual experience, further work is needed. Neither option should be silently substituted for the other.

## 7. The constructive physics programme

This candidate now has an action, fields, constraints, an explicit constrained initial configuration, an internal clock reduction, an experiential hypothesis and concrete restrictions on observable behavior. The next substantive steps are:

1. **Develop the coupled evolution:** [the continuation](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) now evolves the initial state in a controlled planar gauge, checks numerical constraint convergence and makes a limited clock-matched backreaction comparison. Next establish a fully relational observable and broader gauge/three-dimensional controls, and assess whether any parameter regime approximates observed physics; the separate flat-field energy calculation here is not the nonlinear gravitational evolution.
2. **Specify and test B:** define actual local subjects and the incidence/quality rule independently of the desired zero. Derive how χ and A couple to ordinary matter and a reportable local valence measure, then test the conservation and wavelength-cost predictions against existing evidence.
3. **Unify the quantities:** identify whether the candidate's charge, the relevant all-history experiential total and a physically meaningful whole-level energy have a common origin or are distinct constraints. Do not equate them merely because they each can be zero.
4. **Derive rather than merely assume:** show how the action, parameters, topology/domain, clock, gauge constraint and experiential bridge follow from zero-totality's own self-subsistent constitution, or replace this effective action with a deeper theory that recovers it. No law, occurrence or qualitative fact is accepted as a final unexplained residue.
5. **Quantum and causal recovery:** construct physical constrained states and relational observables, recover ordinary quantum and relativistic behavior where tested, and distinguish unconditional local signals from postselection. The classical analysis does not establish a Born rule, a quantum gravity theory or the experiential identity.

These are concrete tasks, not a claim of completed physics. The user's rejection of infinity is not reopened here; the working hypothesis is zero, with real local experience and no external creator or cosmic subject.

## Verification

`python -m unittest verification.covariant_gauge_clock_framework_test -v` checks the periodic Gauss constraint, integrated positive and negative density, current continuity at the stated initial time, the energy formula and wavelength scaling, gauge-invariance controls, the algebraic clock branch, and the lapse-weighted counterexample. It also checks the explicit coupled Einstein–matter–clock initial constraint equations and clock periodicity on a dense grid. The closed-form identities establish those initial constraints; the numerical checks are not a nonlinear evolution, empirical validation or derivation of the fundamental action.

Related: [GR constraint and relational time](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md), [local boundary balance](ZERO_TOTALITY_LOCALITY_AND_BOUNDARY_BALANCE.md), and [actual-history experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
