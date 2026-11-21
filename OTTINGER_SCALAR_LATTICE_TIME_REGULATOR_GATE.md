# Öttinger’s scalar lattice sum: a proper-time regulator gate

## Result and limitations

**Follow-up:** The [universal-gap calculation](OTTINGER_SCALAR_REGULATOR_UNIVERSAL_GAP.md) derives the exact limiting difference and establishes convergence of the common-exponential prescription as well. The [continuum proper-time gate](OTTINGER_SCALAR_CONTINUUM_EXPLICIT_GATE.md) then derives its infinite-volume grouped result and the volume/proper-time interchange. Statements below about what is not proved refer to this original gate in isolation.

For the massive three-dimensional finite-volume lattice in Öttinger’s eq. (2.51), a **specified proper-time regularization of the grouped expression has a finite cutoff-removal limit**. The argument below isolates the ultraviolet cancellation analytically; it is not a proof of the book’s original sharp momentum-cutoff limit or of a dissipative QFT. In fact, a seemingly innocuous alternative—multiplying the original summands by a common exponential—differs from our prescription by a positive amount bounded away from zero as the regulator is removed, for nonzero external momentum. The two prescriptions therefore cannot be identified without a finite counterterm or further analysis.

This advances the question identified on printed p. 125 of the [full-book audit](OTTINGER_FULL_BOOK_SCALAR_QED_FOLLOWUP.md) while leaving it open in its original form. The proof below is an analytic derivation under stated assumptions, not an independently peer-reviewed theorem or a consequence of the numerical tests.

## 1. Definition of the target and regulator

Fix a cubic periodic spatial box of side `L>0`, momentum lattice `Λ=(2π/L) Z³`, mass `m>0`, external `k∈Λ`, and `ω_p=√(m²+|p|²)`. Write `Ω=ω_p+ω_q+ω_r` and `δ_{p+q+r,k}` for the lattice constraint. Ignoring the book’s overall prefactors, its formal sum is

```text
S = Σ_{p,q,r∈Λ} 1/(ω_p ω_q ω_r)
      · [(δ_{p+q+r,0} − δ_{p+q+r,k})/Ω
         − |k|² δ_{p+q+r,0}/Ω³].                    (1)
```

This is eq. (2.51), with the book’s mass and lattice conventions. At finite momentum cutoff the **same individual-mode cutoff** is imposed on all three momenta in both terms. At infinite cutoff, (1) must not be treated as a difference of independently convergent sums.

For `t>0`, all the following sums converge absolutely:

```text
A_k(t) = Σ_{p+q+r=k} exp(−t Ω)/(ω_p ω_q ω_r).
S_time(ε) = ∫_ε^∞ [A_0(t) − A_k(t) − |k|² t² A_0(t)/2] dt,  ε>0.  (2)
```

Equivalently, in momentum space, the weights on the `δ₀` and `δₖ` terms are respectively

```text
exp(−εΩ) [1/Ω − |k|²(1/Ω³ + ε/Ω² + ε²/(2Ω))],
−exp(−εΩ)/Ω.                                                 (3)
```

The `ε/Ω²` and `ε²/(2Ω)` pieces are essential: they are what makes (2) the integral cut off at `t=ε`. They are **not** in the formal expression (1) at finite `ε`. At any fixed finite mode set they vanish as `ε→0`; this pointwise observation does not justify interchanging the two limits.

**Claim A.** For each fixed `L>0`, `m>0` and fixed lattice `k`, `lim_{ε→0+} S_time(ε)` exists and is finite. More precisely, for some constant depending on `L,m,k`, the difference from the limit is `O(ε)`. No uniformity in `L`, `m→0`, `k`, or any dissipative coefficient is claimed.

For `k=0`, (2) is identically zero. The remainder assumes fixed `k`, possibly nonzero.

## 2. Proof of Claim A

Define the periodic kernel

```text
G(t,x) = L⁻³ Σ_{p∈Λ} [exp(−t ω_p)/ω_p] exp(i p·x),  x∈T³_L.
```

The lattice is inversion-symmetric, so `G` is real. Absolute convergence at fixed `t>0` permits multiplication and Fourier inversion. Thus

