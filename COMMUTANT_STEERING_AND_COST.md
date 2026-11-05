# An exact preparation-cost law without local density matrices

## 1. Result and connection

The [local preparation construction](LOCAL_PREPARATION_AND_ACCESS.md) proved that bounded-interval conditional operations approximate arbitrary vectors, while one fixed disjoint displacement target requires vanishing success probability at increasing accuracy. We now identify the general quantity governing this cost.

Let N=A(J) be a target interval algebra, omega its vacuum state, and phi any normal target state on N. Define the order constant

    c_*(phi|omega)=inf{c>=1 : phi(B)<=c*omega(B) for every B>=0 in N},
    D_max(phi||omega)=log c_*,

with c_*=infinity when no finite constant works. Then the exact maximum success probability for preparation by a contraction in the **full commutant N'** is

    p_max = exp[-D_max(phi||omega)] = 1/c_*.

The reciprocal of infinity is zero. If p_max>0 it is attained by a complete two-outcome commutant instrument. The proof applies to the standard interval/vacuum pair already constructed; no trace or density matrix on N is assumed.

For a bounded disjoint interval I, A(I) is contained in N', so the same expression is an upper bound. Equality for A(I) is **not** inferred. This separates information-theoretic feasibility from availability in a particular local region.

This is established operator-algebraic Radon-Nikodym/steering mathematics, developed here as an exact bridge between the net, its vacuum, and the recorded preparation instruments. It is not a claim to have discovered max-relative entropy or steering.

Verification: [steering_cost.py](verification/steering_cost.py), [output](verification/steering_cost.json). Exact finite examples test optimal filters, their failure completions, and the classical resolution bound. Infinite-algebra sufficiency is an analytic argument below, using one explicitly invoked standard-form theorem.

## 2. Necessity from no-signaling

Suppose K in N' is a contraction with success probability p=||K Omega||^2>0. Its conditional state on N is

    phi(B)=<K Omega,B K Omega>/p.

For every positive B in N, commutation and 0<=K^*K<=I give

    p*phi(B)=<Omega,B K^*K Omega> <= omega(B).

The complement L=(I-K^*K)^(1/2) lies in N'. The unconditioned instrument preserves omega on N. Therefore p<=1/c_*, and if c_*=infinity no exact positive-probability preparation is possible. The same argument holds for a success outcome with multiple Kraus operators, using their summed effect.

This state-order statement contains the projection-tail bounds of the earlier report but is stronger: it tests **all** positive observables in N, not just one selected readout.

## 3. Sufficiency in the full commutant

The previous local-cyclicity proof made Omega cyclic and separating for N on the original Fock space. We invoke the standard-form representation theorem: every normal positive functional on N has an implementing vector in the natural positive cone of this standard representation. For normalized phi, choose its unit vector xi_phi, so phi(B)=<xi_phi,B xi_phi>.

Suppose p*phi<=omega. On the dense domain N Omega define

    K_0(B Omega)=sqrt(p)*B xi_phi.

This is well defined and contractive because

    ||K_0(B Omega)||^2 = p*phi(B^*B) <= omega(B^*B)=||B Omega||^2.

It extends uniquely to a contraction K on the whole Hilbert space. On the dense domain N Omega it commutes with every C in N:

    K C(B Omega)=sqrt(p)*C B xi_phi=C K(B Omega).

Thus K belongs to N'. Also K Omega=sqrt(p) xi_phi, which gives the desired conditional state with probability p. Together with L=(I-K^*K)^(1/2), this is a complete two-outcome instrument. The existing unitary dilation writes its success/failure record in a supplied pointer.

If c_* is finite, the infimum is attained: take finite constants decreasing to c_* in the scalar inequalities phi(B)<=c omega(B), separately for each positive B. Then p=1/c_* works. For p=0 the formula describes impossibility, not a zero-probability conditional state.

The construction is exact but existential: the natural-cone vector and bounded extension are not an efficient synthesis algorithm for a laboratory apparatus.

## 4. Why this is not an unrestricted local preparation theorem

There are three different operation classes:

1. **A specified bounded interval A(I), disjoint from J.** Locality puts its operations in N', but it may be a strict part of N'.
2. **The full commutant N'.** The theorem gives the exact optimum here. We do not identify it with a geometrically bounded complement or assume Haag duality.
3. **Arbitrary global operations.** These need not commute with N and are not subject to the same no-signaling preparation constraint.

Section 3 proves sufficiency only for class 2. An upper bound for class 1 does not supply a bounded-region implementation attaining it. Reeh-Schlieder cyclicity still supplies arbitrary vector approximation in class 1, but with no positive uniform success guarantee.

Nor is the target here necessarily a prescribed **global vector**. The theorem specifies its state on N. Other global correlations can differ. Its commutant construction produces the natural-cone implementation, not every global vector sharing that restricted state. This distinction prevents an unjustified upgrade of remote-state steering into arbitrary exact global preparation.

## 5. Approximate targets and smoothing

For normal states psi,phi let

    d(psi,phi)=sup_{0<=B<=I}|psi(B)-phi(B)|.

