# S09-trained EEG classifier tested on S01

## Result

The 13 S01 EEG files you supplied were accessible. I applied the **unchanged S09-trained three-state classifier** to S01's six documented rivalry scans, without fitting or tuning it on S01 reports. On 299 report-labeled, artifact-clean two-second windows, it agreed with S01's reports on **177/299 (59.2%)**. The frozen S09-majority baseline scored **170/299 (56.9%)**, and the S09 timing-only baseline **166/299 (55.5%)**.

**The intended mixed-state test was not possible under the fixed scoring rule:** none of the 299 eligible windows was labeled predominantly mixed. This does **not** mean S01 never reported mixed perception. A separate descriptive check found many mixed-report events, but none of the 630 two-second windows contained mixed report for at least the required 75% of its samples. Therefore mixed-state recall and three-class macro recall are **undefined**, not zero or a success. This test concerns one new participant and observational report agreement, not consciousness or population generalization.

## 1. Files and integrity

All 13 files in the supplied Dropbox folder matched the listed file sizes and Dropbox content hashes after local download. Two transfer calls reported save errors, but complete local copies existed; independent size and hash checks passed for both. **No re-upload is needed.** This verifies consistency with the supplied Dropbox files, not the checksum of the original published ZIP. The raw inputs remain in the ignored private `.arena/roy_s01_input/` cache and are not committed. MATLAB structures can include sensitive metadata; this analysis does not intentionally inspect or publish DICOM fields.

All 13 files contained the selected fields, five trial markers, a unique POz channel, sampling rate 250 Hz and stored tag frequencies approximately 6.667 and 8.571 Hz. The six prespecified rivalry scans were **1, 3, 5, 7, 10 and 12**, using the [original release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) and [pinned reanalysis condition list](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m). They are consistent but may share a source; they do not independently confirm actual acquisition logs, trial-level eye assignment or perceptual timing. The other seven files were verified and schema-checked, but not used to score the rivalry test.

## 2. Frozen test

The [analysis plan](ROY_S01_FROZEN_CROSS_PARTICIPANT_THREE_STATE_PLAN.md) was written before reading S01 EEG contents or report outcomes. The model came from the earlier [S09 three-state pilot](ROY_S09_THREE_STATE_EEG_REPORT_EXPLORATORY_RESULTS.md); its stored receipt was checked against a fixed SHA-256. There was no S01-derived refitting, threshold selection, timing adjustment, or label remapping. The prior study and S09 development were retrospective, and the plan has no independent timestamp establishing its creation before analysis; this is a new-participant test for this procedure, **not a prospective trial**.

As before, each of five assumed 42-second trials per scan was divided into 21 two-second windows. Reconstructed report states start unknown and are carried forward from report-event markers. A window is assigned code 1, 2 or mixed code 3 if at least **75%** of its samples have that code; other windows are unresolved. This is a window-level convention, not proof that the entire window is phenomenally homogeneous. A window with any `bad_epoch` sample is excluded from scoring. A clean window gets a prediction irrespective of whether its report target is resolved; the EEG feature is the preselected POz low-/high-tag log-power ratio.

| S01 rivalry scan | Labeled-clean / 105 | EEG correct | S09-majority correct | S09 time-only correct |
|---|---:|---:|---:|---:|
| 1 | 55 | 33 | 30 | 31 |
| 3 | 53 | 33 | 30 | 30 |
| 5 | 42 | 24 | 23 | 24 |
| 7 | 47 | 27 | 28 | 27 |
| 10 | 54 | 31 | 28 | 27 |
| 12 | 48 | 29 | 31 | 27 |
| **Pooled** | **299 / 630** | **177 / 299** | **170 / 299** | **166 / 299** |

These counts are descriptive: windows and runs from one participant are not independent people. The pooled differences—seven and eleven correct windows over the respective baselines—are not evidence of a statistically reliable advantage. There is no participant-level confidence interval or population claim.

The EEG confusion matrix (true reports in rows, predictions in columns) is:

```text
              predicted 1   predicted 2   predicted mixed
true 1             84             39               6
true 2             68             93               9
true mixed          0              0               0
```

Recalls for codes 1 and 2 are **84/129 (65.1%)** and **93/170 (54.7%)**. All 15 mixed predictions on these labeled windows occurred when the report-derived label was 1 or 2. This is a mistake relative to the stipulated **predominant-window** label, not proof that there was no mixed experience at any instant within those windows. The absent mixed row prevents estimating mixed recall.

