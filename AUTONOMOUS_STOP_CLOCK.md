# An autonomous stopped-clock event instrument

## 1. Constructive result—and the distinction it does not erase

We now specify a positive, time-independent Hamiltonian that lets an internal pointer run on the approach side of a boundary and stops its free motion on the transmitted side. Exact scattering derives a **complete click/no-click instrument**, including energy-transfer backaction. In the outgoing channel the recorded coordinate is stationary: its statistics do not require choosing a late auxiliary-time slice. Dressed outgoing record effects are conserved observables of the full Hamiltonian.

A controlled fixed-mean-speed resource family approximates a calibrated one-pass arrival reading. There are both a full-output state bound and a direct timing-error bound.

**Important scope:** this device measures an operational stopped/sojourn-clock observable. It does not establish a universal sharp quantum first-entry time. Reflection and quantum recrossing cannot simply be deleted from an arrival definition. The construction is asymptotic scattering, not yet a finite-time first-click latch or a single combined proof for the [finite record tape](AUTONOMOUS_RECORD_TAPE.md). It supplies the internally stored event observable missing from the earlier slice-based readout, but not all remaining detection hardware.

Code: [autonomous_stop_clock.py](verification/autonomous_stop_clock.py). Results: [autonomous_stop_clock.json](verification/autonomous_stop_clock.json).

## 2. A bounded-below autonomous stopping Hamiltonian

Let X,P be the approaching carrier clock and Y,K the clock-pointer coordinate/momentum. Use hbar=1 and

    H=P^2/(2m)+Theta(-X) K^2/(2M),    m,M>0.

The coefficient is fixed in space, not switched at a prescribed time. Before the boundary, both coordinates have quadratic free motion. After transmission to the right, the pointer's bare free Hamiltonian is zero. Switching the pointer kinetic term to zero is an engineered model assumption, not a derived material mechanism or stability guarantee against perturbations.

For fixed pointer momentum k the operator is

    H_k=P^2/(2m)+epsilon(k) Theta(-X),
    epsilon(k)=k^2/(2M).

Each fiber is self-adjoint on H2(R) and nonnegative. The physical H is their self-adjoint direct integral on the maximal spectral domain. Equivalently it is the nonnegative closed-form realization with kinetic form

    integral dx dy [ |partial_x psi|^2/(2m)
                    +Theta(-x)|partial_y psi|^2/(2M) ].

A naive common H2 domain for both coordinates is not required. The right-side pointer Hamiltonian is degenerate; no unbounded-below linear-momentum clock is being proposed.

K is conserved. On the appropriate finite-energy domain the Heisenberg equation gives

    Y(t)-Y(0)=(K/M) integral_0^t Theta(-X(s)) ds.

This exposes the operational meaning: the pointer accumulates residence on the approach side. For a classical one-pass trajectory that equals the approach time. It is not, for arbitrary quantum histories, automatically the time of the first crossing.

## 3. Exact scattering, energy transfer and correct channel variables

Prepare the incoming **left channel** in a product of carrier energy amplitude F(e), e>0, and pointer momentum amplitude g(k). The incoming free Hamiltonian is

    H_in,left=e+epsilon(k).

At the boundary, conservation of total energy gives

    p=sqrt(2me),
    E=e+epsilon(k),
    q=sqrt(2mE).

The transmitted carrier accelerates: the pointer's former kinetic energy is transferred to it. Boundary continuity of the wavefunction and its X derivative yields

    r(e,k)=(p-q)/(p+q),
    T(e,k)=2sqrt(pq)/(p+q),
    |r|^2+|T|^2=1.

T is **flux normalized**. The transmitted plane-wave coefficient is `2p/(p+q)`, not T; confusing the two breaks normalization.

The transmitted joint energy amplitude is

    Phi_T(E,k)=T(E-epsilon(k),k) F(E-epsilon(k)) g(k),

with F zero for nonpositive arguments. The reflected amplitude, in left-channel carrier energy e and pointer momentum k, is

    Phi_R(e,k)=r(e,k)F(e)g(k).

