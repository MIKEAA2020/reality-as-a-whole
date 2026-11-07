# Step 32 — Infinite-rank excitations with controlled local mode tails

## Result

An explicit infinite-rank, trace-class positive-energy excitation of the Wilson ground state has a controlled local relative current limit. Both its lattice composite and its continuum target admit mode-cutoff bounds that do not diverge as inverse lattice area. The rank cutoff, lattice spacing, and point separation can therefore be removed jointly under stated conditions.

This extends [step 31](../wilson_multimode_composite/REPORT.md) beyond fixed finite rank. It does not remove compact momentum support, quasifreeness, positive-energy-only excitation, or the reference-ground subtraction. Infinite rank here does **not** mean infinite expected particle number or a thermodynamic finite-density state.

## 1. An actual infinite-rank state

For i=0,1,… put dᵢ=2⁻ⁱ⁻¹, lᵢ=1+dᵢ, λᵢ=dᵢ, and define an amplitude supported on [lᵢ,lᵢ+dᵢ] by

\[
f_i(l_i+d_i z)=\sqrt{30/d_i}\,z(1-z),\qquad 0\leq z\leq1.
\]

Each amplitude has unit L² norm because 30∫₀¹z²(1−z)²dz=1. Their bands are disjoint except for measure-zero boundaries, so the amplitudes are orthonormal. All bands lie in (1,2]. Every λᵢ is positive and their sum is 1.

Use the same Wilson positive-energy spinor and exact spectral evolution as step 30. For 2a<π, all modes are strictly inside the Brillouin zone. Their full lattice vectors Vᵢ,ₐ are orthonormal by Fourier Parseval. Thus

\[
T_a(t)=\sum_{i\geq0}\lambda_i|V_{i,a}(t)\rangle\langle V_{i,a}(t)|,
\qquad C_a(t)=P_-+T_a(t)
\]

converges in trace norm for the excitation operator Tₐ, has infinite rank, and satisfies 0≤Cₐ≤I. This defines a gauge-invariant quasifree state of the actual infinite lattice, with exact Hamiltonian evolution. The unfilled positive subspace is not silently assigned arbitrary extra occupation. The excitation trace is 1; the sea filling itself is not trace class.

For the first N modes, ∥Tₐ−Tₐ,N∥₁=2⁻ᴺ, uniformly in a and time. This fact establishes a controlled state approximation, but alone is insufficient to control the current composite, whose norm grows as a⁻². The additional local estimates below are essential.

The same construction works more generally for a positive trace-class occupation operator on a fixed compact positive-momentum band: spectral diagonalization gives orthonormal modes with summable occupations. Cauchy–Schwarz bounds their momentum L¹ moments uniformly, providing the summability required below. The explicit disjoint-band family gives particularly transparent tails and is the implemented witness, not an enumeration of all such operators.

## 2. Summable local moments

Write vᵢ,ₐ for the upper packet component and set

\[
B_{i,j}=\frac1{\sqrt{2\pi}}\int |f_i(k)|k^j dk.
\]

Cauchy–Schwarz on a band of width dᵢ, with k≤2, gives

\[
B_{i,j}\leq2^j\sqrt{d_i/(2\pi)}.
\]

Consequently, for any nonnegative integers j,k,

\[
\sum_{i\geq N}\lambda_i B_{i,j}B_{i,k}
\leq M_{j+k}(N),\qquad
M_q(N)=\frac{2^q4^{-N}}{6\pi}.
\]

These bounds control the kernels, derivatives, and all positive pair sums needed for the composite. In particular the infinite sums and their stated derivatives converge uniformly in position and on bounded time intervals. This justifies taking the finite-rank formulas to infinite rank, rather than assuming convergence from the mode labels alone.

## 3. Infinite-rank composite and continuum limit

Let h=na, Wₙ=n²/(n²−1/4), and zᵢ=vᵢ,ₐ↑. The exact infinite-rank relative current is the absolutely convergent expression

\[
\Delta S_{a,n}=W_n\sum_i\lambda_i
\frac{\operatorname{Im}[\overline{z_i(x-h/2)}z_i(x+h/2)]}{h}
+\pi\sum_{i<j}\lambda_i\lambda_j
|z_i(x+h/2)z_j(x-h/2)-z_j(x+h/2)z_i(x-h/2)|^2.
\]

