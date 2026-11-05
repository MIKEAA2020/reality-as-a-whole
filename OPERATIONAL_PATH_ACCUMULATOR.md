# An operational quantum path accumulator and a clock-conversion instrument

## 1. Result and relation to the experiment

The [five-trace cold-atom comparison](COLD_ATOM_CLOCK_COMPARISON.md) computed a cumulative path reading retrospectively. Here we supply a **reversible online update law** for such a register, then derive an explicit first-arrival clock instrument. This closes the missing update-law step in a specified discrete model; it does not derive the cold-atom apparatus or its entropy clock.

The construction gives:

- a unitary, motion-controlled counter update with no supplied numerical trajectory;
- a positive counter-rate operator even though position can return;
- a stationary constrained-history presentation with positive integer-group rigging;
- a completely positive conversion from an initial preparation to a counter-triggered event, including arrival index and overshoot;
- an exact example in which this **specified measured/coarse-grained conversion** identifies orthogonal input states, while its coherent record dilation preserves them;
- an exact completed internal clock T=(q+3*a)/4 and coherent uncomputation of redundant arrival labels;
- an equal-speed control where the counter event is just a fixed-update event;
- reversible arithmetic replay and finite-register requirements on all 272 experimental observations.

The main gain is that a clock change is no longer an unspecified substitution of scalar labels. We can compute its detector effects, required records and observable probabilities. This is an established quantum-walk/instrument/group-averaging construction applied to our particular time target, not a claim of a new general quantum-gravity theorem.

Verification: [operational_accumulator.py](verification/operational_accumulator.py), [exact output](verification/operational_accumulator.json). All finite amplitudes, effects and probabilities use rational arithmetic. Infinite-space statements below are analytic arguments, not inferred from finite tests.

## 2. A reversible accumulator gate

For position-bin inputs x,y and an integer accumulator a define

    G|x,y,a> = |x,y,a+|y-x|>.

It is unitary: the inverse subtracts the same quantity while retaining both inputs. On a finite counter Z_K, addition/subtraction is modulo K and the same formula is an exact permutation unitary:

    G = sum_(x,y) |x,y><x,y| tensor X_K^(|y-x|).

This is not an irreversible overwrite of the old position. A sensor/comparison implementation must retain, reversibly uncompute, or explicitly dispose of the necessary inputs. Controlled arithmetic on orthogonal position-bin states is allowed; it does not copy an arbitrary unknown quantum state without entangling it.

Feeding G a table in laboratory order verifies arithmetic, **not** an autonomous physical clock. We therefore next supply a motion law in which the displacement information is generated internally by the same reversible update.

## 3. Time-homogeneous quantum engine

Take

    H_E = l2(Z_q) tensor C2_d tensor l2(Z_a),
    C = [[3/5,-4/5],[4/5,3/5]],
    delta_0=+1, delta_1=-2,
    S|q,d,a> = |q+delta_d,d,a+|delta_d|>,
    U=S(I tensor C tensor I).

The coin rotation C is unitary. S is a bijection of the complete basis, with inverse subtracting the displacement and its magnitude. Therefore U is unitary on the full infinite lattice, including its negative-counter sector. Preparing a=0 selects the forward positive-counter cone; a unilateral nonnegative shift alone would not be unitary.

U is the **same** update at every iteration. It does not consult a list of future positions or a table of externally chosen clock increments. Each basis history adds its traveled distance. In a coherent superposition the accumulator is a quantum register correlated with histories, not proof of an unmeasured definite classical trajectory.

For example, displacements +1,+1,-2 return q to its starting point but increase a by 4. Position recurrence and accumulator recurrence are different.

Let A be multiplication by a. On finite-support vectors,

    U* A U - A = I_q tensor R tensor I_a,
    R = C* diag(1,2) C = (1/25)[[41,12],[12,34]].

R has eigenvalues 1 and 2. Thus the expectation increment lies between 1 and 2, and a state starting at a=0 has counter support within [n,2n] after n updates. These statements do not make all multi-time quantum readings jointly classical or noninvasive.

