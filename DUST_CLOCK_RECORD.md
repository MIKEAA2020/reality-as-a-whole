# A finite proper-time record operation inside a gravitational constraint

## Result and scope

A homogeneous Einstein–scalar model with negative cosmological constant can include a finite register whose measurement, copying, dephasing and completion gates occur in finite **internal proper time**. Their energy enters the same lapse constraint as the geometry. A positive relational dust-energy budget pays for the controls. The resulting complete instrument has a uniform error bound, and the recorded memory becomes exactly conserved after a finite reference time.

This is a constructive extension of [the gravitating oscillator](GRAVITATING_PROPER_TIME_CLOCK.md), **not a passive change of clock in that model**. It adds physical proper dust and changes the matter content, ordering and boundary problem. The massless scalar remains present. Dust is an ideal continuous reference field; a finite, normalizable, positive-energy clock preparation is not supplied. Neither spatially inhomogeneous Einstein constraints nor a macroscopic readout/reset engine is solved.

The gain is a finite-duration, source-accounted constrained record operation, rather than an external readout appended to gravitational scattering. It is not a general solution of the problem of time or a zero-residue constitution of experience.

## 1. Action: internal controls, not parameter-time driving

Use a unit comoving cell, flat FLRW metric, lapse N, a>0, 8 pi G=1 and hbar=1. The gravitational and massless scalar Lagrangian is

    L_gphi = -3a adot^2/N + a^3 phidot^2/(2N) - N Lambda a^3,
    Lambda<0.

Add comoving proper dust in canonical form and a finite internal register:

    L_dust = p_tau (taudot-N),
    L_reg = i z^dagger zdot - N z^dagger h(tau) z
            - lambda (z^dagger z-1).

Here z has 32 complex components. Quantization in its one-boson sector gives a 32-dimensional register, identified with five qubits. The number constraint makes a scalar energy offset a real source, not an ignorable subtraction. Hermitian h ensures unitary internal evolution. This is a smeared comoving internal apparatus, not a spatially localized detector or a derivation of its microscopic constituents.

There is **no explicit dependence on the arbitrary action parameter**. Controls depend on the dynamical dust coordinate tau. Lapse variation and the canonical transformations give

    C = p_tau - p_a^2/(12a) + p_phi^2/(2a^3)
        + Lambda a^3 + h(tau) = 0.

In particular,

    taudot = N,
    pdot_tau = -N partial_tau h

(with the register expectation in the classical amplitude formulation). The dust reference measures comoving proper time. Its momentum changes when it supplies or receives control energy. Setting p_tau constant while retaining tau-dependent controls would violate this action.

Define r=a^(3/2), p_a=(3/2)sqrt(a) p_r. Then

    C = p_tau - A + h(tau),
    A = (3/16)p_r^2 + |Lambda| r^2 - p_phi^2/(2r^2).

A is conserved because every internal control commutes with it. On the constraint,

    A = p_tau + h(tau).

Thus internal work redistributes the dust-plus-register comoving rest source. It is not work supplied from outside the gravitational model.

## 2. A declared self-adjoint gravitational sector

Choose the measure dr and Fourier-transform phi. In a momentum fiber p=p_phi, use

    A_p = (3/16)[-d_r^2 - g/r^2] + |Lambda|r^2,
    g=8p^2/3.

Restrict to a conserved scalar band |p|<=p_max<sqrt(3/32). Hardy's inequality makes the inverse-square quadratic form subcritical. Take its Friedrichs extension on r>0. Its endpoint behavior is r^(1/2+nu), where

    nu(p)=sqrt(1/4-8p^2/3)>0,
    omega_g=sqrt(3|Lambda|)/2,
    beta=8 omega_g/3.

The normalized eigenfunctions are proportional to

    f_n,p(r)=r^(nu+1/2) exp(-beta r^2/2) L_n^nu(beta r^2),
    epsilon_n(p)=omega_g (2n+1+nu),   n=0,1,... .

