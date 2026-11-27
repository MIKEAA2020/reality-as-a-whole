# Closed plasma: a time-reversal-even response can still weight a cycle unevenly

## Finding

The [relativistic field–matter review](ZERO_CLOSED_RELATIVISTIC_PLASMA_FRAME_BALANCE_REVIEW.md) constructed an autonomous closed plasma in which unequal weights can spoil a pairwise exchange cancellation. Its nonzero example used a specially moving frame. Earlier, the [nonrelativistic closed-plasma example](ZERO_SPHERE_CLOSED_PLASMA_INCIDENCE_GATE.md) used a response that changes under time reversal. Do either of those choices explain the whole obstruction?

No. Extending the **same relativistic closed plasma** with an independent, dynamical neutral scalar gives an explicit state-dependent response that is even under time reversal, charge conjugation and scalar sign reversal. The field, charged streams and scalar all have the **same inertial energy-rest frame**. For suitable small amplitudes a periodic solution has a rigorously nonzero weighted field–matter cycle, although the unweighted exchange cancels pointwise. The opposite phase gives the opposite value, and a symmetry-compatible phase gives zero.

This is a conditional mathematical result, not an explanation of why a particular phase or response is actual, or a demonstration of experience. The scalar frequency is intentionally tuned; the response is stipulated. The two changing weights are **not separately conserved currents**. That distinction prevents this example from being misread as a counterexample to the separate-conserved-transport theorem below.

## 1. One autonomous physical model

Use the prior flat three-torus relativistic two-stream solution, c=1, unit coordinate volume:

```text
E⃗=E(t) ŷ,  B⃗=B_* ŷ,  B_*>0,
w=sqrt(m²+p²),   j=2np/w,
E' = −j,         p'=E,
r=(E²+B_*²)/2,   M=2nw,
r'=−jE=:h_F,     M'=+jE=−h_F.
```

The two species have equal lab densities n, charges ±1 and momenta ±p; their energy currents and the electromagnetic energy current are all at rest in `u=(1,0,0,0)`. The fixed B supplies a nonzero field energy even at E=0 and has no force on streams parallel to it. The prior review checks the Maxwell and Lorentz-force equations and complete stress tensors. There is no external current. The total physical energy is positive, not a whole-level zero.

Add an uncoupled spatially homogeneous real scalar with positive mass parameter Ω and its canonical momentum:

```text
φ'=Π,  Π'=−Ω²φ,
S=(Π²+Ω²φ²)/2,   S'=0.
```

Its stress tensor has zero momentum density in the same frame. Because the scalar is uncoupled, the combined field–two-stream–scalar system is still autonomous and conserved; no energy is transferred to the scalar. It is an internal dynamical **reference variable**, not an externally forced clock or an established subject. Decoupling also means its ability to influence the proposed response is an extra hypothesis, not a physical interaction derived from these equations.

Choose an orbit with `E(0)=A>0`, `p(0)=0`. Set

```text
P=sqrt((m+A²/(4n))²−m²),   |p|≤P,   |E|≤A,
T=plasma orbit period,       ω=2π/T,    Ω=2ω,
φ(0)=D sinθ/Ω,              Π(0)=D cosθ,    D>0.
```

Thus `φ=(D/Ω)sin(Ωt+θ)` and `Π=D cos(Ωt+θ)`. The scalar makes two complete cycles per plasma period. **Tuning Ω to this particular orbit is an explicit construction**, not a generic resonance or an explanation of this initial state. A and P can be read from the plasma's conserved energy and D from the scalar's conserved energy; they are not extra time-dependent drivers. Ω is a fixed parameter of the chosen model.

## 2. A bounded, symmetry-even candidate response

For `0<k<1` define

```text
α = k (E p)/(A P) · (2Ω φΠ)/D²,
χ_F=(1+α)/2,     χ_M=(1−α)/2.
```

Both factors in α have absolute value at most one. Therefore `χ_F+χ_M=1` and both lie in `[(1−k)/2,(1+k)/2]`. These are **response shares**, not identified physical subjects. They are functions of the instantaneous physical state and conserved orbit constants; the scalar's role and the formula remain stipulated. In the common matter rest frame, `Ep` can be written as the electric-field dot product with the positive species' momentum, so no choice of spatial orientation is needed for that product.

The actual symmetry transformations matter:

- Under charge conjugation E, B and the positive-species momentum p reverse, while the neutral scalar is unchanged. `Ep`, α and `h_F=−jE` are even.
- Under physical time reversal p, Π and B reverse, while E and φ are even. Each of `Ep` and `φΠ` is odd, so α is **even**, whereas `h_F` is odd.
- Under the scalar's independent reflection `(φ,Π)→(−φ,−Π)`, α is also even.

The magnetic flux reverses under physical time reversal; the opposite-flux sector has the same reduced oscillator and exchange because the aligned B has no magnetic force. Time-reversal invariance of a **law** or of this response does not imply that a selected initial state or its phase is invariant.

With a common observer and equal response weights, `h_F+h_M=0` exactly. For these unequal weights the candidate pair total is

```text
W = ∫₀ᵀ (χ_F h_F+χ_M h_M)dt = ∫₀ᵀ α h_F dt
  = −(2nk/(AP)) ∫₀ᵀ (Ep)²/w · sin(2Ωt+2θ) dt.
```

