# What does a no-report rivalry study actually calibrate?

## Decision

[Frässle et al. (2014)](https://www.jneurosci.org/content/34/5/1738) provide useful **human evidence that eye signals track reported rivalry and that an fMRI rivalry–replay contrast depends on the report condition**. The study is an important challenge to treating every frontal signal observed during reported rivalry as a neural correlate of perception alone. But it does **not** demonstrate that passive-viewing eye signals retain the same error rates against experience, that conscious perception requires no frontal activity, or that any specific neural region is unnecessary for experience. Its direct comparison is informative, but its interpretation depends on how report, attention, rivalry dynamics and measurement change together.

This is a source audit, **not an independent analysis or replication**. I read the primary paper's methods, results, discussion and figure captions, the substantive text of [Zaretskaya and Narinyan's 2014 commentary](https://doi.org/10.3389/fnhum.2014.00527), the abstract of [Naber et al. (2011)](https://doi.org/10.1371/journal.pone.0020910), and the [Nichols et al. conjunction-method summary and abstract](https://www.nisox.org/research/ValConj/). I did not inspect the underlying participant data, fMRI maps, original code or a statistical design file. Reported results below are the paper's, not new estimates. The later [Roy–Jamison dataset assessment](RIVALRY_EEG_FMRI_FEASIBILITY_AND_REANALYSIS_GATE.md) concerns a **different experiment**.

## 1. What was done

Twenty healthy adults took part in an fMRI experiment with eight conditions: two stimulus/indicator types × rivalry versus physical replay × active report versus passive viewing, four 60.9-second trials per condition. For moving gratings, **optokinetic nystagmus** (OKN)—the slow phase of an eye movement—provided a proxy for motion direction. A separate set of static, differently colored, oriented and luminant gratings used **pupil size** as a proxy for which brightness was dominant. The channels were not simultaneous independent measures of one identical stimulus or target.

In rivalry, different images were delivered to the two eyes. In replay, the same image was delivered to both eyes and physically alternated; replay timing came from button presses in the preceding active-rivalry trial. This matched a temporal sequence, not the full spatial or experiential dynamics of rivalry. In active trials participants continuously held one of two buttons for the **most dominant** percept, even if both were partly visible. Most later mentioned piecemeal rivalry; binary compliance therefore is not evidence that perception was always binary. Passive trials had no ongoing report.

Within each stimulus type, trial order repeated **active rivalry → active replay → passive rivalry → passive replay**. The order of the two stimulus-type sessions was balanced across observers, but this four-condition sequence was fixed. Thus condition can be entangled with time, carryover, expectation and order; counterbalancing stimulus type does not counterbalance this sequence. The matched replay is useful, but it also ties each passive replay's switching schedule to an earlier active trial rather than the immediately preceding passive experience.

## 2. What the behavioral comparisons show

The paper reports the following **time-fraction agreement with buttons**, using each participant's optimal lag selected from 0–2 seconds. Values are reproduced as printed, including ± notation; they are not independent, held-out classifier accuracies against experience.

| Active-report condition | OKN and button agreement | Pupil and button agreement |
|---|---:|---:|
| Rivalry | `82 ± 2%` | `59 ± 1%` |
| Physical replay | `88 ± 2%` | `83 ± 1%` |

The difference between the pupil values is particularly relevant to transport: a channel's agreement in physically alternating replay is not automatically its agreement in rivalry. The two channels also differ materially in rivalry. The authors report greater-than-chance agreement and report-aligned eye traces consistent with perceptual transitions. This supports their use as **imperfect, task-specific proxies**, particularly the OKN in this sample. Optimization of each participant's lag on the evaluated data can make the descriptive agreement optimistic for a new sample or frozen decoder; without the raw data and split details, its size cannot be calculated here. The aggregate is not a class-specific sensitivity or false-positive rate and does not estimate those rates against the actual experience.

For rivalry, the reported average optimal eye-to-button lead was `0.52 ± 0.07 s` for OKN and `0.42 ± 0.12 s` for pupil. The physical-switch replay provided further timing comparisons, but the actual experienced transition time during rivalry is not separately known. A lead relative to a button is not by itself a direct measurement of phenomenal onset.

The paper also reports median dominance duration from eye measures during active versus passive rivalry: OKN `1.57 ± 0.14` versus `1.58 ± 0.17 s` (`p=0.79`); pupil `1.48 ± 0.04` versus `1.57 ± 0.05 s` (`p=0.004`). These are published comparisons, not new effect estimates or error bounds. The pupil result is compatible with changed dynamics, a changed measurement channel, or both; it does not isolate the mechanism. The nonsignificant OKN comparison does **not** establish equality or a negligible difference. The article interprets the pupil result as reporting influencing rivalry dynamics, while noting attention as a possible mechanism.

## 3. What the fMRI contrast supports

For each indicator, the central comparison was a **difference of rivalry–replay contrasts**:

```text
(active rivalry − active replay) − (passive rivalry − passive replay).
```

Regressors used the continuous eye traces transformed to emphasize zero-crossing-like transitions and convolved with a canonical hemodynamic response. The authors found rivalry-related occipital and parietal activation in passive viewing, along with a right inferior orbitofrontal locus; the thresholded middle-frontal pattern seen with active report was not found in the passive map. They also tested the direct difference rather than relying only on one map being significant and another not. The authors interpret the reduced frontal contrast as evidence that monitoring/reporting contributes to the reported-rivalry pattern and as casting doubt on a driving role in initiating switches. That interpretation is meaningful, but BOLD association and this task comparison do not by themselves establish the causal role or necessity of a particular region.

Important limits:

- The difference-in-differences rules out a simple **identical additive** motor effect common to rivalry and replay within each report condition. It does not rule out motor, attention, task, conflict, timing or eye-signal effects that interact with rivalry. Active reporting also entails percept monitoring and motor action; these are not separately manipulated.
- The authors describe their across-indicator analysis as a **global-null conjunction**. Figure 3A/B maps use cluster `p<0.01` FWE with voxel `p<0.001` uncorrected, while the reported Figure 3C conjunction is **`p<0.001` uncorrected**. Do not transfer the corrected map threshold to the conjunction. A global-null conjunction rejects the hypothesis that all included effects are null; it is not, by itself, a valid logical-AND demonstration that the contrast is independently significant for **both** stimulus types. The [Nichols et al. account](https://www.nisox.org/research/ValConj/) explains why the conjunction null must instead be tested for that claim. This methodological caution does not establish that either individual effect is absent, nor that the authors' results are false; the separate statistics and analysis would need inspection.
- A missing thresholded cluster is not evidence of zero activity, equivalence, or no necessity. A non-significant difference between indicators is also not an equivalence test. Zaretskaya and Narinyan note that other frontal loci were not significantly reduced and that attentional differences could contribute; lack of a significant reduction also does not establish those areas' causal contribution. The original authors themselves qualify that they cannot fully exclude a role for frontal areas in some forms of rivalry.
- The replay and rivalry stimuli differ physically and phenomenally, and image analysis measures BOLD contrast, not direct neuronal causation or felt quality. Fixed order, changing task demands, imperfect alignment, correlated regressors and stimulus-dependent proxies limit attribution to a single process. No numerical distortion or causal bias is estimated here.

## 4. The specific calibration gap

Let `E` be a carefully specified experienced dominance contrast, `R` the button report and `Y` an eye-based classification. The study supplies evidence about `P(Y=R | active rivalry)` after a participant-optimized time shift, not an externally verified `P(Y≠E | passive rivalry)`. First-person experience is a genuine datum for the participant, and their report is important evidence; transmission, mixed states, timing and attention can still complicate the mapping to a binary, timestamped external label.

Three distinct claims must not be substituted for each other:

1. **Active report–eye agreement:** supported descriptively for the tested tasks, subject to the paper's timing selection and binary coding.
2. **Active eye–experience error:** needs an additional justified relationship between the timestamped report and the specific experienced contrast. Agreement alone does not give an independent ground truth or separate false-positive and false-negative rates.
3. **Passive eye–experience error:** additionally needs target-condition calibration or a warranted transport bound. Passive experience is not continuously reported in the original design. Changes in attention, piecemeal dominance, latency or oculomotor responses could change the channel; this possibility does not show that it actually did.

The previous [randomized contrast analysis](RANDOMIZED_EXPERIENCE_CONTRAST_PARTIAL_IDENTIFICATION.md) assumed common sensitivity and false-positive rates across arms. This paper does not provide those quantities for the passive condition, and its behavioral contrast concerns dominance durations, **not** the invented positive-response probabilities in that analysis. We cannot insert `82%` as the sensitivity, `18%` as the target experiential error, or the reported `p` values into those bounds. Likewise, the 10% decoder–report disagreement target in the [random-audit proposal](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) is a different, conservative estimand and prospective threshold; the published 82% optimized agreement is not a formal test of it.

The eye signals are physical measurements, not unmediated observations of experience; equally, their imperfection does not make passive perception illusory or license dismissing participants' testimony. These results do not address whether bacteria or machines experience anything, nor do they determine subject count, token identity or a phenomenal quality map.

## 5. A sharper next test

A new, ethics-reviewed, consenting human study could test parts of the missing chain without pretending to directly observe a fully unreported episode:

1. **Separate development and evaluation.** Prespecify motion or brightness, target window and mixed/uncertain state. On development participants or runs, fix filtering, thresholds, lag and decoder; evaluate on held-out participants or runs with no test-label tuning. Report all eligible time, missingness, class-conditional agreement and confidence intervals accounting for participant and temporal dependence. Test each indicator only for its matching stimulus; don't pool them as independent probes of an identical trial.
2. **Randomize the block order and audit schedule.** Compare continuous-report, *prompt-possible* sparse randomized post-window report, and genuinely no-prompt blocks. Reveal audit draws only after their target windows. Randomize or counterbalance order and account for carryover. Specify the prospective estimand and report delays, uncertain and mixed responses. Replay controls should be specified and matched without turning the comparison into a fixed sequence; replay remains a physical control, not phenomenal ground truth.
3. **Test operational drift, not an unavailable oracle.** In prompt-possible windows, compare frozen `Y` to randomly sampled reports and quantify how that agreement changes across carefully defined contexts; measure latency, mixed-state rate and eye-signal distributions. An observable discrepancy can challenge a proposed stability model. Similar observed distributions or report agreement, however, cannot prove equal `P(Y|E)` or rule out shared error. Participants expecting possible prompts may attend differently from those in genuinely no-prompt blocks, so extrapolation to the latter remains a separate assumption.
4. **Predefine competing fMRI predictions.** Specify a small set of independently defined regions and an active/passive rivalry–replay interaction, including plausible changes to the eye regressor, replay mismatch, attention and uncertainty. Analyze each indicator's effect and appropriate multiplicity correction, and use a conjunction-null procedure if claiming evidence for both. Use equivalence bounds, not nonsignificance alone, when the question is practical absence. fMRI correlations alone do not prove neural necessity.
5. **Stop at the warranted conclusion.** If target-valid error bounds or transport cannot be justified, report the operational findings and the unresolved experience bridge. Any hypothetical causal neural intervention would need separate safety, specificity and ethical justification; this proposal does not require one.

**Bottom line for the project:** this source strengthens the case that measured report-related processes matter, and supplies real constraints a proposed assay must respect. It does not close the mapping from organized processes to experiences or subjects. More precise data and a better design could narrow the uncertainty; the remaining first-person and transport premises must still be named.
