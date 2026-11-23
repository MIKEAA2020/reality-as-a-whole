# A constructive energy-locked incidence model

## Result

The preceding [organization–energy balance gate](ZERO_TOTALITY_ORGANIZATION_ENERGY_BALANCE_GATE.md) identified an extra term when an experiential organization moves relative to physical energy flow. Here is a concrete way that term can vanish **without inserting a compensating contribution by hand**:

1. Take a physical energy current `C` and a positive incidence current `K` whose flow is aligned with `C`.
2. Transport a positive organization marker `χ` along that flow.
3. If the weighted energy flux through the complete boundary vanishes, the organization-weighted signed energy exchange vanishes.

This is a conditional construction: it does **not** establish that actual subjects follow electromagnetic energy flow, that the relevant energy current is electromagnetic, that the necessary boundary condition is fundamental, or that energy exchange constitutes felt valence. Its benefit is to turn the previously missing cancellation into an explicit dynamical compatibility requirement, which can be checked and challenged.

## 1. Covariant form of the compatibility condition

In a smooth effective spacetime, let `h` be a specified signed exchange density and `C^μ` a physical current satisfying

```text
h = ∇_μ C^μ.
```

For an admissible scalar `χ`,

```text
χ h = ∇_μ(χ C^μ) − C^μ∇_μχ.
```

Suppose the proposed actual-incidence current is `K^μ=λ C^μ`, with `λ>0` on the relevant domain, and that the organization marker is transported along it:

```text
K^μ ∇_μχ = 0.
```

Then `C^μ∇_μχ=0`, so the weighted signed total becomes an explicit boundary flux:

```text
∫_D χ h dV = ∮_∂D χ C^μ dΣ_μ.
```

If that **weighted** flux is zero, the integral is zero. It is not enough that the unweighted boundary flux be zero; `χ` must also be included. This form does not demand an external or fundamental global clock. An effective future direction and appropriate domain still need to be physically specified.

There is a material qualification: for the electromagnetic energy-exchange density `h=−j^μF_{μν}u^ν`, the previous report gives

```text
h = ∇_μ C^μ + T_EM^{μν}∇_μ u_ν,
C^μ = −T_EM^{μν}u_ν.
```

Therefore the simple theorem applies directly in a suitable inertial fixed-background setting where the additional term vanishes, or to a different current whose divergence has independently been shown to be the full relevant exchange. In general curvature, expansion, acceleration or shear contribute an additional weighted volume term. It cannot be dropped by calling the calculation covariant.

### Incidence conservation is an extra equation

Even when `K=λC`, a conserved incidence current does not follow from the exchange law, since `∇·C=h`. Requiring `∇·K=0` gives

```text
C·∇λ = −λ h.
```

For smooth regular characteristics and positive initial `λ`, this transport equation preserves positive `λ` on a finite regular domain. It is a consistent way to construct a conserved auxiliary current; it is **not a derivation of real subjects**. A theory must explain why an actual subject measure has this transport and normalization, rather than choosing it to enforce balance.

## 2. Is electromagnetic energy flow a possible timelike incidence flow?

In a fixed inertial frame use `C=(u,S)`, where `u=(|E|²+|B|²)/2` and `S=E×B` in units with `c=1`. For `u>0`, the candidate energy-flow velocity is

```text
v_E = S/u.
```

The electromagnetic identity

```text
u² − |S|² = (|E|²−|B|²)²/4 + (E·B)² ≥ 0
```

shows `|v_E|≤1`. When the right-hand side is strictly positive, the energy current is timelike and can in principle be aligned with a timelike current. For a null field such as an ideal plane wave, `|v_E|=1`: a nonzero timelike subject current **cannot** be parallel to that null energy current. Where `u=0`, `v_E` is undefined. These are genuine domain restrictions, not proof that the electromagnetic energy current represents an experiencing subject. A different current or constitutive law would be needed in null or vanishing-field regions.

Even in the timelike case, energy flow and an actual organism's subject flow need not coincide. This strong alignment hypothesis requires physical and experiential justification; its mathematical availability is not that justification.

## 3. Explicit Maxwell test: two incidence flows, one physical field

On a periodic spatial ring `0≤x<2π`, with unit transverse area and `0≤t≤2π`, prescribe in a fixed inertial frame

```text
E_y = 1 + A sin(t) cos(2x),
B_z = −2A cos(t) sin(2x),
j_y = 3A cos(t) cos(2x),       A=0.1.
```

These fields satisfy Faraday's law and Ampère's law with the stated current; `ρ=0`, so Gauss's law and charge continuity hold. Their energy density `u` and flux `S_x=E_y B_z` satisfy `h=−j_y E_y=∂t u+∂x S_x`. The source current is **externally specified**, not derived from a material action or a complete closed universe. We compare two positive, conserved candidate incidence flows on exactly these same electromagnetic fields:

