# Sharper cutoff certificate for the 3+1 field–probe model

## Result and qualification

The [earlier 3+1 certificate](THREE_DIMENSIONAL_QUANTITATIVE_CHANNEL_CERTIFICATE.md) gave a very loose `O(N⁻¹/¹²)` sufficient interaction-channel bound. By using spatial smoothness more carefully in its pair-block estimate **and optimizing the energy projection**, I obtain a conditional improved asymptotic rate `O(N⁻¹/⁶)` for the same restricted model.

At its illustrative dimensionless parameters `E=100`, `λ=1`, the resulting floating-point bound for the **interaction channel only** falls below `.01` at the round cutoff `N=10⁸⁰`, versus `10⁷²⁹` for the previous simple sufficient formula. This is a reduction in an extremely loose **upper-bound certificate**, not a reduction in a known necessary physical cutoff: `10⁸⁰` is still completely impractical. The earlier, unreviewed nonperturbative Bogoliubov and channel arguments remain assumptions of this refinement; the improved algebra does not independently validate them. The bump integrals are numerical, not interval-certified. Source/readout errors, apparatus work and gravity are additional.

The technique uses standard Fourier/Sobolev tail bounds and energy-constrained channel methods, not a new theorem in Fourier analysis or quantum information; compare [Fourier-series and Sobolev notes](https://www.math.ucdavis.edu/~hunter/m201b/m201b_topics.pdf) and [energy-constrained Gaussian-channel analysis](https://arxiv.org/abs/1810.12335). The present application is a sharper estimate for this project's particular two-field primitive and a correction to how the earlier conservative numerical certificate should be interpreted.

## 1. Inherited setting

Retain all definitions and qualifications of the [nonperturbative model](THREE_DIMENSIONAL_COMPLETE_INSTRUMENT_CONTINUUM.md): two positive-mass free scalar fields on a compact three-torus with volume `V=(2π)³`, smooth real spatial coupling F, normalized smooth compact time switch χ, cubic cutoff `|k|∞≤N`, and a joint field–reference input with normal-ordered total field energy at most E. The illustrative masses are `m_A=.5`, `m_B=.7` and `m_*=.5`.

For one pair block, write Fourier coefficients `F_p=V⁻¹ ∫F(x)e^(−ip·x)dx` and frequencies `ω_X,k=√(|k|²+m_X²)`. Its frequency-sum primitive has entries of modulus

`|C_kl| = |F_{k+l}| / [2√(ω_A,k ω_B,l)(ω_A,k+ω_B,l)]`.

The factor `e^{i(ω_A,k+ω_B,l)t}` has unit modulus. The finite N primitive C_N keeps both modes in the cutoff. The other species block has the same Hilbert–Schmidt norm. Denote

```text
W = Σ_p |F_p|² = ||F||²₂ / V,
D = Σ_p |p|² |F_p|² = ||∇F||²₂ / V,
Z_X = m_X⁻⁴ + 4π² + π⁴/45,
T(q) = 24/q + 2/(3q³),      q ≥ 1.
```

The previously used cube-shell estimate gives `Σ_k ω_X,k⁻⁴≤Z_X` and `Σ_{|k|∞>q}ω_X,k⁻⁴≤T(q)`. Smooth F has finite D. Translation of the bump does not change W or D.

## 2. Momentum splitting: the improved primitive tail

Fix `N≥2` and `q=floor(N/2)`. Since `(ω_A+ω_B)² ≥ 4ω_Aω_B`,

```text
|C_kl|² ≤ |F_{k+l}|² / (16 ω_A,k² ω_B,l²).
```

Consider matrix elements omitted at cutoff N and split according to `p=k+l`:

1. **Low total momentum, `|p|∞≤q`.** If either `|k|∞>N` or `|l|∞>N`, both `|k|∞>q` and `|l|∞>q`. Cauchy–Schwarz over k, with `l=p−k`, bounds the inner sum by `√(T_A(q)T_B(q))≤T(q)`. Summing `|F_p|²` gives at most `W T(q)`.
2. **High total momentum, `|p|∞>q`.** Dropping the cutoff restriction and applying Cauchy–Schwarz gives an inner sum at most `√(Z_A Z_B)`. Parseval and `|p|²≥(q+1)²` give the remaining Fourier tail at most `D/(q+1)²`.

Thus, for the two off-diagonal species blocks together and uniformly in time,

```text
||C−C_N||²_HS ≤ [ W T(q) + D √(Z_A Z_B)/(q+1)² ] / 8.   (1)
```

For finite `M≥N`, `C_M−C_N` is supported within the same omitted matrix entries, so the same bound applies. No independence of k and l is assumed; the `p=k+l` split is what preserves their correlation.

For a simpler closed bound, `q≥N/3` and `q+1≥N/2` for integer `N≥2`, hence

```text
T(q) ≤ 76.5/N,
(q+1)⁻² ≤ 2/N,
||C−C_N||_HS ≤ d_new N⁻¹/²,
d_new = sqrt([76.5 W + 2 D √(Z_A Z_B)] / 8).                (2)
```

The old bound used the full `Z` sum for one factor at a time and gave `O(N⁻¹/⁴)`. The new bound need not be smaller at small N; either valid upper bound may be used. It concerns the **frequency-sum primitive**, not the instantaneous pair generator, which remains non-Hilbert–Schmidt in the relevant 3D continuum. Finite checks below are controls; the argument here is the basis for the estimate.

### Sharpness for this primitive, not for the channel

For the normalized product bump, `F₀=1/V`. The diagonal `l=−k` is part of the primitive tail. Define `c_X=√(3+m_X²)`; on a cube shell `|k|∞=n≥1`, `ω_X,k≤c_X n` and there are `24n²+2` points. Keeping just these terms in both species blocks and using `Σ_{n>N}n⁻²≥1/(N+1)` gives

```text
||C−C_N||²_HS ≥ 12 |F₀|² / [c_A c_B (c_A+c_B)² (N+1)].  (2a)
```

For these masses the square-root coefficient is about `.002073`. Thus this primitive's `N⁻¹/²` Hilbert–Schmidt tail rate is sharp up to constants when `F₀≠0`. This lower bound is **not** a lower bound on the full switched β block or channel error: oscillations and cancellations can make those converge faster. A finite-M diagonal lower control appears in the verifier.

## 3. Conditional propagation to the interaction channel

Use the earlier certificate's definitions `c,ν,h,d₀,Q,B_*,e₀` and its finite-cutoff integration-by-parts/Grönwall estimates, but replace its primitive-tail coefficient by `d_new` from (2). The exact same three terms then give, for `M≥N≥2`,

```text
I_new = |λ|[d_new ν Q + h e₀ Q + h |λ| d₀ ν ||χ||²₂],
dβ_new = ν[I_new + |λ| d₀ B_*],
a₀ = ν e₀,
b₀,new = ν dβ_new + B_* e₀,
a := ||α_rel−I|| ≤ a₀ N⁻¹/²,
b := ||β_rel||_HS ≤ b₀,new N⁻¹/².                         (3)
```

Here the relative transformation is the same `S_M⁻¹S_N` used in the earlier analysis. These inequalities and the following channel result are **conditional on** that analysis' operator-norm, Grönwall, implementer and energy-projection bounds; the new lattice estimate alone is not a full continuum proof.

The earlier energy projection, for any `R>0` and `k=floor(R/m_*)`, yields

`distance ≤ min{2, 2[b(k+2)+k(a+b²/2)] + 4√(E/R)}`.

Since `k≤R/m_*`, put `A=(a+b+b²/2)/m_*`. For `E>0` and `A>0`, taking

`R=(√E/A)^(2/3)`

gives the explicit upper bound

```text
min{2, 6(AE)^(1/3) + 4b}.                                  (4)
```

For E=0 the vacuum-sector choice gives `min{2,4b}`; zero coupling gives zero. As `N→∞` at fixed E and fixed finite λ, `a,b=O(N⁻¹/²)`, so (4) is `O(N⁻¹/⁶)`. The arbitrary-reference and energy-constrained interpretation is inherited from the earlier proof. This is not an unrestricted diamond-norm result or an assertion of optimal rate.

**Where the numerical gain comes from:** changing only the energy-projection choice, while retaining the old `N⁻¹/⁴` pair-block estimate, gives a round illustrative `.01` cutoff near `10¹⁶⁰`. The additional momentum-split tail estimate reduces that round sufficient example to `10⁸⁰`. Thus much of the gap from `10⁷²⁹` came from the deliberately weak earlier simplified coefficient, not from a physical effect.

## 4. Numbers and adversarial checks

For the earlier normalized product bump, numerical quadrature gives `W` as before and `D≈1.11848954`; 256- and 512-point Gauss–Legendre evaluations agree to about `1.2×10⁻¹⁴`. For `λ=1` the calculated coefficients are approximately `d_new=3.81497`, `a₀=2.598×10¹⁴`, `b₀,new=1.621×10²⁹`. These are floating-point approximations, not guaranteed upper enclosures.

| Round N | Optimized bound (4), `E=100` | Status |
|---|---:|---|
| `10⁷⁸` | `0.01913` | Above `.01` |
| `10⁷⁹` | `0.01303` | Above `.01` |
| `10⁸⁰` | `0.008880` | Below `.01` |

These comparisons only evaluate this sufficient upper bound; **they do not show** that `10⁸⁰` is the smallest sufficient N or that any smaller N fails. The cutoff is an index, not a physical length without further unit conversion. The estimate at `10⁸⁰` used an energy projection `R≈4.57×10⁷` in the model's dimensionless units; it is not the average input energy E or an apparatus-energy budget.

The [verifier](verification/three_dimensional_sharper_tail.py) evaluates (1) against independently summed finite `M=6` primitive entries for N=2,3,4,5, checks derivative quadrature convergence, reproduces the optimized arithmetic, and retains the previous shared-M weak-coupling ODE comparison. The sharper asymptotic bound is actually **larger** than the old one at these small N; its improvement is not claimed at every cutoff. The ODE control uses N=1, so it tests the **old** bound only, not the new N≥2 estimate. These checks neither establish an error bound for omitted `M>6` modes empirically nor certify the earlier infinite-dimensional proof.

The complete readout and the two source orders inherit this interaction term only after adding the separate source and readout tails from the prior report, including its source-first energy enlargement. Their sum has **not** been evaluated at `10⁸⁰` here. The result does not resolve independent review, an implementable local apparatus, total stress-energy, dynamical gravity, emergent spacetime, experience or necessity. It is nonetheless a concrete reduction of a named mathematical bottleneck without changing the model, the error criterion, or the target framework.

## Reproduction

Install `verification/requirements-field-probe.txt`, then run `python verification/three_dimensional_sharper_tail.py`. The [JSON receipt](verification/three_dimensional_sharper_tail.json) records both old and new numerical upper bounds and limitations. No huge Fock space, matrix or `10⁸⁰`-sized dataset is constructed.
