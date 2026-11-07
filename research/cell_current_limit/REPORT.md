# Constructive step 27: a spatial-cell CAR composite and its relative stress limit

## Result and scope

[Step 26](../relative_subtraction/REPORT.md) controlled a continuum regulator but not an actual lattice observable. Here we construct **cell CAR modes, positive lattice quasifree states, and a finite two-cell current product**, then prove a joint spacing/coincidence limit for its relative expectation.

The state choice is explicit: the lattice covariances are cell compressions of the continuum conformal states, not ground states of the Wilson or Floquet regulators. This does not close that state-identification problem. It does, however, go beyond bounded-field convergence: the composite norm diverges as a^-2, and an explicit short-distance estimate controls the amplified state difference.

The result exposes a necessary matching distinction. Uncalibrated fixed-cell-count coincidence retains a cell-shape factor; a mesoscopic separation removes it, or one can divide by an explicit state-independent factor. Thirty-two finite tests check these alternatives and an actual two-mode Fock realization.

## 1. A genuine spatial lattice with positive states

Use one complex chiral Cauchy Hilbert space H=L²(R,du), identified with the spatial line, up to orientation, on the chosen Cauchy slice. The other chirality can be treated independently. Let C₀ be its negative-momentum vacuum projection and let C_f be the positive projection transported by the half-density unitary of a smooth increasing diffeomorphism f. We use f(u)=u+αu³, α≥0, for explicit diagnostics.

The covariance kernel has the distributional form

\[
C_f(x,y)=\tfrac12\delta(x-y)+\frac1{2\pi i}
\frac{\sqrt{f'(x)f'(y)}}{f(x)-f(y)},
\]

with the principal-value/current conventions of step 25. For the reference, the last fraction is 1/(x-y). These are specified continuum state inputs, not guessed finite covariance matrices.

At spacing a let e_j^a=a^-1/2 times the indicator of the jth cell. The isometry J_a from ℓ² into H gives exact lattice CAR modes c_j=a(e_j^a). Define

\[
C_{f,a}=J_a^*C_fJ_a.
\]

It is a positive contraction, so it defines a gauge-invariant quasifree state on the lattice CAR algebra. Compression may make it mixed even when C_f is a pure projection. The reference uses the **same** physical cells and J_a, rather than cells rescaled in f coordinates.

For this zero-charge conformal family the diagonal occupations are 1/2: the delta term contributes 1/2 and the antisymmetric principal-value part integrates to zero on a diagonal cell square. For distinct cells,

\[
(C_{f,a})_{jk}=\frac a{2\pi i}\,\overline k_f^a,
\qquad
\overline k_f^a=\frac1{a^2}\int_{C_j}\!dx\int_{C_k}\!dy\,
\frac{\sqrt{f'(x)f'(y)}}{f(x)-f(y)}.
\]

The overline denotes a cell average, not complex conjugation. This exact cell-integral definition, rather than numerical quadrature alone, establishes positivity for arbitrary finite collections of cells.

## 2. A finite operator whose norm is not uniformly bounded

Define the centered cell current and the two-cell composite

\[
J_j^a=\frac{c_j^*c_j-1/2}{a},\qquad
O_{jk}^a=\pi J_j^aJ_k^a\quad(j\ne k).
\]

It is an even self-adjoint CAR observable. Its norm is π/(4a²), so the bounded fixed-observable convergence theorems of earlier steps do not directly control its limit.

Wick's rule and the zero centered means give

\[
\omega_{f,a}(J_j^aJ_k^a)=-\frac{|(C_{f,a})_{jk}|^2}{a^2}.
\]

Hence the relative expectation of the **same operator** in the two lattice states is

\[
\Delta E_{a,jk}:=\omega_{f,a}(O_{jk}^a)-\omega_{0,a}(O_{jk}^a)
=-\frac1{4\pi}\left[(\overline k_f^a)^2-(\overline k_0^a)^2\right].
\]

The square is of the averaged fermion kernel. It is not the average of the continuum squared current kernel. Averaging and forming the quadratic observable do not commute; the finite shape correction below measures a consequence of that difference.

For two modes, the covariance is [[1/2,z],[z*,1/2]]. Its finite Fock density has empty/full probabilities d=1/4-|z|², one-particle diagonal entries 1/2-d, and off-diagonal entries z,z*. It is normalized and positive, with eigenvalues d,d,(1/2-|z|)²,(1/2+|z|)². The code realizes it on four occupation states and verifies the covariance and current expectation by matrix traces. No positivity claim rests solely on hard-coded scores or scalar kernel fitting.