**A. Energy-locked flow.** Define `v_E=S_x/u`, evolve `∂tN+∂x(N v_E)=0` from `N(0,x)=1`, and evolve the marker `∂tχ+v_E∂xχ=0` from `χ(0,x)=1+0.4 cos(2x)`. Thus `K=(N,Nv_E)=λ(u,S_x)`, with `λ=N/u`. The local candidate valence is `v_X=αh/N`, the candidate incidence measure is `dμ=χN dx dt`, and their total is `α∫χh`. The interval's boundary condition is satisfied in this example: `u` returns, and the velocity has the form `v_E=cos(t) f(x,sin(t))`, so its characteristics retrace as `sin(t)` goes `0→1→−1→0`; the marker returns too. Consequently `∫χh=0`.

**B. Independently moving flow.** Take `K=(1,1/2)` and `χ=1+0.4 cos(2x−t)`. Both `K` and `χK` are conserved, `χ` is transported by `K`, and `χ` and `u` have the same endpoint values as in A. The relative energy flow does not vanish. Exactly,

```text
∫χh dx dt = −3 A (0.4) π² = −0.12π² ≈ −1.18435.
```

The correction term in the preceding weighted identity is `+1.18435`, giving the negative total because the weighted boundary term is zero. The unweighted total is zero in **both** cases. Under the separately hypothesized normalized incidence/self-location rule, the corresponding whole-interval means are zero for A and `−0.03α` for B; neither is an actual prediction of human or cosmic experience.

The contrast is specific: **same physical electromagnetic fields and same marker initially, but different transport and incidence laws**. It demonstrates what the energy-locking condition does and why conserved subject-like flow alone does not suffice. It does not decide which flow, if either, describes actual subjects.

## 4. Numerical verification and limits

We evolved the marker and `N` for A with fourth-order periodic differences and RK4. For a full cycle, all three grids give a weighted exchange near floating-point roundoff, whereas B reproduces `−1.18435252813`. This full-cycle cancellation is aided by the special time-reversal structure of the prescribed fields; near-roundoff values are **not** evidence of general numerical constraint convergence.

A partial interval `0≤t≤1.1` provides a nontrivial test: the energy-locked weighted exchange is about `−0.35954`, matching the *nonzero* change of weighted field energy. Its discrete residual decreases at approximately fourth order:

| Grid | Energy-locked exchange | Balance residual |
|---:|---:|---:|
| 64 | `−0.3595516` | `−2.46e−5` |
| 128 | `−0.3595431` | `−1.54e−6` |
| 256 | `−0.3595425` | `−9.66e−8` |

On the 256-grid full cycle, sampled `N` remained above `0.4305`, sampled `χ` above `0.6000`, and the sampled energy-flow speed below `0.3846`. These are sampled numerical checks, not a proof of all-time positivity between samples or of a more general continuum result. The conservation of integrated `N` follows from the matched periodic discrete derivative; the smooth partial-interval residual supplies the more meaningful convergence control. The [receipt](verification/energy_flow_locked_incidence_receipt.json) records the full data.

## 5. What remains to derive

The construction offers a definite candidate for integrating physical dynamics, organizational incidence and zero signed history balance. Its remaining obligations are substantial:

- **Identify the energy current:** electromagnetic field energy is only a part of physical energy. The chosen field-plus-source model has positive field energy and does not establish a whole-level zero physical energy.
- **Derive incidence and organization:** `K` and `χ` are mathematically constructed auxiliary fields, not demonstrated subjects or experience. The source current has no derived matter dynamics, and a biological subject is not generally expected to move with Poynting flux.
- **Derive the physical–experiential identity:** `v_X=αh/N` is a proposed mapping with no independently established sign, phenomenal scale, or subject unity. Positive and negative values do not erase actual suffering.
- **Derive the relevant boundary:** the example's periodic source and returning marker make a closed cycle by construction. Whole-history boundary conditions cannot be chosen solely to secure zero.
- **Handle spacetime and statistics:** the flat inertial field is not an emergent-spacetime derivation. Curvature and observer-deformation terms, quantum dynamics, and the relationship between physical incidence, self-location credence and observed frequencies remain unresolved.
- **Meet the no-residue demand:** all these ingredients must ultimately be explained through the self-subsistent whole's constitution; this calculation does not treat their present stipulation as a final account.

The concrete next challenge is therefore not simply to find another zero integral. It is to determine whether a physically derived **subject-organizing current** aligns with a defensible whole-energy flow, or whether a different constitutive relation produces the necessary balance without that demanding alignment. The result also leaves room for a non-additive zero-totality account if the additive construction proves inadequate.

## Reproduction

With NumPy available:

```text
python -m verification.energy_flow_locked_incidence --grids 64 128 256
python -m unittest verification.energy_flow_locked_incidence_test -v
```

Tests check the specified Maxwell and Poynting identities, full-cycle and partial-interval weighted accounting, conserved auxiliary incidence, sampled bounds, and the null-field restriction. They do not establish actual experience, empirical subject identity, a gravitational solution or self-subsistence.
