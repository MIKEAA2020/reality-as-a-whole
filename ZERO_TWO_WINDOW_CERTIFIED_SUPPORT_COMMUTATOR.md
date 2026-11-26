# A certified continuum bound for the support commutator

## Result

For the **specified** two-window continuum model and the incident/receding packet span P used in the [time-independent support interaction](ZERO_TWO_WINDOW_AUTONOMOUS_SUPPORT_DYNAMICS.md), let Q=I−P. An exact-rational calculation, with explicit analytic remainder bounds, establishes

```text
||[Θ_h,Q]|| < 0.419,              h=0,1.
```

Consequently the support interaction with g=1.2 has the uniform continuum amplitude and probability bounds

```text
D < 50699/305760 ≈ 0.1658131,
miss probability < D² < 0.0275,
false-flag probability < D² < 0.0275.
```

This improves the earlier conservative probability bound 0.678 and meets the proposed `<0.028` target. The inequalities apply to all initial states in the stated P or Q sectors; the coherent-sector population bound also applies to arbitrary superpositions and h correlations. They are conditional on the exact altered constraint and global Q coupling specified in the prior report, not on a finite-grid approximation.

The certificate is computed entirely with Python's exact rational integers and fractions: [verification/zero_two_window_commutator_certificate.py](verification/zero_two_window_commutator_certificate.py). It uses bounded Taylor remainders and exact integration, not floating-point quadrature. The [test module](verification/zero_two_window_commutator_certificate_test.py) additionally compares a finite Nyström calculation as a **control**, not as the proof. The mathematical model, proof steps and arithmetic verifier remain open to independent checking.

## 1. The operator and the two packets

Use the earlier continuum momentum band `p∈(−7,−6)` and set `t=p+6.5∈(−1/2,1/2)`. The packet factor is `g(t)=1/4−t²`. Up to irrelevant constant phases, the two normalized momentum wavefunctions spanning P are

```text
f_±(t)=sqrt(30) g(t) exp(±15 i t).
```

Their common internal state is the balanced pointer `d=(|0⟩+i|1⟩)/sqrt(2)` and both original memories in 0. Let `v_±=f_±⊗d⊗|00⟩` and `F(z₊,z₋)=z₊v₊+z₋v₋`; P projects onto the range of F. The logical h label is retained separately, and the interaction has `Θ₁=Θ₀−2I`. Hence the commutator with Q is the same for both h sectors.

Choose the exact rational center `k=7.046`. Since `QF=0`,

```text
||[Θ₀,Q]|| = ||QΘ₀P||
             ≤ ||(Θ₀−k)F|| / σ_min(F).
```

The numerator can be bounded using the 2×2 Gram matrix of the residuals `Z_±=(Θ₀−k)v_±`. The denominator must retain the nonzero overlap between the two packets; they are **not** assumed orthogonal.

For `w(x)=30x²(1−x)²`, x=t+1/2, the overlap is a phase times `∫₀¹ w(x) exp(30ix) dx`. Integration by parts twice, with w and w′ vanishing at both endpoints, and Cauchy–Schwarz yield

```text
|⟨v₊,v₋⟩| ≤ sqrt(∫₀¹ |w″(x)|²dx)/30²
             = sqrt(720)/900 < 0.03,
σ_min(F)² ≥ 0.97.
```

## 2. Reducing the residual to scalar kernel integrals

The pointer is a +1 eigenvector of `σ_yᴰ`; each memory starts in z=0. With the original couplings 0.5, 0.65, 0.65, the residual has mutually orthogonal internal components

```text
Z_j = d|00⟩ [(T−k)f_j − E_−5 f_j]
    + (1.3/sqrt(2)) |1,1,0⟩ E_0 f_j
    + (1.3/sqrt(2)) |1,0,1⟩ E_5 f_j,
T(p)=p²/6.
```

The order of the last two labels is D,M₁,M₂. Thus each residual Gram entry reduces to three scalar inner products, with coefficient `1.3²/2=169/200` for each memory term. The exact window kernel is

```text
E_a(t,s) = exp[−ia(t−s)] exp[−(t−s)²/2]
           sin[2(t−s)] / [π(t−s)],       a=−5,0,5,
```

with its continuous value at t=s.

The verifier replaces the packet phase by its degree-40 Taylor polynomial; the window phase by degree 32; and the Gaussian and sinc factors by their series through index 12. It represents every polynomial coefficient as a rational multiple of `i^k` and evaluates all integrals exactly using

```text
∫_−1/2^1/2 t^k dt = 0                         for odd k,
                         1/[(k+1)2^k]          for even k.
```

