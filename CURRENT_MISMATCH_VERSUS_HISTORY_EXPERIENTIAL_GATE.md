# Current mismatch versus experiential history: a common-domain gate

## Result and status

A concrete, experience-respecting rival can agree with E-L about the physical four-spin system and its selected pair while disagreeing about *when* that pair's designated unpleasant contrast occurs. In the existing equilibrium kernel, the current-level and onset-only assignments disagree on exactly **71/448** of transitions. More strongly, two positive-probability histories have the **same complete current four-spin state** but different onset labels. Even an optimally chosen function of the entire current state cannot reconstruct those stipulated onset labels perfectly: its minimum error is **41/448** under the specified equilibrium distribution. These are exact mathematical results about toy assignments, not evidence that either assignment is felt, that spins are persons, or that nature lacks physical memory.

The comparison is informed by a real first-person finding: Alter et al. (2020) reported different pain-intensity ratings at the same final thermode temperature after different heat histories. That finding rejects a simple temperature-only description of those reports, not E-L's internal mismatch law. The article did not measure our q, and pain intensity is not itself a separately measured unpleasantness rating. No new empirical q test or bridge follows.

## 1. The common domain and two completed assignments

Reuse the [E-L sector](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) and the exact [horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md): at `t=1/4` the four-sign chain is sampled from its positive equilibrium distribution and advanced one random-site heat-bath update. In this section `t` is the coupling parameter, **not** a time coordinate. Let `s⁰,s¹` be successive ordered states, and `qᵏ=(1−s⁽ᵏ⁾₀s⁽ᵏ⁾₁)/2` for the left pair. The physical variables, kernel, L selector and assumed existence of the selected pair's field are the same in both packages. Supposing a field has a quality in a specified local episode is an additional assumption. It requires a persistence/episode bridge between the two states; the unchanged selector does not establish persistence.

Consider a binary contrast `U`, designated unpleasant versus neutral, not an exhaustive phenomenology:

- **E-L-level:** `U_level=q¹`. This is exactly the candidate's postulated pair contrast, within its restricted domain.
- **E-L-onset:** `U_onset=1` exactly when `q⁰=0` and `q¹=1`; otherwise `U_onset=0`. This alternative postulates an intrinsically unpleasant contrast specifically on the onset of mismatch, with a neutral designated contrast on the other three histories. The field remains experienced under both assignments. It is a deliberately sharp history-sensitive **formal rival**, not a claim that all relief or all valence is binary or onset-only.

Neither assignment follows from the physical mechanism or from the phrase experiential ground. These are competing interpretive proposals, not asserted genuinely possible worlds under the project's strong global modal thesis. They share the same stipulated physical transitions; no physiological or behavioral effects of U are automatically implied. We have not built a noncircular neural q, nor supplied a justified rule that couples U to reports.

| `q⁰ → q¹` | equilibrium probability | `U_level` | `U_onset` |
|---|---:|---:|---:|
| `0 → 0` | 295/448 | 0 | 0 |
| `0 → 1` | 41/448 | 1 | 1 |
| `1 → 0` | 41/448 | 0 | 0 |
| `1 → 1` | 71/448 | 1 | 0 |

The exact [program](verification/integrated_level_history_contrast.py) and [result](verification/integrated_level_history_contrast.json) recompute these entries from the underlying kernel and stationary distribution. They verify detailed balance transition-by-transition. Under equilibrium the positive and negative physical changes have the same probability, 41/448; the onset label nevertheless picks only positive change. In particular, the two quality assignments differ on persistent mismatch `1→1`, not on every mismatch transition. The 71/448 is the **unconditional equilibrium probability of their stipulated disagreement**, not a probability of an observed disagreement, pain or subject selection. These examples were constructed after the prior table was known, not preregistered predictions.

## 2. Stronger control: even the entire current toy state can be insufficient

The same endpoint `s¹=(1,−1,1,1)` occurs with positive joint probability following either:

- `s⁰=(−1,−1,1,1)`, `q⁰→q¹=0→1`, joint mass `27/4096`; or
- `s⁰=(1,−1,1,1)`, `q⁰→q¹=1→1`, joint mass `57/3584` (a no-change update).

