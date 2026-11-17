# Unpleasantness: empirical baselines and the missing mismatch measurement

## Result in brief

A family-held-out analysis of a published pain/placebo dataset provides a benchmark for the proposed experiential-misalignment framework, but **does not test the proposed mismatch–experience identity**. For 4,380 complete participant-condition means, a model using experimental condition alone had out-of-family RMSE **0.1537** on the source `Yunp` scale. Adding both established fMRI signatures reduced this to **0.1441**. These are exploratory predictions within one published study, not evidence that the signatures are frustration, or that experience is fundamentally experiential rather than neutral.

The important advance is a sharper empirical boundary: **a name for mismatch cannot do the work of an independently identified mismatch measurement**. The available table supplies condition means and signature scores, not the phase-resolved interactions, preferred offsets, selective perturbations or independently calibrated readout needed to measure the proposed channel-level mismatch. Nor can a discrepancy between a reported treatment expectation and an experimental stimulus be treated as that mismatch without a new, justified measurement model. A later [separate cardiac-feedback study analysis](CARDIAC_FEEDBACK_UNPLEASANTNESS_EMPIRICAL_GATE.md) compares directional and unsigned condition-label predictors, without claiming that either directly measures neural mismatch.

## 1. What is established already

[Botvinik-Nezer et al., *Nature Communications* 15, 6017 (2024)](https://doi.org/10.1038/s41467-024-50103-8) report a large placebo analgesia experiment in 392 participants, including twins, with thermal and mechanical pain. They report robust placebo analgesia and differences between their nociceptive and more evaluative fMRI measures. They explicitly caution that unpleasantness and intensity ratings are strongly correlated; SIIPS should not automatically be labeled an affect-specific pain measure. Their study and the literature it cites already develop expectation, cognitive evaluation and pain prediction. This report does **not** claim to discover placebo analgesia, predictive coding, the signatures or their relationship to pain.

The shared [source repository](https://github.com/rotemb9/paingen-placebo-fmri-paper/tree/da46f2f9739ad2e9eeb9658711582be6357c1026) describes intensity and unpleasantness ratings averaged within each participant, condition, modality and stimulus level. Its `expectation_data.csv` is expected **Prodicaine efficacy**, measured after conditioning and before scanning. That one treatment-efficacy expectation is not a trial-specific prediction of stimulus intensity, is not on the same scale as the received stimulus, and is not a direct measure of channel mismatch. We therefore did **not** subtract it from a stimulus or pain report. Using a post-stimulus outcome to manufacture a prediction error would also risk outcome leakage.

Two fMRI summaries are used as established comparators: NPS, associated with nociceptive pain processing, and SIIPS, developed to predict pain beyond stimulus intensity. They are not individually selective phase channels. fMRI and condition-level reports correspond to the same condition; these are concurrent/post-stimulus associations, **not forecasts available before stimulation**. The article provides the experimental interpretation and limitations; this project did not recompute fMRI maps from scans.

## 2. What was done

The [analysis plan](PAINGEN_UNPLEASANTNESS_PREDICTOR_PROTOCOL.md) was written after inspecting the source schema but **before running the prediction analysis**; it is retrospective, not a public preregistration. The authors' study was already published and its data accessible, so it is not a blinded discovery. The [verifier](verification/paingen_unpleasantness_baselines.py) downloads or reads a single 3.73 MB pinned table, verifies its exact SHA-256, and produces only [aggregate results](verification/paingen_unpleasantness_baselines.json). No raw images or participant-level records are published here.

From 4,687 source rows for 392 people in 243 families, 307 rows with incomplete required outcomes/predictors were dropped. This leaves **4,380 rows, 376 people and 237 families**. Missingness is not assumed random, and these condition means are not independent trials. A deterministic five-fold hash partition holds out entire families, including all observations for relatives. Every model uses the same complete rows and the same folds. Each regression uses training-fold coefficients and, where needed, training-fold signature scaling; no person-level or outcome information from held-out families trains that model.

Baseline is 12 condition cells (modality × stimulus level × treatment); three fixed alternatives add NPS, SIIPS, or both. The table below reports out-of-fold row-weighted RMSE and Pearson *r*; family-weighted RMSE gives every family equal weight after averaging its rows' squared errors. Lower RMSE is better. Scale is the numeric `Yunp` field as provided, not a calibrated physical unit.

| Model | Row RMSE | Family RMSE | Row Pearson r |
|---|---:|---:|---:|
| Condition only | 0.1537 | 0.1584 | 0.175 |
| Condition + NPS | 0.1504 | 0.1544 | 0.266 |
| Condition + SIIPS | 0.1458 | 0.1496 | 0.356 |
| Condition + both | 0.1441 | 0.1475 | 0.384 |

Both signatures together reduce row RMSE by **0.0096**, or approximately **6.2%**, relative to condition alone, for this particular split and sample. The numbers are descriptive, without uncertainty intervals or a claim of statistical significance. Grouped cross-validation protects family separation here, but is not a held-out independent study, new scanner, protocol, population or publication. The training origin of published signature maps and any possible overlap with source studies must be checked before making a broader independence claim. Squared-error performance does not establish clinical usefulness.

## 3. Within-person condition differences

For each participant × modality × stimulus level with both conditions available, subtract placebo from control in both the observed mean and the held-out model predictions. There are **2,155 paired condition means**, not 2,155 independent participants: 1,080 thermal and 1,075 mechanical, with family clusters. A zero-effect prediction is a benchmark, not an empirical conclusion.

| Prediction of control − placebo | All RMSE | Thermal RMSE | Mechanical RMSE | All Pearson r |
|---|---:|---:|---:|---:|
| Zero effect | 0.1432 | 0.1394 | 0.1468 | undefined (constant) |
| Condition only | 0.1360 | 0.1293 | 0.1424 | 0.042 |
| Condition + NPS | 0.1340 | 0.1275 | 0.1402 | 0.193 |
| Condition + SIIPS | 0.1341 | 0.1288 | 0.1393 | 0.237 |
| Condition + both | 0.1330 | 0.1277 | 0.1382 | 0.275 |

The condition-only model estimates an average contrast from other families; its all-pairs RMSE improvement over zero does not establish individual response prediction. Its low correlation also depends on variation across condition cells and folds. The pair differences derived from the row-prediction models are **not** models separately optimized for contrasts. The results show no guarantee of improvement for every model in every subgroup: NPS-only slightly outperforms both signatures for thermal RMSE. MAE moves differently: across all pairs, the zero benchmark has MAE **0.0901**, lower than both-signature MAE **0.0940**; better RMSE need not mean better absolute-error performance. The source study's design, treatment order, conditioning, repeated observations and site effects matter; this descriptive prediction exercise is not an independent causal analysis.

## 4. A reproducible source consistency check

A separate [checker](verification/paingen_source_crosscheck.py) matches the brain-measures table against the authors' behavioral export after translating centered condition codes. It finds **4,687 of 4,687 brain rows** in the behavioral table; **9,374 of 9,374** intensity and unpleasantness fields agree, counting matching missing values. The behavioral export has 22 rows absent from the brain table. See the [aggregate receipt](verification/paingen_source_crosscheck.json). Both files come from the same study and authors: this checks source transformation consistency, **not independent replication**, original trial reconstruction or a full data-quality audit.

Pinned source: commit `da46f2f9739ad2e9eeb9658711582be6357c1026`; brain CSV SHA-256 `0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56`; behavioral CSV SHA-256 `b40b4a1b1e001f2317fea07a49c6ee6de062f181a20affe149fe50a81b58545b`. The repository lists an MIT license. No source participant table is copied into this public repository. Reproduce with `python verification/paingen_unpleasantness_baselines.py` and `python verification/paingen_source_crosscheck.py`; NumPy is in `verification/requirements-framework-battery.txt`. Each also accepts local pinned files for offline replay; digest and size mismatches stop the run.

## 5. The identification gate for the framework

The project’s candidate posits a relation between a physical relational state and unpleasant experience. It must distinguish at least four quantities:

1. stimulus level (the experimental input);
2. treatment expectation or a prediction error (a psychological/model-dependent variable);
3. experimentally inferred **current channel mismatch** relative to preferred relational offsets;
4. reported unpleasantness, an imperfect and context-sensitive behavioral readout.

None is automatically identical to another. The project’s toy state-mismatch definition is also distinct from minimum frustration, as shown in [the integrated candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md). Placebo and neural signatures are compatible with many causal and constitutive accounts. They cannot distinguish an experiential-ground account from a neutral-ground rival constructed to have the same observables; nor do they identify a subject boundary.

A simple underdetermination illustrates why fitting alone is inadequate. For any observed pairs of existing predictors `X` and unpleasantness `Y`, one model may take latent mismatch `M=Y` and report `Y=M`; another may set `M=0` and take `Y` to be driven by another process, with both reproducing the same observed data. The first construction is circular if `M` is defined from the outcome. This is an example of non-identification when no independent constraints on `M` are given, **not a proof that every physically specified mismatch model is unidentifiable**. An independently specified measurement and intervention model can narrow the alternatives.

### Concrete path to an informative test

1. **Specify channels and readout before outcomes.** Identify what variables, coupling directions, preferred offsets and mismatch functional are meant physically; give units, symmetry rules, the subject/episode boundary and conditions under which the signal is measurable. Avoid fitting offsets to unpleasantness. Use selective probes and alias controls as described in [the channel certificate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md), or establish a different validated observable.
2. **Obtain matched measurements.** Record predeclared channel information and unpleasantness separately on the same trials, with calibrated timing and missing-data rules; measure plausible alternative predictors and response biases. An fMRI signature alone does not supply the required selective channels. Train mappings and thresholds exclusively outside held-out families and, ideally, outside the target cohort.
3. **State a falsifiable competitive claim.** For example, a *specific* fixed operational hypothesis could predict that independently measured mismatch adds held-out explanatory accuracy over condition, NPS and SIIPS, with a prespecified minimum effect and independent cohort. A failure would count against that specified operational model at its stated precision, not every metaphysical possibility; a success would still not prove an identity or eliminate all confounding.
4. **Separate intervention from constitution.** Where ethically feasible, perturb identified coupling while measuring other pathways and report; employ sham, nonspecific stimulation and order controls. Show what causal effects are actually identified and what remains confounded. The independent experiential assay and ground-selection issues remain open even after a successful prediction.

This moves the proposal from an unconstrained analogy toward an explicit empirical burden, without pretending that this dataset already measures the target. The project still lacks a complete necessity argument, physical subject criterion, bridge from independently measured structure to experience, and derived physics. Those gaps are not closed by out-of-family pain prediction.
