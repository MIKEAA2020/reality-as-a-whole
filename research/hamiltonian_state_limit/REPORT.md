# Constructive step 23: a gap-controlled curved-background lattice-state limit

## Result and scope

[Step 22](../curved_dirac/REPORT.md) gave a curved Dirac propagator limit but explicitly withheld a lattice-vacuum theorem. Here a **different Hamiltonian regulator** supplies that missing type of result: a uniform spectral gap and core consistency imply convergence of negative-energy projections, hence convergence of quasifree states and fixed bounded finite-time correlations.

This is not a proof about the variable walk's principal-quasienergy polarization. The new regulator has continuous time, central spatial differences, ultraviolet doubling, and nonzero finite-spacing propagation tails. Those differences are retained rather than hidden by calling every regulator “the same lattice theory.”

The result is a conditional free-field state limit on the specified static background. It does not prove an interacting universality class, stress-energy renormalization, Hadamard regularity, backreaction, or physical actuality. Thirty-two finite tests accompany the analytic infinite-line argument.

## 1. The regulator and its precise relation to the previous model

Retain m>0 and the global static geometry Ω(x)=1+ε cos(qx), |ε|<1, q>0. In the rescaled Cauchy Hilbert space H=L²(R,C²), the continuum generator is

\[
H=-iZ\partial_x+M(x)X,\qquad M=m\Omega.
\]

Let H_a=ℓ²(Z,C²), with compact-cell isometry J_a and averaging adjoint S_a from step 18. Define the central-difference momentum and static lattice Hamiltonian

\[
(p_a u)_j=\frac{u_{j+1}-u_{j-1}}{2ia},\qquad
H_a^{\rm lat}=p_a Z+M(aj)X.
\]

For each a it is bounded self-adjoint. Its continuous-time dynamics is exp(-itH_a^lat), and its ground-state covariance will be its negative spectral projection. It is **not** the logarithm of the coin-then-shift walk. Even for constant mass the symbols differ:

\[
h_a(k)=\frac{\sin(ka)}a Z+mX,
\qquad W_a(k)=e^{-ikaZ}e^{-imaX}.
\]

The physical coupling and background remain those chosen in step 22, but the regulator and clock structure have changed. No automatic equivalence of their ultraviolet states is assumed.

## 2. A common Hilbert-space extension with a uniform gap

Write R_a=J_aS_a. On continuum functions the central difference uses translations by exactly a, so it commutes with the cell projection R_a. The sampled mass M_a(x)=M(aj) on each cell also commutes with R_a and satisfies

\[
\|M_a-M\|_\infty\le\tfrac a2\|M'\|_\infty.
\]

For comparison on one H, define

\[
\widehat H_a=(p_aZ+M_aX)R_a+mX(I-R_a).
\]

The first part is exactly J_a H_a^lat J_a*. The second is an artificial gapped complement, chosen only to apply common-space spectral arguments. All pieces reduce R_a, and H-hat_a is bounded self-adjoint for each a.

For zero ε the square of this extension is

\[
(\widehat H_{a,0})^2=p_a^2R_a+m^2I\ge m^2I.
\]

The variable-mass perturbation has norm at most m|ε|, uniformly in a. The same resolvent Neumann-series argument as in step 22 gives

\[
\operatorname{spec}\widehat H_a\cap(-g_*,g_*)=\varnothing,
\qquad g_*=m(1-|\epsilon|)>0.
\]

The restriction H_a^lat inherits this gap; so does the continuum H. This explicit uniform control is what finite-time convergence alone did not provide.

## 3. Core consistency gives strong-resolvent convergence

For f in C_c^∞(R,C²), central differences satisfy p_a f→pf in L², where p=-i∂x. In Fourier space this follows from sin(ak)/a→k and |sin(ak)/a|≤|k|. Moreover

\[
p_aR_af=R_ap_af\longrightarrow pf.
\]

The remaining terms converge because R_af→f, M_a→M in multiplication-operator norm, and the complement term mX(I-R_a)f→0. Therefore

