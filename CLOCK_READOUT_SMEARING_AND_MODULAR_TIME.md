# Same modular flow, different clock records

**Result.** In one specified three-level constrained history, a sharp clock and a noisy clock POVM have the **same unconditional Gibbs system state and modular flow**, but different clock-conditioned system records and entropies. The difference is not removable for all physical input states by a stochastic relabelling of the noisy clock outcome alone, even though the classical mixing matrix is algebraically invertible. A pure cyclic relabelling of the sharp clock is an exact equivalence control. This is a controlled calculation about readout resolution, not evidence that two gravitational reference frames or their algebras are inequivalent.

The calculation also compares two declared Lüders instruments. Their nonselective operations disturb the kinematical constraint by different amounts; another instrument with the **same noisy POVM** has a different poststate. These are finite-model disturbance diagnostics, **not gravitational backreaction**. The original stationary constraint and readout measurement are supplied, not dynamically derived. In particular, the readout operations do not preserve the constraint sector, so the kinematical postmeasurement states must not be presented as physical states of a closed constrained universe.

Numerical receipt: [JSON](verification/clock_smearing_modular_comparison.json); [calculation](verification/clock_smearing_modular_comparison.py), [eight tests](verification/clock_smearing_modular_comparison_test.py). The identities below are analytic; floating-point tests check examples. The model reuses [the Gibbs relational clock](RELATIONAL_MODULAR_CLOCK.md) and complements [the ideal-frame equivalence and filter examples](CLOCK_CHOICE_EQUIVALENCE.md). It addresses a finite-resolution version of the proposed comparison in the [Lighthouse assessment](LIGHTHOUSE_V22_COMPARATIVE_ASSESSMENT.md), not its gravitational completion.

## 1. One constrained history and two physical POVMs

Let C and S both be `C³`, with clock basis `|j>`, system Hamiltonian `H=diag(0,1,2)`, and

    t_j=2*pi*j/3,   U_j=exp(-i H t_j),   U_(j+3)=U_j.
    J phi = (1/sqrt(3)) sum_j |j> tensor U_j phi.
    D_j x = x_(j+1) - U_1 x_j,  j=0,1;  C = sum_j D_j^* D_j.

`J` is an isometry and `C J=0`; the kernel is its image. `j` is a supplied cyclic label, not a globally monotone clock. The common physical initial state is `J|psi>`, where

    p_n = exp(-n)/Z,  |psi> = sum_n sqrt(p_n)|n>,  rho_j=U_j|psi><psi|U_j^*.

The unconditional system state is `tau=diag(p_0,p_1,p_2)` by the three-point phase average. `tau` is faithful and Gibbs at beta 1. Using `sigma_s^tau(A)=tau^(is) A tau^(-is)` and `alpha_t(A)=exp(iHt) A exp(-iHt)`, the pre-existing identity is `sigma_s^tau=alpha_(-s)`. This has a specified sign and scale; the clock does not derive either.

The first instrument reads sharp projectors `P_j=|j><j|`. The second reads the three-outcome POVM, with indices modulo 3,

    E_j = (1-e) P_j + e P_(j-1),   0<=e<=1.

Use the Lüders Kraus operator `K_j=sqrt(E_j)` for the second; sharp readout uses `P_j`. For the main comparison set `e=1/4`. Operationally, `E_j` has the same outcome statistics as a sharp reading whose label is shifted forward with probability `e`, but the Lüders postmeasurement state is generally **not** the poststate of sharp measurement followed by a noisy label. No assumptions about a local detector, clock Hamiltonian, or an interaction implementing these Kraus operators are supplied.

## 2. Common events and probability distributions

Use the same system yes/no projector in both protocols:

    B=|psi><psi|,    B_yes=B,  B_no=I-B.

At outcome `j`, clock first and then system `B` has root-sector effects

    F_(j,b) = J^*(P_j tensor B_b) J
    G_(j,b) = J^*(E_j tensor B_b) J
            = (1-e) F_(j,b) + e F_(j-1,b).

The system and clock factors commute; these formulas are valid for **every input density on the physical/root sector**, and both families are normalized POVMs. The operators `J F_(j,b) J^*` and `J G_(j,b) J^*`, extended by zero on the constraint complement, commute with C. They represent the same declared clock/system correlations in the physical sector; this construction of effects does not turn the chosen kinematical measurement update into a constraint-preserving instrument. We compare the fixed system operator B at each reported clock label, not the differently transported frame observables whose equality is the separate ideal-frame statement in [CLOCK_CHOICE_EQUIVALENCE.md](CLOCK_CHOICE_EQUIVALENCE.md).

For the specified `|psi>`, let

    f = |<psi|U_1|psi>|² = (3 sum_n p_n² - 1)/2 = 0.2658145868... .

All clock label probabilities are `1/3` in either protocol. Sharp conditional states are `rho_j`; noisy conditional states are

    rho'_j=(1-e)rho_j+e rho_(j-1).

The joint probabilities, in rows j=0,1,2 and columns yes/no, are approximately:

| Clock | j=0 | j=1 | j=2 |
|---|---|---|---|
| Sharp | (0.333333, 0) | (0.088605, 0.244728) | (0.088605, 0.244728) |
| Noisy, e=1/4 | (0.272151, 0.061182) | (0.149787, 0.183546) | (0.088605, 0.244728) |

