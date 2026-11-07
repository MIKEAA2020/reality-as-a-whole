# One physical clock, a finite noisy record tape

## 1. Advance and scope

The [one-event autonomous recorder](AUTONOMOUS_RECORD_INSTRUMENT.md) is extended to **n observations driven by one initially prepared clock packet**, not n separately reset clocks. All interactions and all tape cells are specified in one bounded-below, time-independent Hamiltonian. Imperfect memory-writing angles derive a calibrated noisy instrument. The ideal reference process has an explicit hidden-state Markov law; a single global estimate bounds the actual physical tape instrument, including entangled reference inputs.

This supplies a **finite, discrete multi-event observation model** and a physical-versus-observation-error separation. It does not derive a continuous-time jump limit or the double-dot rates. A false negative here means a wrong binary flag at an observation site, not a physical transition missed between sites. The bare autonomous Hamiltonian, preparation and coupling calibration remain assumed effective physics, not a complete constitution of reality.

Code: [autonomous_record_tape.py](verification/autonomous_record_tape.py). Results: [autonomous_record_tape.json](verification/autonomous_record_tape.json).

## 2. One Hamiltonian and explicit finite resources

Use S and a continuous massive clock X,P, with n initially blank detector qubits D_j, n initially blank memory qubits M_j and n environment qubits E_j initially in the product state I/2^n. Each environment qubit has zero free Hamiltonian. The bare detector/memory Hamiltonians are zero. Let H_S=omega X_S.

The same prepared compact-position clock packet and spatial bump shapes as in the one-event report are used. Every spatial interval has length ell and successive intervals have gap d. A profile with area A is

    kappa_A(x)=(2A/ell) sin^2(pi(x-x_left)/ell)

inside its interval and zero outside. All A below lie in [0,pi]. For an observation stage j, four successive regions implement the following positive-projector interactions:

| Region | Projector B | Profile area A |
|---|---|---:|
| Background memory rotation | (I-X_Mj)/2 | 2 gamma |
| System-to-detector copy | P1_S (I-X_Dj)/2 | pi |
| Imperfect detector-to-memory write | P1_Dj (I-X_Mj)/2 | beta=pi-2 epsilon |
| Memory/environment coupling | P1_Mj (I-X_Ej)/2 | pi |

Here 0<=gamma,epsilon<=pi/2. Between consecutive stages insert one system-rotation region with projector `(I+X_S)/2` and area `2 alpha`, with 0<=alpha<=pi/2. Its reference unitary is, up to an irrelevant scalar phase,

    R_alpha=exp(-i alpha X_S).

These are fixed spatial interactions, not gates switched by a laboratory clock. For n stages there are

    r=5n-1 regions,
    K_n(x)=sum_regions kappa_A(x) B_region,
    H_n=P^2/(2m)+omega X_S+vK_n(X).

Every B is positive, so H_n is self-adjoint on H2 with the finite internal space and is bounded below by -omega. The physical system undergoes the entire H_n evolution; no intermediate clock measurement, clock reset, bath refresh or register reinitialization is inserted.

All fresh cells are prepared at the beginning and counted: n detector blanks, n memory blanks, n independent thermal environment bits. The tape is exhausted after n sites. This is finite resource expenditure, not indefinite reuse or an unaccounted supply of fresh bath bits.

## 3. Derive the faulty observation channel

In the exact transport reference, the system copy records z in D_j. Conditional on z, the two memory rotations commute and add. Acting on its blank state, the memory undergoes

    V_z=exp[-i(2 gamma+z beta)(I-X_M)/2].

Coupling M to E and tracing E dephases M in the Z basis. **Tracing the used detector D as well** removes cross terms between different z. The resulting system-plus-memory channel is

    J(rho)=sum_{r,z} R(r|z) P_z rho P_z tensor |r><r|,

where

    R(1|z)=sin^2(gamma+z beta/2),
    R(0|z)=cos^2(gamma+z beta/2).

Consequently,

    false positive: R(1|0)=sin^2(gamma),
    false negative: R(0|1)=sin^2(gamma-epsilon).

This is a **derived noisy instrument**, not a classical noise channel appended by assumption. The memory-only output is classical in the reference model. Discarding detector access is part of the specified output channel: the detector still exists physically and is not reset or deleted. With imperfect writing, retaining the full coherent detector output is a different channel and must not be silently replaced by J.

The discarded detector carries the exact Z label at the reference-copy stage. It is therefore an explicit information sink/resource in this construction. The environment is not the sole source of reduced-state decoherence. This is not a nondisturbing noisy observation of an otherwise untouched system: even a missed flag accompanies a projective Z disturbance because the detector obtained the information.

The derivation holds on every system matrix unit, hence also with an arbitrary untouched entangled reference. It is not inferred merely from testing two classical input states.

## 4. A derived hidden Markov law for the whole tape

Used D_j,E_j never interact again. They can be traced immediately in the mathematical reduction without changing later reduced predictions. The exact reference channel is therefore

    J_n o R_alpha o J_(n-1) o ... o R_alpha o J_1,

with each J writing its own retained memory slot. This reduction does not mean that a physical discard/reset operation is performed between sites.

