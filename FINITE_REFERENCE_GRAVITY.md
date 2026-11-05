# A finite carrier clock without dust: gravitational spectral matching and completed records

## 1. Constructive result

The [proper-dust record model](DUST_CLOCK_RECORD.md) supplied a finite register schedule but retained an ideal continuous reference field. Here **the dust field is removed from the action**. A normalizable, finite-energy internal carrier moves through four fixed gate regions. Its kinetic energy, the register energy and every control interaction enter the gravitational lapse constraint.

The nontrivial constraint issue is solved explicitly: the carrier/register preparation must fit a gravitational spectral window. A controlled spectral projection followed by polar normalization supplies an **isometric preparation for arbitrary system inputs**, rather than state-dependent postselection. This preparation is not the unchanged product used in the nongravitational model.

For the resulting physical states there is a finite-epoch complete record POVM, a uniform late single-interrogation error bound, and a conserved, energy-compatible outgoing record instrument including failure. The error bounds are derived anew for this Hamiltonian and preparation. No dust-clock error number is imported.

**Scope:** homogeneous Einstein–scalar gravity, a declared radial ordering/Friedrichs domain, engineered comoving internal mechanics and ideal mathematical record extraction. A finite-band gravitational–scalar phase POVM indexes relational epochs; it is nonorthogonal, not a canonical perfect clock. No microscopic implementation of that phase readout, macroscopic reset engine, general refoliation or zero-residue phenomenal constitution is claimed.

## 2. One autonomous lapse-coupled action

Retain the flat FLRW Einstein–scalar Lagrangian and negative Lambda of the previous construction. Replace the dust and tau-dependent apparatus by an internal carrier X,P and register z:

    L = L_gphi + P Xdot + i z^dagger zdot
        - N [P^2/(2m) + z^dagger h(X) z]
        - lambda (z^dagger z-1),

    h(X)=E_b I + omega X_S + v sum_j kappa_j(X) B_j.

There are five qubits S,D,M,E,F. The positive projectors B_j are the S-to-D, D-to-M, M-to-E controlled-copy generators and flag-flip generator defined in the dust report. The register one-boson sector has dimension 32. A purification of the mixed E preparation can be included as an untouched zero-energy ancillary degree of freedom.

X is an **internal apparatus coordinate**, not the spatial position of a freely moving cosmological particle. Its Hamiltonian is independent of a because the apparatus is smeared comovingly as before. A localized spacetime particle would require additional scale-factor dependence and inhomogeneous constraints; it is not described by this action.

Four spatial profiles of width ell and gap d are

    kappa_j(x)=(2pi/ell) sin^2[pi(x-x_j)/ell],
    x_j=(j-1)(ell+d),

inside each region and zero outside. Each has area pi. The device ends at L=4ell+3d. There is no lapse-parameter switching and no tau field.

With r=a^(3/2), the constraint is

    C=H_app-A,
    H_app=P^2/(2m)+h(X),
    A=(3/16)p_r^2+|Lambda|r^2-p_phi^2/(2r^2).

Since E_b>=omega and all B_j are positive,

    H_app >= (E_b-omega) I >=0.

H_app is self-adjoint on H^2(R_X) tensor C^32, with a bounded matrix potential. A is the declared gravitational operator, not an externally prescribed energy parameter. The joint constraint is defined by their strongly commuting spectral measures. There is no substitution of a linear vP clock for the physical positive quadratic Hamiltonian.

## 3. The gravitational spectrum determines the admissible apparatus energies

Use the same radial measure and Friedrichs extension as in the dust construction, but choose a positive scalar band

    0<p_lo<=p_phi<=p_hi<sqrt(3/32).

For a fixed radial level n,

    epsilon_n(p)=omega_g[2n+1+nu(p)],
    omega_g=sqrt(3|Lambda|)/2,
    nu(p)=sqrt(1/4-8p^2/3).

This is strictly decreasing in p, with

    J(p)=|d epsilon_n/dp|=8 omega_g p/(3nu)>0.

Let I=[epsilon_n(p_hi),epsilon_n(p_lo)]. Restricting to a positive band avoids a two-branch degeneracy and a zero Jacobian. The scalar is retained as matter; its conjugate position is not assumed to be a globally canonical observable within this band.

For a test section f(p,E) in the apparatus spectral representation, group averaging gives, up to one fixed normalization,

    ||eta f||_phys^2
      = integral_I d mu_app(E)
          ||f(p(E),E)||^2 / J(p(E)).

Here d mu_app denotes the apparatus spectral measure with its multiplicities, not necessarily pure Lebesgue measure. The root amplitude

    psi(E)=f(p(E),E)/sqrt(J(p(E)))

therefore identifies the physical Hilbert space with

    H_phys,n,I = 1_I(H_app) H_app_space.

