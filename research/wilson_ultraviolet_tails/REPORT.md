# Step 33 — Removing the fixed momentum band with weighted ultraviolet tails

## Result and distinction from step 32

The limiting continuum excitation can have **unbounded momentum support**. An explicit summable family of positive-energy packets admits uniform local composite estimates even while the maximum retained momentum grows. A cutoff-dependent family of actual Wilson states approaches the full continuum local energy under a stated joint rank/spacing limit.

Unlike [step 32](../wilson_infinite_rank/REPORT.md), the continuum modes are not confined to one compact band. Unlike a claim of arbitrary ultraviolet universality, the proof requires weighted excitation moments and controls an explicitly chosen low-angle spectral preparation. It does not establish the result for every lattice state with the same low-energy observables.

## 1. Unbounded-support continuum state and actual lattice preparations

For i=0,1,… define a normalized packet amplitude on [i+1,i+2] by

\[
f_i(i+1+z)=\sqrt{30}\,z(1-z),\quad 0\leq z\leq1,
\qquad \lambda_i=2^{-i-1}.
\]

Disjoint supports give orthonormality; 30∫z²(1−z)²dz=1 gives normalization. Every occupation is nonzero, so the combined continuum excitation has no finite upper momentum cutoff. Its occupation operator is positive and trace class with trace 1. Its total continuum energy is

\[
\sum_i\lambda_i\int k|f_i(k)|^2dk
=\sum_i\lambda_i(i+3/2)=5/2.
\]

For each spacing a choose an integer N≥1 such that a(N+1)≤1. Retain i=0,…,N−1 and use the exact massless Wilson spinor and dispersion from step 30:

\[
u_a(k)=(\cos(ak/4),\sin(ak/4))^T,
\qquad E_a(k)=2\sin(ak/2)/a.
\]

The occupied physical bands satisfy ak≤1<π, inside the positive-momentum Brillouin branch. Fourier Parseval gives orthonormal positive-energy lattice vectors Vᵢ,ₐ. Thus

\[
C_{a,N}(t)=P_-+\sum_{i<N}\lambda_i|V_{i,a}(t)\rangle\langle V_{i,a}(t)|
\]

is an actual positive-contraction quasifree covariance evolving with the Wilson Hamiltonian. Omitted positive modes remain unoccupied; the rest of the negative-energy sea remains filled. The cutoff is part of this state-preparation family, not a change to the Wilson Hamiltonian or a hard cutoff on its full spectrum.

There is no single fixed-a lattice covariance containing every arbitrarily large physical momentum without a prescription for folding or truncation. Here that prescription is explicit. The theorem concerns the family Cₐ,ᴺ as a→0 and N→∞, not an undefined embedding of all continuum momenta into one lattice.

## 2. Weighted moments replace a common band bound

Set

\[
B_{i,j}=\frac1{\sqrt{2\pi}}\int |f_i(k)|k^j dk
\leq\frac{(i+2)^j}{\sqrt{2\pi}}.
\]

Consequently all needed occupation-weighted products are bounded by

\[
\sum_i\lambda_i B_{i,j}B_{i,k}\leq S_{j+k},
\quad S_q=\frac1{2\pi}\sum_i2^{-i-1}(i+2)^q.
\]

For q=0,…,4, the raw sums are respectively 1, 3, 11, 51, 299. These are computed independently in the tests. In particular the constants do not grow with the maximum retained momentum or number of retained modes. The moments needed for uniform derivatives and time bounds are finite.

The full continuum local chiral energy is the absolutely convergent sum

\[
t(x,t)=\sum_{i\geq0}\lambda_i
\operatorname{Im}[\overline{v_i(x,t)}\partial_xv_i(x,t)],
\quad
v_i(x,t)=\frac1{\sqrt{2\pi}}\int f_i(k)e^{ik(x-t)}dk.
\]

Its omitted-mode tail obeys the explicit uniform bound

\[
|t-t^N|\leq T_N=\frac{2^{-N}(N+3)}{2\pi}.
\]

This follows by summing the derivative product bound over i≥N, not by declaring high-energy occupation negligible without a quantitative estimate.

