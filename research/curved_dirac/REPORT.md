# Constructive step 22: Dirac dynamics on a reconstructed conformal geometry

## Result and scope

[Step 21](../refinement_completion/REPORT.md) constructed measured conformal patches but did not supply their field dynamics. This step adds an explicit **minimally coupled free Dirac law**, derives its spin-connection correction and conserved Cauchy inner product, and constructs a globally smooth static example with a gapped stationary quasifree ground state. A variable-coin walk has exact finite-range causality and a strong continuum approximation to that curved-background dynamics.

This connects a specified nonconstant volume geometry to a specified field law. It does not derive minimal coupling, CAR statistics, a gravitational field equation, or a preferred state from incidence data. Nor does propagator convergence prove convergence of lattice vacuum polarizations. The finite spectral examples below are diagnostics, not an unproved ultraviolet vacuum theorem.

Thirty-two new tests pass. Analytic arguments, finite identities, and numerical checks are distinguished throughout.

## 1. From the completed volume density to the metric

In an admitted smooth null chart u=t+x, v=t-x, write the reconstructed measure as dμ=ρ(u,v)du dv. Retain the previous null-direction interpretation and set

\[
g=\Omega^2(t,x)(dt^2-dx^2),\qquad \Omega=\sqrt{2\rho}.
\]

Thus dμ=Ω²dt dx, with Ω>0. This uses the geometric interpretation of step 21, not a fresh extraction of metric or dimension from an unlabelled quantum algebra.

The spinor construction below is local and applies to its nonstatic affine-density example as well. For global evolution and spectral claims we choose a separate, globally defined static representative:

\[
\Omega(x)=1+\epsilon\cos(qx),\qquad |\epsilon|<1,\quad q>0.
\]

It is positive, smooth, bounded above and below, and has bounded derivatives of every order. It defines an explicit admissible refinement system by integrating ρ=Ω²/2 over dyadic null cells. Those valuations are positive and additive. Their density bounds are (1-|ε|)²/2 and (1+|ε|)²/2; adjacent-average differences satisfy a uniform Lipschitz bound because

\[
|\partial_u\rho|,|\partial_v\rho|
\le(1+|\epsilon|)|\epsilon|q/2.
\]

Consequently this example satisfies the measure and smoothness conditions of step 21. It is not asserted to be the same geometry as that step's explicitly time-dependent affine example, or to be a unique extension of a finite observed patch.

With σ=log Ω and the previous curvature convention,

