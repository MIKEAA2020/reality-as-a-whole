# Reusing one finite reference: joint records, correlations and a finite capacity

## 1. Result: no fresh reservoir between readouts

The [fixed-gap source clock](FIXED_GAP_SOURCE_CLOCK.md) supplied one noncommuting readout with a finite energy-and-phase reservoir. Here **m distinct systems share that same reservoir**, without reset or replacement. Each retains H_Sj=0.1 X_Sj. One finite source excitation drives one finite program containing all m readout blocks.

The result has three parts:

1. An exact guarded **joint history instrument**, retaining the reservoir updates and all outcome correlations.
2. A joint, entangled-input error bound of order m^2/D^2 for the specified reference family, with a GHZ parity witness showing that quadratic scaling is genuine in the narrow-phase regime.
3. Explicit reservoir energy depletion, disturbance and boundary effects, including a finite-use energy-capacity bound for the declared no-refill device.

A nearly unchanged single-readout visibility is **not** evidence of a fresh or indefinitely reusable reference. The calculation exhibits correlated wrong records even when that marginal visibility is unchanged.

This extends a conditional homogeneous gravitational model. It does not supply arbitrary adaptive reuse, a pump preparing/resetting the reservoir, an external extraction engine, inhomogeneous gravity or phenomenal constitution. The source and coherent reference remain counted initial physical resources.

## 2. Actual sequential instrument and a finite guard

Use m S qubits and the same reservoir levels n=0,...,N, with

    H_f=omega sum_j X_Sj+2omega N_B, omega=0.1.

In each S energy basis write e_j=0 for ground energy -omega and e_j=1 for excited energy +omega. The conserved charge is

    q=n+sum_j e_j.

For use j, T_j flips S_j while lowering or raising B by one so q is conserved. At its unmatched finite-ladder states it acts as the identity, exactly as in the one-use construction. The joint detector-outcome Kraus operators are

    A_dj^(j)=[I+(-1)^dj T_j]/2.

The actual sequential operators are

    K_d=A_dm^(m)...A_d1^(1),
    I_d(rho)=Tr_B[K_d(rho tensor |b><b|)K_d^dagger].

There is **no trace-and-reset of B between factors**. Sum_d K_d^dagger K_d=I, even when boundary effects occur. Full conditional reservoir/system states are retained by K_d; the reduced formula does not assert factorization after an outcome.

For a certified m-use run, choose the initial packet with an m-site guard:

    b_n=sqrt(2/D) sin[pi(n-m+1)/D],  m<=n<=N-m,
    b_n=0 otherwise,
    D=N-2m+2>=2.

It is normalized and symmetric about N/2, so <H_B>=omega N. Before the last of m interactions, every shifted branch still has reservoir level between 1 and N-1. The unmatched boundary rule is therefore never used during the certified run. Branches can reach an endpoint **after** the last use.

The guard is an initial preparation cost. We do not assert that the old one-use packet can be used m times with its old formula unchanged. An unguarded counterexample is checked explicitly below.

The fresh systems may have an arbitrary joint input state, including entanglement with an untouched reference, but are initially independent of B. They are loaded as distinct registers in the finite apparatus; an on-demand input-injection mechanism is not assumed or constructed. Intermediate arbitrary feedback or extra couplings to B are outside this theorem.

## 3. Exact common-phase identity for the reduced joint instrument

Extend b by zero outside the physical ladder and define its finite autocorrelations

    C_l=sum_n b_n b_(n+l), C_-l=C_l.

For 0<=l<D,

    C_l=[(D-1-l)cos(l theta)+sin((l+1)theta)/sin(theta)]/D,
    theta=pi/D.

For l>=D, C_l=0. In particular,

    C_1=cos(theta),
    C_2=cos(2theta)+(2/D)sin^2(theta).

A ket path through the m lifted gates shifts B by its total input-minus-output S energy charge. A ket/bra pair therefore contributes C_l with |l|<=2m. In the S energy basis, for input matrix unit |r><s|, output matrix element (e,f) and outcome bit string d, the exact value is

    [I_d(|r><s|)]_(e,f)
      =2^(-2m) (-1)^[d dot(e xor r)+d dot(f xor s)]
        C_[wt(r)-wt(e)-wt(s)+wt(f)].

This derives the whole joint instrument, not just its separate one-use marginals.

