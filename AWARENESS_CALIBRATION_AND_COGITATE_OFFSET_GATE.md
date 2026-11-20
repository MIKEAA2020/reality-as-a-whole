# Awareness calibration and the offset-ignition dispute

## Result

A theory that predicts a neural event **when a particular experience occurs** cannot be decisively tested by a negative neural result unless the relevant experience was sufficiently prevalent in the tested condition and the neural readout was sufficiently sensitive. This is not a reason to dismiss negative evidence: with independently justified lower bounds on awareness prevalence and event-detection sensitivity, a low observed event rate can rule out a quantitatively specified prediction.

We apply this measurement logic to the dispute over stimulus-offset ignition in the COGITATE comparison. The finite example below is **not a reanalysis of COGITATE**: its event rates and calibration values are invented for illustration. In particular, COGITATE's reported model-comparison and electrode-level findings are not trial-level rates and cannot be substituted for the toy's `y`.

The methodological gain is a concrete, falsifiable contract: state what awareness means at offset, how often it is present, what event the theory predicts, and the accuracy of the observation pipeline in the same condition. This improves the project’s experience–record interface without claiming that a proxy constitutes or perfectly measures experience.

## 1. The primary result and the dispute

The [COGITATE Consortium's adversarial study](https://www.nature.com/articles/s41586-025-08888-1) compared specified predictions of integrated information theory (IIT) and global neuronal workspace theory (GNWT) using fMRI, MEG and intracranial EEG. It reported partial alignment with each theory and challenges to specific predictions of both. It is not a direct test of this project's metaphysics or of subject number.

For the temporal GNWT prediction, the authors tested a preregistered onset-and-offset response model. They report onset-responsive PFC electrodes, but no PFC electrodes matching the specified combined onset–offset profile in that analysis; they also report an exploratory earlier-response exception and qualifying MEG and other controls. Their discussion treats the general lack of the predicted offset response as a substantial challenge, while noting modality and methodological issues. The paper's relevant claims concern **their specified models and analyses**, not an unqualified proof that no offset-related PFC signal exists anywhere or on any trial.

In their [commentary](https://doi.org/10.1093/nc/niaf037), Naccache and colleagues argue that offset ignition is not a general core prediction, but is expected when the offset is consciously attended. They question whether task-irrelevant offsets were systematically experienced, and also discuss limits on decoding mixed-selectivity prefrontal populations. They regard onset and other results more favorably for GNWT. These are proponents' interpretations, not independent measurements of awareness on the disputed trials. The original consortium explicitly argues that the shift to the blank screen is an update and that multiple methods support sensitivity. The two sides differ about theoretical commitment and the relevant experience, not merely about whether a p-value crossed a threshold.

A further [MEG reanalysis by Bandara, Rowe and Garrido](https://doi.org/10.64898/2026.07.16.738188) reports model-derived effective-connectivity findings consistent with onset and offset responses under its dynamic causal modelling. It is a **preprint**, not peer-reviewed in the version inspected, and uses the existing dataset rather than a new independent replication. Its models and posterior estimates are not themselves interventions or proof of the directed mechanisms; the authors also caution that their post-hoc face-selectivity validation did not yield strong evidence. Do not conflate this analysis with the original preregistered endpoint or claim that it proves either theory.

The user-facing project candidate, common recurrent access, does not automatically inherit either camp's anatomical predictions. It must separately state the contents, interval and realized causal organization required by its own rule. A task-irrelevant physical stimulus, a perceived stimulus, an experienced offset and report of that offset are distinct variables.

## 2. A minimal conditional model

Fix one declared class of experimental trials, a time window, population, neural event definition and analysis pipeline. Let

```text
A = 1  if the target offset is experienced in the specified sense,
E = 1  if the theory's specified neural event really occurs,
Y = 1  if the observed neural pipeline reports that event,
T = 1  if a specified awareness proxy is positive.
```

Here A is an **idealized latent target**, not a claim that conscious experience is a binary observable or that stimulus disappearance equals awareness of disappearance. E is also an idealized, physically defined event; Y is its imperfect readout. The binary abstraction is deliberately much simpler than the original COGITATE analysis.

Define

```text
π = P(A=1),                 q = P(E=1 | A=1),
y = P(Y=1),                 t = P(T=1).
```

We only define q when `π>0`. A conditional theory prediction might assert `q ≥ q_min`, not that every stimulus offset causes E regardless of awareness. We do not attribute a numerical q_min to GNWT, IIT, the consortium, or the commentators.

Without any calibration, even perfect knowledge of the entire observed `(Y,T)` distribution need not identify q. The verifier gives two models with the **same joint distribution** of Y and T:

| Model | P(A=1) | P(E=1 given A=1) | P(Y=1) |
|---|---:|---:|---:|
| Higher awareness, weaker relation | 4/5 | 1/4 | 1/5 |
| Lower awareness, perfect conditional relation | 1/5 | 1 | 1/5 |

In both, `E=Y` and T is an independent, uncalibrated positive indicator with rate `41/50`. This is an explicit non-identifiability witness, not a claim that T is in fact uninformative or that these are the only possible mechanisms. It does not show any particular participant was unaware. Stronger justified calibration or additional evidence can exclude one or both models.

## 3. Turn the awareness objection into a quantitative test

Assume in the target condition:

```text
P(T=0 | A=0) ≥ c > 0                    (proxy specificity),
P(Y=1 | E=1, A=1) ≥ r > 0               (neural event sensitivity).
```

These are **lower bounds**, not assumed perfect tests. We do not assume the awareness proxy and neural readout are conditionally independent. By the law of total probability,

```text
t ≤ π + (1−c)(1−π),
π ≥ π_L := max[0, (t+c−1)/c].
```

No lower bound on proxy sensitivity is needed for this *lower* bound on prevalence. Separately,

```text
y ≥ P(A=1, E=1, Y=1) ≥ π q r.
```

If `π_L>0`, it follows that

```text
q ≤ min[1, y/(π_L r)].                                   (1)
```

If `π_L=0`, these premises provide no nontrivial upper bound on q. If `r` is unknown or could be arbitrarily small, they likewise provide no useful quantitative upper bound. False-positive Y events can only raise y, so no specificity of the neural readout is required for this one-sided bound. The inequalities remain valid with arbitrary dependencies between T and Y. If the theory instead predicts a deterministic or graded continuous neural signature, equation (1) is not automatically its appropriate test.

This is an elementary partial-identification application of established diagnostic misclassification reasoning, not a new screening theorem. It addresses the particular joint burden of **experience prevalence and neural detectability** for conditional theory predictions.

### Illustrative values, not observations

Suppose, solely for calculation,

```text
t = 41/50 = 0.82,       c = 19/20 = 0.95,
y = 1/5   = 0.20,       r = 9/10  = 0.90.
```

Then `π ≥ 77/95 ≈ 0.811` and `q ≤ 190/693 ≈ 0.274`. A candidate asserting `q ≥ 0.9` would conflict with these jointly valid premises and hypothetical population rates. The verifier also constructs an exact joint law attaining `q=190/693`: the bound is **sharp for these margins and assumptions**, not merely a loose calculation. Full joint observations or additional constraints could tighten it.

This conclusion does not follow from low y alone: if almost no offset experiences occurred, or if detection sensitivity in the relevant event class were poor, a strong conditional prediction might remain compatible. Conversely, proposing unspecified awareness lapses or detector failure does not automatically rescue the theory when credible calibration rules them out.

## 4. What a real test would have to establish

1. **Define the experiential event before inspecting results.** Distinguish awareness of the offset from simple visibility of the stimulus, fixation, task relevance, an inferred attentional state, and the later memory of a change. Permit unclear or mixed cases; do not silently count them as either category.
2. **Define E and Y physically.** Specify where, when, scale, event threshold or waveform, content criterion and estimator. Establish actual detection properties for the relevant event class, not merely the ability to detect different onset responses or events in another brain region. If no independent event reference exists, report a sensitivity range and model its uncertainty.
3. **Justify the awareness proxy.** Specificity here is about false positives against the target A, not stimulus detection accuracy. Eye movements, performance, probe responses and retrospective reports can help, but may reflect motor, memory, attention or criterion effects. No perfectly calibrated experiential assay is established by this document. Calibration using reports itself assumes something about their relation to experience.
4. **Address the no-report transport problem.** The specificity bound must apply to the same population, condition, time window and definition as the target trials. If a probe changes attention or produces post-perceptual processing, its behavior may not transport to unprobed trials. Randomly interleaved probes, prospective perturbation checks, and multiple probes are possible strategies, not automatic solutions; report task effects and shared errors.
5. **Use the actual estimator and sampling design.** A nonsignificant group contrast, a Bayes factor or a fraction of significant electrodes is not y. Define a suitable trial-level event detector or derive the corresponding bound for the original aggregate statistic. Account for within-person and electrode clustering, multiplicity, missing data, modality-specific coverage and measurement dependence. Use simultaneous uncertainty bounds for t, c, y and r; if `t≥t_L`, `c≥c_L`, `y≤y_U`, and `r≥r_L` hold jointly, replace them in (1). A zero `π_L` or `r_L` makes the exclusion uninformative.
6. **Precommit rival predictions.** Compare no-offset, awareness-conditional and onset/offset models with concrete thresholds and held-out parameters. Specify what the proposed recurrent-access rule predicts, including alternatives in which offset is unexperienced. A physical difference detected between models does not by itself establish the qualitative identity or number of subjects.

A statistically significant or nonsignificant readout is not a private experience. Yet absence of a perfect phenomenal oracle does not make every disciplined test worthless: explicit uncertainty, operational anchoring and cross-condition calibration can yield informative **conditional** evidence. Neither epistemic extreme—declaring no-report evidence conclusive by definition or declaring empirical consciousness research impossible—follows from this model.

## 5. Implications for the whole-account

The target remains a timeless, self-sufficient, intrinsically experiential relational whole with genuinely plural perspectives, not a universal consciousness or external creator. To connect it to neuroscience, the project still owes an independent constitution rule for subject incidence and experience quality, a representation-invariant physical event definition, and a transportable observation bridge. This gate adds a quantitative way to expose what a conditional theory test needs; it does not supply those missing laws or establish that experience is fundamental or necessary.

## Sources and access limits

- [*Adversarial testing of global neuronal workspace and integrated information theories of consciousness*](https://www.nature.com/articles/s41586-025-08888-1): HTML chunks 0–10 of 38 read, including the main reported results and discussion through the start of Methods. Remaining Methods, supplementary information, preregistration and figure images were not fully inspected here; participant data and pipeline were not reanalyzed. The project’s earlier [pinned protocol audit](WORKSPACE_TOGETHERNESS_CANDIDATE.md) and [selected source-code audit](NEURAL_TIMING_CONSTITUTION_AUDIT.md) have their own declared scopes.
- Naccache et al., [*GNW theoretical framework and the “adversarial testing of global neuronal workspace and integrated information theories of consciousness”*](https://doi.org/10.1093/nc/niaf037): all three extracted chunks of the [author-hosted PDF](https://sergent-consciousness-lab.u-paris.fr/wp-content/uploads/sites/68/2025/12/GNW-theoritical-framework-and-the-adversarial-testing-of-global-neuronal-workspace-and-integrated-information-theories-of-consciousness-Naccahe-all.pdf) read; no independent verification of its historical claims or referenced models was attempted.
- Bandara, Rowe and Garrido, [*Testing the Spatiotemporal Predictions of Global Neuronal Workspace Theory and Integrated Information Theory*](https://www.biorxiv.org/content/10.64898/2026.07.16.738188v1.full): abstract and chunk 0 of 25 read; full preprint, figures, data and code not audited.
- [*An open-access multi-site fMRI dataset for investigating conscious visual perception*](https://www.nature.com/articles/s41597-026-07377-y): abstract and beginning of chunk 0 of 13 read; underlying recordings and access route not inspected. Its advertised dataset is not a calibration or a new analysis in this gate.
- Rogan and Gladen, [*Estimating prevalence from the results of a screening test*](https://doi.org/10.1093/oxfordjournals.aje.a112510), and [*Sensitivity and specificity in prevalence studies: The importance of considering uncertainty*](https://pubmed.ncbi.nlm.nih.gov/33331403/): search abstracts/excerpts only; direct PubMed fetches returned HTTP 500 and the full articles were not read. Their established screening context is background, not a phenomenal gold standard.

## Reproduction

`python verification/awareness_ignition_partial_identification.py` checks the exact matched-observation models, the numerical sharpness witness, and 40,000 rational parameter combinations for the inequalities. The [source](verification/awareness_ignition_partial_identification.py) and [receipt](verification/awareness_ignition_partial_identification.json) use synthetic distributions only. Finite grid checks do not independently prove calibration assumptions, neuroscience findings or the general inequalities, whose elementary derivation is given above.
