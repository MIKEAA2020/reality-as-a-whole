# Local cyclicity, conditional preparation and the cost of access

## 1. Result in the existing model

The [modular local net](MODULAR_LOCAL_NET.md) left bounded-interval vacuum cyclicity unproved. We now prove it directly, on the same Fock space and with the same vacuum:

    closure(A(I) Omega)=H_Fock for every nonempty bounded interval I.

Together with the separating property already proved, each interval is a standard algebra/vacuum pair. This is a Reeh-Schlieder property of this concrete positive-energy model, not a finite-dimensional approximation.

It yields an explicit general preparation scheme: a local two-outcome instrument can conditionally approximate any target vector. But there is a sharp operational qualification. For an explicit target obtained by a Weyl displacement in a disjoint interval, arbitrarily accurate local preparation is possible **only with success probability tending to zero**. Exact nonzero-probability bounded local preparation of that target is impossible.

These are applications of established Reeh-Schlieder and local-preparation mathematics, not claims to have discovered those principles. The gain here is a direct proof and explicit access-cost bound integrated with the existing net and record instruments.

Thus algebraic density is not unrestricted finite-region control. Localization, positive energy, global entanglement, conditional access and access cost are now linked by theorems in one model.

Verification: [local_preparation.py](verification/local_preparation.py), [output](verification/local_preparation.json). The analytic density theorem is proved below; finite checks concern Kraus completeness, displaced Gaussian distributions and the quantitative probability bound.

## 2. One-particle density in any interval

Retain H=L2(R+,dp/p), P=p>0 and

    F_f(p)=i*p*f_hat(p),
    T(t)F(p)=exp(itp)F(p).

Fix a nonzero real smooth compact smear g whose support lies strictly inside I. For all sufficiently small real t, g_t(x)=g(x-t) is still supported inside I, so W(F_(g_t)) belongs to A(I).

Suppose h in H is orthogonal to F_f for every real smooth f compactly supported in I. Define

    C(z)=<h,exp(izP)F_g>, Im(z)>0.

This is a bounded analytic function, continuous to the real boundary. Positivity of P makes exp(izP) a contraction; holomorphic differentiation inside the upper half-plane is justified by boundedness of p^n exp(-yp), y>0. On an open real interval around zero, C(t)=0 by the support condition.

A bounded analytic function continuous with zero boundary values on an open interval vanishes identically: Schwarz reflection across that interval extends it analytically, and the identity theorem applies. Thus C(t)=0 for every real t.

C is the Fourier transform of the finite complex measure

    dmu(p)=conjugate(h(p))*F_g(p) dp/p.

Its total variation is finite by Cauchy-Schwarz. Uniqueness of Fourier transforms of finite measures gives conjugate(h)F_g=0 almost everywhere. Since g is compact and nonzero, g_hat is a nonzero entire function. Its positive-real zeros are isolated, so F_g is nonzero almost everywhere. Hence h=0.

Therefore the complex span of the interval's real-smear vectors is dense in H. This proof uses positive energy and Fourier/analytic uniqueness; it does not assume a Reeh-Schlieder theorem as its conclusion.

## 3. From one particle to the local algebra

Let L_I be the closed real span of F_f with real smooth f compactly supported in I. The previous net construction puts it inside T(a)K for I=(a,b), hence

    L_I intersect iL_I={0}.

Section 2 proves closure(L_I+iL_I)=H, so L_I is standard. By the standard CCR exponential-vector cyclicity theorem, Omega is cyclic for R(L_I). Since R(L_I) is contained in A(I), Omega is cyclic for A(I) as well.

Separating is inherited from A(I) subset M_a. Consequently the vector state is faithful and normal on A(I), and its local Tomita operator is well defined on the dense domain A(I)Omega:

    S_I(A Omega)=A^* Omega.

Its closure has a polar decomposition J_I Delta_I^(1/2). We have established existence of local modular data, not a geometric formula for this interval modular group, Haag duality or a complete conformal-net reconstruction.

The general CCR theorem remains an explicit mathematical input. The new work is the bounded-interval one-particle density proof and its operational consequences for this particular net.

## 4. Turning density into a normalized local instrument

Let chi be any unit target vector, and choose A in A(I) with

    ||A Omega-chi|| < delta < 1.

Set c=max(1,||A||) and

    K=A/c,
    L=(I-K^*K)^(1/2).

Functional calculus keeps L inside A(I), and K^*K+L^*L=I. Thus these are the success/failure Kraus operators of a complete local instrument. Success probability and normalized output are

    p=||A Omega||^2/c^2 > 0,
    psi_success=A Omega/||A Omega||,
    ||psi_success-chi|| < 2 delta.

The last bound follows from the reverse triangle inequality. The three-level local unitary completion from the previous report writes success/failure into a supplied blank pointer. No unbounded measurement operation is required for any one approximation, although the norms of the approximating A may grow without bound as accuracy improves.

The density theorem is existential. It does not supply an efficient algorithm to find A for an arbitrary target, a uniform resource bound, or a positive uniform success rate.

## 5. No-signaling imposes a preparation bound

Let J be disjoint from I and Q be any projection in A(J). Completeness and locality give

    omega(Q)=p*omega_success(Q)+(1-p)*omega_failure(Q).

