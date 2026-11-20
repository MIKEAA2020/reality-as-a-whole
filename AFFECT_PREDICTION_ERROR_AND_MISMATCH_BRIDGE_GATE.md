# Discriminating mismatch from affect-prediction error

## Result and scope

A subject-held-out retrospective analysis of two published social-choice datasets finds that **post-offer reported valence predicted choice better than the reported valence prediction error** in the fixed comparisons below. This is a genuine out-of-sample predictive comparison, but it is **not a new physical test** of mismatch, a replication in new participants, a causal result, or a test of whether experience is intrinsic. The competing comparison was already made by Vollberg and Cikara. The contribution here is the explicit participant-held-out analysis, its outcome-leakage boundary, and a falsifiable design separating the proposed physical mismatch from rival experience-respecting accounts.

Experience is a valid datum. The governing criterion C3 is **full structural and experiential intelligibility**, to be satisfied jointly with C1–C7. None of the analysis below supplies full structural or experiential intelligibility. It does not assume a universal subject, an external clock, or that an actual simulation exists.

## Three variables that must not be conflated

For a specified subject and local experimental episode, distinguish:

- **Current physical mismatch:** `q(t)`, an independently specified physical variable in the proposed constituent substrate-independent description. In the existing E-L candidate, `q=1` unpleasant and `q=0` neutral are stipulated, not derived. The present analysis does not measure q.
- **Change in physical mismatch:** `Δq=q(t)−q(t−1)`, if the local episode has a defensible relational ordering, matched interval and physical observable. This is not automatically an emotion prediction error. In a timeless whole, `t` here labels locally ordered records or interventions, not an external absolute time.
- **Reported emotion prediction error:** `D=V−P`, where `P` is an anticipated valence report and `V` is the post-outcome valence report. `D` is constructed using `V`; it is not an independent physical readout. It can legitimately predict a *subsequent* choice, but using it as a predictor of that same `V` is circular and does not independently explain valence.

These are different mathematical objects even if they sometimes correlate. Joffily and Coricelli's variational-free-energy proposal involves a rate of change in a particular theoretical quantity; it does not identify that quantity with E-L's q. Physical, computational and experiential variables require separate mappings, independently specified scales and measurement models.

## Held-out comparison of reports and subsequent choice

Methods, fixed before computing the comparison but after knowing the literature and inspecting column names and author code, are in [the retrospective analysis plan](AFFECT_EXPECTATION_OUTCOME_HELDOUT_PLAN.md); the reproducible program and aggregate results are [here](verification/affect_choice_heldout.py) and [here](verification/affect_choice_heldout.json). The program verifies pinned source file hashes. It uses the authors' neutral-label exclusion, common complete cases, five disjoint participant folds, training-only feature standardization and the same regularized logistic form. It is not the authors' random-effects regression and does not attempt to reproduce the published model coefficients. Scores are mean held-out log loss per person; lower is better. `R` is reward prediction error, `V` post-offer valence, `P` expected valence and `D=V−P`.

| Experiment | People / trials | R only | R + D | R + V | R + P + V | Paired loss D−V, 95% interval |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 364 / 7,280 | 0.5353 | 0.5050 | 0.4030 | 0.4011 | 0.1020 [0.0855, 0.1190] |
| 2, emotion-and-reward group | 228 / 4,560 | 0.5093 | 0.4667 | 0.3929 | 0.3945 | 0.0737 [0.0527, 0.0933] |

The intervals resample participants' **fixed out-of-fold predictions**, not the whole training procedure, and are exploratory and unadjusted across studies. Here each included person contributed 20 trials, so trial- and participant-weighted losses happen to coincide. The binary recorded choice event rates were approximately 0.302 in each sample. Both models used a common reward predictor, no arousal predictor, no individual-specific effects, and equally fixed regularization; this does not prove the relative ranking would survive every alternative model, penalty or intervention. The two datasets share research design and authorship. No independent replication is claimed.

