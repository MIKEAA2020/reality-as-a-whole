# Two clock constraints: closure, path consistency and the averaging measure

## 1. Direct target and result

The [coupled-rate construction](INTERACTING_CLOCK_RATE.md) solved one constraint and explicitly did not establish a multiple-constraint algebra. Here we construct an exact two-clock system whose constraints are self-adjoint, noncommuting and close with a nonconstant structure function:

    [D_1,D_2]=-i*beta(x)*D_2.

We solve its physical space, identify bounded strong Dirac observables, compare clock-update paths, and derive a positive, order-independent averaging prescription for the selected physical observable algebra.

A central check is negative but constructive: **naively averaging the two noncommuting constraints in sequence is not a valid physical projector.** One order even gives a non-Hermitian rigging form. Inserting the clock Jacobian repairs both orders and gives the same positive physical inner product.

This is a finite-system, two-internal-clock analogue of consistency under different clock-update routes. It is **not** the gravitational hypersurface-deformation algebra: there are no spatial metric fields, local lapse functions or Einstein constraints here. The structure function is engineered by a declared clock-rate rescaling. No solution of gravitational refoliation is claimed.

Code: [multi_clock.py](verification/multi_clock.py). Output: [multi_clock.json](verification/multi_clock.json). Exact tests concern matrix transports, curvature cancellation, event records, lapse compensation and the averaging counterexample. Domains, continuum kernels and measure identities are analytic below.

## 2. A common kinematic space and compatible clock equations

Let x be periodic modulo 2*pi, y real, and

    H_kin=L2(S1,dx/(2*pi)) tensor L2(R,dy) tensor C2.

Write A=Z, B=X, two noncommuting Pauli matrices. Define

    U(x,y)=exp(-iyB) exp(-ixA),
    (Qf)(x,y)=U(x,y)f(x,y).

U is periodic in x, so Q is a globally defined kinematic unitary. Define the commuting self-adjoint constraints

    C_1=Q p_x Q^*, C_2=Q p_y Q^*,
    C_1=p_x+H_1(y), H_1(y)=exp(-iyB) A exp(iyB),
    C_2=p_y+B.

Their self-adjoint domains and strong commutation follow from conjugating the periodic derivative and real-line derivative, not just formal commutator cancellation.

Despite [H_1,B] generally being nonzero, the connection is flat:

    partial_x B-partial_y H_1+i[H_1,B]=0.

The derivative term cancels the matrix commutator. Holding both noncommuting generators constant instead would not solve the same consistency problem. For constant A=Z,B=X, [p_x+A,p_y+B]=[A,B] is invertible on C2; a common distributional solution would have to vanish.

The exact common solutions of the compatible constraints are

    Psi_phi(x,y)=U(x,y)phi.

They are not normalizable in the noncompact y clock. Compact x periodicity is compatible because exp(-i*2*pi*A)=I.

## 3. A noncommuting first-class constraint pair

Choose a positive, bounded, nonconstant rate

    a=3/5,
    f(x)=1/(1+a*cos(x)),  5/8<=f<=5/2,
    beta(x)=f'(x)/f(x)=a*sin(x)/(1+a*cos(x)).

Set

    D_1=C_1, D_2=f(x)C_2.

Since f commutes with C_2, D_2 is self-adjoint by the joint spectral calculus; equivalently D_2=Q f(x)p_y Q^*. D_1 and D_2 are not strongly commuting. On the common smooth periodic/Schwartz core,

    [D_1,D_2]=-i f'(x)C_2=-i beta(x)D_2.

This closes on the constraints with no extra anomaly term on that core. Beta commutes with D_2, consistent with the skew-adjoint bracket. Higher common-domain and functional-algebra statements are not inferred solely from this core identity; the explicit Q representation controls the finite flows used below.

Because f and its inverse are bounded, the common generalized zero solutions are exactly Psi_phi. The rescaling has not changed that solution set. But equality of solution sets alone would not justify reusing an averaging measure; that is checked in section 5.

## 4. Physical space and strong observables

For smooth periodic functions of x and Schwartz functions of y, with system components, define

    eta g=integral dx/(2*pi) integral dy U(x,y)^*g(x,y).

The form <eta g,eta h> is positive. Eta is onto C2 by using g=U phi v(y), with integral v=1. Quotient by the null form and completion gives H_phys=C2. Integration by parts verifies eta D_1 g=eta D_2 g=0 on the test space. Section 5 also obtains this form from a corrected averaging kernel.

For any bounded system operator O, the kinematic multiplication operator

    R(O)=Q (I_clock tensor O) Q^*

is a faithful unital *-representation. It strongly commutes with both D_a because the constant system O commutes with p_x and f(x)p_y before conjugation. It obeys eta R(O)=O eta, including the adjoint relation. Thus the selected physical observable algebra has consistent kinematic and physical representations.

This constructs a rigged physical space for that declared algebra. We do not assert uniqueness under all possible choices of rigging prescription or prove adjoint intertwining for every operator in the entire kinematic commutant. No Haar averaging over an unspecified infinite gauge group is assumed.

