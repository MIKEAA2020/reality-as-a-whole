# Step 34 — Signed particle/hole excitations and local stress

## Main result

Holes in the negative-energy sea also admit a controlled local composite limit. The relative covariance is no longer positive, and the Gram term in the exact current product need not be nonnegative. Its **absolute value** is nevertheless quadratically small in the point separation under the same smooth-packet hypotheses.

The explicit state contains one positive-energy packet and a hole in a mirrored negative-energy packet. Its net relative particle number can be zero while its excitation energy is positive. The continuum current limit agrees with independently evaluated local Hamiltonian energy.

This extends the particle-only construction; it does not establish arbitrary particle/hole coherence, nonquasifree states, full stress Ward identities, or absolute curved renormalization.

## 1. State positivity with a signed update

Retain the Wilson Hamiltonian, sea covariance P₋, and normalized amplitude f(k) on [1,3] from [step 30](../wilson_wavepacket_composite/REPORT.md). For signed momentum k in either [1,3] or [−3,−1], write

\[
u_a(k)=(\cos(ak/4),\sin(ak/4))^T,
\qquad \varepsilon_a(k)=2\sin(ak/2)/a.
\]

For 3a<π, hₐ(ak)uₐ(k)=εₐ(k)uₐ(k). The energy ε is negative on the hole band. This is the upper-component chiral branch, not a claim that all eigenvalues of the full two-component Hamiltonian have one signed dispersion.

Let Vₚ and Vₕ be normalized lattice packets with respective amplitudes f(k) and f(−k), carrying the signed Hamiltonian phases exp(−iεt). Their Fourier supports are disjoint and they lie in the positive and negative spectral subspaces respectively. For 0≤λ,μ≤1,

\[
C_a(t)=P_-+\lambda|V_p(t)\rangle\langle V_p(t)|
-\mu|V_h(t)\rangle\langle V_h(t)|.
\]

This is a positive contraction: the added positive mode has occupation λ, the affected negative mode has remaining occupation 1−μ, and all orthogonal spectral modes retain their ground occupations. The negative update is permitted because it removes occupation from a filled mode. A negative rank-one term on an arbitrary vector would not automatically preserve positivity.

Thus Cₐ defines an actual gauge-invariant quasifree state evolving under the Wilson Hamiltonian. The covariance difference Cₐ−P₋ is signed; it must not be treated as the positive excitation kernel of steps 31–33. The relative number is λ−μ, whereas the excitation number relative to the sea counts λ+μ. Neither is a new degree of freedom in addition to the CAR state.

## 2. Exact two-site composite and sign change

Let zₚ,zₕ denote the packets' upper components. The signed kernel is

\[
K_a(x,y)=\lambda z_p(x)\overline{z_p(y)}-\mu z_h(x)\overline{z_h(y)}.
\]

For h=na and x±=x±h/2, the exact Wick expression for the ground-subtracted current product π(n₊−1/2)(n₋−1/2)/a² is

\[
\Delta S_{a,n}
=W_n\frac{\lambda\operatorname{Im}[\overline{z_p(x_-)}z_p(x_+)]
-\mu\operatorname{Im}[\overline{z_h(x_-)}z_h(x_+)]}{h}
+G_{a,h},
\qquad W_n=\frac{n^2}{n^2-1/4},
\]

\[
G_{a,h}=-\pi\lambda\mu
|z_p(x_+)z_h(x_-)-z_h(x_+)z_p(x_-)|^2.
\]

The Gram-determinant algebra survives with signed weights; its positivity does not. Here G is generally negative. Simply carrying over the earlier nonnegative remainder claim would therefore be wrong. The code retains this finite-spacing correction and checks the full expression against the actual two-mode Fock observable.

For real mirrored amplitudes, zₕ=conj(zₚ), while the lower spinor obeys vₕ↓=−conj(vₚ↓). The hole's upper-component local chiral density is the negative of the particle's before applying the negative covariance weight. In particular the limiting relative stress is

\[
t(x,t)=(\lambda+\mu)\operatorname{Im}[\overline{v(x,t)}\partial_xv(x,t)],
\]

with v the continuum positive packet. The two excitations add in energy rather than canceling with their relative particle numbers.

