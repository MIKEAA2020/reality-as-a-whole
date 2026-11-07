# Ciupa's brain-centric many-blockworlds proposal: quantum and subject gates

## Source and scope

Martin Ciupa, *Many Worlds, Many Minds: A Brain-Centric Interpretation of Quantum Mechanics/Relativity*, supplied in full by the user in this conversation. This corrects the limitation in our [previous Cicurel book audit](CICUREL_BRAIN_CENTRIC_BOOK_AUDIT.md): I have now read Ciupa's actual text. I also inspected its linked historical review [arXiv:2405.06924](https://arxiv.org/html/2405.06924v1) and the [MIT Press overview](https://thereader.mitpress.mit.edu/the-many-worlds-theory/). The linked separate experimental-proposal page returned an HTTP error; **the specific experiments on that page were not read**. The article reproduced in chat is not itself copied here.

## What the article proposes

Ciupa combines Everettian many-worlds, Wheeler's participatory idea, the Wheeler–DeWitt (WdW) equation, and Cicurel's brain-centric account. He suggests that individual conscious experience may “pilot” a path among many blockworlds, that those blocks are in superposition, and that brain activity and quantum events might be studied empirically. This is explicitly presented as a **possibility for research**, not a completed mathematical theory. It does not specify the mathematical pilot rule, weights, physical measurement channel, shared-record rule, or a distinct quantitative prediction.

The proposal is genuinely relevant to our project: it puts individual experience at the center, considers a timeless whole containing temporal perspectives, and tries to connect quantum theory with minds. It need not require one all-encompassing universal subject. But **subject plurality, Everettian unitarity, participation and WdW are separate commitments**, not consequences of one another. We have not established that they form a mutually consistent or empirically superior package.

## 1. Why WdW does not yet give us many experienced blockworlds

The canonical WdW equation is schematically

```
Ĥ(x) Ψ[h,φ] = 0,   with additional spatial-diffeomorphism constraints.
```

