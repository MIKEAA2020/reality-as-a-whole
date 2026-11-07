# Constructive step 17: a spacetime-indexed free Dirac CAR net

## Result and scope

The previous steps provided [CAR dynamics](../fermionic_lift/REPORT.md) and a [quasifree ground state](../quasifree_vacuum/REPORT.md). Here they are organized into an explicit spacetime field net and its parity-even observable net in 1+1-dimensional Minkowski space. The construction establishes isotony, graded/even locality, a diamond time-slice property, proper-orthochronous Poincaré covariance, and an invariant positive-energy vacuum representation. These are conditional properties of the specified **free** model, not empirical derivations of spacetime, statistics, or the physical vacuum.

A spacetime-smearing limit connects this continuum construction to the walk. It is convergence of fixed smeared fields and bounded correlations, **not** exact finite-spacing inclusion of lattice regional algebras or a general theorem of net convergence. The parity-even construction also requires a qualification about disconnected-region additivity.

The continuum arguments below are analytic. Thirty-two finite tests check signs, finite analogues, quadrature, geometry, and counterexamples; they do not numerically prove infinite-dimensional statements.

## 1. From spacetime sources to equal-time CAR

Use H = L²(R,C²), h = -iZ∂x + mX, m > 0, and D_t = exp(-ith), with the conventions of steps 14–16. For a smooth compactly supported spinor source F(t,x), define the Bochner integral

\[
QF=\int_{\mathbb R}D_t^*F_t\,dt,\qquad
\Psi(F)=a(QF).
\]

The map Q is linear and satisfies ||QF|| ≤ ∫||F_t|| dt. The field Ψ is antilinear in F and bounded for each such smearing. Point fields are not bounded operators obtained by evaluating this formula at a delta function.

Let P = i∂t-h. Integration by parts, with no boundary contribution for compact temporal support, gives

\[
Q(PF)=\int D_t^*(i\partial_t-h)F_t\,dt=0.
\]

Thus the field satisfies the free equation in smeared form. This states the necessary null relation, without asserting an unproved characterization of every element of ker Q. The CAR are

\[
\{\Psi(F),\Psi(G)\}=0,\qquad
\{\Psi(F),\Psi(G)^*\}=\langle QF,QG\rangle I.
\]

Equivalently,

\[
\langle QF,QG\rangle
=\int dt\,ds\,\langle F_t,D_{t-s}G_s\rangle.
\]

This is the causal anticommutator pairing, not a rule assigning independent tensor factors to different times.

## 2. Regions, isotony, and causal locality

For an open spacetime region O, set

\[
\mathcal F(O)=C^*\{I,\Psi(F),\Psi(F)^*:F\in C_c^\infty(O,\mathbb C^2)\},
\qquad \mathcal A(O)=\mathcal F(O)^{\rm even}.
\]

The superscript means the fixed points of the parity automorphism a(f) ↦ -a(f). Both nets are isotonic: O₁ ⊂ O₂ implies inclusion of the corresponding algebras. This is a chosen observable subnet; CAR alone does not establish all physical superselection rules or decide actuality.

The Dirac propagator has propagation speed at most one. For spacelike-separated O₁,O₂, all supports in the pairing above are separated beyond |t-s|, so that pairing vanishes. Hence odd generators from the two field algebras anticommute, and their mixed anticommutators vanish. Reordering finite monomials gives graded locality; parity-even polynomials commute across the regions, and norm closure gives

\[
[\mathcal A(O_1),\mathcal A(O_2)]=0.
\]

**Do not replace this proof by disjointness of reference-slice shadows.** Two spacelike regions far in the future can have overlapping causal shadows at t=0. Their propagated subspaces are nevertheless orthogonal by the propagator identity. A finite inverse-walk check explicitly exhibits overlapping supports with zero inner product.

## 3. Time slices and diamonds

Let I = (x₀-R,x₀+R) at t=0 and D(I) = {(t,x): |t|+|x-x₀| < R}. Every F compactly supported in D(I) has QF supported inside I, by finite propagation. Conversely take f in C_c^∞(I,C²), with distance d > 0 from the endpoints, and choose χ in C_c^∞((-ε,ε)) with integral one and 2ε < d. Put

\[
F_t=\chi(t)D_t f.
\]

This is smooth and compactly supported in D(I), because propagation expands the support of f by at most |t|, and

\[
QF=\int\chi(t)D_t^*D_t f\,dt=f.
\]

By density of such f in H(I) = L²(I,C²), the generated field algebra is exactly the embedded CAR algebra on that subspace:

