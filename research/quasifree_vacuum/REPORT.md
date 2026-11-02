# Constructive step 16: a declared quasifree vacuum and its continuum limit

## What is now supplied

[Step 15](../fermionic_lift/REPORT.md) supplied the CAR dynamics but left its state open. This step supplies a **conditional free-field ground-state construction**: choose positive mass, fill the negative spectral subspace, define the gauge-invariant quasifree state, and represent particles and holes with nonnegative excitation energy. The corresponding walk polarizations converge strongly, and their states converge on every fixed CAR observable. Together with step 15, this gives convergence of fixed finite-time smeared correlation functions.

The selection principle is added explicitly: **use a ground state of a specified Hamiltonian branch**, not merely a stationary state. A discrete-time walk does not uniquely specify that branch or an absolute energy. No interacting theory, empirical law, phenomenal identity, or ultimate explanation is inferred.

## 1. Covariance and conventions

Work on H = L²(R, C²), in momentum representation, with m > 0 and h(k) = kZ + mX. Let E(k) = sqrt(k² + m²), and define

\[
C(k)=P_-(k)=\frac12\left(I-\frac{h(k)}{E(k)}\right).
\]

Since h² = E²I, C is an orthogonal projection and hC = -EC. Multiplication by C(k) defines a bounded orthogonal projection on H, commuting with D_t = exp(-ith).

A gauge-invariant quasifree state with covariance 0 ≤ C ≤ I is specified by

\[
\omega_C(a(f)^*a(g))=\langle g,Cf\rangle,\qquad
\omega_C(a(f)a(g)^*)=\langle f,(I-C)g\rangle.
\]

Our fields are antilinear in their smear and the inner product is conjugate-linear in its first slot. Anomalous two-point functions vanish. Normal-ordered balanced monomials obey

\[
\omega_C\big(a(f_1)^*\cdots a(f_r)^*a(g_r)\cdots a(g_1)\big)
=\det\big[\langle g_j,Cf_i\rangle\big]_{j,i=1}^r.
\]

Unbalanced monomials vanish; CAR puts arbitrary finite words into this form. Existence and positivity are not assumptions about a fitted table: for a projection C, the explicit particle/hole Fock construction in section 4 realizes these expectations as vector-state expectations. It is a pure quasifree state. Other positive contractions describe mixed quasifree states, but they are not the selected polarization here.

For example, with n_f = a(f)*a(f),

\[
\omega_C(n_fn_g)=\langle f,Cf\rangle\langle g,Cg\rangle
+\langle g,Cf\rangle\langle f,(I-C)g\rangle.
\]

Conventions matter: swapping the slots in the covariance formula would conjugate general complex off-diagonal expectations. The finite tests include complex smearings and a nonzero two-particle Wick determinant.

## 2. The walk state requires a quasienergy branch

Write the walk symbol as

\[
W_a(k)=c_a(k)I-i\,q_a(k)\cdot\sigma,
\]

where c_a = cos(ka)cos(ma) and

\[
q_a=(\cos(ka)\sin(ma),\ \sin(ka)\sin(ma),\ \sin(ka)\cos(ma)).
\]

Assume 0 < ma < π/2. Then q_a never vanishes. Let θ_a = atan2(|q_a|, c_a), in (0,π), and choose the principal branch

\[
h_a(k)=\frac{\theta_a(k)}{a}\frac{q_a(k)\cdot\sigma}{|q_a(k)|},\qquad
C_a(k)=\frac12\left(I-\frac{q_a(k)\cdot\sigma}{|q_a(k)|}\right).
\]

Thus exp(-iah_a) = W_a, h_a C_a = -(θ_a/a)C_a, and C_a commutes with W_a. Filling this negative branch gives a stationary pure quasifree state. On any finite ring, filling all negative modes is the unique unrestricted Fock ground vector for this chosen nonzero-spectrum quadratic Hamiltonian, up to phase. This is stronger than stationarity, which allowed empty, filled, and mixed alternatives in step 15.

**But the branch is an added choice.** Shifting eigenvalues by integer multiples of 2π/a leaves the discrete-time unitary unchanged and can change what is called negative energy. The small-spacing, fixed-momentum target motivates the chosen branch without making its entire ultraviolet interpretation empirically compulsory. On the common continuum comparison space below the out-of-zone dynamics is the identity, so the extension there has zero-energy degeneracy; no unique ground-state claim is made for that artificially extended generator.

