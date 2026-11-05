# A worked modular clock-selection construction

## 1. Result: a pair of algebras determines a transport generator

The [infinite relational clock](INFINITE_RELATIONAL_CLOCK.md) removed a global clock prior from event predictions, but still supplied the transports. Here a specified localization/state pair determines a positive translation generator through its two modular operators:

    overline[(log Delta_N - log Delta_M)/(2*pi*a)] = P_total >= 0.

This is proved in an explicit infinite-dimensional bosonic example. There is no independently adjustable transport sequence after the pair and state have been fixed. There are, however, substantial inputs to choosing that pair. This is **modular recovery of a clock candidate**, not a derivation of unique physical time from the absolute.

Three additional results matter:

- the previous finite AKLT restrictions do not give a nontrivial half-sided modular clock;
- modular invariance of the reference state does not make all two-event predictions constant;
- the modular transports can feed the existing intervention/history construction without being assumed to be unitaries inside the local algebra.

Code: [modular_clock.py](verification/modular_clock.py). Output: [modular_clock.json](verification/modular_clock.json). Infinite-space existence and inclusion arguments are analytic; finite checks do not replace them.

The modular/CCR bridge used below is a standard second-quantization theorem. The affine relation is the familiar Borchers-type relation. These are established mathematical structures, not new discoveries claimed here.

## 2. Why the earlier finite-block recipe is insufficient

For the AKLT construction, rho_1=I_3/3. Its finite-algebra modular flow rho_1^(it) A rho_1^(-it) is the identity.

For n>=2, rho_n has rank four on a 3^n-dimensional block, so the state is not faithful on the full block algebra. Compress to its support; on M_4 its eigenvalues are

    lambda_0=(1+3x)/4,  lambda_1=lambda_2=lambda_3=(1-x)/4,
    x=(-1/3)^n.

The nonzero modular frequencies are plus and minus the oriented scalar/triplet frequency

    nu_n = log[(1+3x)/(1-x)].

For n=2,3,4 this is log(3/2), log(6/7), log(21/20). It changes sign with parity and tends to zero. In fact, for n>=2,

    |nu_n| <= 6*3^(-n).

Proof: the derivative of log[(1+3x)/(1-x)] is 4/[(1+3x)(1-x)]. On |x|<=1/9 the denominator is at least 20/27>2/3, so integration from zero gives the bound. After removing an irrelevant scalar phase, the implementing unitary is exp(it nu_n P_0). Thus

    ||sigma_t(A)-A|| <= 2|t nu_n| ||A||.

The supported block flow approaches the identity at fixed t as blocks grow. Rescaling t to avoid this would introduce a block-dependent clock calibration, not derive one.

There is also a general finite-dimensional obstruction. If sigma_t(N) is contained in finite-dimensional N, both have the same dimension and the inclusion must be equality. A one-sided compression cannot be strict. Modular-invariant proper subalgebras may exist, but they do not provide the nontrivial half-sided motion sought here.

This rules out this finite-block clock recipe, not all modular constructions associated with the infinite AKLT state.

## 3. Explicit infinite standard real subspace

Take the one-particle Hilbert space H=L2(R,dtheta). Define

    (D(s)F)(theta)=F(theta+s),
    B=-i d/dtheta,  D(s)=exp(isB),
    (JF)(theta)=overline(F(theta)),
    Delta=exp(-2*pi*B).

B is self-adjoint on its usual first-Sobolev domain. J B J=-B, hence J Delta J=Delta^(-1). The closed antilinear involution

    S_0=J Delta^(1/2)

has dense domain. Define the closed real subspace K=Fix(S_0). It is standard:

    K intersect iK={0},   closure(K+iK)=H.

To verify this, any F in Dom(S_0) decomposes as (F+S_0F)/2 plus i(F-S_0F)/(2i), with both real components in K. Anti-linearity gives the trivial intersection, and closedness of S_0 gives closedness of K.

Equivalently, Dom(Delta^(1/2)) consists of the appropriate L2 analytic strip boundary functions, with

    Delta^(1/2)F(theta)=F(theta+i*pi).

K has the reality condition F(theta+i*pi)=overline(F(theta)). This is the Hardy-strip realization used for the inclusion proof. Translation of theta by real s preserves K.

## 4. A proper half-sided inclusion, with a direct proof

Define unitaries on the real boundary by

    (T(a)F)(theta)=exp(i*a*exp(theta)) F(theta),
    P F(theta)=exp(theta) F(theta),   T(a)=exp(iaP).

