# On-shell incoming preparation without a polar controller

## 1. Constructive result and its precise limit

The [two-carrier internal reader](INTERNAL_REFERENCE_EVENT.md) used a polar-normalized spectral encoding to specify physical initial states. That established existence and an error bound, but not how the encoding was generated. Here that encoding is **replaced by incoming scattering preparation under the very same autonomous Hamiltonian**.

Choose smooth, finite momentum-band incoming packets whose *entire* free total-energy support fits the gravitational window. The incoming wave operator maps these already-on-shell free physical states into interacting physical states. It preserves total energy and the constraint, needs no ideal controller, and uses no postselection on the system input. A quantitative bound certifies approximate blank/ready apparatus states at finite upstream epochs.

This is a source-accounted **scattering preparation**, not exact finite-time synthesis from an arbitrary kinematic product state. It still specifies an incoming physical state as boundary data. It does not derive that boundary state, ordinary wave-packet production, or the universe's initial conditions from nothing. In/out descriptions are representations of one constrained solution, not an external account of reality being created in time.

The gain is concrete: the previously assumed nonlocal polar preparation map is no longer needed for the construction, and the preparation cost is included in the completed-record bounds rather than declared negligible.

## 2. One Hamiltonian, two constraint representations

Retain all degrees of freedom, positive spatial gate projectors, internal-coordinate interpretation and declared gravitational domain of the two-carrier report. The physical Hamiltonian and its free incoming counterpart are

    H_2=P^2/(2m)+P_Q^2/(2M)+E_b+omega X_S
        +v K_X(X)+u K_Q(Q),
    H_0=P^2/(2m)+P_Q^2/(2M)+E_b+omega X_S,
    H_2,H_0 >= E_b-omega >=0.

There are four X recorder gates and three Q reader gates, including validity sampling and conditional memory copy. Every potential is part of the lapse-coupled matter action. The free operator H_0 is an asymptotic comparison, **not an externally switched stage** of the actual H_2. Its free constraint is a boundary representation on the incoming sector, not a claimed global equivalence of constraint theories or scalar-clock quantizations.

Let

    C_2=H_2-A, C_0=H_0-A,
    A_p eigenvalues epsilon_n(p)=omega_g[2n+1+nu(p)],
    nu(p)=sqrt(1/4-8p^2/3).

On a fixed radial level and positive subcritical scalar band, A has the continuous window I with Jacobian J(p)=8 omega_g p/(3nu). The two physical root spaces are

    H_phys,0 = 1_I(H_0) H_free,
    H_phys,2 = 1_I(H_2) H_interacting.

Their rigging norms both include division by J(p(E)) before the root rescaling. Geometry and apparatus energy are constrained together; a physical incoming seed is not a tensor product of an independently chosen geometry with an arbitrary clock.

### Why physical preparation must start on-shell

In this sector the zero spectral projector of C_j on the ordinary kinematic Hilbert space is zero: for any fixed apparatus energy E, the set of scalar momenta satisfying E=epsilon_n(p) has Lebesgue measure zero. This remains true if the apparatus has atomic spectral components. Thus there is no nonzero normalizable **kinematic** vector in ker(C_j).

Group averaging supplies normalizable **physical** states in a different norm. An ordinary bounded kinematic unitary cannot turn a normalizable off-shell vector into a generalized zero-constraint history. This does not prohibit preparation in constrained physics. It specifies the right task: map physical input states to physical output states, or give physical incoming data and its interacting realization. The construction below does exactly that.

## 3. Smooth finite-band free packets

For each carrier begin with the normalized compact cos-squared comparison packet used previously:

    psi_comp(x)=exp(i p0 x) f(x+d), p0=mv,
    supp(f)=[-a,a],
    f_1=||f'||=pi/(sqrt(3)a),
    f_2=||f''||=pi^2/(sqrt(3)a^2).

The comparison packet is not being asserted to have finite momentum support. Let s=p-p0 and choose 0<Delta<p0/2. Define an even C1 cutoff

    chi_Delta(s)=1,                                      |s|<=Delta/2,
                cos^2[pi(|s|-Delta/2)/Delta], Delta/2<|s|<Delta,
                0,                                      |s|>=Delta.

