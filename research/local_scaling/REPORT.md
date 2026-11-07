# Constructive step 18: compact-cell, region-preserving approximation

## Result and scope

The [spacetime-net construction](../spacetime_net/REPORT.md) left sharp localization unresolved because its Fourier comparison map produced sinc tails. This step uses a **different comparison embedding**, by normalized cell indicators. It preserves compact support up to one cell and intertwines the lattice walk exactly with a continuum split-step unitary.

This earns three statements:

1. Compact spacetime sources have genuinely finite-support, region-assigned lattice approximants with a controlled continuum limit.
2. For diamonds based on the reference time slice, the embedded lattice local algebra is **exactly a subalgebra** of the continuum local algebra, and approximates each fixed continuum element in norm.
3. The same lattice negative-branch quasifree states converge under this new embedding; local bounded correlations converge as well.

The approximation is not uniform on the local unit ball. Exact inclusion is not established for every spacetime region under one fixed embedding, nor is the finite lattice boost covariant. These are specific results for the previously declared free Dirac/CAR model, not a derivation of actual physics or phenomenal constitution.

## 1. Replace the comparison map, not the walk

Let H_a = ℓ²(Z,C²), H = L²(R,C²), and let C_j^a = [a(j-1/2),a(j+1/2)). Define

\[
(J_a u)(x)=a^{-1/2}u_j\quad(x\in C_j^a),\qquad
(S_a f)_j=a^{-1/2}\int_{C_j^a}f(x)dx.
\]

Then S_a = J_a*, S_a J_a = I, and R_a = J_a S_a is orthogonal projection onto cellwise-constant functions. Thus J_a is isometric and S_a is contractive. For f in H¹(R,C²), interval Poincaré estimates, with a deliberately loose constant, give

\[
\|R_a f-f\|\le a\|\partial_x f\|.
\]

Density and contraction extend R_a f → f to every fixed f in H. If f has compact support K, only finitely many cell averages are nonzero; their centers are within a/2 of K and their full cells are within distance a of K. For K compactly contained in an open interval I, all these cells are contained in I once a is small enough.

This J_a is not the Fourier/sinc embedding E_a. It is not bandlimited and no claim of equality between the two finite-spacing maps is made. The walk on H_a remains exactly the same coin-then-shift rule. Both embeddings can have the same continuum limit without having identical support properties.

## 2. Exact split-step intertwining and an H¹ error bound

Let p = -i∂x, A = pZ, B = mX, h = A+B. On all of H define

\[
V_a=e^{-iaA}e^{-iaB}.
\]

The first factor shifts component 0 right by a and component 1 left by a. Both shifts and the constant coin preserve the cell subspace, for forward and inverse evolution. Consequently

\[
J_a W_a=V_a J_a,\qquad [R_a,V_a]=0.
\]

On H¹, [A,B] = 2im pY, so its action has norm at most 2|m| ||∂x f||. The unitary product Duhamel bound yields

\[
\|(V_a-D_a)f\|\le a^2|m|\|\partial_x f\|.
\]

All propagators here preserve the derivative norm: their Fourier multipliers are unitary and commute with multiplication by k. Telescoping therefore gives, for every integer n, positive or negative,

\[
\|(V_a^n-D_{na})f\|
\le |na|a|m|\|\partial_x f\|.
\]

For negative powers use the adjoint one-step identity and the same derivative bound; no inverse-time instability is introduced. Apply this estimate to f, not to the discontinuous R_a f. The projection error is handled separately by unitarity:

\[
\boxed{\ \|J_a W_a^n S_a f-D_{na}f\|
\le a(1+|na||m|)\|\partial_x f\|.\ }
\]

This is a direct compact-cell approximation bound. It neither assumes a bandlimit nor establishes all-spectrum operator-norm convergence: its derivative factor grows for increasingly oscillatory f. For arbitrary fixed L² data, smooth approximation and contraction give strong convergence at bounded fixed times, with clock rounding controlled by strong continuity of D_t.

## 3. Exact CAR embeddings, but no exact averaging inverse

An isometry induces an injective isometric CAR *-homomorphism

\[
\iota_a:\operatorname{CAR}(H_a)\hookrightarrow\operatorname{CAR}(H),\qquad
\iota_a(a_a(u))=a(J_a u).
\]

For f compactly supported inside I, a_a(S_a f) is a finite-support lattice field inside I for sufficiently small a, and

\[
\|\iota_a(a_a(S_a f))-a(f)\|=\|R_a f-f\|.
\]