For the absolutely continuous apparatus sector the integral is the usual dE channel integral. If point-spectrum sectors occur, the same spectral-calculus formula gives their corresponding atomic contributions. They are not silently deleted; the outgoing instrument below includes their complement as failure.

This is the central compatibility condition: **an arbitrary nongravitational clock packet is not already a physical state of this gravitational code**. Total apparatus energy must lie in I, with the correct rigging Jacobian. Treating gravitational and apparatus energies as independently prepared would miss the constraint.

The ordering, restricted scalar band and boundary condition remain declared inputs. This is not a proof of equivalence with the older scalar-time KL/Morse quantizations or of physical singularity resolution.

## 4. Constraint-compatible preparation without input-dependent success selection

Begin with a comparison isometry V from an arbitrary S input (also entangled with an untouched reference). Prepare D,M,F in |0>, E in I/2, and the carrier in

    exp(i p0 x) f(x+d0),   p0=mv,

where f is the normalized real cos-squared envelope supported on [-a,a], with d0>a. Its derivative norms are

    f_1=||f'||=pi/(sqrt(3)a),
    f_2=||f''||=pi^2/(sqrt(3)a^2).

Purify E when discussing isometries. All initial resources other than S are fixed independently of the input.

The initial support lies strictly left of every spatial gate, so the potential terms annihilate it. With

    E_c=E_b+p0^2/(2m),
    sigma=v f_1+f_2/(2m)+omega,

one has the uniform operator bound

    ||(H_app-E_c)V||<=sigma.

Choose I=[E_c-W,E_c+W], and let Pi=1_I(H_app). The spectral theorem gives

    ||(I-Pi)V||<=epsilon=sigma/W.

For epsilon<1, define G=V^dagger Pi V and

    V_I=Pi V G^(-1/2).

Then

    V_I^dagger V_I=I,
    ||V_I-V||^2 <= 2[1-sqrt(1-epsilon^2)],
    ||V_I-V|| <= 2epsilon =: alpha.

The equality follows from V^dagger V_I=sqrt(G); the bound follows from G>=(1-epsilon^2)I. The normalization is **an operator acting on the encoded input**, not division by a state-dependent detection probability. V_I defines a linear deterministic encoding of all input density operators and reference entanglement.

The energy centering is a calibration assumption, not a free infinite precision claim: an offset delta_cal is covered by replacing sigma with sigma+|delta_cal|. Thus the preparation and subsequent vector bounds increase by at most 2|delta_cal|/W. For example, allowing 2|delta_cal|/W<=10^(-6) adds at most 10^(-6) to each listed vector/channel bound, with the probability bounds then squared accordingly. The table uses the exactly specified centering formulas; rounded floating metadata is not an independent high-precision calibration certificate.

This supplies admissible physical initial states through the rigging identification. They are normalizable in the physical norm, have bounded total energy in I, and contain a finite normalizable carrier. They are not exact carrier/register product states, do not have exactly compact position support, and need not have strictly positive momentum. The alpha comparison cost accounts for these changes. The initial probability outside the comparison localization interval is at most alpha^2, since V is exactly supported there. A sharp spectral projection can nevertheless generate long position tails; finite RMS position spread is not proved by this norm estimate. No inexpensive preparation Hamiltonian for V_I is claimed: a physical source for this encoding is a remaining resource obligation.

## 5. Relational epochs without reintroducing canonical dust time

In the gravitational–scalar band, use energy-normalized eigenvectors |E>_g. The finite-band phase POVM is

    |t>_g = integral_I dE exp(iEt)|E>_g,
    F_g(dt)=|t><t| dt/(2pi),
    integral_R F_g(dt)=I_g.