Let z_j denote the hidden Z outcome and r_j the observed memory flag. Then

    P(z_next|z)=cos^2(alpha) if z_next=z,
                sin^2(alpha) otherwise,

and

    Pr(r_1,...,r_n)
      =sum_[z_1,...,z_n] p(z_1)
         product_[j=2..n] P(z_j|z_(j-1))
         product_[j=1..n] R(r_j|z_j),

where p(z_1)=Tr(P_z1 rho_S). Coherent initial S inputs are included; their initial Z coherences are removed by the first actual detector interaction in the reference model.

For alpha=pi/6, the hidden flip probability is 1/4. Repeated identical hidden labels are genuine repeated observations, not necessarily additional transitions. A transition from 0 to 1 between sites must not be confused with the state flag z=1 at a site.

This is an exact finite hidden-state model **for the derived reference output**. It does not prove that arbitrary weak-measurement records are classical Markov chains. Here the rank-one Z disturbance and discarded detector labels make that reduction possible. Nor does it establish a continuous-time autonomous jump process: the intersite rotation is a specified spatial Hamiltonian interaction, and the sites provide a finite observation schedule.

## 5. One global physical-clock bound, not per-step clock replacement

Because only one profile is active at each x,

    sup ||K_n|| <= 2pi/ell,
    sup ||K_n'|| <= 2pi^2/ell^2.

These bounds do not grow with the number of internal qubits or the number of already traversed regions. The ordered-exponential endpoint derivative used in the one-event proof remains valid for arbitrarily many noncommuting regions. With

    C=pi^2/(sqrt(3)a^2)+4pi^2/(sqrt(3)a ell)+6pi^2/ell^2,
    D_n=r ell+(r-1)d+4a,
    T_n=D_n/v,

the single Duhamel comparison on the entire physical trajectory gives

    delta_n=T_n [C/(2m)+omega] + h ||f''||/(2m).

The holding interval h starts after the whole reference packet has passed the last region. With S allowed to evolve freely during h, trace out the physical clock and used detectors/environments. The actual complete S-plus-memory tape instrument obeys

    (1/2)||I_physical - I_noisy_reference||_diamond <= min(1,delta_n).

This includes arbitrary entangled inputs and correlations across all retained memory slots. The actual output need not be exactly a hidden Markov distribution; **every full-tape event probability** differs from the specified reference distribution by at most delta_n. No clock/environment independence is re-assumed halfway through the proof. Recoil, reflection and spreading are in the physical H_n; the transport Hamiltonian is only the comparison tool.

As before, an outgoing-position check made at the stated epoch has failure probability at most min(1,delta_n^2), because the ideal packet lies entirely beyond the device. This is not an internally triggered first-arrival detector. The finite-time slice has not been eliminated.

## 6. Separate observation faults from physical implementation error

Let

    q=max[sin^2(gamma), sin^2(gamma-epsilon)].

The one-stage instrument differs from the perfectly labelled Z instrument in half-diamond distance by at most q. A hybrid composition argument, retaining earlier memory slots and reference systems, gives

    (1/2)||I_noisy_reference - I_perfect_reference||_diamond <= min(1,nq),
    (1/2)||I_physical - I_perfect_reference||_diamond <= min(1,delta_n+nq).

Within the reference hidden-state model the probability of at least one wrong flag is also at most min(1,nq), without assuming independent hidden outcomes. Observation errors are conditionally independent given the hidden path because the cells are prepared independently; hidden outcomes themselves are correlated.

The two budgets must remain separate. Improving the mass/localization implementation does not remove a fixed systematic write-angle error. Accurate classical eigenstate calibration alone would not establish a correct quantum instrument; the full local channel derivation supplies the disturbance information as well.

## 7. Finite resource examples

Keep omega=0.1, h=1, and scale

    m=lambda^3, v=100,
    a=10/lambda, ell=20/lambda, d=10/lambda.

Mean speed remains fixed. Let C_0 and fpp_0 be the derivative constants at lambda=1. Then D_n=150n/lambda and

    delta_n=150n C_0/(200lambda^2)
             +[150n omega/100+h fpp_0/2]/lambda.

For gamma=0.05, epsilon=0.15 the false-positive rate is about 0.002498 and false-negative rate about 0.009967.

| n | lambda | Physical vs derived noisy tape bound | Physical vs perfectly labelled tape bound |
|---:|---:|---:|---:|
| 1 | 100 | 0.001809 | 0.011776 |
| 4 | 100 | 0.006381 | 0.046248 |
| 8 | 100 | 0.012477 | 0.092210 |
| 16 | 100 | 0.024668 | 0.184136 |

For **eight events**, lambda=1000 and improved angle calibration gamma=0.005, epsilon=0.015 give

    physical vs noisy tape <= 0.001230406,
    physical vs perfect tape <= 0.002030379.

These are full-tape uniform instrument/event bounds, not per-event error rates or measured hardware statistics. All numbers are dimensionless, from analytical formulas evaluated in floating point, not interval certificates or physical PDE simulations. The latter example uses m=10^9 and carrier kinetic energy 5*10^12 in model units. Its large prepared resources cannot be omitted.

