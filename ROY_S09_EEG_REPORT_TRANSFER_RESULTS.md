# S09 EEG–report test: later-run transfer

## Result

A simple POz frequency-tag rule fitted on documented rivalry scans 1–3 did **not consistently beat a timing-only baseline** on the two later documented rivalry scans. Among windows with a stable pure report and no `bad_epoch` samples, the EEG rule agreed with reports on **24/39 (61.5%)** in scan 5 and **25/50 (50.0%)** in scan 7. The corresponding timing-only results were **22/39 (56.4%)** and **31/50 (62.0%)**. On the pooled 89 eligible windows the EEG rule scored **49/89 (55.1%)**, versus **53/89 (59.6%)** for timing alone and **47/89 (52.8%)** for the training-majority rule. These are descriptive counts from one person, not independent Bernoulli trials or evidence of population differences.

This is a genuine fit-held-out comparison: the later runs did not fit the model. It is **not a blind or prospective preregistered test**: this participant's data and training POz associations were inspected previously, and some held-out runs' report patterns were already known. Runs within a participant—and especially replay runs derived from earlier reports—need not be independent. It tests a selected simple procedure, not every possible EEG decoder or the published optimized method.

## Fixed procedure

The [analysis plan](ROY_S09_EEG_REPORT_HELD_OUT_PLAN.md) and [implementation](verification/roy_s09_eeg_report_transfer.py) were committed before this run. Nine previously supplied EEG files were re-fetched in two bounded batches after the first file; each SHA-256 matched its prior inspection. They remain in a private cache, not Git. The plan was written after prior exploration, not before data collection.

- Training: rivalry scans 1–3. Test: rivalry scans 5 and 7; smooth replay scans 4 and 6; instantaneous replay scans 8 and 9. Condition labels come from the dataset README and [reanalysis code audit](ROY_S09_PUBLIC_SUPPORT_MOTION_AND_CONDITIONS.md). Replay-source trial identity and eye assignments remain unverified.
- For each of five assumed 42-second trials, divide time into 21 non-overlapping two-second windows. Carry the recorded report state forward from each event; before the first event it is unknown. A pure window contains exclusively code 1 or exclusively code 2 throughout. Windows containing code 3, unknown, or any within-window report change are treated as unresolved; any `bad_epoch` sample excludes an otherwise pure window. This is an intentionally strict report-based evaluation selection, **not an algorithm that detects mixed states or knows in advance which windows are pure**.
- The EEG feature is the log10 low-tag/high-tag power ratio at POz, computed using mean removal, a symmetric Hann window and direct projections at the two stored frequencies. For eligible training windows, calculate one mean per code; predict the nearer mean, with ties to code 1. Training had 39 code-1 and 57 code-2 pure-clean windows. Their mean features were +0.016 and +0.237, respectively. The sign reflects the fitted data and should not be taken as a verified color/frequency mapping or a biological explanation.
- The training-majority baseline always predicts code 2. The timing-only baseline predicts the most common training label at the same position in the 42-second trial, falling back to training majority for ties or unobserved positions. All three have the same test eligibility rule. No test-set features or labels tune the rule. The baseline can exploit run/trial timing and possible replay structure; it is not a causal control.

## All held-out results

| Scan | Documented condition | Pure-clean windows / 105 | EEG accuracy (correct / eligible) | Training-majority accuracy | Time-only accuracy | EEG full-grid failure* |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 5 | Rivalry | 39 | 24/39 = 61.5% | 20/39 = 51.3% | 22/39 = 56.4% | 81/105 = 77.1% |
| 7 | Rivalry | 50 | 25/50 = 50.0% | 27/50 = 54.0% | 31/50 = 62.0% | 80/105 = 76.2% |
| 4 | Smooth replay | 9 | 6/9 = 66.7% | 5/9 = 55.6% | 5/9 = 55.6% | 99/105 = 94.3% |
| 6 | Smooth replay | 11 | 9/11 = 81.8% | 4/11 = 36.4% | 4/11 = 36.4% | 96/105 = 91.4% |
| 8 | Instantaneous replay | 16 | 12/16 = 75.0% | 8/16 = 50.0% | 11/16 = 68.8% | 93/105 = 88.6% |
| 9 | Instantaneous replay | 49 | 27/49 = 55.1% | 24/49 = 49.0% | 26/49 = 53.1% | 78/105 = 74.3% |

\*Full-grid failure is `1 − (correct pure-clean windows / 105)`. It counts **every** mixed, unknown, transitioning or artifact-affected window as failure regardless of what a classifier would output. This is a conservative two-second-window **report-agreement accounting convention**, not measured experience error and not a detector deployed across all windows. In particular, a window with one brief mixed or unknown sample is unresolved for the whole window. The earlier 18.659% pooled sample-level unknown/mixed fraction has a different denominator and resolution and cannot be compared directly to these window failure percentages. The large values do not mean the participant experienced no clear percept for that proportion of time.

Conditional accuracies can look high while covering very little: scans 4 and 6 have only **9 and 11 eligible windows out of 105**. The apparent replay performance is exploratory; their reports can be linked to prior rivalry trials, and the previously observed 4/6 timing resemblance was itself post hoc. Counts by class, balanced accuracies, all three confusion matrices and unresolved/artifact denominators are in the [machine-readable results](verification/roy_s09_eeg_report_transfer.json). No inferential confidence interval or significance test is reported.

## What this contributes to the framework test

This experiment narrows a practical claim: **this fixed, previously motivated POz rule did not reliably outperform the simple timing-only control across the two later rivalry scans of S09.** It does not prove that a better EEG feature, spatial filter, lag convention, different windowing, or a different participant cannot track reports. Nor can its performance calibrate report against felt experience. The existing conditional bridge still requires an independently justified report-to-experience error bound and suitable intervention; this study supplies neither. No EEG–fMRI alignment was assumed or used.

The constructive next step is an independently specified report decoder with training and testing across **participants**, explicit replay/source grouping and held-out controls, ideally a prospective task with separately audited reports. Further tuning on these six test runs would turn them into development data; any new result on them must be labeled exploratory. The original Roy and Jamison methods and [Lyu et al.](https://doi.org/10.1038/s41467-022-34410-6) are established work to consult rather than present as a new derivation.

## Reproduction

With all nine authorized S09 EEG MAT files locally present and `numpy==2.2.6`, `scipy==1.15.3`:

```sh
PYTHONPATH=/your/deps python verification/roy_s09_eeg_report_transfer_test.py
PYTHONPATH=/your/deps python verification/roy_s09_eeg_report_transfer.py /private/path/S09_scan{1,2,3,4,5,6,7,8,9}_filtered_gac_cbc.mat
```

The synthetic test checks spectral ordering, fit isolation, tie behavior, both baselines, confusion accounting, artifact abstention and invalid input stops. It does not validate reported experience, scan-label truth or generalization. The data release specifies research/noncommercial use and requests citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024). Raw EEG, event sequences and DICOM metadata are not committed.
