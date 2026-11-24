# A normalizable quantum-cosmology packet for the sphere clock

## What advances

The [preceding integration](ZERO_POINT_SPHERE_RELATIONAL_QUANTUM_GRAVITY_TIME.md) used a fixed, generalized cosmological momentum and then inserted its phase rates into a finite five-reading history. Here the geometry, scalar clock and sphere–record clock are instead placed **in one continuous constrained minisuperspace model**. We choose a normalizable wavepacket on a positive-scalar-momentum branch, specify a physical inner product and exhibit its exact relational evolution. The clock's two internal energy sectors have different relational geometry velocities; an initially unentangled geometry and logical clock become entangled, and their reduced clock visibility falls.

A simple rotor action also gives one explicit source of the previously stipulated `h/a³` coupling. The identification of its two levels with the existing, nonlocal sphere–record logical qubit is an engineered encoding, **not** a derivation that real sphere records are a homogeneous fundamental field. The packet and the physical state are normalizable in the specified *physical* Hilbert space; the corresponding stationary solution is not a normalizable vector over all values of the scalar clock in the kinematical tensor product.

A further clock change maps the *same* physical state unitarily to an expanding-geometry-clock representation. Natural qubit visibility at `φ=0` and at `α=0` differs dramatically, but these are different relational conditionings. Transporting the same physical observable restores agreement. This is a concrete illustration of why changing clocks is more than relabeling.

This is a nontrivial example of quantum relational time in a constrained cosmology, not a solution of full quantum gravity or proof of the whole's objective energy zero. It does not derive the sphere, the action, the state, actual subjectivity, a metric scale or an outcome measure from zero. Its construction and 16 tests are in [verification/zero_sphere_flrw_normalizable_clock_test.py](verification/zero_sphere_flrw_normalizable_clock_test.py).

## 1. One action and the clock coupling

Consider compact flat FLRW minisuperspace with unit fiducial coordinate volume, `κ=8πG=1`, lapse `N`, scale factor `a>0`, homogeneous massless scalar `φ`, and a periodic homogeneous variable `X` with inertia `I>0`. Let `α=ln a`. In units `ℏ=1`, take

```text
L = −3 a (dot a)²/N + a³ (dot φ)²/(2N) + I a³ (dot X)²/(2N).
```

`X` is a simple compact massless field/rotor, not a literal externally placed device. Its canonical momentum is `p_X=I a³ dot X/N`. The lapse imposes the Hamiltonian constraint

```text
C = a^(−3) [−p_α²/12 + p_φ²/2 + p_X²/(2I)] = 0.
```

For finite `a>0`, multiplying by `a³` preserves the classical zero surface and changes the lapse convention:

```text
C̃ = −p_α²/12 + p_φ²/2 + h = 0,      h=p_X²/(2I).
```

A rotor of period `2π` has integer momenta. Choosing `I=1/2` gives `h=n²`: the invariant two-level sector `n=0,1` has energies `h=0,1`. The `n=−1` and all other modes are excluded by choosing this invariant sector, not forbidden by the action; the full rotor is more degenerate and larger. Because the rotor momentum is conserved here, the selected two-level sector is dynamically closed under this model's Hamiltonian. The scalar and rotor densities are positive when their momenta are nonzero, scaling as `a^(−6)`. The negative gravitational term is a constraint contribution, not a uniquely local negative energy density.

To couple to the existing sphere–record construction, identify the two rotor levels by an explicit **unitary encoding** with the two active logical states `|+⟩` and `|−⟩=Z_M₁|+⟩` of the prior five-ray joint state, so the corresponding logical Hamiltonian has eigenvalues 0 and 1. The test evaluates these actual finite-system vectors and their reductions, not just an abstract qubit. The physical microscopic realization of such a homogeneous rotor as that nonlocal multi-register logical degree of freedom is not supplied. In particular, this correspondence cannot be used to infer its locality or stress tensor. The complementary finite subspace in the prior code carries `h=1/2` but the physical packet below has **zero support there**; it is only a unitary extension for testing.

## 2. Physical branch, packet and constraint

On the expanding classical branch choose `p_α<0` and `p_φ>0`. For a logical energy h define

```text
ω_h(p)=√(p²/6−2h),     p=p_α.
```

Work on the invariant momentum band `−7<p<−6` with `h=0,1`; both roots are strictly positive and bounded away from zero there. This is a **chosen spectral sector**, not a claim that every cosmological state belongs to it. In particular, the branch and chosen levels are part of the model; the `n=2` rotor level does not even have a real root throughout this band.

For this sector the reduced Hilbert space is