Both have the identical complete present spin tuple. The onset assignment differs while the level assignment does not. The verifier groups transition mass by each of all 16 endpoint states and the onset label. For any deterministic current-state-only binary prediction, the minimum achievable error is the sum of the smaller label mass in each endpoint group, **41/448**. Independent randomization cannot reduce this Bayes error. This bound concerns predicting the *stipulated onset label*; it is not an assay accuracy, a model fit or a lower bound on prediction of actual affect.

It also does **not** prove that physicalism or every current-state account fails. Add a physical memory register or other degrees of freedom and the complete enlarged present state can encode prior history. An experiential law on an extended episode can likewise be redescribed as a law on such a state, if that enlargement and mapping are justified. An actual brain's states were neither measured nor matched in Alter et al. Equal current thermode temperature is vastly weaker than equal complete physical state. The finite construction shows a real information constraint for the specifically defined four-spin state, not an impossibility theorem for all state descriptions.

## 3. What the pain experiment actually establishes

[Alter, Aung, Strigo and Fields (2020)](https://doi.org/10.1371/journal.pone.0231124) tested 74 healthy volunteers. An individually calibrated T1 and T2=T1+1°C were used in randomized stepped and constant heat protocols. Subjects continuously rated **pain intensity** on a 0–100 mm scale, anchored at no pain sensation and the most intense pain imaginable. In the critical inverted protocol, T2 for five seconds was followed by T1 for five seconds and then T2 for twenty seconds; the control stayed at T2 for thirty seconds. At the same final T2, ratings after the decrease-and-rise were higher than during the constant control; their local-extremum contrast was **13.2 mm, 95% CI 9.3–17 mm**, using each participant's stepped-curve maximum and the control value at its corresponding time. The reported repeated-measures analysis for the final period found a protocol-by-time interaction. For offset and stepdown protocols the final temperature was T1 and ratings fell relative to a constant-T1 control. All comparisons match *target thermode temperature*, not independent internal states.

Important qualifications:

1. This is an existing group report, not a replication or our own raw-data analysis. The extrema-based contrast uses outcome-selected time points; the paper also reports time-series analyses. Do not replace a preregistered fixed-window test with a post hoc extremum. The authors' nonsignificant comparison of absolute onset and offset effects is not an equivalence test.
2. The final pain-intensity measure is not a separately assessed unpleasantness or positive relief measure. A change in intensity need not equal a change in hedonic valence. The paper's ratings are relevant experiential evidence without being an independent assay of the proposed binary quality.
3. Equal thermode set temperature is not equal tissue temperature, nociceptive input, neural state, q, expectation, attention or report dynamics. The randomized protocol changes whole histories. The authors discuss alternative temporal processes and offer a neural/predictive account as a hypothesis, not a demonstrated mechanism. Their T1 condition incorporated one calibration trial as a replicate; experimental order, site rotation and timing are described in their methods.
4. A rival in which prior stimulus changes *current internal q* can reproduce history-sensitive reports while preserving a current-q law. Conversely identical q could coexist with different context and reports. No contrast in this paper conditions on, manipulates or validates that q. It therefore tests neither `U_level` against `U_onset` nor a same-state brain-level law.

The [Dryad record](https://doi.org/10.7272/Q6028PSC) lists a 2020 ZIP archive. Its data and code were not downloaded or inspected here. We read the complete extracted published main text and captions; figure images, supplement and underlying data were not independently inspected. The source's prior model of perceptual change is not identified with our new toy postulate.

[Joffily and Coricelli (2013)](https://doi.org/10.1371/journal.pcbi.1003094) propose a negative *temporal derivative of variational free energy* as emotional valence and illustrate it in artificial-agent simulations. Our `q¹−q⁰` is a discrete difference in a binary spin mismatch, not their variational free energy, its derivative, a reported emotion-prediction error, or thermodynamic energy. A true derivative also requires a defined variable, time scale and regularity. The present onset-only assignment is not their model and is not a quantitative prediction of it. For that article we inspected extracted chunks 0–8 of 18, including abstract and models; equations rendered as images and those images and remaining chunks were not inspected.

## 4. A prospective discrimination, not an already completed experiment

The subsequent [first-person assay error gate](HISTORY_MISMATCH_FIRST_PERSON_ASSAY_ERROR_GATE.md) quantifies conditional report and physical-history classification tolerances, including what happens when only global error bounds or a full physical posterior are available. Its numerical calibrations are hypothetical.

Use the [crossed physical-history design](AFFECT_PREDICTION_ERROR_AND_MISMATCH_BRIDGE_GATE.md), but first resolve the stop conditions below. The primary endpoint would be a **current-episode unpleasantness report**, not pain intensity, measured with a declared neutral anchor, a validated scale and a preselected window. Separately acquire intensity and pleasantness/relief so that these constructs cannot be silently substituted. Use safe, ethically reviewed paradigms with informed consent and stopping rules; this is a research outline, not a prescription for administering painful stimuli.

**Before outcome access**, specify and independently validate: the candidate physical organization and q's preferred relation, measurement units/uncertainty, the measurement windows and temporal ordering, a defensible real-person subject/episode mapping, assay calibration and how report error can vary with history. Physical measurements and preprocessing must not be defined from the same target unpleasantness ratings used for evaluation. Specify an independent calibration sample, transformations, delay/response-lag handling, missingness, and blinded frozen pipelines. If q, its two levels, the subject bridge or report reliability cannot be established, **stop: no q-law comparison**. Do not call a stimulus, an EEG scalar, an expectation report or pain intensity q by definition.

Randomize history protocols with the intent of reaching the four measured `(q⁰,q¹)` cells, using multiple intervention types with different sensory and expectation side effects if feasible. Prespecify a quality-control and overlap rule: report numbers and uncertainty in all four measured cells, including measurement error and manipulation failures. The original heat study's cells are not those physical cells. Randomization balances assignment, not automatically measured post-assignment q; conditioning on a mediator can introduce selection/collider bias. If cell membership depends on outcome or unreliable q, the intended comparisons are not identified. Prespecify sensitivity analyses and stratified or hierarchical handling; do not present post-treatment cell contrasts as randomized effects of q.

With suitable independently validated and comparable assay distributions, the rival assignments imply:

| Matched physical comparison | Level assignment | Onset assignment |
|---|---|---|
| `1→1` versus `0→1` | same designated unpleasant contrast | neutral versus unpleasant |
| `0→0` versus `1→0` | same neutral contrast | same neutral contrast |
| `0→0` versus `1→1` | neutral versus unpleasant | same neutral contrast |

These are quality restrictions, not automatic equalities of raw reports when report channels, sensory contexts or subject identity differ. Predeclare allowable assay error and a smallest meaningful difference; use confidence/credible intervals and explicit equivalence margins rather than interpreting nonsignificance as equality. Use independent held-out participants or sessions for predictive evaluation, matched q-measurement coverage, and a shared calibrated observation model; allow a mixed `q¹` plus history model and context-sensitive alternatives. If strict level and strict onset both fail, that is a legitimate result. Choosing a threshold or report channel after observing which theory wins is not a test.

To move from associations to an intervention effect of q rather than history assignment, one needs additional causal identification, e.g. well-justified exclusion restrictions, measured confounding, or convergent interventions with appropriately modeled side effects. Expectation, attention, sensory input, arousal, physical memory, reporting behavior and other mediators can change together. A common calibrated report model is a substantive bridge assumption; if its validity or invariance fails, the observed difference cannot be attributed uniquely to quality. Held-out report prediction, even with causal evidence, cannot alone derive why the quality is intrinsically felt or choose experiential over neutral grounding.

## 5. What advances and what remains open

The comparison advances the project from a general appeal to history into a precisely contrasting experience-respecting package on the same finite physical domain. It demonstrates a matched full-current-state witness and a sharp reconstruction limit, and connects the design to real controlled first-person data without overstating that data. It supplies neither the requested ultimate derivation nor a test of the actual internal mismatch. B4–B5/F2 (subject and quality), B9/F3 (measure) and B10 remain open. C3 remains **full structural and experiential intelligibility**, jointly with C1–C7; a finite verifier passing is not a substantive battery pass.

Reproduce using `PYTHONPATH=verification python verification/integrated_level_history_contrast.py` and `PYTHONPATH=verification python -m unittest integrated_level_history_contrast_test`. No external data or nonstandard dependencies are needed for these two commands. The scripts use exact fractions and the existing stationary distribution and heat-bath transition; they do not independently derive those inputs from physical or experiential foundations.