Its weak derivative bounds are

    ||chi'||_infinity<=pi/Delta,
    ||chi''||_infinity<=2pi^2/Delta^2.

Let g(s)=chi_Delta(s) f_hat(s)/N, where N is its L2 normalization. Include the same position-centering phase exp(i s d) and boost p0. The packet is chosen as an incoming resource; multiplying by chi is a mathematical specification, not an assertion that a spectral filter has been physically applied for free.

Chebyshev and Plancherel give

    eta_b=2 f_1/Delta,
    ||(1-chi)f_hat||<=eta_b,
    N>=sqrt(1-eta_b^2)>=1-eta_b,
    ||psi_band-psi_comp||<=2eta_b.

The incoming packet has compact positive momentum support, finite kinetic energy and variance, and finite position variance: its momentum amplitude and first derivative are square integrable. It is not compactly supported in position. For both carriers, the product preparation differs from the previous compact comparison by at most

    beta=2eta_bX+2eta_bQ.

The finite position-moment statement is about the **free incoming packets**. The norm dressing bound below does not by itself prove finite position variance of the exact interacting state; its finite-energy normalizability and probability-concentration estimates must not be confused with moment bounds.

## 4. Exact spectral fit before any interaction

Take independent free incoming carrier packets, the fixed blank register preparation, and arbitrary S input, including entanglement with an untouched reference. Use an untouched zero-energy purification of E when writing the preparation as an isometry. Call this product isometry V_band. Free detector, memory, validity and flag levels remain degenerate as declared in the apparatus model.

Write

    K_c=mv^2/2+Mu^2/2,
    E_c=E_b+K_c,
    W=half-width of the gravitational window.

The exact carrier bands imply

    |H_0-E_c| <= B_free on range(V_band),

    B_free=v Delta_X+Delta_X^2/(2m)
           +u Delta_Q+Delta_Q^2/(2M)+omega.

If B_free<W, then

    1_I(H_0)V_band=V_band

exactly. No polar inverse, input-dependent success probability, or neglected tail outside the gravitational window is needed. This fits both S energy levels and their coherences, not just one eigenstate or the mean energy.

Via the free rigging map, V_band therefore specifies normalized physical incoming states. Their geometric energy is tied to their total free energy. The free-root product form does not eliminate those joint gravitational correlations.

## 5. Incoming wave operator and constraint intertwining

On the free sector with both momenta positive, define

    Omega_- = strong-limit_(s->infinity) exp(-iH_2 s)exp(iH_0 s).

The next section gives an integrable incoming Cook bound. Applying it first on a dense set of smooth positive-momentum packets, then extending by isometry, constructs Omega_-. No asymptotic completeness assumption is required.

It obeys

    exp(-iH_2 t)Omega_-=Omega_-exp(-iH_0 t),
    1_I(H_2)Omega_-=Omega_-1_I(H_0).

Acting trivially on gravity, it consequently intertwines the joint constraints:

    exp(-iC_2 t)(I_g tensor Omega_-)
       =(I_g tensor Omega_-)exp(-iC_0 t).

Group averaging transports this relation to the physical Hilbert spaces. The energy and Jacobian J are unchanged. Thus

    V_in=Omega_- V_band

is a physical interacting preparation isometry, with source energy bounded in I. This is an on-shell scattering construction generated by H_2 itself, not projection of an arbitrary off-shell state onto the constraint.

No pulse work is missing: H_2 is autonomous, the potentials and system Hamiltonian can exchange energy with carrier kinetic energy, and the conserved total source remains A. Selecting the free seed wave packets and the declared gravitational sector is still incoming boundary/resource data, not a zero-residue derivation of it.

## 6. A finite-upstream readiness certificate

Here is the explicit incoming estimate, including its constants. For one carrier with initial center -d, let L_0,L_1,L_2 be the centered Fourier L1 derivative bounds from the earlier compact packet:

    L_0=sqrt(pi/a) sqrt(1+a^2 f_1^2),
    L_1=sqrt(pi/a) sqrt(a^2+a^2(1+a f_1)^2),
    L_2=sqrt(pi/a) sqrt(a^4+a^2(2a+a^2 f_1)^2).

