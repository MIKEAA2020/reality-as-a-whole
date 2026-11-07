# Step 31 — Finite-rank wavepacket composites beyond exact rank-one cancellation

## Main result

The local relative stress limit survives multiple occupied positive-energy Wilson wavepackets. The extra finite-separation term is a nonnegative Gram determinant. It need not vanish at finite spacing, but smoothness bounds it by O(h²), where h is the point separation. The continuum limit is the sum of the packets' independently defined chiral Hamiltonian energy densities.

The proof covers any fixed finite number of orthonormal compact-positive-momentum packets with sufficient integrable momentum moments. The executable model checks two explicit orthonormal packets. This is not a theorem uniform in particle number or momentum support, nor a theorem for arbitrary states or full stress correlations.

## 1. A positive many-mode state

Use the positive spectral spinor and energy from [step 30](../wilson_wavepacket_composite/REPORT.md). Choose orthonormal amplitudes fᵢ in a fixed compact interval [k₀,k₁] with k₀>0 and ak₁<π. Define

\[
v_{i,a}(x,t)=\frac1{\sqrt{2\pi}}\int f_i(k)u_a(k)e^{ikx-iE_a(k)t}dk,
\qquad V_{i,a,j}=\sqrt a\,v_{i,a}(aj,t).
\]

Fourier Parseval preserves orthonormality of the full two-component lattice modes: the common spinor has unit norm. Their positive-energy subspace is orthogonal to the ground filling P₋. Thus, for a fixed finite N and 0≤λᵢ≤1,

\[
C_a(t)=P_-+\sum_{i=1}^N\lambda_i|V_{i,a}(t)\rangle\langle V_{i,a}(t)|
\]

is a positive contraction defining a gauge-invariant quasifree CAR state. Its evolution is the actual Hamiltonian evolution. All λᵢ=1 gives a finite Slater excitation above the sea; partial occupation need not give a pure state. Positivity depends on orthonormality (or an equivalent contraction condition), not merely on each update having a positive coefficient.

The implemented pair is

\[
f_0(k)=\frac{\sqrt{15}}4(k-1)(3-k)1_{[1,3]}(k),
\qquad f_1(k)=\sqrt7(k-2)f_0(k).
\]

The first squared amplitude has mean k=2 and variance 1/7, so both modes are normalized and orthogonal. Their full spinors remain orthonormal even though their upper-component restrictions need not be. Each continuum packet has mean energy 2 in the declared units.

## 2. Exact finite-spacing current formula

Let zᵢ(x,t) denote the upper component of vᵢ,ₐ and set

\[
K_a(x,y)=\sum_i\lambda_i z_i(x)\overline{z_i(y)},
\quad x_\pm=x\pm h/2,\quad h=na,\quad W_n=\frac{n^2}{n^2-1/4}.
\]

The lattice two-mode covariance update is aKₐ. The unchanged ground diagonal is 1/2 and its (+,−) entry is −iaWₙ/(2πh). Wick's rule for the same observable π(n₊−1/2)(n₋−1/2)/a² gives the exact relative expectation

\[
\Delta S_{a,n}
= W_n\sum_i\lambda_i\frac{\operatorname{Im}[\overline{z_i(x_-)}z_i(x_+)]}{h}
+\pi\left[K_a(x_+,x_+)K_a(x_-,x_-)-|K_a(x_+,x_-)|^2\right].
\]

The second term is not discarded or absorbed into the definition of stress. The Gram determinant identity expresses it as

\[
G_{a,h}=\pi\sum_{i<j}\lambda_i\lambda_j
|z_i(x_+)z_j(x_-)-z_j(x_+)z_i(x_-)|^2.
\]

For one occupied mode it vanishes identically, recovering step 30. For two modes it is generally positive, and the exact current is not additive in their occupations at finite separation. This is a Wick/exclusion contribution to this composite, not an interaction added to the free Hamiltonian.

As before the endpoints must be actual lattice sites. Translated lattices can have a specified midpoint; on a fixed-origin lattice use admissible approaching midpoints and include positional error. Evaluating an interpolant at an arbitrary real coordinate is not itself a new lattice observable.

## 3. Why the extra term vanishes

For each packet put