\[
\widehat H_af\longrightarrow Hf
\quad\text{on }C_c^\infty.
\]

This domain is a core for H: the derivative operator has the usual smooth compact core and the potential is bounded. For Im z≠0, on the dense set of vectors (H-z)f from this core,

\[
(\widehat H_a-z)^{-1}(H-z)f-f
=(\widehat H_a-z)^{-1}(H-\widehat H_a)f\longrightarrow0.
\]

Self-adjointness bounds each resolvent by 1/|Im z|, so density extends the conclusion to every fixed vector in H. This proves strong-resolvent convergence directly. It is not an operator-norm convergence claim for the unbounded continuum generators.

## 4. The spectral-state step is now justified

Let C_g=1_(-infinity,0)(H) and C-hat_a=1_(-infinity,0)(H-hat_a). To make the role of the gap explicit, use on core vectors the sign-integral identity

\[
1_{(-\infty,0)}(A)=\tfrac12 I-
\frac1\pi\int_0^\infty A(A^2+s^2)^{-1}\,ds.
\]

For each s>0 the integrand is a combination of resolvents at ±is, so it converges strongly. Near s=0 the uniform gap gives the bound ||A(A²+s²)^-1 f||≤||f||/g_*. For large s, the bound is ||Af||/s². Core consistency ensures that ||H-hat_a f|| remains bounded. Dominated convergence therefore proves

\[
\widehat C_af\longrightarrow C_gf
\]

on the core, and contraction/density extends it to every fixed f in H. The gap and the common-core bounds supply exactly the missing control in passing from dynamics to a discontinuous spectral selection.

For the actual lattice covariance take

\[
C_a^{\rm lat}=1_{(-\infty,0)}(H_a^{\rm lat}).
\]

The common comparison state can use an **empty** complement, as in previous steps:

\[
\widetilde C_a=J_aC_a^{\rm lat}J_a^*.
\]

It differs from C-hat_a only by P_-^X(I-R_a), with P_-^X=(I-X)/2. Its action on fixed f is bounded by ||(I-R_a)f||→0. Thus C-tilde_a also converges strongly to C_g. The artificial massive complement was a proof device, not a new physical particle sector or a changed lattice ground state.

Each covariance is a projection and defines a pure gauge-invariant quasifree state. Its restriction under the CAR embedding a_a(u)↦a(J_au) is exactly the negative-energy ground state of the chosen lattice Hamiltonian.

## 5. States, dynamics, and bounded correlations

Strong covariance convergence gives convergence of all fixed smeared two-point functions; CAR reduction and Wick determinants give convergence on field polynomials. Norm density and unit norm of states extend this to

\[
\widetilde\omega_a(A)\longrightarrow\omega_g(A)
\quad\text{for every fixed }A\in\operatorname{CAR}(H).
\]

This is weak-* convergence of states, not state-norm convergence or convergence of global density matrices in a fixed empty Fock representation.

Strong-resolvent convergence of the self-adjoint generators also gives strong convergence of their unitary groups, locally uniformly in bounded times. The identity-complement extension

\[
V_a(t)=J_ae^{-itH_a^{\rm lat}}J_a^*+(I-R_a)
\]

differs from exp(-itH-hat_a) only on (I-R_a)H, with fixed-vector discrepancy at most 2||(I-R_a)f||. It therefore converges strongly to exp(-itH), as do its adjoints. The exact CAR norm identity converts this into point-norm convergence of the induced automorphisms on the common CAR algebra.

Combining state and automorphism convergence proves convergence of any fixed finite product of bounded time-evolved observables and its quasifree ground-state expectation. The lattice state is genuinely stationary for its own Hamiltonian; it has not been obtained merely by pulling back the continuum covariance.

For smooth compact initial data, cell averages are finite-support and remain inside the intended equal-time region for small a. Thus fixed local equal-time observables and correlations have support-respecting approximants. Compact spacetime smearings converge using strong evolution and temporal quadrature, but their finite-spacing spacetime locality needs the qualification below.

## 6. Local generator does not mean a strict continuous-time cone

