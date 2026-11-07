# Constructive step 24: a Wilson regulator with controlled low-energy ultraviolet exclusion

## Result and scope

[Step 23](../hamiltonian_state_limit/REPORT.md) proved a curved-background ground-state limit for a central-difference Hamiltonian, while retaining its ultraviolet doubler. This step adds a **positive Wilson term**. It preserves the common-core and uniform-gap argument, so the regulated ground states still converge on fixed bounded CAR observables. It also removes the free zone-edge low-energy branch and bounds ultraviolet weight in fixed-energy states under the nonconstant background perturbation.

These are separate statements: fixed-observable convergence, free spectral branch control, and a bounded-perturbation high-zone estimate. Together they improve the regulator; they do not prove uniform ultraviolet convergence, interacting universality, Hadamard regularity, renormalized stress-energy, or gravitational backreaction.

The regulator remains a continuous-time Hamiltonian, not the earlier Floquet walk. It retains finite-time lattice tails and breaks the massless axial symmetry at nonzero spacing. Thirty-two finite tests accompany the analytic arguments.

## 1. Define the added operator explicitly

Keep the same static geometry and continuum law:

\[
\Omega(x)=1+\epsilon\cos(qx),\quad |\epsilon|<1,\quad m>0,
\qquad H=-iZ\partial_x+m\Omega(x)X.
\]

On H_a=ℓ²(Z,C²), retain central p_a and define the scalar positive Wilson operator

\[
W_a=\frac r a\left(I-\frac{T_a+T_a^*}{2}\right),\qquad r>0,
\]

where T_a shifts by one site. Its Fourier symbol is r(1-cos ka)/a. The new Hamiltonian is

\[
H_a^W=p_aZ+\big(m\Omega(aj)+W_a\big)X.
\]

The Wilson operator is not a fitted local change of the physical mass m. It is a specified momentum-dependent cutoff term, vanishing on fixed smooth data as a→0. For r=0 this reduces exactly to step 23. The calculations below use r=1 where the dispersion simplifies.

W_a is nearest-neighbor and commutes with X, Z and p_a, but not generally with the nonconstant multiplication Ω(aj). We do **not** square the full inhomogeneous Hamiltonian as if these scalar spatial operators commuted. Its gap is instead established by a bounded perturbation of the constant-mass free operator.

## 2. The uniform gap and state limit survive

For constant mass, the free symbol is

\[
h_{a,0}^W(k)=\frac{\sin ka}{a}Z+
\left(m+\frac r a(1-\cos ka)\right)X.
\]

The two terms anticommute in their spin indices and commute spatially, so

\[
(E_{a,0}^W(k))^2=\frac{\sin^2ka}{a^2}
+\left(m+\frac r a(1-\cos ka)\right)^2\ge m^2.
\]

The background adds V_a=mε cos(qaj)X, with ||V_a||≤m|ε|. The resolvent perturbation estimate therefore gives the same spacing-independent gap

\[
\operatorname{spec}H_a^W\cap(-g_*,g_*)=\varnothing,
\qquad g_*=m(1-|\epsilon|)>0.
\]

The continuum H has that gap too, as in step 22.

### Common core rather than formal symbol matching

Let J_a,S_a,R_a be the compact-cell maps. On the continuum comparison space use

\[
\widehat H_a^W=(p_aZ+(M_a+W_a)X)R_a+mX(I-R_a),
\qquad M_a=m\Omega(aj)\text{ on its cell}.
\]

The cell projection commutes with translations by a, hence with W_a. On f in H²,

\[
\|W_af\|\le\frac{ra}{2}\|\partial_x^2 f\|,
\]

by 1-cos(ak)≤a²k²/2. In particular W_aR_af=R_aW_af→0 on C_c^∞. The derivative, sampled potential and complement terms already converge on that core by step 23. Thus H-hat_a^W f→Hf on a core of the self-adjoint H.

Each fixed-a extension is bounded self-adjoint, with the same uniform gap. The dense-range resolvent argument and the dominated sign-integral proof from step 23 apply without modification. Consequently

