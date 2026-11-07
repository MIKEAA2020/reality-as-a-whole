# Step 35 — Coherent particle–hole rotation and local interference

## Result

A finite-rank unitary rotation of the filled sea gives a pure quasifree state with particle–hole coherence. Its local current composite has an explicitly bounded mesoscopic limit equal to the independently evaluated local Hamiltonian energy. The local limit depends on a coherence phase even though total energy and relative particle number do not.

This extends [step 34](../wilson_particle_hole/REPORT.md) beyond occupation-diagonal particle/hole changes. It does not establish arbitrary coherent infinite-rank states, nonquasifree stress formulas, full Ward identities, or absolute curved stress.

## 1. Positivity by rotation, not by diagonal occupation

Use a positive-energy packet p with normalized amplitude f(k) on [1,3], as in step 30. The hole packet h instead has negative momentum q=−(k+1), k∈[1,3], with the same amplitude f(k). Its band is [−4,−2]. The unequal energy magnitudes avoid a special mirror symmetry that would cancel local energy interference pointwise.

For either signed momentum q, the relevant Wilson spinor and signed eigenvalue are

\[
u_a(q)=(\cos(aq/4),\sin(aq/4))^T,
\qquad \varepsilon_a(q)=2\sin(aq/2)/a.
\]

Assume 4a<π. Fourier Parseval gives orthonormal lattice packets Vₚ,Vₕ in the positive and negative spectral subspaces. They evolve with their actual signed Hamiltonian phases. The sea has occupation matrix diag(0,1) on their span. Replace its occupied vector Vₕ by

\[
W=\sin\theta\,e^{i\phi}V_p+\cos\theta\,V_h,
\quad 0\leq\theta\leq\pi/2.
\]

Then

\[
C_a=P_- - |V_h\rangle\langle V_h|+|W\rangle\langle W|
=P_-+\sum_{i,j\in\{p,h\}}M_{ij}|V_i\rangle\langle V_j|,
\]

\[
M=\begin{pmatrix}s^2&sc e^{i\phi}\\sc e^{-i\phi}&-s^2\end{pmatrix},
\qquad s=\sin\theta,\quad c=\cos\theta.
\]

The full covariance is an orthogonal projection, hence a positive contraction defining a pure gauge-invariant quasifree state. In the two-mode sector C²=C and tr C=1. The relative update is Hermitian and indefinite, with det M=−s². Positivity comes from the rotation of a filled mode, not from positivity of M or from assigning independent diagonal occupations.

At later times W(t)=s e^{iφ}Vₚ(t)+cVₕ(t) gives exact Hamiltonian evolution. This is coherence between distinct one-particle spectral sectors in a number-conserving state, not an anomalous pairing covariance or a change of the CAR.

## 2. Exact local composite

Let zᵢ be the upper packet components and define

\[
K_a(x,y)=\sum_{i,j}M_{ij}z_i(x)\overline{z_j(y)}.
\]

For h=na, x±=x±h/2, and Wₙ=n²/(n²−1/4), the exact ground-subtracted expectation of π(n₊−1/2)(n₋−1/2)/a² is

\[
\Delta S_{a,n}=W_n\frac{\operatorname{Im}K_a(x_+,x_-)}h
+\pi\det\begin{pmatrix}K_a(x_+,x_+)&K_a(x_+,x_-)\\K_a(x_-,x_+)&K_a(x_-,x_-)\end{pmatrix}.
\]

The determinant factors without assuming that M is diagonal:

\[
G_{a,h}=-\pi s^2
|z_p(x_+)z_h(x_-)-z_h(x_+)z_p(x_-)|^2.
\]

The coefficient is −s², not the −s⁴ that would result from keeping only the diagonal particle/hole weights. Coherence changes the exact finite-spacing formula and the limiting linear term. The implementation checks the full expression against the actual two-mode Fock observable and reconstructs its two-point covariance.

The endpoints must be actual lattice sites. Translated lattices or approaching admissible midpoints give the stated continuum-point comparison; evaluating an interpolant elsewhere does not automatically produce a lattice observable.

## 3. Explicit bound for the coherent limit

Let vᵢ be the continuum upper packets. Define

\[
t_M(x,t)=\operatorname{Im}\sum_{i,j}M_{ij}
(\partial_xv_i)\overline{v_j}.
\]

