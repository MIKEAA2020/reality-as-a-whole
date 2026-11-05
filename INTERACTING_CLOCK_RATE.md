# A system-dependent clock rate: constraint, rigging and physical evolution

## 1. Direct problem-of-time advance

The [turning-clock atlas](TURNING_CLOCK_ATLAS.md) used a supplied periodic phase whose velocity was a scalar. Here clock velocity is an operator on the system, and it does not commute with the system term. We solve this coupled constraint, derive its physical inner product from group averaging, and check sequential records in both reduced representations.

The constraint is

    C=N p_t+H, p_t=-i*d/dt,

with constant positive-definite system matrix N and Hermitian H. Because [N,H] need not vanish, this is not merely a scalar rescaling of an uncoupled clock. On the kinematic test domain,

    i[C,t]=N.

The clock-rate operator is system dependent. Positivity excludes rate zeros and reversal in this report; it does not solve the harder sign-changing case.

The result is a unitary reduced dynamics in a **flux-derived physical metric**, not generally in the ordinary norm of the bare conditional system vector. A concrete example has [N,H] nonzero and changing bare conditional norm while the physical norm and record probabilities stay fixed.

This is established first-order constrained-system mathematics applied explicitly to our time programme, not a new general solution of quantum gravity.

Code: [interacting_clock.py](verification/interacting_clock.py). Output: [interacting_clock.json](verification/interacting_clock.json). The infinite clock and spectral rigging arguments are analytic. Exact finite checks test spectral residues, evolution, metrics, recovery and anchored instruments.

## 2. Self-adjoint constraint and the correct reduction

Let H_kin=L2(R,dt) tensor C^d. Assume N is constant, Hermitian and uniformly positive, H is a constant Hermitian matrix. In Fourier variable k,

    C(k)=kN+H.

Multiplication by this Hermitian matrix function is self-adjoint on its maximal domain, which equals the vector first-Sobolev domain because N has a bounded inverse and H is bounded. This establishes C, rather than just its formal differential expression.

Write

    M=N^(1/2), K=M^(-1) H M^(-1), chi=M psi.

Then

    C=M (p_t+K) M,
    C psi=0 iff i*d chi/dt=K chi.

The factorization is a congruence, **not a unitary equivalence on the kinematic L2 space**. It must not be used to assume an unchanged group-average measure. Section 3 computes that measure independently.

Since K is Hermitian, every generalized solution is

    chi_phi(t)=U(t)phi, U(t)=exp(-itK),
    psi_phi(t)=M^(-1)U(t)phi.

The conserved bilinear flux is

    <psi_phi(t),N psi_eta(t)>=<phi,eta>.

In general the ordinary norm <psi,psi> is not constant. Equivalently the bare generator N^(-1)H is N-self-adjoint, not generally self-adjoint in the ordinary system metric. The reduction does not obtain unitarity by falsely setting N^(-1)H equal to a Hermitian Hamiltonian.

## 3. Group averaging derives the flux metric

Use Fourier convention f_hat(k)=(1/sqrt(2*pi)) integral exp(-ikt) f(t) dt and Schwartz test vectors. For clarity assume K has distinct eigenvalues kappa_j with orthogonal spectral projections Pi_j. The example below meets this assumption. Degenerate K requires a block version of the residue argument and is not used as an unproved extension here.

C(k) has a zero exactly at k=-kappa_j. If e_j is a unit K-eigenvector, its zero vector is v_j=M^(-1)e_j. Set r_j=||v_j||^2. The corresponding normalized C(k) eigenvalue has slope

    lambda'_j(-kappa_j)=<v_j,N v_j>/r_j=1/r_j>0.

Its spectral projection at zero is |v_j><v_j|/r_j. The projection divided by the slope is therefore |v_j><v_j|, proving the matrix distribution identity

    delta(kN+H)=M^(-1) sum_j Pi_j delta(k+kappa_j) M^(-1).

No nonunitary congruence rule for delta was assumed. The slope is the crucial clock-rate factor.