\[
\widehat H_a^W\longrightarrow H\quad\text{in strong resolvent sense},
\qquad
J_a1_{(-\infty,0)}(H_a^W)J_a^*\longrightarrow C_g
\quad\text{strongly}.
\]

The empty complementary covariance again differs from the gapped proof extension by a projection acting only on (I-R_a)H, which vanishes on each fixed vector in the limit.

The actual stationary negative-energy quasifree states of H_a^W therefore converge weak-* on the common CAR algebra to the curved static state ω_g. Their fixed bounded finite-time correlations converge as well. The limit does not follow just from adding a term with the right low-momentum Taylor expansion: the uniform gap and common-core estimates are what justify the spectral selection.

Both central and Wilson regulators now have proved agreement on every fixed bounded CAR observable after their prescribed embeddings. This is a limited free-field regulator-independence result. It is not agreement in state norm, in all cutoff traces, or for every ultraviolet-sensitive observable.

## 3. Free spectral control: the doubler is lifted

For r=1 the exact dispersion is

\[
(E_a^W(k))^2=m^2+
\frac{4(1+ma)}{a^2}\sin^2(ka/2).
\]

On the Brillouin interval [-π/a,π/a), this is strictly increasing with |k| away from zero. In particular

\[
E_a^W(0)=m,\qquad E_a^W(\pi/a)=m+2/a.
\]

The central regulator instead has energy m at both zero and the zone edge. The Wilson branch at the edge is pushed to diverging energy, rather than merely made invisible to fixed smearings.

For a fixed finite cutoff Λ≥m, the free states of energy at most Λ have

\[
|k|\le\frac2a\arcsin\left(
\frac a2\sqrt{\frac{\Lambda^2-m^2}{1+ma}}\right),
\]

when the arcsine argument is at most one; otherwise the whole finite zone is allowed. At fixed Λ and small a, this bound tends to sqrt(Λ²-m²). Thus bounded-energy momenta remain near the intended continuum branch, not near π/a. On a fixed periodic circle the free low-energy mode counts eventually agree with the continuum counts away from energy thresholds.

The low-momentum Wilson term is approximately ra k²/2. The first-order cutoff mass correction can make fixed-momentum convergence slower than for the central derivative alone; it is the price of lifting the unwanted branch, not an error hidden in the tests.

## 4. Low-energy ultraviolet exclusion on the nonconstant background

The background mixes momenta, so the free dispersion is not a collection of exact eigenvalues for the full H_a^W. Nevertheless it gives a robust operator estimate.

Let P_Λ be the spectral projection of H_a^W onto [-Λ,Λ], and let Q_θ be the Fourier projection onto the high-zone sector |ak|≥θ₀, with 0<θ₀≤π. For any normalized ψ in the range of P_Λ,

\[
\|H_{a,0}^W\psi\|
\le\|H_a^W\psi\|+\|V_a\psi\|
\le\Lambda+m|\epsilon|.
\]

On Q_θ the free energy is at least 2sqrt(1+ma)sin(θ₀/2)/a. Since this free energy multiplier commutes with Q_θ,

\[
\boxed{\ \|Q_\theta P_\Lambda\|
\le\frac{a(\Lambda+m|\epsilon|)}
{2\sqrt{1+ma}\sin(\theta_0/2)}\longrightarrow0.\ }
\]

This is an operator-norm estimate on the **fixed low-energy spectral subspace**, not on the full Hilbert unit ball. It excludes low-energy states retaining substantial weight in a fixed-angle zone-edge sector, even with the specified nonconstant geometry. The finite tests evaluate the corresponding norm from the low-eigenspace Gram matrix, rather than taking only a maximum over individual eigenvectors.

This does not classify every possible finite-energy bound state or prove all interacting spectral properties. The estimate relies on the bounded background perturbation and positive Wilson choice; changing the geometry, interaction, or regulator requires checking those hypotheses again.

## 5. What this improvement still does not establish

### No uniform polarization limit