There is an important **clock-completion identity**, not to be hidden:

    T=(Q_position+3*A)/4,   U* T U=T+I.

Indeed delta_d+3*|delta_d|=4 for both displacements. From the specified q=a=0 preparation, T reads exactly n on the whole coherent state. The pair (q,a) therefore contains an ideal discrete clock even though a alone advances at a state-dependent rate. This is a special consequence of our engineered displacement law and unbounded registers, not a universal discovery of time or a property derived from the cold-atom tables.

**Autonomy scope:** this is an autonomous discrete update law. We have not derived a local time-independent Hamiltonian, a physical engine supplying the update, its preparation, or the complete self-scheduling detector/storage hardware. Merely taking a logarithm of U would not establish such an implementation.

## 4. Stationary constrained history and physical measure

The iteration index need not be interpreted as an additional measured absolute time. On

    H_kin = l2(Z_n) tensor H_E,
    (Wf)_n = U f_(n-1),

impose the first-order unitary constraint W Psi=Psi. Formal solutions are Psi_n=U^n psi. They are not normalizable in the n factor unless zero; use finite-n-support test sequences and the rigging map

    eta(f)=sum_n U^(-n) f_n.

For the discrete group generated by W,

    sum_(k in Z) <f,W^k g> = <eta(f),eta(g)>.

The sum is finite on these test sequences because their n supports are finite. It is positive and eta(Wf)=eta(f). It is onto H_E by f_0=psi, so quotienting its null space and completing gives H_phys=H_E. There is no assumed normal uniform prior on Z.

For any bounded physical effect E on H_E,

    (R(E)f)_n = U^n E U^(-n) f_n

commutes with W and satisfies eta R(E)=E eta. Preparation-sector detector effects below can therefore be represented as Dirac effects. Embedding an effect on the q=0,a=0 preparation sector gives effects summing to its preparation projector; an extra “outside preparation” outcome completes the full effect family if desired.

A positive expression 2I-W-W* may be written down, but its full formal distributional kernel is **not** being equated with this first-order physical space. Generalized solutions such as n U^n psi illustrate the extra-mode issue. The first-order constraint and specified rigging remain binding.

This removes a normalizable external n-clock assumption from the history description. It does not derive U, select a unique clock, or reproduce the gravitational constraint algebra.

## 5. An operational counter event, not a coordinate substitution

Prepare q=0,a=0 with an arbitrary coin input; let J0 embed that two-dimensional input into H_E. Choose an integer threshold B>=1. Set

    Q = projector onto a<B,
    P_r = projector onto a=B+r,  r in {0,1},
    K_(n,r) = P_r U (Q U)^(n-1) J0.

This defines a monitored first-crossing instrument. It records the first update n that crosses the threshold and the overshoot r. Overshoot matters: a two-unit jump can skip an exact clock value. Necessarily ceil(B/2)<=n<=B.

The effects telescope:

    sum_(n=1..B,r) K_(n,r)* K_(n,r)
      = I - J0* [(Q U)^B]* (Q U)^B J0 = I.

The surviving term vanishes because each update advances the counter by at least one. Thus

    Phi_B(rho)=sum_(n,r) K_(n,r) rho K_(n,r)*

is completely positive and trace preserving. The coherent record map

    V_B psi=sum_(n,r) |n,r> tensor K_(n,r) psi

is an isometry. For an isometry V, an explicit self-adjoint unitary on input-plus-output sectors is

    D = [[0,V*],[V,I-VV*]],   D*=D, D^2=I.

It maps (psi,0) to (0,V psi). The threshold-2 example has a three-row rational V and an exactly checked five-dimensional D. This supplies a coherent converter gate, not a proof that an irreversible absorbing halt rule is itself unitary. The protocol specifies stopping-time outputs; delivery/storage at a common later engine reading is additional controlled dynamics. No unnoticed comparison between states at different delivery times is intended.

