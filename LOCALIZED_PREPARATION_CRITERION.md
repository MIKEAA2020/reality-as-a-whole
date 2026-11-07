# Localized preparation: the complete complementary-state criterion

## 1. The gap being closed

[Commutant steering](COMMUTANT_STEERING_AND_COST.md) gave an exact optimum for operations in the full algebra commuting with a target algebra N. A particular distant control region M=A(I) may be strictly smaller than N'. The target's restricted state alone therefore supplies a bound, not a complete regional feasibility test.

Here is the sharper result, on the same standard interval/vacuum representation. For a fixed unit **global target vector** chi, the exact optimal success probability of a bounded success operator in M is

    p_M(chi)=exp[-D_max(omega_chi restricted to M' || omega restricted to M')].

The criterion tests the target on the **entire commutant of the actual control algebra**, not only on a selected distant readout. It is necessary and sufficient, even when no density matrices exist. Approximation gives a corresponding smoothed vector criterion.

An explicit three-part finite example shows a strict gap:

    target-only commutant optimum = 1/2,
    actual control-subsystem optimum = 9/50.

The inaccessible correlated subsystem accounts for the difference. The example is not substituted for the field net; it demonstrates why the additional complementary-state condition is substantive.

Code: [localized_preparation.py](verification/localized_preparation.py). Output: [localized_preparation.json](verification/localized_preparation.json). The general theorem is analytic; the finite optimality and instrument identities are exact rational checks.

## 2. Exact bounded-region theorem

Let M=A(I), Omega the vacuum, and chi a unit vector. The earlier interval-cyclicity proof makes Omega cyclic and separating for M and hence also for M'. Define

    c_M(chi)=inf{c>=1 : <chi,B' chi> <= c <Omega,B' Omega>
                            for every positive B' in M'}.

Set c_M=infinity when no finite bound exists. Then p_M(chi)=1/c_M(chi), with value zero when c_M is infinite.

**Necessity.** If K in M is a contraction and K Omega=sqrt(p) chi, commutation gives

    p <chi,B' chi>=<Omega,B' K^*K Omega> <= <Omega,B' Omega>.