An equivalent useful expression is

    w(phi)=|sum_n b_n exp(i n phi)|^2/(2pi), -pi<=phi<=pi,
    integral w(phi)dphi=1,
    I_joint=integral w(phi) I_phi^(tensor m) dphi.

Here I_phi is the ideal S measurement instrument rotated in its energy phase by phi, with its S-state update retained. **The same phi appears in every factor.** Replacing this by a product of separately averaged instruments gives the wrong channel.

w is derived from a finite quantum state's phase distribution on a compact circle. It is not a prior over interrogation epochs, not uniform time sampling, and not a classical hidden-state replacement for the full reservoir. The equality describes the reduced joint channel after B is traced; the complete quantum reservoir output contains more information.

## 4. Joint error, including entangled inputs

Let Q_S=sum_j |e><e|_j. Its spectrum is 0,...,m. On both input and quantum output, the phase commutator superoperator has diamond norm at most m after centering Q_S by m/2. The phase-rotated joint instrument satisfies

    I_phi=U_phi,out I_0 U_-phi,in,
    ||partial_phi^2 I_phi||_diamond<=4m^2.

The real packet makes w even, so its first phase moment vanishes. Taylor's integral remainder gives

    (1/2)||I_joint-I_0||_diamond
        <=m^2 integral phi^2 w(phi)dphi.

Since phi^2<=(pi^2/2)(1-cos(phi)) on [-pi,pi],

    epsilon_joint <= min(1,(pi^2/2)m^2(1-C_1)).

This is a complete joint-instrument bound, uniform with entangled inputs. The known free evolution generated by sum_j H_Sj is included on both output instruments and does not change it. No omega times elapsed-time term is present.

### A lower witness: joint error really can be quadratic

Take the S input GHZ state in the energy basis,

    (|g...g>+|e...e>)/sqrt(2).

Ideal Z_S readouts have even record parity with certainty. The reused reference gives parity visibility C_m, hence

    Pr(wrong parity)=(1-C_m)/2,
    epsilon_joint>=(1-C_m)/2.

For m/D small, this lower bound is of order m^2/D^2, as is the upper bound. Independent fresh copies would instead give GHZ parity visibility C_1^m. In the eight-readout device below, even eight times the fresh one-use instrument **upper** bound is only about 1.431e-5, below the actual shared-reference GHZ error 3.807e-5. Thus summing those fresh-reference bounds would be demonstrably invalid for the joint reused instrument. This is a family-specific resource scaling, not a universal optimal-reference theorem.

## 5. Explicit correlated errors

For two independent initial +Z_S inputs, define a wrong record to be bit 1. The one-record error probability is

    q_wrong=(1-C_1)/2.

The actual joint wrong probability is

    P(1,1)=(3-4C_1+C_2)/8,
    Cov(wrong_1,wrong_2)=(1+C_2-2C_1^2)/8
                       =sin^2(pi/D)/(4D)>0.

For N=12,m=2,D=10 the exact sequential calculation gives

    each wrong-record probability: 0.02447174,
    both wrong:                    0.00298615,
    fresh-reference product:       0.00059887.

The nearly fivefold difference is not caused by discarding bad outcomes. It is present in the normalized complete joint instrument. Conditioning on an earlier wrong result changes later risk; unconditional marginal accuracy alone does not diagnose that correlation.

These inputs have zero mean initial S energy. The correlation witness is distinct from the ground-input energy-depletion witness below; there is no claim that every input consumes the same mean reservoir energy.

## 6. Actual state update, depletion and the boundary

For fresh energy-ground S inputs, trace all processed systems and records only to examine the **reservoir marginal**. During the guarded run it evolves exactly as

    rho_B^(j)=1/2 [rho_B^(j-1)+L_B rho_B^(j-1)L_B^dagger],
    rho_B^(m)=2^(-m) sum_(k=0)^m binom(m,k)
                 L_B^k |b><b| (L_B^dagger)^k.

This is a result of the actual joint protocol, not an assumed reset or an assertion that B is uncorrelated with prior outputs. Consequently

    <H_B>_m=omega N-m omega,
    Var(H_B)_m=Var(H_B)_0+m omega^2,
    <b|rho_B^(m)|b>=2^(-m) sum_k binom(m,k)|C_k|^2.

