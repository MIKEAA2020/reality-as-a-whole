# A gravitating proper-time clock and its derived readout instrument

## 1. The detector is no longer a spectator

The [Einstein–scalar recollapse model](RECOLLAPSING_GRAVITATIONAL_CLOCK.md) left the detector's gravitational contribution unspecified. Here a comoving oscillator is added to the reduced Einstein–matter action. Its energy changes the constraint and the geometry. Quantization is an exactly solvable **Morse-potential** problem rather than the previous exponential wall.

The oscillator's first two energy levels form an invariant probe sector. An incoming coherent superposition acquires energy-dependent gravitational reflection phases. Reading its outgoing coherence gives a derived, normalized two-outcome **Ramsey instrument on the geometry**. Its phase response has a controlled relation to elapsed comoving proper time.

A consequential domain issue is resolved explicitly: the gravitating matter produces negative auxiliary bound eigenvalues, so the old globally positive square-root reduction cannot simply be reused. The real-spectrum constraint selects the allowed continuum.

**Scope:** this is a homogeneous, smeared comoving phase-clock model. It is not a local detector in an inhomogeneous spacetime, the old arrival/completion apparatus with gravity silently appended, or a full preparation/readout/reset engine. Negative Lambda remains a solvable test, not a claim about the observed cosmological constant. No full refoliation or singularity resolution is established.

Code: [gravitating_clock_probe.py](verification/gravitating_clock_probe.py). Results: [gravitating_clock_probe.json](verification/gravitating_clock_probe.json).

## 2. Derive the matter contribution from the lapse-coupled action

Keep 8piG=hbar=1 and the same fixed unit fiducial cell. Add a proper-time oscillator q to the reduced action:

    L=-3a adot^2/N + a^3 phidot^2/(2N)-N Lambda a^3
        +qdot^2/(2N)-N Omega^2 q^2/2.

The last two terms describe an internal oscillator carried by conserved comoving matter, homogeneously smeared to preserve FLRW. Its integrated energy has no explicit scale-factor dependence; its density is h_D/a^3 and its pressure is zero. This is **not** the Lagrangian of a spatially homogeneous Klein–Gordon field, which would have different a^3 factors. The reduced comoving-matter ansatz is specified, not claimed to derive a localized laboratory apparatus from a covariant fluid/field theory.

The oscillator momentum and proper energy are

    p_q=qdot/N,
    h_D=(p_q^2+Omega^2 q^2)/2.

The ADM lapse multiplies

    C_ADM=-p_a^2/(12a)+p_phi^2/(2a^3)+Lambda a^3+h_D.

Using x=3ln(a), T=sqrt(3/2)phi and the same positive densitization gives

    C=p_T^2-p_x^2-mu^2 exp(2x)+(4/3)exp(x)h_D,
    mu^2=4|Lambda|/3.

The sign and volume dependence of the detector term are derived, not chosen to preserve the old scalar Hamiltonian. The detector is not assigned zero gravitational energy merely because it is called a measuring device.

Upon quantization,

    E_n=Omega(n+1/2).

The zero-point energy is retained. Subtracting it would change the comoving matter source and must be specified as a different action/counterterm, not a free change of notation. Number n is conserved by the bulk constraint; initial support on n=0,1 is therefore an exactly invariant sector, not an uncontrolled truncation of bulk dynamics. Coherent preparation and readout between those levels are boundary operations whose energy-reference apparatus is not yet included.

## 3. Classical backreaction and proper lifetime

For one fixed detector energy E define

    kappa=2E/(3mu),    k=-p_T>0,
    V=exp(x),    R=sqrt(k^2+kappa^2).

The constraint is

    k^2=p_x^2+mu^2 V^2-2mu kappa V.

In increasing scalar time T, its exact recollapsing trajectory is

    V(T)=k^2/[mu(R cosh(T-T_*)-kappa)],
    p_x(T)=-k R sinh(T-T_*)/[R cosh(T-T_*)-kappa].

Thus

    V_max=(kappa+sqrt(kappa^2+k^2))/mu,

larger than the unprobed value k/mu. The clock's source energy changes the geometry even when it remains in an energy eigenstate. The two energy branches in a coherent probe generally describe different conditional geometries.

The relation to comoving proper time s follows directly from the ADM scalar equation:

    |ds/dT|=2V/(3k).

The absolute bang-to-crunch proper lifetime is therefore

    T_proper(E,k)=(2/(3k)) integral_[all T] V(T)dT
       =4/(3mu)[pi/2+arctan(kappa/k)].