Across all 630 windows, 329 had unresolved report targets, 9 had artifacts and 7 belonged to both groups, leaving 299 labeled and clean. The EEG model correctly matched **177/630 (28.1%)** under the conservative full-grid convention; baselines were **170/630 (27.0%)** and **166/630 (26.3%)**. Every unresolved or artifact window counts as not successful in that score, not as a wrong or absent experience. The EEG rule did make predictions for the 322 clean unresolved windows, but no accuracy can be assigned to them under this label convention.

## 3. Why the mixed class was absent from the score

After the frozen test, a separately marked [descriptive coverage diagnostic](verification/roy_s01_mixed_coverage_diagnostic.json) reconstructed the same report states without altering the classifier. Across the six rivalry runs it found **523 code-3 event markers** within trials and **82.964 seconds** carrying code 3 out of 1,260 assumed trial seconds. Of 630 windows, **503 contained at least one code-3 sample**, one contained at least 50% code 3, and none reached 75%; the largest window fraction was **58.4%**. These coverage counts include artifact windows and are subject to the same marker, trial-onset and carry-forward assumptions. They do not give ground truth about private perception or prove the precise onset and duration of each experience.

The high number of windows containing *some* mixed report alongside zero windows predominantly mixed explains why the fixed two-second target cannot assess mixed recall here. We did **not** replace the threshold or window size after seeing S01 outcomes and present a new score as held out. A revised event-based or shorter-window design must be fixed and evaluated on genuinely new participants or new held-out data, with attention to tag-frequency resolution and latency; shorter EEG windows can also degrade the frequency feature.

## 4. What this does and does not establish

- It is a real **cross-participant transfer** of a fixed S09-trained classifier to S01 report codes. The small numerical advantage over the two frozen baselines describes this participant and target definition only; no generalization to a population follows.
- It cannot evaluate mixed-report recall under the chosen threshold. Its inability to score mixed labels is a **measurement-design limitation**, not evidence that the participant had no mixed percepts or that all three-state EEG approaches fail.
- Two participants, one used for development and one for this test, are insufficient for a reliable population claim. The EEG–report association is not a calibrated report-to-experience error rate and cannot settle subject identity, qualitative character or the metaphysics of experience.
- The [previous S09 pilot](ROY_S09_THREE_STATE_EEG_REPORT_EXPLORATORY_RESULTS.md) had mixed-labeled windows; the present result shows why class coverage must be checked across participants rather than assumed from development data.

## 5. Reproduction and checks

The [fixed-transfer script](verification/roy_s01_frozen_three_state_transfer.py), [aggregate results](verification/roy_s01_frozen_three_state_transfer.json), [post-test coverage script](verification/roy_s01_mixed_coverage_diagnostic.py) and [coverage receipt](verification/roy_s01_mixed_coverage_diagnostic.json) do not publish raw EEG, individual event sequences or sensitive metadata. [Synthetic transfer tests](verification/roy_s01_frozen_three_state_transfer_test.py) check model-hash rejection, source-hash arithmetic, pooled accounting and model immutability; the [coverage test](verification/roy_s01_mixed_coverage_diagnostic_test.py) checks threshold arithmetic. For the actual six scans, all 630 diagnostic labels and artifact flags were also checked for agreement with the transfer parser, and both result files were reproduced byte-for-byte. These checks do not independently validate the parser, the participant's subjective reports or the timing reconstruction. The existing S09 tests and 45 selected finite-model regressions also passed; they are not evidence of experiential accuracy.

With the user's authorized S01 files in the ignored cache and NumPy 2.2.6/SciPy 1.15.3:

```sh
PYTHONPATH=.arena/python-deps python verification/roy_s01_frozen_three_state_transfer_test.py
PYTHONPATH=.arena/python-deps python verification/roy_s01_frozen_three_state_transfer.py .arena/roy_s01_input --output .arena/s01-reproduction.json
PYTHONPATH=.arena/python-deps python verification/roy_s01_mixed_coverage_diagnostic.py .arena/roy_s01_input --output .arena/s01-coverage-reproduction.json
```

The public dataset is research/noncommercial as described in its README; cite [Roy et al. (2017)](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al. (2015)](https://doi.org/10.1016/j.jneumeth.2015.01.024) when using it. No fMRI files or authors' correspondence were needed or requested.