## 3. Local current estimate with growing ultraviolet support

For h=na and Wₙ=n²/(n²−1/4), the finite-N actual current-product expectation is exactly the linear term plus the Gram term derived in step 31. No mode-dependent composite normalization is added. Summing the packet estimates using the weighted constants gives

\[
|\Delta S_{a,n,N}-t(x,t)|\leq E_{a,h,n}(t)+T_N,
\]

\[
E_{a,h,n}(t)=W_n\left[\frac{h^2S_3}{6}
+a^2\left(\frac{S_3}{16}+\frac{|t|S_4}{12}\right)\right]
+(W_n-1)S_1+2\pi h^2S_0S_2.
\]

The linear estimates use |Eₐ(k)−k|≤a²k³/24 and |cos(ak/4)−1|≤a²k²/32 on every retained band. The Gram contribution is bounded by 2πh²S₀S₂. Although individual high-momentum packets have large derivative bounds, the summable occupation weights control their sum.

It follows that any joint sequence satisfying

\[
a\to0,\quad h=na\to0,\quad n\to\infty,
\quad N\to\infty,\quad a(N+1)\leq1
\]

has ΔSₐ,ₙ,ᴺ→t uniformly in x on bounded time intervals. There is no additional condition of the form 2⁻ᴺ/a²→0. For example a=n⁻² with N=2⌊log₂n⌋ meets the hypotheses and is tested numerically. A maximal retained window N of order a⁻¹ is also allowed by the estimate, although not enumerated to arbitrarily large N by the implementation.

Keeping N fixed would converge only to the truncated target. Keeping n fixed would retain the Wₙ bias. Neither limit can silently substitute for the stated joint limit. The endpoints of the current observable must also be actual lattice sites; translated lattices or converging admissible midpoints are required as in steps 30–32.

## 4. Independent Hamiltonian energy

The spectral total relative energy is computed independently:

\[
\epsilon_{a,N}=\sum_{i<N}\lambda_i\int E_a(k)|f_i(k)|^2dk.
\]

The uniform weighted third moment and omitted continuum first moment give

\[
|\epsilon_{a,N}-5/2|
\leq a^2\frac{51}{24}+2^{-N}(N+3).
\]

The local symmetrized Hamiltonian diagnostic is likewise computed by applying the actual spectral Hamiltonian to both spin components. For retained modes the upper component differs from the continuum field by controlled a² moment terms; the lower field and lower Hamiltonian image each carry an a factor. Summing their products is bounded by weighted moments of the same type. Adding T_N for omitted continuum modes proves local convergence to t. The numerical checks compare it independently with the current limit; no finite-a operator equality or unique lattice energy-density prescription is asserted.

The continuum transport law (∂ₜ+∂ₓ)t=0 follows from packet translation and the summable derivative bounds. Total energy and expected number are finite even though momentum support and rank are unbounded. This is not an infinite-density or thermal state.

## 5. Verification and explanatory boundary

`model.py` implements the unbounded-band packet family, actual finite-a covariance preparations, exact finite-N current formula, weighted moment and tail bounds, and independent local/total Hamiltonian energy. Twenty-four tests check normalization, moment sums, cutoff estimates, joint convergence, positivity, finite-Fock expectation and two-point reconstruction, spectral energy bounds, local energy agreement, and numerical refinement. `enumeration.json` records diagnostics. Integrals use numerical Simpson quadrature; the analytic bounds control continuum/lattice and omitted-mode errors, not certified quadrature intervals.

This closes a controlled **unbounded continuum excitation support → lattice preparation → local relative composite** bridge. The occupations and ultraviolet preparation are inputs, not derived physical selection laws. More slowly decaying or non-trace-class occupations require their own bounds; nonquasifree states, holes, arbitrary coherences, stress operator distributions and full Ward identities, absolute curved anomaly, interactions, and backreaction remain outside the theorem. Physical actuality and phenomenal constitution are not established by convergence of a free-field observable.

## Continuation

[Step 34](../wilson_particle_hole/REPORT.md) treats signed particle/hole occupation changes, including a determinant correction that is not nonnegative, with an absolute-value local bound.