P is positive. For a>=0, the analytic multiplier m_a(z)=exp(i*a*exp(z)) satisfies

    |m_a(x+iy)|=exp[-a*exp(x)*sin(y)] <= 1  for 0<y<pi,
    m_a(theta+i*pi)=overline(m_a(theta)).

It therefore preserves the Hardy domain and real boundary condition, proving

    T(a)K subset K  for a>=0.

The inclusion is strict for a>0. An explicit witness in K is

    F_lambda(theta) = i*exp(theta) /
                      [sqrt(2*pi)*(lambda-i*exp(theta))^2], lambda>0.

It is analytic in the strip, has the required reality boundary value, and has uniformly bounded horizontal L2 norms: the denominator modulus squared is lambda^2+2 lambda exp(x) sin(y)+exp(2x). But T(-a)F_lambda grows at the midline like exp(a exp(x)-x), which is not square integrable. Thus F_lambda is not in T(a)K.

Now use the standard bosonic CCR theorem. On symmetric Fock space over H, let M=R(K) be the von Neumann algebra generated by Weyl operators W(F), F in K. The Fock vacuum Omega is cyclic and separating because K is standard. Its state on M is faithful and normal, and its modular operator is Gamma(Delta). This theorem, including the order-preserving, injective real-subspace/CCR correspondence, is invoked rather than reproved as a theorem of von Neumann algebras.

Let N_a=Gamma(T(a)) M Gamma(T(a))^*. Then N_a is a proper subalgebra of M for a>0, and Omega is also cyclic and separating for N_a. The vacuum is invariant under second-quantized one-particle unitaries.

The affine relation is explicit:

    D(s) T(a) D(-s)=T(exp(s)*a).

Therefore the modular action gives

    Delta_M^(it) N_a Delta_M^(-it)=N_(exp(-2*pi*t)*a) subset N_a, t<=0.

This is a proper half-sided modular inclusion. We have not proved cyclicity for the relative commutant N_a' intersect M or reconstructed a complete local conformal/AQFT net; those stronger claims are not needed for this worked pair.

## 5. Recovering the generator from the two modular operators

On the common smooth compact-support core in theta,

    T(a) B T(-a)=B-aP.

Because Gamma(T(a)) fixes Omega, covariance of modular operators gives

    log Delta_M = -2*pi*dGamma(B),
    log Delta_N = -2*pi*dGamma(B-aP).

On the finite-particle common core their difference is 2*pi*a*dGamma(P). Its closure is the positive self-adjoint P_total=dGamma(P) stated in section 1. Differences of unbounded logarithms are not assumed to be everywhere-defined bounded operators.

Thus a fixed pair (N_a subset M,Omega) determines its translation group. Without a separately specified length a, the intrinsic recovered generator is a P_total; a physical metric calibration is not supplied for free.

There is also an elementary rigidity statement within the multiplication-generator class. If a continuous positive g(theta) satisfies

    g(theta+s)=exp(s) g(theta) for all theta,s,

then g(theta)=c exp(theta), c>0. The affine covariance fixes this functional shape up to scale. This is not a classification of all possible quantum clocks or all modular inclusions.

## 6. Nontrivial operational consequences in an invariant state

The vacuum is modular-invariant: omega(sigma_t(A))=omega(A). Consequently nontriviality must not be claimed from a changing one-time vacuum expectation. Two-event correlations and interventions can nevertheless vary.

For a real half-line smearing f, use Fourier convention

    f_hat(p)=(1/sqrt(2*pi)) integral exp(ipx) f(x) dx,
    F_f(theta)=i exp(theta) f_hat(exp(theta)).

The explicit witness above comes from f_lambda(x)=x exp(-lambda x) for x>0 and zero otherwise. Its norm squared is 1/(4*pi*lambda^2). These smearings belong to K by the strip proof; no complete classification of all local subspaces is required here.

The symplectic form and Weyl law are

    sigma(f,g)=2 Im<F_f,F_g>=integral f(x)g'(x) dx,
    W(f)W(g)=exp[-i sigma(f,g)/2] W(f+g).

A modular dilation sends f_lambda to g_r(x)=r x exp(-lambda*r*x), with r=exp(2*pi*t). Elementary integration gives

    sigma(f_lambda,g_r)=r(1-r) / [lambda^2(1+r)^3].

At lambda=1,r=2 this is -2/27. The group commutator of the two Weyl operations is exp[-i sigma] I. An internal Ramsey control comparing their two orders therefore has

    p_plus=(1+cos(sigma))/2.

This is a nonconstant recorded prediction, despite invariance of the reference state. The controlled couplings and control readout can be included with the previously constructed instrument dilations.