An algebraic caution: `R+P+D` and `R+P+V` define the same *unpenalized* linear predictor family because `D=V−P`. Thus evidence that a joint model fits better cannot by itself distinguish a separate emotion-error mechanism from the component reports. Penalty choices and measurement error can change fitted comparisons. The `R+D` and `R+V` restricted families are different; their held-out ranking is a real predictive comparison, not a mathematical necessity. Neither establishes what causes choice or experience.

The result is compatible with the published commentary's reanalysis, but is not its independent replay: its BIC and model choices differ. It does not refute all prediction-error theories. It also cannot decide whether mismatch is intrinsically unpleasant, because no independent physical q, pain, subject boundary or experiential identity is measured.

## A crossed physical-history test that could actually discriminate

The smallest decisive design is not simply to correlate a mismatch proxy with a report. First specify, on independent grounds, the subject candidate, a physically measurable q or calibrated observable with measurement error, and its units and sampling interval. Define `q₀` and `q₁` at two locally ordered moments, interventions and measurement schedule before observing the target ratings. Use distinct experimental arms to manipulate present level and prior history as independently as possible while measuring both. A schematic target design is:

| Cell | Previous mismatch q₀ | Current mismatch q₁ | Δq |
|---|---:|---:|---:|
| A | 0 | 0 | 0 |
| B | 1 | 0 | −1 |
| C | 0 | 1 | +1 |
| D | 1 | 1 | 0 |

Values 0 and 1 are intended physical levels, not affect ratings. They are schematic: actual interventions may not achieve them, and randomization cannot guarantee a manipulation changed q without its independent measurement. With sufficient repeated exposures, preregistered analysis and calibrated uncertainty:

1. **Current-level restriction:** A and B share q₁; C and D share q₁. A strict current-only model predicts the same valence distribution within each pair, conditional on relevant context. A vs C and B vs D assess the level contrast.
2. **Change-only restriction:** A and D share Δq=0 and hence must have the same valence distribution, conditional on the same context. B and C have different Δq, but their difference is not sufficient on its own to separate level and change because q₁ also differs. A vs D directly challenges a strict change-only account.
3. **History dependence:** A vs B or C vs D, at fixed q₁, can challenge a strict current-only account. Both restrictions can fail; a mixed, nonlinear, multi-timescale or context-sensitive model is possible. The sparse design cannot fully identify arbitrary functions of q₀, q₁ and context.

The E-L postulate is more specific than a generic current-level model: its binary states stipulate neutral versus unpleasant. Appropriate tests require predeclared operational predictions for rating distributions and assay errors, not merely a significant difference. To test **equivalence**, specify in advance a scientifically meaningful maximum difference and use a valid equivalence interval; a nonsignificant difference does not establish equality. Report manipulation failures, uncertainty, missingness and protocol deviations. Random assignment identifies effects of assignment under its assumptions, not the causal effect of q if the intervention also changes expectation, attention, arousal, sensory input, report tendencies or other unmeasured pathways. Directly attributing effects to q needs further defensible exclusion, mediator or other identification assumptions, or multiple interventions with differing side effects. No such identification is asserted here.

Add independently randomized expectation manipulation only if it can vary `P` without systematically changing q or other outcome-relevant pathways; verify rather than assume this. Measure expectation on a separate schedule and use independent, counterbalanced report/no-report trials to test report-induced changes. On the report trials, record outcomes after the relevant episode; on the no-report trials, use a separately validated behavioural or physiological proxy, not a claimed direct measurement of phenomenology. Definitions and measurements of each variable must be registered in advance; use blinded outcome scoring and prespecified held-out participants where feasible. Separate sensory intensity from unpleasantness with independent measures, but a null intensity effect alone is not equivalence. Real participants are assumed to have experience, not treated as proving a general subject-selection rule.

## Where the framework still needs work

