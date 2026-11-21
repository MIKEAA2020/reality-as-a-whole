# Scalar proper-time gate: infinite volume and an explicit continuum integral

## Result

For the **specific grouped proper-time prescription** analyzed in the [finite-volume lattice gate](OTTINGER_SCALAR_LATTICE_TIME_REGULATOR_GATE.md), the volume-normalized massive scalar expression has a controlled infinite-volume limit. Its spatial-volume and proper-time-cutoff limits commute under the conditions below. In the resulting continuum expression, the finite `k²` term is absent and the result is strictly negative for nonzero momentum; at small momentum it starts at order `k⁴`.

This is a conditional result for a selected second-order, zero-friction scalar expression. It does **not** prove convergence of Öttinger’s original sharp momentum cutoff, interchange a dissipation limit, or establish full interacting QFT. In particular, the [common-exponential prescription](OTTINGER_SCALAR_REGULATOR_UNIVERSAL_GAP.md) gives a different finite `k²` term. The estimates and calculations below have not undergone independent mathematical review.

## 1. Definitions and a limit statement

Use `ω_p=√(m²+|p|²)` with fixed `m>0`, a cubic periodic box `V=L³`, and the raw sums `S_time^{L,k}(ε)` defined in the finite-volume note. Let `k_n∈(2π/L_n)Z³`, with `L_n→∞` and `k_n→k∈R³`. This permits arbitrary fixed continuum `k` by choosing compatible lattice approximants; in special directions one can also use exactly the same `k` at every `L_n`.

Define the infinite-space kernel

```text
g(t,x) = m K₁(mR)/(2π²R),     R=√(t²+|x|²),   t>0,
F_k(t,x) = 1 − cos(k·x) − |k|²t²/2,
C_ε(k) = ∫_ε^∞ dt ∫_{R³} d³x g(t,x)³ F_k(t,x).           (1)
```

The finite-lattice expression normalized by `L⁶=V²` equals the same integral over the box using the periodic kernel `G_L(t,x)=Σ_{n∈Z³}g(t,x+nL)`. At every `ε>0`, the integrals and Fourier sums are well-defined. Set `C(k)=lim_{ε→0+} C_ε(k)` with the space integral taken first.

**Claim.** For fixed positive `m` and any bounded sequence `k_n→k` as above,

```text
lim_{n→∞} lim_{ε→0+} S_time^{L_n,k_n}(ε)/L_n⁶
 = lim_{ε→0+} lim_{n→∞} S_time^{L_n,k_n}(ε)/L_n⁶
 = C(k).                                                    (2)
```

This is **volume versus this proper-time cutoff**, not volume versus Öttinger’s friction parameter `γ`. No assertion is made for `m→0` or a uniform range of external momenta growing with `L`.

## 2. Why volume and proper-time removal commute here

Take a centered fundamental cube and split `G_L=g+H_L`, where `H_L` is the sum of nonzero spatial images. Each nonzero image is at least `L/2` from every point of the cube. The standard exponential large-argument decay of `K₁`, together with `√(t²+r²)≥(t+r)/√2`, gives constants depending on `m` and a chosen `L₀>0` such that for `L≥L₀`,

```text
0 ≤ H_L(t,x) ≤ C exp(−cL) exp(−ct)          (x in the cube).  (3)
```

The sum over images is controlled by the exponential in their lattice distance. Expanding the cube, the diagonal terms `Σ_j g(t,x+jL)³` unfold to the integral over all `R³`: since `k_n` is a lattice momentum, `F_{k_n}(t,x+jL)=F_{k_n}(t,x)`.

Only mixed-image terms remain. They are nonnegative before multiplication by `F`, and are bounded by

```text
3g²H_L + 3gH_L² + H_L³.
```

Use `|F_{k_n}(t,x)| ≤ K²(t²+|x|²)/2` for a fixed bound `|k_n|≤K`. The singular `g²F` term is integrable near `(t,x)=0`: `g²=O(R⁻⁴)` and `F=O(R²)`, while the four-dimensional measure is `O(R³ dR)`. Its tail is integrable by the mass gap. The term with `gH²` is likewise integrable; the `H³` term can be bounded by the finite box volume and a polynomial in `L` times the exponential. Hence, uniformly for **all** `ε≥0` at which the grouped integrals are defined,

```text
|S_time^{L,k_n}(ε)/L⁶ − C_ε(k_n)| ≤ C_K (1+L⁵) exp(−cL).  (4)
```

The right-hand side tends to zero. The existence of `C(k)`, continuity in bounded `k`, and removal of its cutoff follow from the explicit representation in §3. Thus taking the two limits in either order yields (2). This argument applies to this periodic geometry, massive kernel, grouped subtraction and volume normalization; it is not a general theorem about a dissipative instrument or its local observables.

## 3. A manifestly finite Euclidean representation