For the recovered translation, g(x)=f_lambda(x-a), a>=0, gives instead

    sigma(f_lambda,g)=a exp(-lambda*a)/(4 lambda).

Thus the recovered translation is not merely an uninterpreted parameter: it acts nontrivially on an observable experiment algebra. These protocols are operational witnesses of flow, not a constructed autonomous clock or a unique global reading device. Implementing a modularly related smearing remains an experimental assumption.

## 7. Reference-state dependence: an exact cocycle example

For finite faithful density matrices rho,sigma, their modular flows obey

    sigma_t^sigma(A)=u_t sigma_t^rho(A) u_t^*,
    u_t=sigma^(it) rho^(-it),
    u_(t+s)=u_t sigma_t^rho(u_s).

The last law is a twisted cocycle, not generally u_(t+s)=u_t u_s. The analogous comparison for faithful normal states is the standard Connes cocycle theorem; no general infinite cocycle is calculated here.

The script takes rho=diag(2/3,1/3), sigma=R rho R^*, with the earlier rational rotation R. At t*=pi/log(2), all common scalar phases cancel. It verifies the cocycle law exactly, while u_(t*)^2 is not I and u_(2t*)=I. In the fixed sigma state, X has expectation 8/25, but after rho's modular flow at t* it has -8/25. Each reference state's own flow preserves that state.

Thus state changes need not be mere clock-unit changes. Cocycle equivalence is not by itself operational equivalence if instruments and their interpretation are held fixed. An independently warranted reference state or a justified equivalence criterion remains necessary.

## 8. Interface with the history and record constructions

Modular implementers are canonical unitaries on the common GNS Hilbert space; they are not assumed to belong to the local algebra M. A faithful state on M is also not a faithful vector state on all B(H). We do not move the modular input to the larger algebra to bypass this distinction.

The earlier Hilbert-space history and infinite rigging constructions accept these bounded unitary implementers. If P_n normalizes the represented observable algebra, the Dirac block P_n P_v^* A P_v P_n^* remains in that observable algebra even when P_n is not itself an element of it. Modular evolution and inner recording couplings both normalize the system-pointer algebra, so finite compositions retain this property.

The coherent finite-clock core can be formed in B(H_GNS), with matrix elements <Omega,P_n^* x_nm P_m Omega>. One must not substitute an expression omega(P_n^* x_nm P_m) in the local algebra when its argument need not belong there. A fully intrinsic algebraic implementation would require the implementing/crossed-product extension to be specified; it is not silently assumed.

For event times t_j and inner instrument operators K_j, modular transport gives a particularly simple local formula. Put

    L_j = sigma_(-t_j)^omega(K_j),
    B_alpha = L_n ... L_1,
    p(alpha)=sum_mu omega(B_alpha,mu^* B_alpha,mu).

This follows by moving the canonical modular unitaries to the left of the chronological branch product; they fix Omega. Automorphism invariance preserves the instrument completeness identities. Therefore prefix normalization, back-action, feedback and persistent records follow as before, but free evolution between events is now fixed by the reference modular structure rather than an arbitrary unitary table. Event placements, intervention choices, and coherent implementations remain supplied.

## 9. What was recovered and what was imported

**Recovered from the fixed pair and state:** the positive translation generator, its affine covariance, nontrivial two-event predictions, and transports usable in the constrained-history formalism.

**Imported in constructing this example:** an infinite Hilbert space with a real log-variable, the strip and its orientation, a real standard localization structure, the particular inner multiplier embedding N_a, bosonic CCR statistics, and the vacuum reference state. The multiplier already contains exp(theta); the worked construction demonstrates modular recovery and consistency, not an independent proof that nature must have this embedding. The scale a remains a calibration input.

Thus the stopping rule is respected: time has not been derived from absence of temporal structure. A free transport sequence has been replaced by a transport generator determined by a declared localization/state pair. Which pair is actual, why its localization is appropriate, and whether it selects a distinguished physical clock remain open.

The example provides an infinite von Neumann-algebra inclusion, not a complete field theory, a derivation of Lorentzian geometry, a gravitational constraint algebra, or a theorem about brains. No factor-type classification, complete AQFT net, experiential ownership, or necessary actuality is claimed. This develops M0 within W1-W6 while retaining the full experiential and axiological completion requirements.


## Continuation: localization from the same translation orbit

[The modular local net](MODULAR_LOCAL_NET.md) constructs A((a,b))=M_a intersect M_b' on the same Fock space. It proves that every interval contains noncommuting observables, establishes locality and affine covariance, and gives localized record instruments and a no-signaling theorem. No bounded-interval cyclicity or complete conformal-net reconstruction is inferred from these results.