With c_1=pi/Delta and c_2=2pi^2/Delta^2, use the safe normalized bounds

    D_0=L_0/(1-eta_b),
    D_1=(L_1+c_1 L_0)/(1-eta_b),
    D_2=(L_2+2c_1 L_1+c_2 L_0)/(1-eta_b),
    p_min=p0-Delta, v_min=p_min/m,
    A_in=(D_2+3D_1/p_min+3D_0/p_min^2)/sqrt(2pi).


During backward free evolution by s>=0, the phase derivative on x>=0 is

    x+d+ps/m >= x+d+v_min s.

Two integrations by parts therefore give

    ||1_[X>=0] exp(iH_0 s)psi_band||
      <= A_in/[sqrt(3)(d+v_min s)^(3/2)].

The interaction in that coordinate is bounded by v k, k=2pi/ell. Its complete incoming integral is at most

    C_in(d)=2 v k A_in/[sqrt(3)v_min sqrt(d)].

For two carriers the potential lives in two strips, so sum the two incoming bounds:

    ||(Omega_--I)V_band|| <= C_in,X(d_X)+C_in,Q(d_Q)=:C_in,total.

This is an operator norm on the prepared S-input isometry, uniformly over reference entanglement, not a small operator norm of Omega_--I on its entire Hilbert space.

At an earlier finite relational epoch -s, intertwining and the tail integral give

    ||exp(iH_2 s)V_in-exp(iH_0 s)V_band||
       <= sum_i c_i/sqrt(d_i+v_min,i s),

where c_i=2v_i k_i A_in,i/(sqrt(3)v_min,i). For any readiness tolerance zeta>0, a sufficient finite past duration is

    s_ready=max(0,max_i {[(2c_i/zeta)^2-d_i]/v_min,i}).

The actual incoming state is then within zeta of the freely evolving ready packets. Since the free packets have blank detector/reader bits, the probability of any nonblank ready bit at that epoch is at most zeta^2. The freely evolved S state is not constrained to be blank.

This is a finite-past approximation certificate for an incoming boundary preparation. It is **not** an exact finite-time state-synthesis algorithm, a projection onto C=0, or a guarantee that arbitrary physical initial states relax into the desired preparation. Earlier packet centers, flight durations and spreads are resources; making readiness arbitrarily accurate is not free.

## 7. Complete record bounds with the preparation cost included

The previous two-carrier transport and future escape comparison is for the same Hamiltonian H_2 and the same compact comparison packets V_0. It can therefore be reused **only after changing the preparation estimate**:

    ||V_in-V_0|| <= beta+C_in,total =:delta_prep.

The previous polar cost alpha_2 is removed, not added again. All other comparison constants are evaluated for the chosen late or early relative-carrier preparation. With delta_tr, eta_out and E_escape as in the two-carrier report,

    Delta_in = delta_prep+delta_tr+2eta_out+E_escape,
    Delta_out,in = delta_prep+delta_tr+4eta_out
                   +E_escape/(1-eta_out).

For every late single interrogation after the common clearance, Delta_in bounds the complete register-output channel in half-diamond distance, capped at one. For the late preparation,

    Pr(V=0 or G=0)<=Delta_in^2,
    Pr(R!=M_mem)<=Delta_in^2.

For the early preparation, separately evaluating its constants gives

    Pr(V=0,G=1)>=1-Delta_in,early^2.

The joint outgoing projectors L_rvg and L_perp from the earlier construction commute with H_2 and C_2. Restricted to V_in, they still define the complete physical instrument

    J_y(rho)=L_y rho L_y,
    sum_y Tr J_y(rho)=Tr rho.

In free incoming coordinates the record effects are

    E_y=V_band^dagger Omega_-^dagger L_y Omega_- V_band,
    sum_y E_y=I_S.

