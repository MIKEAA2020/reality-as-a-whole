# Geometry-clock spectrum: no singular-continuous sector and one exterior bound state

**Continuation:** [the full continuum slice construction](ZERO_GEOMETRY_CLOCK_FULL_CONTINUUM_SLICE.md) proves that this specific model also has no embedded eigenvalues and obtains a full-state slice map for almost every geometry value.

## Result

The last open question was whether the interacting geometry-slice model might hide a singular-continuous sector or additional exterior bound states. For the **specific band, window and coupling used in our model**, the following continuum results can be derived:

1. The interacting operator has **no singular-continuous spectral component**. The proof uses a local positive-commutator estimate and standard Mourre theory; trace-class perturbation alone would not be enough.
2. In each pointer channel there is **exactly one eigenvalue outside the free band**, counted with multiplicity. It is simple: below the band for d=+ and above the band for d=−. Neither band endpoint is an eigenvalue.
3. Embedded eigenvalues inside the band have finite multiplicity and are locally finite away from the endpoints. This analysis **does not prove they are absent or simple**.

Combined with [the preceding cyclicity result](ZERO_GEOMETRY_CLOCK_CONTINUUM_CYCLICITY.md), almost every geometry slice recovers the full scattering sector and the unique exterior bound state. It also recovers every simple embedded eigenstate; possible invisible directions can only be in degenerate embedded eigenspaces. Therefore, **if** all embedded eigenvalues are simple or absent, almost every slice recovers the full physical state from its complete complex scalar-clock signal. That condition is not established here.

These are statements about an idealized homogeneous constrained model, not a proof of a physical global clock, full quantum gravity, subjective time, or zero's derivation of the chosen model. The spectral proofs below are analytic and depend on standard theorems; [the numerical controls](verification/zero_interacting_clock_mourre_spectrum_test.py) do not themselves prove continuum spectrum.

## 1. Operator and window

Let `I=(−7,−6)`, `T(p)=p²/6`, and for h=0,1 and d=±1 let

```text
H_(h,d) = T − 2h − c d E,       Ω_(h,d)=√H_(h,d),      c=0.8.
```

E has the Gaussian-smeared-window kernel

```text
K(p,q) = exp[−(p−q)²/2] sin[2(p−q)]/[π(p−q)]
       = (1/2π) ∫_ℝ g(x) exp[i(p−q)x] dx,

g(x) = ∫_(−2)^2 exp[−(x−r)²/2]/√(2π) dr.
```

The previous reports show E is positive, trace class and bounded by I, so H≥3.2 on the chosen branch. Its essential spectrum is `[6−2h,49/6−2h]`. The earlier variational proof establishes an eigenvalue below that band for d=+ and one above it for d=−. Our improvements apply to the continuum operator, not merely to its Nyström regulator.

## 2. Exactly one exterior eigenvalue in each pointer channel

It suffices to consider h=0; the `−2h` shift changes eigenvalues but not eigenvectors. Let `f∈L²(I)` obey the single linear condition `∫_I f(p)dp=0`. Let `u` denote distance to either band edge, with `0<u<1`. Subtracting the zero Fourier mode and applying weighted Cauchy–Schwarz gives

```text
|∫_I exp(ipx) f(p)dp|²
  ≤ (∫_I u |f(p)|²dp) × ∫_0^1 |exp(iux)−1|²/u du
  ≤ (x²/2) ∫_I u |f(p)|²dp.
```

The sign of u is immaterial to the modulus. Since the Gaussian-smoothed window satisfies

```text
∫ x² g(x)dx = ∫_(−2)^2 (r²+1)dr = 28/3,
C ≡ (1/4π) ∫ x²g(x)dx = 7/(3π),
```

we obtain the uniform estimate

```text
⟨f,Ef⟩ ≤ C ∫_I u |f|² dp       whenever ∫ f=0.
```

For the lower edge take `u=−p−6`; then `T−6=2u+u²/6≥2u`. For the upper edge take `u=p+7`; then `49/6−T=(14u−u²)/6≥(13/6)u`. Because

```text
c C = 28/(15π) ≈ 0.594 < 2 and < 13/6,
```

the quadratic forms of `H_(0,+)−6` and `49/6−H_(0,−)` are **strictly positive** on every nonzero vector in the closed codimension-one subspace `∫f=0`.

If either operator had two linearly independent eigenvectors at or beyond the corresponding exterior edge, their two-dimensional span would intersect this codimension-one subspace in a nonzero vector on which the appropriate quadratic form is nonpositive—a contradiction. The already-proved exterior eigenvalue exists; consequently it is the **only** one and is simple. The same argument also excludes an eigenvalue at its adjacent edge, since an edge eigenvector together with the exterior one would form such a two-dimensional subspace. At the opposite edge, positivity of E and strict inequalities `T<49/6` and `T>6` almost everywhere exclude an eigenvector directly. Thus neither endpoint is an eigenvalue, and positivity also rules out an exterior eigenvalue on the opposite side of the band.