```text
H_phys = L²((-7,−6),dp) ⊗ span{|+⟩,|−⟩},
H_φ(p,h) = −ω_h(p),
U(φ) = exp[−i H_φ φ] = exp[i ω_h(p) φ].
```

The multiplication operator `H_φ` is bounded and self-adjoint on this band. Its unitary evolution is with respect to the **internal scalar value** `φ`. With `p̂_φ=−i∂_φ`, the branch equation `(p̂_φ+H_φ)χ=0` implies `p̂_φχ=ωχ` and also the quadratic constraint `C̃χ=0` in the distributional/generalized-solution sense. It does not require an external time.

Specify a Klein–Gordon-type physical product on the `p_φ>0` branch. For solutions `Ψ(φ,p)` use the sign

```text
(Ψ₁,Ψ₂)_KG = −i ∫ dp [Ψ₁†∂_φΨ₂ − (∂_φΨ₁)†Ψ₂].
```

A mode `e^(+iωφ)/√(2ω)` then has positive unit weight. The map from reduced data `f_h(p)` to the covariant solution

```text
Ψ(φ,p) = Σ_h f_h(p) e^(+iω_h(p)φ) |h⟩ / √(2ω_h(p))
```

is an isometry from the displayed `L²` product to this chosen positive-branch product. In particular, the factor `1/√(2ω_h)` is **not** discarded in the covariant representation. This specifies one physical inner product and factor ordering for this sector; it is not a proof that all quantizations, clock choices or constraint rescalings produce the same measure. Positive-frequency scalar-clock quantum cosmology is an existing approach, not a novel discovery; compare the earlier [FRW modular-clock analysis](FRW_MODULAR_CLOCK.md).

Choose the real, normalized momentum wavefunction

```text
u=p+7,      f(p)=√30 u(1−u),   0<u<1;       f(p)=0 otherwise,
∫ |f(p)|² dp = 1.
```

The extension by zero has a square-integrable weak first derivative. The initial encoded clock is the actual previous state `|v⟩=(|+⟩+i|−⟩)/√2`. The reduced physical solution is therefore

```text
χ(φ,p) = f(p)/√2 [ e^(iω₀(p)φ)|+⟩ + i e^(iω₁(p)φ)|−⟩ ].
```

Its norm is one for every `φ`, and the covariant solution follows by adding the mode-normalization factors above. There is no additional normalizable uniform probability over `φ∈R`: the clock is a conditioning variable, not a sampled external time. Sharp `p` is a generalized momentum value; statements about a momentum-resolved clock refer to the fibers almost everywhere, while a finite momentum bin can itself exhibit residual dephasing.

## 3. Zero with nonzero terms, now in a normalizable state

On the physical solutions the gravitational, scalar and internal contributions cancel pointwise on each mode. For the chosen packet and equal clock-level populations, the physical expectations of the rescaled constraint terms are exactly

```text
⟨−p_α²/12⟩ = −74/21,
⟨ p_φ²/2 ⟩ = 127/42,
⟨ h ⟩       = 1/2,
                         sum = 0.
```

The test evaluates the integrals numerically and verifies the pointwise constraint. These are expectation values in the declared physical representation, not a derivation of an objective global energy observable. They supply an explicit nonzero-positive/nonzero-negative cancellation in one quantum model.

There is also an important distinction between **changing physics** and **redistributing the names of constraint terms**. If the `h` spectrum is shifted but the gravitational and scalar terms are held fixed, the constraint changes and so do the roots and allowed states. But the simultaneous algebraic replacement `h→h+c`, `C_grav→C_grav−c` leaves the entire constraint operator unchanged. Therefore the zero of the sum by itself cannot fix a unique split or establish which summand is the whole's fundamental energy. The underlying action can supply a conventional split in this model; it does not, by itself, prove that split to be the uniquely objective ontology.

## 4. Clock phase, entanglement and geometry backreaction

For the earlier sphere–record quadratures `Y` and `Z_M₁`, define

```text
F(φ) = ∫_(−7)^(−6) dp |f(p)|² exp{i[ω₀(p)−ω₁(p)]φ}.
⟨Y⟩ = Re F(φ),      ⟨Z_M₁⟩ = Im F(φ).
visibility = |F(φ)|.
```

The integral is not a classical uncertainty added after the fact: the physical state is a pure superposition of geometry momenta and clock sectors. Ignoring geometry leaves a logical density operator with eigenvalues `(1±|F|)/2`. The reduced logical and reduced geometry purities both equal `(1+|F|²)/2` for this pure bipartite state. Calculated values are:

| Scalar reading φ | Clock visibility | Reduced purity |
|---:|---:|---:|
| 0 | 1.000000 | 1.000000 |
| 10 | 0.990111 | 0.990160 |
| 50 | 0.774878 | 0.800218 |
| 100 | 0.324286 | 0.552581 |
| 200 | 0.041451 | 0.500859 |