The scattering map between the positive incoming and positive outgoing sectors need not be unitary onto the latter. The orthogonal outgoing failure effect is retained; neither bound states nor other escape channels are declared absent. The probability outside the joint right-outgoing sector is at most

    [delta_prep+delta_tr+2eta_out+E_escape/(1-eta_out)]^2.

These probabilities need no sharp phase interrogation or time-sampling prior. The earlier single-interrogation, external extraction/reset and macroscopic-noise limitations remain. The incoming representation changes preparation, not the nature of a human observation or phenomenal constitution.

## 8. Six finite witnesses in the same fixed gravitational model

Keep the two-carrier parameters, fixed omega_g=10^28, negative Lambda, scalar band [0.05,0.25], register source E_b and late/early distances of the preceding report. For each carrier choose

    Delta=10^12 f_1.

Then eta_b=2e-12 per packet and beta=8e-12. Each band is strictly positive, Delta<p0/2. The free energy support occupies less than 3.55e-6 of the available half-window even in the largest design. Thus the spectral fit includes a large explicit margin; exact centering is not being numerically inferred by subtracting huge nearby energies. A centering error smaller than W-B_free preserves the exact support inclusion.

| Schedule | q | Preparation comparison cost delta_prep | Complete record error Delta_in | Flag-pattern error probability bound |
|---|---:|---:|---:|---:|
| Late | 100 | 0.00478612 | 0.025244 | 6.373e-4 |
| Late | 1000 | 0.000050117 | 0.00036097 | 1.303e-7 |
| Late | 10000 | 0.00000050414 | 0.000013522 | 1.829e-10 |
| Early | 100 | 0.01328555 | 0.035808 | 1.283e-3 |
| Early | 1000 | 0.000133112 | 0.00046316 | 2.146e-7 |
| Early | 10000 | 0.00000133118 | 0.000014539 | 2.114e-10 |

The expected flag pattern is V=G=1 for late readout and V=0,G=1 for early readout. The cost is larger than with an assumed exact polar controller; the construction pays the actual incoming-dressing bound.

Finite-past readiness at norm tolerance 1e-7 is certified, for the late designs, after moving the reference origin earlier by approximately 4.12e7, 4092 and 0.400 time units respectively. For the strongest early design 0.409 suffices. These are conservative sufficient durations, not minimal preparation times or measured cosmological quantities. The huge energies, masses and negative Lambda remain formal conditional resources, not realistic cosmological parameters.

## 9. Verification and the remaining target

Run:

    python verification/incoming_constraint_preparation.py
    python -m verification.incoming_constraint_preparation

The verifier writes [incoming_constraint_preparation.json](verification/incoming_constraint_preparation.json). It checks 201 cutoff samples, 94 derivative comparisons, 81 incoming phase inequalities, six exact-support/bound designs, 18 finite-past readiness certificates, and the inherited full eight-qubit late/early gate channels (four system matrix units each). It computes incoming costs separately for each relative preparation. Analytic functional calculus, Cook estimates and constraint intertwining establish the continuum claims; floating evaluations are consistency witnesses, not interval certificates or a simulated gravitational experiment.

**Supplied:** explicit finite-band free physical seeds, an autonomous source-preserving incoming scattering map, no polar controller or off-shell postselection, finite-upstream readiness bounds, and complete output instruments with the new preparation cost.

**Not supplied:** a finite-time synthesis from arbitrary physical input, the origin/production of the chosen incoming wave packets and gravitational boundary data, a cyclic source/readout/reset engine, noise protection, a unique gravitational domain, inhomogeneous constraints, or phenomenal constitution.

A [finite source–clock alternative](FINITE_SOURCE_CLOCK.md) now supplies an already-physical excited source feeding a finite lattice program clock, with explicit depletion and pending outcomes. It replaces the apparatus rather than synthesizing this report's continuous incoming packets. Its entire finite spectrum fits the gravitational window, but finite recurrences restrict its retention theorem to a controlled readout window; fixed-gap dynamics and initial resource data remain obligations. The scattering preparation above remains an independent conditional construction, not an off-shell history-generation algorithm or a derivation of boundary data.
