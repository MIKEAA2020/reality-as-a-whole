# Sequential interventions and persistent records in a constrained history

## 1. What is now constructed

[Relational time](RELATIONAL_TIME_CONSTRUCTION.md) supplied changing clock-conditioned states and constraint-commuting observables. Here that construction is extended to arbitrary finite sequences of recorded interventions, including measurement back-action and classical feedback.

The output is not merely a list of one-time expectations:

    finite inner instruments and blank memories
      -> explicit unitary recording interactions
      -> one coherent zero-constraint history
      -> commuting relational record projectors
      -> sequential Born probabilities and selective updates.

We also prove persistence, prefix normalization, invariance of event predictions under clock-edge refinement, and independence from unused unitary-completion choices in the forward recording protocol. A worked example distinguishes forgetting an outcome, omitting an intervention, reversing the coupling, transferring a record, and coherently erasing which-outcome information.

The unitary dilation and instrument rules are established quantum measurement mathematics. The contribution is an explicit integration with the constrained algebraic framework, its stated generality, and exact reproducible examples. It is not a derivation of the Born rule, unique outcome selection, consciousness, or fundamental time.

Code: [relational_records.py](verification/relational_records.py). Results: [relational_records.json](verification/relational_records.json).

## 2. Instruments without a finite global density matrix

Let A be a unital C*-algebra with state omega. A finite inner instrument is specified by elements K_(a,mu) in A satisfying

    sum_(a,mu) K_(a,mu)^* K_(a,mu) = I.

Here a is the recorded outcome; mu is a possible internal Kraus refinement. In Heisenberg form,

    I_a^*(b) = sum_mu K_(a,mu)^* b K_(a,mu).

Its probability is omega(I_a^*(I)). Given a nonzero probability, the updated state is

    omega_a(b) = omega(I_a^*(b)) / omega(I_a^*(I)).

This does not assume a trace or a density matrix for A. It does assume a finite inner Kraus representation; arbitrary CP maps on an arbitrary C*-algebra have not been identified with this subclass. Finite matrix examples are included, and the construction also applies to such instruments in the preceding infinite quasi-local algebra.

## 3. A specified unitary completion, not an unspecified apparatus

Let L be the number of pairs (a,mu). Stack the Kraus elements into a column V in M_(L,1)(A). Then V^*V=I. Adjoin a pointer with a distinct blank state and L written states. On blank plus written sectors define

    U_V = [[0, V^*],
           [V, I - V V^*]].

Every entry belongs to A. Direct multiplication gives

    U_V^*=U_V,   U_V^2=I.

Indeed VV^* is a projection, V^*(I-VV^*)=0, and (I-VV^*)V=0. Thus no choice of orthogonal complement or square root is needed. On an input with blank pointer,

    psi tensor |blank> -> sum_(a,mu) K_(a,mu) psi tensor |a,mu>,

in Hilbert-space notation. The block formula itself is algebraic and remains valid without assuming a finite-dimensional system Hilbert space.

For outcome a let Q_a be the sum of the written pointer projectors labelled (a,mu). Include the blank projector to obtain a complete pointer PVM. It has zero probability after this write interaction on a blank input.

Other unitary extensions agreeing on the blank-input subspace produce the same forward recording process if every next pointer is fresh and later gates use only the specified reachable actions. This is proved inductively: the prepared state enters each interaction in its blank-input subspace. It is not a claim of equivalence for arbitrary later operations exploring unused completion sectors.

The formula fixes a completion for a specified Kraus family, not for a CP instrument with all coherent implementation information erased. Section 9 makes this distinction explicit.

## 4. Arbitrarily many steps, including feedback

At step j the Kraus family may depend on previous recorded outcomes h=(a_1,...,a_(j-1)):

    sum_(a_j,mu_j) K_(a_j,mu_j|h)^* K_(a_j,mu_j|h) = I.

Intervening unitaries can be absorbed into these operators. At each finite step pad the finitely many history-dependent families with zero operators to a common outcome/refinement label set, so the controlled operators act on one fixed pointer space. Keep old pointers, append a fresh blank pointer, and control the corresponding U_V by the orthogonal projectors for h. On unused old-memory configurations an identity action can complete the control. These controlled operators are unitary and commute with every previously written coarse-outcome projector.

For alpha=(a_1,...,a_n) and mu=(mu_1,...,mu_n), put

    B_(alpha,mu) = K_(a_n,mu_n|alpha_<n) ... K_(a_1,mu_1).

