# Finite completion, a stopped time record, and controlled future escape

## 1. The connecting construction

This combines the [finite autonomous recorder](AUTONOMOUS_RECORD_INSTRUMENT.md) and the [stopped-clock mechanism](AUTONOMOUS_STOP_CLOCK.md) in **one specified Hamiltonian and one preparation**. It is not a sum of error numbers from incompatible earlier packets.

The result supplies:

- A finite-time, complete completion-flag/time-record instrument.
- An explicit bound on a flag firing before the stopping region has been passed, for any one interrogation epoch.
- A stopped internal time reading and a quantum-system record with a finite completion guarantee.
- A **uniform all-future error bound**, replacing the earlier linearly growing holding-time estimate by an integrable escape estimate.
- A controlled comparison with conserved outgoing record effects for this same device, including a failure complement.

**Not claimed:** continuous first-click monitoring, an exactly irreversible latch, a universal quantum first-entry observable, resistance to arbitrary memory noise, or gravitational refoliation. The operational time reading is still a calibrated stopped/sojourn-clock reading. All accuracy claims concern the specified closed model and prepared resources.

Code: [finite_completion_clock.py](verification/finite_completion_clock.py). Results: [finite_completion_clock.json](verification/finite_completion_clock.json).

## 2. One autonomous, bounded-below Hamiltonian

Use carrier X,P, pointer Y,K, measured qubit S, detector D, memory M, environment E and completion flag F. Set

    B_AB=P1_A (I-X_B)/2,    B_F=(I-X_F)/2,
    H_S=omega X_S,
    epsilon(K)=K^2/(2M_pointer).

There are three record regions of length ell, separated by gap d:

    [0,ell], [ell+d,2ell+d], [2ell+2d,3ell+2d].

Their positive projectors are B_SD, B_DM, B_ME. Each profile is

    kappa(x)=(2pi/ell) sin^2(pi(x-x_left)/ell),

inside its region and zero outside, with area pi. Let

    x_s=3ell+3d.

The pointer stopping coefficient is

    r(x)=1                                      for x<=x_s,
         cos^2(pi(x-x_s)/(2ell))                 for x_s<x<x_s+ell,
         0                                      for x>=x_s+ell.

After another gap d, a fourth profile rotates the completion flag, in

    [4ell+4d,5ell+4d].

Write L=5ell+4d for its end. K_rec(x) denotes the three record profiles plus the flag profile, with their projectors. The full physical Hamiltonian is

    H=P^2/(2m)+H_S+v K_rec(X)+r(X) epsilon(K).

All spatial controls are fixed. No physical coupling is externally switched at a chosen time. All potentials except H_S are positive, so H>=-omega. Since pointer momentum K is conserved, H is defined as the self-adjoint direct integral over k of quadratic carrier Hamiltonians with bounded matrix potentials, on its maximal spectral domain. Equivalently use the corresponding closed kinetic form. A naive common H2 domain for both coordinates is not required.

The apparatus assumptions are explicit: degenerate free detector/memory/flag Hamiltonians, an exactly vanishing right-side pointer kinetic term and engineered controlled interactions. They are not material-device derivations or thermodynamic guarantees of a robust macroscopic latch.

## 3. Product preparation and reference calibration

Prepare the carrier in

    exp(i p0 x) f(x+d0),    p0=mv,

where f is the normalized real cos-squared envelope on [-a,a], d0>a. Its exact norms are

    ||f'||=pi/(sqrt(3)a)=:f_1,
    ||f''||=pi^2/(sqrt(3)a^2)=:f_2.

Prepare the pointer in the real cosine momentum packet g(k), centered at k0 with half-band b<k0. Thus epsilon<=epsilon_max=(k0+b)^2/(2M_pointer) throughout the actual evolution. The ready internal state is

    arbitrary rho_SR, |0>_D |0>_M, I_E/2, |0>_F,

independent of the carrier/pointer; R is an arbitrary untouched reference. Blank registers and the coherent pointer preparation are counted initial resources.

For proof only, boost the carrier and compare its quadratic Hamiltonian with transport vP. Include H_S exactly before

    t_pre=(d0-a)/v,

the earliest reference entry into the first record region. Omit H_S in the comparison during the short active interval, and include it exactly again after

    T_0=(L+d0+2a)/v.

The switching here is **only in a comparison trajectory**, not in the physical H. The target Z record refers to the freely evolved input at t_pre. Its relation to the finite-width internal entrance event is a calibration, not an externally triggered measurement gate.

The reference carrier moves as x=x0+vt. The stopping-pointer phase is exact, not linearized in its momentum:

    exp[-i epsilon(k)/v integral_[x0]^x r(u)du].