It encloses π rationally using the alternating series in Machin's identity `π=16 arctan(1/5)−4 arctan(1/239)`; the reciprocal used by the polynomial is rational, with its difference from `1/π` included in the kernel error. No approximation to π is silently treated as exact.

The rational residual-Gram calculation verifies the following **strict rational bounds**:

```text
D̃_++ < 0.168294,        D̃_−− < 0.168294,
|Re D̃_+−| < 0.000834,  |Im D̃_+−| < 0.000671.
```

For reference, the exact rational values print approximately 0.168292959, 0.168287560, −0.000832282 and −0.000669558. The displayed rounded values are not the inequalities on which the certificate relies.

## 3. Uniform series remainders and the certificate

Throughout the band, `|t|≤1/2` and `|t−s|≤1`. The verifier uses these uniform remainder bounds:

```text
packet phase:       e_f ≤ (15/2)^41/41!,
Gaussian:           e_g ≤ (1/2)^13/13!,
sin(2d)/d:          e_s ≤ 2^27/27!,
window phase:       e_p ≤ 5^33/33!.
```

The real-phase exponential bound follows from Taylor's integral remainder; the Gaussian and sinc estimates follow from their alternating series. Together with the rational reciprocal-π enclosure they give a uniform kernel error e_K. On a unit-length band the resulting integral-operator error is at most e_K by the Hilbert–Schmidt bound. Since the interaction coefficients have total norm weight 3.6 and `||Θ₀−k||<4`, each exact residual differs from its polynomial approximation by at most

```text
η = 4e_f + 3.6 e_K (1+e_f) < 10^−11.
```

The exact rational code verifies this last inequality. The approximate residual norms are below 1, so diagonal and off-diagonal Gram errors are each at most `2η+η²`. Gershgorin's inequality then gives

```text
||[Θ_h,Q]||²
 < [0.168294 + 0.000834 + 0.000671 + 4η + 2η²]/0.97
 < 0.419².
```

All threshold comparisons in the verifier use fractions, not rounded decimal output. The result applies in the full continuous band Hilbert space of the selected model; it does not assert that a different packet, band, coupling or apparatus has the same bound.

## 4. Consequence for the support interaction

For positive `Θ_h≥a_h²`, the square-root commutator inequality used previously is

```text
||[sqrt(Θ_h),Q]|| ≤ ||[Θ_h,Q]||/(2a_h).
```

The original spectral bound gives `a_h≥a₁>1.3`. With g=6/5 and `π<22/7`, the Duhamel estimate is therefore bounded using rational numbers:

```text
D ≤ π² ||[Θ_h,Q]||/(16 g a_h)
  < (22/7)² (419/1000)/(16 (6/5) (13/10))
  = 50699/305760 < 0.166.
```

Squaring yields the stated `<0.0275` uniform miss and false-flag bounds. The same result is robust to an additional bounded self-adjoint generator error `δ` by replacing D with `D+τδ`, provided the perturbed positive branch remains positive. But such an operator-norm error guarantee must be justified separately; finite successful calibration alone does not prove it.

The coherent-state inequality from the previous report becomes

```text
λ = Tr(Qρ) ≤ min[1,(sqrt(q)+50699/305760)²],
```

where q is the probability of the new flag at `τ=π/(2g)` in the **altered** constraint. If a matching continuum experiment on independent copies observed the earlier illustrative 1,519 flags in 100,000 trials, its one-sided 95% binomial bound is `q_U<0.019485`; the certified inequality would then give `λ<0.094` with that statistical coverage. The earlier count was a finite-model simulation, not an actual continuum experiment, and the inference remains conditional on the exact detector model.

## 5. What this does and does not resolve

The previously conditional commutator target is now met by a continuum bound with explicit, reproducible arithmetic. It does not prove that the global packet-support coupling can be physically implemented, that the actual Hamiltonian is within a specified norm tolerance, or that the ideal scalar reference is operationally available. The new interaction changes the constraint and does not automatically realize the old record protocol.

The flag's **reversible loss remains**: the prior control shows it nearly returns to zero as the coupling continues. A next step would need a specified autonomous transfer or stopping mechanism, followed by a fresh error and backaction analysis; adding such a mechanism changes the mathematical model again. None of this establishes local general covariance, exact crossing counts, actual subjects, felt succession, or a derivation of the whole from zero.

## Reproduce

```sh
# Exact-rational certificate itself: Python standard library only
python verification/zero_two_window_commutator_certificate.py

# Includes an independent finite-grid control; NumPy needed for that control
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_commutator_certificate_test -v
```
