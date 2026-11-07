# A two-subject, reversible-record selector: first finite model

## Purpose and status

This is the next micro-step after the [brain-centric many-blockworlds audit](BRAIN_CENTRIC_MANY_BLOCKWORLDS_QUANTUM_AUDIT.md). The target is a **single finite example** in which two distinct subject slots have definite matching experiences while the physical record can either be read or coherently reversed. We compare its operational predictions with standard quantum mechanics and expose exactly which rule is added.

**Status:** a mathematically consistent probability extension for two specified protocols—not a physical realization, a theory of brains, a derivation of experience, a general many-minds interpretation, or a solution of quantum gravity. “Subject,” “experience,” and their identity are modeled by labels with stipulated semantics. The selector is not forced by the quantum state. The finite circuit uses an ordinary laboratory ordering; it does not establish a fundamental external clock.

Many-minds and observer-history models are established prior work, not invented here. Compare Albert and Loewer's formulation in the [Stanford Encyclopedia treatment](https://plato.stanford.edu/entries/qm-everett/), Matthew Donald's [brain-history approach](https://arxiv.org/html/quant-ph/9703008), and the [decoherent-histories review](https://arxiv.org/abs/gr-qc/9407040). Our limited contribution is to put a **particular two-slot probability extension** beside our own reversible-record and Local Friendliness gates and make its extra conditional assumptions explicit; no literature-wide novelty is claimed.

## 1. The physical circuit

Let `S` be a qubit and `F,G` two qubit memory registers. Initially:

```
|+>_S |0>_F |0>_G,      |+>=(|0>+|1>)/√2.
```

Apply CNOT from `S` to `F`, then CNOT from `S` to `G`:

```
|Ψ> = (|000> + |111>)/√2,   in the order S,F,G.
```

We compare two subsequently chosen procedures:

- **Read:** measure `F` and `G` in the Z basis. Quantum mechanics predicts `00` and `11`, each with probability `1/2`.
- **Reverse:** coherently undo both CNOTs, then measure `X` on `S`. Quantum mechanics predicts `X=+` with probability `1`. Both memories return to `0` in this ideal operation.

These are distinct procedures. If an independent physical record of the friend values is first created and then left uncontrolled, it must also be included in the state; the advertised perfect reversal does not automatically apply. Nor does a qubit memory establish the presence of a phenomenal subject.

## 2. A stipulated two-subject extension

Now add **two named, distinct subject slots**, `σF` and `σG`. At the intermediate record stage, introduce a single additional bit `λ`, with

```
P(λ=0)=P(λ=1)=1/2,
experience(σF)=λ,  experience(σG)=λ.
```

Here the 0/1 labels specify the *modeled content* “the subject experiences record 0/1”; they do not capture color, feeling, valence or any intrinsic nature of the experience. `σF` and `σG` remain two slots even when their contents agree. We stipulate—not derive—that both refer to distinct persisting subjects at the modeled intermediate stage.

Define the operational responses of this extension as follows:

| Context | `λ` | Stipulated subjective labels | Observable outcome | Weight |
|---|---:|---|---|---:|
| Read | 0 | `(σF=0, σG=0)` | `F=0, G=0` | 1/2 |
| Read | 1 | `(σF=1, σG=1)` | `F=1, G=1` | 1/2 |
| Reverse | 0 | `(σF=0, σG=0)` | `X=+` | 1/2 |
| Reverse | 1 | `(σF=1, σG=1)` | `X=+` | 1/2 |

For each context, the physical outcome marginal exactly matches the specified quantum circuit. The distribution of the earlier subjective labels is the same regardless of which later procedure is chosen. In the read procedure, the subject labels and readouts agree. In the reverse procedure, the previously written physical memories have been reset: **no durable report of `λ` is furnished by the specified circuit**.

This finite probability table demonstrates a logical point: *definite stipulated subjective values plus matching read-context records and coherent reverse-context statistics are not algebraically inconsistent for these two protocols alone.* It does not demonstrate that the stipulated experiences exist, that a real subject is present during a coherent interaction, or that the rule can be extended consistently to all physical operations.

It also does not claim that generating `λ` turns a merely possible world into an actual one. The probability table can be read as a finite run/subject-indexing model; whether any such measure captures the user's stronger `possibility = actuality` thesis is a separate question.

## 3. The exact extra premise: conditional Born probabilities

The physical quantum state `|Ψ>` used in this toy model is the **same** for both values of `λ`. If we require a *deterministic* function of that same unconditioned quantum state and the same fixed subject slot to select one bit, it returns only one value. It cannot by itself produce both 0 and 1 with probability `1/2`. Our example therefore **adds** `λ` and its distribution. Other routes—including stochastic laws, relative/branch-indexed subjects or further physical variables—make different assumptions.

More importantly, in the read context this extension stipulates

```
P(Fread=λ | λ) = 1.
```

But if one additionally demands the **ordinary Born rule conditional on `λ`** using the *same pure state* `|Ψ>` in each `λ` subensemble, each `F` outcome is still `1/2`; the probability of agreement with `λ` is only `1/2`. Our read table has perfect agreement, so it **does not satisfy that extra conditional-Born assumption**, even though its *unconditional* observable read probabilities are the standard ones. This is where the extra hidden/experiential response law enters. A consistent full completion must explain that law, its allowed conditioning and its physical/phenomenal status; no quantum instrument implementing a non-disturbing measurement of `λ` has been constructed.

The converse is also important: this argument is only about a selector that returns a **single absolute label from the same unconditioned state**. An Everettian may instead assign distinct branch-relative subjects or describe a set of subjects; such a proposal is not ruled out by this elementary single-output observation. It must still specify branch selection, probability/measure, subject incidence and comparisons. Likewise, nothing here proves that the hidden `λ` model is the right interpretation.

## 4. Why experience cannot simply be replaced by a projective intervention

Change the physical procedure: after the two records are written, perform a projective measurement distinguishing the 0 and 1 record branches and discard its result; then undo the two CNOTs and measure `X` on `S`. That physical measurement creates an incoherent mixture:

```
P(X=+ | uninterrupted coherent reversal) = 1
P(X=+ | intervening unread projective measurement) = 1/2.
```

Thus identifying the subjective `λ` with an actual Lüders-collapse intervention would change this protocol's predictions. Our stipulated selector instead assigns `λ` **without** inserting that measurement. It is an extra hidden-event rule, not the claim that quantum theory itself derives a definite experience.

Nor can the model obtain a perfectly reliable untouched external record of `λ` for free through the standard branch-copying interaction. Such a record distinguishes the two physical paths and constrains interference. Our independently checked [record-complementarity model](REVERSIBLE_FRIEND_RECORD_COMPLEMENTARITY.md), using the established visibility–distinguishability principle of [Englert](https://doi.org/10.1103/PhysRevLett.77.2154), quantifies the tradeoff in its specified circuit. It does **not** prove that experience requires an indelible record. To recover coherence after making a copy, a reversal must include the relevant copy and any further physical traces, under that model's assumptions.

The model therefore keeps three propositions distinct:

1. There was a stipulated first-person value `λ` at the intermediate stage.
2. The specified memory registers physically encode matching alternatives before reversal.
3. There exists an independently accessible, durable report after reversal.

It assumes the first, shows the second only at the level of the quantum state, and **does not supply** the third. Experiential reports remain valid data when available; the model cannot use a report that its own reversal protocol has erased.

## 5. What the model narrows down

| Question | Finite-model result | Still missing |
|---|---|---|
| Can two distinct labeled subjects agree on a record? | Yes, by the explicit shared-`λ` table. | Why these labels denote real subjects and why they agree. |
| Does a definite stipulated experience require physical collapse? | No logical requirement in this restricted extension. | A full conditional subject/physics law compatible with actual interventions. |
| Does the unchanged quantum state select a unique definite value by itself? | Not as a deterministic single-valued function of this same unconditioned state. | Justification of hidden/stochastic variables or of branch-relative subjects. |
| Are all quantum and relativistic constraints met? | Not established: only two local procedures are checked. | General operations, repeatable subjective reports, shared records, contextuality and locality. |
| Is subject identity over time explained? | No: two subject slots and their intermediate values are stipulated. | Individuation, persistence, unity and conditions for birth/death or branching. |
| Does this select pain or explain its quality? | No: λ only models a binary record. | The phenomenology/physical identity and independent calibration gates. |

In particular, do not extrapolate this one-lab table to the two-party Local Friendliness scenario. Our earlier [exact extension](SUBJECT_IDENTITY_LOCAL_FRIENDLINESS_TEST.md) shows that, under its explicitly stated friend-event and Local Agency assumptions, a Bell-violating extension carries a quantified hidden-joint dependence cost. This new selector has no remote Bob, no spacelike choice and no general response law, so it does not evade that result or demonstrate superluminal signalling.

## 6. Next dependency: from a table to a lawful subject selector

A defensible next model must specify, *before choosing an experiment*:

1. The physical variables or operational/relational criteria that select distinct subject slots, and which transformations are mere redescription.
2. How the additional subject/event variables are distributed, updated, and correlated with records for a **family** of possible instruments—not just the two rows above—and whether the usual Born rule applies after conditioning on them.
3. Which actual reports can be produced and retained, including the physical cost and availability of a reversal; agreement between observers must be a derived or explicitly stipulated joint law.
4. The response to a two-party Local Friendliness experiment and the chosen status of absolute events, locality and free settings.
5. An independently calibrated relation between the physical criterion and experience. Labels alone do not establish a subject, an episode, or the intrinsic quality of feeling.

Those dependencies sit below, not instead of, the wider objective: an intelligible timeless basis, local physics and real experience. They do not resolve the question of one universal consciousness, and under the user's adopted `perfect whole ⇒ best universe` and `universe not best` premises they give no basis for restoring whole perfection.

A subsequent [two-report circuit](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md) tests the second and third dependencies for two explicit physical record architectures. It shows that perfect report consensus alone does not establish faithful reporting, and makes the interference cost of a specified retained record explicit. It still does not provide a subject-to-report law.

## Verification

Run `python verification/two_subject_reversible_selector.py`. The [receipt](verification/two_subject_reversible_selector.json) checks the three-qubit read and reversal outcomes with exact rational arithmetic, the stipulated joint distributions, the unread-projective-control difference, and the conditional-Born agreement calculation. Rerun [the friend-history](verification/friend_history_selector_gate.py), [external-record](verification/reversible_friend_record_tradeoff.py), and [Local Friendliness extension](verification/subject_friend_quantum_extensions.py) checks for the separate existing gates. Passing these scripts is not a demonstration of conscious observers, a physically complete hidden-variable model, or a resolution of an open physics problem.