Monitoring/recording this event is a physical instrument, not automatically the statistics of an undisturbed trajectory. If a clock can stall, the finite termination proof fails; a finite-horizon instrument must then include a no-arrival outcome. This qualification matters for the actual finite-resolution tables below.

## 6. Exact clock conversion at threshold B=2

Write <c_d| for row d of C. The three nonzero Kraus maps are

    K_(1,0)=|-2,1,2> (4/5,3/5),
    K_(2,0)=| 2,0,2> (9/25,-12/25),
    K_(2,1)=|-1,1,3> (12/25,-16/25).

Their effects sum exactly to I_2. For initial coin |0>, the arrival probabilities are

| First update n | Overshoot r | Probability |
|---:|---:|---:|
| 1 | 0 | 16/25 |
| 2 | 0 | 81/625 |
| 2 | 1 | 144/625 |

Writing f1,f2,f3 for the three displayed output basis states, the channel is explicitly measure-and-prepare:

    Phi_2(rho)=p1 |f1><f1| + p0 [(9/25)|f2><f2|+(16/25)|f3><f3|],
    pd=<c_d|rho|c_d>.

The reduced output purity for initial |0> is 187297/390625, below one. More strongly, the orthogonal input rays

    chi_+ = C* (|0>+|1>)/sqrt(2),
    chi_- = C* (|0>-|1>)/sqrt(2)

have identical outputs under Phi_2. Consequently no state-independent reversible/unitary identification represents this **reduced instrument channel** on the entire input space.

The coherent V_2 keeps the two outputs orthogonal and pure. Keeping the arrival values only as a **dephased classical record** does not recover the lost relative phase: every individual branch here is rank one and already identifies these rays. Quantum-coherent record retention and merely writing down classical outcomes are different resources.

### Reversible clock completion, not unavoidable information loss

Here the arrival label is actually redundant with the coherent outgoing q/a registers:

    n=(q+3*a)/4,   r=a-B.

Thus an undephased arrival record can be uncomputed by controlled subtraction using q,a. On this prepared support the branch outputs are orthogonal, so the coherent sum

    V_tilde_B=sum_(n,r) K_(n,r),   V_tilde_B* V_tilde_B=I

is itself an isometry into the engine output, without an extra retained arrival register. The verifier checks this through threshold 8. The five-dimensional D above realizes the threshold-2 three-row coherent converter, with output sectors identified with the three outgoing basis states. Its inverse recovers the coin input on the encoded range.

This supplies an explicit reversible completion of the clock conversion. The information loss in Phi_B is the consequence of the **specified which-arrival measurement/dephasing**, not a theorem that the counter description intrinsically destroys information. Once the record has actually decohered into inaccessible degrees of freedom, subtracting its classical value is not quantum erasure and cannot restore the phase.

This does not prove that all counter-clock formulations are intrinsically nonunitary. Alternative covariant readouts or physical inner products are different constructions; our [interacting-rate model](INTERACTING_CLOCK_RATE.md) explicitly retains its derived flux metric. Here the chosen detector and its coarse-graining are stated, not silently substituted for an ideal change of frame.

### Matched versus mismatched events

Let an additional detector read coin b at arrival. Its preparation-space effect is

    E_(n,r,b)=K_(n,r)* P_b K_(n,r).

Computing it from engine-indexed threshold histories or from the arrival instrument gives the same joint probabilities; the verifier checks them exactly. These are the **same anchored events**, with the Dirac representation in section 4.

By contrast, “coin 1 at update 2” and “coin 1 when threshold 2 first fires” are different events. For initial |0>,

    p(coin 1 at fixed update 2) = 288/625,
    p(coin 1 at first threshold-2 crossing) = 544/625.

This difference is not a clock-choice inconsistency. It is the consequence of changing the detector event. A genuine conversion must transport the event definition, including its trigger and records, not just replace n by B in a formula.

## 7. Equal-speed control and physical backaction

