# A closed relativistic field–matter frame and incidence ledger

## Result and relation to existing work

The repository already contains a [closed nonrelativistic plasma oscillator](ZERO_SPHERE_CLOSED_PLASMA_INCIDENCE_GATE.md); closure is not new here. This review strengthens that particular example to a homogeneous **relativistic**, collisionless two-stream/Maxwell solution and applies the moving energy-frame analysis from the [previous review](ZERO_ENERGY_FRAME_DEFORMATION_RIGOR_REVIEW.md) to both sides of the same physical exchange.

For a specified common observer, field and matter exchange cancel **pointwise** when given the same weight, irrespective of observer deformation. Yet, in the exact same closed periodic solution, the field's separately integrated exchange in a moving field-energy frame is strictly nonzero despite zero boundary flux; the matter exchange is its opposite. Unequal positive complementary weights then leave a nonzero weighted pair total. This is a rigorous conditional counterexample to *automatic* weighted cancellation, not a prediction about experience or a refutation of the current zero-energy framework.

The observer and the weights are engineered and are not derived subjects. The model has positive conserved energy, flat effective background, no gravity and a specially prepared pair of streams. These limitations are central, not incidental.

## 1. Autonomous two-stream Maxwell dynamics

Work on a flat three-torus of unit coordinate volume with metric `(−,+,+,+)` and c=1. In units with unit charge magnitude and permittivity, use two collisionless cold species of equal rest mass `m>0`, uniform lab number density `n>0` each, charges `+1` and `−1`, and opposite momenta `+p(t) ŷ` and `−p(t) ŷ`. The electromagnetic fields are

```text
E⃗ = E(t) ŷ,      B⃗ = B_* ŷ,      B_*>0 constant.
w = sqrt(m²+p²),  j⃗ = (2np/w) ŷ,  ρ=0.
E' = −2np/w,      p' = E.
```

Both species satisfy their Lorentz-force equations: their velocities are `±p/w` parallel to B, so the magnetic force vanishes; the negative species has momentum derivative `−E`. Their separate continuity equations hold. Gauss, Faraday and Ampère laws hold, including zero total charge; the homogeneous magnetic flux is a permitted classical torus sector, not assumed to have a globally periodic vector potential. No external source or prescribed energy input is used. The constant magnetic component keeps the electromagnetic energy current nonzero even when E crosses zero; it does not change the oscillator equation.

The field and matter stress tensors in `(t,x,y,z)` coordinates, with `r=(E²+B_*²)/2`, `M=2nw` and `P=2np²/w`, are

```text
T_F = diag(r, r, −r, r),       T_M = diag(M, 0, P, 0),
f^μ = (jE, 0, 0, 0),          j=2np/w,
∂_μ T_F^{μν}=−f^ν,             ∂_μ T_M^{μν}=+f^ν.
```

These are full stress tensors, not just an assigned scalar compensator: `T_M` is the sum of two positive-energy relativistic dust streams. In particular,

```text
r' = −jE,   M' = jE,   H=r+M=constant > 0.
```

For initial `E(0)=A>0, p(0)=0`,

```text
E² = A² − 4n(sqrt(m²+p²)−m),
p_max = sqrt((m+A²/(4n))²−m²).
```

The smooth phase-plane orbit is compact and closed, with finite period: p rises from 0 to `p_max`, falls to `−p_max`, and returns. The reduced E–p oscillator is invariant under `t→−t, E→E, p→−p`; physical electromagnetic time reversal also reverses the magnetic field and exchanges the two magnetic-flux sectors. This is a specified effective-time evolution, not a derivation of fundamental time or of emergent spacetime.

## 2. Common observer, deformation and incidence

Pick a smooth observer congruence moving along the common field direction:

```text
v(t)=b+c E(t)p(t),   gamma=(1−v²)^(−1/2),
u^μ=gamma(1,0,v,0).
```

Choose `m=n=B_*=1`, `A=0.8`, `b=0.4`, `c=0.5`. Since `|Ep|≤A p_max` and `p_max≈0.58787754`, the rigorous bound is `0.16484<v<0.63516`. Thus u is smooth and future timelike throughout. This state-dependent frame is an illustrative prescription using a selected direction and constants, not a demonstrated organization or subject. The time-reversal-sensitive `Ep` term and offset b are especially important: a constant observer velocity would give a zero cycle integral here.

For each sector use `C_i^μ=−T_i^{μν}u_ν`, with field exchange `h_F=f^νu_ν=−gamma jE` and matter exchange `h_M=−h_F`. Their identity is

```text
h_i = ∂_μ C_i^μ + T_i^{μν} ∂_μ u_ν.
```

Here the fields are homogeneous, so the spatial divergence is zero, and

```text
C_F^0 = gamma r,      deformation_F = −r gamma',
C_M^0 = gamma M,      deformation_M = −M gamma',
h_F = gamma r',       h_M = gamma M' = −h_F.
```

The deformation terms do **not** generally cancel pointwise: their sum is `−H gamma'`. It cancels the corresponding divergence `∂t(gamma H)` in the closed **total** ledger. Since the physical fields and this selected u return after one period, each sector's time-boundary term also vanishes; spatial boundaries are periodic.

The field tensor has `T_F u = −r u`, hence `C_F=r u` everywhere. The constant magnetic component guarantees `r≥B_*²/2>0`. A smooth, positive, conserved auxiliary current aligned with it is

