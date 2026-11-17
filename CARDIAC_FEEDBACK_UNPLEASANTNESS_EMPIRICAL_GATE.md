# Feedback direction, unpleasantness, and the mismatch proposal

## Decision

A second published dataset gives a useful **behavioral control** for a simplistic mismatch story, not a direct test of the project's proposed physical mismatch. In an exploratory participant-held-out comparison, adding the direction of assigned cardiac-feedback manipulation to stimulus level and trial position produced only a **very small change in overall unpleasantness-prediction error**. The assigned unsigned-deviation label also added essentially nothing to that metric.

The result does **not** say feedback has no effect: the original study found a faster-versus-slower effect in its interoceptive experiment using a different, within-person analysis. A small population-average effect can coexist with little improvement in individual trial prediction when individual differences and rating noise dominate. Nor does this study measure a neural channel's preferred phase, frustration or state excess. Treating assigned `Faster`/`Slower` labels as actual neural mismatch would be an unsupported substitution.

## 1. The real experiment and what it measured

[Parrotta et al. (2026)](https://doi.org/10.7554/eLife.90013.3) studied electrically evoked pain after auditory feedback. In one experiment, participants were told the sound represented their heart rate; in the other, it was presented as an external sound. During the feedback phase, the sound followed `Congruent`, `Faster` or `Slower` assigned conditions, based on each participant's earlier no-feedback baseline. Pain intensity was rated first; unpleasantness followed on a five-point scale whose lowest anchor was “no pain.”

The authors reported a faster-versus-slower difference in the interoceptive experiment and much weaker effects in the external-sound comparison. Their results and extensive mixed-model analyses precede this work; neither prediction of context effects nor a comparison of feedback directions is claimed as a new discovery. Their study also discusses expectation and bodily inference, not the project's proposed identity of an independently measured physical mismatch with a felt quality.

A crucial constraint: faster/slower feedback was constructed relative to an earlier baseline and changed over the trial. The workbook contains condition labels and average physiological summaries, not a validated continuously synchronized feedback-versus-current-heartbeat discrepancy. Moreover, the paper describes changes to **R–R intervals**; equal percentage changes in R–R intervals are not equal percentage changes in beats per minute. The two assigned non-congruent labels are therefore **not** verified equal instantaneous deviations in a common metric. `Congruent` does not prove zero deviation in a given trial. We use the labels as randomized-condition descriptors, not measurements of actual error.

## 2. The independent analysis plan

The [fixed plan](CARDIAC_FEEDBACK_PAIN_PREDICTION_PROTOCOL.md) was written after checking the workbook's schema and the published methods but before running the predictive calculations. It is retrospective, not a prospective preregistration or an independent dataset from the original paper. The source is the authors' [pinned GitHub workbook](https://github.com/EP171993/painperception/tree/c1c8721f0e3d00fefc602ed32b84e24c218c56d3), 537,743 bytes, SHA-256 `c186908c35e4819d2ea094fa339b4a9fc691556b13dc62585d12d09c6041bb02`; the repository declares an MIT license. Only aggregate results are stored in this repository, not the individual workbook records.

The workbook has 1,764 rows; the 630 no-feedback rows are not used here. The remaining **1,134 feedback trials** come from **63 people**: 34 interoceptive and 29 exteroceptive. All have 18 feedback trials and complete usable unpleasantness values; every participant has two trials per stimulus-level × feedback cell. The two experiments use different people. This sample is small, and 1,134 trials do not mean 1,134 independent people.

All models predict the same five-point unpleasantness report from a six-cell experiment × stimulus baseline and experiment-specific trial-position slopes. Each holds out whole participants in the same deterministic five folds. We compare additional group-specific features:

- **Unsigned label:** both faster and slower coded as 1, congruent as 0.
- **Signed label:** faster +1, slower −1, congruent 0.
- **Both labels:** the two contrasts together, spanning all three feedback categories within each experiment.

These are simple linear benchmarks, not physiologically measured discrepancies. Their limited fixed effects differ from the authors' mixed-effects models; in particular, they do not add feedback × stimulus × trial interactions. Neither individual baseline unpleasantness nor the intensity rating given immediately beforehand is used as a predictor. The numeric 1–5 treatment of an ordinal response is an approximation; results in these units are not cardinal measurements of suffering. Predictions are not clipped.

## 3. Held-out prediction

| Model | All trials RMSE | Interoceptive RMSE | External-sound RMSE | All trials MAE |
|---|---:|---:|---:|---:|
| Baseline | 0.84724 | 0.85402 | 0.83922 | 0.68450 |
| + unsigned label | 0.84727 | 0.85421 | 0.83907 | 0.68381 |
| + signed label | 0.84642 | 0.85257 | 0.83916 | 0.68377 |
| + both labels | 0.84643 | 0.85271 | 0.83901 | 0.68304 |

In this split, adding signed direction changes pooled RMSE by **−0.00082**, around **0.10%** of baseline. Both labels change it by **−0.00081**; the unsigned-only model changes it by **+0.00004**. These are tiny descriptive differences, not significance tests or a basis for asserting an ordering of true generalization performance. The outcome is discrete, trials repeat within people, folds share training data, and the group-specific models were trained and tested inside the same two published experiments. There is no independent cohort, confidence interval, calibration of experiential identity, or clinical-use claim. All predictions happened to fall within 1–5. Each participant contributes the same number of trials, so row-weighted and equally participant-weighted RMSE coincide here.

## 4. Balanced within-person descriptions

For each person and stimulus level, average each feedback condition, then weight the three stimulus levels equally and average across participants. All participants have all nine required cells. The two prespecified contrasts are faster minus slower and `(faster+slower)/2−congruent`:

| Experiment | People | Congruent mean | Slower mean | Faster mean | Faster − slower | Unsigned contrast |
|---|---:|---:|---:|---:|---:|---:|
| Interoceptive | 34 | 2.985 | 2.985 | 3.162 | +0.176 | +0.088 |
| External sound | 29 | 3.029 | 3.052 | 3.121 | +0.069 | +0.057 |

These are raw, unadjusted descriptions of the same reported study, not novel causal-effect estimates, equivalence tests or a reproduction of the paper's normalized ANOVAs and mixed models. The groups are separate participants; do not read the numerical difference between these two group contrasts as a tested interaction. The original authors' inferences use their own analysis and assumptions. A similar mean for two conditions does not establish equality.

The apparent tension between an interoceptive directional mean difference and the tiny held-out RMSE gain is important rather than contradictory: the first is a *within-person average contrast*, the second scores trial-level ratings of new participants without their personal baselines. They have different targets, variance and modeling assumptions. This test does not show that the paper's reported effect is unimportant or that feedback direction could never improve a more appropriate predictor.

An independent implementation reads the workbook's zipped XML rather than using `openpyxl`, and agrees on **all ten** reported group means and derived contrasts, as well as the group row counts; see the [cross-check receipt](verification/cardiac_pain_xml_crosscheck.json). It reads the same file, so this is a parsing/aggregation check, not new data or verification of the regression code.

## 5. Consequence for the experiential framework

A strictly symmetric label-only rule predicts identical values for faster and slower feedback **at the same stimulus, experiment and trial covariates**. That is a narrow operational comparator, not the user's general claim. In the unadjusted interoceptive sample the two mean reports differ, but the study does not independently establish identical actual physiological mismatch across the two conditions, and trial order, expectations, interpretation and other state changes matter. Consequently **this observation does not falsify a physical mismatch–experience identity**. Nor does it prove that faster or slower perceived cardiac feedback constitutes discomfort by mismatch.

The joint lesson from this and the [PAINgen benchmark](PAINGEN_UNPLEASANTNESS_BASELINE_AND_MISMATCH_GATE.md) is that an adequate account must contend with **input, context, evaluation and bodily state**, not just label a deviation “dissonance.” It may still posit a more specific internal relational mismatch, but must define the relevant system, channels, preferred states and temporal/subject boundary without choosing them from the outcome. The [state-contrast](STATE_MISMATCH_CONTRAST_AND_FALSIFICATION_GATE.md), [net-response](NET_RESPONSE_STATE_MISMATCH_WORK_GATE.md), and [coarse-graining](EQUILIBRIUM_MISMATCH_AND_COARSE_GRAINING_GATE.md) gates state different ways such an observable could fail to be identified. Passing a prediction test would be evidence for a specified model, not by itself a derivation of a phenomenological identity, a plural-subject criterion, or experiential fundamentality.

### Next empirical step—not yet done

A more direct cardiac-error test would need synchronized delivered audio-event times and ECG beat times, explicit handling of phase, rate, anticipatory adjustments, variable delays, units and participant awareness. It should compare independently specified signed and unsigned errors with stimulus, trial and cue interpretation baselines; use held-out participants and preferably an independent setting; and separately report missingness and calibration uncertainty. Even a valid cardiac feedback error would remain a **different candidate variable** from subject-internal phase frustration. The paper links raw ECG through OSF, but the corresponding exact delivered audio waveform/timing, and feasibility of the full comparison, have **not** been verified here. No additional dataset or intervention is claimed to be necessary to sustain the broader self-sufficient-whole thesis.

## Reproduction

Install `verification/requirements-cardiac-pain.txt` in an isolated environment, then run `python verification/cardiac_feedback_pain_predictions.py` and `python verification/cardiac_pain_xml_crosscheck.py`. Each downloads only the pinned workbook and verifies size and digest; each accepts `--data PATH` for a local identical copy. The [prediction receipt](verification/cardiac_feedback_pain_predictions.json) records folds, all four models and balanced summaries. These checks do not validate the experimental authors' original preprocessing, the subjective-report bridge, or the wider metaphysical and physical framework.