Replace the displacements by +1,-1. The counter then advances exactly one at every update, factors as |a=n>, and threshold B has only (n=B,r=0). On the full q/coin system the counter conversion is the ordinary unitary B-step walk. Restricted to the chosen q=0 preparation it is an isometry. Thus the loss above is not inevitable merely because position turns.

The variable-speed counter is also not a cost-free relabeling of an unrecorded walk. After one update from |q=0,d=0,a=0>, tracing out a gives q/coin purity 337/625 instead of the unrecorded pure walk's purity one. Implementing the register entangles it with motion. A retrospective path calculation and an online quantum counter can therefore have different retained observable algebras and backaction.

## 8. Applying the reversible arithmetic to the five actual traces

Use exactly archived positions in micrometers, not the two-displacement motion model. At resolution epsilon define q_i=floor(phi_i/epsilon), then replay the same G gate with those adjacent bins. Counter subtraction reverses every update. No experimental motion law is fitted or claimed.

For a run with final integer counter M, a nonwrapping counter needs M+1 states; a binary register needs ceil(log2(M+1)) bits. This is the counter alone, excluding sensors, input retention, comparators, work and timing hardware. The exact script checks 0.1, 0.5 and 1 micrometer resolutions and the bound

    |L_epsilon-L_sampled| <= (number_of_observations-1)*epsilon.

Each displacement error is less than epsilon because both floor residuals lie in [0,epsilon).

At **1 micrometer resolution**:

| Trace | Final path-counter units | Counter bits for this observed run | Adjacent pairs with no counter advance |
|---|---:|---:|---:|
| V0 | 140 | 8 | 5 |
| V03 | 143 | 8 | 6 |
| V06 | 141 | 8 | 10 |
| V09 | 50 | 6 | 31 |
| V1 | 20 | 5 | 33 |

At 0.1 micrometers the stall counts are 0,0,2,6,8 respectively. These are central-value arithmetic results, not resolution- or noise-certified physical clock performance.

**Important consequence:** a finite-resolution path-only clock does not resolve every supplied event. Even the smallest reported bin size leaves stalls in three traces. Adding one per engine update would resolve them in the model, but would define a different clock and require an actual internal update event. We do not smuggle the laboratory index into the path reading to eliminate this problem.

The earlier five-label/three-bit conditional bound concerns a different task: extra labels for width prediction from a coarse position bin. It is not this accumulator's storage cost.

For the autonomous model, a K-state modular counter initially at zero avoids wrap for all histories through N updates iff K>=2N+1. All two-unit histories make the worst-case bound necessary. Unlimited unit-resolution advance cannot fit in a bounded-range register: the positive increment inequality would iterate past its upper bound. The infinite register is a supplied idealization; finite runs have explicit finite capacities.

## 9. What has advanced, and what remains

We have supplied the missing **reversible counter rule**, its constrained-history embedding, and an explicit event-conversion instrument rather than simply assuming a clock-frame unitary. We can now state exactly when classical arrival conditioning loses information, when coherent records preserve it, when equal-rate reduction is unitary, and where finite resolution prevents a clock from resolving all events.

[The finite-mass Hamiltonian detector](HAMILTONIAN_CLOCK_DETECTOR.md) now supplies a continuous-time, bounded-below alternative with real reflection/backaction and a quantitative ideal-instrument bound. It is not a Hamiltonian implementation of this particular discrete walk, nor a finite-time first-arrival storage mechanism.

For the cold-atom system, the remaining physical task is to derive and calibrate an admissible accumulator/detector from its actual variables and couplings, including stalling, noise, backaction and image-derived ensemble inputs. The completed clock T uses the specified two-displacement engine law; applying it to unrelated measured displacements would not reproduce its identity. This walk does not reconstruct the paper's whole-cloud entropy, validate its effective Hamiltonian, or implement its atom cloud. Those are not consequences of reversible arithmetic.

The construction remains direct M0/W1-W6 problem-of-time work. It does not settle refoliation, gravitational constraints, phenomenal passage, the Gamma/chi constitution law or necessary actuality. The motion/update law, preparation and record architecture are specified premises, not a zero-residue derivation of them.