At k_a=π/a-a, the Wilson mass dominates, so the regulated negative projector tends toward (I-X)/2, whereas the continuum negative projector at that changing momentum tends toward (I-Z)/2. Their discrepancy remains of order one. Lifting low-energy doublers is not uniform convergence of projectors across an expanding ultraviolet zone.

The surviving high-energy modes can affect unbounded products, vacuum-energy densities, currents, trace sums and anomalies. Bounded smeared correlation convergence does not determine those limits or their subtraction terms.

### Axial symmetry and spectral sign pairing are distinct

For m=0 the continuum generator pZ commutes with Z, the generator of the axial spinor rotation in this representation. The Wilson mass term is proportional to X and breaks that commutation at finite a. The breaking vanishes at fixed momentum as a→0, but not uniformly in ultraviolet momentum. No anomaly calculation or symmetry-restoration theorem for interactions is provided.

The constant matrix Y still anticommutes with this real-mass Hamiltonian, giving sign-paired energies. That spectral pairing is not the same symmetry as commutation with Z. It cannot be used to claim the massless axial symmetry was preserved.

### Continuous-time tails remain

Nearest-neighbor H_a^W still exponentiates to arbitrarily long paths. Even for m=0,r=1, its square has scalar Fourier symbol 2(1-cos ka)/a². Its cubic power has a nonzero two-site hopping coefficient. Thus the small-time propagator has a nonzero two-site term of order (t/a)³, outside a strict cone when t is sufficiently smaller than a. Finite Fourier evaluation confirms the witness.

Therefore exact finite-spacing Einstein locality has not been restored. Fixed continuum smearings recover graded/even locality through norm convergence, as before. Neither the continuous clock nor the Wilson term makes this a finite-range Floquet walk or an exactly Lorentz-invariant lattice theory.

### No stress tensor or gravitational equation yet

The continuum static state is the same C_g selected in step 22. No Hadamard short-distance proof, locally covariant subtraction, conserved renormalized stress tensor, trace anomaly, or backreaction solution has been obtained from the Wilson construction. The geometry remains an external input under an explicitly chosen minimal coupling. Removing a free doubler is an earned ultraviolet improvement, not a solution of those remaining field/gravity obligations.

## 6. Verification and integration ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 new tests cover the Wilson dispersion and energy window, central-doubler control, free and curved gaps, spectral residuals/projectors, core suppression, fixed-smearing and cross-regulator convergence diagnostics, the low-energy high-zone bound, ultraviolet nonuniformity, axial breaking, continuous-time tails, and circle low-energy counts.

The spectral matrices are finite periodic site rings with cyclic momentum coupling from the sampled cosine mass. Comparison uses a finite continuum-circle Galerkin reference, not an exact infinite-line solution. These checks illustrate the separate common-core/gap proof; they do not establish a thermodynamic limit, ultraviolet trace limit, or an interacting theorem. Exact formulas, numerical errors and bounds are recorded in `enumeration.json`.

**Earned:** a Wilson Hamiltonian state limit on the stated curved static background; free doubler lifting; a uniform high-zone suppression estimate within any fixed finite-energy spectral subspace; agreement of two specified regulators on fixed bounded free-field observables.

**Not earned:** uniform ultraviolet convergence, exact finite-spacing spacetime locality or axial symmetry, a Floquet-vacuum theorem, interacting universality, renormalized local observables or gravity, empirical selection, all-framework integration, phenomenal constitution, or ultimate explanation. A regulator-independent type of prediction still does not identify an actual realization token or an observer.

**Next obligation:** specify and control a short-distance subtraction for local composite observables, including its state, covariance, conservation and finite-renormalization assumptions. That is the bridge from bounded smeared fields toward physical stress-energy, not an automatic corollary of this cutoff improvement.

## Continuation: a massless continuum composite prescription

[Step 25](../conformal_stress/REPORT.md) supplies an explicit conformal point-splitting remainder and a conserved anomalous stress expectation under a stated continuum Ward prescription. It is a separate massless calculation, not a theorem that this massive Wilson regulator converges to the renormalized stress tensor.