This is one half of the predual norm distance for states. Define, with precisely this smoothing convention,

    D_max^epsilon(phi||omega)
       = inf{D_max(psi||omega) : psi normal state, d(psi,phi)<=epsilon}.

The **supremal** success probability for commutant preparation within this error is

    exp[-D_max^epsilon(phi||omega)].

The supremum need not be attained; no compactness of the state ball is asserted. This follows by optimizing the exact theorem over admissible psi. It remains an upper bound for operations confined to A(I).

For any effect Q with phi(Q)>epsilon, a directly testable bound is

    p <= omega(Q)/(phi(Q)-epsilon).

A vector approximation of norm error delta has d at most 2 delta by the elementary estimate used previously, so the earlier Gaussian bound is a special case. This is a probability/accuracy law, not a derived energy or computational-time bound.

## 6. Recovering the Gaussian obstruction

For the disjoint Weyl target of the previous report, choose a remote quadrature of vacuum variance v and positive mean displacement mu in the target. Its tail effects Q_R have probabilities q_R and q'_R satisfying

    q_R/q'_R <= exp[-mu*R/v+mu^2/(2v)].

Hence q'_R/q_R is unbounded as R increases. No finite order constant c_* can exist, and

    D_max(phi||omega)=infinity,  p_max=0.

This rules out exact target-state preparation even in the full commutant, not merely in a selected distant interval. The previous vanishing-success bound for increasingly accurate local vector preparation remains valid. The new theorem explains its cause as failure of bounded state domination, not a lack of algebraic density.

The vacuum is faithful and every finite Gaussian tail has nonzero probability. **Faithfulness does not imply a finite domination constant.** Thus the obstruction is not a forbidden-outcome support mismatch.

## 7. Finite-resolution readouts: exact relaxed optimum

Take a finite projective readout {Q_j} in N, all with q_j=omega(Q_j)>0, and desired probabilities r_j>=0 summing to one. Every commuting preparation of those statistics must satisfy

    p*r_j <= q_j,
    p <= min_(r_j>0)(q_j/r_j).

This bound is exactly attainable in the **relaxed commuting-readout problem**. Set

    p_*=min_(r_j>0)(q_j/r_j),
    K=sum_j sqrt(p_* r_j/q_j) Q_j,
    L=(I-K^*K)^(1/2).

Then K is a contraction, the instrument is complete, success has probability p_*, and conditional bin probabilities are exactly r_j. K lies in the commutant of the finite abelian readout algebra (in fact in that algebra itself).

This does **not** prove that K is in N' or A(I): it generally is a filter acting on the target readout. Thus this is a sharp classical/readout relaxation, not a secretly assumed distant implementation. Matching finitely many bins is weaker than preparing the complete state on N.

For refinements that separate a target distribution from the reference ever more strongly, these relaxed optima can tend to zero. The Gaussian tails exhibit this explicitly. Coarse finite readouts may conceal an infinite full-state D_max; finite experimental adequacy must not be confused with exact state identity.

## 8. A finite bipartite example where the commutant optimum is local

For comparison, in a finite pure Schmidt state

    Omega=sum_j d_j |j>_L |j>_R, d_j>0,
    rho_R=diag(d_j^2),

the full commutant of the right matrix algebra is exactly the left matrix algebra. Here the state-order criterion becomes the familiar matrix inequality p*sigma<=rho_R.

For a pure right target |psi><psi|,

    p_max = 1/<psi,rho_R^(-1) psi>.

Indeed, congruence by rho_R^(-1/2) reduces positivity of rho_R-p|psi><psi| to positivity of I-p|rho_R^(-1/2)psi><rho_R^(-1/2)psi|.

An explicit left filter is A=|0><conjugate(psi)| D^(-1), D=diag(d_j), then K=A/||A||. It produces the right vector psi and a fixed left vector on success. The complex conjugation specifies the Schmidt-basis convention; the tests use real amplitudes.

With d=(3/5,4/5) and psi=(3/5,4/5), A has first row (1,1) and second row zero. Its squared norm is 2 and p_max=1/2. For psi=(5/13,12/13), the exact optimum is 1521/2650. The script verifies the filter effects, failure completion, conditional target density and positivity of rho_R-p*sigma at the optimum.

This example illustrates when the commutant optimum really is a local subsystem optimum. It is not a finite-matrix proof of tensor factorization or this attainability for disjoint intervals in the field net.

## 9. What this adds to the unified account

The physical bridge now has a general accuracy/probability criterion compatible with infinite local algebras: common state structure, modular standardness, local and commuting operations, conditional records and information-theoretic cost are related without replacing the local algebra by an assumed finite density matrix.

It also prevents three conflations: conditional approximation with deterministic control, full-commutant access with bounded-region access, and finite recorded statistics with identity of a full state. These distinctions constrain any proposed account of finite disclosure; they do not independently determine experiential quality or ownership.

The initial modular/localization pair, actual reference state, realistic matter and constitutive Gamma/chi remain open. This is a further M0 construction within W1-W6, not a derivation of necessary actuality or a completed no-residue account.