## 5. Why naive successive averaging fails

Work first in the Q frame, with g_tilde=Q^*g. Define the partial averages distributionally by their known flows:

    P_1 g_tilde = integral_0^(2*pi) ds/(2*pi) g_tilde(x+s,y),
    P_2 g_tilde = integral_R ds g_tilde(x,y+f(x)s)
                = (1/f(x)) integral_R dz g_tilde(x,z).

P_1 is the normalized circle average; P_2 is a real-line spectral/distributional average. Neither their noncompact products nor the corrected final map are bounded projections on H_kin.

Let m(g)=integral dx/(2*pi)dy g_tilde and m_f(g)=integral dx/(2*pi)dy g_tilde/f(x). Direct substitution gives

    P_1 P_2 g_tilde = m_f(g),
    P_2 P_1 g_tilde = m(g)/f(x).

The latter is not annihilated by p_x. The former is a constant solution but gives the rigging form m(g)^*m_f(h), which need not be Hermitian. Reaching a solution is not enough to define a positive physical inner product.

An exact witness uses normalized integral in y, a fixed unit system vector, and x profiles g=1, h=cos(x). Then

    m(g)=m_f(g)=1, m(h)=0, m_f(h)=a/2=3/10.

So <g,P_1 P_2 h>=3/10 but <h,P_1 P_2 g>=0. This is a genuine continuum Fourier-integral calculation, not numerical discretization.

### Corrected averaging

Insert the positive rate multiplier between the partial averages:

    P_1 f P_2 g_tilde=m(g),
    P_2 f P_1 g_tilde=m(g).

Both orders give the same constant solution. After conjugation by Q, their kernel is U(x,y)U(x',y')^*, with circle-normalized x measure, and its test-space pairing is exactly <eta g,eta h>. This proves positivity and order independence of this corrected prescription.

The factor f is also the local gauge-fixing determinant: for clock sections x=x_0,y=y_0, the clock-velocity matrix of D_1,D_2 is diag(1,f(x_0)). Thus the missing factor is the clock-coordinate Jacobian. This is established Faddeev-Popov/rigging mathematics in a fully solvable setting, not a derivation of a gravitational path-integral measure.

No claim that arbitrary products of constraint delta functions are defined or order independent follows. The displayed products are defined through these explicit partial-flow integrals on the chosen test space.

## 6. Comparing clock-update routes

For the compatible C_a, transport between clock points z=(x,y) is

    T(z_b,z_a)=U(z_b)U(z_a)^*.

It composes and depends only on endpoints. Along x at fixed y the generator is H_1(y); along y it is B. The two coordinate orders from (0,0) to (x,y) agree:

    y after x: exp(-iyB)exp(-ixA),
    x after y: exp(-iyB)exp(-ixA)exp(iyB)exp(-iyB).

Using A unchanged on the second route would create a false path dependence by dropping the y dependence that enforces compatibility.

For D_2, a raw gauge parameter b moves y by b*f(x). Therefore equal gauge-parameter sequences in different orders need not reach the same clock endpoint. Starting from (0,0), apply an x update to alpha=arccos(3/5) and a D_2 parameter b=4/5:

    x then y: y=10/17,
    y then x with the same b: y=1/2.

These are different events, not contradictory descriptions of one event. Using b_adjusted=b*f(alpha)/f(0)=16/17 in the second route reaches the same endpoint. The nonzero bracket describes this coordinate/gauge-flow mismatch, while the properly endpoint-matched physical transport remains consistent.

## 7. Anchored intervention records

For event points z_j and reduced instrument operators k_j, set L_j=U(z_j)^*k_j U(z_j). A physical branch B=L_n...L_1 has probability Tr(B rho B^*). Using any compatible clock-update route between the same ordered event points yields the same reduced branch U(z_n)B, hence the same recorded probabilities.

The exact script uses nontrivial rational-phase rotations, compares both coordinate routes, checks two-event instrument normalization and prefix marginalization, and verifies that using the incompatible constant generators can change predictions. Path changes do not license changing the anchored event set or reordering noncommuting interventions.

These are physical/Dirac instrument predictions on the solved space. Autonomous trigger dynamics, operational access to both clocks and apparatus resources remain supplied, not inferred from path independence.

## 8. What this does and does not solve

**Constructed:** a self-adjoint noncommuting two-constraint system with a nonconstant structure function, a physical Hilbert space and faithful strong observable embedding, consistent endpoint transport, and a positive averaging prescription whose Jacobian cures an explicit naive-ordering failure.

**Not constructed:** the gravitational hypersurface-deformation algebra, spatially varying lapse/shift fields, metric-dependent structure functions, a continuum interacting field reduction, or physical selection of the clocks. Compatibility was built using a global unitary Q, and the noncommuting algebra was produced by a supplied positive rescaling. These are strong simplifying assumptions, not consequences of the absolute account.

This is direct progress on multiple-clock consistency and the measure problem within M0/W1-W6. It makes a particular constraint-closure and averaging issue explicit and solvable; it does not establish general refoliation invariance, a preferred actual time or phenomenal passage.