The maps have the correct measures dE dk and de dk, respectively; dE=de at fixed k. If physical outgoing carrier momentum is used instead, the transmitted amplitude is multiplied by sqrt(q/m), with E=q^2/(2m).

**Why tracing E is legitimate here:** on the right, the pointer free Hamiltonian is zero, so E is the physical outgoing carrier energy independently of k. This differs from tracing an incoming total energy as if it belonged to the carrier alone while the pointer still had energy epsilon(k). The shifted F(E-epsilon) and all pointer coherences must be retained.

The potential step has no bound channel for these incoming states. Both propagating channels are open because e>0. Left-incoming states scatter into transmitted and reflected sectors; neither sector is silently discarded.

## 4. Complete internally defined click/no-click instrument

Define click as the transmitted outgoing sector, with pointer coordinate y read there. Its Kraus density, mapping incoming carrier energy to outgoing carrier energy, is

    (K_y F)(E)=1/sqrt(2pi) integral dk exp(iky) g(k)
                   T(E-epsilon(k),k) F(E-epsilon(k)).

The reflected no-click branch, with its still-running pointer ignored, has Kraus family

    (N_k F)(e)=g(k) r(e,k) F(e).

Thus

    I_click(B)(rho)=integral_[y in B] dy K_y rho K_y^dagger,
    I_no_click(rho)=integral dk N_k rho N_k^dagger.

Fourier Parseval, the energy-shift substitution and flux conservation prove

    integral dy K_y^dagger K_y + integral dk N_k^dagger N_k=I.

This is a completely positive, normalized instrument, valid also with arbitrary untouched references. No-click means **reflection in the asymptotic experiment**, not a claim that the carrier has merely not arrived by a specified finite deadline. A finite-deadline no-click instrument is a different object and is not supplied here.

### Why the click record no longer needs an auxiliary readout epoch

The outgoing right Hamiltonian is E tensor I_Y. Consequently

    rho_Y(k,k')=integral dE Phi_T(E,k) Phi_T(E,k')*

is invariant under outgoing free evolution: the factors exp(-iEt) cancel. The pointer distribution is a stored asymptotic record, not an instantaneous clock position evaluated on an arbitrarily selected late slice. On the reflected branch only the branch probability is used, so its still-running pointer is not misidentified as a stopped time record.

For the physical finite-time wavefunction, scattering convergence approaches this outgoing description. An explicit convergence rate, finite-distance latch and finite-time interrogation error are **not derived** here. Exact stationarity of the outgoing asymptote must not be promoted to literal cessation of every wavefunction tail at a finite epoch.

### Conserved record effects in the full physical description

Let Omega_out be the standard outgoing channel wave operator for the step Hamiltonian. At fixed k the usual matching solutions give its scattering representation; the open-channel 2x2 flux matrix has diagonal r,-r and equal off-diagonal T, hence is unitary. Below the left-channel threshold only the right channel is open and its reflection has unit modulus. There is no normalizable bound state for this monotone step. These standard step-scattering facts give the complete scattering-sector channel representation, not a conclusion inferred from a numerical grid.

In the outgoing representation the bounded record effect

    O_B,out=Pi_transmitted 1_B(Y)

commutes with H_out. Intertwining therefore gives

    O_B=Omega_out O_B,out Omega_out^dagger,
    [O_B,H]=0

in the strong spectral sense on the scattering sector. The no-click effect is dressed similarly. These are generally **asymptotic, nonlocal observables**, not local instantaneous first-crossing projectors.

For C_aux=P_T+H on its maximal joint-spectral domain, they are also Dirac observables, independent of the auxiliary coordinate T. This is a concrete internally recorded event observable, not merely another finite-T conditional probability. This invariance belongs to the full carrier-plus-pointer observable, not to a clock-only POVM after the coherent pointer has been prepared and removed from the description. The coherent ready pointer and incoming preparation still provide the relative time origin; no normalizable uniform time prior or absolute external time is introduced or derived.

## 5. A controlled one-pass calibration and full-output bound