Products and adjoints converge by telescoping; parity is preserved. Even-polynomial approximants remain even. The full C*-norm, not a matrix Frobenius norm, is used in these analytic statements.

**A type distinction matters:** mapping a(f) to a_a(S_a f) is not an exact inverse CAR homomorphism. S_a is only contractive; its pairings need not equal the original ones. We construct approximants to fixed fields and polynomials and use density, rather than assert a nonexistent exact inverse map on the whole algebra.

## 4. Lattice spacetime regions and exact aligned-diamond inclusion

Define a lattice field net by including the generators

\[
a_a(W_a^{-n}e_{j,r})\quad\text{when}\quad
\{na\}\times\overline{C_j^a}\subset O,
\]

with r = 0,1, and take their adjoints, identity and C*-closure. Call it F_a(O); let A_a(O) be its parity-even fixed points. This defines locality by the spacetime labels before pulling back to the common reference slice. It does not assign independent degrees of freedom to every time label.

The lattice cone satisfies |j-k| ≤ |n-l| for potentially nonzero propagation from (l,k) to (n,j). Hence spacelike-separated region labels give vanishing mixed CAR anticommutators and commuting even algebras, exactly. Both nets are isotonic. This is an infinite line, not a finite ring with possible wraparound.

Now take the reference-slice diamond D(I) from step 17, I = (x₀-R,x₀+R). If a cell at time na lies in this diamond, pulling it back n steps produces only cells wholly contained in I. Conversely every cell whose closure lies in I is already a generator at n=0. Thus, with H_a(I) the finite-dimensional span of those full cells and both components,

\[
\mathcal F_a(D(I))=\operatorname{CAR}(H_a(I)),
\qquad
\iota_a(\mathcal F_a(D(I)))\subset\mathcal F(D(I)).
\]

The equality uses the exact lattice cone; the continuum inclusion uses the continuum diamond time-slice equality F(D(I)) = CAR(H(I)) established in step 17. The same inclusion holds for the even algebras. This closes a genuine localization gap for this specified class of regions.

For every fixed A in F(D(I)),

\[
\operatorname{dist}\big(A,\iota_a(\mathcal F_a(D(I)))\big)\longrightarrow0,
\]

and analogously for A in A(D(I)) with even lattice approximants. To prove it, first approximate A by a finite polynomial with smooth initial smearings compactly contained in I, then average those smearings. For sufficiently small a their cells are inside I and the polynomial converges. Even polynomials are dense in the even algebra by parity averaging. No nesting of the different grids is required.

This is **pointwise inner approximation of aligned-diamond C*-algebras**. For diamonds based on another Cauchy time, an adapted time-translated comparison embedding gives the corresponding result. Under one fixed J_a, however, split evolution does not exactly equal Dirac evolution, so exact inclusion for every translated/boosted diamond or arbitrary O is not inferred. Stronger simultaneous net convergence would require an explicitly chosen topology and further compatibility estimates.

## 5. Compact spacetime-source approximation without Fourier tails

For F in C_c^∞(O,C²), define

\[
Q_a^{\rm loc}F=a\sum_{n\in\mathbb Z}W_a^{-n}S_aF_{na}.
\]

It has finite support: the time sum is finite, each source has finitely many cells, and each pullback has finite range. Since supp F is a compact subset of O, a positive support margin ensures that every full source cell at sampled time na lies in O for sufficiently small a. Consequently

\[
a_a(Q_a^{\rm loc}F)\in\mathcal F_a(O)
\]

exactly, not merely up to nonzero distant tails.

Let |t| ≤ L contain the temporal support, and set G(t)=D_t*F_t. The evolution bound and whole-line Riemann quadrature estimate give

\[
\|J_aQ_a^{\rm loc}F-QF\|
\le a(1+L|m|)\,a\sum_n\|\partial_x F_{na}\|
+a\int\|ihF_t+\partial_tF_t\|dt.
\]

The sums are bounded Riemann sums, so the error is O(a) for each fixed smooth compact source. By the exact CAR field norm, the embedded fields converge in norm; so do fixed finite products and even polynomials.

For general O the embedded field need not itself belong to F(O) at finite a: its reference-slice propagation is split rather than exact Dirac evolution. Region preservation here means an exactly region-assigned lattice operator and convergence to the region-assigned continuum operator. The stronger exact embedded inclusion was proved separately for reference-slice diamonds. This distinction prevents the support problem from being hidden under a change of words.

## 6. The same lattice vacuum also converges in this embedding