```text
L⁻⁶ A_k(t) = ∫_{T³_L} G(t,x)³ cos(k·x) d³x,
L⁻⁶ S_time(ε) = ∫_ε^∞ dt ∫_{T³_L} d³x G(t,x)³
                       · [1 − cos(k·x) − |k|²t²/2].          (4)
```

Here `cos(k·x)` is a well-defined torus function because `k∈Λ`. The expression is integrated **first in space at fixed positive `t`**. We do not assert absolute convergence of the unsplit joint integral as `ε→0`.

### Local singularity

Let `R=√(t²+|x|²)`, with `x` chosen inside a ball around the origin contained in the fundamental cube. Poisson summation gives the periodization of the massive Euclidean kernel

```text
G_∞(t,x) = m K₁(mR)/(2π²R).
```

The zero image has `G_∞=c/R²+O(1+|log R|)` as `R→0`, where `c=1/(2π²)`. With `m>0`, nonzero images decay exponentially and are uniformly smooth in this ball. Hence

```text
G(t,x) = c/R² + O(1+|log R|),
G(t,x)³ = c³/R⁶ + O(R⁻⁴(1+|log R|))              (R→0).      (5)
```

The second estimate follows by expanding the cube and taking a sufficiently small neighborhood. The standard small- and large-argument properties of `K₁` are described in the NIST DLMF [power series](https://dlmf.nist.gov/10.31) and [large-argument asymptotics](https://dlmf.nist.gov/10.40). Away from the origin on the compact spatial torus the kernel is bounded as `t→0`; for large `t` the massive spectral gap gives exponential decay, even after the polynomial `t²` factor.

### Cancellation of the logarithmic singularity

Choose a smooth radial spatial cutoff `χ(x)` equal to 1 near zero and supported strictly inside the torus cell. Decompose the singular part of (4) using

```text
1 − cos(k·x) − |k|²t²/2
  = [(k·x)² − |k|²t²]/2 + O(|k|⁴ |x|⁴).                  (6)
```

For every `t>0`, rotational symmetry and elementary radial integrals give the exact identity

```text
∫_{R³} [(k·x)² − |k|²t²]/(t²+|x|²)³ d³x = 0,
∫_{R³} x_i²/(t²+|x|²)³ d³x = π²/(4t),
∫_{R³} t²/(t²+|x|²)³ d³x = π²/(4t).                     (7)
```

Consequently, the integral with `χ` is the negative of the integral with `1−χ` over `R³`. Its absolute value is bounded uniformly for `0<t<1`: on the support of `1−χ`, `|x|` stays away from zero, and the radial tail behaves as `|x|⁻² d|x|` or better. Thus the only potentially logarithmic term, the quadratic part of `χ c³/R⁶`, has a **bounded space-integrated value** as `t→0`.

The other terms are absolutely integrable near `(t,x)=(0,0)`. For example, the `O(R⁻⁴(1+|log R|))` correction multiplied by the quadratic bracket is at most `C R⁻²(1+|log R|)`, and the quartic cosine remainder multiplied by `R⁻⁶` is at most `C |x|⁴/R⁶`. Their spatial integrals are uniformly bounded for small `t` (split `|x|<t` and `t≤|x|<a`). The nonsingular part outside the cutoff ball is bounded. These estimates show that the **complete spatial integral in (4) is uniformly bounded near `t=0`**. Its integral over `0<t<ε` is therefore `O(ε)`, and the tail at large `t` is finite. This proves Claim A.

The cancellation uses the short-distance four-dimensional isotropy of the leading massive kernel, even though the spatial torus as a whole is not Euclidean-rotation invariant. It does not say the integrand is pointwise nonnegative, that the original double sum is absolutely convergent, or that a different regulator gives the same finite value.

## 3. The finite-regulator correction survives cutoff removal

Define the distinct common-exponential prescription by inserting `exp(−εΩ)` directly into **every** term of (1):

```text
S_exp(ε) = Σ exp(−εΩ)/(ω_p ω_q ω_r)
              · [(δ₀−δₖ)/Ω − |k|² δ₀/Ω³].                 (8)
```

For every `ε>0`, both prescriptions are well-defined. Their difference is exactly

```text
S_exp(ε) − S_time(ε)
  = |k|² Σ_{p+q+r=0} exp(−εΩ)/(ω_p ω_q ω_r)
          · [ε/Ω² + ε²/(2Ω)]  ≥ 0.                         (9)
```

For nonzero `k` this difference is not merely positive at fixed `ε`: it is bounded **strictly away from zero** for all sufficiently small `ε`. A constructive bound illustrates why. Put `h=2π/L`, take `εm≤1`, and restrict `p` and `q` to lattice vectors whose six components each lie in `[1/ε,2/ε]`. For sufficiently small `ε` there are at least `(2hε)⁻⁶` such pairs; set `r=−p−q`. For each pair,

```text
ω_p,ω_q ≤ √13/ε,   ω_r ≤ 7/ε,
Ω ≤ C/ε,           C = 2√13 + 7.
```

Keeping only the first positive term in (9) yields the explicit lower bound

```text
S_exp(ε) − S_time(ε)
 ≥ |k|² exp(−C) / [91 C² (2h)⁶]  > 0.                   (10)
```

This deliberately crude bound is sufficient and independent of `ε`. It holds after removing the auxiliary momentum cutoff at each fixed `ε`. Consequently, the two prescriptions cannot have the same limit; **if** `S_exp` also converges, their limits differ by at least this constant. We do not claim here that `S_exp` converges, nor that either prescription equals the book’s sharp-cube momentum limit. The difference is proportional to the local structure `|k|²`, so a finite subtraction could compensate it, but no particular physical renormalization condition has been established here.

Equations (9)–(10) also give a concrete warning against exchanging the finite-mode and regulator limits: the added terms vanish term-by-term at fixed momenta, yet their collective contribution does not vanish when all modes are included first. This is distinct from the free damping example in the [earlier audit](OTTINGER_DISSIPATIVE_QFT_UPLOADED_EXCERPT_AUDIT.md).

## 4. Numerical checks and their limits

[The verifier](verification/ottinger_scalar_regulator_gate.py) imposes a cubic individual-mode cutoff `|p_i|,|q_i|,|r_i|≤N` on both prescriptions and evaluates (3) and (8), with `m=1`, spacing `h=1`, `k=(1,0,0)` and no `L⁻⁶` factor. It records 12 finite-cutoff samples in [JSON](verification/ottinger_scalar_regulator_gate.json). For example:

| `ε` | `N` | `S_time` | `S_exp` | positive gap |
|---:|---:|---:|---:|---:|
| 0.5 | 6 | −1.238034 | 0.266765 | 1.504800 |
| 0.5 | 8 | −1.248882 | 0.264436 | 1.513318 |
| 1.0 | 6 | −0.206613 | 0.030407 | 0.237020 |
| 1.0 | 8 | −0.206621 | 0.030406 | 0.237026 |

The samples suggest stability as `N` grows at fixed positive `ε`, as expected from exponential damping; they are not a measurement of the `ε→0` limits and do not independently prove (10). The eight tests cover the zero-momentum cancellation, inversion symmetry, equality at `ε=0` for a fixed finite mode set, positive/growing sampled gaps, one shell-bound example, invalid inputs, numerical radial cancellation and independent Simpson integration of the finite-`N=1` time representation against the closed-form weights. These are checks, not a proof for infinite sums.

Run with NumPy available:

```text
PYTHONPATH=verification python -m unittest ottinger_scalar_regulator_gate_test
python verification/ottinger_scalar_regulator_gate.py
```

## 5. Consequences for the project

- The original [full-book follow-up](OTTINGER_FULL_BOOK_SCALAR_QED_FOLLOWUP.md) correctly identified (2.51) as an open finite-lattice/cutoff question. This note provides a finite-volume **alternative regulated result** and an explicit scheme-dependence obstruction; it does not close that question.
- Next, prove or refute convergence of the source’s original sharp individual-mode cutoff and establish its relation to (2) under an explicit renormalization condition. Separately, compare the finite-`γ` expression with these prescriptions and prove any `γ→0`, `L→∞` and regulator-limit interchanges. None of those is done here.
- The result concerns a second-order scalar expression within the source’s approximations, not nonlinear positivity, an interacting 3+1-dimensional continuum, BRST, microcausality, empirical validation or experiential individuation. The project’s unresolved B4–B5/F2, B9/F3, B10 and full C3 remain open. The reversible [instrument-uniformity work](CUTOFF_INSTRUMENT_UNIFORMITY.md) does not automatically apply to this model.
