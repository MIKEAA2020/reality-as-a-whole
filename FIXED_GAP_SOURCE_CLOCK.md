# Fixed-gap relational readout with a finite energy reservoir

## 1. Result: the system Hamiltonian is retained, not perturbed away

The [finite source/program clock](FINITE_SOURCE_CLOCK.md) had an exact degenerate-system solution and a noncommuting correction bounded by omega T. This construction removes that growing correction while retaining the actual fixed system Hamiltonian

    H_S=omega X_S, omega=0.1,

at **every** clock position. The measured S observable is Z_S, which does not commute with H_S.

Add a finite energy-and-phase reservoir. Replace the first measurement gate by a unitary that conserves H_S+H_B exactly, exchanging system energy with that reservoir. Every later program gate already conserves this free energy. The exact finite-clock solution is recovered with unchanged onsite H_S, not a position-dependent redefinition of the system Hamiltonian.

The replacement cost is a finite-reference measurement error, not an error proportional to elapsed time. The full complete S-and-record instrument has a derived error bound of order 1/N^2 for the specified one-use reservoir family. Its energy, disturbance, source contribution and gravitational spectral fit are all retained.

**Important operational meaning:** the target is the initial S Z observable **relative to the prepared finite reservoir phase**, followed by the actual free S rotation. It is not a measurement of a fixed externally oriented Z at an unknown later instant. No perfect external phase reference or sharp random trigger time is supplied.

The finite coherent reservoir is an additional counted initial resource. Its preparation/reset is not derived from the clock source. Finite-clock recurrences, external extraction, the gravitational domain choices and phenomenal constitution remain open as before.

## 2. A finite energy-conserving gate

Use S energy states |g>=|-X_S>, |e>=|+X_S>, with energies -omega,+omega. In this basis Z_S is the flip X_E. Let the reservoir have levels n=0,...,N and

    H_B=Delta N_B, Delta=2omega.

The free energy is

    H_f=H_S+H_B=-omega+Delta q,
    q=n+e, e=0 for g and 1 for e.

Define a Hermitian swap T_SB on every interior charge block:

    T|g,n>=|e,n-1>,  1<=n<=N,
    T|e,n>=|g,n+1>,  0<=n<N.

At the two unmatched boundary states |g,0> and |e,N>, let T act as the identity. Then

    T^2=I, [T,H_f]=0.

In the detector X basis, the desired ideal CNOT_(Z_S->D) is

    U_ideal=I_S tensor P_+,D + X_E tensor P_-,D.

Its actual energy-conserving replacement is

    U_tilde=I_SB tensor P_+,D + T_SB tensor P_-,D.

It is an exactly unitary finite-dimensional operator, and [U_tilde,H_f]=0. The detector remains energy degenerate. The S flip raises or lowers reservoir energy by exactly 2omega; no system transition energy is discarded.

This is not an assertion that the bare S measurement commutes with its Hamiltonian. The exact joint observable will be T_SB, a **relational** observable involving the finite reservoir. Its induced S instrument approximates Z_S with a nonzero finite-resource error.

## 3. One-use reference state and its two overlaps

Prepare the real sine packet

    |b_N>=sqrt(2/N) sum_(n=1)^(N-1) sin(pi n/N)|n>, N>=2.

The endpoint amplitudes vanish. This is a normalized finite state, not success postselection. It has

    <H_B>=omega N,
    0<=H_B<=2omega N.

Its energy variance is finite and is included in the verifier. For the initial product resource, the total energy variance is gamma^2+Var(H_S)+Var(H_B), not just the clock hopping variance gamma^2. Its real adjacent coherence selects the initial relative phase used to define Z_S. Under free evolution this phase rotates with the reservoir rather than serving as an external fixed reference.

Let L_B lower the finite ladder and R_B=L_B^dagger raise it. On this preparation both shifted packets have norm one. Define

    c=<b|L_B b>=<b|R_B b>=cos(pi/N),
    r=<L_B b|R_B b>
      =cos(2pi/N)+(2/N)sin^2(pi/N).

The two overlaps have different roles: c determines record probabilities, while r also controls the conditional S-state update. Replacing both by a single visibility would lose part of the instrument.

