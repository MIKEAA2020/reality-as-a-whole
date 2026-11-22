# Brief mixed reports: development result and frozen S02 test protocol

> **Later update:** the planned S02 test has now been run; see the [S02 results](ROY_S02_FROZEN_REPORT_CENTER_TRANSFER_RESULTS.md). This document otherwise preserves the pre-test development and protocol.

## Bottom line

The earlier 75%-of-two-seconds target missed every S01 mixed window. A revised **report-at-center** target can count very brief mixed reports while retaining a two-second EEG feature, but it has an important cost: the EEG window usually includes other reports before and after the mixed center. It does not isolate a mixed-specific neural signal.

In exploratory development, fitting on one previously inspected participant and evaluating the other yielded mixed-report recalls of **31/399 (7.8%) for S01** and **73/1,057 (6.9%) for S09**. Mixed-prediction precision was **31/338 (9.2%)** and **73/346 (21.1%)**, respectively. These are weak results, not a demonstration of a useful detector. Both S01 and S09 were previously examined; these comparisons are not blinded independent replications. No uncertainty estimate can be inferred by treating overlapping centers as independent observations.

The candidate below, including its unfavorable development results and fitted parameters, is frozen for a **single new-participant S02 transfer test**. This is a feasibility test of this particular candidate, not a claim that the candidate is already promising or a commitment to keep using it if it fails. S02 has not been accessed or scored in this exercise. If its files or schema are incompatible, report that and stop; do not adapt to S02 outcomes.

## 1. Why a different target

The [S01 frozen S09 transfer result](ROY_S01_FROZEN_CROSS_PARTICIPANT_THREE_STATE_RESULTS.md) found code-3 events but no two-second windows at least 75% mixed. Simply shortening the EEG windows would make the two frequency tags harder to separate. Here the target is instead the **report code at the center instant**, not the predominant report throughout the EEG window. Center sampling every 0.2 s is a fixed grid, not selection of favorable mixed events.

This choice does **not** identify whether the signal comes from the center state, the preceding/following states, eye movements, button behavior, transition-related activity, filtering or timing differences. Windows overlap by 90%, so centers are strongly dependent. The EEG feature looks one second ahead of the center: this is an **offline** association, not real-time prediction. No separate matched-transition control is supplied; specificity to mixed perception versus transitions remains unresolved. All timing and state labels remain provisional, as in the S01 audit.

## 2. Development method and data

- Data: the six documented S01 rivalry scans 1, 3, 5, 7, 10, 12 and the five S09 rivalry scans 1, 2, 3, 5, 7, all previously inspected. S01 files match the supplied Dropbox hashes; S09 files match the earlier committed SHA-256 inspections. Raw files remain in the ignored private cache, not in Git.
- Parser: five assumed 42-second trials per scan at 250 Hz; events `latency_s1/s2/s3` are provisional 1-based sample positions. Within each trial, state is unknown until the first report and is then carried forward to the next event. Out-of-bounds trials, duplicate event times, wrong sampling/channel/tag/mask schema, or missing training classes cause failure rather than silent adjustment.
- Grid: 201 centers per trial, at seconds 1.0, 1.2, …, 41.0. The input for each is the two-second interval `[center−1 s, center+1 s)`. Code at the exact center is the target, and unknown centers are excluded from labeled scores. A window containing any bad-epoch sample is excluded from labeled scores. The feature is computed for **all artifact-clean centers**, regardless of label; report-dependent eligibility is a scoring convention, not real-time abstention.
- Feature: same two-second, mean-centered, Hann-tapered POz log10 power ratio at the stored lower/higher tags (approximately 6.667 and 8.571 Hz). The nominal Fourier-bin spacing for two seconds is 0.5 Hz; this implementation directly evaluates the two frequencies. A synthetic pure-tone check detects both directions, but **does not establish adequate signal-to-noise, tag isolation or mixed-state temporal resolution in actual EEG**.
- Model: one mean ratio per class. For two-participant fitting, calculate each participant's mean separately within each class, then average the two means equally; nearest mean wins, with smallest code for an exact tie. This is not class-balanced optimization and does not guarantee good minority recall. The pooled means are `[-0.1351527435, 0.0929803373, -0.0186919460]` for codes 1, 2, 3; the full machine-readable parameters are in the [development receipt](verification/roy_report_center_development.json).
- Baselines: majority report code (2 for pooled development) and a within-trial integer-second rule. The latter chooses the largest mean of participant-specific clean labeled class proportions in each slot; ties choose the smallest code and unobserved slots fall back to global majority. These time rules use development reports only; they may exploit trial dynamics and are not causal controls.
- Segments: consecutive samples of the same carried-forward report code form a segment. For mixed segments having at least one eligible center, calculate the fraction predicted mixed in each segment and average those fractions equally. Also count segments with at least one mixed prediction. Segments with no eligible center are excluded, and their count is not estimated by that metric. The latter count is sensitive to duration and repeated opportunities; neither segment metric is an independent-trial statistical test.