At fixed n,h the bound tends to zero as lambda grows, provided observation-angle errors also shrink if convergence to the perfectly labelled instrument is desired. At fixed lambda, increasing n grows the physical bound and exhausts more tape cells. There is no unlimited-memory or fixed-resource ideal-clock conclusion.

### A constructive sufficient design for any finite tape length

Write the physical bound as

    delta_n=A n/lambda^2+(B n+C_h)/lambda,
    A=150 C_0/200, B=150 omega/100, C_h=h fpp_0/2.

For any n>=1 and desired total error 0<eta<1, choose

    lambda >= max[1, sqrt(4An/eta), 4(Bn+C_h)/eta],
    gamma=sqrt(eta/(8n)), epsilon=3 gamma.

Then each term of delta_n is at most eta/4, while
`q=sin^2(2gamma)<=4gamma^2=eta/(2n)`. Hence the full physical tape instrument is within eta of the perfectly labelled reference instrument. An integer ceiling for lambda is sufficient. This is a constructive finite-horizon resource prescription, not just a table or an assumption that per-step errors remain unchanged after reuse.

For fixed hold and nonzero omega, this sufficient prescription has lambda=O(n/eta), mass/kinetic energy O((n/eta)^3), n memory blanks, n detector blanks and n thermal cells, with increasingly tight write-angle calibration. The verifier checks nine such designs, including 100 records at a requested 1% full-tape error. The growing resources and shrinking spatial scales preclude a fixed-resource indefinite-use conclusion; arbitrary hardware realizability is not established.

## 8. Record entropy and environmental correlations

### Joint record information is not one independent bit per slot

In the perfect observation limit, with unbiased first outcome and hidden flip probability p_flip, the classical path entropy is

    H(Z_1,...,Z_n)=ln(2)+(n-1)h_2(p_flip).

For n=8, alpha=pi/6 this is 4.629493193 nats, below 8ln(2)=5.545177444. Detector and memory tapes duplicate that same path in this perfect limit; their joint entropy is not twice its path entropy. Ideal reversible-limit reset bounds must use the actual joint record and the stipulated available side information, not simply count register labels. A resetting Hamiltonian, work storage and a finite-rate reset cost are **not supplied** here.

### An unchanged bath marginal still does not license reuse

Every physical term commutes with every X_Ej. With the environment initially I/2^n, its full joint marginal stays I/2^n. The working state W=(clock,S,all D,all M) is a mixture of 2^n conditional unitary evolutions. The exact initially-product thermal-environment information identity gives

    Q_bare_environment=0,
    Sigma/k_B=Delta S_W/k_B=I(W:E_all) in nats <= n ln(2).

This is a finite information-capacity statement, not a positive heat-current cost or a steady-state reservoir limit. The environment may be correlated with W despite retaining its initial joint marginal. Prepared pure detector/memory blanks are additional resources. The observed channel traces detectors too; any entropy budget for that further loss of access must account for them and their correlations.

Reusing one phase environment instead of independent ones dephases only the parity of a general memory string. Its overlap factor for histories r,r' is

    Tr[tau X^(sum_j r_j-sum_j r'_j)]
       =1 for equal parity, 0 for opposite parity.

Thus coherence between 00 and 11 can survive; fresh independent phase environments remove it. This is an obstruction to replacing a general **full-register dephasing channel** by a one-bit bath, not a universal lower bound of one thermal qubit per observed classical flag. In particular, computational-basis outcome probabilities can agree even when register coherences differ, and in the perfect-copy case discarded detectors already dephase the retained observable channel. The n thermal bits used here are sufficient counted resources, not proved necessary for every observation architecture.

## 9. Relational-time connection, verification and next target

The model embeds in the same auxiliary-history constraint C=P_T+H_n on its maximal joint-spectral domain. Generalized histories yield the finite-slice predictions above. The clock's own coordinate supplies all interaction ordering. The global tape bound therefore strengthens the autonomous physical-record part of the relational-time programme, without claiming that an auxiliary time slice has become an internal first-arrival event or that the constraint is gravitational.

The verifier independently derives each local reduced channel from its 16-dimensional unitary on all four system matrix units for four calibration cases. It compares **1,530 complete sequence probabilities** through eight stages using instrument recursion versus explicit hidden-path summation, checks normalization and the exact path entropy, and evaluates the global bounds. The derivative/Duhamel proof—not numerical sampling of a trajectory—justifies the physical bound.

The next direct time task is to replace the remaining finite-slice interrogation by an internally triggered detection event with controlled backaction and a complete no-click/click instrument. Multi-event tape resources are now explicit; a continuous-time reservoir limit, robust storage/reset and gravitational refoliation remain unsupplied. No classical record or dissipative budget is identified with phenomenal occurrence or the complete absolute constitution by these results.

**Internal event-readout continuation:** [The autonomous stop clock](AUTONOMOUS_STOP_CLOCK.md) supplies a separately derived complete scattering instrument and conserved outgoing time-record effects. It is a stopped/sojourn-clock model, not yet the finite-time first-click instrument or a combined proof for this tape. The two preparations and their error bounds must not be combined without deriving the joint device.
