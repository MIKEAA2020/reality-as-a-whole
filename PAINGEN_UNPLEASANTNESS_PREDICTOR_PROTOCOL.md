# Pain unpleasantness: fixed secondary-analysis plan

## Purpose and scope

This plan precedes running the calculations in its companion verifier. It is a **retrospective exploratory secondary analysis of published, already-analyzed data**, not a preregistration, a new independent study, or a test of a neural-frustration model. The source is Botvinik-Nezer and colleagues' [2024 placebo study](https://doi.org/10.1038/s41467-024-50103-8), using their released condition-level table at the [pinned repository commit](https://github.com/rotemb9/paingen-placebo-fmri-paper/tree/da46f2f9739ad2e9eeb9658711582be6357c1026). They studied 392 people, including twins. The article already analyzes this dataset and its predefined brain signatures; our prediction comparison is not independent confirmation of the paper.

The question is limited but consequential: **what can stimulus, context and existing brain-signature baselines predict about unpleasantness reports across held-out families?** A proposed relational misalignment measure would need to add value against such baselines and be independently identifiable. This table does not provide the relevant phase-interaction channels, so we will **not calculate or fit a frustration measure**, equate fMRI signatures with frustration, or infer that a predictor is identical with experience.

## Fixed inputs and protection of participants

Use only `pain_evoked_brain_measures.csv`, 3,728,915 bytes, SHA-256 `0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56`, from commit `da46f2f9739ad2e9eeb9658711582be6357c1026`. The repository's MIT license covers its distributed software/materials, but source licenses and primary data rights should not be conflated. To avoid duplicating participant and family identifiers in the public project, fetch the single pinned file on demand or accept a local copy, check its digest, and retain only **aggregate results** in the repository. No images, raw fMRI, demographics or other data files are required.

The source reports `Yunp` (mean unpleasantness rating), `nps`, `siips`, `stimLvl`, `heat`, `prodicaine`, participant ID and family ID. These are averaged **condition-level rows**, not individual trials. The brain-measures file uses centered condition codes: `heat∈{−0.5,+0.5}`, `prodicaine∈{−0.5,+0.5}`, `stimLvl∈{−0.5,0,+0.5}`. Check the values and unique participant–condition keys; keep only rows with finite `Yunp`, `nps` and `siips` and a nonempty participant and family ID. Verify one family per participant. Treat IDs as opaque, never emit them. Family grouping is essential because relatives, including twins, are not independent held-out people.

## Fixed prediction plan

Use five folds defined by SHA-256 of `paingen-family-split-v1:` plus the exact source family-ID string, interpreted as a hexadecimal integer modulo 5. Every condition and every person from a family must be in the same fold. No training on test-family labels. Using a deterministic split does not make this retrospective analysis prospective or make the folds independent replications.

For each fold, fit ordinary least-squares models to the remaining families. The fixed baseline has **12 condition indicators** for the fully crossed modality × stimulus level × treatment categories, without a separate intercept. For the signature models, standardize each signature using the training rows' mean and population standard deviation, then append:

1. condition indicators only;
2. indicators + NPS;
3. indicators + SIIPS;
4. indicators + both NPS and SIIPS.

No participant identity, age, sex or outcome rating `Yint` is an input. A simultaneous intensity report is not a prestimulus predictor and might share response variance with unpleasantness. NPS and SIIPS are prespecified *established neural summaries*, not channel-identification methods or our newly discovered mechanisms. The paper-derived fMRI maps and model's same-study context matter: evaluation is out-of-**family** but not out-of-study, scanner, protocol, or independent cohort. Condition labels are known experimental predictors, not a neural assay.

Compute out-of-fold predictions for the same complete-case rows. Report row-weighted RMSE, MAE and Pearson correlation, plus family-averaged RMSE (square root of the mean of family mean squared errors). These are descriptive out-of-fold metrics. Include improvement over the condition-only model as a raw RMSE difference, not a proof of neural specificity. This measures condition-average prediction, not trial-level accuracy or diagnostic use.

## Within-person placebo contrasts

For each participant × modality × stimulus level, retain a pair only when both placebo and control rows survive the complete-case filter. Compute target and each out-of-fold model's prediction as **control minus placebo**, then report RMSE and Pearson correlation for all matched pairs and separately for thermal and mechanical pairs. Both arms of a pair belong to one family and are held out together. A zero-effect prediction is a transparent benchmark for these contrasts. Do not use the measured intensity rating or the target person's own unpleasantness values to construct a prediction.

These are descriptive held-out *prediction* contrasts—not the paper's preregistered mixed-effects causal analysis, not independent new trials, and not an estimate of an unconfounded treatment effect. The study's conditioning, treatment sites, run order and other context matter. Repeated conditions and related participants preclude treating pairs as independent people. No hypothesis tests, confidence intervals or clinical effect estimates are planned here.

## Intended interpretation and stopping rules

- Report all four candidate models and both modalities, even if signatures do not improve performance. Do not tune features, exclusions or outcome thresholds after seeing the results.
- Inspect actual field encodings and sample attrition; if the stated schema, unique keys or family mapping fail, stop rather than silently alter the plan.
- Predictor associations with reported unpleasantness do not by themselves establish mechanisms, individual phenomenal identity, independent assay error, subject boundaries or experiential ground. NPS and SIIPS measure particular fMRI patterns, not the proposed network preferred phase offsets or channel-level mismatch.
- No raw participants' ratings or identifiers, imaging or demographic values should be added to the public repository. Publish aggregate data receipt, code and source provenance only.
- These observations cannot decide whether the neutral-ground and experiential-ground rival accounts share their phenomenology by identity or constitution.

Follow-up after results must be clearly labeled post-analysis. A true discrimination test would require a prespecified physical mismatch observable with individually calibrated channel selectivity, suitable interventions or other identifiable dynamics, and independent experiential/behavioral measures. On the present inputs, the misalignment identity is **unidentified**, not confirmed or refuted.