For the ready detector |0>, the joint measurement-gate isometry differs from the ideal gate leaving B unchanged by

    epsilon_joint=sqrt(1-c).

This is a full-output norm bound of order 1/N. The smaller reduced instrument error derived below does **not** apply to an output that retains the reservoir unchanged.

## 4. Exact reduced measurement instrument

Measuring D after the gate gives the joint S,B Kraus operators

    A_d=[I+(-1)^d T]/2, d=0,1.

They are orthogonal projections, and sum_d A_d^dagger A_d=I. The complete S instrument after tracing the reservoir is

    J_d(rho)=Tr_B[A_d(rho tensor |b><b|)A_d^dagger].

Write D_r for S dephasing in its energy basis: diagonal entries are unchanged and off-diagonal entries are multiplied by r. A direct calculation gives

    J_d(rho)=1/4 [rho+X_E D_r(rho) X_E
                  +(-1)^d c (X_E rho+rho X_E)].

This formula retains both outcomes and their actual S states. Its effective S effects are

    E_d=[I+(-1)^d c X_E]/2.

For an initial Z_S eigenstate, the wrong-record probability is exactly

    p_wrong=(1-c)/2>0.

The ideal target is the Lüders instrument P_d rho P_d, P_d=[I+(-1)^d X_E]/2. For the complete classical-output instrument,

    epsilon_ref := (1/2)||J-J_ideal||_diamond
        <= (1-r)/4+(1-c)/2 =: epsilon_N.

To see the bound, use ||D_r-id||_diamond=1-r for the energy-basis dephasing channel, and the bound two for the anticommutator map rho -> X_E rho+rho X_E. Summing the two classical output blocks yields the displayed coefficients. This is uniform with arbitrary S/reference entanglement, not merely a probability bound on basis inputs.

The wrong-record witness also gives epsilon_ref>=(1-c)/2. Thus the reduced one-use error scales as 1/N^2 for this family, within explicit upper/lower bounds. No universal reservoir-optimality or energy–time lower bound is asserted.

## 5. The finite source clock remains exactly solvable

Keep the eight-bond source/program architecture and its conserved single-excitation source/clock sector. All whole-spectrum inclusions below refer to that declared sector, not to arbitrary extra clock excitations. Replace only its measurement bond U_1 by U_tilde; all other bonds, including the identity source-emission bond, are unchanged. The later gates involve only D,M,E,F,R,V,G and commute with H_f.

Let W_n be the product of these actual gates and Q=sum_n |n><n| tensor W_n. Since every W_n commutes with H_f,

    [Q,H_f]=0.

The actual lapse-coupled apparatus Hamiltonian is

    H=E_c I+gamma sum_n [|n+1><n| tensor U_n+h.c.]+H_f
     =Q[(E_c I+gamma A_K) tensor I+I_clock tensor H_f]Q^dagger.

Consequently the onsite free Hamiltonian really is H_S+H_B at all positions. It has not been replaced by W_n H_S W_n^dagger. All terms are autonomous and source-accounted.

Starting with the source excitation |0>, the ready detector/record bits and |b_N>,

    Psi(t)=sum_n a_n^(K)(t)|n> tensor
               W_n exp(-iH_f t)|psi_ready,b_N>
          =sum_n a_n^(K)(t)|n> tensor
               exp(-iH_f t) W_n |psi_ready,b_N>.

The a_n are **exactly the same finite-chain amplitudes** as in the source-clock report, apart from its different E_c common phase. They are independent of S and reservoir input. Source depletion and incomplete-clock probabilities are therefore unchanged, not assigned a small-omega correction.

For completed positions, tracing B commutes with its free rotation. The actual S output is the known free rotation exp(-iH_S t) applied to J_d(rho). The appropriate ideal comparison is the same free rotation applied to P_d rho P_d. Unitary invariance leaves the error epsilon_N independent of t. The classical record probabilities are independent of this free rotation outright.

This does not freeze S or measure bare Z_S at an unspecified later proper-time instant. It compares the initial S phase with the initial finite reservoir phase, while their subsequent free dynamics are fully retained. No omega T error is being hidden in a renamed target state.

## 6. Complete operation with finite-clock failure retained