## 3. Controlled polarization and state convergence

### A quantitative fixed-band estimate

Put v_a = q_a/a and v = (m,0,k). Elementary sine/cosine remainder bounds give, uniformly |k| ≤ K,

\[
|v_a-v|\le B_a(K)
=aKm+a^2\left(\frac{mK^2}{2}+\frac{m^3}{6}
+\frac{Km^2}{2}+\frac{K^3}{6}\right).
\]

Here the Euclidean norm is bounded by the sum of the component bounds. Normalization satisfies |x/|x| - y/|y|| ≤ 2|x-y|/|y|. Since |v| ≥ m and the operator norm of z·σ is |z|,

\[
\sup_{|k|\le K}\|C_a(k)-C(k)\|
\le \varepsilon_a(K):=\min(1,B_a(K)/m)\longrightarrow0.
\]

The min with one uses the general norm bound for a difference of orthogonal projections. This proof intentionally assumes a positive mass gap; it does not cover the massless zero-mode/polarization issue.

### The common-algebra state comparison

Use the same H and Brillouin projection P_a as step 15. Define the common covariance by C_a on B_a = [-π/a,π/a) and **zero outside B_a**. This is an orthogonal projection, denoted C-tilde_a, hence defines a genuine state on CAR(H). It extends the embedded lattice state by an empty tail; it is not a claim about observable out-of-zone particles.

For f_K = 1_{[-K,K]}f with K < π/a,

\[
\|(\widetilde C_a-C)f\|
\le\varepsilon_a(K)\|f_K\|+\|f-f_K\|.
\]

First take a → 0, then K → infinity. This proves strong convergence of the common covariance to C on every fixed f in H. Other projection choices within the complementary tail have the same limit, because their difference on that tail is uniformly bounded. Such extensions should remain distinguished from changing the actual in-zone lattice state.

Pairings therefore converge; Wick determinants and CAR reductions give convergence of all finite field-polynomial expectations. Since states have norm one and these polynomials are norm dense, the estimate

\[
|\omega_a(A)-\omega_C(A)|
\le 2\|A-P\|+|\omega_a(P)-\omega_C(P)|
\]

proves convergence on **every fixed A in CAR(H)**. This is weak-* convergence of states, not state-norm convergence or convergence of density matrices on a preselected global Hilbert representation.

### Joint dynamics and correlations

Step 15 gave point-norm convergence α_a,t(A) → α_D,t(A) on this same algebra. Consequently

\[
|\omega_a(\alpha_{a,t}(A))-\omega_C(\alpha_{D,t}(A))|
\le\|\alpha_{a,t}(A)-\alpha_{D,t}(A)\|
+|\omega_a(\alpha_{D,t}(A))-\omega_C(\alpha_{D,t}(A))|
\longrightarrow0.
\]

A telescoping product gives the analogous statement for any fixed finite product of time-evolved bounded observables, at finitely many fixed times. One can take a common spacing sequence, or round each time to the nearest available step; the fixed-band time-rounding and tail bounds then apply. This statement includes fixed smeared two- and higher-point functions, not unsmeared point-field distributions or unbounded energy observables.

### What convergence does not mean

Polarization convergence is not uniform over all momenta. At k = π/a the walk projector tends to (I+X)/2, whereas the continuum negative projector tends to (I-Z)/2, with discrepancy tending to 1/sqrt(2). Narrow L² packets near this edge preserve the obstruction but change with a. They do not refute strong covariance convergence or convergence on fixed CAR elements. No state-norm convergence is claimed.

Nor does state convergence identify exactly local lattice and continuum regional algebras: the Fourier embedding still has sinc tails.

## 4. Ground-state representation and positive particle/hole energy

The empty Fock representation of H is not the correct sea vacuum representation. Instead set H_+ = (I-C)H and H_- = CH, and form

\[
\mathcal K=H_+\oplus\overline{H_-},\qquad
\mathcal H_{\rm sea}=\mathcal F_-(\mathcal K).
\]

Use annihilators b on H_+ and d on the conjugate negative-energy space, with cross CAR, and define

\[
\pi_C(a(f))=b((I-C)f)+d^*(\overline{Cf}).
\]

Both terms are antilinear in f. Their CAR give exactly the original CAR. The empty b,d Fock vector Ω realizes the covariance above: its nonzero occupation contribution comes from d d*. This constructs the state with ordinary positive Hilbert-space probabilities and a cyclic vacuum. In this projection case the field algebra generates the irreducible particle/hole Fock representation, giving purity.