The final coherent recorded state has these branch amplitudes in the tensor product of pointer spaces. Orthogonality of the full written labels yields

    p(alpha) = sum_mu omega(B_(alpha,mu)^* B_(alpha,mu)),
    omega_alpha(b) = sum_mu omega(B_(alpha,mu)^* b B_(alpha,mu)) / p(alpha).

This is precisely the sequential instrument rule, including disturbance and feedback. It follows from the one unitary recording network, rather than adding independent collapse events to the history.

**Normalization proof.** Sum over the last outcome and refinement. Completeness replaces sum K_n^*K_n by I on each prefix. Repeat until the result is omega(I)=1. The same argument gives

    sum_(future suffixes) p(prefix,suffix) = p(prefix).

Consequently later trace-preserving choices cannot alter the unconditioned distribution of a retained prefix record under the stated nondemolition architecture. Conditioning on selected later outcomes can change a retrodictive distribution; that is not a violation of this prefix identity.

Fresh memories and the stipulated feedback architecture are supplied assumptions. Reusing unmodelled environments can invalidate an instrument description based only on the visible prefix.

## 5. One constrained history and its record observables

Let B be the enlarged algebra of system and all pointers, initially in state eta = omega tensor blank-pointer states. Let P_t be the cumulative unitary through clock reading t. Define edge transports U_t=P_(t+1)P_t^* and the positive propagation constraint C from the previous construction.

The one history state is

    eta_hat(|t><s| tensor b) = eta(P_t^* b P_s)/M.

It is positive, normalized, and zero-constraint. All interactions, settings, and blank resources belong to this enlarged internal description; no external observer acting on an absolute is assumed.

At the final clock reading f, let Q_alpha be the product of the different-pointer outcome projectors. Define the relational record operator

    R_f(Q_alpha) = diag_t(P_t P_f^* Q_alpha P_f P_t^*).

Because R_f is a unital *-homomorphism,

    [C,R_f(Q_alpha)]=0,
    R_f(Q_alpha) R_f(Q_beta)=0 for distinct complete records,
    eta_hat(R_f(Q_alpha)) = eta(P_f^* Q_alpha P_f) = p(alpha).

Thus all joint outcome probabilities have constraint-commuting representatives. Selective system updates are obtained by including b together with the final record projector and normalizing; system and pointer observables commute before pulling them back.

Written-record projectors need not sum to the identity on unprepared blank/invalid memory sectors. Include the corresponding additional projector for a complete PVM. Its probability is zero in the prepared post-write state. No normalization on arbitrary unprepared memory states is silently assumed.

This closes the previous construction's sequential-instrument gap for the stated class. It does not explain why one particular outcome is experienced or select a phenomenal incidence law.

## 6. Persistence is a theorem with a physical condition

Suppose Q records an event at reading t_0, and all subsequent gates commute with Q. Then for t>=t_0,

    P_t^* Q P_t = P_(t_0)^* Q P_(t_0),
    R_t(Q) = R_(t_0)(Q).

**Proof.** Write P_t=U_(t-1)...U_(t_0) P_(t_0). Every later unitary cancels against its adjoint across Q. The second identity follows from the definition of R_t.

Feedback controlled by a record satisfies this nondemolition condition: control can change the system without changing the controlling label. It need not preserve all off-diagonal pointer observables.

Persistence is not asserted before writing. A current record of an event is not the event itself, and the formula does not make an event occur earlier. Erasure, overwriting, or coherent mixing of labels can violate the commutation premise. If a record moves to a new carrier, the appropriate transported record observable must be followed instead of continuing to inspect the reset carrier.

## 7. A precise clock-refinement invariance

Subdivide an edge U into V_k ... V_1=U, identifying the original event readings in the refined clock. At those readings cumulative P_t, and hence root effects P_t^* Q P_t, remain unchanged. Therefore every associated conditional record probability is unchanged.

In a Hilbert-space presentation let J and J' encode the old and new histories. The map J'J^* is unitary **between their physical kernel subspaces** and intertwines the corresponding event observables restricted to those subspaces. Both restrictions pull back to the same root operator P_t^* Q P_t.

This is not equality of the full kinematic clock models. With uniform parallel-section amplitudes, clock weights are 1/M and 1/M' and generally differ. Nor is it a theorem for arbitrary noncommuting choices of physical clock. What is invariant is the event experiment under subdivision that preserves its ordered couplings and record identification.

The code checks a nontrivial factorization R=(R X)X, not just idle padding.

## 8. Exact recorded experiment

Take a qubit in state (3|0>+4|1>)/5. Write its Z outcome into a fresh ternary pointer with labels blank,0,1. Apply

    R = [[3/5,-4/5],[4/5,3/5]]