## 3. Exact flat cell shape

Choose cell centers u±h/2 with h=na, n≥2 even. They are actual sites on the grid with origin u and indices ±n/2, and their closures are disjoint. On a fixed-origin grid one may instead use a lattice midpoint u_a within a/2 of the desired u; smooth midpoint dependence gives the same limit, with an additional O(a) error. The flat average is

\[
\overline k_0^a=\frac{L(h+a)-2L(h)+L(h-a)}{a^2},
\qquad L(s)=s\log s-s.
\]

Equivalently,

\[
h\overline k_0^a=R(a/h),\qquad
R(r)=\sum_{p=0}^\infty\frac{2r^{2p}}{(2p+1)(2p+2)}.
\]

The series follows by averaging 1/(h+ξ-η) over the two uniform cells. Odd moments vanish and E(ξ-η)^(2p)=2a^(2p)/((2p+1)(2p+2)). For r<1 it is absolutely convergent, positive and stable to evaluate. In particular

\[
0\le R(r)-1\le\frac{r^2}{6(1-r^2)}.
\]

For fixed n, R(1/n) is independent of a, not a vanishing cutoff artifact. At n=2 it is 2(3log3-4log2), approximately 1.0464962875.

## 4. The local kernel estimate that controls the composite

Let s=x-y and v=(x+y)/2. Write the smooth relative fermion kernel as

\[
d_f(v,s)=\frac{\sqrt{f'(v+s/2)f'(v-s/2)}}{f(v+s/2)-f(v-s/2)}-\frac1s.
\]

Step 26 supplied the smooth even current remainder F_f(v,s). They are related without singular cancellation by

\[
d_f(v,s)=\frac{sF_f(v,s)}{\sqrt{1+s^2F_f(v,s)}+1}.
\]

Thus d_f=s b(v,s²), with b smooth locally and b(u,0)=F_f(u,0)/2. This proves regularity of the relative fermion kernel at coincidence and supplies the stable quadrature used in the code.

Within the cells, write v=u+(ξ+η)/2 and s=h+ξ-η. Symmetric averaging cancels not only Eξ and Eη but also E[(ξ+η)(ξ-η)]. Taylor expansion of b therefore yields, uniformly for a≤h/2 in a fixed small neighborhood,

\[
\overline d_f^a
=\overline k_f^a-\overline k_0^a
=\frac h2F_f(u,0)+O(h^3).
\]

The constants depend on bounded local derivatives and positive f', not on n within a/h≤1/2. Combining this with the exact flat shape gives

\[
(\overline k_f^a)^2-(\overline k_0^a)^2
=2\overline k_0^a\overline d_f^a+(\overline d_f^a)^2
=R(a/h)F_f(u,0)+O(h^2).
\]

This is the estimate that licenses amplification by the diverging current normalization. Merely knowing C_{f,a}-C_{0,a} tends to zero would not establish it.

## 5. Three limits, with different normalization requirements

The target continuum relative stress is t_f(u)=-F_f(u,0)/(4π)=-{f,u}/(24π).

### A. Mesoscopic separation: no extra shape calibration

Take a→0, h→0, with h/a=n→infinity through even integers. Then

\[
\Delta E_{a,jk}\longrightarrow t_f(u),\qquad
|\Delta E_{a,jk}-t_f(u)|\le C\left(h^2+(a/h)^2\right)
\]

locally, for a suitable C and a/h≤1/2. The split points approach the target point while remaining separated by many cells. For example a=N^-2, h=N^-1, n=N gives an O(N^-2) error with this estimate. The lattice operator is supported in a region shrinking to u even though the number of intervening cells grows.

### B. Fixed number of cells: a real finite matching factor

At fixed even n and a→0,

\[
\Delta E_{a,n}\longrightarrow R(1/n)\,t_f(u).
\]

This is generally not the uncalibrated continuum stress. The limit is not made correct merely by sending both a and h to zero. In the diagnostic α=0.2,u=0.4, the target is about -0.01070558451; the n=2 raw limit is about -0.01120335444.

This factor is not evidence of a different physical central charge or a failed positive state. It comes from the explicitly defined cell-bilinear observable and its finite point-splitting geometry. The normalization must be matched before assigning it the continuum stress interpretation.