\[
\mathcal F(D(I))=\operatorname{CAR}(H(I))\subset\operatorname{CAR}(H).
\]

If N is any open subset of D(I) containing its whole base slice {0}×I, the same right inverse can be supported in N: for each compact initial support choose ε sufficiently small. Thus F(N) = F(D(I)), and likewise for their even parts. Translations and boosts transport this result to the corresponding diamonds and Cauchy slices. Globally every open strip containing the full reference Cauchy surface generates CAR(H). These are precise time-slice statements; an arbitrary small patch of a Cauchy surface does not generate every spacetime observable.

## 4. Poincaré covariance, including the source transformation

### Translations

For b = (s,y), define F_b(t,x) = F(t-s,x-y), and let T_y f(x) = f(x-y). Then

\[
QF_b=D_s^*T_y QF.
\]

These one-particle unitaries induce the translation automorphisms of CAR(H), carry F(O) to F(O+b), and preserve parity.

### Boosts on solutions and Cauchy data

Use Λ_η(t,x) = (coshη t-sinhη x, coshη x-sinhη t), and S_η = exp(-ηZ/2). With γ⁰=X, γ¹=-iY, the gamma identities of step 14 imply that

\[
\psi'(z)=S_\eta\psi(\Lambda_\eta^{-1}z)
\]

maps Dirac solutions to solutions. The induced Cauchy-data map U_η is unitary, even though S_η is not a unitary 2×2 matrix. One can establish this from the conserved Dirac current on tilted Cauchy surfaces; explicitly it also follows in momentum space as follows.

On branch σ = ±1, E_σ(k) = σ sqrt(k²+m²), put