The total S energy gain is m omega. H_f conservation accounts for it exactly. The reference's original-state fidelity drops even though

    Tr(L_B rho_B^(j))=C_1

throughout the certified run. An unchanged adjacent coherence is therefore compatible with depletion and growing record correlations. It is not free catalytic reuse.

After m uses the bottom population is already

    rho_B^(m)(0,0)=2^(-m)|b_m|^2>0.

For one additional ground-input use, the full finite boundary rule yields

    rho_B' =1/2 rho_B+1/2 L_B rho_B L_B^dagger
             +1/2 rho_B(0,0)|0><0|,
    Delta<H_S>=omega[1-rho_B(0,0)],
    P(D=0)=1/2[1+rho_B(0,0)].

The old symmetric one-use formula has acquired a bias. This does not forbid another use; it invalidates the guarded formula and requires the updated finite-boundary instrument. Coherence C_1 alone does not capture it. For N=12,m=2, the bottom population after the planned run is approximately 0.00477458; the next ground readout has label-zero bias about 0.00238729.

The verifier also deliberately reuses the **unguarded** old packet (N=8, initial guard one) twice. The exact complete channel remains trace preserving, but differs from the common-phase formula by more than 0.0068 in a tested matrix element. Boundary effects are real dynamics, not an event to normalize away.

### A finite-use energy-capacity law

For this no-refill apparatus, all program interactions conserve H_f, so the clock source does not secretly recharge B. Suppose m fresh ground-input readouts each have unconditional marginal instrument error at most epsilon<1/2 relative to the target. Trace-distance control of S energy gives a gain of at least omega(1-2epsilon) per system. Since H_B>=0 and initially <H_B>=omega N,

    m <= N/(1-2epsilon).

The statement includes failure in the marginal error; it cannot be applied only to selected successes while ignoring the rest. It is a necessary energy-capacity bound for this declared mechanism and task, not a universal limit on apparatuses with additional pumps or reservoirs.

Mean energy capacity and coherent **joint** accuracy are different constraints. The guarded family also pays its m-site initial guard and the m^2/D^2 phase-error budget. No optimal reuse lifetime is claimed.

## 7. One finite source program, not m resets

Use one source excitation and a finite lattice clock. After its identity emission bond, concatenate m seven-gate readout blocks. Each block contains the energy-conserving lifted S_j-to-D_j gate, detector/memory/environment copying, recorder completion, validity sampling, readout copying and its local completion flag. The total programmed length is

    L=1+7m.

Every gate commutes with H_f. Therefore the source-clock history unitary Q obeys [Q,H_f]=0 and the actual Hamiltonian is exactly

    H=Q[(E_c I+gamma A_K) tensor I+I_clock tensor H_f]Q^dagger.

All S Hamiltonians remain fixed at every clock site. Source emission and clock amplitudes are the exact finite-chain amplitudes, independent of the joint S input and B state. The final block's G flag certifies the entire program on the accessible histories.

For gamma=1/64 and a window with scaled minimum epoch tau=gamma T_min, maximum epoch 2tau, use the general finite-clock bound

    B_clock=[sqrt(S_L)/tau+epsilon_b]^2,
    S_L=L(L+1)(2L+1)/6,
    epsilon_b=1e-12.

Choose K=32tau; the missing-boundary-bond estimate is far below that positive cap. Since L changed, S_L is **recomputed**, not copied from the eight-bond one-readout example. The complete operation obeys

    error_complete <=B_clock+(1-B_clock)epsilon_joint.

Source-pending probability is separately bounded by [1/tau+epsilon_b]^2. The joint error includes noncompletion and all record strings. Finite-clock recurrences still prevent a small all-future retention bound. All statements concern one query after unmonitored evolution in the certified window, not repeated monitoring of the clock.

## 8. Gravity counts all m systems and the shared reservoir

The lapse constraint is C=H-A with the same declared radial ordering and positive scalar band [0.05,0.25]. In the conserved one-excitation source/clock sector the exact energies are

    E_jq=E_c+2gamma cos[pi j/(K+1)]-m omega+2omega q,
    0<=q<=N+m.

Thus

    E_c-2gamma-m omega <=H<=E_c+2gamma+2omega N+m omega.

