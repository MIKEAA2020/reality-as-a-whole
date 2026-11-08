# Roy S09: nine scans, report coverage and a descriptive EEG contrast

## Scope

The user supplied the remaining three EEG scans, S09 scans 1–3. They were downloaded **one at a time**, examined and verified against their Dropbox file hashes. Together with the previously processed scans 4–9, this provides summaries of **nine scans from one participant**. The full ZIP was not downloaded, and raw EEG files were not committed.

This note reports a coverage summary across the nine scans and a **new, explicitly exploratory EEG/report association** for scans 1–3. It does not infer scan conditions, train or evaluate a decoder, calibrate report against experience, replicate Roy's EEG–fMRI finding, or settle the framework's experience bridge. The raw files contain DICOM-related fields that may be sensitive; none of those values is published here.

## 1. The three additional files

| Scan | Size (bytes) | SHA-256 | Dropbox content hash matched? | EEG samples | EEG TR markers | Report event codes 1 / 2 / 3 |
| --- | ---: | --- | --- | ---: | ---: | --- |
| 1 | 32,694,114 | `6b33288f2db8d899a8948a46de7300094c2812ba09aabb8c832b5ed8b85f56cf` | yes | 70,505 | 124 | 26 / 28 / 51 |
| 2 | 32,696,359 | `c9058648ea025ea29d316eddbd471ff7019304c232fd8acc5d688f1c86ad909c` | yes | 70,497 | 124 | 23 / 29 / 47 |
| 3 | 34,112,455 | `c4f5414be3ac09f3ad6fa2ebec3f262b1c4b7258fc993de1477e22517a4d866d` | yes | 70,510 | 127 | 24 / 29 / 48 |

All three contain 64-channel EEG at 250 Hz with finite sample values, five trial markers, the two frequency tags about 8.57 and 6.67 Hz and distinct one-to-one nearest same-code matches between the two recorded response representations. The EEG `condition` field is empty in each. TR counts here are markers in the EEG, **not fMRI volume counts**. Hash matches confirm that the local bytes match the Dropbox listing, not that they were independently checked against the original Zenodo archive.