\[
k'=\cosh\eta\,k-\sinh\eta\,E_\sigma(k),\qquad
J_\sigma(k)=\frac{dk'}{dk}=\cosh\eta-\sinh\eta\,\frac{k}{E_\sigma(k)}>0.
\]

For a branch-valued amplitude φ_σ(k), the transformed amplitude is S_η φ_σ(k)/J_σ(k), evaluated at k'. The transformed spinor lies in the same energy-sign branch at k', and ||S_η φ_σ||² = J_σ||φ_σ||². Changing variables dk' = J_σ dk proves preservation of the L² norm. The two branches remain orthogonal at each transformed momentum. The inverse boost establishes surjectivity. The solution action gives the group law and its covariance with translations; on dense smooth wavepackets the formulas are strongly continuous and extend to all H.

### Sources transform contragrediently

The source transformation compatible with Q is **not** simply S_η F at the transformed point. It is

\[
F_\eta(z)=(S_\eta^{-1})^*F(\Lambda_\eta^{-1}z),\qquad
QF_\eta=U_\eta QF.
\]

To see this, pair QF with arbitrary initial data f, write the pairing as the spacetime integral of (D_t f)*F, use unitarity of U_η on Cauchy data, and change variables by Λ_η, whose determinant is one. The adjoint inverse is forced by this pairing. The finite tests check this duality and show why replacing it by S_η would fail.

The CAR automorphism a(f) ↦ a(U_η f) therefore carries F(O) exactly to F(Λ_η O), and likewise for A. This constructs proper-orthochronous Poincaré covariance of the continuum net. Parity and time reversal, higher-dimensional spin structures, and covariance of the finite lattice are not claimed here.

## 5. Vacuum implementation and the spectrum condition

The polarization C=P_- commutes with translations. Proper-orthochronous boosts preserve energy sign on the massive mass shell, so U_η also commutes with C. Thus ω_C is invariant under all the preceding automorphisms. Its particle/hole Fock representation implements them by the second quantization of

\[
U|_{H_+}\oplus\overline{U|_{H_-}},
\]

fixing the vacuum. In particular, with the convention V(s,y) = exp(iK s-iP y), particles have energy/momentum (E(k),k), and holes (E(k),-k). Both lie on the future mass shell. Finite sums and their spectral closure lie in the closed forward cone, so K ≥ |P| and the vacuum has zero excitation energy/momentum. This is the joint translation spectrum condition, not just positivity at one chosen time.

For the observable net the vacuum representation is taken on the cyclic subspace closure of π(A(global))Ω, namely the even particle/hole sector. The full field Fock space also contains odd charged sectors; its vacuum is not cyclic for the even algebra on that larger space. Restricting to the observable vacuum sector preserves covariance and the spectrum condition. No observer or episode is identified with one of these sectors.

## 6. A genuine qualification: disconnected even regions

The field net is additive under open covers: split compact test functions by a partition of unity and use linearity of Q. The even fixed-point prescription is not automatically additive for disconnected unions.

If O₁ and O₂ are disjoint, a product of one odd field from each is even in F(O₁∪O₂). It need not belong to the algebra generated by A(O₁) and A(O₂). In a finite CAR example c₀* c₃ is globally even but fails to commute with the parity of the first component, whereas both separate even algebras commute with that parity. Hence it cannot be generated by them. This is not a failure of spacelike commutation. It is a distinction between the fixed-point algebra assigned to a disconnected union and the additive algebra generated by its components.

We keep the definition A(O)=F(O)^even explicit and do not assert unrestricted disconnected-region additivity, Haag duality, or other stronger net axioms. No algebra type, modular identification, nuclearity, or interacting existence theorem is established by these calculations.

## 7. What the lattice approximation preserves

For F compact in time and space, define a discrete comparison smearing on the same continuum H:

\[
Q_aF=a\sum_{n\in\mathbb Z}\widetilde U_a^{-n}P_a F_{na},
\]

where P_a is the Brillouin projection and U-tilde_a is the **one-step** embedded walk, identity on the complementary tail. The sum is finite by temporal compactness. This formula uses the same common-space convention as steps 15–16; negative powers exist by unitarity.

For a fixed band |k| ≤ K and sampled times |na| ≤ L, the adjoint/negative-time product bound is at most LaK|m|. If G(t)=D_t*F_t, whole-line left Riemann quadrature obeys

\[
\left\|a\sum_nG(na)-\int G(t)dt\right\|
\le a\int\|G'(t)\|dt,
\qquad G'(t)=D_t^*(ihF_t+\partial_tF_t).
\]

The derivative is integrable for smooth compact sources. Comparing the discrete evolution with G at each sampled time gives

\[
\|Q_aF-QF\|
\le LaK|m|\,a\sum_n\|(F_{na})_K\|
+2a\sum_n\|F_{na}-(F_{na})_K\|
+a\int\|G'(t)\|dt.
\]

First let a → 0 with K fixed. Then let K → infinity. The temporal family F_t has compact image in H, so momentum cutoffs converge uniformly on that family; temporal support bounds the sums. This proves Q_aF → QF in H. The exact CAR field norm transfers it to

\[
\|a(Q_aF)-\Psi(F)\|\longrightarrow0.
\]

Telescoping products and the weak-* state convergence of step 16 give convergence of fixed finite smeared correlations, including the quasifree vacuum correlations.

**What is not preserved exactly:** P_aF_t has noncompact spatial tails. Its inverse lattice Fourier image therefore generally has arbitrarily distant nonzero coefficients, even though F is spacetime compact. The above approximants are not asserted to belong to a sharply corresponding finite-spacing local region. Nor are all continuum test functions exactly bandlimited. Thus we have an exact local continuum net and a controlled fixed-smearing approximation, not a proof of exact regional-algebra convergence, uniform convergence over all smearings, or lattice boost covariance. A region-preserving scaling construction would require additional localization estimates and a specified notion of net convergence.

## 8. Verification and integration ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests check smearing linearity/CAR, time-slice cancellation, equation-of-motion quadrature, translation signs, support budgets, spacelike geometry, inverse-walk cones and orthogonality, boost shell/Jacobian/source formulas, even locality and disconnected additivity obstruction, and refinement of continuum/walk spacetime quadrature. Momentum samples are not compactly supported spacetime sources; their numerical roles are limited accordingly. Representative diagnostics are saved in `enumeration.json`.

**Earned:** an explicit free spacetime field/observable construction with stated locality, time-slice, covariance, vacuum, and spectrum properties; fixed-smearing lattice approximation with its support limitation exposed.

**Not earned:** derivation of Minkowski geometry from the lattice or from mathematical necessity; physical selection of CAR, the free law, or the chosen vacuum criterion; all AQFT axioms for every region prescription; interactions, quantum gravity, or a bridge to the remaining geometric frameworks; phenomenal constitution or ultimate explanation. This is a concrete quantum-information/operator-algebra/relativistic-field overlap, not the completed whole-account.

**Next useful bridge:** address region-preserving approximation rather than merely global smear convergence, or introduce an explicit geometric reconstruction problem and test what the causal/local net actually determines. Neither should be treated as automatic from covariance.

## Continuation: compact-cell scaling

[Step 18](../local_scaling/REPORT.md) resolves part of the localization gap using a different, compact-cell comparison isometry. It proves exact embedded inclusion and fixed-element approximation for reference-slice diamonds, plus compact spacetime-smearing and vacuum-state convergence. It does not silently turn the earlier Fourier embedding into a compact one, or assert uniform approximation and exact inclusion for every spacetime region.