Take the incoming carrier amplitude

    F(e)=A(e) exp[i d sqrt(2me)],
    A(e)=1/sqrt(Delta) cos(pi(e-e0)/(2Delta))

on `[e0-Delta,e0+Delta]`, zero elsewhere, with e_min=e0-Delta>0. In the incoming free-channel preparation the carrier's reference center is X=-d at the epoch at which the real pointer packet is centered at Y=0. This is a product incoming scattering preparation, not a claim of strict finite-time localization wholly to the left.

Let g(k) be the normalized real cosine packet on `[k0-b,k0+b]`, with k0>b>0. Define

    epsilon_max=(k0+b)^2/(2M),
    p_min=sqrt(2m e_min),
    rho=(sqrt(1+epsilon_max/e_min)-1)
          /(sqrt(1+epsilon_max/e_min)+1).

Then reflection probability is at most rho^2. Compare the full output with an ideal all-transmitted stopped-pointer state

    Phi_id(E,k)=A(E) exp[i d sqrt(2mE)] g(k)
                      exp[-i epsilon(k) tau(E)],
    tau(E)=dm/sqrt(2mE).

The pointer in this comparison runs freely for the calibrated one-pass time tau(E). Its carrier energy uses the original A envelope. It is a comparison state for this specified preparation, **not an asserted universal arrival-time POVM for arbitrary carrier phases**.

Three estimates control the comparison:

1. Replacing the exact reflected/transmitted interface by perfect transmission costs vector norm at most sqrt(2)rho, since `(1-T)^2+|r|^2=2(1-T)<=2rho^2`.
2. Shifting A by epsilon costs at most `epsilon_max ||A'||`, and `||A'||=pi/(2Delta)`.
3. Taylor expansion of `d sqrt(2m(E-epsilon))` has residual at most `d m^2 epsilon_max^2/(2p_min^3)` after its linear term `-epsilon tau(E)`.

Consequently the **full outgoing state**, including its reflection flag, obeys

    D_trace(actual,ideal) <= min(1,delta),
    delta=sqrt(2)rho + pi epsilon_max/(2Delta)
              +d m^2 epsilon_max^2/(2p_min^3).

The vector inequality supplies this trace-distance statement; it is not squared into an arbitrary observable error. Reading y and the branch flag is a contraction, so every arrival-report event has probability error at most delta. The fixed-preparation estimate is not an unrestricted diamond-norm bound over arbitrary incoming clock packets.

The amplitude-shift term explicitly requires a sufficiently broad **absolute carrier energy band** to absorb the pointer-energy transfer coherently. Narrow relative velocity uncertainty alone does not supply an accurate stopped-clock record.

## 6. Timing precision: an actual bound, not an unbounded-moment inference

Use the pointer reading

    tau_hat=M y/k0,
    tau0=d sqrt(m/(2e0)).

Let tau_min,tau_max be the extrema of tau(e) across the carrier energy band, and

    J=max(tau_max-tau0,tau0-tau_min),
    c=1/3-2/pi^2.

For the ideal comparison state, the real cosine packet has initial position variance pi^2/(4b^2), momentum variance c b^2 and zero initial position–momentum covariance. Hence

    MSE_id(tau_hat,tau0)
       <= (M pi/(2k0 b))^2 + c b^2 tau_max^2/k0^2 + J^2
       =: B_id.

For every a>0 the complete actual probability of either no-click or a click with `|tau_hat-tau0|>=a` is at most

    min(1,delta+B_id/a^2).

This uses an event-probability bound. Trace distance alone is **not** used to bound the actual pointer's unbounded second moment.

A separate direct actual moment bound is available. Write the transmitted amplitude at fixed outgoing E as

    Phi_T(E,k)=a(E,k) exp[i d sqrt(2m(E-epsilon(k)))],
    a(E,k)=T A(E-epsilon(k))g(k).

At fixed E,

    partial_k a=T A g'-(k/M)[T_e A+T A']g,
    T_e/T=|r|/(4e),    e=E-epsilon(k).

