# Scalar lattice regulators: the exact finite scheme difference

## Result

**Follow-up:** The [continuum proper-time gate](OTTINGER_SCALAR_CONTINUUM_EXPLICIT_GATE.md) derives an infinite-volume limit and its interchange with this proper-time cutoff, plus an explicit finite continuum integral. It does not address the source's dissipation or sharp-cutoff limits.

Under the assumptions and proper-time convergence argument of the [previous scalar lattice gate](OTTINGER_SCALAR_LATTICE_TIME_REGULATOR_GATE.md), the difference between its two regulated versions of Öttinger’s sum has a definite limit. For a periodic cube of side `L>0`, mass `m>0`, lattice external momentum `k∈(2π/L)Z³`, and the **raw momentum sums** defined below,

```text
lim_{ε→0+} [S_exp(ε) − S_time(ε)] = 3 L⁶ |k|²/(128 π⁴).       (1)
```

Consequently **both prescribed sums converge** as `ε→0+`, and their limits differ by the displayed finite local term. After dividing the raw sums by the conventional `V²=L⁶`, the coefficient is `3|k|²/(128π⁴)`, independent of fixed `L` and `m`.

This derives a specific relationship between two artificial regulators; it does **not** prove convergence of the book’s sharp mode cutoff, identify either scheme with its finite-friction prescription, or establish an interacting continuum theory. The analytic calculation rests on the kernel estimates and convergence proof in the previous note and has not been independently peer reviewed. The finite numerical checks below are not a proof of its limit.

## 1. The exact difference

Let `ω_p=√(m²+|p|²)`, `Ω=ω_p+ω_q+ω_r`, and

```text
A_0(t) = Σ_{p+q+r=0} exp(−tΩ)/(ω_p ω_q ω_r),
a_0(t) = A_0(t)/L⁶,          t>0.
```

`S_time` is the integral from `t=ε` of the grouped heat-kernel integrand. `S_exp` instead multiplies the unmodified summands in the book’s eq. (2.51) by `exp(−εΩ)`. Their definitions and the finite-`ε` identity are in the previous note. With `D(ε)=S_exp(ε)−S_time(ε)`,

```text
D(ε)/L⁶ = |k|² Σ_{p+q+r=0} exp(−εΩ)/(L⁶ ω_p ω_q ω_r)
                  · [ε/Ω² + ε²/(2Ω)].                       (2)
```

All terms are nonnegative. Using the elementary Laplace identities

```text
exp(−εΩ)/Ω² = ∫_ε^∞ (t−ε) exp(−tΩ) dt,
exp(−εΩ)/Ω  = ∫_ε^∞ exp(−tΩ) dt,
```

and Tonelli’s theorem for these positive sums gives

```text
D(ε)/(L⁶ |k|²) = ε ∫_ε^∞ (t−ε)a_0(t) dt
                   + ε²/2 ∫_ε^∞ a_0(t) dt.                (3)
```

The division by `|k|²` is only for `k≠0`; the original identity gives `D=0` for `k=0`.

## 2. Short-time coefficient

The previous note defines the periodic kernel

```text
G(t,x) = L⁻³ Σ_p [exp(−tω_p)/ω_p] exp(i p·x),
a_0(t) = ∫_{T³_L} G(t,x)³ d³x.
```

At distances much smaller than `L` and `m⁻¹`,

```text
G(t,x) = 1/[2π²(t²+|x|²)] + O(1+|log √(t²+|x|²)|).
```

Nonzero periodic images are smooth near the origin, because `m>0`. Rescaling `x=t y` in a small fixed ball and using dominated convergence gives

```text
lim_{t→0+} t³ a_0(t)
  = (1/(2π²))³ ∫_{R³} d³y/(1+|y|²)³
  = (1/(2π²))³ · π²/4
  = 1/(32π⁴) ≡ c₀.                                       (4)
```

For the domination, the previous local kernel estimate bounds `|G|` by a constant times `(t²+|x|²)⁻¹` in a fixed neighborhood; after rescaling, the dominating function is proportional to `(1+|y|²)⁻³`. The integral outside that neighborhood is uniformly bounded in `t`, so its contribution to `t³a₀(t)` vanishes. The radial integral is `4π ∫₀∞ r²/(1+r²)³ dr=π²/4`.

