# A universal subject without a God's-eye ledger: the comparison gate

## The result

A universal subject's **limited knowledge alone** does not evade Local Friendliness. If the friend has a single absolute outcome, later readouts track it, and the relevant Local Agency conditions hold, the contradiction applies even if the universal subject does not know that outcome. To take the relational route seriously, the framework must give up or modify the **single absolute friend-event assumption**, not just say the universal subject is ignorant of an event that is nevertheless absolute. Alternatively it can retain absolute events and revise Local Agency or another premise. The theorem does not force one particular choice.

A precise finite test makes the cost of the single-event option visible. For the project's existing ideal one-friend circuit with `S=14/5`, suppose a single binary friend-event `c` is present in a joint distribution with Alice's and Bob's outcomes. If Alice's read disagrees with `c` with probability at most `e` for either of Bob's settings, and the joint `(b,c)` distribution is independent of Alice's setting, then

    TV[P(a,c | x=2,y=1), P(a,c | x=2,y=2)] >= 2/5 - 2e.

Total variation is nonnegative, so the bound is informative for `e<1/5`. In this circuit **full Local Agency** requires the left side to vanish: with that and the other stipulated conditions, `e>=1/5`. We give exact probability tables achieving equality for all `0<=e<=1/5`. This is a sharp mathematical gate on this toy circuit—not an observed rate, proof of conscious friends, or physical theory of hidden experiences.