At E=0 it reduces to 2pi/(3mu)=pi/sqrt(3|Lambda|), the massless-scalar result. Branch labels and phases use increasing T with p_T<0; reversing time orientation reverses the oriented phase convention. The positive lifetime above is a magnitude, not an assertion that increasing T has the positive-proper-lapse orientation. It is the model's formal boundary-to-boundary lifetime at V->0, not a claim that a laboratory device survives the singular endpoints or that this minisuperspace approximation is valid at arbitrarily high curvature. A finite-volume preparation/readout experiment needs its own controlled comparison.

## 4. Quantum constraint: a Morse operator with an essential qualification

For a fixed oscillator energy,

    C_n=p_T^2-Theta_n,
    Theta_n=-partial_x^2+mu^2 exp(2x)-2mu kappa_n exp(x).

Each Theta_n is a self-adjoint, semibounded Morse Schrödinger operator on its natural domain. The full number-resolved operator is the self-adjoint direct sum; the constraint uses the maximal joint-spectral domain. On the invariant two-level sector all potential lower bounds are finite.

Set z=2mu exp(x). The decaying generalized mode is

    f_(kappa,k)(x)=z^(-1/2) W_(kappa,ik)(z),

where W is the Whittaker function. Its continuum eigenvalue is k^2>0. In addition, when kappa>1/2 there are auxiliary bound eigenvalues

    lambda_j=-(kappa-j-1/2)^2,
    j=0,1,... with j<kappa-1/2.

The zero-energy threshold is not a normalizable extra mode. Bound eigenfunctions are proportional to

    exp(-z/2) z^s L_j^(2s)(z),
    s=kappa-j-1/2>0.

### Do not take a square root on the negative auxiliary spectrum

For a bound eigenvalue -s^2 the constraint would require

    p_T^2+s^2=0.

There is no real p_T solution. Group averaging with self-adjoint p_T annihilates this sector; it is not a physical no-click state to be postselected away and renormalized. Formal exponential-in-T solutions of the differential equation are not states of this real-spectral rigging construction.

Only on the nonnegative continuum does the chosen scalar-frequency sector obey

    i partial_T psi=sqrt(Theta_n) psi.

The square root here is restricted by the spectral projection onto that sector. Replacing Theta_n with |Theta_n| would change the constraint and add spurious states.

For mu=1, Omega=0.6, the two energies are 0.3 and 0.9, giving kappa_0=0.2 and kappa_1=0.6. The excited channel has one auxiliary eigenvalue **-0.01**. This is a concrete failure of blindly importing the previous globally positive scalar Hamiltonian, not an instability inferred from a physical negative-frequency state.

### One physical norm, including the apparatus

Normalize each continuum mode by its incoming amplitude. Its modulus before normalization is

    |A_in|=|Gamma(-2ik)/Gamma(1/2-kappa-ik)|.

Thus the real normalization factor is

    N_kappa(k)=|Gamma(1/2-kappa-ik)|
                  /[sqrt(2pi)|Gamma(-2ik)|].

The resulting incoming/outgoing plane amplitudes have modulus 1/sqrt(2pi). Standard Morse scattering spectral theory gives the continuum transform. On the two-level physical sector,

    H_phys = L2(R_+,dk) direct-sum L2(R_+,dk).

The original squared-constraint rigging retains the same factor 1/(2k) in each normalized spectral channel. Reduced coefficients are obtained by dividing on-shell test amplitudes by sqrt(2k), as in the prior gravitational construction. Negative bound sectors contribute no physical branch. No normalizable uniform scalar-time prior is introduced.

## 5. Exact joint gravitational scattering

The small-volume expansion of z^(-1/2)W is

    A_in z^(ik)+A_out z^(-ik),
    A_in=Gamma(-2ik)/Gamma(1/2-kappa-ik),
    A_out=Gamma(2ik)/Gamma(1/2-kappa+ik).

Consequently the reflection multiplier, with a common volume-plane phase convention, is

    S_kappa(k)=Gamma(2ik)/Gamma(-2ik)
       *Gamma(1/2-kappa-ik)/Gamma(1/2-kappa+ik)
       *(2mu)^(-2ik),
    |S_kappa(k)|=1.

At kappa=0 Gamma duplication recovers exactly the previous exponential-wall phase

    S_0(k)=Gamma(ik)/Gamma(-ik)*(mu/2)^(-2ik).

The joint reflection map is

    U_grav=sum_[n=0,1] S_(kappa_n)(k) tensor |n><n|.

This is unitary on the common constrained continuum. It includes the clock's gravitational backreaction rather than evolving the geometry with one bare S and attaching a readout afterward.