All pointer terms commute with the internal record interactions. At T_0 the complete reference packet lies beyond L+a, every record gate has completed and F=1. The internal product of gates gives the same Lüders S/D/M channel as before after E is traced.

The pointer has stopped after running for

    tau(x0)=(x_s+ell/2-x0)/v,
    tau0=(x_s+ell/2+d0)/v.

The ell/(2v) contribution is the calibrated smooth stopping latency, not an asserted zero-width first-crossing time. The pointer remains correlated with initial carrier position. That correlation is retained in the bound, not replaced by one sharp classical path.

## 4. Finite-time Duhamel estimate, including stopping backaction

On the initial packet support K_rec(x0)=0 and r(x0)=1. Differentiating the ordered reference propagator with both endpoints shifted gives the effective derivative generator

    D(x)=K_rec(x)+(r(x)-1)epsilon/v.

This accounts for pointer-energy release: it is not legitimate to retain the old derivative bound and ignore the stopping term. Define

    k=2pi/ell, k'=2pi^2/ell^2, r'=pi/(2ell),
    b_D=k+epsilon_max/v,
    C_in=f_2+2b_D f_1+k'+r' epsilon_max/v+b_D^2,
    C_out=f_2+2(epsilon_max/v)f_1+(epsilon_max/v)^2.

The carrier second-derivative norm is at most f_2 during the free approach, C_in during active registration/stopping and C_out after completion in the transport comparison. Therefore, uniformly over all system/reference inputs,

    delta_0=t_pre f_2/(2m)
             +(T_0-t_pre)[C_in/(2m)+omega].

This bounds the full purified actual/reference vector difference at T_0. Both the carrier and stopped pointer are retained; reflection, recoil and spreading have not been removed.

For a chosen clearance distance D>2a, continue the reference for

    h_clear=(D-2a)/v,
    T_c=T_0+h_clear,
    delta_c=delta_0+h_clear C_out/(2m).

At T_c the reference carrier center is L+D. H_S is included exactly during this continuation. For D<=2a use h_clear=0 and the actual clearance D=2a. This finite construction already gives half-diamond instrument error at most min(1,delta_c), but would still yield a growing future bound if transport comparison were continued indefinitely. The next estimate removes that growth.

## 5. Escape estimate: control all later recrossing amplitudes

After T_c compare with the **physical quadratic outgoing Hamiltonian**

    H_out=P^2/(2m)+H_S,

rather than with continued linear transport. The pointer and all record qubits are stationary under H_out. On the invariant prepared pointer band,

    W=H-H_out,
    ||W||<=W_max=vk+epsilon_max,
    W vanishes for X>L.

The reference carrier at T_c, conditional on pointer k, has centered momentum envelope

    f_hat(p-p0-epsilon(k)/v).

This extra momentum shift is retained. It is precisely why stopping backaction contributes to the derivative estimates.

### Remove a controlled small low-momentum tail

Choose a C1 sine-squared cutoff chi(p), zero below p0/4 and one above p0/2, with

    ||chi'||_infinity<=2pi/p0=:c_1,
    ||chi''||_infinity<=8pi^2/p0^2=:c_2.

The removed norm is at most

    eta=2f_1/p0,

by Chebyshev on the centered carrier momentum; epsilon/v>=0 only improves the estimate. Assume eta<1. No claim of exactly positive momentum is made for the original compact-position packet.

### Explicit integrable left-tail estimate

Weighted Cauchy–Schwarz and Plancherel give uniform L1 bounds for the centered Fourier envelope and its first two momentum derivatives:

    L_0=sqrt(pi/a) sqrt(1+a^2 f_1^2),
    L_1=sqrt(pi/a) sqrt(a^2+a^2(1+a f_1)^2),
    L_2=sqrt(pi/a) sqrt(a^4+a^2(2a+a^2 f_1)^2).

After the cutoff, set

    H_0=L_0,
    H_1=L_1+c_1 L_0,
    H_2=L_2+2c_1 L_1+c_2 L_0,
    p_min=p0/4, v_min=p_min/m,
    A_tail=[H_2+3H_1/p_min+3H_0/p_min^2]/sqrt(2pi).

For x<=L, two integrations by parts in the free quadratic phase give

    |psi_out(s,x)|<=A_tail/(L+D-x+v_min s)^2.

Indeed the phase derivative has magnitude at least L+D-x+v_min*s; the second derivative is -s/m, and s/m is at most that denominator divided by p_min. Integrating the squared bound over x<=L yields

    ||1_[X<=L] exp(-iH_out s) chi psi_ref||
       <=A_tail/[sqrt(3)(D+v_min s)^(3/2)].