Thus `Pr(B=yes | j=0)` is 1 for sharp readout and `(1-e)+e f = 0.8164536467...` for the noisy instrument. Both are valid predictions of the same model; the discrepancy is a changed measurement, not a contradiction.

## 3. Equivalence and the limits of recovery

A **cyclic relabelling** of the sharp measurement is equivalent: use `Q_j=P_(j-1)`, undo the known label shift and all joint effects, state updates and distributions agree. This is deliberately a simple control, not a claim that any two independently realized clocks are equivalent.

For `e=1/4`, noisy effects are the sharp family postprocessed by `M=(3/4)I+(1/4)T`, where `T` shifts clock labels forward and `T³=I`. Algebraically,

    M^(-1) = (9 I - 3 T + T²)/7.

It contains negative entries, so is not a classical stochastic channel. For the **joint events** this cannot be sidestepped by a different stochastic relabelling that works for every physical input: the three `F_(j,yes)=(1/3) U_j^* B U_j` are linearly independent. Their Hilbert–Schmidt Gram matrix has diagonal `1/9`, off-diagonal `f/9`, and positive eigenvalues `(1+2f)/9,(1-f)/9,(1-f)/9`. Consequently equality of all recovered yes effects uniquely forces the negative inverse above.

This does not say the bare clock marginals alone distinguish the protocols: they are uniformly distributed for **every** physical input in this history embedding. Nor does it forbid quasiprobability/unbiased statistical reconstruction with sampling cost, a recovery using extra system information, probabilistic quantum reversal, or a different apparatus. It only rules out deterministic state-independent classical relabelling of the noisy clock outcome alone reproducing the declared sharp *joint effects* for all inputs. The finite sample values above do not by themselves prove this all-state claim; the effect linear-independence argument does.

## 4. Conditional entropy versus unchanged modular state

The sharp conditional system states are pure. Each noisy conditional system state has nonzero eigenvalues

    lambda_± = [1 ± sqrt(1 - 4 e(1-e)(1-f))]/2.

At `e=1/4`, its von Neumann entropy is `0.4475898662` nats; the sharp value is zero. Averaging over the three outcomes gives `tau` in both cases, whose entropy is `0.8323955818` nats. The corresponding Holevo quantities `S(tau) - sum_j p(j) S(rho_j)` are `0.8323955818` nats sharp and `0.3848057157` nats noisy. These describe the declared classical-record/system ensemble, not generalized gravitational entropy or a measured accessible information value.

Because cyclic smearing is covariant, `rho'_j=U_j rho'_0 U_j^*`: the noisy states still follow the **same** relational unitary sequence from a different, mixed initial conditional state. The Gibbs marginal `tau` and its modular automorphisms also stay exactly the same. Hence same flow does not by itself fix finite-resolution conditional predictions. Conversely, different conditional entropies here do not show that the underlying modular flow has changed. The sharp conditional states have rank one and the noisy ones rank two in this three-dimensional model; neither is faithful on the full matrix algebra, and neither is silently substituted for the faithful modular reference `tau`.

## 5. What the chosen interventions disturb

For the nonselective Lüders instrument, the clock off-diagonal blocks are multiplied by `kappa=sqrt(e(1-e))`; the sharp measurement gives `kappa=0`. A direct sum of the two edge contributions yields

    Tr(C rho_before)=0,
    Tr(C rho_sharp_after)=4/3,
    Tr(C rho_noisy_after)=(4/3)[1-sqrt(e(1-e))]=0.7559830641...  (e=1/4).

These numbers use the explicit graph constraint above, not a physical energy, Hamiltonian cost, or quantitative gravitational backreaction. Nonselective clock operations leave the reduced system marginal `tau` unchanged, as no-signalling requires; they can still alter global clock–system coherence and leave the kernel of C. This violation is why interpreting the kinematical poststates as closed-universe physical histories would be invalid.

The same noisy effects can instead be implemented by the two Kraus operators per reported outcome `sqrt(1-e) P_j` and `sqrt(e) P_(j-1)`—sharp measurement followed by classical label noise. Its nonselective poststate is the sharp dephased state, with `Tr(C rho_after)=4/3`, not the Lüders value above. It yields the same joint clock/system probabilities and conditional system states, but a different global poststate. Effects alone do not specify backaction.

## 6. Implications and open gates

This result tightens the claim that a state-defined modular flow determines time: even granting a Gibbs reference and exact flow match, the operational record depends on a specified clock POVM and instrument. It does not select a unique state or clock, prove that the noisy and sharp clocks are different physical reference frames, establish a physical arrow, or establish a type-II crossed-product entropy effect. Nor does it test the local ideal-dust detector; that instrument is a separate quantization and was not transferred to this qutrit model. The full B7 local-time/spacetime/gravity derivation, backreaction, clock implementation, and the experiential bridge remain open.

A substantive next step is to construct a **constraint-compatible readout coupling**, with a finite clock and detector defined inside one model, and calculate its resource cost and postselection as well as the corresponding conditional distributions. To make this a gravity result requires explicit local gravitational observables, common regulated algebra, physically selected states and a justified comparison of genuinely different clocks—not merely replacing a POVM in an externally given finite history.