Prepare an **incoming-channel product** a(k) tensor (|0>+|1>)/sqrt(2). That is not a claim that a finite-volume geometry/detector wavefunction factorizes: the channel eigenfunctions depend on n. A product in the wrong total-energy or position representation would be a different preparation. Channel rephasings must also transport the preparation and readout reference, not alter S while holding their numerical matrices fixed.

## 6. Derive the complete Ramsey instrument

Read the outgoing oscillator in |+>=(|0>+|1>)/sqrt(2) and |->=(|0>-|1>)/sqrt(2). The induced Kraus multipliers on geometry are

    M_+(k)=[S_(kappa_0)(k)+S_(kappa_1)(k)]/2,
    M_-(k)=[S_(kappa_0)(k)-S_(kappa_1)(k)]/2.

They satisfy exactly

    M_+^dagger M_+ + M_-^dagger M_-=I.

These completeness claims use the invariant prepared two-level code. If other oscillator levels are admitted, the joint readout is extended with the orthogonal out-of-calibration projector; it has zero probability for the specified preparation. That physical calibration outcome is distinct from the negative auxiliary bound modes, which have no real-spectrum physical weight.

Thus both readout outcomes, their probabilities and their conditioned geometry states are supplied. On a narrow spectral packet,

    p_+=[1+cos(Delta phase)]/2,
    p_-=[1-cos(Delta phase)]/2,
    Delta phase=arg S_(kappa_1)-arg S_(kappa_0).

For the mu=1, Omega=0.6 example, the spectral response p_- is approximately 0.79746 at k=0.4 and 0.36464 at k=8. A change of the actual scalar-energy state changes detector statistics: the probe extracts information. These are spectral response values, not probabilities assigned to nonnormalizable eigenstates in an experimental preparation; packet probabilities are their |a(k)|^2 averages.