The continuum excitation generator is

\[
K_{\rm exc}=d\Gamma\big(E|_{H_+}\oplus\overline{E|_{H_-}}\big)\ge0.
\]

It annihilates Ω and implements the specified Heisenberg dynamics. Particle annihilators acquire exp(-itE), while the hole creation term acquires exp(+itE), exactly matching a(D_t* f) and the negative sign of h on H_-. Both particle and hole excitations have positive energy E(k), mass gap m, and the same mass-shell relation. This is an explicit ground-state representation of the **free** CAR dynamics, rather than simply a stationary covariance. A complete spacetime/Poincaré-covariant net construction is not proved here.

At one finite momentum, let v_- and v_+ be the normalized eigenvectors. Then

\[
d\Gamma(h)+E I=E\big[(I-n_{v_-})+n_{v_+}\big]\ge0.
\]

The filled negative-mode vector has zero subtracted energy; removing it creates a hole of energy E, and adding a positive-mode particle costs E. These identities are checked as finite Fock matrices. They explain the subtraction without assigning physical reality to an infinite numerical constant.

## 5. Infinite sea and absolute energy are not finite matrices

C has infinite-dimensional range. The corresponding state is not normal in empty Fock over the original H. To see why, choose infinitely many orthonormal negative-energy modes. Covariance C assigns occupation one to every one of them. Any hypothetical normal empty-Fock state with these expectations would give probability one to total particle number at least n for every n. But in empty Fock the projections onto number ≥ n decrease strongly to zero; every normal state assigns them probabilities tending to zero. This contradiction holds even for normal states with infinite *expected* number. A new polarization representation is genuinely required, not merely a large finite vector in the old one.

The bare continuum energy density with symmetric momentum cutoff Λ is

\[
e_0(\Lambda)=-\frac1{2\pi}\int_{-\Lambda}^{\Lambda}\sqrt{k^2+m^2}\,dk
=-\frac{\Lambda\sqrt{\Lambda^2+m^2}+m^2\operatorname{asinh}(\Lambda/m)}{2\pi}
\sim-\frac{\Lambda^2}{2\pi}.
\]

It diverges. Normal ordering defines excitation energy relative to the chosen vacuum; it neither predicts an absolute gravitating vacuum energy nor solves the cosmological-constant problem. Convergence of bounded CAR correlations does not imply convergence of unbounded Hamiltonians, stress tensors, or their renormalized local products. Those need domains, regulators, and additional estimates. The finite principal-branch Hamiltonian can also be spatially nonlocal; finite-range locality of W does not automatically give finite-range locality of its logarithm.

## 6. Verification and explanatory ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` at the repository root. All 32 new tests pass. They cover spectral projections, Bloch signs, stationarity, branch reconstruction, projector bounds and edge failure, complex covariance conventions, Wick correlations, finite ground and particle/hole energies, convergence diagnostics, divergent cutoff energy, and parameter guards. Numerical samples and Frobenius upper bounds check finite identities; the infinite-space statements rely on the arguments above. Representative errors are recorded in `enumeration.json`.

**Earned:** explicit additional state-selection conditions; a pure stationary quasifree state; positive-energy particle/hole ground-state representation; controlled convergence of polarizations, states, and fixed finite-time bounded correlations.

**Still conditional/open:** empirical selection of this free 1+1-dimensional model and branch; massless treatment; exact regional-net scaling and full spacetime covariance; unbounded observable renormalization; interactions and higher dimensions; compatibility with the remaining geometric frameworks; phenomenal constitution and ultimate explanation. No mathematical mode, occupied orbital, or GNS representation counts an observer or establishes an actual realization token.

**Next constructive obligation:** turn the equal-time continuum field and ground state into an explicitly spacetime-indexed local observable construction, with the precise covariance/locality conditions and the finite-spacing support mismatch stated rather than hidden. Alternatively, interactions demand an independently specified Hamiltonian and a new convergence proof; they are not licensed by the free calculation.

## Continuation: spacetime net

[Step 17](../spacetime_net/REPORT.md) supplies the spacetime source map, causal locality, diamond time-slice construction, and proper-orthochronous Poincaré implementation. It also extends the lattice comparison to fixed spacetime smearings, without identifying sharp regional algebras at finite spacing. Disconnected even-region additivity is not silently assumed.