Moreover `t³a₀(t)` is bounded for all `t>0`: the same local estimate gives a bound near zero, while the mass gap gives exponential decay at infinity. These statements are for fixed positive `m` and `L`; they do not assert uniform bounds as either parameter changes.

## 3. Removal of the regulator

Substitute `t=εu` in (3):

```text
D(ε)/(L⁶ |k|²)
 = ∫₁∞ [(u−1)/u³ + 1/(2u³)] · [(εu)³ a₀(εu)] du.       (5)
```

The bracketed kernel is bounded uniformly in `ε,u` by §2, and the displayed nonnegative weight is integrable on `[1,∞)`. Dominated convergence and (4) therefore give

```text
lim D(ε)/(L⁶ |k|²)
  = c₀ [∫₁∞ (u−1)/u³ du + (1/2)∫₁∞ du/u³]
  = c₀ (1/2 + 1/4)
  = 3/(128π⁴).                                            (6)
```

This proves (1). In the same conventions as the previous note, the latter’s convergence of `S_time` and (6) together prove convergence of `S_exp`. If one chooses to match the two schemes, the explicit finite subtraction is `−3L⁶|k|²/(128π⁴)` applied to `S_exp`. This is a scheme-matching term, not a derived physical renormalization condition. It does not decide which value is appropriate for an observable or for the book’s dissipative regulator.

When `h=2π/L=1` and `|k|²=1`, the raw gap limit is `3π²/2 ≈ 14.8044066`. The dimensionless raw value is larger than the `V⁻²`-normalized value because `L⁶=(2π)⁶` in this particular example.

## 4. Independent finite-mode checks

[The verifier](verification/ottinger_scalar_universal_gap.py) calculates the gap by an independent route: at each `t`, an FFT computes the zero-momentum triple convolution on a finite cube `|p_i|≤N`, and Gauss–Legendre quadrature integrates after setting `z=ε/t`:

```text
D_N(ε)/|k|² = ∫₀¹ (1−z/2) (ε/z)³ A_{0,N}(ε/z) dz.         (7)
```

The FFT array has side `3N+1`; since the sum of three cube momenta lies between `−3N` and `3N` in each coordinate, no nonzero momentum sum aliases into zero. The independent finite-mode test compares the FFT against direct triple enumeration and (7) against the closed-form sum used in the earlier verifier. A numerical radial integral and the coefficient `3/4` are also checked. All use floating-point arithmetic.

[Recorded samples](verification/ottinger_scalar_universal_gap.json), `m=h=1`, `|k|²=1`, with `32` quadrature points:

| `ε` | `N` | finite-mode gap |
|---:|---:|---:|
| 0.5 | 8 / 20 | 1.513318 / 1.514490 |
| 0.25 | 12 / 32 | 4.211649 / 4.228080 |
| 0.125 | 20 / 48 | 7.414564 / 7.475361 |

These values are not expected to equal the limiting `14.8044` at finite `ε`. Decreasing `ε` requires larger `N` to resolve the ultraviolet tail. The observed progression is consistent with, but does not establish, the derived limit; the tables give neither rigorous quadrature errors nor bounds on mode-tail errors. As an additional diagnostic, finite-mode values of `t³ A₀(t)` at `(t,N)=(0.5,20), (0.25,36), (0.125,64)` are approximately `7.0810, 13.1023, 16.9599`, respectively, versus the raw short-time coefficient `2π²≈19.7392`. These too are truncated calculations rather than certified error estimates.

Reproduce with NumPy installed:

```text
PYTHONPATH=verification python -m unittest ottinger_scalar_universal_gap_test
python verification/ottinger_scalar_universal_gap.py
```

## 5. What remains open

1. Determine whether Öttinger’s original sharp individual-mode cutoff converges and what finite matching term relates it to either prescription. The above result does not show cutoff-shape independence.
2. Establish the actual finite-dissipation/zero-dissipation and volume-limit relationship under the source’s dynamics. The common exponential here is an analytically defined comparison, not the source’s `γ|k|⁴` dissipation.
3. These are low-order scalar manipulations, not a proof of positivity, relativistic microcausality, BRST consistency, experimental adequacy or experiential constitution. The [full-book audit](OTTINGER_FULL_BOOK_SCALAR_QED_FOLLOWUP.md) and current framework status retain those distinctions.
