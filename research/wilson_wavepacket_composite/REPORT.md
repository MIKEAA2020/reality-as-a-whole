# Step 30 — A spatially varying, time-dependent Wilson wavepacket composite

## Result

A normalized positive-energy wavepacket of the infinite massless Wilson Hamiltonian defines an actual positive quasifree excitation of its ground state. Its time-dependent, spatially varying current-product expectation has an explicitly bounded mesoscopic limit. That limit equals the continuum packet's local chiral energy density, independently obtained from the one-particle Hamiltonian.

This removes homogeneity and stationarity for a **rank-one, compact-momentum excitation**. It does not establish arbitrary-state local renormalization, absolute stress, curved anomalies, massive/interacting dynamics, or backreaction.

## 1. Positive state and exact evolution

Retain the Hamiltonian, ground covariance P₋, and ground same-component kernel of [step 28](../wilson_thermal_composite/REPORT.md). For positive physical momentum 1≤k≤3 and a·3<π, its positive-energy eigenvector and energy are

\[
u_a(k)=\begin{pmatrix}\cos(ak/4)\\\sin(ak/4)\end{pmatrix},\qquad
E_a(k)=2\sin(ak/2)/a.
\]

Choose the real compact-support amplitude

\[
f(k)=\frac{\sqrt{15}}4(k-1)(3-k)\,1_{[1,3]}(k),
\qquad \int |f(k)|^2dk=1.
\]

Define a bandlimited interpolant and its lattice vector by

\[
v_a(x,t)=\frac1{\sqrt{2\pi}}\int_1^3 f(k)u_a(k)e^{ikx-iE_a(k)t}\,dk,
\qquad V_{a,j}(t)=\sqrt a\,v_a(aj,t).
\]

Discrete Fourier Parseval gives ∥Vₐ∥=1: the support lies strictly inside the physical Brillouin zone and the spinor has unit norm. It is in the positive spectral subspace and evolves with the actual Wilson Hamiltonian. For 0≤λ≤1,

\[
C_a(t)=P_-+\lambda|V_a(t)\rangle\langle V_a(t)|
\]

is a positive contraction: its ground negative subspace stays filled and a single orthogonal positive mode has occupation λ. Thus it defines a gauge-invariant quasifree CAR state. At λ=1 it is the one-particle excitation; for intermediate λ it is partial occupation of that mode. Its covariance is not stationary because the packet contains a range of energies. The ground is stationary but the excitation is not.

## 2. The actual composite and a useful cancellation

Take two upper-component sites at x±h/2, h=na, and the same observable as before,

\[
O_{a,n}=\frac\pi{a^2}(n_+-1/2)(n_--1/2),
\qquad \|O_{a,n}\|=\frac\pi{4a^2}.
\]

The two sites must belong to the chosen lattice. One can center a translated lattice at each chosen midpoint; on a single fixed-origin lattice, select admissible midpoints approaching x and include their positional error. The interpolated formula is otherwise defined for every real x, but that alone does not make every interpolated point a lattice observable.

Write v for the upper component of vₐ. The ground diagonal occupations are 1/2 and the ground off-diagonal is −iaWₙ/(2πh), Wₙ=n²/(n²−1/4), with row order (+,−). Wick's rule gives

\[
\langle(n_+-1/2)(n_--1/2)\rangle
=(C_{++}-1/2)(C_{--}-1/2)-|C_{+-}|^2.
\]

The diagonal occupation correction is now nonzero; the half-filled density formula used in earlier rounds cannot be reused. However the two terms quadratic in λ cancel exactly because the covariance update has rank one. Consequently the exact relative expectation is

\[
\Delta S_{a,n}(x,t)
=\lambda W_n\frac{\operatorname{Im}[\overline{v_a^\uparrow(x-h/2,t)}v_a^\uparrow(x+h/2,t)]}{h}.
\]

The implementation uses a general two-mode quasifree density matrix to verify this against the actual finite Fock observable, rather than assuming half filling for the excited state.

## 3. Uniform local estimate on bounded time intervals