Ignoring the oscillator produces

    rho_out(k,k')=1/2 sum_n S_n(k)S_n(k')* rho_in(k,k').

Summing the two Kraus outcome channels gives exactly this reduced map. It preserves the k distribution but can destroy k coherence. A two-alternative spectral algebra control gives reduced geometry purity about 0.98440 from a pure joint incoming state. Narrow disjoint continuum packets can approximate that control; it is not claimed to be an exact normalizable two-point energy state.

This is derived measurement backaction, not a phenomenological noise channel. On the **joint** physical Hilbert space the clock-frame/scattering relation remains unitary. After discarding the clock, a geometry-only map need not be unitary. Applying the old bare reflection to geometry alone therefore changes the model, rather than exhibiting inconsistent clock descriptions.

### Gravitationally dressed record effects, not a bare detector flip

The outgoing free scalar evolution is multiplication by exp(-ikT) on both detector channels. Its readout projectors P_+ and P_- therefore commute with that evolution. In the incoming continuum representation, the joint record effects are

    F_+/-=U_grav^dagger (I tensor P_+/-) U_grav.

They act at fixed k and commute with k^2 I_D. Let V_in be the direct-sum normalized Morse transform including the incoming channel phases. On the auxiliary positive-continuum subspace define

    O_+/-=V_in^dagger F_+/- V_in,

and extend them by zero on the negative bound subspace. These bounded effects strongly commute with Theta_D. Acting identically on the scalar coordinate they also commute with p_T^2 and hence with the actual gravitational constraint C. On the physical two-level sector O_++O_-=I_phys. Their kinematic sum is the continuum projector, not the whole auxiliary identity; the complementary bound projector has zero rigging weight, not a physical detection failure probability.

This is an explicit conserved gravitational record algebra. It is generally nonlocal in x. The bare finite-volume detector flip is **not** the same observable:

    [Theta_D,X_D]=-(4/3)exp(x)[h_D,X_D] != 0.

The dressing changes the conditional geometry along with the detector channel and preserves the constraint eigenvalue. It does not supply a local finite-time pulse that flips detector energy without accounting for the source. This distinction is precisely what is lost by attaching an unchanged external readout operator to the geometry.

There is no lost transmission channel in this reflecting continuum problem. The two-outcome instrument is complete for its stated asymptotic readout. Finite-time failure-to-complete, preparation failure, macroscopic readout efficiency and reset are **not** thereby modelled. They must not be assigned invented probabilities or silently identified with the excluded auxiliary bound modes.

## 7. The phase is an elapsed-proper-time response

Differentiate the exact reflection phase with respect to the clock's proper energy E, holding scalar k fixed:

    tau_quantum(E,k)=partial_E arg S_E(k)
       =4/(3mu) Im digamma(1/2-kappa+ik).

The classical counterpart follows from the reduced Hamiltonian:

    partial_E H_T=-2V/(3k),
    -integral partial_E H_T dT = T_proper(E,k).

In the controlled high-k limit, the digamma response approaches

    tau_quantum(E,k) -> 4/(3mu)[pi/2+arctan(kappa/k)],

with the asymptotic difference checked explicitly in the verifier, including a large-action limit in which k and kappa grow together at fixed ratio. This is the same classical proper lifetime derived from the Einstein equations, not a new independent time parameter fitted to an unrelated phase.

At E=0 there is also an exact quantum identity:

    tau_quantum(0,k)=2pi/(3mu) tanh(pi k).

It tends to the classical 2pi/(3mu) at high k, while low-k response differs. This is a response function of this quantum-clock scattering experiment, not proof of a universal replacement of classical proper time.

For a finite oscillator gap Omega,

    Delta phase/Omega
      =(1/Omega) integral_[E0]^E1 tau_quantum(E,k) dE,

on a continuous unwrapped phase branch. The two clock energies gravitate differently. Therefore the finite-gap result is an **average response across backreacted geometries**, not automatically the proper duration of one unperturbed classical spacetime. The small-gap/semiclassical limit is the controlled route to that interpretation.

One quadrature measures a cosine; it does not unwrap an arbitrarily large elapsed time. Another coherent quadrature/reference and a calibrated range are needed for an actual phase-time estimate. A two-level phase clock is periodic, not a global monotonic coordinate or a self-adjoint canonical time operator for a semibounded energy.

## 8. Controlled weak-clock limit: backreaction and signal vanish together

On a compact scalar band k in [k_min,k_max], k_min>0, let kappa range from zero to kappa_max. Choose

    J=ceil(kappa_max),
    a_min=1/2-kappa_max+J>0,
    L=2[k_max(a_min^(-2)+a_min^(-1))+J/k_min].

The digamma recurrence shifts all real parts positive, and its imaginary-part series is bounded by a first term plus an integral. Therefore

    |partial_kappa arg S|<=L,
    |S_kappa1-S_kappa0|<=L |kappa1-kappa0|,
    p_-<=min(1,L^2 |kappa1-kappa0|^2/4).

This is an explicit uniform analytic bound, not a maximum over sampled k values. Near k=0, bound-state thresholds/resonances require separate treatment; the compact-band condition is binding.

For the oscillator ground/excited pair, kappa_0=Omega/(3mu) and kappa_1=Omega/mu. As Omega tends to zero, both reflection channels approach the bare geometry and the per-pass phase contrast tends to zero. The divided response Delta phase/Omega can remain finite, but its statistical readout noise cannot be divided away for free. Repetition, quadrature references and preparation resources would need accounting.

This proves a resource trade-off **for this family**, not a universal information–gravity disturbance inequality. An arbitrarily weak probe is not disproved; an uninformative one-pass zero-coupling limit is distinguished from a free precise clock.

**Record information and coherence follow-up:** [TIME_DECISIVE_TEST_GRAVITY_RECORD.md](TIME_DECISIVE_TEST_GRAVITY_RECORD.md) uses this scattering model for a finite-wavepacket spectral discrimination and visibility comparison. It applies known complementarity, assumes boundary preparation and readout, and does not by itself supply a duration instrument or general gravity result.

## 9. What has been closed and what remains

**Supplied:** a matter-action contribution to the actual gravitational constraint; exact conditional backreaction; correct spectral selection when positivity fails; a joint constrained Hilbert space; a derived complete geometry-readout instrument and strongly constraint-compatible dressed record effects; and a proper-time phase response with a classical limit.

**Not supplied:** a localized detector compatible with inhomogeneous Einstein constraints, a finite-time completed arrival/latch apparatus with all of its gravitational energy, a Hamiltonian for boundary preparation and phase-reference readout, a cyclic thermal/reset budget, full refoliation or a zero-residue physical–phenomenal constitution. The older nongravitational completion error bound remains unavailable as a cosmological error bar.

The verifier checks 120 classical backreacted constraint cases, 64 Whittaker-mode differential equations, 16 zero-probe Bessel reductions, 21 bound-mode differential equations, 12 phase derivatives, the proper-time classical limit, Kraus completeness/reduced-channel agreement and uniform weak-probe estimates. Floating evaluations are consistency witnesses, not interval certificates or empirical observations.

A [finite-duration proper-dust extension](DUST_CLOCK_RECORD.md) now supplies an action-coupled register operation with complete instrument, finite completion and positive relational source budget. It **adds reference matter and declares a different ordering/domain**, rather than proving a passive clock equivalence or completing the original oscillator boundary-readout engine. Its ideal continuous dust remains an unsupplied finite-reference resource. The Morse model above still requires its real-spectrum selection; the extension does not remove that requirement or import the old autonomous apparatus error. Spatially inhomogeneous constraints remain a further, distinct obligation.
