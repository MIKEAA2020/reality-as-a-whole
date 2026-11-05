# An energy-exchanging physical clock: complete instrument and coherence budget

## 1. Constructive advance

The [finite-mass detector](HAMILTONIAN_CLOCK_DETECTOR.md) had degenerate free internal levels. We now remove that restriction: the system Hamiltonian **does not commute with the measured observable**, transitions change its energy, and the clock recoils.

We obtain an exact coupled-channel scattering instrument, a necessary energy-coherence bound, and a sufficient uniform approximation bound for the **full outgoing quantum state**, hence also for the instrument after pointer/direction readout. A sharper bound controls the pointer event alone. Full-output errors use trace distance (one half of the trace norm), uniformly also with an entangled reference, not elapsed-time estimation variance.

The new resource distinction matters: **narrow relative velocity spread and adequate absolute energy coherence are different requirements**. Making the clock momentum band arbitrarily narrow can improve velocity control while making the intended noncommuting measurement impossible to distinguish better than chance under the specified readout.

This is a concrete conservation-law measurement construction, related to standard Wigner–Araki–Yanase resource issues, not a claim that all internal clocks are impossible or a new general solution of gravity.

Code: [energy_exchange_clock.py](verification/energy_exchange_clock.py). [Results](verification/energy_exchange_clock.json). The formulas provide the model bounds; floating-point matching and quadrature are witnesses, not interval-certified evaluations.

## 2. Hamiltonian and anchored reference event

Use hbar=1 and

    H=P^2/(2m) + H_S + g 1_[-L/2,L/2](X) B,
    H_S=omega X_S,  B=P1_Z tensor Y_D,
    omega>0, g>0, P1_Z=|1_Z><1_Z|.

The detector's free Hamiltonian remains zero. H is self-adjoint on H2(R) tensor C4 and bounded below by -omega-g. The compact spatial interaction supplies the pulse; no externally scheduled change of coupling is assumed. The commutator [H_S,gB] has norm omega*g, not zero.

The incoming preparation is a **product** of an arbitrary system state, a ready pointer |0>_D, and the real cosine momentum packet f(p) from the previous model, supported in [p0-Delta,p0+Delta]. Its free reference packet is focused at X=0 at reference epoch T=0. The ideal comparison is the Z measurement at that same reference epoch, centered on the detector, with

    theta=gmL/p0=pi/2,  U=exp(-i theta B).

This anchoring avoids comparing an entrance-time observable with a different midpoint-time observable. It does not define a sharp quantum arrival time.

In the X_S energy basis,

    H_S=omega Z,  epsilon_+=omega, epsilon_-=-omega,
    P1_Z=(I-X)/2.

At fixed total energy E the free momenta are

    k_s(E)=sqrt(2m(E-epsilon_s)).

A transition s->t transfers epsilon_t-epsilon_s=+/-2omega to the system and the opposite amount to clock kinetic energy. We keep the unequal momenta and their velocity factors.

Let K_min=(p0-Delta)^2/(2m), K_max=(p0+Delta)^2/(2m). The entire prepared total-energy range is

    E_min=K_min-omega, E_max=K_max+omega.

Assume E_min>omega+g. Every exterior and interior channel is then propagating. Bound states remain in H but not in the incoming scattering preparation. Closed/evanescent channels are not silently covered by this open-channel bound.

## 3. Exact matrix scattering, not scalar substitution

Y_D is conserved. In each y=+1,-1 sector the interior system matrix is

    V_y=omega Z + yg(I-X)/2.

Its eigenvalues and projectors are

    lambda_(y,sigma)=yg/2 + sigma r,  r=sqrt(omega^2+g^2/4),
    Pi_(y,sigma)=[I+sigma(omega Z-ygX/2)/r]/2.

Define kappa_sigma=sqrt(2m(E-lambda_(y,sigma))) and

    C_y=sum_sigma cos(kappa_sigma L) Pi_sigma,
    D_y=sum_sigma sin(kappa_sigma L)/kappa_sigma Pi_sigma,
    F_y=-sum_sigma kappa_sigma sin(kappa_sigma L) Pi_sigma.