It is the Wick expectation of the same actual two-site observable with the same ground reference, not a new observable defined by this sum. As in earlier rounds, endpoints must be actual lattice sites; translated lattices or controlled approaching midpoints are required when fixing a desired continuum point.

For the infinite continuum packet family define

\[
t(x,t)=\sum_i\lambda_i\operatorname{Im}[\overline{v_i(x,t)}\partial_xv_i(x,t)].
\]

Let Mq denote Mq(0). Summing the derivative/dispersion estimates of step 30 and the pair bound of step 31 gives

\[
|\Delta S_{a,n}-t|\leq E_{a,h,n}(t),
\]

\[
E_{a,h,n}(t)=W_n\left[h^2M_3(1/24+1/8)
+a^2(M_3/16+|t|M_4/12)\right]
+(W_n-1)M_1+2\pi h^2M_0M_2.
\]

The pair term follows from (ab+cd)²≤2a²b²+2c²d² and summation over pairs; it does not require a finite number of modes. Hence a→0, h→0, n→∞ proves the infinite-rank local limit uniformly in x and on bounded time intervals. Fixed n instead leaves the same Wₙ factor. No uniformity for unbounded times or unbounded momentum bands is asserted.

## 4. Removing the numerical mode cutoff jointly

Let ΔSᴺ and tᴺ retain the first N modes. Their omitted continuum target is bounded by

\[
|t-t^N|\leq M_1(N).
\]

Using the local derivative bound for each term, not the diverging observable norm, gives

\[
|\Delta S_{a,n}-\Delta S^N_{a,n}|
\leq W_nM_1(N)+2\pi h^2[M_0(N)M_2(0)+M_0(0)M_2(N)]
=:R_{a,h,n}(N).
\]

The second term bounds all Gram pairs involving at least one omitted mode. These are uniform in position and time. In particular N→∞ can be taken jointly with the mesoscopic spacing limit without requiring 2⁻ᴺ/a²→0. The computational truncation of a bounded-moment excitation is controlled by R, not by an invalid application of fixed-observable convergence to a cutoff-dependent operator.

The code evaluates finite-mode integrals on the fixed interval z∈[0,1] to avoid cancellation from ever-narrower momentum bands. Its numerical index cap of 128 is an implementation bound only; the analytic state and estimates use all nonnegative indices. Quadrature errors are separate from the omitted-mode bounds and are not interval-certified.

## 5. Independent energy and transport

The continuum symmetrized Hamiltonian density for each right-moving packet is Im(v̄ᵢ∂ₓvᵢ). The summable moments justify its weighted sum and transport law (∂ₜ+∂ₓ)t=0. Orthogonality gives the independently computed total excitation energy

\[
\sum_i\lambda_i\int k|f_i(k)|^2dk
=\sum_i d_i(1+3d_i/2)=3/2.
\]

The total expected number is 1, despite infinite rank. The omitted integrated energy after N modes is at most 2·2⁻ᴺ. For the Wilson Hamiltonian the integrated relative energy is ∑λᵢ∫Eₐ(k)|fᵢ|²dk and converges to 3/2 by the uniform compact-band dispersion estimate. The corresponding local symmetrized spectral energy converges by the same weighted moment bounds: upper-component errors are O(a²) and lower-component contributions are O(a²). This is an expectation-level relative result, not a unique lattice energy-density prescription or a full stress Ward identity.

## 6. Checks and boundaries

`model.py` implements the disjoint-band states, exact finite-mode Wick formula, uniform infinite-rank error bound, and omitted-mode bounds. Twenty-four tests check normalization, orthogonality through disjoint support, trace tails, packet derivatives, cutoff bounds, Gram positivity, joint rank/spacing convergence, actual finite-Fock expectation, and total continuum energy. `enumeration.json` records cutoff and mesoscopic diagnostics.

The result establishes a summable infinite-rank bridge within a fixed compact positive-energy band. It does not claim ultraviolet removal for arbitrary occupation tails, infinite-density states, holes, nonquasifree correlations, general full stress operators, absolute curved renormalization, interactions, or backreaction. A common vacuum subtraction works for this controlled excitation class; it does not derive the anomaly or select the actual physical state. The physical-actuality and phenomenal-constitution obligations remain independent.

## Continuation

[Step 33](../wilson_ultraviolet_tails/REPORT.md) removes the fixed compact continuum momentum band for a weighted-moment excitation family, with an explicit growing-window lattice preparation and joint ultraviolet tail bound.
