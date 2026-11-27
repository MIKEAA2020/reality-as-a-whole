# Two-window continuum certificate: analytic recheck and tighter bound

## Result and scope

For the **specified** continuum two-window model, the selected packet span and the altered support-flag constraint in [the prior certificate](ZERO_TWO_WINDOW_CERTIFIED_SUPPORT_COMMUTATOR.md), rechecking the analytic chain and tightening its overlap and matrix-norm estimates yields

```text
||[Θ_h,Q]|| < 0.412,       h=0,1,
flag miss probability, false-flag probability < (12463/76440)² < 0.0266.
```

The earlier bounds `<0.419` and `<0.0275` remain valid. This is a mathematical improvement for that exact model; the coupling to the global packet projector, clock, state preparation and the changed constraint are inputs. The flag remains reversible and not a durable history record. Neither the calculation nor its scalar-clock parameter assumes fundamental spacetime, nor derives a physical spacetime, a whole-level physical energy zero, subjects, or lived succession.

The [refined verifier](verification/zero_two_window_commutator_refined_certificate.py) uses exact rational arithmetic for the improved overlap and threshold comparisons but **reuses** the original verifier's exact-rational residual Gram entries and error bound. A [later independent rational-polynomial implementation](ZERO_TWO_WINDOW_INDEPENDENT_CERTIFICATE_AND_CURSOR_BOUND.md) now recomputes and exactly matches the Gram entries and gives separate overlap/remainder bounds; it still shares the model assumptions and is not a machine-checked formal proof. The finite-grid and quadrature controls are not continuum proofs. This recheck covers selected bounds and their flag consequence, not the entire two-window programme.

## 1. Explicit packet overlap

With `t∈[−1/2,1/2]`, `f_±(t)=sqrt(30)(1/4−t²)e^(±15it)` and the same normalized internal pointer state, put `x=t+1/2`, `w(x)=30x²(1−x)²`. Then both packets have norm one, and their overlap is the real number

```text
r = ∫₀¹ w(x)e^(30i(x−1/2)) dx
  = 120 [−888 sin(15) − 180 cos(15)] / 30⁵.
```

The formula follows from elementary integration by parts; `w` and `w′` vanish at both endpoints. The Gram matrix of the packet map F therefore has eigenvalues `1±|r|`, so `σ_min(F)²=1−|r|`. The old proof's `<0.03` is sound but needlessly loose.

The new exact-rational computation evaluates the real Taylor polynomials for `sin(15)` through degree 79 and `cos(15)` through degree 80. Their absolute errors are at most `15^80/80!` and `15^81/81!`, respectively, by the real integral remainder and the unit bound on sine/cosine derivatives. Substitution and the triangle inequality certify

```text
|r| < 11/5000 = 0.0022,       σ_min(F)² > 0.9978.
```

The overlap is approximately `−0.002176354458`; this decimal is for orientation only. Nonorthogonality is retained, not discarded.

## 2. Residual-Gram audit and sharpened estimate

For a bounded self-adjoint Θ and the orthogonal projection P onto `ran F`, set `Q=I−P`, `k=7.046` and `Z=(Θ₀−k)F`. Since `QF=0`,

```text
||[Θ₀,Q]|| = ||QΘ₀P|| ≤ ||Z|| / σ_min(F).
```

The first equality holds because the commutator's two off-diagonal blocks are adjoints up to sign; the inequality is an operator bound for **all** packet-span vectors, not a bound only for the two supplied packets separately. Also `Θ₁=Θ₀−2I`, hence both commutators coincide.

The earlier verifier obtains exact polynomial residual Gram entries `G̃_ij`, normalized by the common packet factor sqrt(30), and establishes entrywise error at most `2η+η²`, with `η<10⁻¹¹`. Its rational comparisons bound both diagonals by `0.168294` and the absolute real/imaginary parts of the off-diagonal by `0.000834`, `0.000671`. The off-diagonal *modulus* is bounded by

```text
sqrt(0.000834²+0.000671²) < 0.001071,
```

rather than the sum of those two components. A two-by-two Hermitian row-sum bound and the overlap estimate give the strict rational inequality

```text
||[Θ_h,Q]||²
 < (0.168294 + 0.001071 + 4η + 2η²) / 0.9978
 < 0.412².
```