### C. Fixed cells with a state-independent multiplicative calibration

Define O_cal=O/R(1/n). Then its relative expectation tends to t_f(u) even at fixed n, with error O(h²). The factor depends only on the cell shape and count, not on f or the state. This is an explicit operator-matching choice, not tuning a separate counterterm for each desired answer.

The theorem concerns this relative expectation in the conformal family; it is not a proof of all stress operator products, Virasoro commutators, or absolute Ward terms for the finite lattice. Mesoscopic separation provides a way to obtain the same limit without that finite factor.

## 6. Numerical evaluation and actual finite CAR checks

The code integrates only d_f, which is smooth, and evaluates the flat average through the convergent positive series. It computes the difference of squares as 2 k₀ d+d², avoiding cancellation of two O(h^-2) quantities. The cubic F_f has the exact rational formula from step 26.

Cell integrals in the theorem are exact. Numerical midpoint quadrature is an approximation, checked by refinement. For smooth d_f its averaged quadrature error is bounded by a constant times a²/Q² times the supremum of its second derivatives, where Q is the number of cells per quadrature direction. Its contribution after multiplication by k₀=O(1/h) tends to zero at least as a²/(hQ²) in the controlled a≤h/2 limit. It is not silently treated as an exact distributional integration rule.

Finite Fock tests use moderate spacings so that direct density-matrix subtraction can be compared with the stable formula. A separate scaling check shows the off-diagonal state difference shrinks as a² at fixed n while the composite difference stays finite. This illustrates concretely why bounded-state convergence alone was too weak.

## 7. Curved interpretation and the remaining state bridge

The lattice modes are those of the rescaled massless χ field. To interpret ψ on the admitted conformal geometry, retain the inner-product/source factors of steps 22 and 25. The computed relative chiral terms can be added to the separately specified curved geometric stress expectation. The difference has zero mixed component, zero trace, and chiral conservation; any common Cg_ab finite counterterm cancels.

The continuum relative limit is tensorial when both states and the reference are transformed. The finite cell prescription chooses a chart and is not asserted covariant at nonzero a. Likewise the compatibility checks with the curved Ward formulas do not prove a discrete stress-conservation law for a newly specified lattice dynamics: no such dynamics was selected here.

Most importantly, these states were **pulled back from continuum conformal covariances**. Their positivity and exact definition are clear, but they have not been identified with Wilson ground states, a Floquet vacuum, or the earlier massive static state. The construction earns a lattice-observable limit within a declared state class; it does not independently select that class from geometry or manufacture the missing Hamiltonian short-distance estimates.

The absolute anomaly remains supplied by the continuum Ward prescription. A theorem deriving it from the chosen lattice current algebra or regulated effective action is still separate. No massive Hadamard theorem, stress fluctuation limit, gravitational equation, or backreaction solution follows here.

## 8. Reproducibility and explanatory ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover CAR, positive covariances/densities, finite operator traces, current Wick contraction, diverging norm, exact cell shape, smooth kernel control, fixed-count bias, mesoscopic and calibrated limits, quadrature, shrinking support, and compatibility with relative curved stress. Representative errors and shape factors are saved in `enumeration.json`.

**Earned:** an actual finite spatial-CAR composite with a controlled relative continuum stress limit; a quantitative distinction between cell spacing and point separation; state-independent matching at fixed cell count.

**Not earned:** a Wilson/Floquet vacuum composite theorem, full operator-valued stress or anomaly derivation from the lattice, absolute vacuum energy, dynamics/backreaction, empirical selection, all-framework integration, phenomenal constitution, or ultimate explanation. A lattice current, shape factor, or renormalized expectation is not a subject or realization token.

**Next bridge:** prove corresponding short-distance estimates for an independently specified Hamiltonian lattice state, rather than importing its covariance from the continuum. That requires more than the previously proved fixed-observable state limit.

## Continuation: Hamiltonian-selected thermal states

[Step 28](../wilson_thermal_composite/REPORT.md) derives a corresponding relative composite limit directly from massless Wilson ground/thermal covariances, rather than continuum compression. It supplies a short-distance estimate and comparison with Hamiltonian energy, while retaining fixed-separation normalization and chirality-mixing artifacts. This is a thermal massless result, not a general massive stress theorem.