Let p_pending(t) be the probability that the clock has not reached its completed program positions. It is independent of the input. Given completion, the actual instrument is J with the common free S rotation. Given noncompletion, retain the actual intermediate-history maps under separate source/program-pending labels.

If B_K bounds p_pending throughout the finite readout window, the complete instrument obeys

    error_complete <= B_K+(1-B_K)epsilon_N,

with errors capped at one when necessary. This follows by distinguishing the incomplete labels from the completed channel and applying the complete reduced-instrument bound on success. It is not normalization by an unknown input-dependent success probability.

The hardware G flag still exactly marks completed positions on the accessible histories. Its noncompletion probability remains <=B_K; reservoir measurement error does not falsely change the clock flag. G certifies schedule completion, not exact S measurement or an undisturbed phase reservoir.

The uniform finite-chain window bound and the finite-clock recurrence qualification are unchanged. This removes time growth from the **reference measurement error**, not the need for a finite completion/retention window. Repeated readout or repeated reservoir use requires its own instrument analysis.

## 7. Reservoir depletion and disturbance are real resources

The energy-conserving gate, every later unitary and the full hopping Hamiltonian commute with H_f. Hence, without conditioning away outcomes,

    Delta<H_B>=-Delta<H_S>.

For the stated reference with zero endpoint amplitudes, the nonselective S output has zero mean H_S for every input. For an energy-ground input the S energy increases by omega and B loses omega; for an excited input B gains omega. With omega=0.1 these are explicit transfers of 0.1, not work supplied by an omitted controller.

For either energy eigeninput, the unconditional B state is a half mixture of its original packet and a shifted packet. Its fidelity against the original pure reference is

    <b|rho_B,out|b>=(1+c^2)/2<1.

The same fidelity expression holds for arbitrary S input in this one-use preparation. The post-use reservoir state depends on input energy populations and on the outcome if conditioned; endpoint populations can become nonzero. One may not reuse the original c,r or symmetric-error formula after a run without checking the changed state.

The source clock also retains its own budget: its two-level source onsite energy E_c transfers to the moving clock excitation, with the same source-pending probability as before. The mean programmed hopping energy remains zero for the source-localized input, while H_S+H_B is separately conserved. This is not a thermal reset cycle, a macroscopic stable memory, or a catalytic reservoir returned unchanged.

## 8. Gravity includes the reservoir energy

The Einstein–scalar constraint is now

    C=H-A,
    A=(3/16)p_r^2+|Lambda|r^2-p_phi^2/(2r^2).

Use the same declared Friedrichs ordering and positive scalar band [0.05,0.25], but one **enlarged fixed gravitational window** for all three devices below:

    omega_g=1024, Lambda=-4 omega_g^2/3, radial level zero,
    E_gcenter=omega_g[1+(nu(0.05)+nu(0.25))/2],
    W_g=omega_g[nu(0.05)-nu(0.25)]/2,
    nu(p)=sqrt(1/4-8p^2/3).

Keep gamma=1/64 and omega=0.1. Choose one common source energy for every device,

    E_c=E_gcenter-0.1*512 = approximately 1373.16527146.

The reservoir has q=0,...,N+1 charge sectors, so the exact total energies are

    E_jq=E_c+2gamma cos[pi j/(K+1)]-omega+2omega q.

All are contained in the conservative interval

    E_c-2gamma-omega <= H <= E_c+2gamma+2omega N+omega.

For N<=512 this lies strictly inside the fixed gravitational window, with margin greater than 53.43 in the model units; the whole matter Hamiltonian is positive. The reservoir's maximum energy and mean energy are not subtracted. E_c is fixed across the three designs: increasing N raises the mean total source by the added mean reservoir energy omega N.

Atomic group averaging gives

    ||eta f||_phys^2=sum_(j,q,a) |f_(j,q,a)(p_jq)|^2/J_g(p_jq),
    epsilon_0(p_jq)=E_jq,
    J_g=8omega_g p/(3nu)>0.

After the usual square-root rescaling this is the full finite root space of dimension K times 256 times (N+1). Initial clock source, S, finite reservoir and ready registers are legitimate physical-root inputs without a polar filter. Their geometric energies are correlated by the constraint, not prepared independently. The strong constraint-compatible instrument lift from the source-clock report applies because the common spectral margin remains positive.