Its normalized overlaps are

    <t|t'>/(2W)=exp[i E_c(t'-t)] sinc[W(t'-t)].

Nearby epochs are not orthogonal. This is not a self-adjoint canonical time operator conjugate to a semibounded energy, nor an infinitely resolving physical timestamp. In particular, a continuous outcome label is not evidence of arbitrarily distinguishable clock states.

Taking the phase representative of a constrained history gives the relational root state

    psi(t)=exp(-i H_app t) psi(0).

The lapse sign follows from the gravitational generator -A. The reference involves the gravitational–scalar spectral phase, not the volume r alone; it is not a claim that volume is a global clock through recollapse. No new ideal linear-momentum matter field has been inserted.

As in group averaging generally, the constrained history is not a normalizable kinematic vector with a uniform probability prior on t. The physical norm is the root norm in section 3. The phase POVM specifies the relational representation; its full dynamical preparation/readout apparatus and unconditional clock-sampling experiment are not provided. The carrier's finite spread and the phase POVM's nonorthogonality remain distinct facts.

## 6. Finite completion for the same finite carrier

The following estimate specializes and rederives the [autonomous finite-completion method](FINITE_COMPLETION_CLOCK.md) for the present Hamiltonian. There is **no stopped pointer** and no old pointer-energy term to transplant.

Boost by p0. The physical carrier generator is vP+P^2/(2m), plus the fixed spatial potential. For a proof-only transport comparison use vP. Include omega X_S until the earliest reference entry

    t_pre=(d0-a)/v.

Omit it during the active interval and restore it after

    T_0=(L+d0+2a)/v.

Only the comparison omits a term; the physical Hamiltonian never switches. The ideal record is the Z measurement of the freely evolved S input at t_pre. Its calibration is not a sharp arrival-time observable.

All reference packet components have passed every gate by T_0. Every spatial pulse then has time area pi, so D copies S, M copies D, E dephases M after it is traced, and F flips to 1. The carrier factorizes again from this ideal internal record. The later free S rotation is retained in the comparison.

Set

    k=2pi/ell,   k'=2pi^2/ell^2,
    C_in=f_2+2k f_1+k'+k^2.

Differentiating the transport propagator twice gives second-derivative norm at most f_2 on approach and C_in during the gates. Thus

    delta_0=t_pre f_2/(2m)
            +(T_0-t_pre)[C_in/(2m)+omega].

For clearance D>2a, continue to

    T_c=T_0+(D-2a)/v,
    delta_c=delta_0+(D-2a) f_2/(2mv).

The reference carrier is centered at L+D. Adding the spectral-encoding cost gives full purified state error at most alpha+delta_c. Reflection, spreading and noncommuting system-energy exchange are included in this Duhamel estimate, not removed by a classical trajectory assumption.

## 7. Uniform future estimate and complete records

After T_c compare with the physical quadratic outgoing Hamiltonian

    H_out=P^2/(2m)+E_b+omega X_S.

The remaining interaction W_app=H_app-H_out is compactly supported on [0,L] and bounded by W_max=vk. The record qubits are stationary under H_out.

For completeness the constants of an integrable escape bound are:

    L_0=sqrt(pi/a) sqrt(1+a^2 f_1^2),
    L_1=sqrt(pi/a) sqrt(a^2+a^2(1+a f_1)^2),
    L_2=sqrt(pi/a) sqrt(a^4+a^2(2a+a^2 f_1)^2),
    c_1=2pi/p0, c_2=8pi^2/p0^2,
    H_0=L_0, H_1=L_1+c_1 L_0,
    H_2=L_2+2c_1 L_1+c_2 L_0,
    p_min=p0/4, v_min=p_min/m,
    A_tail=(H_2+3H_1/p_min+3H_0/p_min^2)/sqrt(2pi),
    eta=2 f_1/p0,
    C_escape=2vk A_tail/[sqrt(3)v_min sqrt(D)].

A smooth momentum cutoff zero below p0/4 and one above p0/2 removes norm at most eta. Weighted Cauchy–Schwarz gives the L_j Fourier bounds; two integrations by parts in the free outgoing phase yield a left-tail norm at most A_tail/[sqrt(3)(D+v_min s)^(3/2)]. Its interaction norm is integrable in s. The same derivation is detailed in the finite-completion report; here no pointer-momentum shift occurs.

For every s>=0 and arbitrary entangled S/reference input,

    ||exp[-i H_app(T_c+s)]V_I
       - exp[-i H_out s]V_ref(T_c)||
      <= alpha+delta_c+2eta+C_escape =: Delta.

Consequently the extracted **complete register-output instrument**, including F=0, has half-diamond error at most min(1,Delta) relative to the ideal completed instrument. In particular,

    Pr(F=0) <= min(1,Delta^2),
    Pr(D!=M) <= min(1,Delta^2),   t>=T_c.

The first probability includes delayed, reflected and imperfectly registered amplitude; no successful-flag postselection is used to normalize away these alternatives. The error estimate concerns one interrogation after unmonitored evolution, at any later relational epoch. It is not a continuous first-click distribution or a joint repeated-read guarantee.

### Finite-epoch POVM versus a source-preserving instrument

At any finite epoch, the actual local flag/memory projectors P_r define the normalized physical-root effects

    E_r(t)=Pi exp(iH_app t) P_r exp(-iH_app t) Pi,
    sum_r E_r(t)=I_phys.

Here r includes F=0 and all F=1 memory outcomes. These effects supply a complete POVM for the record statistics just bounded. Their positive square roots also define a mathematical CP instrument on the physical space.

One must **not** identify that square-root instrument with a literal instantaneous projection of the bare hardware followed by an unchanged geometry. Bare P_r need not preserve the spectral band or commute with H_app. The finite-epoch extracted S/register channel and its error bound specify output statistics/states as an operational comparison; a closed readout interaction implementing that extraction with its own source remains unsupplied.

A stronger, source-preserving outgoing instrument is available without this identification. On the positive-momentum outgoing space define

    Omega_out=strong-limit_(s->infinity) exp(iH_app s) exp(-iH_out s).

The integrable Cook estimate constructs this isometry first on a dense set of smooth right-moving packets, then by extension. It intertwines the two Hamiltonians. No assertion of asymptotic completeness or absence of bound sectors is required.

The free projectors for F and M commute with H_out and positive momentum. Dress them by Omega_out. Their sum is the outgoing-sector projector; add its orthogonal complement as a separate failure outcome. These projectors commute with H_app and hence preserve Pi. On the joint kinematic space they commute strongly with C=H_app-A, so their restrictions define a complete physical record instrument by projection on each outcome, including failure. Unlike bare finite-time readout, this instrument is energy-compatible within the chosen gravitational code.

Comparison with the normalized cutoff outgoing packet gives

    Delta_out=alpha+delta_c+4eta+C_escape/(1-eta),

an outgoing record-channel error bound. The probability outside the right-outgoing sector is at most

    [alpha+delta_c+2eta+C_escape/(1-eta)]^2.

For conditional S-output comparisons, use the outgoing representation Omega_out^dagger on success and an explicit orthogonal failure output, not a trace of the bare S inside an interaction region.

These are conserved asymptotic record effects connected by a quantitative estimate to a finite completion window. They are not exact finite-time bare conserved records as in the ideal dust model. Finite reference resources replace that exactness by controlled noncompletion and recrossing errors.

## 8. One fixed gravitational model and three finite designs

Take v=100, d0=1, omega=0.1, D=1 and

    m=q^8, a=10/q^2, ell=20/q, d=10/q,
    q=100,1000,10000.

Use one fixed gravitational model:

    omega_g=10^28, Lambda=-4 omega_g^2/3,
    p_lo=0.05, p_hi=0.25.

Let nu_mid=[nu(p_lo)+nu(p_hi)]/2 and w_nu=[nu(p_lo)-nu(p_hi)]/2. Choose

    n=max(0,ceil([(mv^2/2+omega)/omega_g-1-nu_mid]/2)),
    E_c=omega_g(2n+1+nu_mid),
    E_b=E_c-mv^2/2,
    W=omega_g w_nu.

Then E_b>=omega and I is exactly the gravitational window. The large rest source is retained, not subtracted. It is a real resource in the constraint. Every design has finite energy and finite mass; the huge numbers and negative cosmological constant make this a formal conditional construction, **not a realistic cosmological parameter fit** or a universal optimality result.

| q | Radial level n | T_c | Preparation norm cost alpha | Uniform record error Delta | Pr(F=0) bound |
|---:|---:|---:|---:|---:|---:|
| 100 | 0 | 0.031 | 3.55e-22 | 0.013896 | 1.931e-4 |
| 1000 | 0 | 0.0211 | 3.55e-20 | 0.00023796 | 5.663e-8 |
| 10000 | 25000000 | 0.02011 | 3.55e-18 | 0.000012280 | 1.508e-10 |

The first design does not meet a one-percent uniform error target: the Cook escape bound, not the first-gate approximation, dominates. The table retains that actual bound rather than advertising a stronger one. The family establishes these three resource witnesses; no arbitrarily accurate limit at fixed gravitational bandwidth is claimed. For still larger q the finite-band preparation cost must be reconsidered.

## 9. Verification, gain and next obligation

Run:

    python verification/finite_reference_gravity.py
    python -m verification.finite_reference_gravity

The verifier writes [finite_reference_gravity.json](verification/finite_reference_gravity.json). It checks three source/spectral/error designs, 117 scaled spectrum-inversion/Jacobian cases, five polar-isometry inequalities, four inherited local record matrix units and explicit finite-band phase overlaps. Scaled energy coordinates avoid subtracting nearby enormous absolute energies in the inverse-spectrum checks. The rigging construction and uniform estimates are analytic statements above; floating evaluations are consistency checks, not interval proofs or numerical solutions of a gravitational PDE.

**What changed:** an ideal dust field no longer drives the controls. A finite normalizable quadratic carrier supplies the motion and energy. The gravitational constraint is enforced through spectral matching and a controlled, input-linear encoding. Finite records and a conserved outgoing instrument retain failure, with explicit bounds connecting them.

**What remains:** a dynamical preparation of the constrained encoding and a source-accounted finite readout of the gravitational–scalar phase reference; a readout/reset engine for the record; physical justification of the boundary/domain choices; localized apparatus and the inhomogeneous constraint algebra; and the independently missing phenomenal constitution. The result does not turn a nonorthogonal phase POVM into a perfect clock or solve general quantum gravity.

The next direct time task is an operational two-reference comparison: replace sharp phase-indexed interrogation by a finite-width, internally generated reference event, derive its complete instrument and quantify the extra timing/control error without assuming an unphysical uniform prior over epochs.
