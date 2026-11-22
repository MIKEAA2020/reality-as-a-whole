# A three-state EEG–report pilot using the already supplied S09 files

## Result

I checked the practical data requirements and found the five needed S09 EEG files in the user's connected Dropbox; **the user does not need to upload S09 again**. I then ran the [fixed exploratory plan](ROY_S09_THREE_STATE_EEG_REPORT_EXPLORATORY_PLAN.md) on those files. This is actual analysis of one previously explored participant, not a new experiment or a population validation.

The simple POz frequency-tag classifier was trained to predict report code 1, code 2 or **mixed** (code 3). On 140 held-out, report-labeled clean windows pooled across two later rivalry scans, it agreed with reports in **66/140 (47.1%)**, compared with **68/140 (48.6%)** for the training-majority baseline and **70/140 (50.0%)** for the training-position-only baseline. It correctly classified **2 of 14 mixed-labeled windows**. Its macro recall was **39.0%**, versus **33.3%** and **35.4%** for those baselines, which never predicted mixed. These are descriptive scores from a small, dependent sample, not significance tests. The result does not show reliable mixed-report decoding, establish a general failure of EEG methods, or measure experience.

The held-out runs were not used to fit the classifier, but the participant and some test-run report patterns were inspected previously. This is **fit-held-out, not blind or prospective**. A comparison of accuracy, macro recall and coverage gives different aspects of performance; do not select one after seeing the results as proof of superiority.

## 1. Inputs, access and provenance

Five already-supplied preprocessed EEG files were fetched individually from Dropbox: `S09_scan1_filtered_gac_cbc.mat`, `S09_scan2_filtered_gac_cbc.mat`, `S09_scan3_filtered_gac_cbc.mat`, `S09_scan5_filtered_gac_cbc.mat` and `S09_scan7_filtered_gac_cbc.mat`. Their SHA-256 values each match the prior committed S09 inspection. These checks show consistency with the earlier supplied files, **not** an independently verified original full-archive checksum. The files were kept in the ignored `.arena/roy_mixed_input/` cache and are not committed. MATLAB EEG structures may include sensitive metadata; the analysis does not intentionally inspect or output DICOM fields. The original archive need not be reuploaded.

