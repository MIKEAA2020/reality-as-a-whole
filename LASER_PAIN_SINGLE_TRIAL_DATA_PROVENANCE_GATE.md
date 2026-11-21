# Laser pain reports: promising data, unresolved trial-label provenance

## Result

A 95-person laser-pain study appears better suited than category-labeled music EEG to a same-trial physiological comparison: its authors describe pain-intensity reports after individual stimuli and provide EEG. But the accessible supplementary table does **not yet support a validated prediction benchmark**. Its label-generation procedure and trial correspondence could not be checked against the underlying EEG files, and its fractional values and substantial missing/zero patterns need clarification. We therefore suppress the computed prediction scores rather than present them as evidence for the framework.

This is a source-readiness result. It neither rejects nor confirms the user's mismatch proposal; pain intensity is not the same target as unpleasantness, and the neural interaction preferences needed to operationalize physical mismatch were not measured here. First-person experience remains valid data. B4–B5/F2, B9/F3 and B10 remain open.

## What was inspected

Zhao and colleagues' [2025 data descriptor](https://doi.org/10.1038/s41597-025-05900-1) describes nine experiments with 678 healthy participants in total; experiment 6 corresponds to the [95-person dataset](https://doi.org/10.18112/openneuro.ds005293.v1.0.0). We read article abstract, introduction, methods, data records and technical-validation prose plus captions, and [table 2](https://www.nature.com/articles/s41597-025-05900-1/tables/2); figures were not visually inspected. Their article says the trialwise pain report and stimulus intensity are in each preprocessed EEGLAB `EEG.epoch`, and describes an 11-point numerical rating scale. The experiment-specific README describes **verbal** reports from 0 to 10 and four individually calibrated levels, approximately targeting 2, 4, 6 and 8. Table 2 lists three different four-energy sets for experiment 6, six blocks and 12–14 trials per block. The report concerns pain intensity, not a separately asked affective-unpleasantness score.