The exact unnormalized transmitted mean-square error is

    integral dy (M y/k0-tau0)^2 p_click(y)
      =(M/k0)^2 integral dE dk |(i partial_k-k0 tau0/M)Phi_T|^2.

Derivative and phase bounds give

    B_actual=[M pi/(2k0 b)
               +(k0+b)/k0 (pi/(2Delta)+rho/(4e_min))]^2
             +[b tau_max/k0+J]^2.

The unnormalized actual click MSE is at most B_actual; its conditional MSE is at most B_actual/(1-rho^2). An alternative complete failure-or-inaccurate-click bound is

    min(1,rho^2+B_actual/a^2).

Thus detector backaction, failure probability and timing noise are accounted for without removing reflection or postselecting a successful click without paying its probability.

## 7. Fixed-speed resource limit and finite values

Set d=1 and, for lambda>=2, choose

    m=lambda^6, M=lambda^2,
    e0=lambda^6/2, Delta=lambda^4/4,
    k0=lambda^2, b=lambda.

Both mean incoming velocities are one. The nominal approach time is tau0=1. Carrier mass/energy grow as lambda^6; pointer mass/energy as lambda^2. Spatial preparation/localization and energy coherence become increasingly demanding; this is not a fixed-resource limit or an assertion of arbitrary material realizability.

Then

    delta=O(lambda^-2),
    B_id=O(lambda^-2), B_actual=O(lambda^-2),
    rho^2=O(lambda^-8).

For any fixed timing tolerance a>0 the complete failure-or-inaccurate-reading probability tends to zero. This is a controlled route to a reliable operational one-pass arrival record at fixed mean speeds, not an exact first-entry theorem at finite resources.

| lambda | Full-output trace bound | Failure or error >=0.1, via reference bound | Numerical conditional time MSE |
|---:|---:|---:|---:|
| 10 | 0.039901 | 1 (uninformative) | 0.02598214 |
| 30 | 0.003887 | 0.292579 | 0.002886779 |
| 100 | 0.000333486 | 0.02631454 | 0.0002598093 |
| 1000 | 0.000003274 | 0.000263083 | 0.000002598093 |

Analytic formulas justify the bounds. Numerical MSEs are evaluations of the exact moment integrals, with 64/128 midpoint convergence checks, not interval certificates. All values are dimensionless and not a calibration to the double-dot experiment or cold-atom apparatus. For lambda=1000 the carrier reference energy is 5*10^17 model units; omitting that resource would misrepresent the result.

## 8. What this does and does not close

**Supplied:** a positive autonomous stopping Hamiltonian; a complete normalized click/no-click instrument; correct energy-transfer and coherence bookkeeping; conserved asymptotic internal record effects; a full-output approximation bound; and both reference-based and direct actual timing-error budgets.

**Not supplied:** a universal quantum first-entry time, continuous monitoring without backaction, finite-deadline no-click statistics, a local irreversible first-click latch, macroscopic readout/reset thermodynamics, or a finite-time combined tape-plus-stopping proof. The sharp spatial control and exactly zero right-side pointer Hamiltonian are model assumptions. Global unitary energy transfer does not establish free cyclic time measurement; pointer preparation, record extraction, storage robustness and reset require their own resources.

This returns directly to the problem of time: the final outgoing record effects commute with the physical Hamiltonian and hence the auxiliary-history constraint. The record can be specified independently of a selected late auxiliary-time slice. But initial boundary/preparation data remain necessary, and the constraint is not gravitational. No refoliation algebra or physical–phenomenal constitution follows from this example.

The verifier checks 48 independent boundary/flux cases, normalization, exact asymptotic moment formulas and their convergence, reflection and timing bounds for four finite resource cases. The CP completeness proof is Parseval plus exact flux conservation; sampled numerical checks do not replace it.

**Finite combined continuation:** [Finite completion and controlled future escape](FINITE_COMPLETION_CLOCK.md) now supplies a single smooth-stop recorder/flag Hamiltonian with finite-time and uniform future bounds plus a comparison to its own conserved outgoing effects. This is not the old sharp-step preparation with an added error number, and does not promote the sojourn-clock reading to a universal first-entry time.
