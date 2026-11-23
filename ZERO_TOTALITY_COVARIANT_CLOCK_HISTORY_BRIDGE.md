# A covariant clock–current history balance

## The constructive result

The [zero-energy research](ZERO_ENERGY_UNIVERSE_DEEP_RESEARCH.md) clarified that a vanishing gravitational Hamiltonian constraint, zero gauge charge, and a possible zero experiential total are not the same quantity. The [existing coupled model](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md) already has a conserved gauge current and a dynamical scalar clock. Here is a more precise way to connect those two ingredients.

On a spacetime region with a suitable clock field `T` and conserved current `J`, define the scalar

```text
B(x) = J^μ ∇_μ T.
```

For a compact boundaryless universe with zero integrated gauge charge, the spacetime integral of `B` over **any regular complete clock interval** vanishes exactly. Local `B` can nevertheless have both signs and evolve. This is a new conditional result for the existing candidate: it extends a zero on spatial slices to a **duration-weighted four-dimensional history** without treating coordinate time as fundamental.

The proposed experiential bridge is now sharper: an actual signed experiential intensity *might* be proportional to `B`, with a common physical conversion factor and a justified incidence measure. But the physical derivation does not establish that `B` is felt valence, that all regions carrying it are subjects, or that the required clock and measure are constitutive. Nor does it equate gauge charge with total physical energy. This remains a candidate, not a solved experiential or foundational identity.

The calculation also exposes an important restriction: arbitrary subject-incidence weighting generally **destroys** the zero. In the existing nonlinear simulation a particular nonuniform weight produces a nonzero result even though the unweighted whole charge is near zero. That is a specific test the bridge must meet, not a reason to discard the zero-totality programme.

## 1. Definitions and derivation

Use the action, sign convention and charged scalar in the [covariant candidate](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md), with signature `(-,+,+,+)`. Let `J^μ` be its gauge-invariant conserved electric-type current,

```text
∇_μ J^μ = 0.
```

Suppose the scalar clock `T` is smooth, has a timelike gradient in a regular region, and increases along future-directed timelike curves (so the raised gradient `∇^μT` is past-directed in our signature). Suppose its levels `Σ_T` are compact Cauchy slices with no spatial boundary. Define

```text
s = sqrt(-∇_μ T ∇^μ T) > 0,
n_μ = - ∇_μ T / s,                ρ_T = -n_μ J^μ,
B = s ρ_T = J^μ ∇_μ T.
```

Here `n` is the future unit normal to the clock slices. `ρ_T` is the signed charge density measured by these clock-normal observers; `s=n^μ∇_μT` is the rate at which the scalar clock changes per unit of their proper time. Both geometry and clock are dynamical fields in the model. The expression `B` is a scalar under spacetime coordinate changes and gauge invariant. Its sign at a point agrees with `ρ_T`, because `s>0`.

Let `D` be the four-dimensional slab bounded by the complete level surfaces `T=T₁` and `T=T₂`, with `T₂>T₁`. The covariant volume decomposes as `dV₄=dT dΣ_T/s`. Therefore

```text
I_B(D) = ∫_D B dV₄
       = ∫_(T₁)^(T₂) dT ∫_(Σ_T) ρ_T dΣ_T
       = (T₂-T₁) Q.
```

`Q` is the flux of `J` across a complete clock slice. Current conservation makes it slice-independent under the stated regularity and boundary conditions. Gauss's law for the model gives `Q=0` on compact boundaryless slices, so

```text
I_B(D) = 0,   even when B(x) is locally nonzero and changes over time.
```

Equivalently, current conservation gives the local identity

```text
J^μ ∇_μT = ∇_μ(T J^μ).
```