Let `X=(t,x)∈R⁴` and `g(R)=mK₁(mR)/(2π²R)`. The potentially non-integrable quadratic part of (1) is proportional to

```text
Q(t,x) = [(k·x)² − |k|²t²]/2.
```

Its four-dimensional angular average is zero. To justify using that cancellation with a time-slab cutoff, isolate the leading singular kernel `1/(2π²R²)³` with a smooth **radial** cutoff equal to 1 near the origin. For every `t>0`, the spatial integral of `Q/R⁶` over all `R³` is exactly zero, as established in the finite-volume note. The complement of the radial cutoff is bounded away from `R=0`, and its integral over `0<t<ε` is `O(ε)`. Thus the time-slab and radial regularizations have the same limit for the leading quadratic piece; its radial angular integral is zero. The remaining kernel correction is absolutely integrable against `Q`, and is likewise killed by angular symmetry. This yields

```text
C(k) = 1/2 ∫_{R⁴} d⁴X g(|X|)³
                  · [1 − cos(k·x) − (k·x)²/2].             (5)
```

The integral in (5) is absolutely convergent: the bracket is `O(|k·x|⁴)` at the origin, while `g³=O(R⁻⁶)`; the mass gives exponential decay at infinity. The half accounts for `t≥0`, since the integrand is even in `t`.

Averaging over the 3-sphere, `⟨cos(k·x)⟩=2J₁(z)/z` and `⟨(k·x)²/2⟩=z²/8`, where `z=|k|R`. Therefore

```text
C(k) = m³/(8π⁴) ∫₀∞ K₁(mR)³
                  · [1 − 2J₁(|k|R)/(|k|R) − |k|²R²/8] dR.   (6)
```

The bracket is interpreted by continuity as zero at `k=0`. The unaveraged bracket in (5) is nonpositive by `1−cos v≤v²/2`, strictly negative whenever `v≠0`. Because `g>0` for `R>0`, **`C(k)<0` for every nonzero `k`**, and `C(0)=0`.

## 4. Small-momentum coefficient and a bound

Taylor’s theorem gives

```text
|1−cos v−v²/2 + v⁴/24| ≤ |v|⁶/720.
```

The four-dimensional angular moments are `⟨x₁⁴⟩=R⁴/8` and `⟨x₁⁶⟩=5R⁶/64`. Consequently, for all `k∈R³` and `m>0`,

```text
| C(k) + c₄ |k|⁴/m² | ≤ c₆ |k|⁶/m⁴,
c₄ = [∫₀∞ u⁴ K₁(u)³ du] / (1536 π⁴),
c₆ = [∫₀∞ u⁶ K₁(u)³ du] / (73728 π⁴).                  (7)
```

Both integrals are finite and positive. The small-`k` conclusion follows from a dominated-integral argument; it is not inferred just from sampled points. Numerical quadrature estimates `c₄≈2.4125816443×10⁻⁶` and `c₆≈6.157363732×10⁻⁸`. These are approximations, not certified error bounds on the constants; the analytic bound uses the integral-defined `c₆`.

For comparison, the exact [regulator-gap result](OTTINGER_SCALAR_REGULATOR_UNIVERSAL_GAP.md) implies that the volume-normalized common-exponential scheme tends to

```text
C_exp(k) = C(k) + 3|k|²/(128π⁴),                           (8)
```

with `ε` removed at finite volume before the volume limit. The difference is a finite local `k²` term. Its cancellation or retention in a physical observable depends on the chosen matching/renormalization conditions; the integral alone does not specify those conditions.

## 5. Checks, integration, and remaining work

[The verifier](verification/ottinger_scalar_continuum.py) evaluates (6) and (7) numerically using `mpmath` at 25 decimal digits. It uses a power series for the small-argument Bessel bracket to avoid catastrophic cancellation. For `m=1`, the samples are `C(0.5)≈−1.4983433×10⁻⁷`, `C(1)≈−2.3534874×10⁻⁶`, and `C(2)≈−3.5213292×10⁻⁵`; each satisfies the integral-defined sixth-order bound. [JSON results](verification/ottinger_scalar_continuum.json) and four tests include an independent one-dimensional angular average, a small-argument check, positivity/sign and the remainder inequality. Numerical integration checks do not prove the analytic limit or certify their own error.

```text
PYTHONPATH=verification python -m unittest ottinger_scalar_continuum_test
python verification/ottinger_scalar_continuum.py
```

Both commands require `mpmath`. Further decisive work is still to establish the **original sharp individual-mode cutoff** and its matching to (6), and separately relate either prescription to the source’s finite-dissipation evolution. The result does not transfer [reversible instrument bounds](CUTOFF_INSTRUMENT_UNIFORMITY.md) to nonlinear interacting dynamics, and it does not address experiential constitution or the full framework’s open criteria. See the [full-book audit](OTTINGER_FULL_BOOK_SCALAR_QED_FOLLOWUP.md) for those boundaries.