```text
K= (1,0,v,0) = C_F/(gamma r),     ∂·K=0.
```

The constant marker `χ=1` is transported by K, and both K and the fields are periodic as Eulerian fields. K's individual worldlines need not close after one cycle on the torus; matching Eulerian boundary data is the condition used. K is a constructed current, not evidence of a subject or a physical incidence measure.

A further restriction appears when **both** sectors are required to share that same rest frame. For matter,

```text
C_M^0=gamma M,   C_M^y=−gamma v P,
C_M^y−v C_M^0=−gamma v(P+M).
```

Because `P+M>0`, matter's energy current aligns with u only for `v=0`. The matter center frame is then also a field-energy frame and is inertial in this solution. Thus the moving counterexample aligns the field current with the chosen u, **not** both sector currents. Simultaneous alignment is a strong extra condition that removes this particular moving-frame example; it is not derived for general matter, field configurations, incidence flows or curved spacetime.

## 3. Analytic sign on the full cycle

Although the complete field boundary flux vanishes, define

```text
W = ∫₀ᵀ h_F dt = −∫₀ᵀ gamma(b+cEp) (2npE/w) dt.
```

This is strictly negative for the stated parameters. It is not merely a grid result. Write

```text
E_+(p)=sqrt(A²−4n(sqrt(m²+p²)−m)) ≥ 0.
```

Using `p'=E`, traverse the orbit once, with E positive on the increasing-p branch and negative on the decreasing-p branch:

```text
W = −2n ∫_{−p_max}^{p_max} (p/w)
       [gamma(b+c p E_+(p)) − gamma(b−c p E_+(p))] dp.
```

The two gamma arguments remain positive and below one. Gamma is strictly increasing on `(0,1)`; the bracket therefore has the sign of p wherever `0<|p|<p_max`. The integrand is strictly negative there, proving `W<0`. It follows that the period integral of the field deformation is W and that of matter deformation is `−W`; each time-boundary contribution is exactly zero. Numerical adaptive ODE evolution and a separate phase-plane quadrature give `T≈4.703086110` and `W≈−0.06171476522`; these decimals are checks, while the sign proof above is analytic.

## 4. Common versus different weights and frames

With the **same observer u** and equal scalar weight χ, the local physical exchange cancels identically:

```text
χ h_F + χ h_M = 0.
```

This does not require each sector's boundary or deformation term to vanish. It also does not identify χ with actual experience. For two different candidate weights,

```text
χ_F h_F + χ_M h_M = (χ_F−χ_M) h_F.
```

On the same closed cycle, choose strict complementary constants `χ_F=3/4`, `χ_M=1/4`. They can partition the same conserved K into `K_F=χ_F K` and `K_M=χ_M K`, with both positive and conserved. The weighted pair integral is `W/2≈−0.03085738261`, despite exact physical conservation, periodic endpoints and equal-and-opposite exchanges. This is a deliberately stipulated *sector-weighting* rule. A candidate theory must independently justify why sector weights represent subject incidence and how it avoids double-counting; these constants do not establish subjects or valence. Equal weights, or any independently derived condition making `∫(χ_F−χ_M)h_F=0`, restore the weighted cancellation. Pointwise equality is sufficient, not necessary.

If sector exchanges are instead evaluated in different physical observers `u_F,u_M`, then the formal weighted sum is `f·(χ_F u_F−χ_M u_M)`. Changing a physical observer is not merely changing coordinates, and there is no automatic pairwise cancellation. Whether such a mixed-frame sum represents an operationally or phenomenally meaningful quantity is an additional question, not something established by writing a covariant scalar.

## 5. What this does and does not accomplish

This calculation removes the earlier *external-current* gap in a specific relativistic toy and identifies two different mechanisms: an observer-deformation ledger for each subsystem and an independent sector-weighting mismatch. It also shows that a common field–matter rest frame can restore the simple inertial cancellation **in this model**, but does not show that the common frame or equal weights are required by the current framework.

The total energy here is `H=(A²+B_*²)/2+2nm>0`: local exchange cancellation is not a derivation of an objective whole-level zero. The flat metric, torus topology, Maxwell and dust equations, initial state and effective time are inputs. The magnetic sector, ideal collisionless streams and lack of gravitational backreaction are idealizations. A dynamical frame prescription was chosen to exhibit a real mathematical possibility, not derived from physical subject organization. There is no inference from energy exchange to pleasure, pain, a universal subject, an incidence probability, or actual phenomenal unity.

A next integrated step is to derive a non-arbitrary organization and its frame/weights from the same physical constitution, then test the resulting complete field–matter–gravity ledger and its effective clock and boundary conditions. Such a route must show how effective spacetime and internally experienced succession arise from non-fundamental space and time, rather than promoting this background into a fundamental premise. The existing [nonrelativistic closed oscillator](ZERO_SPHERE_CLOSED_PLASMA_INCIDENCE_GATE.md) and [quantum incidence partition review](ZERO_CYCLE_INCIDENCE_PARTITION_RIGOR_REVIEW.md) provide independent controls; their models are not thereby identified with this one.

## Verification

[Focused executable tests](verification/zero_closed_relativistic_plasma_frame_review_test.py) check field/matter balances, stress eigenvectors and observer-deformation signs symbolically; independently compute the periodic solution and phase-plane integral; and check endpoint, energy, velocity and weighting controls. They validate the assertions they encode, not the subject or whole-level interpretations.
