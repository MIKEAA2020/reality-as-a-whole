# Cardiac-feedback pain data: fixed exploratory comparison

## Question and nonclaims

Using a small, published, trial-level dataset, compare whether **direction** of the assigned feedback condition predicts unpleasantness differently from an unsigned **condition label** for both faster and slower feedback. This is a retrospective, exploratory secondary analysis, not a preregistration or an independent replication. It is not a direct test of the project's relational channel mismatch: the derived labels do not measure actual feedback–heart-beat error, neural phase frustration, or state excess. We do not know that a congruent label means zero error on any individual trial.

Source: Parrotta et al., [*Exposure to false cardiac feedback alters pain perception and anticipatory cardiac frequency*](https://doi.org/10.7554/eLife.90013.3), and their [pinned repository](https://github.com/EP171993/painperception/tree/c1c8721f0e3d00fefc602ed32b84e24c218c56d3). In the interoceptive experiment the auditory cue was presented as heart feedback; a separate exteroceptive experiment used non-heart sound. The authors already compare faster and slower cues and use extensive mixed models. These data are not new or independent of those findings.

Feedback was personalized to a prior no-feedback baseline, not instantaneously matched to the participant's ongoing heart rate; the source paper describes a gradually changing R-R interval. The workbook does not contain a validated sample-by-sample realized feedback–heartbeat discrepancy. A binary `different` label encodes only the intended condition, not a physically calibrated magnitude; it must not be called an actual prediction error. R-R changes do not translate linearly into equal-and-opposite bpm changes. Participants rated intensity before unpleasantness, and the unpleasantness lowest anchor was `no pain`: report and order effects are relevant.

## Data and access

Fetch only `Data_v3 - 2504.xlsx` from commit `c1c8721f0e3d00fefc602ed32b84e24c218c56d3`, exact 537,743 bytes, SHA-256 `c186908c35e4819d2ea094fa339b4a9fc691556b13dc62585d12d09c6041bb02`. The author's repository declares an MIT license; avoid copying the underlying individual records into this public project. Read only sheet `Data`; use fields `Exp`, `SSID`, `Session`, `Trial`, `Feedback`, `StimInt`, `LIK`. Do not use outcomes `VAS` or participant-specific baseline pain in features. `LIK` is the 1–5 ordered unpleasantness report; treating it as an interval scale for RMSE and averaging is an approximation, not a claim of cardinal phenomenal units.

Primary selection: `Session=2`, `Feedback` in `Congruent`, `Faster`, `Slower`, and `StimInt∈{2,3,4}` (the feedback phase). Verify experiment categories `Intero`, `Extero`, valid finite outcome and trial values, participant IDs, valid condition keys and that each participant belongs to only one experiment. Fail if schema/condition consistency fails. Exclusions/missing cells must be counted. Do not change the feature set after observing results. No calibration from test participants' current or other unpleasantness values. Participant identifiers stay in memory and never appear in results.

## Fixed held-out comparison

Assign each participant to one of five folds with SHA-256 of `cardiac-pain-participant-split-v1:` plus its canonical workbook ID (numeric integer converted to decimal string); interpret digest as an integer modulo 5. Keep all trials from a participant together. Within each fold, train ordinary least squares on other participants and predict held-out participants. This is **out of participant**, not out of study, cohort, laboratory or publication; the split is selected retrospectively and is not a new prospective study.

All models include six indicators for experiment × calibrated stimulus level and two terms for `Trial` × experiment. The original workbook already centers trial; use the recorded value without outcome-based adjustment. Add the following predeclared group-specific features:

1. **Baseline:** no feedback term.
2. **Unsigned label:** `different=1` for Faster or Slower, 0 for Congruent, with separate coefficients for each experiment.
3. **Signed label:** `direction=+1` for Faster, −1 for Slower, 0 for Congruent, with separate coefficients for each experiment.
4. **Both:** all the unsigned and signed terms above. These two contrasts span the three categorical feedback labels, separately for each experiment.

All models use the same rows and folds; no tuning, participant intercept, normalization from a held-out participant's outcomes, or simultaneous intensity rating. Do not clamp predictions or fit per-condition functions after evaluation. Train `Trial` and condition features in raw source scale; the unit and timing of `Trial` are as recorded, not assumed to be seconds. Check rank in every fold. Report pooled and experiment-specific trial RMSE, MAE, correlation, plus subject-averaged RMSE. Include all four models even if null or counterintuitive. Because differences in out-of-fold errors may be small and folds share training data, do not claim a statistically significant improvement without a valid uncertainty analysis. Numeric predictions can extend outside the 1–5 scale; count them rather than hiding them.

## Predeclared descriptive contrasts

For each participant and each of the three stimulus levels, compute the average `LIK` for each feedback label. Require at least one row in **all three** conditions at each level; if a participant is incomplete, exclude them from these paired contrasts and report counts. Compute the equally weighted across-level mean for each label and the following contrasts, averaged equally across complete participants, separately in each experiment:

- faster minus slower (directional contrast);
- `(faster + slower)/2 − congruent` (unsigned-label contrast).

The counts of people and usable cells must be shown. These are simple descriptive unadjusted within-person condition contrasts, not the authors' normalized ANOVAs, their mixed-effects estimates, a separately replicated finding, or proof of an isolated causal mediator. The participants' ordering and adaptation can matter even with randomized condition order. The two experiments have different participant groups and may have other procedural differences. Do not call a non-significant contrast equivalent; no hypothesis tests or confidence intervals are planned here.

## Stop / interpretation

Inspect integrity and fold composition; fail on unknown encodings, missing essential columns, duplicate grouping ambiguity or rank deficiency rather than silently repairing. Do not infer that all mismatches cause suffering or that the channel-level conjecture fails from a signed-vs-unsigned condition comparison. A dataset can challenge an overly simple fixed unsigned-feedback-label predictor without testing the physical identity hypothesis. Any claimed physical intervention comparison requires attention to actual cue timing, pulse timing, frequency units, participant interpretation, common input and the independent measurement gap.
