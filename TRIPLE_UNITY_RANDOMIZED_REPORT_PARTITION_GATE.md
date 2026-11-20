# Testing exclusive phenomenal unity with randomized pair and triple probes

## Result and its limits

The previous [unity identification gate](PHENOMENAL_UNITY_AND_PLURAL_SUBJECT_IDENTIFICATION_GATE.md) showed that the very same pairwise unity table can correspond to a single triple or to three overlapping pairs. Here we connect that structural ambiguity to an **operationally specified, error-tolerant comparison across randomized trials**. We do not claim a new general probability theorem, a completed experiment, or a valid assay of phenomenal unity.

For three *predefined experiential aspects* in each trial, let `p_AB, p_AC, p_BC` be the probabilities that the respective pair is jointly present in at least one phenomenal field, and let `t` be the probability that all three are jointly present in one field. If all actual aspects in a trial belong to exclusive, internally unified fields, with pair and triple incidence defined consistently, then the following sharp population bound holds:

```text
max(0, (p_AB + p_AC + p_BC − 1)/2) ≤ t ≤ min(p_AB, p_AC, p_BC).
```

For example, pair probabilities all equal to 0.9 force `t ≥ 0.85` **under that exclusive-partition hypothesis**. A nonexclusive abstract family can have the same three 0.9 pair probabilities and `t=0.1`. If independently calibrated pair and triple probes could establish such a gap, the conjunction of the exclusive-partition assumptions, common-target assumptions and calibration would be challenged. It would **not** automatically prove overlap, identify a subject count, or decide whether the ground is experiential or neutral. At present we do not have a validated probe of this target, especially for perspectives inaccessible to a reporting participant.

## 1. Fix the target before the measurement

For each member of a specified population of local episodes, identify three candidate aspects `A,B,C`, and a predeclared local experiential window. The window can be an operationally defined interval in the experiment; this is not a fundamental clock of the whole. An aspect may be absent. When present, it is an occurrence or part of an occurrence, not merely a stimulus type or a physical component. Fix a token-identification convention that would remain meaningful across the queries; whether experience really decomposes this way is itself an assumption.

Define `P_AB=1` iff A and B belong **together** to at least one phenomenal field in that window, and similarly for `P_AC,P_BC`. Define `T=1` iff A, B and C belong together to at least one field in that window. If an aspect is absent, all incidences involving it are zero. A triple field entails its pair fields: `T≤P_AB,P_AC,P_BC`. Here “together” means genuine jointly lived phenomenology, not just co-occurring physical representations, successful matching or common response access. This is a *hypothetical* target; the formal notation does not establish that the model's aspects or fields exist as separate objects.

The exclusive-partition hypothesis E says that each present aspect belongs to exactly one field, and that every subset of a field is jointly present in that field. It does not assume that all actual subjects or all actual experiences are observed. It does assume that the three selected aspects have been identified consistently, that fields are well-defined for this task and that token-sharing/overlap across them is absent. On E, the three pair indicators are either all zero, exactly one is one, or all three are one; in the last case `T=1`. A `1,1,0` pair pattern is impossible. This is a stronger premise than the mere statement that triple jointness implies each pair jointness.

**Important:** if a probe asks whether *the reporting person* experiences A and B together, that is a subject-indexed target, not necessarily the existential target “some field contains A and B.” These can differ, especially when another putative subject cannot report. The following bound applies only to the explicitly defined targets, not to a mixture of the two. If one assumes the only relevant field is the reporter's, say so as an additional coverage assumption; do not infer it from successful reports.

## 2. The exact exclusive bound

Under E, in every episode,

```text
P_AB + P_AC + P_BC ≤ 1 + 2T,
T ≤ each of P_AB, P_AC, P_BC.
```