Put Bᵢ,ⱼ=(2π)⁻¹ᐟ²∫|fᵢ(q)||q|ʲdq and Dᵢ,ⱼ=Bᵢ,ⱼ₊₂/32+|t|Bᵢ,ⱼ₊₃/24. The packet error is bounded by a²Dᵢ,ⱼ as before, including the negative-momentum packet. Define

\[
Q_M=\frac1{48}\sum_{i,j}|M_{ij}|
(B_{i,3}B_{j,0}+3B_{i,2}B_{j,1}+3B_{i,1}B_{j,2}+B_{i,0}B_{j,3}),
\]

\[
D_M=\sum_{i,j}|M_{ij}|(D_{i,1}B_{j,0}+B_{i,1}D_{j,0}),
\qquad T_M=\sum_{i,j}|M_{ij}|B_{i,1}B_{j,0}.
\]

Hermiticity ensures K(x,x) is real and K(x−h/2,x+h/2)=conj K(x+h/2,x−h/2). A symmetric Taylor estimate thus bounds the imaginary difference quotient without a spurious 1/h divergence. Combining its third-derivative remainder, the spectral packet error, and the determinant gives

\[
|\Delta S_{a,n}-t_M|
\leq W_n(h^2Q_M+a^2D_M)+(W_n-1)T_M
+\pi s^2h^2(B_{p,0}B_{h,1}+B_{h,0}B_{p,1})^2.
\]

Therefore a→0, h→0, n→∞ yields the local limit uniformly in position on bounded time intervals. Fixed n retains WₙtM. This is a controlled coherent finite-rank result, not a bound uniform over arbitrary coherence kernels or unlimited times.

## 4. Interference, independent energy, and transport

The implementation computes the local symmetrized Wilson Hamiltonian diagnostic independently by signed spectral action on both spin components:

\[
\epsilon_a(x,t)=\operatorname{Re}\sum_{i,j,s}
M_{ij}\overline{v_{j,a,s}}(H_av_{i,a})_s.
\]

Its upper component tends to Re∑Mᵢⱼ v̄ⱼ(−i∂ₓ)vᵢ=tM, and its lower contribution vanishes by compact-band estimates. This establishes agreement with a Hamiltonian expression rather than defining energy from the current product. No finite-spacing operator identity or uniquely selected lattice density is claimed.

The off-diagonal terms contribute to tM. In the continuum vₕ(x,t)=exp[−i(x−t)]conj(vₚ(x,t)), so the extra phase factor prevents the pointwise cancellation in the exactly mirrored example of step 34. Tests compare different φ and compare the coherent local energy with the occupation-diagonal value. Both distinguish the local stress.

Globally the cross terms integrate to zero because the positive and negative packet supports are orthogonal and the Hamiltonian preserves their spectral sectors. The relative number is tr M=0 and total continuum energy is

\[
\Delta E=s^2(\langle p,Hp\rangle-\langle h,Hh\rangle)
=5\sin^2\theta,
\]

independent of φ. The lattice total energy is computed by its own dispersion integral and tends to this value. At the default θ=π/4 it is 5/2. Local interference therefore carries information not fixed by total energy or charge. Both continuum packets translate to the right, yielding (∂ₜ+∂ₓ)tM=0.

Discarding off-diagonal covariance entries loses this information. One must also distinguish the quasifree state of the diagonalized covariance from a literal phase average of the full pure many-body state: the latter need not be quasifree. The theorem here does not apply Wick's rule to that phase-averaged state without checking its higher correlations.

## 5. Verification and boundaries

`model.py` implements the coherent Hermitian update, exact packet evolution, local current and determinant, error bound, and independent local/total Hamiltonian energy. Twenty-four tests check projection/positivity, phase-sensitive interference, determinant algebra, finite-Fock expectation and two-point reconstruction, bounds, mesoscopic and fixed-site limits, energy, translation, and quadrature refinement. `enumeration.json` records phase and convergence diagnostics. Numerical integrals are not interval-certified; the analytic bounds do not automatically certify quadrature errors.

The surviving result is a coherent state-to-local-composite bridge within a finite-rank free-field class. It does not select the physical coherence phase, extend automatically to nonquasifree correlations, construct a full stress operator distribution or absolute anomaly, or supply interactions, backreaction, physical actuality, or phenomenal constitution. Compatibility of these constructions remains distinct from their actual realization.

## Continuation

[Step 36](../wilson_nonquasifree_mixture/REPORT.md) constructs the actual nonquasifree phase mixture and separates its connected four-point contribution from the quasifree state of its mean covariance.
