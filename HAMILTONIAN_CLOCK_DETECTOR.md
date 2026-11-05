# A finite-mass Hamiltonian clock and spatially triggered quantum detector

## 1. Constructive target and result

The [operational accumulator](OPERATIONAL_PATH_ACCUMULATOR.md) supplied a discrete unitary update. Here a **time-independent, bounded-below Hamiltonian** supplies the motion and clock–detector coupling. There is no prescribed update sequence or prerecorded trajectory.

We solve a finite-mass clock particle scattering through a finite detector region. Its internal interaction implements an approximate quantum measurement. The exact solution retains reflection, clock–system entanglement, finite momentum bandwidth and spatial calibration uncertainty. An analytic uniform bound controls disagreement with the ideal instrument. Accuracy here concerns detector-event/instrument probabilities, not a universal elapsed-time estimation error.

This improves physical-clock adequacy beyond a linear-momentum clock or an engineered discrete shift. It is still a specified, nonrelativistic, deparametrizable model: its geometry, Hamiltonian and preparation are premises, not a derivation of gravitational constraints or a zero-residue constitution.

Verification: [hamiltonian_detector.py](verification/hamiltonian_detector.py), [results](verification/hamiltonian_detector.json). The inequalities below provide the uniform model bounds. Floating-point sampling and quadrature are independent numerical witnesses, **not** interval-certified proofs of those inequalities.

## 2. Hamiltonian, detector and preparation

Set hbar=1 and take

    H_E = L2(R_X) tensor C2_S tensor C2_D,
    H = P^2/(2m) + g 1_[0,L](X) B,
    B = P1_S tensor Y_D,   P1=|1><1|,   g>0.

The clock has ordinary quadratic kinetic energy. The system S and detector D have zero free Hamiltonians in this baseline; their asymptotic levels are degenerate. B has eigenvalues 0,+1,-1. The bounded potential makes H self-adjoint on H2(R) tensor C4 and H>=-g. The spatial interaction, rather than an externally scheduled pulse, produces the detector rotation. Its two edges cause state-dependent momentum scattering and possible reflection.

Prepare the detector in |0>_D and an incoming clock packet from the left, with normalized momentum amplitude f supported in

    p in [p_min,p_max]=[p0-Delta,p0+Delta],
    0<Delta<p0,   p_min^2>2mg.

This is an **asymptotic incoming scattering preparation**. The attractive eigenchannel has bound states; they are not removed from H, but are outside this incoming scattering preparation. Wave operators identify the free incoming packet with its interacting scattering state. No claim is made that an arbitrary finite-position packet has exactly zero bound-state component.

A straight classical passage at momentum p0 would give

    U_ideal=exp(-i theta B),   theta=gmL0/p0,

where L0 is the nominal region length. At theta=pi/2,

    U_ideal |psi>_S |0>_D
      = P0|psi> |0>_D + P1|psi> |1>_D.

Reading the pointer then implements the ideal Lüders instrument {P0,P1}. The pointer is stable outside the region because its free Hamiltonian is zero; classical decoherence or irreversible record amplification is not modeled. This is an actual system-dependent detector coupling, not a pointer rotation whose probabilities are independent of the system.

We allow the actual length L to lie in [L0-ell,L0+ell], 0<=ell<L0. Here ell represents finite spatial registration/calibration of the detector region. It is distinct from packet position spread and is not called an arrival-time uncertainty.

## 3. Exact position description: both orientations and flux

In eigenchannel b of B, a stationary incoming component satisfies

    [-1/(2m) d^2/dX^2 + gb 1_[0,L](X)] psi = p^2/(2m) psi.

Let

    k_b=sqrt(p^2-2mgb),
    A_b=(p^2+k_b^2)/(2p k_b),
    D_b=cos(k_b L)-i A_b sin(k_b L).

Continuity of psi and psi' at both edges gives

    t_b(p,L)=exp(-ipL)/D_b,
    r_b(p,L)=-i (p^2-k_b^2)/(2p k_b) sin(k_b L)/D_b.