This changes the gravitational parameter from the previous narrow-window example to accommodate the actual added matter. It is not a passive clock change or a claim that the reservoir has no backreaction. The large source offset, finite coherent reference and declared boundary condition are conditional model resources, not observed cosmological parameters or a zero-residue explanation of them.

At fixed window the allowed reservoir energy is bounded. Sending N to infinity is not a free accuracy limit in that same gravitational code; the window or sector would need reconsideration.

## 9. Three fixed-gap resource witnesses

All devices have the same omega=0.1, gamma=1/64, E_c and gravitational parameters. Reservoir cutoff N, clock size K and the readout window are counted separately.

| N (ladder dimension N+1) | Mean reservoir energy | Clock/source positions K | Readout window | Completed instrument error epsilon_N | Complete error bound |
|---:|---:|---:|---:|---:|---:|
| 32 | 3.2 | 4096 | [8192,16384] | 0.0070613 | 0.019425 |
| 128 | 12.8 | 16384 | [32768,65536] | 0.00044938 | 0.0012273 |
| 512 | 51.2 | 65536 | [131072,262144] | 0.000028201 | 0.000076837 |

The largest device keeps a fixed system energy gap 0.2 over a window lasting 131072 units. Its completed-instrument error is below 2.821e-5, without any omega T term. The complete error below 7.684e-5 additionally pays finite-clock noncompletion. The larger error relative to the tiny-omega perturbative example buys a genuinely fixed noncommuting gap with a counted finite reservoir.

For N=512 the full-output isometry bound is about 0.00434, not 2.821e-5. The reservoir fidelity after one use is about 0.99998118 and its energy exchange is nonzero for energy eigeninputs. Reduced-instrument accuracy must not be promoted into an unchanged-resource guarantee.

The finite reference's sine state is specified initial resource data; no source pump producing that state or cyclic reset is supplied. The source excitation alone is not claimed to generate all of its energy coherence.

## 10. Verification and remaining work

Run:

    python verification/fixed_gap_source_clock.py
    python -m verification.fixed_gap_source_clock

The verifier writes [fixed_gap_source_clock.json](verification/fixed_gap_source_clock.json). For each of three reservoirs it checks ladder normalization and overlap formulas, all charge-swap involutions including boundaries, all four S matrix units for both outcomes against the exact reduced instrument, eigeninput wrong-record probabilities, source/reference energy exchange, reservoir disturbance and free-evolution covariance through the full long readout window. It separately recomputes the total gravitational spectrum bounds and 45 selected inverse/Jacobian cases, while reusing only the **identical clock amplitudes and completion bounds**, not the old tiny-omega perturbation or gravitational fit. The three clock-window designs and their spectral-sum samples run again through that dependency. Four additional detector matrix units check the exact later memory/dephasing/flag transport with S and B as spectators. Floating checks are consistency witnesses, not interval certificates or a gravitational experiment.

**Supplied:** a fixed noncommuting H_S, finite energy-conserving reservoir lift, exact joint relational measurement, complete reduced-instrument bounds independent of elapsed time, explicit reference disturbance and energy exchange, autonomous source preparation/clock motion, and a new source-accounted gravitational spectral fit.

**Still open:** preparation/reset of the coherent reservoir and blank source resources; a microscopic Hamiltonian for external record extraction; noise resistance and repeated use; a realistic localized stress tensor and inhomogeneous constraints; justification of the boundary/domain choices; and phenomenal constitution. Finite-clock recurrences remain, and absolute external-phase measurement has not been smuggled into the relational instrument.

A [shared-reference reuse construction](REUSED_REFERENCE_CLOCK.md) now supplies a guarded joint instrument for multiple fixed-gap systems, retaining actual reference updates and all record correlations. It derives entangled-input joint error bounds, a GHZ witness, explicit depletion and finite-boundary bias, plus a no-refill capacity bound and new source/gravity budgets. Unchanged single-use visibility is not an unchanged or indefinitely reusable resource; the old one-use state is not silently substituted between interactions. Finite pumping/reset and adaptive reuse remain open.