1. **Subject constitution:** specify which relational structure constitutes a subject and why, including overlap and boundaries, without importing a universal subject or treating connectedness as sufficient.
2. **Physical observable and local time:** derive or independently operationalize q from an applicable relational physical model, including scales, coarse-graining, noise and locally ordered episodes. Do not infer a clock external to the whole.
3. **Experiential mapping:** explain why that physical relation is *this* experienced valence, and why one experience belongs to the selected subject; a successful predictor or intervention alone cannot establish identity.
4. **Negative and positive valence:** E-L's current binary neutral/unpleasant stipulation is incomplete as a general account. The rival is not denial of experience: alternatives can accept valence as intrinsic while locating it in another physical relation, in contextual/historical organization, or in additional psychophysical principles.
5. **Measure and plenitude:** specify occurrence and observer selection without making all possibilities equiprobable or defining the measure from the desired outcomes. Predict reported data with subject selection and errors included.
6. **Cross-domain transport and physics:** demonstrate calibrated bridges across persons, species, modality and substrate, then derive actual physical applicability rather than assuming finite spin examples describe neural or string dynamics.

Each step needs an independently testable interface or a clearly labeled metaphysical postulate. Statistical preference for one fitted model is not experiential intelligibility. The [Ney wave-function-realism audit](NEY_WAVE_FUNCTION_REALISM_AND_RELATIONAL_EXPERIENCE_AUDIT.md) adds a physical coherence and representation-consistency control for a prospective quantum mismatch variable, without claiming such a variable has been derived. B4, B5, B9, B10 and B11 remain open, as do the other previously open gates; B3 remains only conditional.

## Source scope and reproducibility

- Heffner, Son and FeldmanHall, [*Emotion Prediction Errors Guide Socially Adaptive Behavior*](https://doi.org/10.1038/s41562-021-01213-6): abstract, introduction, experiment-1 design/results and data availability read; other paper methods/results, figure images and supplements not fully inspected. The repository README, specified sections of the main R Markdown, category encodings, neutral-exclusion inputs and the four pinned cleaned CSV files were inspected or processed for the present analysis. Raw task records, the other experiments, supplementary code, and the full analysis code were not replayed. Study 3 mouse-tracking data are stated by the authors to be hosted separately, not inspected.
- Vollberg and Cikara, [*Post-Outcome Valence, Not Emotion Prediction Errors, as a Primary Predictor of Behavior*](https://doi.org/10.1525/collabra.147528): commentary text and figure caption read; figure image, supplementary analyses, raw data and code not independently inspected. Their reanalysis is not an independent experiment, and their comparison does not rule out all error models.
- Joffily and Coricelli, [*Emotional Valence and the Free-Energy Principle*](https://doi.org/10.1371/journal.pcbi.1003094): abstract, author summary and start of introduction only; full model, assumptions, proofs, figures and supplement not inspected. Its suggested rate-of-free-energy interpretation is not equated with q.
- Jepma et al., [*Different brain systems support learning from received and avoided pain during human pain-avoidance learning*](https://doi.org/10.7554/eLife.74149): abstract and introduction only; remaining methods/results, figures, raw data and code not inspected. It is not a test of the proposed phenomenal identity.

To rerun, install [the pinned dependencies](verification/requirements-affective-choice.txt), obtain the four exact files via the GitHub contents API into `.arena/epe` (see source paths and hashes in the script), then run `OPENBLAS_NUM_THREADS=1 python verification/affect_choice_heldout.py`. The optional `--download` uses raw.githubusercontent.com, which may not be reachable in restricted environments; the GitHub contents API method was used here. The aggregate JSON does not contain participant data. The existing [E-L candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md), [subject/horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md), [pain-affect evidence](MATCHED_STIMULUS_UNPLEASANTNESS_AND_EXPERIENTIAL_BRIDGE.md) and [selection bound](KENT_PLENITUDE_OBSERVATION_SELECTION_RECOVERY.md) provide further boundaries.