In particular,

    p*omega_success(Q) <= omega(Q).

If ||psi_success-chi||<=epsilon, then for every projection Q,

    |omega_success(Q)-<chi,Q chi>| <= 2 epsilon.

Therefore, whenever <chi,Q chi> > 2 epsilon,

    p <= omega(Q) / [<chi,Q chi>-2 epsilon].

This is a state-dependent operational limit, not just a declaration that communication is forbidden. Conditioning can change remote statistics, but its probability is constrained by the unconditioned state. The success label must itself become available to identify the conditional ensemble; discarding failures is not a remotely controllable deterministic preparation.

## 6. A fixed disjoint target forces success probability to zero

Choose real compact f,g supported in J with sigma(f,g) nonzero, as explicitly constructed in the local-net report. Scale/sign g so

    mu=-sigma(f,g)>0.

Let X_f be the self-adjoint generator of W(tf)=exp(it X_f). Since these unitaries lie in A(J), its spectral projections lie there. In the vacuum,

    <Omega,exp(it X_f)Omega>=exp(-v*t^2/2), v=||F_f||^2>0.

Thus X_f has centered Gaussian distribution with variance v. For the fixed unit target

    chi=W(g)Omega,

CCR conjugation gives W(g)^* X_f W(g)=X_f+mu. The target's distribution is the Gaussian with mean mu and the same variance v.

For Q_R=1_(R,infinity)(X_f), put

    q_R=omega(Q_R),
    q'_R=<chi,Q_R chi>.

Both are strictly positive for finite R. Their Gaussian densities obey, for x>=R,

    density_0(x)/density_mu(x)
       = exp[-mu*x/v+mu^2/(2v)]
       <= exp[-mu*R/v+mu^2/(2v)].

Integration gives

    q_R/q'_R <= exp[-mu*R/v+mu^2/(2v)].

For any local preparation with vector error epsilon<=q'_R/4, section 5 now yields the explicit bound

    p <= 2 exp[-mu*R/v+mu^2/(2v)].

For any proposed positive success floor, first take R large enough that the right side lies below it, then take epsilon small enough. Therefore **every sequence of increasingly accurate local preparations of this fixed disjoint Weyl target has p tending to zero**. Section 4 nevertheless guarantees some positive p for each finite requested accuracy.

For exact preparation epsilon=0, p<=q_R/q'_R for every R, immediately forcing p=0. This proves impossibility of exact positive-probability preparation by the bounded local success operator. It does not contradict the density theorem: density is approximation without a norm/success-probability bound.

### Operator-norm cost of the approximants

For the density approximants A Omega with error delta, section 4 gives normalized error below 2 delta. If delta<=q'_R/8, the same bound implies

    max(1,||A||) >= (1-delta)/sqrt(2)
                    * exp[mu*R/(2v)-mu^2/(4v)].

Indeed ||A Omega||>=1-delta and p=||A Omega||^2/max(1,||A||)^2. Thus any sequence A_n Omega converging to this fixed target must have ||A_n|| tending to infinity. Each implemented success operator K_n remains a contraction; the diverging approximant norm appears operationally as vanishing success probability. This is an operator/probability cost, not a derived bound on laboratory energy, elapsed time or computational complexity.

More generally, any complete local instrument's success branch must satisfy the same domination bound on the remote algebra. The single-Kraus construction makes the attainable approximation claim precise; no universal assertion about efficient arbitrary laboratory operations is made.

## 7. What a finite perspective can and cannot inherit from this

These results give a mathematically precise distinction relevant to the common-constitution programme:

- A local algebra in this entangled positive-energy vacuum is not an independent finite tensor factor with a separate store of reality.
- Local action on the vacuum has dense global reach in the conditional, approximation-theoretic sense.
- This does not make global control freely available. Even one fixed disjoint displacement target demands a vanishing success rate as accuracy approaches perfection.
- Apparatus, instrument choice, records, accuracy and probability must be part of an operational account of finite access; abstract algebraic density alone is insufficient.

No local region is thereby a conscious subject, no algebraic cyclic vector is identified with awareness, and no local/global mathematical relation settles phenomenal ownership. Nor does the theorem show that limited experience is metaphysically necessary. It supplies a concrete physical distinction between encompassing state structure and limited operational disclosure, without adding a separate observer to the field model.

## 8. Completion boundary

This result strengthens the same M0 construction within W1-W6. It establishes interval standardness and local modular existence, conditional preparation and a quantitative access-cost obstruction. The locality/state pair remains supplied; realistic matter, physical reference-state selection, intrinsic qualitative nature, Gamma/chi and necessary actuality remain to be constructed or justified. These unfinished tasks are not declared impossible by the preparation theorem.


## Continuation: general state-order steering optimum

[Commutant steering and preparation cost](COMMUTANT_STEERING_AND_COST.md) generalizes the projection bound to all positive observables: p*phi<=omega is necessary and sufficient for a full-commutant success contraction, with exact optimum exp(-D_max). It derives smoothed accuracy bounds and distinguishes full-commutant sufficiency from bounded-region availability. The Gaussian target above has infinite D_max, so its exact restricted state cannot be prepared with positive probability even in the full commutant.