As in earlier rounds, the two endpoints must be actual lattice sites. An arbitrary evaluation of a Fourier interpolant is not itself a lattice observable; use translated lattices or admissible approaching midpoints, with the positional error included when fixing an external continuum point.

## 3. Absolute remainder control and limit

Use the packet moments Bⱼ and rank-one error bound E₁(a,n,t) established in step 30. The mirrored hole has identical absolute derivative moments, so

\[
|G_{a,h}|\leq\pi\lambda\mu h^2(2B_0B_1)^2,
\]

\[
|\Delta S_{a,n}-t(x,t)|
\leq(\lambda+\mu)E_1(a,n,t)
+\pi\lambda\mu h^2(2B_0B_1)^2.
\]

Therefore a→0, h→0, n→∞ gives the local current limit, uniformly in position on bounded time intervals. Fixed n retains Wₙt. No claim is made of uniformity over unbounded time, arbitrary momentum occupation, or non-smooth excitation kernels.

More generally, for finitely many mutually orthonormal positive particles and negative holes, write signed weights wᵢ=σᵢλᵢ with σᵢ=±1. The determinant term is

\[
\pi\sum_{i<j}w_iw_j
|z_i(x_+)z_j(x_-)-z_j(x_+)z_i(x_-)|^2.
\]

Its absolute value is bounded by replacing wᵢwⱼ with |wᵢwⱼ| in the finite-rank bound. The linear estimates likewise use absolute weights, while the target keeps their signs. This yields the finite-rank signed extension whenever spectral filling/removal gives a positive covariance. An infinite-rank signed extension needs summability of these absolute-weight derivative bounds and explicit ultraviolet preparation as appropriate; it is not asserted for arbitrary signed kernels. The executable witness here is the two-mode mirrored case.

## 4. Independent energy and neutral excitation

The implementation evaluates the Hamiltonian image of both packets by direct signed spectral integration, including both spin components. The local relative energy is

\[
\epsilon_a(x,t)=\lambda\operatorname{Re}\sum_s\overline{v_{p,a,s}}(H_av_{p,a})_s
-\mu\operatorname{Re}\sum_s\overline{v_{h,a,s}}(H_av_{h,a})_s.
\]

The negative signed energy of the removed mode makes the hole contribution positive after ground subtraction. Mirror symmetry gives εₐ=(λ+μ)εₐ,particle, which the direct calculation checks. The same compact-band estimates give εₐ→t. Integrated energy is (λ+μ)∫Eₐ(k)|f(k)|²dk→2(λ+μ).

At λ=μ=1 the relative particle number is zero but the total excitation energy is 4, not 0. The two-site diagonal occupations return to 1/2 in this symmetric case, but off-diagonal correlations change and the state is not the vacuum. Half filling, charge neutrality, and ground-state identity are distinct properties. For hole-only preparation the local diagonal covariance decreases below 1/2 while remaining positive, explicitly demonstrating why a positive-update assumption is unavailable.

The continuum energy density is transported as t(x,t)=t(x−t,0). This is a relative expectation-level result, not a finite-spacing identity between current and energy operators, a unique lattice density prescription, or a derivation of a full stress tensor.

## 5. Checks and scope

`model.py` implements the mirrored spectral packets, signed covariance, exact linear and signed determinant terms, absolute bounds, and independent local Hamiltonian action. Twenty-four tests cover negative-band eigenvectors, spectral positivity, compressed-state positivity, general finite-Fock expectation, determinant sign and algebra, bounds and limits, hole-only/particle-only reductions, neutral positive-energy excitation, and Hamiltonian agreement. `enumeration.json` records convergence and the finite-CAR witness. Numerical quadrature is not interval-certified; the stated analytic bounds control lattice and point-separation errors, not automatic numerical integration errors.

The shared ground subtraction now works for these controlled additions **and removals** of occupation. Particle/hole coherences, nonquasifree correlations, arbitrary infinite-density states, absolute curved stress and anomaly, interactions, geometry dynamics, actual physical state selection, and phenomenal constitution remain additional obligations. Neither a neutral excitation nor a stress limit selects a phenomenal episode or establishes the physical framework as actual.

## Continuation

[Step 35](../wilson_coherent_rotation/REPORT.md) includes coherent mixing between a filled negative mode and an empty positive mode, with projection positivity and phase-sensitive local energy.