to the system, then write a second Z outcome into a second pointer. Both writes are the explicit canonical completion from section 3, with the ordering of system/pointer tensor factors adjusted accordingly.

The joint recorded probabilities are

                    second 0      second 1
    first 0          81/625        144/625
    first 1         256/625        144/625.

The code derives the table twice: by sequential Kraus products and by the full coherent recording circuit. Relational record operators commute with C and give the same table in the stationary history.

Forgetting the first outcome gives second-outcome probabilities

    (337/625, 288/625).

Omitting the first interaction gives instead

    (49/625, 576/625).

Thus summing over a real intervention is not equivalent to removing it. The difference is the instrument's disturbance, not merely bookkeeping.

For feedback, apply R only when the first outcome is 0. The joint table becomes

    [[81/625,144/625], [0,16/25]].

Both protocols have first-record distribution (9/25,16/25), as the prefix theorem requires. The executable also checks a nonprojective amplitude-damping instrument and exact within-outcome Kraus changes.

### Direct continuation of the AKLT input

For the earlier four-site AKLT ring, measure the Cartesian basis of the first qutrit, apply the same x-z rotation used in the clock construction, and measure that qutrit again. Direct contraction of the original integer-coefficient ground vector gives

    p(a,b) = [[3/25, 0,   16/75],
              [0,    1/3, 0    ],
              [16/75,0,   3/25 ]].

The state change also steers the adjacent qutrit conditionally: immediately after first outcome a, its Cartesian-basis probabilities are 3/7 for the matching label and 2/7 for either other label. Averaging a restores I_3/3. These conditional states are calculated from the previously determined ground state, not supplied as a new phenomenal or experimental table. The same record-dilation and relational-observable theorems apply.

## 9. Coarse-graining, erasure, and the information an instrument omits

**Coarse-graining.** Not reading the first pointer retains its physical interaction. Summing its orthogonal branches removes interference from the visible system distribution. It does not replace sum K_a rho K_a^* by (sum K_a) rho (sum K_a)^*.

**Transfer/reset.** Swap the first pointer with a fresh blank environment. The visible pointer is reset, but the original joint distribution is now carried by the environment and second pointer. Its effect on the unconditioned second statistics remains. This is a unitary transfer of information, not annihilation of a record.

**Uncomputation.** Reversing the first write before the later system gate restores the unmeasured input if no other carrier retains its label. If a copy remains in an environment, undoing only the visible pointer does not restore the system interference. The code checks both cases.

**Coherent eraser.** Read the first written-label subspace in the +/- basis instead of its Z-label basis. For the specified positive-phase recording implementation,

    p(+,second 0)=49/1250,
    p(+,second 1)=576/1250,
    p(+)=1/2.

Conditioned on +, the second distribution is the unmeasured one. Summing both eraser outcomes leaves the disturbed marginal (337/625,288/625). No unconditional recovery or backwards signalling is asserted. The +/- projectors do not commute with the original label projectors, so these are not additional jointly available classical facts about the same pointer.

**Instrument versus coherent implementation.** Replace K_1 by -K_1 in the first instrument. Each CP outcome map, every Z-record probability, and every subsequent record-diagonal feedback prediction stays unchanged. But the same fixed + eraser readout now gives

    p(+,second 0)=1/2,   p(+,second 1)=0.

An instrument therefore fixes the classical-record operational process, not every possible cross-outcome interference experiment. Such experiments require coherent implementation data. Transforming both dilation and readout together can be a change of presentation; changing the interaction while holding the eraser observable fixed can describe a genuinely different experiment.

This distinction prevents the construction from claiming more determination than its premises supply. Unit-completion freedom on unused sectors, within-outcome Kraus presentation freedom, and physically anchored cross-outcome phases are not interchangeable.

## 10. Position reached

We now have a general finite-inner-instrument construction of sequential Born weights, state updates, feedback, persistent internal records, constraint-commuting joint record observables, and a precisely delimited clock-refinement invariance. It is a continuation of the general C*-algebra framework, not an assumption that all systems have finite global density matrices.

What remains supplied includes the system algebra and state, instrument families, coherent implementations where tested, initial blank resources, clock graph, and record identification. The construction does not derive a fundamental arrow from reversible dynamics, arbitrary clock equivalence, gravitational constraints, a selected measurement outcome, qualitative identity, or absolute perfection. Operational probabilities are derived within quantum theory, not an explanation of why the entire quantum constitution is necessary.

This is work within M0 and W1-W6. It replaces the previous single-time limitation with a checked multi-time intervention model without changing the experiential and axiological completion requirements.