The four-dimensional divergence theorem gives the upper-minus-lower boundary flux `(T₂-T₁)Q`. Both derivations rely on a **complete slab** and no lateral boundary flux. Regional subdomains have a lateral flux term and need not balance. For charge-flux and hypersurface-decomposition background see Bini, Germani and Jantzen, [*Gravitoelectromagnetism and the Integral Formulation of Maxwell's Equations*](https://arxiv.org/abs/gr-qc/0012068); the result here is our application, not a claim those authors proposed an experiential identity.

### What is—and is not—clock independence

This is coordinate covariant, and the physical clock field specifies the normal rather than an arbitrarily chosen slicing. It does not establish a unique clock from first principles: the candidate includes a real clock field whose particular solutions select a physical congruence. It is not an assertion of a fundamental preferred foliation, but neither is selecting that field physically vacuous.

Changing coordinates while retaining the *same physical field and measure* does not change `B dV₄`. Replacing `T` in the bridge by another physical clock is a new identification, not a mere coordinate change. In particular, if `T'=f(T)` is increasing and one **redefines the bridge** as `B'=J·∇T'=f'(T)B`, local intensities change, although the complete-slab zero still follows since `∫f'(T)Q dT=0`. A physical clock unit and common conversion factor are thus necessary for a quantitative experiential claim. A mere relabeling of the same physical measure instead includes the appropriate Jacobian and does not change the actual intensity. Nonlinear redefinitions need not preserve the clock's free-scalar equation, either.

The theorem applies to a regular finite slab. It says nothing by itself about regions outside the clock patch, singularities, a complete subject's actual lifetime, noncompact boundaries, quantum histories or the convergence of a putative whole-history integral. A zero on each admissible finite complete slab is strong, but it is not a proof that the actual complete experiential domain is such a slab.

## 2. Why the rate factor matters

The earlier tentative bridge used `ρ_T` itself. Its proper-spacetime-volume integral is

```text
∫_D ρ_T dV₄ = ∫ dT ∫_(Σ_T) (ρ_T/s) dΣ_T.
```

Because `s` can vary across a slice, zero `∫ρ_T dΣ_T` does not generally make the right-hand side zero. The candidate `B=sρ_T` is not just a change of notation; it is a **different local intensity hypothesis**. It obtains a four-dimensional balance by using the actual local clock rate as a weight.

A transparent counterexample uses a flat two-dimensional cylinder with `x` periodic, interpreted only as a conserved-current/clock example:

```text
J^t = cos(2x),  J^x = 0,       T = t + 0.6 sin(x),
s = sqrt(1 - 0.36 cos²x),      ρ_T = cos(2x)/s.
```

The clock is timelike, current is conserved, and total charge is zero. Over `0<=T<=1` and one spatial period,

```text
∫ ρ_T dV₂ ≈ +0.389660532,       ∫ sρ_T dV₂ = ∫ cos(2x) dT dx = 0.
```

The former result is nonzero despite a zero charge on every complete clock slice. This toy current is not asserted to solve the complete Einstein–matter field system; it isolates the conservation and clock-measure issue. It also shows why it would be incorrect to infer the history balance directly from the previous unmodified bridge.

## 3. Test against the existing coupled nonlinear solution

The [planar gravity–gauge–clock solver](verification/evolve_covariant_zero_initial_data.py) evolves the prior coupled initial data with `κ=0.02`. Here a separate analysis reconstructs surfaces of constant `T` by linearly interpolating between time steps at each spatial point. All selected clock levels lie strictly between the maximum initial T and the minimum final T, so each grid point crosses them. The code checks sampled timelikeness and forward clock rate; this is not a proof between samples.

In the solver's coordinates, put `q=√(-g) J^t`, `j=√(-g) J^x`. The flux density on a tilted constant-clock slice is

```text
q_T = q + j T_x/T_t.
```

The second term is essential: just summing the coordinate-time density `q` on a tilted surface is generally wrong. A separate analytic conserved-current test produces an exact zero for the correct tilted integral and approximately `0.79346` when the tilt term is omitted.

For the 256-point coupled evolution, integrating over the full three-torus, in the model's normalized units:

| Clock reading T | Whole current flux Q | Range of local slice-flux density | Tilt-term RMS |
|---:|---:|---:|---:|
| 0.3 | `1.11e-14` | `[-0.817, +0.817]` | `0.0844` |
| 0.6 | `3.77e-15` | `[-0.609, +0.609]` | `0.0873` |
| 1.0 | `-8.70e-15` | `[-0.297, +0.297]` | `0.0309` |

This exhibits nonzero positive and negative local contributions on dynamically reconstructed clock slices. The net is near roundoff **partly because this initial state has an exact half-period sign symmetry**, not because the computation independently proves general constraint propagation to roundoff. The underlying fourth-order constraint convergence and sampled clock timelikeness were checked separately in the [evolution report](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md). Linear clock-crossing interpolation is only second-order accurate, and the three selected clock levels are samples, not a numerical integration over all clock readings. The continuum divergence theorem above supplies the interval result under its assumptions.

In this unusually symmetric run, even the integrated unscaled `ρ_T` happens to vanish numerically; this is not the generic theorem, as the counterexample in section 2 shows. The slice code records both quantities to make the distinction visible.

## 4. Actual incidence is the decisive bridge condition

Suppose a nonnegative scalar weight `w(x)` represents a proposed local density of actual subject incidences, allocation across overlapping subjects, or an experiential calibration. If one simply multiplies the physical candidate by it, the total becomes

```text
I_w = ∫_D w J^μ∇_μT dV₄,
∇_μ(wJ^μ) = J^μ∇_μw.
```

Unless `w` is constant along the current in the appropriate sense, the weighted current need not be conserved. The unweighted charge theorem alone therefore gives **no guarantee** that `I_w=0`.

A concrete counterexample follows already in section 2: take `w=1+0.5 cos(2x)>0`. Over the same slab,

```text
∫ w B dV₂ = π/2,      although ∫ B dV₂ = 0.
```

In the nonlinear gravity run, a purely illustrative coordinate-grid weight `w=1+0.5 cos(x)` gives weighted slice integrands approximately `58.22`, `43.40` and `15.65` at `T=0.3, 0.6, 1.0`, while the unweighted whole flux is near zero. This weight is **not** claimed to be a covariantly constructed subject field or an observed distribution; it is an explicit test showing that incidence cannot be inserted freely after the fact. The dependence on the chosen weight is not evidence of actual net experience.

A successful bridge must therefore do at least one of the following, with independent justification rather than tuning:

- establish that the relevant actual-incidence measure counts the physical current exactly once over its complete support;
- derive a separate **conserved experiential current** `J_X` whose actual incidence and signed contents are determined by the underlying constitution;
- derive justified compensating flux/source or boundary terms for the weighted subject domain; or
- replace the additive current proposal with another well-defined composition principle.

The first option cannot quietly count non-experiential charge as felt experience. Nor can it assume a cosmic subject: a field with local contributions might support multiple distinct subjects, but the incidence and unity laws must establish that. Positive and negative contributions to a total do not undo or excuse actual pain.

## 5. Physical and experiential predictions of the candidate

If, and only if, actual signed valence intensity per proper four-volume is `v_X=αB` with one independently fixed constant `α`, the model predicts:

1. The properly measured total over every **complete regular clock slab** is zero, not merely over a final lifetime. This is a strong empirical and constitutive requirement, not something inferred from observed individual pain and pleasure.
2. For a regional domain, the history integral is a boundary-flux quantity. Regional imbalance is allowed and must be accounted for by the clock-weighted current crossing the boundary and/or charges on its initial and final pieces.
3. Local sign follows the clock-frame charge density, while intensity also scales with the clock rate `s`. Two otherwise similar experiences with different clock-rate factors would be assigned different intensity by this precise bridge. A mismatch with independently calibrated valence and measured field/current would challenge it.
4. Charge conjugation reverses `B` with the same geometry and clock in the charge-symmetric classical model. Physics alone does not fix which orientation is pleasure and which is suffering; the orientation and common experiential units need independent grounding.

No measured hidden current, subject-incidence law, coupling to brains, common phenomenal scale or nonlocal aggregation has been established. Also, a proper four-volume integral is not automatically the earlier **sum of subject intensities over their own proper times**: deriving the spatial weighting and avoiding double counting are essential. The model currently provides a structural target and falsifiable conditional restrictions, not evidence that gauge charge is experience.

## 6. Connection to zero energy and self-subsistence

The model now contains two calculable but distinct zeros: the Einstein Hamiltonian constraint and the clock-weighted gauge-current history integral. The latter depends on Gauss neutrality, a regular clock and complete domain; neither quantity is automatically a global physical energy or an actual experiential balance. The new derivation narrows how an energy–experience bridge could work: if an eventual deeper theory unifies these quantities, it must explain their relation, the sign and scale of valence, the matter action and the actual organization together, without adding an unexplained balancing agent.

A further open problem is whether a genuinely experiential current can be derived from an intrinsic constitutive organization rather than assigned by hand, and whether its nonzero local values correspond to real differentiated subjects. The present result does not settle those questions or claim zero-residue performance; it specifies a path and a concrete obstruction for the next construction. It does not reopen the user's settled case against infinity.

## Reproduction

```text
python -m verification.covariant_clock_history_balance --grids 64 128 256
python -m unittest verification.covariant_clock_history_test -v
```

The [receipt](verification/covariant_clock_history_receipt.json) records the three-grid run. The tests include the coupled clock slices, nonuniform weights, the generic unscaled-density counterexample, a tilted-surface flux control, clock-rate rescaling and invalid-domain guards. They verify the declared physical/mathematical model, not conscious experience or its metaphysical identity.