## 3. Exploratory leave-one-participant-out checks

Each row below uses one already-inspected participant to fit the model and the other to score. This illustrates transfer under the candidate, but influenced by prior analysis and followed by the decision to use the same candidate. It is not a held-out result.

| Test participant; training participant | Clean labeled centers | Class 1 / 2 / mixed recall | Three-class macro recall | Overall accuracy | Mixed precision |
|---|---:|---|---:|---:|---:|
| S01; S09 | 5,970 | 50.1% / 58.6% / **7.8%** | 38.8% | 51.4% | 9.2% |
| S09; S01 | 4,811 | 57.6% / 48.0% / **6.9%** | 37.5% | 42.4% | 21.1% |

Training-majority macro recall was 33.3% for each. Time-only macro recall was 32.3% and 33.4%, respectively. Both baselines predicted no mixed centers, so their mixed precision is undefined, not zero. Mixed equal-segment recall was 7.1% over 303 eligible S01 mixed segments and 8.2% over 204 eligible S09 mixed segments. The EEG rule produced at least one mixed prediction in 27/303 and 50/204 of those segments. All are descriptive counts from heavily overlapping windows, not independent samples or evidence of generalization.

The report-center definition changes the target and denominator; these percentages are not directly comparable to the older 75%-window S01 result. The modest macro-recall advantage over the baselines is descriptive and may arise from sampling, transition context, confounding or previous analysis choices. It does not cancel the very low mixed recall.

## 4. Frozen test: participant S02

The next target is S02, with rivalry scans **1, 2, 4, 6, 8 and 11**, from the [pinned scan-condition mapping](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m). Mapping and trial timing are not independent acquisition-log verification. Replay scans are excluded. The external source is the [Roy–Jamison S02 archive](https://zenodo.org/records/5035511/files/S02.zip?download=1), whose published MD5 is `02f9ab78531e9b9cc5093ed5e3abf767`; the archive itself has not been downloaded or verified here.

The [S02 runner](verification/roy_s02_frozen_center_transfer.py) checks the development receipt and analysis dependencies against fixed SHA-256 values before use, accepts exactly the six scan filenames and a separately recorded source-SHA manifest, validates the expected MAT structure, applies the already-fitted S01+S09 model without refitting, and reports per-scan and pooled confusion matrices, center accuracy, three-class recall, mixed precision, coverage and segment diagnostics. It does not require any target labels to make predictions on clean centers. If a class is absent, its recall and macro recall are undefined; if no mixed predictions occur, mixed precision is undefined. Do not change parameters, label rules or scans after inspecting S02. Any later revision needs a separately labeled exploratory analysis and a further untouched participant.

**Interpretation:** Report S02's raw counts, all three class recalls, macro recall, mixed precision and the two baselines together. Mixed recall near the weak development values, no mixed targets, or errors in source/schema/timing would limit the candidate; do not use overall accuracy alone to claim mixed detection. No p-values, confidence intervals treating centers or segments as independent, or population-level claims are planned. One new person cannot show generalization. Repeat across independently held-out participants and use participant-level inference only after designing an appropriate multi-participant study.

**Provenance:** Verify source sizes and Dropbox content hashes before recording SHA-256 values, or verify the original archive against the published MD5 before extraction. A source manifest computed from files alone detects later changes, not authenticity. Do not publish raw EEG, event sequences, sensitive metadata or private Dropbox links. Keep the full zip and MAT files outside Git. The public dataset is subject to its stated research/noncommercial conditions; see [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).

**Access check:** Dropbox filename search found no S02 scan files, and a direct request from this sandbox to the public S02 archive failed during TLS connection. The prior S09 and S01 files need not be supplied again. No S02 data or outcome was accessed, and no author correspondence was sent.

## 5. Reproduction and checks

The implementation and aggregate receipt are [here](verification/roy_report_center_development.py) and [here](verification/roy_report_center_development.json). With already supplied, hash-verified inputs and NumPy 2.2.6/SciPy 1.15.3:

```sh
PYTHONPATH=.arena/python-deps python verification/roy_report_center_development_test.py
PYTHONPATH=.arena/python-deps python verification/roy_s02_frozen_center_transfer_test.py
PYTHONPATH=.arena/python-deps python verification/roy_report_center_development.py .arena/roy_s01_input .arena/roy_s09_input --output .arena/center-reproduction.json
```

Tests cover synthetic tag ordering, brief mixed center coverage, artifact exclusion, participant weighting, label-independent prediction, segments, fixed-model integrity, test scan selection and pooling. The actual development receipt was independently rerun and reproduced byte-for-byte. These checks validate implementation arithmetic, not the event reconstruction or ground-truth experience. The S02 runner's real-data path remains untested until S02 is supplied.