The [public release](https://zenodo.org/records/5035511) lists 20 participant ZIPs and a README; the repository's [prior source audit](ROY_S09_PUBLIC_SUPPORT_MOTION_AND_CONDITIONS.md) verified the S09 scan-condition labels from the original README layout and corroborating code. Scans 1, 2, 3, 5 and 7 are documented as rivalry. This is not independent confirmation of actual stimulus logs, trial-specific eye assignment or report timing. The release describes research/noncommercial use and requests citation of both [Roy et al. (2017)](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al. (2015)](https://doi.org/10.1016/j.jneumeth.2015.01.024). Check the applicable release terms before redistribution.

To extend this to another participant, obtain that participant's **preprocessed EEG MAT files for all documented rivalry scans**, the [release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1), and any participant-specific condition/timing documentation. The public archives also contain MRI, but **MRI is not needed** for the EEG–report pilot. The public ZIPs are large—for example [S01.zip](https://zenodo.org/records/5035511/files/S01.zip?download=1) is listed as 912.1 MB, MD5 `20949e6a10ada6cef7280ab4d31b7c04`—and were not downloaded or inspected here. The exact S01 internal file names, schema and usable rivalry scan count remain unverified; do not assume they match S09. Extracted authorized EEG files may avoid the connector's previously encountered 100 MiB per-file limit; check individual sizes and privacy before transfer. A single additional person is an independent individual case, not enough by itself for a population generalization. Wider evaluation needs multiple held-out participants and a frozen, participant-independent procedure.

## 2. Analysis and denominators

Follow the existing provisional timing reconstruction: five 42-second trials per scan begin at recorded trial markers, with report state unknown before the first event and then carried forward from `latency_s1`, `latency_s2`, or `latency_s3` to the next event. Divide each trial into 21 consecutive two-second windows. A window is assigned code 1, 2 or 3 when **at least 75%** of its samples carry that code; otherwise its report target is unresolved. This is a stipulated window-level summary, not a claim that the person's entire window was homogeneous or that a mixed report is an error. Any `bad_epoch` sample leads to classifier abstention.

For **every artifact-clean window**, independently of its report label, compute the POz log ratio of power at the lower and higher stored tag frequencies using the fixed Hann-window projection from the prior binary pilot. Fit class means on labeled, clean windows of scans 1–3 and predict the nearest mean, breaking ties toward the lower code. The training-set majority baseline predicts code 2; the time-only baseline learns a majority report at each trial position on the training data, falling back to the overall training majority on ties or missing positions. Code meanings, target construction, feature, thresholds and split were fixed in the plan before running this pilot. The classifier is not Roy's optimized SSVEP method.

| Scan | Labeled-clean / all windows | EEG correct / labeled-clean | Training majority | Time-only | EEG macro recall |
|---|---:|---:|---:|---:|---:|
| 5 | 67 / 105 | 33 / 67 = 49.3% | 28 / 67 = 41.8% | 27 / 67 = 40.3% | 41.1% |
| 7 | 73 / 105 | 33 / 73 = 45.2% | 40 / 73 = 54.8% | 43 / 73 = 58.9% | 41.9% |
| **Pooled** | **140 / 210** | **66 / 140 = 47.1%** | **68 / 140 = 48.6%** | **70 / 140 = 50.0%** | **39.0%** |

Pooled labeled-clean class counts are 58, 68 and 14 for codes 1, 2 and 3. Pooled EEG recalls are **34/58**, **30/68**, and **2/14** respectively. Its pooled confusion matrix, true classes in rows and predicted classes in columns, is:

```text
             predicted 1   predicted 2   predicted 3
true 1            34             18              6
true 2            36             30              2
true 3             8              4              2
```

Thus 10 labeled-clean windows were predicted as mixed, of which two were mixed-labeled; 12 of 14 mixed-labeled windows were predicted as a pure code. The small mixed count makes its recall highly unstable; temporally adjacent windows and runs are dependent. The two baseline rules predicted no mixed windows because mixed was never a training-position majority. A higher macro recall than those particular baselines is descriptive, not a statistical demonstration of generalization.

Across all 210 test windows, 65 were unresolved under the 75% report rule, 8 had artifacts, and 3 were in both categories, leaving 140 labeled and clean. Each method still produced predictions for all 62 **clean but unresolved** windows; labels were not used for abstention. The conservative full-grid correct fraction is **66/210 = 31.4%** for EEG, **68/210 = 32.4%** for majority and **70/210 = 33.3%** for time-only. Unresolved and artifact windows are counted as not successful by definition; that is not a statement that the participant lacked clear experience, that all mixed reports are wrong, or that their EEG was wrong in those windows. Labeled-clean accuracy is conditioned on report coverage and cannot be interpreted as all-time accuracy.

The earlier [binary pilot](ROY_S09_EEG_REPORT_TRANSFER_RESULTS.md) used a different, stricter all-samples-pure label definition and excluded mixed reports from its binary target. Its percentages and this pilot's are therefore **not a controlled head-to-head comparison of two- versus three-state classifiers**. Neither result is an assessment of felt experience or a replication of the published analysis.

## 3. What would make the next test stronger?

- Fix a development cohort and a separately held-out set of participants, not just held-out runs from an already inspected person. Check each participant's actual scan labels, artifact and event schema, report codes, frequency assignments and trial timing before scoring; stop on ambiguity rather than infer condition from performance.
- Decide in advance whether the target is window majority, explicitly mixed content, transitions, or another construct; report all-time coverage, abstentions, class frequencies and per-participant confusion matrices. The 75% rule here is only one arbitrary operational target.
- Fit all learned preprocessing, timing, feature selection and model parameters on development participants; use the same held-out windows for EEG and baselines. Handle participant-specific features without using held-out report labels to fit or tune. Preserve trial/run/participant grouping and prevent replay-derived data leakage. A calibration phase using test-participant labels changes the task to a separately reported personalized analysis.
- Report participant-level uncertainty where enough independent people are available and account for within-person dependence and missing classes. A three-state report classifier still requires a separate, defensible report-to-experience bridge, and a global mixed report cannot by itself resolve the spatial organization of perception discussed in the [Naber audit](NABER_2011_GRADED_RIVALRY_AND_REPORT_AUDIT.md).

## 4. Verification and reproduction

[Implementation](verification/roy_s09_three_state_pilot.py) and [aggregate receipt](verification/roy_s09_three_state_pilot.json); [synthetic tests](verification/roy_s09_three_state_pilot_test.py) cover the 75% boundary, spectral ordering, training/ties, artifact abstention, unlabeled-window predictions, confusion accounting and fit isolation. The actual run used NumPy 2.4.6 and SciPy 1.15.3 in an ignored environment. With those dependencies and the five already-authorized local files:

```sh
PYTHONPATH=.arena/python-deps python verification/roy_s09_three_state_pilot_test.py
PYTHONPATH=.arena/python-deps python verification/roy_s09_three_state_pilot.py /private/path/to/five/files --output /private/path/to/summary.json
```

The script checks each source hash against earlier S09 inspection summaries before loading selected variables. It writes aggregate outcomes only. Tests verify the implementation on synthetic inputs, not the correctness of participant reports, the provisional timing reconstruction, source labels, consciousness or causal interpretation.
