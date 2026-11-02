# Step 36 — An actual nonquasifree mixture and its connected four-point term

## Main result

A phase-averaged coherent sea rotation is generally **not quasifree**. It has the same one-particle covariance as a corresponding quasifree state, but different four-point functions. Computing the actual mixed-state current rather than applying Wick's rule to its mean covariance gives an extra connected term. For the controlled smooth packets here, that term is O(h²) and vanishes in the mesoscopic stress limit.

This establishes a nonquasifree example and a finite-convex-mixture extension of the preceding limit. It does not justify Wick factorization for general mixed states or imply that equality of limiting stress identifies the state.

## 1. Phase averaging is a mixture of states

Use the positive packet p, negative packet h, and coherent Slater rotation of [step 35](../wilson_coherent_rotation/REPORT.md). Let q=sin²θ. Averaging its many-body state over the coherence phase produces

\[
\omega_{\rm mix}=(1-q)\omega_0+q\omega_{\rm swap},
\]

where ω₀ is the original sea and ωswap is the pure sea with h emptied and p filled. This equality follows from the one-occupied-mode state on the two-dimensional packet sector: its phase-dependent off-diagonal density entries average to zero. Two opposite phases already realize this average exactly for this rank-two sector; no uncontrolled finite approximation to a phase integral is needed.

The averaged covariance is

\[
\overline C_a=P_-+q|V_p\rangle\langle V_p|-q|V_h\rangle\langle V_h|.
\]

It is a positive contraction and therefore also defines a quasifree state ωQF. But the existence of that quasifree state does not make it equal to ωmix.

In the packet-sector basis (empty, p, h, both), the actual mixture is

\[
\rho_{\rm mix}=\operatorname{diag}(0,q,1-q,0).
\]

The quasifree state with the same covariance diag(q,1−q) has

\[
\rho_{\rm QF}=\operatorname{diag}(q(1-q),q^2,(1-q)^2,q(1-q)).
\]

Both have the same two-point functions, but

\[
\langle n_pn_h\rangle_{\rm mix}=0,
\qquad \langle n_pn_h\rangle_{\rm QF}=q(1-q).
\]

For 0<q<1 this disproves quasifreeness of the actual mixture. Its packet number is exactly 1, while ωQF has packet-number variance 2q(1−q). The sea is unchanged outside this finite packet sector. These are explicit physical correlation distinctions, not an assignment of different phenomenal identities.

## 2. Exact current: do not Wick-factorize the mean covariance

For the actual two-site observable O=π(n₊−1/2)(n₋−1/2)/a², expectation is linear in the state. Thus its sea-relative expectation is exactly

\[
\Delta S_{\rm mix}=q\Delta S_{\rm swap}.
\]

Write the full-swap result from step 35 as L+G, with L its linear term and

\[
G=-\pi|z_p(x_+)z_h(x_-)-z_h(x_+)z_p(x_-)|^2.
\]

Then

\[
\Delta S_{\rm mix}=qL+qG,
\qquad \Delta S_{\rm QF}=qL+q^2G.
\]

The latter is obtained by Wick's rule in ωQF, where it is valid. The difference is the exact connected contribution relative to the Wick functional of the common covariance:

\[
\Delta S_{\rm conn}=-\pi q(1-q)
|z_p(x_+)z_h(x_-)-z_h(x_+)z_p(x_-)|^2.
\]

It is generally nonzero at finite spacing and separation. Replacing the actual mixture by the quasifree state of its covariance would therefore give a wrong current expectation, even though every two-point measurement agrees.

The implementation constructs the actual local density as (1−q)ρ₀+qρswap, not as ρQF(C̄). It checks both predictions against their respective finite-Fock observables and verifies their difference. The two endpoints must be actual lattice sites, with translated lattices or controlled admissible midpoint limits as previously specified.

## 3. Why the extra correlation disappears in this local limit

The smooth-packet derivative bounds imply

\[
|\Delta S_{\rm conn}|\leq\pi q(1-q)h^2
(B_{p,0}B_{h,1}+B_{h,0}B_{p,1})^2.
\]

This is an explicit bound on the connected term after the observable's a⁻² normalization. The underlying difference in the two local occupation four-point functions is a² times this current difference divided by π. It cannot be set to zero before checking the scaling.

If E_swap(a,n,t) denotes the full-swap bound from step 35, then

\[
|\Delta S_{\rm mix}-t_{\rm mix}(x,t)|\leq qE_{\rm swap}(a,n,t),
\]

\[
t_{\rm mix}=q\left\{\operatorname{Im}(\overline{v_p}\partial_xv_p)
-\operatorname{Im}(\overline{v_h}\partial_xv_h)\right\}.
\]

Consequently a→0, h=na→0, n→∞ gives the same limiting local stress for ωmix and ωQF, uniformly in position on bounded time intervals. The proof for ωmix uses linearity in actual states; it does not apply Wick's rule to a nonquasifree state. The connected estimate then compares the two states. At fixed n the familiar Wₙ factor remains in both limits.

Their equality in this limit does **not** mean that the full continuum states become equal or quasifree. The packet-mode four-point witness above remains q(1−q) in the continuum comparison. This composite loses information about that correlation structure.

## 4. Independent energy and a finite-mixture theorem

Hamiltonian energy is bilinear in the fields. Since the two states have the same covariance, their symmetrized local Hamiltonian diagnostics and total relative energies agree already before taking the continuum limit. They can nevertheless disagree on the current product, which is quartic at finite spacing.

The independent local diagnostic is q times the full-swap signed spectral Hamiltonian expression, and tends to t_mix. Total continuum excitation energy is 5q; relative particle number is zero. At q=1/2 the energy is 5/2, while actual packet-number variance is zero rather than the quasifree value 1/2. Continuum transport follows from translation of both chiral packets.

More generally, suppose finitely many actual states ωα share a reference subtraction and an observable Oₐ with relative limits tα and explicit errors Eα. For probabilities pα independent of the regulators,

\[
\left|\sum_\alpha p_\alpha\Delta S_\alpha-\sum_\alpha p_\alpha t_\alpha\right|
\leq\sum_\alpha p_\alpha E_\alpha.
\]

Thus a finite convex mixture of the controlled quasifree examples inherits an expectation-level composite limit, even if the mixture is not quasifree. Infinite mixtures require an integrable uniform bound or another justification for exchanging limits; arbitrary nonquasifree states do not follow from this argument.

## 5. Verification and boundaries

`model.py` implements actual mixed densities, the distinct quasifree densities of the same covariance, exact current and connected terms, and analytic bounds. Twenty-four tests check positivity/normalization, identical two-point data, unequal packet four-point data and number variance, exact phase averaging, local density distinction, both finite-Fock current expectations, connected-term algebra and suppression, local energy agreement, and limits. `enumeration.json` records the correlation and convergence witnesses. The numerical quadrature is not interval-certified; omitted mathematical terms are controlled analytically rather than by a generic claim that tests prove the continuum theorem.

This supplies an actual nonquasifree state-to-composite bridge on a controlled mixture class. It also sharpens nonidentifiability: covariance equality is not state equality, and equality of limiting stress does not recover higher correlations. General nonquasifree regularity, full stress operator distributions and Ward identities, absolute curved anomaly, interactions and backreaction, actual state selection, and phenomenal constitution remain additional obligations. The mathematical construction alone does not settle any of those bridges.