\[
B_{i,j}=\frac1{\sqrt{2\pi}}\int |f_i(k)|k^j dk,
\quad D_{i,j}(t)=B_{i,j+2}/32+|t|B_{i,j+3}/24,
\quad Q_i=B_{i,0}B_{i,3}/24+B_{i,1}B_{i,2}/8.
\]

Compact support guarantees the moments used below. The derivative and dispersion estimates of step 30 apply separately to every packet, without requiring fᵢ to be real. In particular |zᵢ|≤Bᵢ,₀ and |∂ₓzᵢ|≤Bᵢ,₁. Subtracting values across the interval of length h shows

\[
|z_i(x_+)z_j(x_-)-z_j(x_+)z_i(x_-)|
\leq h(B_{i,0}B_{j,1}+B_{j,0}B_{i,1}).
\]

Consequently

\[
0\leq G_{a,h}\leq\pi h^2\sum_{i<j}\lambda_i\lambda_j
(B_{i,0}B_{j,1}+B_{j,0}B_{i,1})^2=:G^{\rm bound}_h.
\]

Let vᵢ be the continuum upper packet and let

\[
t(x,t)=\sum_i\lambda_i\operatorname{Im}[\overline{v_i(x,t)}\partial_xv_i(x,t)].
\]

The full error is bounded by

\[
|\Delta S_{a,n}-t|\leq G^{\rm bound}_h+
\sum_i\lambda_i\left\{W_n[h^2Q_i+a^2(D_{i,0}B_{i,1}+B_{i,0}D_{i,1})]
+(W_n-1)B_{i,0}B_{i,1}\right\}.
\]

For fixed finite N, fixed amplitudes and occupations, this tends to zero as a→0, h→0, n→∞. It is uniform in x and on bounded time intervals. Fixed n instead leaves Wₙt; the Gram term still vanishes. The estimate is not uniform over arbitrary high-frequency packets, growing rank, or unbounded times. Those limits require additional summability and uniformity hypotheses, not a silent interchange of limits.

## 4. Independent energy, transport, and subtraction

The continuum one-particle Hamiltonian is −i∂ₓ on these positive right-moving modes. Its local symmetrized expectation is exactly t above; it is linear in the one-particle covariance. Since each vᵢ(x,t)=vᵢ(x−t,0), (∂ₜ+∂ₓ)t=0. The total relative energy is ∑λᵢ∫k|fᵢ|²dk; for the implemented pair it is 2(λ₀+λ₁).

The code also evaluates the local symmetrized Wilson Hamiltonian diagnostic by spectral action, independently of the current formula. Each upper-component contribution converges and each lower-component contribution vanishes, so their finite sum approaches t. No finite-spacing identity between the two local expressions is asserted, nor is this density claimed to be uniquely selected by a lattice Ward identity.

All states in this finite-rank class use the same ground reference and same lattice composite; no packet-dependent counterterm is introduced. This is a shared **relative subtraction within a restricted excitation class**, not a construction of an absolute anomaly or a general locally covariant stress operator. The observable norms still diverge as a⁻²: the displayed bounds, rather than fixed-observable state convergence, justify the limit.

## 5. Executable checks and remaining obligations

`model.py` implements two orthonormal packets, occupation-weighted kernels, linear and Gram contributions, two-mode covariances, bounds, and independent energy. Twenty-four tests check orthonormality, spectral packet representation, positivity, general Fock density and two-point reconstruction, actual composite expectation, the Gram identity, nonadditivity at finite separation, quadratic suppression, full error bounds, fixed-site and mesoscopic limits, and energy agreement. `enumeration.json` records convergence and the finite-CAR witness. Quadrature is numerical and not interval-certified; the analytic estimates do not rely on the sample table.

The result removes the exact-rank-one-cancellation restriction for fixed finite-rank positive-energy quasifree excitations. Infinite-rank/infinite-density bounds, holes and general coherences, nonquasifree correlations, full stress operator distributions and Ward identities, massive/curved absolute stress, interactions, gravitational dynamics, physical actuality, and phenomenal constitution remain separate obligations. In particular no statement about subject boundaries or phenomenal identity follows from a free-field stress limit.

## Continuation

[Step 32](../wilson_infinite_rank/REPORT.md) removes fixed finite rank for a compact-band trace-class class, using summable local moments and explicit mode-tail bounds.