Substitution into the differential equation gives the spectrum; the Friedrichs boundary condition excludes the other endpoint branch. The full chosen sector is the direct integral of these fiber Hilbert spaces over the scalar band.

These are substantive model choices. No Friedrichs construction for supercritical scalar momenta is asserted. No equivalence to the earlier logarithmic-volume/KL or Morse quantization follows merely from the classical canonical transformation. Nor does an imposed self-adjoint endpoint condition establish physical singularity resolution. A globally canonical scalar-position observable within the restricted momentum band is not assumed.

For an apparatus calibration select n_min<=n<=n_min+2 and square-integrable scalar wave packets within the band. This gives an invariant gravitational code with

    A_min I <= A <= A_max I.

A fixed continuous p eigenvector is not a normalizable preparation. The code uses genuine packets. Since the controls act only on the register, neither pulse evolution nor register readout leaks out of this gravitational code. The unrestricted reduced generator -A is not being advertised as a positive matter Hamiltonian.

## 3. Constraint domain, physical norm and conserved record operators

On the gravitational sector times the register, let

    H(tau)=-A+h(tau),
    i partial_tau U(tau,0)=H(tau)U(tau,0),
    U(tau,0)=exp(i A tau) U_h(tau,0).

The compactly supported controls below are bounded. This defines unitary propagation also outside the finite calibration code. On the kinematic space L^2(R,d tau) tensor H_root, multiplication by U defines a unitary Q. Set

    C = Q p_tau Q^dagger,
    D(C)=Q D(p_tau),
    p_tau=-i partial_tau.

The differential expression is exactly p_tau-A+h(tau). The transported domain is the self-adjoint realization; a naive intersection of unbounded operator domains is not substituted for it.

Group averaging is now the unitary transport of the ordinary linear-momentum constraint. Histories have the form

    Psi(tau)=U(tau,0) psi_0,
    <Psi,Phi>_phys=<psi_0,phi_0>_root

up to one fixed rigging normalization convention. This is not a normalizable uniform probability distribution over tau. Physical histories are generalized kinematic states, with a well-defined root Hilbert space and normalized relational probabilities.

For every bounded root observable R_0,

    O_R = Q R_0 Q^dagger

strongly commutes with C: after conjugation, R_0 is constant in tau and commutes with the spectral projections of p_tau. For a hardware record R read at tau_f, choose

    R_0=U(tau_f,0)^dagger R U(tau_f,0).

If the controls have stopped and R commutes with H_free, then its dressed fiber obeys

    O_R(tau)=R,   tau>=tau_f.

Thus a final bare memory projection is the late-time representative of a genuine Dirac observable, **at finite time**, not only in an asymptotic scattering limit. Earlier in the operation the dressed representative is generally not the bare projection.

## 4. Four finite pulses

Use qubits S (system), D (detector), M (memory), E (dephasing ancilla), F (completion flag). Initially D,M,F are |0>; E is I/2. S may be entangled with any additional reference, including the gravitational state. Let P_1=(I-Z)/2 and

    h(tau)=E_b I + omega X_S + sum_j g_j(tau) B_j,
    E_b>=omega>0,

    B_1=P_1,S tensor (I-X_D)/2,
    B_2=P_1,D tensor (I-X_M)/2,
    B_3=P_1,M tensor (I-X_E)/2,
    B_4=(I-X_F)/2.

Each B_j is a positive projector. Four nonoverlapping pulses have width ell, gap ell/4 and starts s_j=(j-1)5ell/4:

    g_j(tau)=(2pi/ell) sin^2[pi(tau-s_j)/ell]

inside their pulse window, and zero outside. They are continuously differentiable at their endpoints. Every pulse has area pi and finite peak 2pi/ell. Without the S Hamiltonian, the first three are exact controlled-X gates and the fourth is X_F. The total duration is

    tau_f=4ell+3ell/4=19ell/4.

The completion flag certifies completion of this calibrated schedule, not error-free measurement or validity of the model's assumptions.

