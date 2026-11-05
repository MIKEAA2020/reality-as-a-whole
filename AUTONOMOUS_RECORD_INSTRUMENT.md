# Autonomous finite-time detector–memory registration

## 1. The milestone supplied

The previous [energy-exchange clock](ENERGY_EXCHANGE_CLOCK.md) derived a physical clock–pointer instrument in asymptotic scattering. The [classical tick bridge](CLASSICAL_TICK_READOUT.md) identified the missing detector/memory layer but stipulated its observation channel. Here we supply a **single time-independent, bounded-below Hamiltonian** whose finite-time evolution approximates a detector–memory recording instrument, with an explicit uniform bound.

The construction includes a finite environment initially thermal for a degenerate Hamiltonian. Its reduction gives decoherence of the record without assuming a dissipative readout channel. An exact reuse example shows why the same environment cannot simply be treated as fresh at each use.

**What is new within this programme:** autonomous spatial ordering of three noncommuting interactions; finite-time rather than asymptotic passage; a derived redundant record channel; an explicit finite retention-window bound; and an environment-correlation/reuse ledger. The transport/Duhamel and controlled-gate mathematics are standard, not claimed as new general theorems of measurement physics.

This is the **first milestone**, not the entire proposed clock–detector–bath programme. It does not derive a calibrated jump process, a macroscopic mixing reservoir, a cyclic heat engine or a gravitational constraint algebra. The Hamiltonian and initial resources are specified, not derived from a complete constitution of reality.

This is a new finite-time model and packet preparation, not a serial composition with the earlier scattering example. Its bound is derived below; the old numerical scattering bound must not be transplanted to this different preparation.

Code: [autonomous_record.py](verification/autonomous_record.py). Results: [autonomous_record.json](verification/autonomous_record.json).

## 2. One physical Hamiltonian, three fixed interaction regions

Use hbar=1, a massive clock coordinate X on R with P=-i d/dx, and four internal qubits: measured system S, detector D, memory M and environment E. Define

    B_AB = P1_A tensor (I-X_B)/2,     P1_A=(I-Z_A)/2.

Each B_AB is an orthogonal projector, hence positive with norm one. Use three successive pairs

    B_1=B_SD,  B_2=B_DM,  B_3=B_ME.

They need not commute: B_SD and B_DM do not. Tensor identities on other qubits are implicit.

For length ell and gap d>=0, put the interaction intervals at

    [0,ell], [ell+d,2ell+d], [2ell+2d,3ell+2d].

In interval j with left endpoint x_j define

    kappa_j(x) = (2 pi/ell) sin^2(pi(x-x_j)/ell),

and zero outside it. The profiles and their first derivatives vanish at the edges. Their integrals are pi. Set

    K(x)=sum_j kappa_j(x) B_j,
    H = P^2/(2m) + H_S + v K(X),
    H_S=omega X_S,   m>0, v>0, omega>=0.

D, M and E have zero bare free Hamiltonians. H_S does not commute with the measured Z observable or with the first interaction. The profiles are fixed in space; **no coupling is switched by an external clock**. Engineering these controlled spatial interactions remains an assumption, not a material-device derivation or a relativistically local field theory.

Since K is bounded and positive, H is self-adjoint on H2(R) tensor C16 and

    H >= -omega.

The physical clock has quadratic kinetic energy, not a linear unbounded-below spectrum. All finite-time reflection, recoil, spreading and negative-momentum components are included in the actual H evolution. We do not discard them or replace that evolution by a prescribed classical trajectory.

The incoming clock is independent of the system, detector, memory and any reference:

    f_p0(x)=exp(i p0 x) f(x),   p0=m v,
    f(x)=2/sqrt(3a) cos^2(pi(x+2a)/(2a)) on [-3a,-a],

and zero otherwise. f is normalized and belongs to H2, including at the edges. Its exact derivative norms are

    ||f'|| = pi/(sqrt(3) a),
    ||f''|| = pi^2/(sqrt(3) a^2).

Its mean clock momentum is p0, and mean kinetic energy is

    p0^2/(2m) + ||f'||^2/(2m).

The ready resources are `|0>_D |0>_M` and

    tau_E=I_E/2.

The latter is a thermal state of H_E=0 at any positive temperature. D and M are **prepared pure blank registers**, not thermal equilibrium registers supplied for free.

## 3. Exact ordered reference evolution—only a proof tool

Boost by exp(i p0 X) and subtract the irrelevant carrier energy. The physical Hamiltonian becomes

    H_boost = vP + P^2/(2m) + H_S + vK(X).

Compare it with the auxiliary transport Hamiltonian

    H_ref=vP+vK(X).