The detailed summaries are [scan 1](verification/roy_s09_scan1_inspection.json), [scan 2](verification/roy_s09_scan2_inspection.json) and [scan 3](verification/roy_s09_scan3_inspection.json); [scans 4–6](ROY_S09_ADDITIONAL_SCANS_AND_REPEATED_REPORT_PATTERN.md) and [7–9](ROY_S09_THREE_SCAN_EMPIRICAL_INSPECTION.md) were analyzed earlier in separate runs. All refer to the [Roy data release](https://zenodo.org/records/5035511), its [README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1), [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).

## 2. Coverage across the available S09 scans

Following the previous [coverage reconstruction](ROY_S09_REPORT_COVERAGE_AND_DECODER_FLOOR.md), each run contributes five assumed 42-second trial windows. A report code is carried from its event until the next event or the end of that trial; before the first event the state is unknown. Code 3 is mixed. Unknown and mixed are treated as unresolved for this **binary** score, not as incorrect experiences. Exact stimulus onset and event semantics remain incompletely validated.

| Scan | Unknown + mixed / 210 s | Conditional union with `bad_epoch` |
| --- | ---: | ---: |
| 1 | 23.417% | 26.352% |
| 2 | 32.636% | 35.027% |
| 3 | 25.474% | 25.888% |
| 4 | 19.815% | 20.632% |
| 5 | 23.478% | 25.301% |
| 6 | 20.303% | 22.838% |
| 7 | 12.105% | 13.861% |
| 8 | 6.956% | 8.941% |
| 9 | 3.747% | 12.781% |

Across the nine equal-length scan windows, the pooled total is 1,890 seconds, including 34.944 seconds initially unknown and 317.712 seconds mixed; the combined fraction is **18.659%**. This is a descriptive total for the available recordings of one participant, not a population estimate or a claim about all conditions.

A binary full-coverage score that counts any unresolved report as a disagreement has a lower bound equal to the third column; for the pooled recording it is at least 18.659%, before considering the EEG. The last column is a stronger bound **only if a decoder also abstains on each `bad_epoch` sample**, counting overlaps once. This does not measure experience or a decoder's error, and the illustrative 10% target of the different randomized motion-audit protocol is not a prespecified success threshold here. [New scans 1–3 coverage output](verification/roy_s09_scans1_to3_report_coverage.json); earlier outputs cover [4–6](verification/roy_s09_scans4_to6_report_coverage.json) and [7–9](verification/roy_s09_report_coverage.json).

## 3. Exploratory EEG/report contrast, scans 1–3

To use the EEG without overriding the stop on condition-dependent decoding, I computed a descriptive, condition-blind association for the three newly available scans. It uses **POz only**, not a trained classifier and not the authors' optimized spatial filter or RLS pipeline:

1. In each assumed 42-second trial, partition time into 21 nonoverlapping two-second windows anchored to the recorded trial trigger. Keep a window only if every sample is reconstructed as the same pure report code (1 or 2) and no sample is marked `bad_epoch`.
2. Subtract the window mean and apply a symmetric Hann window. Project the EEG on complex sinusoids at the exact lower and higher stored tag frequencies, about 6.67 and 8.57 Hz. Compute `L = log10(power_low / power_high)` for each eligible window. Direct projection avoids rounding the frequency, but two-second windows still have limited frequency resolution and can include leakage and unrelated activity.
3. Within each trial, calculate the median L for code 1 minus the median L for code 2 if both exist. The scan summary below is the mean of the five paired-trial median differences. A positive value means the lower-to-higher power ratio is larger in code-1 than code-2 windows; it is not itself an accuracy or an effect on experience.

| Scan | Eligible code-1 / code-2 windows | Paired trials | Five within-trial differences (log10 power ratio) | Mean difference |
| --- | --- | ---: | --- | ---: |
| 1 | 15 / 18 | 5 | −0.035, −0.816, −1.076, −0.802, +1.085 | **−0.329** |
| 2 | 12 / 18 | 5 | +0.834, +0.179, −1.319, −2.305, +0.331 | **−0.456** |
| 3 | 12 / 21 | 5 | −0.097, +0.188, +0.593, +0.036, −0.039 | **+0.136** |

The selected pure, artifact-free windows cover just 66/210, 60/210 and 66/210 seconds in scans 1, 2 and 3. These are **report-selected stable windows**, not representative all-time coverage. Results vary in sign between and within scans; they were produced after earlier data inspections and are not a prespecified hypothesis test. Consecutive EEG windows and trials are not independent participants. No confidence interval or population inference follows from these numbers.

The release documentation describes report code 1 as green and 2 as red, and green/red tags near 6.67/8.57 Hz. A simplistic dominance-tracking intuition might suggest a positive contrast, but the negative means in scans 1–2 are **not** proof of a reversed mapping or a failed published method. The scan condition and trial-specific stimulus mapping need independent verification; the estimated signal may be weak, artifacts or background EEG may dominate, and this simple POz projection is not the optimized extraction used in the papers. Do not switch signs or choose a favorable electrode or time lag after looking at these outcomes and call that held-out performance. There is no decoder, and no neural–experience error rate is estimated.

## 4. What the complete set does and does not resolve

The additional scans strengthen the *descriptive single-person coverage accounting*. They do not turn the prior report-pattern similarity in [scans 4 and 6](ROY_S09_ADDITIONAL_SCANS_AND_REPEATED_REPORT_PATTERN.md) into evidence of identical stimulus histories: condition and replay lineage remain unverified. In this turn's additional exploratory comparison, among 75 between-scan pairs of trials in scans 1–3, seven pairs had equal numbers of report events; none had all ordinal event-time differences within 200 ms. This does not exclude shared stimulus history, because the comparison does not cover unequal-count pairs, other alignments or scans 4–9, and the 200 ms threshold was prompted by the previously observed pair. It is not an independent test of the earlier finding.

The next discriminating input is the **S09 scan-condition and stimulus/replay log**, or a reliable inspection of the original source document specifying that mapping. Until then, do not fit a task-labeled rivalry-versus-replay decoder or interpret any difference as a condition effect. Once mapping and trial lineage are independently established, freeze an EEG pipeline and its timing-only control on development data, hold out genuinely independent sequences, and report both all-time coverage and pure-report conditional performance. Even a successful prediction would concern report agreement; a separately warranted report-to-experience bound and the physical intervention gate remain missing.

## 5. Reproduction and checks

The calculations use NumPy 2.2.6 and SciPy 1.15.3. Given the authorized scan files, run:

```
PYTHONPATH=/your/dependency/dir python verification/roy_s09_report_coverage.py /path/to/scan1.mat /path/to/scan2.mat /path/to/scan3.mat
PYTHONPATH=/your/dependency/dir python verification/roy_s09_descriptive_tag_report.py /path/to/scan1.mat /path/to/scan2.mat /path/to/scan3.mat
PYTHONPATH=/your/dependency/dir python verification/roy_s09_descriptive_tag_report_test.py
```

The [descriptive EEG summary](verification/roy_s09_scans1_to3_descriptive_tag_report.json) records window counts and trial-level aggregates, without raw signals, event sequences or DICOM metadata. The [event-pattern screen](verification/roy_s09_event_similarity_screen.py) and its [aggregate output](verification/roy_s09_scans1_to3_event_similarity_screen.json) reproduce the 75 comparisons; give the same three scan paths to the script. The synthetic test checks frequency ordering, expected contrast for a constructed signal and exclusion of a bad window. It does not validate stimulus labels, human-report truth, preprocessing or any phenomenal claim. Respect the release's research/noncommercial terms and cite Roy and Jamison as requested.