The integral is evaluated with Simpson quadrature; successive refinements are checked. This loss of reduced visibility is **entanglement-induced dephasing in this chosen model**, not a proof of fundamental irreversible decoherence or an interference correction relative to a matched classical momentum mixture. Conditioning on a sufficiently narrow geometry-momentum bin can recover visibility; retaining the whole state retains its coherence.

The geometry responds differently in the two h sectors. The relational velocity for the canonically conjugate `α=ln a` in the reduced representation is

```text
v_h(p) = ∂H_φ/∂p = −p/[6ω_h(p)].
```

For this packet, `⟨v₀⟩=1/√6≈0.408248` and `⟨v₁⟩≈0.482817`. Thus at `φ=100` the branch-conditioned means of the relational `α` coordinate differ by approximately `7.45686`. In the h=1 branch its velocity variance is approximately `3.16414×10⁻⁵`, so, for this real unchirped initial packet, `Var(α)_1(100)≈10.3164` versus `Var(α)_1(0)=10`. This calculation uses the `i∂_p` quadratic form on the chosen packet: the packet lies in its derivative domain and vanishes at the band endpoints. **The band-restricted derivative is not thereby established as a self-adjoint global α observable.** Extending the construction to a complete geometric observable and its boundary conditions is a separate problem.

These are internal, branch-conditioned quantum correlations, not two simultaneous classical scale factors selected by an observer. The scalar and rotor momenta are conserved; this example does not demonstrate a time-dependent energy transfer between sectors. Nor is `φ` automatically proper time. Comparing with physical proper time requires reconstructing an appropriate metric and clock prescription.

A useful control is an incoherent equal mixture of `h=0,1`: it has no `Y` or `Z_M₁` phase signal even initially, whereas the coherent state has unit initial visibility and retains approximately 0.324 at `φ=100`. This shows what coherence contributes in the encoded model; it is not the same question as the proposed quantum time-dilation correction for coherently recombined *motional* alternatives.

## 5. Confined domain and the clock-neutral lesson

At each momentum and scalar reading, the sphere–record state remains in the same two-level phase orbit. Its full confined candidate-subsystem density and the five-ray table remain the same as in the earlier construction:

| Sphere label | Record 01 | Record 10 |
|---|---:|---:|
| 0 | 3/40 | 1/20 |
| 1 | 1/10 | 3/10 |
| 2 | 13/40 | 3/20 |

The test checks full density matrices at sample momenta and four phases that determine the constant, sine and cosine terms of the two-level reduced density; by linearity, tracing the momentum packet preserves the same confined state. Pair and triple contexts also give equal full receiver states over that tested phase orbit. These are properties of the stipulated states and accessible subsystems, not a general proof of relativistic locality or an experienced event.

This remains analogous to the player's thought versus chess moves, and the traveler's room chord versus the surface-restricted position held at A until return to B. The traveler is not a surface inhabitant and the player is not a piece. The unchanged confined description does not itself mean a confined inhabitant can access the extra correlation, and no holding interaction is required for the analogy.

For a bounded reduced observable A, a formal complete observable at scalar value τ in the first-order branch representation is

```text
O_A(τ;φ) = U(φ−τ) A U(φ−τ)†,
[p̂_φ+H_φ, O_A(τ;φ)] = 0
```

on an appropriate common domain, with `O_A(τ;τ)=A`. Its expectation in a physical solution equals the expectation of A in the reduced state at τ. This is the continuum counterpart of the previous finite transported observable, for this chosen global branch. It is not a general solution for interacting clocks, turning points, local field observables or the refoliation constraint algebra.

The point–sphere idea contributes an interpretation and preexisting kinematic candidate: the point denotes no outside location/time, while the sphere expresses internal differentiated directions. The action, clock coupling, wavepacket and scalar branch are **not derived from the sphere**. The Lorentz-cone construction likewise does not determine the conformal scale or this cosmological dynamics. Selecting a scalar clock is a relational description of this homogeneous model, not a claim that fundamental reality has a preferred foliation.

## 6. Changing from the scalar clock to an expanding-geometry clock

The same constraint also permits a second deparametrization **on this selected branch**. Let `s=p_φ>0` and `α` be the internal reading. The negative-p momentum solution is

```text
p_h(s) = −P_h(s),    P_h(s)=√(6s²+12h),    J_h(s)=|dp_h/ds|=6s/P_h(s).
H_α = P_h(s),        U_α(α)=exp[−iP_h(s)α].
```

The classical `α` increases with φ on this branch. A factor-ordered positive-branch Klein–Gordon flux gives a unitary change of spectral coordinate between the two reduced physical representations:

```text
(W f)_h(s) = √J_h(s) f_h(p_h(s)).
```

Use the support mapped from `−7<p<−6` in each h sector, and extend by zero to compare the sectors. The Jacobian is essential: `∫ds |(Wf)_h|²=∫dp |f_h|²`. The tests verify both roots, Jacobian, component norms and selected oscillatory integrals. One way to see the flux normalization is to use the constraint `p_φ²−p_α²/6−2h=0`: the α-direction Klein–Gordon flux carries the coefficient `1/6`, rather than treating α and φ as identically normalized coordinates. This is a selected positive-momentum branch and physical measure, not a proof of equivalence for all branches, clocks or orderings.

The natural clock-relative logical visibility after tracing the remaining scalar-momentum degree of freedom at `α=0` is

```text
V_α(0) = ∫ ds √[J₀(s)J₁(s)] f(p₀(s)) f(p₁(s)) ≈ 0.00211769.
```

At `φ=0`, by contrast, the natural scalar-clock logical visibility is 1. The reason is explicit: the h=0 scalar-momentum support is `(√6,7/√6)` and the h=1 support is `(2,√(37/6))`, with only a narrow common interval. The `α=0` and `φ=0` descriptions condition on **different physical clock surfaces** and trace different degrees of freedom. Comparing their untransformed qubit operators is not a comparison of the same relational observable.

Indeed, if `A` is the `φ=0` logical observable in the first representation, the identical physical observable in the second is `W A W†`. For the normalized physical state, `⟨Wχ|W A W†|Wχ⟩=⟨χ|A|χ⟩`; it is generally not the simple same-scalar-momentum Pauli operator whose visibility was computed above. The amplitude transformation and unitarity are proved by the change of variables; the tests separately check the two natural conditioning results and calculate the transported observable's expectation as 1. In the α-clock representation this operator connects different scalar momenta in the two internal sectors, rather than acting as a same-momentum Pauli matrix. A full measurement scheme for finite-resolution quantum clock readings and all transported instruments is not implemented. In particular, `α` here is a deparametrization coordinate with a chosen positive-flux physical product, **not** a demonstrated self-adjoint clock operator on the band or an assertion that infinitely sharp band-limited readings form an orthogonal PVM.

This comparison makes the clock-choice issue constructive: the two representations preserve physical inner products and transported predictions, while distinct clock-conditioned questions can have very different answers. It does not make either clock fundamental, and it does not establish refoliation invariance in inhomogeneous gravity.

## 7. Experience, necessity and the next discriminating construction

A stationary physical state, an internal phase, a record distribution and a confined restriction are four different ingredients. None entails that the phase is felt, that a subject persists, or that an outcome is actual. The earlier rival incidence laws remain compatible with these physical data. If a suitable signed experiential quantity balances globally, local suffering is still suffering for its subject; neither a positive experience elsewhere nor an algebraic zero erases it. The thesis that genuine possibility and actuality coincide is a candidate account of necessity, not a consequence of the packet's normalization or its conditional probabilities.

This continuation has removed the fixed-momentum and finite-clock regulator from one concrete minisuperspace sector and given a classical action for the coupling. The next steps that would materially test the proposal are:

1. **Operational clock change:** implement finite-resolution scalar and geometric clock instruments and transported observables on a common physical domain, including branch boundaries, reversals and the effects of imperfect clocks. The present flux-based switch is not a globally valid self-adjoint α clock or a full instrument construction.
2. **Beyond the engineered encoding:** derive a local realization whose stress tensor and record dynamics reproduce the assumed internal sector; explain why that coupling and initial state follow from the proposed constitution, rather than choosing them.
3. **Beyond homogeneity:** construct inhomogeneous constraints and local relational observables, demonstrate closure/anomaly freedom and slicing-independent predictions, and recover metric scale and observed relativistic physics.
4. **Whole and experience:** define a justified objective total quantity and show its zero rather than equating it with a constraint; derive or independently test subject selection, incidence, signed valence and their measure. Show how necessity fixes these without residue and without canceling local suffering away.

No residue is resolved by calling the specified action, sector or state self-evident. Whether the internal constitution of a self-sufficient zero can require them is the outstanding foundational problem that the mathematical model makes sharper.

## Reproduction and scope

```sh
python -m unittest verification.zero_sphere_flrw_normalizable_clock_test -v
```

Tests use only Python's standard library and existing project modules. They combine exact identities, analytic physical-Hilbert-space definitions, numerical one-dimensional integration and finite-vector reductions. Test success is evidence for the encoded statements, not full quantum gravity, empirical confirmation, objective energy zero or actual experience.