**Sufficiency.** If the inequality holds for a finite c, define on the dense domain M' Omega

    R_chi(B' Omega)=B' chi.

The separating property makes this well defined. The domination inequality makes it bounded with norm at most sqrt(c). It extends to the whole Hilbert space and commutes with M', so the bicommutant theorem puts R_chi in M. It satisfies R_chi Omega=chi. Its exact squared norm is c_M(chi), because operator norm is the supremum of the same quadratic ratios on this dense domain. Thus

    K=R_chi/sqrt(c_M),
    L=(I-K^*K)^(1/2)

are a complete local success/failure instrument attaining probability 1/c_M. All operators are bounded for finite c_M. The instrument has the previously constructed local unitary recording completion.

The unscaled R_chi is unique whenever it is bounded: if A Omega=chi for A in M, separating implies A=R_chi. No closure of an unbounded R_chi, or domain assertion for one, is needed in the infinite-cost case. The test is bounded extendibility, not an assumed everywhere-defined quotient of vectors.

For exact pure global output, several unresolved success Kraus operators cannot improve the optimum. Each nonzero branch vector must be proportional to chi; separating then makes each Kraus proportional to R_chi. Their summed effect bounds the total probability by 1/c_M. If c_M is infinite, no nonzero such branch exists.

This is a direct application of the same operator-algebraic domination principle, now to the correct complementary algebra. It is not a new general theorem of quantum theory.

## 3. Approximation and regional monotonicity

For unit target chi and vector tolerance epsilon define

    C_M^epsilon(chi)=inf{c_M(psi): ||psi||=1, ||psi-chi||<=epsilon}.

The supremal single-branch success probability at this vector accuracy is 1/C_M^epsilon. The infimum or supremum need not be attained. Global phases can be absorbed into the success operator, so optimizing phase causes no physical change.

Local cyclicity guarantees some finite-cost approximants at every positive tolerance: choose A Omega close to chi and normalize it, as before. It does not guarantee a finite cost at epsilon=0.

If M_1 is contained in M_2, then M_2' is contained in M_1', and

    c_(M_1)(chi)>=c_(M_2)(chi),
    p_(M_1)(chi)<=p_(M_2)(chi).

Increasing the actual control algebra cannot worsen this optimum. This is algebra inclusion, not a claim about physically free expansion of an apparatus.

## 4. Restricted targets require an extension optimization

Suppose only the target state phi on N is prescribed, with N contained in M'. For a **single coherent success operator**, the localized optimum is

    sup over unit chi with omega_chi|N=phi of 1/c_M(chi).

One must optimize the target's otherwise unspecified global correlations as well as its marginal. In the field representation, normal phi has vector implementations by standardness of N. This formula does not identify those implementations with each other.

Restriction to N can only reduce the domination constant, so this localized optimum is bounded above by exp[-D_max(phi||omega|N)]. Equality is not automatic. Multiple success Kraus operators with unresolved outputs require an extension/ensemble optimization beyond the single-vector formula; no equality for that broader class is silently inferred.

For the fixed disjoint Weyl target studied previously, even the restricted-state D_max is infinite. The full complementary cost is therefore infinite as well. The new criterion is stronger where the selected marginal by itself has a finite bound.

## 5. Explicit strict gap: a correlated inaccessible subsystem

Take a control subsystem L of dimension four and two inaccessible qubits E,R. In the basis indexed by (e,r), let

    Omega = sum_(e,r) sqrt(q_er) |er>_L |e>_E |r>_R,
    (q_00,q_01,q_10,q_11)=(9,1,1,9)/20.

The control algebra is M=B(L) tensor I_ER. The target readout algebra is N=B(R). All q_er are positive, so Omega is cyclic and separating for M on this 4-by-4 Schmidt representation. The complementary marginal is rho_ER=diag(q_er), while rho_R=I/2.

Ask for the pure target |+><+| on R. The target-only bound is

    p<=1/<+,rho_R^(-1)+>=1/2.

It is attainable with access to the full commutant of N, which includes E as well as L: Schmidt-decompose Omega across R versus LE. Its two orthonormal partner vectors are

    eta_0=(3|00>_L|0>_E+|10>_L|1>_E)/sqrt(10),
    eta_1=(|01>_L|0>_E+3|11>_L|1>_E)/sqrt(10).

The projection onto eta_+=(eta_0+eta_1)/sqrt(2), acting on LE, succeeds with probability 1/2 and prepares |+> on R. It is not an operation confined to L.

### The tighter control-only optimum

Any success ensemble with pure marginal |+><+| on R must have conditional complementary state tau_E tensor |+><+|. This follows from positivity: a pure marginal leaves no support in the orthogonal R subspace. Commutation of all control operations with ER requires

    p*tau_E tensor |+><+| <= rho_ER.

Dephasing E preserves rho_ER and the target, so for an upper bound we may replace tau_E by diagonal weights t_0,t_1. In block e, the rank-one positivity criterion gives

    p*t_e <= w_e,
    w_e = 1/<+,diag(q_e0,q_e1)^(-1)+>
        = 2*q_e0*q_e1/(q_e0+q_e1) = 9/100.

Summing the two inequalities yields p<=9/50. This upper bound holds even for multiple success Kraus operators; it does not rely on a pure global output assumption.

It is attained by a single control filter. Let K=A/sqrt(10), with rows in the L basis (00,01,10,11):

    A = [[1,3,0,0],
         [0,0,0,0],
         [0,0,3,1],
         [0,0,0,0]].

K^*K is a projection, so L_fail=I-K^*K is a valid failure operator. The success vector has four equal unnormalized amplitudes 3/sqrt(200), with left label 00 for e=0 and 10 for e=1. It has norm squared 9/50 and normalized R marginal |+><+|.

Thus the target-only bound overestimates regional success by the factor 25/9. The missing restriction concerns correlations with E, not just the target's right-qubit probabilities.

## 6. A finite semidefinite synthesis problem

When the control system purifies the entire inaccessible complement with a full-rank finite Schmidt matrix D, the restricted-target problem has a constructive optimization form. Let rho_C=D^2, C=E tensor R. A control effect F=K^*K, 0<=F<=I, produces the subnormalized complementary state

    tau_C=D F^T D.

Conversely every 0<=tau_C<=rho_C is attained: choose

    F=(D^(-1) tau_C D^(-1))^T, K=sqrt(F).

Transpose refers to the chosen Schmidt basis. Thus for a prescribed target state sigma_R the exact optimum is the finite semidefinite program

    maximize p,
    subject to 0<=tau_C<=rho_C,
               Tr_E(tau_C)=p*sigma_R.

This includes mixed restricted targets and unresolved success ensembles. They cannot improve the optimum because every feasible complementary success state already has a single-filter realization in this full-Schmidt control setting. The completion (I-F)^(1/2) records failure.

The preceding example is solved analytically by its two block positivity bounds; its displayed filter supplies a matching feasible solution. No numerical SDP solver or optimization tolerance is needed for that certificate. For general finite inputs this is an algorithmic problem, not a promise of computational efficiency at large dimension.

This finite synthesis formula does not supply a density matrix for the field complement. The field theorem remains the state-order/commutant criterion, and evaluating its optimum for a realistic interval remains open.

## 7. Meaning for localized access

The model now has a complete exact **criterion** for local pure-vector preparation, though generally not an efficient method for evaluating it or synthesizing its operator. The finite example demonstrates why regional control cannot in general be computed from a target region's state alone.

Applied to finite-disclosure candidates, the lesson is specific: the relevant physical access constraints depend on the operation algebra and its full complementary state, not merely an observer-labelled subsystem or a small list of readouts. This supplies a mathematical dependency that a proposed constitution must respect; it does not select a subject or assign an intrinsic quality.

No claim is made that the finite L/E/R factorization is the field net's regional factorization. The field result uses commutants and vector states directly. Determining actual localization, realistic matter, intrinsic qualitative constitution and necessary actuality remains open within the same M0/W1-W6 programme.