Then the exact propagation of (psi,psi') across the region is

    [[C_y,D_y],[F_y,C_y]].

Let K=diag(k_+,k_-). Outside waves are normalized with sqrt(m) K^(-1/2), so their current is incoming norm squared minus reflected norm squared. The common sqrt(m) cancels from matching. Put

    U0=C_y K^(-1/2)+i D_y K^(1/2),
    U1=C_y K^(-1/2)-i D_y K^(1/2),
    W0=F_y K^(-1/2)+i C_y K^(1/2),
    W1=F_y K^(-1/2)-i C_y K^(1/2).

For a region temporarily placed at [0,L],

    R_y=(W1-iK U1)^(-1)(iK U0-W0),
    T_y=exp(-iKL) K^(1/2)(U0+U1 R_y).

Centering the region multiplies these by the appropriate channel-dependent phases:

    T_y -> exp(iKL/2) T_y exp(-iKL/2),
    R_y -> exp(-iKL/2) R_y exp(-iKL/2).

Current conservation gives T_y* T_y+R_y* R_y=I, including off-diagonal column orthogonality. The verifier independently solves the four boundary equations and checks this matrix identity, the free-coupling limit, and the previous degenerate scalar model. Equal momentum amplitudes without the K^(-1/2) factors would not represent the correct probabilities.

Auxiliary-time constrained histories and positive rigging work as in the previous report with this new self-adjoint H: C=P_T+H, eta(f)=integral exp(iHT)f(T)dT. Stationary position solutions and time evolution are descriptions of the same Hamiltonian; no new time-domain grid simulation is claimed.

## 4. Product preparation and the complete physical instrument

At fixed E the four pointer/direction matrices are

    A_T0=(T_++T_-)/2,  A_T1=i(T_+-T_-)/2,
    A_R0=(R_++R_-)/2,  A_R1=i(R_+-R_-)/2.

Their effects sum to I. But a common total-energy envelope is **not** an initially uncorrelated clock for arbitrary system inputs. The actual product preparation has the diagonal energy-space embedding

    F_s(E)=sqrt(m/k_s(E)) f(k_s(E)),
    F(E)=diag(F_+,F_-),  integral F(E)* F(E)dE=I.

The Jacobian is essential. To reconstruct the outgoing physical momentum state define the unitary change of variables

    (W_d a)_s(p)=sqrt(p/m) a_s(p^2/(2m)+epsilon_s),  p>0,

with d specifying right-going or left-going momentum. The four instrument operators are

    (mathcal K_(d,j) psi)=W_d [E -> A_(d,j)(E) F(E) psi].

They map the input system to outgoing **clock plus system**. Their effects sum to I, and their completely positive maps are mathcal K rho mathcal K*. Reflection and the pointer are explicit outcomes. Clock tracing, if desired, occurs in physical momentum space after W_d.

**Do not trace the total-energy label as though it were the clock alone.** Different system energies associate the same clock momentum with different total E. An incoherent integral over E would in general give the wrong system post-state. Pointer probabilities can be integrated over E because the pointer event is energy preserving; a complete outgoing state must retain E,E' coherences.

A concrete check: in the disjoint-band case below, for an initial + energy eigenstate the physical clock momenta associated with the two outgoing system energies have disjoint support. The unnormalized reduced-system T1 output has off-diagonal element exactly zero. Incorrectly tracing the energy-frame label instead gives approximately -0.25013+0.01059i. This is a change of subsystem, not a small numerical discrepancy.

## 5. Necessary coherence: a clock that cannot distinguish the intended alternatives

Let E_click be the incoming-system effect for pointer 1, retaining both exit directions. At each E,

    M(E)=A_T1* A_T1+A_R1* A_R1,  0<=M(E)<=I,
    E_click=integral F(E)* M(E) F(E)dE.

For a two-dimensional positive contraction, |M_+-|<=1/2. Define the overlap visibility

    V=integral |F_+(E) F_-(E)|dE,  0<=V<=1.

Since the ideal P1_Z has off-diagonal magnitude 1/2,

    ||E_click-P1_Z|| >= (1-V)/2.

The operator norm is the worst discrepancy of that event probability over initial system states. This bound does not depend on tuning g or L. Additional clocks or an external energetic phase reference would change the resource assumptions.

If

    2omega >= K_max-K_min = 2p0 Delta/m,

the incoming energy bands do not overlap, V=0, and the worst event error is at least 1/2. The pointer has identical probabilities for the two Z eigenstates, which have equal populations in the energy basis. This is an exact statement, not a quadrature significance claim. It holds even though each incoming momentum is positive and its relative spread can be very small.

This is why the zero-free-Hamiltonian approximation cannot simply be carried forward after adding H_S: velocity accuracy alone is not the relevant clock resource. Energy spread alone is not sufficient for arbitrary mixed preparations either; the specified packet's controlled phases are part of its coherence resource.

## 6. A sufficient uniform bound, including full quantum outputs

Here is a conservative analytic bound, not a grid-fitted error bar. All matrix norms are operator norms. Set

    h=omega+g, q_min=sqrt(2m E_min), q_max=sqrt(2m E_max),
    k_min=sqrt(2m(E_min-h)),
    b=sqrt((E_min+h)/(E_min-h)),
    rho=(b-1)/(b+1),
    eta=mg/(2 k_min^2)+sqrt(b) rho.

### Interfaces, reflection and internal evolution

At one interface between positive wavenumber matrices K0,K1, let Z=K0^(-1/2) K1 K0^(-1/2). The flux reflection is (I+Z)^(-1)(I-Z), hence norm at most rho. Transmission is K1^(1/2) K0^(-1/2)(I+R), a contraction. The square-root Sylvester identity gives ||K1-K0||<=mg/k_min and bounds its deviation from I by eta. The reverse interface has the same bounds.

Interior propagation exp(iK1 L) is unitary. Multiple internal reflections have round-trip norm at most rho^2. The Neumann sum therefore gives

    epsilon_interfaces=2eta+rho^2/(1-rho^2),
    R_max=min(1,[2rho/(1-rho^2)]^2).

Comparing the no-reflection propagation with its first-order matrix phase adds

    epsilon_curv=L m^2[(omega+g)^2+omega^2]
                   /[2 q_min^3(1-h/E_min)^(3/2)].

This follows from spectral Taylor remainders for K(V)=sqrt(2m(EI-V)), not from commuting H_S with B. The leading centered product is

    exp(iH_S tau/2) exp(-i(H_S+gB)tau) exp(iH_S tau/2),
    tau=mL/sqrt(2mE).

Duhamel's inequality bounds its distance from exp(-igB tau) by 2omega tau. Thus let

    epsilon_free=2omega mL/q_min,
    epsilon_angle=gmL max(|1/q_min-1/p0|,|1/q_max-1/p0|),
    epsilon_T=epsilon_interfaces+epsilon_curv+epsilon_free+epsilon_angle,
    epsilon_sc=sqrt(epsilon_T^2+R_max).

At each prepared total energy, the exact left-incoming scattering isometry is within epsilon_sc of ideal transmission plus exp(-i theta B). All inequalities retain reflected output. This estimate is deliberately loose; zero coupling, for example, has a better exact answer than its spectral-range bound.

### The missing energy-shift term for an initially product clock

The physical ideal target is the same clock packet with U acting on the system/pointer. In energy variables it is F(E) U, not U F(E). Ignoring that order would hide recoil and the conservation-law limitation.

For theta=pi/2, direct algebra using P1_Z=(I-X)/2 gives

    integral [U F(E)-F(E) U]*[U F(E)-F(E) U] dE = (1-V) I.

The real nonnegative packet makes V the actual overlap here. Consequently the full outgoing scattering state and the physical product-clock ideal satisfy, uniformly over all system inputs and reference entanglement,

    ||Psi_out-Psi_ideal|| <= epsilon_sc+sqrt(1-V).

After pointer/direction measurement, discarding records or tracing the physical clock, trace-distance contraction gives the same upper bound on instrument output distance and any common event-probability difference. This is not merely a bound on classical basis discrimination.

A closed parameter bound avoids relying on quadrature for V. Write

    h_clock(K)=sqrt(m/p) f(p),  p=sqrt(2mK),
    C_h=m[pi/(2Delta p_min)+1/(2p_min^2)].

For the cosine packet ||h_clock'||<=C_h. Translation by the energy gap gives

    1-V <= 2omega^2 C_h^2,
    epsilon_full=min(1,epsilon_sc+min(1,sqrt(2)omega C_h)).

The square-root phase term is thus controlled analytically. The full-output bound is not obtained by falsely tracing energy or assuming a common incoming E envelope.

### A sharper bound for the pointer event alone

Replacing M(E) by ideal P1_Z gives an effect with diagonals 1/2 and off-diagonal -V/2. Hence

    (1-V)/2 <= ||E_click-P1_Z||
       <= min(1,epsilon_sc+(1-V)/2)
       <= min(1,epsilon_sc+min(1/2,omega^2 C_h^2)).

The first lower bound is exact; the sufficient upper bounds are conservative. Full quantum output accuracy costs sqrt(1-V), whereas this particular pointer probability costs only (1-V)/2. Good basis frequencies alone do not certify preservation of coherent records.

## 7. Worked finite cases and a constructive ideal limit

These are dimensionless examples, not an atom-cloud calibration. Take m=1, omega=0.1, L=5pi, g=p0/10 and the cosine packet. All channels are open. The target angle is pi/2. Table values are rounded; analytic expressions are authoritative, while V and actual effect errors below are numerical quadratures.

| p0 | Delta | Numerical coherence floor (1-V)/2 | Numerical worst pointer-event error | Analytic pointer-error upper bound | Analytic full-output bound |
|---:|---:|---:|---:|---:|---:|
| 10 | 0.002 | **0.5 exactly** | 0.500003 | 0.85972 | 1 |
| 10 | 0.1 | 0.022845 | 0.030934 | 0.40474 | 0.60451 |
| 40 | 0.1 | 0.001516 | 0.005566 | 0.09427 | 0.14844 |
| 160 | 0.1 | 0.0000960 | 0.001345 | 0.02316 | 0.03696 |
| 640 | 0.1 | 0.00000602 | 0.0003354 | 0.005763 | **0.009229** |

The last finite case has clock mean kinetic energy approximately 204800 in these dimensionless units and coupling g=64. It therefore has an analytic full-instrument/event error bound below 1% in trace-distance convention, under the stated asymptotic preparation/readout. Selected full-output numerical trace distances are about 0.00346–0.00351, not a replacement for the uniform bound.

The disjoint-band case has extremely accurate relative velocity but cannot discriminate the two Z eigenstates: both click with probability approximately 0.499998. It nevertheless makes real energy transitions, with probabilities approximately 0.495 and 0.497 from the two incoming energy eigenstates. Energy exchange is not the same as adequate measurement of energy coherence.

For fixed omega, Delta, m and L, take p0->infinity and g=pi p0/(2mL). Then the displayed sufficient bounds show epsilon_sc=O(1/p0), sqrt(1-V)=O(1/p0), and epsilon_full->0. This is a constructive controlled limit, not just a numerical trend. It requires growing clock kinetic energy O(p0^2) and interaction strength O(p0); no free ideal clock has been supplied. Packet minimum spatial spread pi/(2Delta) and detector length stay fixed along this particular route.

Equivalently, a useful regime needs both omega much smaller than the absolute kinetic-energy bandwidth p0 Delta/m and Delta much smaller than p0, together with omega<<g<<p0^2/(2m). These demands can coexist. The obstruction is a missing resource in some preparations, not an impossibility of constructing an accurate internal-clock instrument.

## 8. Verification and scope

The script checks 108 independent matrix boundary-matching cases, flux column orthogonality, the degenerate-model limit, zero coupling, pointer completeness, energy-transfer kinematics, the analytic upper bounds on sampled energies, product-preparation normalization and five parameter cases. Quadrature is split at all channel-support edges; 128/256-panel results are compared. These are floating-point consistency checks, not formally rounded interval certificates. The analytic proofs, not finite sampling, justify the uniform statements.

The complete outgoing instrument is derived, not fitted to the cold-atom observations. The Hamiltonian still uses a prescribed nonrelativistic geometry and coupling, an ideal stable pointer, open scattering channels and asymptotic readout. Spatial calibration uncertainty is not included in this new estimate; the prior scalar calibration formula must not be transplanted without a matrix-phase derivation. Finite-time arrival/storage/decoherence, repeated-use degradation, experimental coupling identification and gravitational refoliation remain constructive tasks.

This directly extends the physical-clock work within M0/W1-W6. It does not derive the supplied Hamiltonian, phenomenal passage, a Gamma/chi constitution law or the necessary absolute. The surviving gain is a correct interacting-clock instrument with explicit coherence requirements and a quantitatively controlled route to ideal-clock behavior.

**Downstream record qualification:** [The classical tick readout bridge](CLASSICAL_TICK_READOUT.md) audits the Wadhia et al. experiment and supplies a separate nondemolition label-readout error composition bound. The less-than-1% example above bounds the stipulated quantum instrument, not physical sensor dissipation, classical record retention or sustained reuse.