## 5. The actual first-pulse instrument and a uniform error theorem

The free term omega X_S does not commute with B_1. It cannot simply be omitted. Remove the common phase from E_b. In the X_D eigenbasis the exact first-pulse propagator has blocks

    U_+ = exp(-i omega ell X_S),
    U_- = T exp[-i integral_0^ell
                    (omega X_S+g_1(tau)P_1,S) d tau].

Starting D in |0>, the actual detector Kraus operators are

    A_0=(U_++U_-)/2,
    A_1=(U_+-U_-)/2.

Unitarity of both blocks proves

    sum_d A_d^dagger A_d=I.

All outcomes are retained. In the zero-free-Hamiltonian comparison U_+=I, U_-=Z, so A_d=P_d. Duhamel's inequality compares the actual S,D unitary with the pulse-only controlled-X:

    ||U_SD-CNOT_SD|| <= integral_0^ell ||omega X_S|| d tau
                     = omega ell = delta.

For unitary channels, half the diamond distance is at most their operator-norm difference. Initialization, later common gates, dephasing and outcome readout are completely positive trace-preserving postprocessing. Therefore the **complete classical-output instrument**, including its conditional S states, satisfies

    (1/2)||I_actual-I_ideal||_diamond <= min(1,omega ell).

The comparison instrument includes the exact free S rotation from ell to tau_f. It is not an assertion that S remains frozen for the whole experiment. Geometry propagation is common to both channels, so the bound also holds for arbitrary initial geometry–S/reference entanglement within the calibrated space.

The bound depends on the first pulse width, not on 19ell/4: the free S Hamiltonian commutes with all later gates. No product of unproven individual pulse errors is used.

## 6. Classical memory and finite completion

Let W=exp[-i omega (tau_f-ell)X_S]. After the D-to-M copy and M-to-E gate, tracing E removes exactly the off-diagonal M terms: the off-diagonal factor is Tr[(I/2)X_E]=0. The final reduced state has the form

    sum_d W A_d rho A_d^dagger W^dagger
          tensor |d><d|_D tensor |d><d|_M tensor |1><1|_F,

with the common gravitational unitary and any reference systems understood. This formula defines the complete recorded instrument; its outcome probabilities sum to one. Memory and detector agree exactly, although their measurement of S has the bounded nonzero error above.

The environment is finite and merely stores correlations. Its being traced is not a claim of permanent objective collapse. With the stated uncoupled post-protocol Hamiltonian, however,

    [Z_M,H_free]=[Z_F,H_free]=0,
    Pr(F=0 | tau>=tau_f)=0.

Memory and flag are exactly conserved thereafter in this self-adjoint ideal model, and their projective readings are nondemolition. This algebraic statement does not establish robustness under noise, macroscopic hardware, or a physically correct extension through a cosmological singularity. The ancillary mixed state and initialized bits are resources; reset and reuse are not supplied.

## 7. Positive relational dust energy and gravitational backreaction

At most one control pulse is active. Positivity of the B_j and E_b>=omega give

    0 <= h(tau) <= h_max I,
    h_max=E_b+omega+2pi/ell.

Choose the gravitational code so A_min>h_max. At each reference reading, the dust energy on the constraint is the relational operator

    P_tau(tau)=A-h(tau) >= (A_min-h_max) I >0.

In the physical root representation conjugate this expression by U(tau,0); the same bound holds. There is also the finite upper bound A_max-(E_b-omega).

**This is positivity of the relational dust energy on an invariant calibrated code. It is not a claim that bare kinematic p_tau has positive spectral support.** Bare p_tau does not commute with the time-dependent constraint. The globally canonical continuous reference representation remains ideal; no normalizable finite clock packet with all these properties has been constructed.

For solutions, the exact energy balance is

    d< h >/d tau = <partial_tau h>,
    d< P_tau >/d tau = -<partial_tau h>,
    d< A >/d tau = 0.