The same estimate holds for the pointer-entangled packet: its momentum shifts have uniform bounds, and integration of |g(k)|^2 is one. Internal/reference unit vectors do not change the spatial estimate.

Consequently the complete future interaction is integrable:

    C_escape=integral_0^infinity ||W exp(-iH_out s)chi psi_ref|| ds
             <=2 W_max A_tail/[sqrt(3)v_min sqrt(D)].

This is a Cook/Duhamel bound, not a sampled assertion that the carrier usually continues right.

### Uniform all-future theorem

Splitting off the low-momentum tail costs at most 2eta in a comparison of two unitary evolutions. Thus for every s>=0,

    ||psi_actual(T_c+s)-exp(-iH_out s)psi_ref(T_c)||
       <=delta_c+2eta+C_escape=:delta_infinity.

The estimate is uniform over system inputs and entangled references. It immediately bounds the **entire completion-flag, memory and pointer record channel** in half-diamond distance by min(1,delta_infinity), for every later interrogation epoch. This no longer grows linearly with the holding duration. It applies to unmonitored autonomous evolution followed by one interrogation at any chosen later epoch, not to a joint history of repeated reads. In particular, a sharp Y measurement can broaden the conserved K distribution and invalidate the prepared-band estimate for subsequent evolution; repeated-read retention requires its own measurement model.

It is a finite-error guarantee for a closed model with exactly degenerate record degrees of freedom, not proof of exact irreversible permanence or stability against additional noise.

## 6. Complete finite instrument and what the flag means

Let V_t be the isometry obtained by the specified initial resource states and actual exp(-itH), including a purification of E if desired. Read the actual flag with projectors P0_F,P1_F. On F=1, read Y and the memory in their respective spectral/computational bases. Schematically,

    J_0,t(rho)=Tr_aux[P0_F V_t rho V_t^dagger P0_F],
    J_1,B,t(rho)=Tr_aux[P1_F 1_B(Y) V_t rho V_t^dagger 1_B(Y)P1_F],

Here Tr_aux traces carrier, pointer, detector, environment and flag, leaving S and memory; tracing the pointer makes the displayed maps additive in B. Additional computational-basis memory labels can then be attached. The usual spectral-measure formulation applies. These are CP maps; integrating all pointer/memory outcomes and adding J_0,t is trace preserving. The flag transition is caused by its spatial Hamiltonian, not an absorbing rule inserted into the evolution.

At completion,

    Pr(F=0 at T_0)<=min(1,delta_0^2).

For every t>=T_c,

    Pr(F=0)<=min(1,delta_infinity^2),
    Pr(D!=M)<=min(1,delta_infinity^2).

Before/during completion, for any one chosen t<=T_0, the reference never has F=1 while X is at or before the stopping region's end. Hence

    Pr(F=1 and X<=x_s+ell at t)<=min(1,delta_0^2).

This is a bound at each **single interrogation**, not the probability of ever observing a false flag under continuous monitoring. Repeated measurements change the dynamics and would require a new instrument analysis.

Finite-time F=0 means **not completed in this flag experiment**. It includes delayed/reflected and imperfectly registered amplitudes; it is not the reflection-only no-click outcome of the earlier asymptotic step model. Conditional completed-state distances can be bounded by 2delta_infinity using the gentle projection estimate, but normalized conditional maps are not assigned a diamond norm. The complete instrument is the primary guarantee.

For any two interrogation times t,t'>=T_c the record distributions differ in total variation by at most min(1,2delta_infinity), since the common ideal memory/flag/pointer record is stationary under H_out. This gives quantified readout-window independence without choosing one privileged late slice.

## 7. Comparison with conserved outgoing records of this same device

The integrable escape estimate constructs the right-outgoing wave operator on the cutoff reference packet. Normalize that packet: its norm is at least 1-eta and its difference from the uncut reference is at most 2eta. Therefore

    ||psi_actual(T_c)-Omega_out psi_cut,normalized||
       <=delta_c+2eta+C_escape/(1-eta).

The usual isometric extension defines the outgoing scattering sector; no assertion that all states escape or that no embedded bound states can occur is needed. Treat its orthogonal complement as failure.

In the outgoing representation, P1_F, the memory-label projectors and 1_B(Y) commute with H_out. Their dressed right-outgoing effects commute with the full H on that scattering sector. Together with the complementary failure outcome they define a complete record POVM on the physical Hilbert space. They also commute with C_aux=P_T+H, defined on its maximal joint-spectral domain.

Comparing their statistics to the original uncut ideal record adds at most 2eta, giving the uniform bound

    delta_asymptotic_record
       =delta_c+4eta+C_escape/(1-eta).

