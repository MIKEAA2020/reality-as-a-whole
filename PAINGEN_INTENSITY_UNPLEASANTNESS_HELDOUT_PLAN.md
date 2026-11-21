# PAINgen intensity–unpleasantness held-out comparison: fixed retrospective plan

## Question and scope

Does the separately recorded **condition-mean intensity report** provide a strong within-study, family-held-out baseline for the condition-mean unpleasantness report, and do the available NPS/SIIPS scores improve that baseline in this fixed linear comparison? This is a report-prediction and target-separation exercise, not a claim that the two experiences are identical, a measurement of the project's internal mismatch `q`, a trial-level analysis, or a forecast before ratings. The data and source study have already been examined, including their known high intensity–unpleasantness correlation and prior unpleasantness-only models. This plan precedes this particular calculation, but is retrospective, non-blinded and not an independent replication or preregistration.

## Input and eligibility

Use the author-provided condition-mean table, pinned exactly as in [the earlier study](PAINGEN_UNPLEASANTNESS_BASELINE_AND_MISMATCH_GATE.md), via `verification/paingen_unpleasantness_baselines.py`: commit `da46f2f9739ad2e9eeb9658711582be6357c1026`, 3,728,915 bytes, SHA-256 `0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56`. Require unique participant × centered modality × level × treatment keys, consistent family IDs, supported condition values and finite `Yint`, `Yunp`, `nps`, `siips`. Count excluded rows by required variable and overall; the per-variable missing counts may overlap. Do not exclude rows based on the observed difference between rating dimensions. For the matched comparison require both conditions to survive the same row screen. Report rows, people, families, cells and matched cells without publishing IDs or individual observations.

The source aggregates ratings by condition, not necessarily identical sets of trials; our prior verification does not establish a one-to-one paired-trial join, response timing, raw measurements or scanner preprocessing. Self-reports are evidence for experience, not infallible measures. The scale is not a cardinal physical unit, and the two prompts, order and response process may influence each other.

## Preselected models and split

Use the prior deterministic SHA-256 family split `fold_for` and its five folds, holding out every member and row of each test family together. Within each training fold estimate all coefficients and feature scaling. With one-hot indicators for the 12 modality × level × treatment cells and global slopes for predictors, fit ordinary least squares:

1. Condition only.
2. Condition + NPS + SIIPS.
3. Condition + `Yint`.
4. Condition + `Yint` + NPS + SIIPS.

All four models use identical complete rows and folds. Require full column rank and nonconstant training-fold features; stop rather than silently change models if either fails. Standardization is fit only on the training fold. These are simple linear benchmarks, not calibrated causal models, gold-standard measurement, individual clinical estimators, or claims that neural signals are physically independent from reports. Unclipped predictions are used; record their range and any outside [0,1], as a diagnostic, not proof of an invalid prediction.

Report pooled row- and family-weighted RMSE and MAE for all four, with differences between model 4 and model 3 (both ways of weighting). For family-weighted RMSE, average each family's mean squared error first, then take the square root across families. For MAE average each family's mean absolute error. No significance threshold, success declaration, or tuning is specified.

## Within-person contrast and uncertainty

For each complete participant × modality × level pair let `dU = U_control − U_placebo`, `dI = I_control − I_placebo`. In all matched pairs and separately by modality report pair-weighted means of `dU`, `dI`, and their difference `dU−dI`; also report `dU` and `dI` root mean squares and Pearson correlation where defined. The difference of numeric scale changes is descriptive only, not a measurement-invariant affect-specific effect: the rating scales are nonlinear, numerically distinct anchors do not validate a common metric, and treatment could alter both experiences, report criteria, or both. No equality of latent intensity is inferred from a nonsignificant result.

Compute matched `dU` predictions by subtracting the two **out-of-fold row predictions**, scoring each model with RMSE and MAE; these models were not separately fit to the contrast. All matching rows of one person share the same held-out family fold. A family bootstrap with 5,000 draws and fixed seed 1907 gives exploratory percentile intervals for the pair-weighted mean `dU−dI` overall and by modality, sampling all matched rows in families together. Separately, bootstrap the family-level squared-error differences between models 4 and 3 on the already computed out-of-fold predictions; give the resulting interval for the difference in pooled row RMSE, with no refitting. The latter is conditional on the fitted folds, not a full nested-CV uncertainty interval: test folds share training sets and effects of refitting are omitted. Stop on any empty category or bootstrap denominator, do not invent results.

## Interpretation and limits

- A strong intensity-report baseline would not show unpleasantness is reducible to, or identical with, intensity; the predictor is another subjective report on related condition averages, not an independent physical assay. Model 4 may improve less than model 2 because much of the same information is already present in intensity; no unique mechanism follows.
- An average difference or predictive increment is neither a selective intervention on affect nor an identification of `q`, phenomenological unity, causal mediation, aspect ontology, or the privileged intrinsic basis of experience. An interval crossing zero does not establish equivalence; group or pair means do not imply identical changes for every person or trial.
- The paired estimates are descriptive of selected complete condition means, with family dependence and possible selection bias; no independent cohort or generalization to new protocols is established. Neither rating is treated as a prior measure available for a real-time prediction. Future cross-context tests need raw synchronized trials, separate response instructions, candidate-specific independent physical measurement, prespecified report-error handling and appropriately held-out people and settings.