The controls' work is paid by the dust, including quantum internal energy changes. For example, S initially |+X> has free energy omega. An ideal Z measurement leaves zero mean X; the corresponding increase omega in dust energy balances the decrease of internal energy. The verifier evaluates the actual Kraus channel and obtains approximately 0.1 for omega=0.1, without discarding any measurement outcome. This is not a thermal reset calculation or a Landauer minimum.

Fixed A makes the geometry independent of *redistribution* between dust and register. That is not absence of gravitation. Changing internal energy at fixed dust energy changes A and hence the geometric solution. Classically, at maximum volume V=a^3 with p_r=0,

    |Lambda| V^2 - A V - p_phi^2/2 = 0,
    V_max=[A+sqrt(A^2+2|Lambda|p_phi^2)]/(2|Lambda|).

In the p_phi=0, A>0 control this reduces to V_max=A/|Lambda|. Raising detector energy by Delta E at fixed dust energy raises V_max by Delta E/|Lambda|. The scalar remains in the general action and in the quantum gravitational spectrum.

## 8. A finite sufficient resource family

Set Lambda=-0.75, p_max=0.1, omega=0.1, E_b=1 and ell=0.02/q for q=1,10,100. Let nu_min=nu(p_max), omega_g=0.75 and choose

    n_min=ceil(((h_max+1)/omega_g-1-nu_min)/2).

Three adjacent levels then guarantee strictly positive relational dust energy throughout every pulse. Scalar momenta are square-integrable packets in the band, not fixed eigenvectors.

| q | Proper duration tau_f | Instrument half-diamond bound | Peak control energy | n_min | Dust energy lower bound |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.095 | 0.002 | 314.1593 | 211 | 2.34517 |
| 10 | 0.0095 | 0.0002 | 3141.5927 | 2096 | 2.41178 |
| 100 | 0.00095 | 0.00002 | 31415.9265 | 20945 | 1.57790 |

For target error eta, choosing ell=eta/omega gives a sufficient peak control energy 2pi omega/eta and a corresponding gravitational/dust code budget. Each nonzero target has finite resources. The zero-error limit is not free: this family needs divergent peak energy and clock-control gradients. These are **sufficient construction costs**, not a universal resource lower bound or an empirical apparatus calibration.

## 9. Verification and remaining direct time work

Run:

    python verification/dust_clock_record.py
    python -m verification.dust_clock_record

The standard-library verifier writes [dust_clock_record.json](verification/dust_clock_record.json). It checks 64 radial eigenmode differential-equation cases; three finite pulse/budget designs; actual Kraus completeness, block-unitary error and classical-input probabilities; all four system matrix units through the full register copies/flag and environment trace; 256-versus-512-panel midpoint convergence; the exact finite flag flip; actual S-to-dust mean energy transfer; and zero-scalar-momentum classical total-source constraints. The analytic arguments above, not the grid, establish self-adjointness, strong constraint commutation, the uniform instrument bound and memory conservation. Floating-point checks are not interval certificates, continuum proofs or observed cosmological data.

**Closed within the declared model:** internal finite-duration control, complete approximate measurement, exact later copying/dephasing/flagging, finite-time conserved record effects, and a positive relational dust-energy budget in the same lapse constraint.

**Still open:** a finite physical reference replacing ideal dust while retaining source accounting and a controlled instrument; a microscopic readout/reset mechanism; derivation or observational justification of the endpoint/domain choices; local gravitational constraints and full refoliation; and the independently missing physical–phenomenal constitution. A passive equivalence to the earlier scalar-clock quantization has not been proved.

A [dust-free finite-carrier construction](FINITE_REFERENCE_GRAVITY.md) now pursues that replacement: an autonomous quadratic carrier supplies the controls, with a gravitational spectral window, controlled correlated preparation and noncompletion bounds. It removes tau from the action, not merely from the notation. Its nonorthogonal gravitational–scalar phase reference and missing encoding/readout engines remain explicit; it does not turn the ideal dust model above into an equivalent finite clock or inherit its exact finite-time memory conservation.