Retain m > 0 and 0 < ma < π/2. Let C_a^lat be the walk's negative-principal-branch covariance on H_a. On continuum Fourier space define the **periodic**, not Brillouin-truncated, projection C_a^per(k) using the Bloch formula of step 16 for all real k. It is the spectral projection of V_a onto the upper semicircle, since the negative branch has eigenvalue exp(+iθ). The spectral gap at ±1 makes this projection unambiguous for each allowed a.

Because R_a reduces V_a, it commutes with this spectral projection. Spectral calculus and J_a W_a = V_a J_a then imply

\[
\widehat C_a:=J_a C_a^{\rm lat}J_a^*
=C_a^{\rm per}R_a=R_a C_a^{\rm per}.
\]

This is a projection on H, zero on the cell subspace's orthogonal complement. It defines a common-algebra quasifree state whose restriction under iota_a is **exactly the original lattice state**, not a newly fitted covariance.

For each fixed momentum C_a^per(k) → C(k). The previous fixed-band bound and the uniform contraction bound give strong convergence C_a^per → C on H by cutoff/density. Hence

\[
\|(\widehat C_a-C)f\|
\le\|R_a f-f\|+\|(C_a^{\rm per}-C)f\|\longrightarrow0.
\]

Wick determinants and polynomial density give weak-* convergence of the associated states on CAR(H). If embedded local approximants A_a → A in norm, their expectations converge by

\[
|\widehat\omega_a(A_a)-\omega_C(A)|
\le\|A_a-A\|+|\widehat\omega_a(A)-\omega_C(A)|.
\]

This controls the local bounded correlations constructed above. The empty complementary covariance is a comparison convention, not additional physical degrees of freedom. State-norm convergence, unbounded-energy convergence, and absolute vacuum-energy renormalization do not follow. The declared branch and vacuum selection conditions from step 16 remain assumptions.

## 7. Why the local unit ball cannot converge uniformly

At any sufficiently fine but fixed a, choose a unit smooth compactly supported f_a inside one cell in I, with zero cell average. An odd-shaped bump about the cell center supplies such a direction. Then f_a is orthogonal to the entire cell subspace, and hence to H_a(I).

The even continuum observable n_{f_a}=a(f_a)*a(f_a) is a norm-one projection. It belongs to A(D(I)), but an independent complement-mode occupation cannot be approximated arbitrarily well by the cell algebra. Restricting to the finite CAR algebra of H_a(I) plus this mode, any B in the cell algebra acts the same in the complement's empty and filled sectors, while n_{f_a} acts as zero and one. Compression gives

\[
\|n_{f_a}-B\|\ge\max(\|B\|,\|I-B\|)\ge\tfrac12.
\]

The scalar B=I/2 attains 1/2, so this distance is exact, also for even B. Faithfulness of finite CAR embeddings preserves this norm in the continuum algebra. Thus even local unit balls do not approach one another uniformly. The witness changes with a; it does not contradict approximation of every **fixed** observable. Its increasingly large derivative also explains why the H¹ bound does not force it to vanish.

## 8. Verification and explanatory ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. All 32 new checks pass. They cover exact polynomial cell integrals, isometry/contraction, support margins, Poincaré error, signed walk evolution, exact massless references, massive coarse/fine Cauchy estimates, diamond cone inclusion, compact spacetime sources, spacelike pairings, invisible within-cell directions, the even unit-ball obstruction, and finite-circle DFT analogues of covariance intertwining and reduction. Coarse/fine massive comparisons are not independent numerical solutions of the continuum PDE; the analytic product estimate supplies that bridge. Numerical data are in `enumeration.json`.

**Earned:** an explicitly support-preserving comparison scheme, a quantitative H¹ dynamical bound, exact inner inclusion and fixed-element norm approximation on reference-slice diamonds, and convergence of the same lattice vacuum's local bounded correlations.

**Not earned:** uniform local-algebra approximation, a single exact covariant embedding of every spacetime region, interacting or higher-dimensional QFT, physical selection of the free model, geometric reconstruction, all-framework integration, phenomenal constitution, or ultimate explanation. Cell, mode, type, and algebra counts still do not establish actual realization tokens or subjects.

**Next substantive direction:** formulate exactly what spacetime geometry can be reconstructed from causal/local structure and state, including its unavoidable scale or conformal ambiguities. This is now a sharper question than simply demanding that all frameworks be compatible.

## Continuation: causal and volume identifiability

[Step 19](../causal_geometry/REPORT.md) asks what the geometric input actually determines. It gives explicit conformal/curvature ambiguity, a calibrated-volume inverse within a declared class, coarse-data counterexamples, and the mass/scale dilation relation of the free net and vacuum. It does not read a continuum geometry out of the existing region labels.