H_ref is self-adjoint but not bounded below. It is **not** the proposed physical clock or a replacement physical postulate. Its exact solution allows a controlled finite-time comparison with H_boost.

If y=x-vt, reference evolution is

    psi_ref(t,x)=f(y) W(x,y) chi,
    W(x,y)=path-ordered exp[-i integral_y^x K(u) du].

Every occupied starting point y lies to the left of all interactions. After the complete packet has passed all three regions, the Wilson product is independent of y:

    U_rec = exp(-i pi B_ME) exp(-i pi B_DM) exp(-i pi B_SD)
          = CNOT_ME CNOT_DM CNOT_SD.

The equality follows from B being a projector: exp(-i pi B)=I-2B. Thus it is derived from the spatial Hamiltonian profiles, not inserted as a sequence of externally timed gates.

The last region ends at L_end=3ell+2d. Choose

    D_travel=3ell+2d+4a,    T=D_travel/v.

At T even the left edge of the reference packet is at L_end+a. The clock factor is then a translated packet, independent of the internal state, and the internal factor has undergone U_rec.

## 4. Derivation of the record channel

For a system matrix unit |s><t|, copying S into D and D into M gives

    |s,s,s><t,t,t| on S,D,M.

The third controlled interaction contributes an environment factor

    X_E^s tau_E X_E^t.

Its trace is delta_st, because Tr(tau_E X_E)=0. Therefore tracing E gives exactly the channel

    L(rho_S) = sum_z P_z rho_S P_z tensor |z,z><z,z|_DM.

The formula also holds with any untouched entangled reference R, replacing rho_S by rho_SR and the projectors by P_z tensor I_R. Reading M in its Z basis yields the Lüders instrument

    L_z(rho_S)=P_z rho_S P_z,

with redundant agreeing detector and memory labels. This is a derivation of an **operational recording instrument within quantum mechanics**, not an additional collapse postulate or an explanation of why a record is experienced.

The maximally mixed environment has not become an independently readable copy of z: its marginal is unchanged. It supplies phase randomization and acquires correlations in the coherent-input case. The detector and memory—not the environment marginal—carry the accessible outcome labels.

## 5. Uniform finite-time bound for the actual physical Hamiltonian