Consequently distributional group averaging gives

    integral ds <f,exp(isC)g>=<eta f,eta g>,
    eta f=sqrt(2*pi) sum_j Pi_j M^(-1) f_hat(-kappa_j)
         =integral dt U(t)^* M^(-1) f(t).

The s integral is an oscillatory/distributional spectral average, not asserted to be absolutely convergent. Evaluation at the finitely many Fourier points makes eta well defined on the chosen test space. Independent Schwartz interpolation at these points proves eta is onto C^d. Quotient by its null space and completion give H_phys=C^d with its ordinary phi inner product, hence exactly the flux inner product on generalized solutions.

This is a derivation of the physical metric from the fixed constraint and rigging prescription, not an arbitrary change of the apparatus Born rule.

There is no nonzero normalizable L2 zero vector: ||psi_phi(t)||^2 is bounded below by ||phi||^2/lambda_max(N), so its time integral diverges. Equivalently the Fourier zeros occupy a finite measure-zero set. The physical state is normalized in the rigged space, not by a uniform normal distribution on real clock readings. The first-order constraint and its stated averaging prescription are retained: replacing the generator by C^2 does not automatically preserve this spectral rigging measure.

### Strong kinematic Dirac representatives in the worked example

For the matrices in section 4, the same spectral construction works at every constraint value E. Define

    K(E)=M^(-1)(H-EI)M^(-1)=X-E*diag(1,1/4),
    kappa_+/-(E)=-5E/8 +/- sqrt(1+9E^2/64).

These eigenvalues never meet. Let Pi_j(E) be their orthogonal projectors. The spectral transform

    (F_C f)(E)=sum_j Pi_j(E) M^(-1) f_hat(-kappa_j(E))

is unitary from the kinematic Hilbert space to L2(R,dE;C2). To check the measure, take the normalized eigenvector of C(k) at eigenvalue E: it is M^(-1)e_j(E)/sqrt(r_j(E)). Changing k to E contributes 1/lambda'_j=r_j, exactly cancelling its normalization. Orthogonality of Pi_j(E) accounts for the two branches. The monotone eigenvalue branches of kN+H range from minus infinity to infinity, so this change exhausts the spectrum and the transform is onto. The construction is first defined on smooth spectral test data and extended by norm completion.

In this representation C is multiplication by E. Therefore every bounded physical A has a bounded strong-commuting representative

    O_A=F_C^(-1) (I_E tensor A) F_C.

It is a faithful unital representation, preserves products and adjoints, and commutes with the spectral projections of C. At E=0 its action is A on the rigged physical space because eta f=sqrt(2*pi)(F_C f)(0). Kinematic evaluation at E=0 is a test-space statement, not bounded point evaluation on all L2 spectral vectors. For smooth spectral representatives, these operators also preserve the required test data.

The bare-coordinate similarity operator in section 5 represents the same physical action on solutions, but must not simply be asserted to commute strongly with C. The spectral representative above supplies that stronger property in the example. Extending A constantly away from E=0 is a chosen off-constraint extension, not an additional preferred physical law.

## 4. Exact noncommuting example

Choose

    N=diag(1,4), M=diag(1,2),
    H=[[0,2],[2,0]], K=[[0,1],[1,0]]=X.

N and H do not commute. The bare generator is

    N^(-1)H=[[0,2],[1/2,0]],

which is not ordinarily Hermitian. Yet U(t)=cos(t)I-i*sin(t)X is unitary, and psi=M^(-1)U(t)phi has constant N norm.

For phi=(3/5,4/5), the ordinary squared norm is 13/25 at t=0 and 73/100 at t=pi/2, while the flux norm is one at both times. Thus bare conditional normalization cannot be treated as a state-independent unitary clock frame.

K has eigenvalues +/-1. At k=-kappa, an unnormalized zero vector of kN+H is (1,kappa/2). Its ordinary squared norm is 5/4 and its slope is 8/5. The code verifies the zero projectors divided by this slope equal M^(-1)Pi_kappa M^(-1), including all factors. It also checks the rigging Gram identity for independent Fourier data at the two poles.