We examined the Git tree, experiment README, event JSON, and description for the [version 1.0.0 GitHub mirror](https://github.com/OpenNeuroDatasets/ds005293/tree/66a97a6f92d49f1ac9742fdcafa052cfd2fcc3f0). Its 570 event TSV entries were inventoried but their contents were not inspected; the experiment's preprocessing script and `.set` files are annex links, not their payloads. EEG, epoch/event objects, original verbal records and experimenter logs were not accessed. The dataset description declares CC0; the separate supplement repository did not expose a GitHub-detected license. We do not redistribute that table.

From the author's [pinned supplementary repository](https://github.com/XiangyueZhao/Supplement-Data/tree/daf9f0b83df047c506cc4714d39551b99980d537), we checked one CSV `CSV/participants_singletrial_95ByBP .csv` (note the space in the original name), its Git blob `8b995c541e7084bc616501c626f90505b35a89cf`, and SHA-256 `12b5d1384ffc64a5f02c22a72ebcc9a29074f2bafac0da8f96f5a37a08861f2b`. We inspected `CODE/mat_creation.m`, `CODE/file_select.m`, and `CODE/function/rating_screen.m`. These select or assemble data by event rating/power, but **do not establish how the CSV was generated or joined to the original verbal reports**. We did not run the MATLAB code or validate the EEG preprocessing. Other supplemental files and studies were not comprehensively inspected.

## Exact table-readiness checks

[Code](verification/laser_pain_trial_baseline.py), [tests](verification/laser_pain_trial_baseline_test.py) and [receipt](verification/laser_pain_trial_baseline.json) verify the pinned CSV's hashes, parse every row and check duplicate `(ID, Trial_Num)` keys. These are checks of a source table, not checks of real trial identity.

| Table property | Count or observation |
|---|---:|
| Rows; distinct IDs | 7,600; 95 |
| Rows and distinct trial keys per ID | 80 each; no duplicate ID/trial keys |
| Positive energy and finite 0–10 rating | 6,238 rows |
| Nonfinite `Painrating` (`NaN`) | 1,053 rows, in 90 IDs |
| Zero `laser_power`, zero `Painrating` | 309 rows, in 56 IDs |
| Noninteger finite `Painrating` | 1,241 rows, in 56 IDs |
| IDs with zero-energy rows occurring only at end of their numbered rows | all 56 affected IDs |

The 309 zero-energy/zero-rating records and 1,053 NaN-rating records are disjoint; the other 6,238 rows meet the basic numeric screen. Counting a finite decimal as a table value is not the same as validating a self-report. The descriptor's “11-point” language and values such as `5.5` merit clarification; fractional verbal responses might be permitted or entered/transformed in some other way. This is **not proof of a data error**. Similarly, zero-energy suffixes are consistent with padding, but could have another explanation; the NaNs might reflect missing, rejected or unavailable records. We cannot infer the reasons, or assume each numbered row maps uniquely to an actual trial. Retention may depend on artifacts or response value, and a prediction conditioned on retained rows might not generalize to the original 7,600 planned slots.

The paper's stimulus and response descriptions provide meaningful motivation, but the verified CSV name and column names alone do not independently establish the full data-generating chain. Recorded joules are not the personalized nominal level: two people at the same energy can have different calibration and history. The CSV has no hand-side column, no explicit timestamps, and no explicit connection to a specific EEG epoch. A future same-trial analysis cannot reconstruct a valid EEG/response join merely from matching positions unless that convention is independently established.

## Protocol transparency

The [fixed plan](LASER_PAIN_SAME_TRIAL_READINESS_FIXED_PLAN.md) preceded inspection of the CSV, and the [post-schema amendment](LASER_PAIN_SAME_TRIAL_PLAN_AMENDMENT.md) replaced unavailable nominal ranks with exact numerical energy and dropped the side comparison. After the amendment we ran an initial leave-person-out calculation, but the larger patterns above revealed that the stop condition had not been adequately satisfied: we had not independently established the source, row semantics or exclusions. **Its numerical scores and confidence interval are suppressed**, and the retained script now performs readiness checks only. This is not a preregistered study, a null result, or proof the data are unusable. The exploratory calculation was performed before suppressing it; the data and any future changes must not be presented as outcome-blind.

To unblock the original analysis:

1. Obtain the experiment-specific `.set` files and preprocessing/behavioral import code or a documented author mapping; verify annex SHA-256 and link `ID` and epoch event IDs to trial time, power, actual rating and hand, including deleted epochs.
2. Obtain the verbal scoring instructions/entry rules, provenance of decimal ratings, and definitions of NaNs and zero suffixes. Specify the target population and exclusion/retention mechanism before scoring; do not silently treat missing trials as zero pain.
3. Verify trial power/ratings against a sample of original behavioral records or an independently documented source, and check calibration and condition assignments. Compare the retained and omitted-trial populations where possible.
4. Only then freeze a retrospective or prospective analysis: matched train/test splits by participant and session, energy-only and subject-calibrated baselines, declared timing, artifacts and physiological controls. The fixed leave-person-out score is one potential benchmark, not a ceiling or validated clinical estimator.

The known first-person [Rainville affect/intensity comparison](RAINVILLE_PAIN_AFFECT_FULL_PAPER_AUDIT.md) independently supports asking both dimensions, while the [cross-modal pain/aversion readiness audit](PAIN_AVERSION_CROSS_MODALITY_EXPERIENTIAL_READINESS_GATE.md) shows why otherwise similar intensity ratings are not automatically a shared unpleasantness measure. Neither establishes the candidate's neural mismatch. A better study would separately elicit intensity and unpleasantness, manipulate or independently identify interaction preferences, and compare mismatch with dose, salience, expectation and power/connectivity controls under the same held-out conditions. Even a strong association would not by itself decide subject boundaries or experiential versus neutral grounding.

## Reproduction without redistribution

Fetch the exact pinned blob from the GitHub path above into a local file, then run `python verification/laser_pain_trial_baseline.py <path>` and `python -m unittest discover -s verification -p 'laser_pain_trial_baseline_test.py'`. The verifier rejects nonmatching bytes and performs no predictive scoring. The table remains outside the repository pending clarification of reuse terms; a Git blob ID verifies the downloaded version, not its biological or behavioral truth.