On the occupied reference support, the initial endpoint is outside the interaction regions. Differentiating the ordered exponential gives

    partial_x W = -i K(x) W,
    partial_x^2 W = [-i K'(x)-K(x)^2] W.

These identities do not require the different B_j to commute. Put

    k = sup_x ||K(x)|| <= 2 pi/ell,
    k' = sup_x ||K'(x)|| <= 2 pi^2/ell^2,
    C = ||f''|| + 2k ||f'|| + k' + k^2
      = pi^2/(sqrt(3)a^2)
        + 4pi^2/(sqrt(3)a ell) + 6pi^2/ell^2.

For every internal vector chi, including any reference/environment purification,

    ||P^2 psi_ref(t)|| <= C.

Duhamel's formula compares H_boost with H_ref on this H2 trajectory:

    ||psi_actual(T)-psi_ref(T)||
       <= integral_0^T [||P^2 psi_ref(t)||/(2m)+||H_S psi_ref(t)||] dt
       <= T [C/(2m)+omega]
       =: delta_write.

The estimate is uniform over the system/reference input and includes the physical clock output. It compares the measured Z observable with its value at the initial preparation epoch: free S motion during the passage contributes the explicit omega*T term. It does not silently identify different measurement epochs.

Purify any mixed input and tau_E. Pure-state trace distance is at most the vector difference; tracing out clock/environment and reading the register are contractions. Consequently,

    (1/2)||I_actual(T)-L||_diamond <= min(1,delta_write).

I_actual is obtained from the specified Hamiltonian and ready states; the classical M label is attached by its final computational-basis readout. The finite-time bound certifies this derived instrument, rather than assuming a classical misclassification channel. It does not bound arbitrary unbounded-observable moments by trace distance.

### Finite retention window

After T, let the reference packet keep translating freely, and let S evolve with its actual H_S. D and M remain unchanged. On this reference trajectory K=0; its only residual against physical evolution is P^2/(2m). Thus for a hold interval h>=0,

    delta_hold(h) = delta_write + h ||f''||/(2m).

The full channel at T+h is within min(1,delta_hold) of

    (exp(-i H_S h) tensor I_DM) L(rho)
        (exp(i H_S h) tensor I_DM).

This time-dependent reference comparison is a proof device, not switching of the physical apparatus. The stored labels refer to the initial Z event; they need not agree with a later measurement of the freely evolving S.

This supplies an actual **finite retention-window guarantee**. It is conservative: it also penalizes harmless clock spreading. It is not an infinite-time stability theorem or a latch protected against arbitrary environmental perturbations.

### Position-confirmed readout and failure events

Let Pi_out select X>=L_end+a/2. At T+h the reference packet is entirely in this outgoing region and the ideal record has D=M. Therefore, by projecting the vector difference,

    Pr_actual(not outgoing) <= min(1,delta_hold^2),
    Pr_actual(D != M)       <= min(1,delta_hold^2).

The complete instrument including the position-success/failure flag is still within min(1,delta_hold) in half-diamond distance of its ideal version. If the outgoing event is selected and its probability is nonzero, the normalized conditional state differs from the ideal state by at most

    min(1, delta_hold + sqrt(Pr(not outgoing))) <= min(1,2 delta_hold).

This is a state-distance statement for a normalized conditional output, **not** a diamond norm for a nonlinear normalization map. Small disagreement does not alone establish correct Born probabilities: the full instrument bound supplies that separate guarantee.

The outgoing-region check is made at a finite readout epoch. It is not a first-arrival measurement, nor a proof that every clock-position conditioning is equivalent to every auxiliary-time conditioning.

## 6. Finite examples and controlled resource limit

Take omega=0.1, hold h=1, and scale

    m=lambda^3,  v=100,
    a=10/lambda, ell=20/lambda, d=10/lambda.

The mean velocity stays fixed; increasing lambda grows the mass and shrinks the packet and apparatus. Let D_0=120, C_0 and fpp_0 denote the travel distance and derivative constants at lambda=1. Then

| lambda | Passage T | Write bound | Bound after hold h=1 | Carrier kinetic energy |
|---:|---:|---:|---:|---:|
| 1 | 1.2 | 0.3113944 | 0.3398855 | 5,000 |
| 10 | 0.12 | 0.01391395 | 0.01676306 | 5,000,000 |
| 100 | 0.012 | 0.001219140 | **0.001504051** | 5,000,000,000 |
| 1000 | 0.0012 | 0.000120192 | **0.000148683** | 5,000,000,000,000 |

All values are dimensionless model evaluations, **not** double-dot or cold-atom calibration and not interval-rounded numerical certificates. The exact displayed formulas, rather than numerical PDE sampling, provide the bounds.

Along this family,

    delta_hold = D_0 C_0/(200 lambda^2)
                 + [D_0 omega/100 + h fpp_0/2]/lambda -> 0.

A controlled finite-time instrument/retention limit is therefore supplied. Its resources grow: mass=lambda^3, p0=100lambda^3, kinetic carrier energy=5000lambda^3, and peak coupling=200pi lambda/20; packet and device lengths shrink as 1/lambda. This is a fixed-speed nonrelativistic model limit, not a claim that the assumed materials or coupling law remain realizable at arbitrary masses or arbitrarily small lengths. No fixed-energy ideal clock or unlimited storage has been obtained. Fixed m and arbitrarily large v alone do not eliminate this conservative fixed-hold spreading term.

For lambda=100, the complete record error after the stated hold is below 0.001505 in half-diamond convention; outgoing-region failure and D/M disagreement are each bounded by about 2.27e-6. These are guarantees for the specified closed model and prepared resources, not experimentally established device error rates.

## 7. Thermodynamics and the finite-environment reuse obstruction

The full physical evolution is unitary and conserves its time-independent total energy. Since H_E=0, the environment's **bare heat exchange is exactly zero** in this idealized model. This does not imply cost-free cyclic measurement, zero entropy production in every subsystem convention, or permanently irreversible records.

For an initially pure system with outcome probability p, the ideal reduced S,D,M state has entropy k_B H(p). E remains maximally mixed. The global entropy is unchanged, and mutual information k_B H(p) between S,D,M and E accounts for the reduced entropy increase. More generally, for initial rho_S,

    Delta S_SDM/k_B = H(p)-S(rho_S) = C_Z(rho_S),

where S is in nats and C_Z is relative entropy of coherence in the measured basis. In the ideal collision description this is also the entropy production attributed to discarding access to the initially uncorrelated thermal E: it is correlation production, **not reservoir heat**. The finite-error physical state admits a controlled entropy estimate too. Let W denote the working degrees of freedom **clock,S,D,M**. Every term of the physical Hamiltonian commutes with X_E. With E initially I/2, actual evolution is an equal mixture of two conditional unitaries on W; the environment marginal remains I/2 exactly. Thus

    Sigma_actual/k_B := Delta S_W/k_B + Q_to_E/(k_B T)
                      = Delta S_W/k_B
                      = I(W:E) in nats,
    0 <= Sigma_actual/k_B <= ln(2).

This is the exact initially-product thermal-environment information identity, not a steady-state heat-current estimate. It need not be monotone in time for a finite correlated environment. Bare E heat is zero; changes of interaction energy must still be included in a complete energy ledger.

For an arbitrary qubit rho_S the initial working state has rank at most two; its actual output, a mixture of two unitary images, has rank at most four. The ideal working output has rank at most two. Their joint support therefore has dimension at most six, despite the clock's infinite-dimensional Hilbert space. Entropy continuity on that support gives, whenever delta_hold<=1/2,

    |Sigma_actual/k_B - C_Z(rho_S)|
        <= h_2(delta_hold) + delta_hold ln(5),

where h_2 uses natural logarithms. This follows from the full-output trace-distance bound, not from a claim that trace distance alone controls entropy on arbitrary infinite-dimensional states. For the lambda=100 example the deviation bound is below 0.01370 nats. For a pure balanced input, Sigma_actual/k_B is consequently between ln(2)-0.01370 and ln(2), even though the bare environment heat is zero. For an already Z-diagonal input the ideal C_Z is zero. Neither result is a universal positive entropy cost for every record or an efficiency comparison with the double-dot sensor.

D and M each have entropy H(p), but their **joint** entropy is H(p), not 2H(p): they store the same bit. A degenerate-memory reset at temperature T, without accessible side information, has the ideal reversible-limit joint bound k_B*T*H(p). Access to correlated S or other retained information changes that task. One cannot charge two independent-bit Landauer costs, nor claim that pure ready registers and preserved outcome records are restored for free in a complete cycle.

### Exact reuse witness

Take a memory initially |+> and E initially I/2. Apply CNOT_ME and discard access to E. The memory becomes I/2. But if the **same correlated E** is kept and the same collision is applied a second time,

    CNOT_ME^2=I,

so the memory returns to |+>. With an independent fresh E for the second collision it remains I/2. The two final memory states have trace distance 1/2.

Thus an unchanged thermal marginal of E is **not** evidence that the environment is ready for independent reuse. Its correlations matter. A macroscopic reservoir, fresh ancillas, decorrelation mechanism or a reuse-aware dynamical analysis is needed to justify repeated Markovian readout. The present finite environment has no claim to infinite append-only irreversibility. This is consistent with the qualifications in the Wadhia audit, not an experimentally calibrated alternative to that sensor.

## 8. Direct connection to relational time

The actual autonomous H admits the same auxiliary-history constraint presentation already developed in the programme,

    C_aux = P_T + H,
    Psi(t)=exp(-itH) psi_initial.

The sum is self-adjoint on its maximal joint-spectral domain. These histories are generalized solutions, not normalizable states with a uniform time prior. With the standard history/rigging physical inner product, finite-time conditional predictions at the auxiliary slice T=t are those derived above. The interaction order itself is supplied by the internal clock coordinate X and fixed spatial regions, not externally prescribed coupling times. Position-confirmed outgoing records have explicit success and error bounds.

This gives a controlled physical record model inside the relational-history framework; it does **not** derive a normalizable uniform time prior, turn quadratic X motion into a globally monotone clock, or establish gravitational refoliation. The initial packet/ready-state event anchors the predictions. Eliminating the remaining auxiliary readout slice through a fully derived internal first-arrival instrument is an additional task, not silently assumed here.

## 9. Verification and remaining tasks

The standard-library verifier checks positive projector generators, the exact three gate exponentials and ordering, all four system matrix units of the reduced channel, an explicit Bell-entangled reference input, the finite-environment reuse witness, resource formulas and the analytic scaling identity. The rigorous estimates are the derivations above; no physical Schrödinger PDE simulation or empirical sensor reproduction is claimed.

Next substantive obligations are:

1. Derive a controlled multi-event observation process, including missed/false events, from an explicit extended detector/reservoir model.
2. Establish reset, finite-memory capacity, retention against specified perturbations and sustained-use error/entropy budgets without replacing correlated resources by fresh ones without accounting.
3. Derive an internally triggered first-arrival readout and compare matched-event clock descriptions.
4. Continue toward genuine gravitational constraints; no laboratory-clock construction substitutes for the refoliation problem.

The gain is a finite-time recording instrument derived from an autonomous bounded-below Hamiltonian, with explicit passage/retention errors and a concrete reuse obstruction. It is neither a complete autonomous timekeeping apparatus nor the complete physical–phenomenal constitution.

**Multi-event continuation:** [The one-clock record tape](AUTONOMOUS_RECORD_TAPE.md) now supplies a finite discrete observation sequence, derived write-angle errors and a global bound with explicit initial tape resources. It does not replace the outstanding continuous-time reservoir limit, reset engine or internal first-arrival problem.