The bound is conditional on the stated E, momentum band and c. It is not a general theorem for all gravitational detectors or all couplings.

## 3. No singular-continuous component: the Mourre estimate

A compact or trace-class perturbation alone does not exclude singular-continuous spectrum. Here the additional **smoothness** of the kernel supplies the needed regularity.

Choose the real smooth vector field on I

```text
v(p)=exp[4−1/((p+7)(−6−p))]  for −7<p<−6,
```

extended by zero at the edges. It is positive in the interior and vanishes to all orders at both endpoints. Its complete flow defines the self-adjoint conjugate generator

```text
A = −i [ v(p) d/dp + v′(p)/2 ].
```

With the convention `[H,iA]=H(iA)−(iA)H`, the free commutator is

```text
[T−2h,iA] = −v(p) p/3 > 0  in the band interior.
```

The interaction commutator is an integral operator with smooth kernel

```text
[E,iA](p,q) = −(v(p)−v(q)) K′(p−q)
              − [v′(p)+v′(q)] K(p−q)/2.
```

It is Hilbert–Schmidt and hence compact. The same holds for further commutators: the vector field and K are smooth on the compact band, with endpoint terms vanishing. In particular H belongs to the regularity class C²(A) needed for the standard Mourre result.

For a compact energy interval J strictly inside the free band, choose a smooth cutoff F supported inside that band and equal to 1 on J. The free positive commutator has a positive lower bound on the p-preimage of `supp F`. Since `H−(T−2h)` is compact, continuous functional calculus gives `F(H)−F(T−2h)` compact. Therefore, for some c_J>0 and compact self-adjoint K_J,

```text
P_J(H) [H,iA] P_J(H) ≥ c_J P_J(H) + K_J.
```

The standard Mourre theorem for a C² self-adjoint operator with this estimate gives absence of singular-continuous spectrum on J and locally finite eigenvalues of finite multiplicity there; see, for example, the positive-commutator background in [Mourre, *Communications in Mathematical Physics* 78 (1981)](https://doi.org/10.1007/BF01942331) and the compact-remainder discussion in [arXiv:1707.05183](https://arxiv.org/abs/1707.05183). Covering the open band by countably many such intervals excludes its singular-continuous part. Outside the band the compact-perturbation spectrum is discrete, and the two endpoints cannot support a continuous measure because a continuous measure has no atoms. Hence `H_(h,d)` has **no singular-continuous component anywhere**.

The positive square root is a smooth, strictly monotone and bi-Lipschitz function on the spectrum, bounded away from zero. Therefore Ω has the same absolutely-continuous, pure-point and singular-continuous subspaces, and no singular-continuous component either. The local estimate does not exclude isolated embedded eigenvalues, and does not establish their multiplicity as one.

## 4. What this changes for the slice question

For almost every α, the preceding result proves the slice cyclic subspace contains the entire a.c. subspace and every simple eigenstate. The present result removes the possibility that an unknown singular-continuous subspace is hiding the remaining information. Because there is exactly one exterior eigenstate per d channel, and it is simple, it is included for almost every α; in fact, its overlap is nonzero for **all |α|<π**, as shown previously.

Thus the only potential missing directions for almost every slice are inside **degenerate embedded eigenspaces**. A single slice vector projects onto at most one direction of an eigenspace with the same frequency, so degeneracy is a real issue rather than something a basis relabeling can fix. For a particular slice such as α=0, a.c. cyclicity still requires a separate proof: the earlier result is almost-everywhere, not pointwise.

The signal used is the entire complex covariant solution `Ψ(α,φ)` for all φ. Its mathematical injectivity is not a finite-clock measurement, an autonomous record, or a globally covariant clock POVM. The bound-state obstruction to such a POVM remains. The finite-window first-reading protocol is a distinct experimental question, whose continuum instrument must be transported as a whole if intermediate operations can leave and return to a restricted subspace.

## 5. Decisive next step

Analyze the embedded eigenvalue equation in the band, including possible degeneracy. A proof that embedded eigenspaces are one-dimensional—or that there are no embedded eigenvalues—would, combined with these results, establish a full-state geometry-slice representation for almost every α in this selected physical model. It would still be an ideal solution-data map; a physical clock requires finite-resolution, local interaction and record dynamics.

The broader point–sphere proposal asks how zero's constitution necessitates physical differentiation and actual experience. This calculation has not derived the action, band, state, measurement, subject, experiential incidence or objective whole energy from zero. A global signed balance, if justified, does not erase locally felt suffering. No fundamental preferred foliation is introduced, but the homogeneous model is not a demonstration of the inhomogeneous GR constraint algebra.

## Reproduce

```sh
python -m unittest verification.zero_interacting_clock_mourre_spectrum_test -v
```

The test checks the window second moment, the codimension-one inequality on representative complex vectors, the conjugate-field derivative, the commutator kernel and integration by parts, and finite-grid edge spectra. It does **not** numerically prove the continuum Mourre theorem or exclude embedded eigenvalues. The note's continuum conclusions rest on the stated analytic estimates and the cited theorem.