Here the wavefunctional is over spatial geometry and matter configurations, not directly a classical probability distribution over complete four-dimensional universes. Operator ordering, constraints, boundary conditions, physical inner products and continuum/control issues matter. The equation does not contain an ordinary universal external time evolution. The article's description of the WdW wave as “constantly changing” is, at best, a heuristic: change must be recovered *relationally* or approximately, using internal degrees of freedom and suitable approximations. Standard treatments include Kiefer and Sandhöfer's review [3](https://arxiv.org/html/0804.0672v3); those known constructions are not re-derived here.

The article's suggested step

```
WdW solution → superposed 4D blockworlds → experienced histories
```

is a **research hypothesis, not a derivation in the article or a consequence of WdW alone**. It needs a physical space of solutions, an appropriate histories/decoherence construction, approximate classical spacetimes, a subject–history map and probability/measure rule. Some of these items are debated even before phenomenology is introduced.

This fits the user's desire for a timeless ultimate basis and no external universal clock, but WdW by itself supplies neither a completed emergent-spacetime theory nor an answer to the problem of time. Our prior restricted-clock results and corrections are summarized in [the time evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md). A classical blockworld is a spacetime history, so making it fundamental would not by itself fulfill the user's stronger desideratum that spacetime itself is nonfundamental; it could instead be an emergent approximation.

## 2. The first gate: histories must preserve interference

A common image says every event instantaneously splits a uniquely defined world. Modern Everettian accounts often treat branching as approximate, coarse-grained and decoherence-dependent; different interpretations of branches and probability remain contested [1](https://plato.stanford.edu/entries/qm-everett/). The article does not supply a rule for when its blockworlds separate or how they can retain interference.

The following elementary control makes the issue exact. Prepare `|+>=(|0>+|1>)/√2` and finally measure `X`:

```
Coherent evolution, no intermediate Z record:        P(X=+) = 1.
Insert a projective Z record and discard its value:  P(X=+) = 1/2.
```

Thus treating both Z alternatives as an ordinary classical mixture *at that stage* destroys an interference prediction. This does not refute blockworlds in general or every ontology of definite experiences; a successful account can retain amplitudes, contextual descriptions, inaccessible records, or an appropriate consistent/decoherent family. The point is narrower: one cannot freely assign a single classical probability distribution to every competing fine-grained quantum history and keep the coherent statistics. This is a known issue in [decoherent-histories theory](https://arxiv.org/abs/gr-qc/9407040) [4](https://arxiv.org/pdf/gr-qc/9407040).

Our [temporary-record history analysis](TEMPORARY_SUBJECT_RECORD_HISTORY_GATE.md) exhibits the same issue in an explicit friend-record circuit. **Neither that circuit nor this qubit control proves anything about an actual conscious subject.**

## 3. “Piloting” has at least three distinct meanings

| Reading | Claim | What would need to be shown |
|---|---|---|
| **Perspective/conditioning** | Each subject has a definite experience relative to a history; physical quantum predictions are unchanged. | Specify subjects, compatible histories, identity over time, shared records and a Born-compatible experience measure. No operational difference follows merely from calling this “piloting.” |
| **Ordinary embodied agency** | A brain and body act on an apparatus and therefore affect later measurement settings or states. | Model the actual physical causal pathway and controls. Standard quantum mechanics already permits experimental choices and feedback. |
| **New physical selection** | Consciousness changes outcome weights, collapse, interference or the physical global state beyond the ordinary controlled process. | State the dynamical law, experience trigger, numerical effect, relativity/no-signalling conditions and an experimental discriminant. |

The article suggests consciousness might influence branching, but does not choose or formalize these options. We should not attribute a specific collapse law or mind-controlled Born-rule violation to Ciupa without further clarification. Nor should we assume that a subject whose experiences are physically constituted is causally inert: ordinary neural actions can matter even when they introduce no new quantum law.

### A conditional no-signalling check, not a refutation of the article

An instructive test is a *hypothetical*, stronger claim: a participant can choose a spacelike measurement basis and somehow bias the **objective** outcome weights while preserving the standard conditional remote states. Start with a Bell pair; Bob measures `Z`. Suppose Alice chooses `Z` or `X`, and the relevant `+` outcome is assigned weight `1/2+ε` in either basis. Then the model gives

```
P(Bob gets 0 | Alice uses Z) = 1/2 + ε
P(Bob gets 0 | Alice uses X) = 1/2.
```

For nonzero `ε`, Bob's local statistics reveal Alice's controllable setting if the choices and readout are genuinely spacelike separated. This is the familiar steering/no-signalling concern in a concrete finite instance, not a new theorem; see the analysis of nonlinear quantum dynamics and its assumptions [1](https://iopscience.iop.org/article/10.1088/1367-2630/adcae1). Our [exact check](verification/brain_centric_blockworld_gates.py) and [receipt](verification/brain_centric_blockworld_gates.json) verify this arithmetic for seven rational biases.

**The assumptions are essential.** This example presumes an actual change to the objective ensemble weights, the stated conditional remote states, controllable basis settings and accessible Bob records. If there is only subjective conditioning, ordinary Born-weighted outcomes, or ordinary postselection whose label reaches Bob through a classical channel, no such signalling follows. A different modified model could also impose further restrictions. We have **not** shown that Ciupa proposes the stronger biased rule, that all consciousness-involving interpretations signal, or that relativity plus quantum mechanics is thereby solved.

## 4. Meaningful experiments require distinguishable predictions

Correlating brain activity with a quantum event can be interesting neuroscience, but correlation alone does not establish that consciousness changes quantum probabilities. The physical apparatus may affect the brain; attention may change reports; participants may influence preparation or selection; records can be postselected; and environmental noise can produce apparent coherence loss. Ciupa's separate linked experiment page was not accessible, so these are **general design requirements**, not criticisms of its unseen details.

A prospective comparison should freeze before data collection:

1. A concrete quantum source, prepared state, settings and independent raw outcome record; define the baseline Born probabilities and apparatus controls.
2. A proposed observable deviation—e.g. an outcome bias beyond modeled preparation/control effects, or a quantitatively specified extra coherence loss—and its predicted size.
3. A controlled contrast in the hypothesized experience trigger, with independently calibrated experience measures and matching of attention, movement, sensory input and environmental coupling as far as possible.
4. A blind, predeclared analysis, treatment of missing data and postselection, sample size, uncertainties, and rejection thresholds. If using separated observers, also specify no-signalling constraints.
5. Competing conventional apparatus/noise models and independent replication.

A no-new-dynamics many-minds reading may instead be empirically equivalent to its reference quantum model for the specified accessible observations; in that case a brain–quantum correlation test **alone** cannot distinguish it. Nor can theory-internal statements about subjective probability substitute for an empirical mapping between experiences and records.

Our earlier [collapse-identifiability audit](CONSCIOUSNESS_COLLAPSE_IDENTIFIABILITY_GATE.md) supplies one exact caution: the same observed dephasing channel can result from different combinations of a putative trigger and ordinary background noise. An independently bounded noise model and a separately calibrated trigger are necessary for that test family. Those controls do not constitute evidence that consciousness collapses a state.

## 5. A disciplined synthesis for our project

A conservative candidate worth exploring is:

1. A timeless underlying structure supports physically admissible correlations, not necessarily an external universal time.
2. Under additional, explicitly stated conditions, approximately classical, mutually consistent record histories emerge.
3. Distinct subjects are associated with some of those histories; subject identity, boundaries, persistence and **why there is experience** are separate unsolved rules.
4. The subject's physically realized brain/body can act within its effective history. It is an open further question whether experience requires a modification of physical quantum laws.
5. A norm-squared or other justified measure must explain observed quantum frequencies and self-locating uncertainty; it cannot be recovered by counting a continuum of minds equally or by just saying “all outcomes exist.”

This is a research sketch, not a completed model or a claim of literature novelty. Histories and many-minds antecedents include Griffiths, Gell-Mann–Hartle and Donald's [history-oriented many-minds proposal](https://arxiv.org/html/quant-ph/9703008). It does not derive the user's `possibility = actuality` identity: nonzero amplitude in a specified quantum model is not automatically every genuine possibility in the user's strongest metaphysical sense. Nor does it infer that one consciousness underlies all subjects. Under the user's adopted perfection premise and non-best-universe premise, the whole is non-perfect; the article does not resolve that question.

**Next micro-step:** ask whether the intended pilot is purely perspectival, ordinary embodied control, or an additional physical selection mechanism; then specify one finite subject–record–history model, its Born weights and its reverse-interference behavior before attempting the WdW/relativity limit. This keeps the global goal visible while isolating the missing join.

## Reproduction

`python verification/brain_centric_blockworld_gates.py` checks the exact qubit interference and conditional signalling calculations; existing checks `verification/friend_history_selector_gate.py` and `verification/experience_collapse_identifiability.py` cover their separately stated finite models. They are mathematical controls, not evidence of a real brain in coherent superposition and not a validation or exclusion of BC-MBWI.