The new verifier executes the last comparison with fractions, including the inherited exact value of η; the gap is small, so rounding the input before comparison would not be an adequate certificate.

### Analytic premises checked

* The continuous band has unit length. The window kernel is the product of the Fourier transform of a positive Gaussian and `sin(2d)/(πd)`, the Fourier transform of a positive uniform density on `[-2,2]` in the stated convention. Thus the window effects are positive trace-class operators with trace `2/π`, and norm at most `2/π`. Their phase translations preserve those properties.
* On the stated h=0 band, `6−7.2/π ≤ Θ₀ ≤ 49/6+7.2/π`, implying `||Θ₀−7.046I||<4`; **this residual estimate is for Θ₀**, with the h=1 commutator obtained by the scalar shift. On h=1 the lower bound is `4−7.2/π > (13/10)²`, so the positive root has lower bound `a₁>1.3`.
* The kernel's Gaussian and sinc series are alternating with decreasing term magnitudes on `|t−s|≤1`; the two real phase exponentials have the usual real-argument Taylor integral remainders. Their product errors and rational π enclosure give the stated uniform kernel error, which is also an integral-operator norm bound by Hilbert–Schmidt on a unit square. The normalized packet envelope has L² norm one; this justifies the inherited η estimate. The polynomial's exact integrals use parity and `∫t^(2j)dt=1/[(2j+1)2^(2j)]`. These observations are independent of the Nyström control, though the long rational sums themselves are calculated by the original code.

## 3. Flag and coherent-state consequences

For positive Θ_h≥a_h², the square-root resolvent integral and `||[Θ_h,Q]||` give

```text
||[sqrt(Θ_h),Q]|| ≤ ||[Θ_h,Q]||/(2a_h).
```

For `H_h=sqrt(Θ_h)⊗I+(6/5)Q⊗σ_y`, the comparison to the ordered ideal unitary via Duhamel at `τ=π/(2g)` gives

```text
D ≤ π² ||[Θ_h,Q]||/(16g a_h)
  < (22/7)² (412/1000) / [16(6/5)(13/10)]
  = 12463/76440.
```

The flag amplitudes relative to the ideal detector differ by at most D for every normalized input, including arbitrary h correlations. For a Q-sector input the miss probability is `<D²`; for a P-sector input the false-flag probability is `<D²`. The same comparison, with purification if necessary, gives for arbitrary initial ρ and actual flag probability q

```text
|sqrt(q)−sqrt(Tr(Qρ))| ≤ D,
Tr(Qρ) ≤ min[1,(sqrt(q)+12463/76440)²].
```

The uncapped right-hand bound is strict; the cap at 1 need not be. This concerns the **altered** experiment and its specified model, not the earlier block-diagonal instrument.

If an independent-copy experiment actually produced the previous *illustrative simulated* count 1,519/100,000 and the prior one-sided 95% binomial upper limit `q_U<0.019485` applied, then using the rational inequality `sqrt(0.019485)<0.13959` gives `Tr(Qρ)<0.0916` at that coverage. No such continuum experiment has been reported; the binomial inference also requires independent identically prepared trials and the assumed detector model.

## 4. Tests and remaining work

The new [test module](verification/zero_two_window_commutator_refined_certificate_test.py) checks exact rational thresholds, compares the analytic overlap with independent Gauss–Legendre quadrature, and directly computes the sampled `QΘP` norm in an independently orthonormalized packet span for both h sectors. These controls do not establish convergence of the mesh, prove that the operator is physically implementable, or independently redo the original long exact-rational integrals. The original [certificate tests](verification/zero_two_window_commutator_certificate_test.py) remain relevant.

**Correction and continuation:** the [independent rational implementation and cursor comparison](ZERO_TWO_WINDOW_INDEPENDENT_CERTIFICATE_AND_CURSOR_BOUND.md) recomputes the Gram matrix and alternative remainder/overlap bounds. The earlier version of this review overlooked existing later work: the [autonomous cursor reader](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) and [instrument/backaction analysis](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md) already supply a conditional finite-horizon transfer mechanism in a further changed constraint. The remaining tasks include independently auditing its unbounded-operator/domain estimates, examining a genuinely distinct clock for that instrument, and connecting these assumptions to a justified physical model. Permanent retention and local implementation are not established. A regulator, numerical agreement, or a designated mathematical flag does not establish that physical–experiential identity has been explained.