The general relaxed Local Friendliness inequality is known, including its `4e` form: see [Laux and Cavalcanti (2026)](https://arxiv.org/html/2609.12527) and the sources cited there. The specific tradeoff and rational saturation here are an application to the **already specified project circuit**, not a claim to have discovered the underlying no-go theorem. Our prior [subject-identity gate](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) supplied the zero-error endpoint and the underlying quantum circuit.

## 1. Which universal-subject claim is being tested?

We distinguish four proposals.

1. **Ignorance of absolute events.** There is one absolute friend-event `c` whether or not the universal subject accesses it. Ignorance changes neither its existence nor the probability constraints. This does not by itself avoid the theorem.
2. **Real relational experience.** A friend experiences a definite outcome relative to an appropriate experiential/physical context, but the account does not assert that all such outcomes form one absolute joint event assignment. The experienced episode is not declared an illusion. This rejects or changes the relevant absoluteness premise, but requires an explicit law and account of comparison.
3. **Absolute event plus a different physical premise.** There is an absolute `c`, but a concrete physical theory rejects a relevant Local Agency condition or another premise. A violation of a hidden-joint independence condition is not automatically a controllable signal. A probability table by itself does not give a relativistic, causal, or dynamical completion.
4. **No recognized friend event.** The model does not treat the supposed system as having a thought or experience in the relevant circumstances. That is a different move, especially for a human-level observer, and it cannot be assumed merely because the model is difficult.

A non-perfect or non-omniscient universal subject is compatible with any of these in principle; those traits alone select none of them. The target is still a genuine, agentive whole-level subject and genuine finite subjects, not merely a formal collection.

## 2. The shared circuit and assumptions

The [existing circuit](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) prepares the Bell state on qubits A and B, lets a memory M coherently record A, and has Alice either read M (`x=1`) or reverse that interaction and measure an incompatible observable (`x=2`). Bob measures one of two observables (`y=1,2`). Outcomes `a,b,c` are ±1. The observed quantum correlations in the ideal model are

| | Bob y=1 | Bob y=2 |
|---|---:|---:|
| Alice read x=1 | 3/5 | 3/5 |
| Alice reverse x=2 | 4/5 | −4/5 |

The local means vanish, and `S=E11+E12+E21−E22=14/5`. The qubit memory is **not** an established thinking or experiencing friend. The calculations are a test of conditional assumptions applied to this circuit; they do not show the human-scale experiment has been performed.

For each actually chosen `x,y` suppose there is a joint distribution `P(a,b,c|x,y)`, where `c` denotes the **same proposed absolute friend-event** and not a label selected after `a` is known. Make these assumptions:

- `P(a != c | x=1,y) <= e` for each y, the read-agreement condition allowing mismatch. This concerns the readout's agreement with the proposed friend-event, **not** the universal subject's knowledge of it.
- `P(b,c | x=1,y) = P(b,c | x=2,y)` for each y, a relevant Local Agency independence condition.
- For the full Local Agency conclusion, additionally require `P(a,c | x=2,y=1) = P(a,c | x=2,y=2)`.

These conditions concern distributions conditional on the settings, with the experimental causal arrangement needed for the Local Agency interpretation. They do not require preassigned outcomes for unperformed measurements. A framework that does not admit the proposed absolute joint variable is not automatically subject to this particular extension test; it then owes the relational comparison law instead.

## 3. Derivation of the tradeoff

Set `E_xy = E(ab|x,y)` and `G_y = E(bc|x=2,y)`. Since all variables are ±1, read disagreement at most `e` gives

    G_y = E(bc|x=1,y) >= E_1y - 2e.

For any joint ±1 variables, `ac >= ab+bc-1` and `ac <= 1+ab-bc` pointwise. Therefore, using `H_y=E(ac|x=2,y)`,

    H_1 >= E_21 + G_1 - 1,
    H_2 <= 1 + E_22 - G_2,
    H_1 - H_2 >= S - 2 - 4e = 4/5 - 4e.

For a ±1 variable, the difference of its expectations under two distributions is at most twice their total variation. Thus

    TV[P(a,c|2,1), P(a,c|2,2)] >= max(0, 2/5 - 2e).

If full Local Agency enforces zero TV, then `e>=1/5`. More generally, unequal read errors `e_1,e_2` give `S <= 2 + 2(e_1+e_2)` under the same exact independence assumptions. No inference follows that errors of this magnitude actually occur in a friend experiment. If the source experiment, settings or record assumptions differ, this quantitative threshold must be rederived.

## 4. Sharpness: not merely an inequality

The earlier zero-mismatch extension gives hidden joint TV `2/5`. The verifier supplies a second exact distribution with the **same four observed quantum distributions**, `(b,c)` independent of `x`, and both read mismatches `1/5`. It also has `(a,c)` independent of `y` at both Alice settings. Thus it satisfies the displayed full independence conditions while relaxing read agreement.

Convexly mix those two extensions with weight `t` on the second, independently for every setting. The observable distributions remain exactly quantum. The mixture has

    e = t/5,       hidden-joint TV = (2/5)(1-t) = 2/5 - 2e,
    0 <= t <= 1.

Thus the bound is tight for all `0<=e<=1/5` within this extension problem. In particular:

| Read mismatch e | Minimum attainable hidden-joint TV |
|---:|---:|
| 0 | 2/5 |
| 1/10 | 1/5 |
| 1/5 | 0 |

The endpoint with `e=1/5` is not an argument that observers' reports are generally wrong. It is a mathematical illustration of the cost of requiring one absolute `c` and these independence conditions while holding the observed circuit correlations fixed. Nor is its `c` derived from the quantum state, an actual subject, or a legitimate nondisturbing physical measurement. For smaller `e`, the hidden `(a,c)` dependence is **not**, by itself, an observable faster-than-light signal; the observed Alice–Bob marginals remain nonsignalling. Providing a physical mechanism and maintaining the distinction between accessible and hidden quantities are further obligations.

## 5. What the no-God's-eye proposal still has to supply

A further [single-subject, two-stage persistence assessment](UNIVERSAL_SUBJECT_PERSISTENCE_AND_QUANTUM_TIME.md) applies an existing published no-go theorem to the proposed shared-experience bridge. It shows why assigning everything to one relative perspective, by itself, does not provide an affine joint history across coherent interventions.

A defensible relational universal-subject proposal needs **all** of the following, not just a vocabulary of perspectives:

- **Occurrence and ownership:** What determines that the friend genuinely has the experience, and that a universal subject is genuinely a subject that shares, represents, or otherwise relates to it? These relations must not be conflated. In particular, a shared experience token may require rejecting exclusive ownership; it does not automatically establish one context-independent outcome usable in every joint distribution.
- **Restricted comparison:** Define which experiences can be placed in a common perspective, what it means for their content to agree, and when that operation is meaningful. If an interaction reads a stable, undisturbed record, reproduce the read correlations; if a reversal removes the record, do not simply postulate the same comparison. Existing relational and cross-perspective-link proposals investigate such issues but are contested and are not by themselves theories of cosmic consciousness; see [Adlam and Rovelli](https://philosophyofphysics.lse.ac.uk/articles/10.31389/pop.8) and the [RQM overview](https://plato.stanford.edu/entries/qm-relational/).
- **No illicit pooling:** Do not assert a single absolute `c,a,b` in each trial together with the full Local Agency constraints and the stated correlations. Nor is a catalogue of actually distinct trials automatically a forbidden set of counterfactual outcomes for the *same* trial. The difficult case is a claimed simultaneous friend-event and later outcomes in the *same* reversal trial, not the mere existence of one whole or a description of different experiments.
- **Universal unity and agency:** State a noncircular criterion for an actually unified agent, including how its agency is internal to a timeless whole rather than a creator acting before it. Context labels and quantum states do not supply such a criterion.
- **Physical and phenomenal bridge:** Give dynamics or laws recovering the relevant probabilities and comparison conditions, plus an independently defensible subject-incidence and qualitative constitution. The proposed quantum-register model supplies none of these bridges.

**Assessment:** The limited-awareness response proposed in the prior note is too weak unless it is supplemented by a non-absolute event ontology or some other explicitly altered premise. A relational subject could still be the right answer, but we do not yet have a worked realization that shows the universal subject remains one agent while preserving genuine finite experiences and the required cross-perspective quantum consistency. The whole's necessary self-existence, possibility=actuality and non-perfection are also not established by this result.

## Verification

Run `python verification/universal_subject_lf_tradeoff.py`. The standard-library script verifies the exact endpoint table and 101 rational mixtures against the specified observable distributions, read mismatches, independence constraints and TV distances. The linear mixture provides equality for the entire stated interval; the finite checks are regression checks rather than the continuum proof. The verifier imports the existing exact extension and produces [its receipt](verification/universal_subject_lf_tradeoff.json). It does not test physical agency, experience, cosmological necessity or a full relational interpretation.
