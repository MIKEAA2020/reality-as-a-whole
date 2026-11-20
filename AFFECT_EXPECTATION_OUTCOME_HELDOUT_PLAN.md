# Fixed retrospective analysis: valence, expectation and social choice

This analysis plan was written after reading the published Heffner study, the Vollberg–Cikara reanalysis, and inspecting source filenames, column names, category encodings and author preprocessing code, but **before** calculating the predictive comparisons below. It is retrospective: the studies and the competing result were already published, so this is not a prospective preregistration, independent confirmation, a new discovery of the comparison, or a direct test of neural mismatch or pain. No outcomes are used to set thresholds or select this plan.

## Question and source

Use only experiments 1 and 2's emotion-and-reward Ultimatum Game files and accompanying emotion-classification files from [Heffner et al.'s published data and code](https://github.com/jpheffne/epe), commit `3031323d4140067b102d6db4fc5e7312038fa745`. Check exact file digests in the verifier. The original team excludes participants whose separate neutral emotion label is outside `[-50,50]` on either dimension; reproduce that criterion for this comparison. Study 2's reward-only group is not included because it does not provide the same emotional reports. The source data are already cleaned, not raw task recordings. The repository declares no license, so this project will save only code and aggregate outputs, not the participant data.

## Frozen comparison

For each experiment independently, predict binary recorded choice in a held-out participant from complete rows with reward prediction error `R`, predicted valence `P`, and post-offer reported valence `V`. Authors define emotion prediction error `D=V−P`. Study 1 uses source RPE; study 2 uses authors' reconstruction `R=(100−offer)/100−RP`. This is a comparison of **reports used to predict a later choice**, not a prediction of valence, an independent readout of experience, or a biological measurement of discrepancy.

Fit four standardized, fixed-regularization logistic models (intercept unpenalized):

1. `R` only.
2. `R + D`: signed affective-report difference.
3. `R + V`: post-offer valence report.
4. `R + P + V`: both constituent reports; compare against models 2 and 3.

Use a common complete-case sample and the same five subject-disjoint folds for all models. Sort participants by SHA-256 of `experiment:subject` and distribute sorted indices round-robin into folds, without using outcomes. Training-only z-score each feature (zero-variance features fail explicitly). Minimize mean logistic loss plus `0.01/2` times the squared non-intercept coefficients, initialized at zero, using BFGS with fixed settings. This penalty and optimizer are not tuned using test data. Outcomes are clipped to `[10^-12,1−10^-12]` only when scoring log loss.

**Primary score:** mean of each person's mean out-of-fold log loss. Report the corresponding Brier score, pooled trial-level log loss, number of people and observations, and each model's event rate. Report the paired per-person mean log-loss difference `D-model − V-model`; positive means the V model predicts better. Use 2,000 resamples of entire people, fixed seed 1729, separately per study, for a percentile interval of this descriptive out-of-fold difference. Training folds overlap: this interval resamples fixed out-of-fold predictions and does not include model refitting or all training-sample uncertainty. If the interval is broad or crosses zero, do not assert a reliable ordering. There is no adjustment for the two experiment-specific comparisons; treat both as exploratory.

Report explicitly that the joint linear model `R + P + D` and `R + P + V` span the same unpenalized predictor space because `D=V−P`; coefficients are reparameterizations, not independent evidence for an error signal. Regularization can break exact fit equivalence unless its penalty is transformed accordingly. The two one-variable models are not equivalent, and the joint model can improve prediction without establishing either coefficient's causal role. Keep any out-of-range predictors, missingness, duplicate exclusion records or failure to converge visible; do not silently change the models.

## Interpretation and stopping rule

Do not use a post-offer valence report as an independent assay for q, nor count its ability to predict another report or choice as an experiential-identity test. A lower loss for `V` than `D` is consistent with the prior reanalysis but does not disprove every prediction-error, friction, misalignment or experiential-ground theory. If `D` wins, it does not establish that mismatch is intrinsically unpleasant. Both competitors can pick up the same latent process, measurement noise, task instructions and decision/report coupling. Without a separately justified physical `q`, this dataset **cannot** test the user's proposed identity. If data decoding or eligibility is ambiguous, stop and disclose instead of fitting a different target.