For all three devices below choose one fixed gravity and source:

    omega_g=4096, Lambda=-4 omega_g^2/3, radial level zero,
    E_gcenter=omega_g[1+(nu(0.05)+nu(0.25))/2],
    W_g=omega_g[nu(0.05)-nu(0.25)]/2,
    E_c=E_gcenter-0.1*2048 = approximately 5492.66108585.

This enlarged common window contains every declared apparatus energy, with margin greater than 213.4 model units. The Hamiltonian is positive. The source energy is the same for every row; increasing N adds actual reservoir energy and increasing m adds actual systems. Neither is subtracted to pretend that gravity is unaffected.

The full spectrum fits, so atomic group averaging again gives a physical root space without polar filtering. Its dimension is

    K (N+1) 2^(8m)

before optional zero-energy purifiers/references. Each energy determines its scalar momentum via epsilon_0(p)=E, with norm weight 1/|epsilon_0'(p)| before rescaling. The physical source/B/register input is a root product with the gravitational correlations required by the constraint; no independent geometric product is assumed.

These are finite but sometimes enormous conditional resources. No large matrix is allocated by the verifier. The new gravitational window is not a passive clock change or an observed cosmology. At a fixed window one cannot send reference energy or number of systems to infinity without rechecking the spectrum.

## 9. Three certified reuse budgets

Each S has the same fixed gap 0.2; the same reservoir is used throughout each run.

| Readouts m | Reservoir top N | Completed joint error: lower witness | Completed joint error: upper bound | Clock/source positions K | Complete operation upper bound |
|---:|---:|---:|---:|---:|---:|
| 2 | 128 | 0.00061660 | 0.0061354 | 32768 | 0.0073107 |
| 4 | 512 | 0.00015342 | 0.0015219 | 131072 | 0.0020310 |
| 8 | 2048 | 0.000038070 | 0.00037672 | 524288 | 0.00061269 |

The corresponding windows are [65536,131072], [262144,524288] and [1048576,2097152]. For the eight-readout device the mean reference energy is 204.8, its mean depletion on all-ground inputs is 0.8, and its final marginal fidelity against the initial reference is approximately 0.99995713. Its small disturbance by that one statistic does not erase the computed joint errors or correlations.

The lower witnesses concern a particular entangled input, while the upper bounds apply to every joint S/reference input. They are not competing numerical estimates of an exactly optimized diamond norm. The clock samples from the earlier small devices are not used as proof for these much larger programs; the general analytic finite-chain bound is evaluated with the new L,K and window.

## 10. Verification and the next direct time task

Run:

    python verification/reused_reference_clock.py
    python -m verification.reused_reference_clock

The verifier writes [reused_reference_clock.json](verification/reused_reference_clock.json). It propagates the shared reservoir through actual sequential finite-ladder Kraus operators, not fresh one-use channels. Exhaustive two- and three-system tests check 576 guarded matrix-unit/outcome cases against the exact joint formula, trace preservation, GHZ parity witnesses and two-system error correlations. A further 64 cases test the unguarded boundary counterexample. Updated reservoir density matrices are checked after every use against the derived binomial mixture, mean/variance, fidelity and unchanged marginal coherence. Three larger analytic resource witnesses recompute program length, clock window, source budget and 36 selected gravitational inverse cases. Those witnesses are bound evaluations, not dense multi-system simulations or interval certificates.

**Supplied:** a finite, non-reset shared reference; a complete joint instrument and exact state updates; explicit correlated errors and a joint entangled-input accuracy theorem; finite boundary/exhaustion effects and a mechanism-specific energy-capacity bound; one autonomous finite source program; and all added matter in the gravitational spectral constraint.

**Still open:** optimized or adaptive lifetimes, reference pumping/reset and its source, a Hamiltonian for external extraction, noise, initial resource preparation, gravitational locality/domain justification, and phenomenal constitution. The result is not an indefinitely catalytic clock, a uniform-time prior, or a completed theory of time.

An [explicit finite pump construction](FINITE_REFERENCE_PUMP.md) now supplies energy-conserving exchanges within the source-clock constraint. A full exchange restores the working packet and transfers the used state and all old correlations into a counted finite pump; a partial exchange can restore energy while leaving memory and introducing phase bias. Complete multi-block instruments and pump/source/gravitational budgets are supplied. This is unitary state transport from a finite precharged source, not a discarded-state replacement or a regenerated coherence cycle; source quality, initial pump preparation and reuse/regeneration remain open.