Taking expectations yields the displayed interval. This is an elementary event-count and union-bound argument, related to the established [Bonferroni inequalities](https://math.iisc.ac.in/~gadgil/MA261/notes/chapter-8.html), not a newly discovered inequality. No independence of the pair events is needed.

It is also **sharp for these exact marginals**: for any `t` in the interval, assign probability `t` to `ABC`, probability `p_AB−t`, `p_AC−t`, `p_BC−t` to the respective two-plus-one partitions, and probability `1−p_AB−p_AC−p_BC+2t` to three singleton blocks. All are nonnegative and sum to one exactly when the interval conditions hold. Presenting absent aspects as singleton placeholders preserves the incidence indicators; it does not assert that absent aspects are actual experiencers. If the lower bound exceeds the upper, the supplied marginals themselves are incompatible with E.

For `p_AB=p_AC=p_BC=0.9`, E permits exactly `0.85≤t≤0.9`. At `t=0.85`, each two-plus-one partition occurs with probability 0.05; at `t=0.9`, 90% of episodes have the triple and 10% have no pair joint. These are probability distributions in a conditional abstract model, not empirical samples or a proposed measure over the whole of reality.

## 3. Why testing triple incidence adds something

Consider another formal family on each trial: 10% contain `ABC`, 80% contain the three sets `AB`, `AC`, `BC` but no `ABC`, and 10% contain no joint pair. The pair incidences are all 0.9, while `t=0.1`. This shares the pair marginals of the exclusive mixture above but violates its required lower bound. It generalizes the exact pair-table ambiguity already in the prior gate; it is **not** a demonstration that the same numerical experience can actually be shared among fields. In particular, the alternatives might instead reflect unstable token identification, a different sense of unity, report artifacts or failure of the assumed window.

For fixed exact marginals, `t<max(0,(Σp−1)/2)` rules out E; `t>min(p)` challenges even triple-to-pair containment. If `t` lies within the E interval, E remains compatible with these marginals, but is not proved: nonexclusive families can also reproduce compatible data. Rejection of E, if all observation premises were somehow established, would not alone distinguish genuine overlap from a non-partitional field ontology or failures of the token and unity assumptions. This is not a claim that Bayne and Chalmers's stronger subject-indexed unity thesis has been refuted: their subject-specific subsumption principle imposes different structure.

## 4. A probe contract, including errors and selection

**Design.** Use a common randomized stimulus and setting distribution, independently assign one of four arms after the target window: report on `AB`, `AC`, `BC` or `ABC`. The contemplated outcome is a participant's judgment about joint experience in that window, not whether the physical stimuli matched. Include first-person instructions and explicitly solicit judgments about co-presence, with uncertainty and no-response recorded; separately measure attention, memory and objective discrimination. Include ordinary wakeful controls as well as any carefully selected clinical sample. Patients are not subjected to surgery or invasive intervention for this investigation.

The inference requires a **common latent target distribution** across arms. The query must not alter the earlier target or selectively change which episodes count; trial histories, expectations and preparation cannot systematically differ by arm, and local temporal extent must be specified. Delayed report, memory distortion, cue-driven reconstruction, post-stimulus processing, attention changes, uncertain token identity and participant-specific response abilities may violate this contract. Randomization alone does not establish it. Randomize at an appropriate stage, analyze all assigned trials, prespecify missing outcomes and compare prompt timing and control conditions. The assessment might itself change experience rather than merely read it; report that limitation rather than defining it away.

**Calibration.** For each arm `i`, write `Z_i` for its target and `Y_i` for a binary positive judgment, with predeclared nonresponse handling. Suppose independently warranted class-conditional bounds in the target population, arm and window are

```text
Pr(Y_i=1 | Z_i=0) ≤ α_i,      Pr(Y_i=0 | Z_i=1) ≤ β_i,
```

or equivalently their joint-probability versions when a class has zero probability. These are bounds relative to real phenomenal incidence, not merely agreement with another proxy, stimulus accuracy or another participant's report. A purely structural or behavioral task does not supply them. First-person reports are genuine evidence of the reporter's experience; they are not infallible external ground truth for every inaccessible subject. In particular, there is currently no justified assumption that a person can report all existential pair incidences across other putative perspectives.

With exact response rate `q_i=Pr(Y_i=1)`, the standard diagnostic-error argument gives conservative bounds

```text
p_i ≥ max(0,(q_i−α_i)/(1−α_i)),
p_i ≤ min(1,q_i/(1−β_i)),
```

for `α_i,β_i<1`, with the same formulas for `t` in the triple arm. These two inequalities are individually sharp for the declared error bounds but the **combined** bound below need not be sharp when further information constrains the arms or errors. The derivation and antecedents of diagnostic misclassification are already noted in [the awareness calibration audit](AWARENESS_CALIBRATION_AND_COGITATE_OFFSET_GATE.md); no gold-standard consciousness test is claimed.

Suppose simultaneous valid intervals `q_i ∈ [q_i^L,q_i^U]` and simultaneous upper bounds `α_i, β_i` are available. Set

```text
l_i = max(0,(q_i^L−α_i)/(1−α_i)),
u_i = min(1,q_i^U/(1−β_i)).
L_E = max(0,(l_AB+l_AC+l_BC−1)/2).
```

If `L_E > u_ABC`, the exclusive-partition package and these simultaneous calibration/sampling premises cannot all be correct. A different contradiction is `l_ABC > min(u_AB,u_AC,u_BC)`, which also challenges triple-to-pair containment. If neither contradiction appears, the test is **inconclusive**: absence of a significant contrast is not evidence of equivalence or proof of E.

## 5. Worked hypothetical and uncertainty accounting

Assume all pair report rates are 0.90 and the triple report rate is 0.10, and suppose each of four observed rates is known within `r=0.05`. Assume independently that **each** class-conditional error is at most 0.05 in its target arm. Then

```text
l_AB = l_AC = l_BC = (0.85−0.05)/0.95 = 16/19,
L_E = (3·16/19−1)/2 = 29/38 ≈ 0.7632,
u_ABC = 0.15/0.95 = 3/19 ≈ 0.1579.
```

The intervals conflict substantially. This is a sensitivity analysis with **invented response rates and error bounds**, not an analysis of data, a feasibility claim or evidence that any such calibration is available. The assumed error bounds must hold for the *same existential experiential target* in the relevant arms, not just for single-feature recognition in healthy participants.

For illustration only, if each arm contained 1,020 independent identically distributed binary observations with fixed means, all four empirical means would simultaneously be within 0.05 of their population means with probability at least `1−8 exp(−2·1020·0.05²) ≈ 0.9512`, by Hoeffding plus a union bound. The sample means 0.9 and 0.1 are integer-compatible with this sample size. No independence between arms is needed for the union bound, but within-arm iid sampling and correct arm assignment are assumptions, not default truths for repeated human trials. No-response must already be represented in the binary model or separately bounded.

The 4.88% bound concerns **sampling only**. If calibration bounds are estimated, add a separate simultaneous confidence-failure budget (and any budget for model or sampling validity); the numerical error-rate bound is not itself a confidence level. Hierarchical or sequential approaches could be appropriate but must be specified before outcomes. A study with these burdens could be infeasible, particularly in rare clinical populations; this is not a recruitment target or ethical justification.

## 6. Real evidence and scope

* Bayne and Chalmers, [*What is the Unity of Consciousness?*](https://consc.net/papers/unity.html), distinguish access and phenomenal unity and discuss an explicitly subject-indexed subsumptive unity thesis. The linked HTML text has since been read in full; see the [three-paper audit](THREE_UNITY_PAPERS_READING_AND_FRAMEWORK_AUDIT.md) for its actual same-subject closure premise and scope.
* Pinto and colleagues, [*Visual integration across fixation: automatic processes are split but conscious processes remain unified in the split-brain*](https://doi.org/10.3389/fnhum.2023.1278025), report results for one patient in simultaneous and sequential tasks and propose an interpretation involving conscious versus automatic processing. The prior [task audit](SPLIT_BRAIN_DEEP_EVIDENCE_AND_TASK_AUDIT.md) gives their reported outcomes and shortcut concerns. For this note we rechecked the abstract and introduction only; we did not newly examine full methods, figures, trial data or code. Their study did not estimate the pair and triple phenomenal incidence probabilities defined above.
* Koivisto and Silvanto, [*Relationship between visual binding, reentry and awareness*](https://doi.org/10.1016/j.concog.2011.02.008), report judgments of feature awareness and misbinding; **only the abstract and accessible publisher introduction/snippets** were inspected, not full methods, figures or data. Their object-feature binding is not the same target as the cross-field subject-level unity here, but it motivates guarding against equating a stimulus conjunction, report, and experienced conjunction.
* The [Bonferroni notes](https://math.iisc.ac.in/~gadgil/MA261/notes/chapter-8.html) were read for the standard union-bound reasoning. The exact partition formula here is a simple application to the specified three-aspect hypothesis, not a claim of priority for probability bounds or subject-unity theory.

## 7. What this advances and what remains

This moves beyond another graph label in a specific way: it derives an observable **conditional inconsistency criterion** for a real candidate metaphysical constraint, identifies the exact target an assay would need to measure, and specifies what an apparently decisive outcome would and would not mean. It also makes a severe obstacle visible: one first-person report cannot straightforwardly calibrate existential statements over potentially inaccessible perspectives. A shared behavioral transcript, even a joint comparison, does not resolve this gap.

The next substantive task is to independently motivate a possible calibration or find a principled way to bound errors and coverage without assuming the very field structure being tested. If that cannot be done, retain the condition as a theoretical stress test rather than report an empirical discovery. This does not settle experiential versus neutral grounding, persistence, subject counts, self-existence, plenitude, emergent physics, or C3—**full structural and experiential intelligibility**—under the seven joint criteria.

## Reproduction

Run [`verification/unity_triple_partition_calibration_gate.py`](verification/unity_triple_partition_calibration_gate.py). The [receipt](verification/unity_triple_partition_calibration_gate.json) checks all 125 triples of quarter-grid marginals and explicit endpoint/midpoint distributions, the nonexclusive family, and the hypothetical error and sample calculations. The exact bound follows from the proof and witness above, not from finite enumeration. The code has no clinical data and does not simulate real experience.