The outside solutions are exp(ipX)+r_b exp(-ipX) on the left and t_b exp(ipX) on the right. b=0 gives t_0=1,r_0=0 exactly. The incoming and outgoing outside speeds have the same magnitude because the asymptotic internal levels are degenerate.

The conserved current is j=Im(psi* psi')/m. Thus

    |t_b|^2+|r_b|^2=1.

Right incidence has reflection amplitude exp(-2ipL) r_b and the same transmission amplitude. The two-incidence scattering matrix is unitary; retaining the reflected orientation is part of its probability conservation.

Positive incoming momentum support does not itself establish positive local arrival current for a packet; no time-of-arrival POVM is inferred from current at a point.

This is not a single first-order unitary evolution in X. X is not a global monotonic clock once reflection is allowed. The position description uses incoming/outgoing branches and their flux normalization, rather than deleting the return branch or assigning it negative probability.

The verifier checks the closed formulas against a separate edge-matching linear solve on 729 parameter/eigenchannel samples, including full two-incidence flux identities.

## 4. Time description, physical inner product and matched events

Ordinary evolution is generated by the same self-adjoint H. Its asymptotic scattering operator is the one above: the stationary generalized eigenfunctions and the time-dependent wave operators describe the same Hamiltonian scattering problem. No direct time-domain grid simulation is claimed here.

Explicitly, with incoming generalized eigenfunctions u_(p,b) normalized to momentum measure dp,

    Psi(X,T)=sum_b integral dp f(p) exp(-i p^2 T/(2m))
                       u_(p,b)(X) Pi_b chi.

Each integrand solves i dPsi/dT=H Psi. Its outgoing wavepacket coefficients are exactly t_b and r_b. This connects the position boundary problem to the same Hamiltonian's time evolution, rather than comparing independently chosen dynamics.

For an explicitly stationary constrained history, introduce auxiliary T and

    H_kin=L2(R_T) tensor H_E,
    C=-i d/dT + H.

The joint spectral multiplier k+E defines a self-adjoint C on its maximal domain. With test functions in L1(R_T,H_E) intersect L2(R_T,H_E),

    eta(f)=integral dT exp(iHT) f(T),
    integral ds <f,exp(isC)g> = <eta(f),eta(g)>.

Absolute integrability follows from the L1 norms and allows the change of variables. eta is onto H_E: choose f(T)=h(T)exp(-iHT)psi with integral h=1. Quotient/completion gives H_phys=H_E with its ordinary positive inner product. Formal histories exp(-iHT)psi are distributional in T, not normalized by a uniform prior on R.

For any bounded detector effect E,

    (R(E)f)(T)=exp(-iHT) E exp(iHT) f(T)

commutes with the constraint group and eta R(E)=E eta. Scattering-sector preparation and output effects therefore have a common Dirac representation. Wave operators are isometries onto the absolutely continuous sector, not onto the omitted bound-state sector.

**Matched event:** prepare the same incoming packet and ready pointer, then read the same outgoing direction and pointer. Its probability computed from H's asymptotic evolution equals the flux-normalized position-scattering calculation. This does not equate “pointer at external time T0” with “pointer after transmission”; these are different events. Nor does it construct a unitary coordinate change from T to one unsigned position value.

## 5. The exact finite-clock instrument

Let tp,tm and rp,rm denote the b=+1,-1 amplitudes. For a fixed incoming p, the system Kraus operators for transmitted/reflected direction and pointer j are

    K_T0 = P0 + (tp+tm)/2 P1,
    K_T1 = i(tp-tm)/2 P1,
    K_R0 = (rp+rm)/2 P1,
    K_R1 = i(rp-rm)/2 P1.

Their effects sum exactly to I. For an unresolved outgoing momentum, the instrument is

    I_(d,j)(rho)=integral dp |f(p)|^2 K_(d,j)(p) rho K_(d,j)(p)*.

Reflection is an explicit outcome, not discarded and renormalized away. Clock momentum remains correlated with the internal state before it is traced out. A readout retaining momentum bins or coherent clock degrees of freedom is a different, more informative instrument.

At the ideal angle pi/2, transmission/pointer 0 corresponds to P0 and transmission/pointer 1 to P1. Reflection is a missed-crossing/failure outcome. A reflected clock need not have left the pointer unchanged, so both reflected pointer results must be retained.

## 6. Uniform analytic validity bound

Write

    delta=2mg/p_min^2 < 1,
    s=sqrt(1-delta),  L_max=L0+ell.

The following bounds hold for the **entire** momentum band, all b in {0,+1,-1}, and every allowed L.

### Interface and reflection error

Since |D_b|>=1,

    |t_b-exp(i(k_b-p)L)| <= A_b-1
      <= alpha = delta^2/[2s(1+s)^2].

Also

    |r_b|^2 <= R_max=min(1,delta^2/[4(1-delta)]).

For the first inequality, D_b-exp(-ik_b L)=-i(A_b-1)sin(k_b L); and A_b-1=(p-k_b)^2/(2p k_b). The reflection inequality follows directly from its numerator and |D_b|>=1.

### Nonlinear phase, momentum bandwidth and spatial calibration

Taylor's remainder for sqrt(1-x), with |x|<=delta, gives

    |(k_b-p)L + b gmL/p|
      <= beta = L_max m^2 g^2/[2 p_min^3(1-delta)^(3/2)].

The difference between this passage phase and the nominal ideal angle obeys

    |gmL/p-gmL0/p0|
      <= gamma_p+gamma_x,
    gamma_p=gmL0 Delta/(p_min p0),
    gamma_x=gm ell/p_min.

Combining |exp(ix)-exp(iy)|<=|x-y|,

    epsilon_T=alpha+beta+gamma_p+gamma_x,
    |t_b-exp(-ib theta)|<=epsilon_T.

### Full output and event probabilities

Transmitted and reflected outgoing clock subspaces are orthogonal. Compare the exact scattering isometry with an ideal transmitted clock packet and U_ideal on S/D. For every normalized internal input, including one entangled with a reference,

    ||Psi_out-Psi_ideal|| <= epsilon
      = sqrt(epsilon_T^2+R_max).

This follows eigenchannel by eigenchannel and then integrates over normalized |f|^2. It is not an estimate obtained by sampling a momentum grid.

Consequently the trace distance of the full outputs, and hence the difference in probability of **any common detector event**, is at most min(1,epsilon). Coarse-graining clock bins or reading only the pointer cannot increase that distance. The statement is unconditional; a postselected transmission calculation needs its own normalization bound.

At theta=pi/2 and initial system |1>, the ideal output has no weight in the union of reflected outcomes and transmitted pointer 0. Therefore

    p(wrong transmitted pointer OR reflection) <= min(1,epsilon^2).

Initial |0> is read exactly in this model. For arbitrary inputs the full instrument comparison still uses the epsilon bound; do not confuse a squared basis-readout failure bound with a squared error bound for every coherent observable.

The bound is conservative: it need not identify an optimal coupling or detector length. Its virtue is explicit dependence on finite energy, bandwidth, spatial calibration and backaction, with no missing reflected branch.

## 7. A sharp bandwidth/localization cost

Use the normalized compact-band packet

    f(p)=cos(pi(p-p0)/(2Delta))/sqrt(Delta)

inside the band, zero outside. It has finite energy and finite position variance. For its unchirped free reference packet,

    Delta X=pi/(2Delta),
    Delta P=Delta sqrt(1/3-2/pi^2),
    <H_free>=[p0^2+Delta^2(1/3-2/pi^2)]/(2m).

In fact Delta X>=pi/(2Delta) for any normalized packet confined to this band with finite position variance. After removing the mean-position phase, this is the Dirichlet Poincare inequality on an interval of width 2Delta; the cosine packet saturates it. Thus reducing the bandwidth term has an explicit minimum spatial-extent cost. Free propagation can broaden the packet; Delta X is **not** being asserted to be its arrival-time standard deviation.

At fixed theta=pi/2, reducing g requires L0=pi p0/(2mg) to grow. It reduces reflection and phase-curvature error, but leaves the bandwidth contribution in this bound unless Delta/p0 also shrinks. More strongly, for actual L=L0 and fixed nonzero bandwidth the weak-coupling limit has

    lim_(g->0, gmL0/p0=theta) p_wrong_on_|1>
      = integral dp |f(p)|^2 cos^2(theta p0/p) > 0,  theta=pi/2.

The transmission amplitudes converge uniformly to exp(-ib theta p0/p), reflection vanishes, and the integrand is positive except at isolated momenta. Thus weak coupling alone does not remove bandwidth error. Arbitrarily ideal behavior along this construction is not supplied at fixed detector extent and fixed localization resources; no universal optimal-clock no-go theorem is inferred.

## 8. Worked finite parameters

These are dimensionless examples with m=1,p0=10,hbar=1, not calibrated rubidium parameters. Values below are rounded evaluations of the analytic expressions; the expressions, not rounded floating-point outputs, define the bounds.

| g | Delta | L0 | ell | Minimum Delta X | epsilon, approximately | Basis failure bound epsilon^2 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.1 | 15.708 | 0 | 15.708 | 0.02637 | 0.0006953 |
| 0.1 | 0.1 | 157.080 | 0 | 15.708 | 0.01671 | 0.0002793 |
| 0.1 | 0.02 | 157.080 | 0 | 78.540 | 0.004067 | 0.00001655 |
| 0.1 | 0.1 | 157.080 | 1.571 | 15.708 | 0.03257 | 0.001061 |

For example, the third case bounds any common event-probability discrepancy by approximately 0.00407, and wrong-pointer-or-reflection probability on |1> by approximately 1.66e-5. The packet's minimum free spatial width is approximately 78.54, half the detector length: the accuracy is not free localization.

Numerical integration gives a |1> failure probability about 1.79e-6 and full-output trace distance about 0.00102 for initial system |+> in that case. Those are quadrature results, not new analytical guarantees. The verifier compares 512/1024-panel Simpson calculations, tests edge-error extremes, and checks the uniform expressions on a dense sample in addition to the independent scattering solve. It does not turn convergence agreement into a rigorous floating-point interval certificate.

## 9. Consequence and remaining task

This supplies the promised worked **Hamiltonian clock–detector model with a quantitative validity bound**. The particle's kinetic energy is bounded below, the detector interaction is spatially local in ordinary nonrelativistic QM, the pointer reads the system, and reflection/backaction are actual predictions. Position-based and auxiliary-time descriptions agree for the same prepared scattering event when orientation and flux are retained.

What remains is consequential:

- The system's free Hamiltonian is zero here. [The energy-exchange extension](ENERGY_EXCHANGE_CLOCK.md) now supplies the required coupled-channel analysis and bounds; it is not obtained by substituting into these degenerate-channel formulas.
- The readout is an asymptotic passage detector. A finite-time first-arrival detector with storage/decoherence needs its own model; it is not silently included.
- The Hamiltonian, spatial geometry, mass, coupling and preparation are supplied. Stationarizing their dynamics does not derive them or solve refoliation.
- The cold-atom tables still do not fix this coupling, incoming packet, image-level entropy or covariance. Their observed path-clock stalls motivate retaining missed events, but do not validate this detector Hamiltonian.

[The energy-exchange construction](ENERGY_EXCHANGE_CLOCK.md) supplies that noncommuting extension, including product-clock preparation, coherent outgoing channels and a controlled full-instrument limit. Finite-time detector delivery/storage remains a separate task. This remains direct M0/W1-W6 time work, not a derivation of consciousness, the Gamma/chi law or the necessary absolute.