H_a^lat has nearest-neighbor hopping and on-site mass, but its exponential contains arbitrary powers of that hopping. At nonzero time there are generally nonzero amplitudes at arbitrarily distant sites. In the massless chiral case the propagator matrix element at r sites is a Bessel amplitude J_r(t/a). For r=2 and t=0.1a,

\[
|J_2(0.1)|\simeq0.00124896>0,
\]

outside a strict speed-one lattice cone. The code checks this explicit witness. A local hopping Hamiltonian admits decay/approximate-cone estimates; it is not the exactly finite-range discrete-time walk of step 22. No optimal Lieb–Robinson estimate is claimed here.

Consequently a region-labelled lattice spacetime algebra built from this continuous evolution is not an exactly Einstein-local net at finite a. For fixed spacelike-separated continuum smearings, norm convergence implies that the lattice graded anticommutators and even commutators tend to their zero continuum values. This is recovered continuum locality on fixed observables, not exact finite-spacing commutation or uniform regional-algebra convergence.

## 7. Ultraviolet doubling and nonuniformity remain

For constant mass the regulated dispersion is

\[
E_a(k)=\sqrt{\sin^2(ka)/a^2+m^2}.
\]

There are low-energy branches near k=0 and the zone edge k=π/a. The second is a central-difference doubler. Near k_a=π/a-a the lattice negative projector tends toward (I-X)/2, while the continuum negative projector tends toward (I-Z)/2. Their difference stays of order one. These witnesses change with a, so they do not contradict strong covariance convergence or convergence on every fixed CAR element.

The proof does not erase the doubler from cutoff traces, unbounded energy observables, loop effects, anomaly calculations, or an interacting continuum limit. A fixed smooth smearing can suppress the changing high-frequency sector even when global ultraviolet content differs. We therefore do not infer a one-species interacting universality class, a physical regulator preference, uniform convergence on the unit ball, or stress-energy convergence. A Wilson-type modification or another regulator would need a separately specified construction and proof.

The old variable-walk principal-quasienergy vacuum remains a different spectral problem. The present result must not be retroactively relabelled as its solution.

## 8. Verification and remaining obligations

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. All 32 new tests pass. They check free and perturbed gaps, eigensystem residuals, spectral signs and sign-integral quadrature, cell/core consistency, complementary-space choices, fixed low-mode covariance/Wick/time-correlation refinement, the locality-tail witness, doubling, and regulator differences.

Finite spectral diagnostics use a **periodic site ring**, represented in Fourier modes. Its sampled cosine mass couples modes cyclically, unlike the hard Galerkin cut used for the comparison reference. The reference is itself a finite continuum-circle Galerkin approximation, not an exact infinite-line solution. These numerical comparisons illustrate the estimates; the infinite-line convergence theorem is the common-core/gap argument above. No circle-to-line thermodynamic limit or ultraviolet state theorem is inferred from these matrices. Representative errors are in `enumeration.json`.

**Earned:** a genuine curved static lattice ground-state limit for an explicitly chosen Hamiltonian regulator, and convergence of fixed bounded local correlations. State selection is now controlled by spectral hypotheses, not smuggled through a propagator limit.

**Not earned:** equivalence to the Floquet vacuum, elimination of doublers, exact finite-spacing spacetime locality, Hadamard regularity, renormalized stress-energy, time-dependent vacuum uniqueness, backreaction, empirical selection, all-framework integration, phenomenal constitution, or ultimate explanation. CAR states, modes and spectral projectors still do not identify actual realization tokens or observers.

**Next obligation:** control a physically sharper ultraviolet regulator or the short-distance/renormalized-observable structure. Bounded smeared correlations are a real bridge, but they are not the stress tensor needed to couple matter back to the geometry.

## Continuation: Wilson control

[Step 24](../wilson_regulator/REPORT.md) adds a Wilson term, preserves the gap-controlled state limit, lifts the free doubler, and bounds high-zone weight in fixed-energy states on the nonconstant background. It does not erase finite-spacing tails, axial breaking, or the remaining short-distance/stress-energy obligations.