The continuum packet has only an upper component,

\[
v(x,t)=\frac1{\sqrt{2\pi}}\int_1^3 f(k)e^{ik(x-t)}dk,
\qquad t_v(x,t)=\lambda\operatorname{Im}[\overline v\,\partial_xv].
\]

For j≥0 set

\[
B_j=\frac1{\sqrt{2\pi}}\int_1^3 |f(k)|k^j dk,
\quad D_j(t)=B_{j+2}/32+|t|B_{j+3}/24.
\]

The inequalities |cos(ak/4)−1|≤a²k²/32 and |Eₐ(k)−k|≤a²k³/24 imply, uniformly in x,

\[
|\partial_x^jv_a^\uparrow-\partial_x^jv|\leq a^2D_j(t),
\qquad |\partial_x^jv_a^\uparrow|\leq B_j.
\]

A symmetric Taylor expansion of the product at separation h gives a remainder bounded by h²K after division by h, where

\[
K=B_0B_3/24+B_1B_2/8.
\]

Indeed the third derivative of the two-point product has modulus at most B₀B₃/4+3B₁B₂/4; its constant term is real and its first imaginary derivative is Im(v̄v′). Combining the two estimates gives

\[
|\Delta S_{a,n}-t_v|
\leq\lambda\left\{W_n\left[h^2K+a^2(D_0B_1+B_0D_1)\right]
+(W_n-1)B_0B_1\right\}.
\]

Hence a→0, h→0, n→∞ proves the desired local composite limit, uniformly in position and on bounded time intervals. Fixed n instead retains Wₙtᵥ. The estimate does not assert uniformity for arbitrarily long times. On a fixed-origin lattice, a midpoint displacement δx contributes at most λ(B₁²+B₀B₂)|δx| to the comparison with the desired continuum point.

## 4. Independently computed energy and transport

For continuum H=−i∂ₓ on this chiral sector, the symmetrized local energy is

\[
\lambda\operatorname{Re}(\overline vHv)
=\lambda\operatorname{Im}(\overline v\partial_xv)=t_v.
\]

It is obtained from H, not defined using the current product. Since v(x,t)=v(x−t,0), this density obeys (∂ₜ+∂ₓ)tᵥ=0. Its integrated energy is λ∫k|f(k)|²dk=2λ, with normalization and mean momentum evaluated independently.

A corresponding lattice diagnostic is λ Re∑ₛ v̄ₐ,ₛ(Hₐvₐ)ₛ at the interpolated coordinate, or that value at an actual site. Compact momentum support gives uniform local convergence to tᵥ: the upper component and its Hamiltonian image converge, while the lower component and its image are O(a). The implementation evaluates the spectral Hamiltonian action directly and checks the agreement numerically. This particular symmetrized density is not claimed to be a uniquely selected lattice stress density or a full finite-spacing continuity/Ward construction. Its total lattice energy is λ∫Eₐ(k)|f(k)|²dk→2λ by Parseval.

## 5. What is established and what is not

`model.py`, `test_model.py`, and `enumeration.json` supply the packet, spectral evolution, covariance, general two-mode density, exact composite formula, analytic bound, and Hamiltonian energy diagnostics. Twenty-four tests cover normalization, positive-energy spinors, transport and time variation, convergence bounds, state positivity, actual finite-Fock expectation, occupation-weight linearity, energy, and quadrature refinement. Numerical Simpson checks support the formulas but do not replace the analytic proof or constitute certified quadrature intervals.

The new arrow is **a nonstationary Hamiltonian state → a controlled spatially local relative composite**. It is stronger than matching equilibrium energies, but the exact rank-one cancellation is a substantive restriction. General finite-rank/many-body excitations, full stress correlations and conservation identities, common state-independent subtraction, absolute curved stress, dynamics of geometry, actual physical selection, and phenomenal constitution are not inferred.

## Continuation

[Step 31](../wilson_multimode_composite/REPORT.md) treats fixed finite-rank positive-energy excitations. It retains and bounds the extra Gram-determinant term rather than assuming the rank-one cancellation persists.