## 5. Observables and sequential records

In flux coordinates the physical evaluation frames are U(t). A root observable A is represented by U(t)A U(t)^*. In bare coordinates the same observable is

    A_bare(t)=M^(-1)U(t) A U(t)^* M.

It obeys A_bare^* N=N A_bare when A is Hermitian. It need not be Hermitian in the ordinary metric. For a bare state vector psi, the physical expectation is <psi,N A_bare psi>, with flux normalization, not an ordinary unweighted expectation silently assigned to a different operator.

The bare transport is

    T_bare(t_2,t_1)=M^(-1)U(t_2)U(t_1)^*M,
    T_bare^* N T_bare=N.

Let k_j be an instrument operator acting in the flux evaluation frame at event t_j. Its anchored physical operator is L_j=U(t_j)^* k_j U(t_j). For a branch B=L_n...L_1, p=Tr(B rho B^*) as before. The same branch in bare coordinates is

    B_bare=M^(-1)U(t_n) B M,
    rho_bare(0)=M^(-1)rho M^(-1),
    p=Tr[N B_bare rho_bare(0) B_bare^*].

These agree identically. A physical density in bare coordinates is normalized by Tr(N rho_bare)=1; it is not generally an ordinary unit-trace conditional density matrix. Converting it to such a density describes a different conditioning prescription unless the metric and measured operators are carried along.

The exact test uses an initial (3/5,4/5) vector, Z measurement at a phase with cos(t_1)=3/5,sin(t_1)=4/5, then another Z measurement at t_2=pi/2. It compares all branches, checks the effect completeness identity and prefix marginal, and verifies that dropping the N factor gives the wrong physical normalization. The exact joint probabilities are [[5392/15625,3033/15625],[2592/15625,4608/15625]]. Moving the first event to t=0 changes its probabilities; this is not a dynamically frozen record example. The operations are anchored physical/Dirac instruments, not autonomously triggered detectors derived from the bare constraint.

## 6. Bare conditioning versus flux: an operational comparison

The bare evaluation E_t=M^(-1)U(t) has G_t=U(t)^*N^(-1)U(t), not a scalar. It therefore fails the ideal-frame criterion of the preceding clock-choice report in the ordinary system norm. Its polar/metric correction has physical content.

For a finite-slice operational comparison, M^(-1)=diag(1,1/2) is a contraction and can be implemented as a filter on the unit flux state U(t)phi. Its success probability is <chi,N^(-1)chi>, which is input and time dependent. A recovery filter R=M/2=diag(1/2,1) satisfies

    R M^(-1)=(1/2)I.

The combined filtering/recovery success probability is 1/4, independent of the flux input. This is an ordinary complete-instrument comparison with a specified failure branch. It is **not** a normalized probability of an exact clock instant or a uniform distribution over R.

The flux representation is the one selected by this constraint's rigging metric. It does not license claiming that a laboratory performing bare position conditioning has already implemented the flux-corrected instrument at no cost.

## 7. Clock choice and remaining boundary

A positive scalar change of clock parameter still transforms U and its event operators by the ordinary chain rule, preserving the above physical predictions. But N here is an operator and cannot generally be replaced by its expectation value as a scalar lapse: that would introduce state-dependent dynamics and discard the noncommutation with H.

This model therefore extends the direct time construction beyond uncoupled scalar clock speed. It is a solvable deparametrizable coupling class, not a claim to have handled generic quantum clock back-reaction. It derives the physical metric and records for a system-dependent positive rate, while keeping distinct ordinary conditioning, physical reduction and operational filtering.

It does not establish refoliation invariance. There is one constraint, so no nontrivial algebra of multiple local lapses or gravitational structure functions has been solved. N and H are supplied finite matrices, time independent; rate zeros/sign changes, unbounded matter generators, realistic clock resources and gravitational back-reaction remain open. No preferred actual clock or phenomenal passage is inferred.

The construction remains within M0/W1-W6 and the common no-residue objective. It supplies a further explicit constrained-time result, not completion of that objective.