All sectors have returned to their initial Eulerian state at T; the spatial boundary is periodic; the unweighted exchange and total energy are conserved. Neither the mere state-dependence nor the discrete symmetries of this response force W to vanish.

## 3. Analytical nonzero result and reversal control

For the initial plasma state above, oscillator symmetry gives `p(T/2−t)=p(t)` and `E(T/2−t)=−E(t)` (with time understood modulo T). Consequently `F(t)=(Ep)²/w` has that reflection symmetry. Since `Ω=2ω`, the term involving `sin(4ωt)` integrates to zero and

```text
W(θ) = −(2nk/(AP)) sin(2θ) ∫₀ᵀ F(t) cos(4ωt) dt.
```

Thus `W(−θ)=−W(θ)` and `W(0)=0` exactly. A time-reversed initial state, possibly followed by the scalar's sign reflection, corresponds to the opposite phase (and opposite magnetic-flux sector), so the two signed values cancel **if equally weighted**. Equal weighting of distinct actual histories is not implied by the model.

To prove that a nonzero value exists without relying on numerical quadrature, fix `m,n,D,k>0`, take `θ=π/4`, and send `A→0+`. Let `ω₀=sqrt(2n/m)` and use the phase `s=2πt/T`. After rescaling E and p, smooth ODE dependence and the simple half-cycle crossing give, uniformly over one period,

```text
E/A → cos s,  p/P → sin s,  (j/A)/ω → sin s,
ω→ω₀,  2ΩφΠ/D² → cos(4s).
```

The scalar limit follows because Ω=2ω and θ=π/4. The simple crossing also makes T continuous near the harmonic limit. Therefore

```text
lim_{A→0+} W/A²
 = −k ∫₀²π cos²s sin²s cos(4s) ds
 = kπ/8 > 0.
```

Hence W is strictly positive for **all sufficiently small nonzero A**, although this existence proof does not provide an explicit amplitude threshold. It uses a family of tuned scalar masses Ω(A); it does not assert nonzero W for every model parameter or generic initial phase. The time-reversed phase has the negative value.

For illustration, with `m=n=B_*=D=1`, `A=0.8`, `k=0.6`, numerical evolution gives `T≈4.703086110`, `Ω≈2.671941427`, and `W(π/4)≈+0.1471787903`; `W(−π/4)` is its negative, while `W(0)` is numerically zero. Independent quadrature of the exchange using the numerically evolved plasma and the exact scalar solution agrees. Those particular decimals and the sign at A=0.8 are numerical, not established by the small-amplitude existence proof.

## 4. What changes in the incidence ledger?

Let `K=(1,0,0,0)` be an auxiliary conserved positive current in the common frame. The complementary candidate currents `K_F=χ_F K`, `K_M=χ_M K` satisfy

```text
∂·K_F=χ_F',    ∂·K_M=χ_M',    ∂·(K_F+K_M)=0.
```

At θ=π/4 and t=0, `χ_F'=kA/(2P)>0`, so the two currents are **not separately conserved**. One may regard the opposite sources as a formal exchange of labels, but no physical mechanism or subject-creation rule follows. If χ is merely a response rather than a population fraction, the derivative is instead a change of response; its phenomenological meaning remains unsettled.

In the common inertial frame, the exact weighted product rule reads

```text
χ_F h_F+χ_M h_M
  = ∂t(χ_F r+χ_M M) − (r χ_F'+M χ_M').
```

The boundary term vanishes on the cycle. The remaining switching/response-gradient term accounts exactly for W; no energy is created or destroyed. It should not be omitted when multiplying the balance by changing weights.

Conversely, if each sector's energy current is `C_i=ε_i u`, each weight is transported by the same u, u is Killing on the relevant domain, and each weighted boundary flux vanishes, then each weighted exchange integral is zero: symmetry of `T_i` kills its deformation and transport kills `C_i·∂χ_i`. This is a **sufficient conditional theorem**, not a general subject or whole-energy law. In this homogeneous example, demanding separate conservation of χ_i K with the chosen K forces each χ_i constant, so the present response is excluded. More general inhomogeneous flows, sources and moving observers need separate analysis.

## 5. What is genuinely left to derive

The calculation advances the compatibility test: even common inertial frames and time-reversal-even state response do not ensure a weighted zero without a justified transport, phase, history-pairing or other cancellation mechanism. It does not choose among these mechanisms. In particular, the uncoupled scalar and tuned phase do not establish a physically constituted subject or empirically relevant organization; no valence follows from h, and positive and negative contributions would not erase suffering.

The model assumes a flat metric, compact space, effective time and classical field equations. To connect with the user's framework, these must ultimately be recovered as effective structures from a non-fundamental spatial and temporal constitution, including internally experienced succession, rather than imposed as fundamental. Gravitational energy and any objective whole-level zero remain unresolved. A next step is to find an independently motivated organization/transport law and calculate its conserved-current and full field–matter–gravity boundary terms on the *same* effective history; a symmetric distribution over paired phases is only a separate hypothesis.

## Verification

[Reproducible model](verification/zero_closed_plasma_scalar_response.py) and [tests](verification/zero_closed_plasma_scalar_response_test.py) check the symmetry transformations, autonomous evolution, bounded complementary weights, matching endpoints, total energy, independent scalar quadrature, opposite phases, equal-phase zero and the small-amplitude limit. They also check that the two weighted currents have opposite nonzero sources. These checks do not validate the chosen response as experience or prove the entire framework.