\[
R=2\Omega^{-2}\partial_x^2\sigma
=\frac{2(\Omega\Omega''-(\Omega')^2)}{\Omega^4},\qquad
R(0)=-\frac{2\epsilon q^2}{(1+\epsilon)^3}.
\]

For ε≠0 it is curved. No Einstein equation or stress tensor has been imposed.

## 2. The spin connection is not optional

Use the conformal tetrad e_a^μ=Ω^-1δ_a^μ, γ⁰=X, γ¹=-iY, and signature (+,-). The curved gamma matrices γ_g^μ=Ω^-1γ^μ satisfy the corresponding curved Clifford relations. In a compatible spin frame the covariant Dirac operator obeys the two-dimensional conformal identity

\[
\slashed\nabla_g\psi
=\Omega^{-3/2}\gamma^\mu\partial_\mu(\Omega^{1/2}\psi)
=\Omega^{-1}\gamma^\mu\left(\partial_\mu+\tfrac12\partial_\mu\sigma\right)\psi.
\]

For example connection matrices Γ_t=(∂xσ)Z/2 and Γ_x=(∂tσ)Z/2 have precisely the contracted term in this formula. The identity follows from the conformal tetrad connection and γ⁰Z=γ¹, γ¹Z=γ⁰. It is the ordinary torsion-free spin connection, an additional geometric/field choice rather than a new inferred interaction.

The assumed field equation (i slash-nabla_g - m)ψ=0 becomes

\[
i\partial_t\psi=
\left[-iZ\left(\partial_x+\tfrac12\partial_x\sigma\right)
-\tfrac i2\partial_t\sigma+m\Omega X\right]\psi.
\]

Naively replacing the flat constant mass by a spatial function while still calling the unrescaled field ψ would miss these connection terms.

Define χ=Ω^(1/2)ψ. Then the equation is exactly

\[
\boxed{\ i\partial_t\chi=H(t)\chi,
\qquad H(t)=-iZ\partial_x+M(t,x)X,\quad M=m\Omega.\ }
\]

The connection terms cancel under this rescaling, including the time derivative of Ω. The physical mass m remains constant; M is the coordinate-time potential after the geometric rescaling. For m=0 the rescaled equation is the flat massless Dirac equation, but the physical field and its normalization still depend on Ω.

## 3. Conserved inner product and finite propagation

The conserved Dirac current gives

\[
\|\psi\|_{\Sigma_t}^2=\int\Omega(t,x)\psi^*\psi\,dx
=\int\chi^*\chi\,dx.
\]

The Cauchy weight is Ω, **not Ω²**. The latter is the spacetime volume weight; confusing them would produce the wrong canonical field normalization.

For real M, the rescaled equation implies

\[
\partial_t(\chi^*\chi)+\partial_x(\chi^*Z\chi)=0,
\qquad |\chi^*Z\chi|\le\chi^*\chi.
\]

Integrating this identity outside an expanding interval proves propagation speed at most one in the conformal coordinates. These are exactly the null cones of g. Density and smooth approximation extend the support statement to the L² evolution.

For the global static example, A=-iZ∂x is self-adjoint on H¹(R,C²), and B=M(x)X is bounded self-adjoint. Therefore H=A+B is self-adjoint on the same domain by bounded perturbation, and exp(-itH) is a unitary group on the rescaled H=L²(R,C²). For smooth bounded time-dependent Ω, locally uniform bounds and norm continuity of B(t) give a unitary two-time propagator through the bounded interaction-picture Dyson construction. Time-dependent weighted ψ spaces are identified with this fixed H by χ=√Ωψ.

This general evolution statement does not provide a time-translation symmetry or a stationary vacuum when Ω depends on time.

## 4. A causal CAR field net on the curved background

Impose CAR on the rescaled Cauchy Hilbert space as before. Let U(t,s) be its evolution. For a compact spacetime source G for χ, put

\[
Q_\chi G=\int U(0,t)G_t\,dt,\qquad
\Psi_\chi(G)=a(Q_\chi G).
\]

Finite propagation gives the same graded locality and parity-even commutation argument as step 17, now with the actual curved causal cones. Time-slice right inverses use G_t=χ₀(t)U(t,0)f with integral χ₀=1; small temporal support and finite propagation preserve the required compact region. This is an external-background free field net, not a new interacting construction.

If a physical ψ source F is paired using dμ=Ω²dt dx and the canonical conjugate-spinor pairing, the corresponding χ source is Ω^(3/2)F:

\[
\int\Omega^2\psi^*F\,dt\,dx
=\int\chi^*\Omega^{3/2}F\,dt\,dx.
\]

Multiplication by this smooth positive factor preserves compact support. Smeared field equations must be transferred with these weights and the appropriate formal adjoint; the flat source equation must not simply be copied unchanged onto the curved test space.

The static geometry has time-translation symmetry and discrete spatial periodicity. General Minkowski translations and boosts are not isometries here. Local Lorentz spin-frame covariance is not global Poincaré symmetry; the flat joint momentum-spectrum conclusion of step 17 is not asserted on this background.

## 5. A specified static ground state, not the old flat vacuum

For m>0 write

\[
H=H_0+V,\quad H_0=-iZ\partial_x+mX,
\quad V=m\epsilon\cos(qx)X,\quad\|V\|\le m|\epsilon|.
\]

The free spectrum avoids (-m,m). If |E|<m(1-|ε|), then dist(E,spec H₀)>||V||, and the resolvent Neumann series excludes E from spec H. Hence the curved static generator has the rigorous gap

\[
\operatorname{spec}H\cap(-g_*,g_*)=\varnothing,
\qquad g_*=m(1-|\epsilon|)>0.
\]

The constant matrix Y anticommutes with H, so the spectrum is paired in sign. Define C_g=1_(-infinity,0)(H). It is a well-defined orthogonal projection commuting with the static dynamics, and gives a pure gauge-invariant quasifree CAR state.

The particle/hole representation uses H_+=(I-C_g)H and H_-=C_gH, with nonnegative excitation generator

\[
K=d\Gamma\left(H|_{H_+}\oplus\overline{-H|_{H_-}}\right)\ge0.
\]

The vacuum is fixed, and each particle/hole costs at least g_*. This is positivity of **static Killing-time excitation energy**, not a flat momentum mass shell or a claim about absolute gravitational vacuum energy.

The selection criterion is still “choose this static ground state,” an explicitly added condition. The flat polarization C₀ generally does not commute with H when ε≠0; retaining it would not give this stationary state. The finite Galerkin example checks that noncommutation directly. For a genuinely time-dependent Ω there is no preferred stationary negative-energy projection supplied by this construction; instantaneous diagonalization is not a proof of a globally preferred vacuum.

No Hadamard/microlocal regularity theorem, renormalized stress tensor, vacuum-energy subtraction prescription for gravity, or backreaction equation is established here. Those require additional analysis even when a static spectral ground state exists.

## 6. A genuinely local variable-coin approximation

Retain the infinite line with spacing/time step a. At site j use coin exp(-iaM(aj)X), then the same right/left component shifts as before. This is a unitary walk W_a^M: a product of on-site unitaries and a permutation shift. Its inverse reverses that order. After n steps support expands by at most |n| sites, so lattice graded/even locality remains exact.

Use the compact-cell embedding J_a,S_a,R_a of step 18. Let M_a(x)=M(aj) on C_j^a. The embedded walk exactly intertwines with

\[
V_a^{\rm cell}=e^{-iaA}e^{-iaM_a(x)X}
\]

on the cell subspace. With L_M=||M'||_infinity,

\[
\|M_a-M\|_\infty\le aL_M/2,
\qquad
\|V_a^{\rm cell}-e^{-iaA}e^{-iaB}\|
\le a^2L_M/2.
\]

At T=na, telescoping contributes at most TaL_M/2. The self-adjoint A, bounded self-adjoint B, and self-adjoint sum H satisfy the unitary Lie–Trotter product formula, so (exp(-iaA)exp(-iaB))^n f → exp(-iTH)f strongly for fixed f, locally uniformly in bounded times. One way to see why its assumptions suffice is to use the strongly continuous bounded interaction-picture potential: the product approximates its Dyson integrals by strong Riemann sums, while the factorial bounds dominate the series. No operator-norm convergence over all ultraviolet states is implied.

Combining this with R_a f→f gives

\[
\|J_a(W_a^M)^nS_af-e^{-iTH}f\|
\le\|R_af-f\|+(TaL_M/2)\|f\|
+\|(e^{-iaA}e^{-iaB})^nf-e^{-iTH}f\|
\longrightarrow0.
\]

Inverse times obey the corresponding reversed-product formula. The previous constant-mass fixed-band bound is not silently reused: M(x) couples momenta. Here the theorem is strong convergence, with the explicit O(a) sampled-potential contribution separated from the product-formula term. Compact-cell source approximants remain finite-support and region-assigned, and their fixed smeared fields converge in norm by the CAR norm identity, using the locally uniform strong convergence and temporal quadrature.

### A remaining spectral bridge

This propagator result does **not** prove convergence of the variable walk's principal-quasienergy negative projections. The finite-spacing walk still has ultraviolet quasienergy structure, and taking a spectral sign is not justified solely by convergence of finite-time evolution. A lattice vacuum theorem needs separate spectral control or a precisely specified regulator/state construction.

One may pull the continuum state back to embedded lattice subalgebras for correlation approximation, but that is a different, explicitly chosen lattice state and need not be the walk's stationary vacuum. We do not conflate these alternatives.

## 7. Verification and interpretation

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. All 32 new tests pass. They cover conformal volumes/curvature/Clifford identities, connection cancellation for static and time-dependent Ω, the Cauchy weight and continuity equation, variable-walk unitarity/inversion/cones, compact-cell refinement, sampled-coin bounds, and static spectral/ground-state identities.

The spectral diagnostic is a finite Fourier **Galerkin** cut on a periodic circle, with momentum coupling from the cosine potential and no cutoff wrap coupling. A small real-symmetric Jacobi eigensolver is checked by independent residual and orthonormality tests. Negative-projector stationarity, failure of flat-projector stationarity, and finite exterior-power sea energies are verified. This finite Fourier cut is not spatially local and is not the infinite-line variable walk. Its projectors do not prove convergence of continuum or lattice vacuum cutoffs. Coarse/fine walk errors are Cauchy diagnostics, not independent exact continuum solutions. Representative diagnostics are in `enumeration.json`.

**Earned:** an explicit metric-to-field coupling, correct spin connection/normalization, causal unitary curved-background dynamics, a conditional static gapped ground state, and a support-preserving variable-coin continuum approximation.

**Not earned:** derivation of minimal coupling or actual metric/field law from causal incidence; quantum gravitational backreaction; a preferred vacuum for time-dependent geometry; Hadamard/stress-energy results or a lattice polarization theorem; all-framework integration, phenomenal constitution, or ultimate explanation. The geometry and field branches now meet at an explicit conditional map, but physical actuality and constitutive identity remain separate obligations.

**Next substantive bridge:** prove a controlled curved-background lattice-state limit or supply the state regularity/renormalized-observable analysis needed for physical stress-energy. Neither can be inferred merely from the successful propagator limit.

## Continuation: a gap-controlled Hamiltonian state limit

[Step 23](../hamiltonian_state_limit/REPORT.md) proves strong-resolvent, polarization, and bounded-correlation convergence for a distinct Hamiltonian regulator. It explicitly retains continuous-time tails and ultraviolet doubling; this is not a proof for the variable-walk principal-quasienergy vacuum withheld above.