This explicitly connects a finite prepared state/completion window to conserved outgoing record effects **for this Hamiltonian**, rather than transplanting the old step-model instrument. The discarded-outgoing-sector probability is bounded by the square of the preceding normalized-state vector bound. These are asymptotic dressed effects, not local instantaneous first-crossing projectors.

The ordinary finite flag readout and the dressed outgoing POVM are different implementations with a common reference record and bounded deviations. For record probabilities their difference is at most delta_infinity+delta_asymptotic_record. Their no-click meanings remain distinct.

## 8. Pointer timing and explicit resources

The ideal stopped-time reading is tau_hat=M_pointer*Y/k0. For the real cosine pointer packet, with c=1/3-2/pi^2 and tau_max=tau0+a/v,

    B_time=(M_pointer*pi/(2k0 b))^2
             +c b^2 tau_max^2/k0^2+a^2/v^2

bounds its ideal MSE relative to tau0. The carrier contribution uses |x0+d0|<=a; it is not omitted. Thus for every t>=T_c and tolerance A>0,

    Pr(F=0 or [F=1 and |tau_hat-tau0|>=A])
       <=min(1,delta_infinity+B_time/A^2).

This is an event-probability statement. An unbounded actual pointer moment is not inferred from trace distance.

For a concrete fixed-speed family choose lambda>=20,

    m=lambda^8, v=100, d0=1,
    a=10/lambda^2, ell=20/lambda, d=10/lambda,
    M_pointer=lambda^2, k0=lambda^2, b=10lambda,
    omega=0.1, D=1.

Then both mean velocities stay fixed (100 and 1). The carrier energy grows as 5000lambda^8, pointer energy as order lambda^2, while packet/device scales shrink. The bounds give

    delta_0=O(lambda^-1), delta_c=O(lambda^-1),
    eta=O(lambda^-6), C_escape=O(lambda^-1),
    B_time=O(lambda^-2).

Hence finite completion, all-future record accuracy and comparison to the conserved outgoing records can all be made accurate in one controlled family. No hardware realizability at arbitrarily small scales or huge masses is established.

The deterministic results file gives three finite cases. At lambda=10000, the uniform all-future record bound is below 0.00023; for tolerance 0.001 the complete not-completed-or-inaccurate-time probability is below 0.0005. The nominal elapsed time is approximately 0.0101. These are dimensionless analytical bounds evaluated in floating point, not interval certificates, PDE simulations or experimental performance. The carrier's reference energy is 5*10^35 model units; the accuracy is emphatically not obtained for free.

The finite thermal E is still a counted correlation resource, not a replenished Markov reservoir. D,M,F are prepared blanks. Pointer preparation, macroscopic readout/reset and perturbation-resistant retention are not supplied by the unitary model.

## 9. Verification and remaining direct time task

The verifier reruns the local record-channel matrix-unit checks, tests 2,010 reference-profile points for stopping/flag ordering and calibration, checks the escape-integral constant, evaluates the full resource bounds and compares their scaling. These checks do not numerically solve the physical carrier PDE. The Duhamel, Fourier-tail and Cook arguments above justify the uniform statements.

This supplies the requested finite registration-and-stop bridge with a completion flag and a controlled outgoing-record comparison. It does **not** turn the stopped-clock observable into a universal exact first-entry time, derive continuously monitored arrival trajectories, establish a macroscopic irreversible cycle, or solve gravitational refoliation.

The next direct time obligation is to compare internal clock descriptions using these completed event instruments—not sharp coordinate substitutions—and then carry the record algebra into a genuinely gravitational constraint model. The present C_aux is a relational-history constraint for specified nongravitational dynamics, not that gravitational model or the complete physical–phenomenal constitution.

**Gravitational continuation:** [The recollapsing Einstein–scalar model](RECOLLAPSING_GRAVITATIONAL_CLOCK.md) now supplies an action-derived gravitational constraint, a common quantized physical space and exact oriented representation/record transport. The present apparatus and its numerical error are not automatically a detector coupled to that cosmology; deriving its gravitational energy contribution remains required.

## Gravitational finite-reference extension

[The dust-free carrier construction](FINITE_REFERENCE_GRAVITY.md) derives an autonomous apparatus in the actual homogeneous gravitational lapse constraint, rather than C_aux=P_T+H. Its rigging Jacobian and gravitational spectral encoding are supplied explicitly. It rederives the completion/escape constants without this report's stopped pointer and includes the preparation cost; the numerical error bounds above are not transferred unchanged. The gravitational–scalar phase POVM, boundary assumptions and missing readout engine delimit that extension.
