# Roy S09: three additional scans and a repeated report pattern

## Summary

The three newly supplied EEG files are S09 scans **4, 5 and 6**. They were downloaded separately, locally inspected and verified against their Dropbox content hashes. This extends the earlier descriptive work on [scans 7–9](ROY_S09_THREE_SCAN_EMPIRICAL_INSPECTION.md); all six are from **one participant**, and the full ZIP was not downloaded. The raw MATLAB files may contain sensitive metadata and are not committed.

A useful new observation emerged: in **trial 4 of scans 4 and 6**, all 37 report events have corresponding event codes when codes 1 and 2 are swapped, and their within-trial event timings are close. This is a **post-hoc report-pattern comparison**, not a decoder, an independent test, or proof of how the experiment generated the pattern. It exposes a concrete reason why splitting by scan alone may be insufficient to rule out shared timing information in a future predictive analysis.

## 1. File and event checks

| Scan | Size (bytes) | SHA-256 | Dropbox content hash matched? | EEG samples | TR marker count | Report-code events 1 / 2 / 3 |
| --- | ---: | --- | --- | ---: | ---: | --- |
| 4 | 33,966,683 | `79dc71c6cf7d9afbcfdbfd982730e9e6e83134e35be91c01c98dd6e8bdbb114a` | yes | 70,518 | 126 | 49 / 51 / 96 |
| 5 | 32,835,533 | `0173436c473a145546b275fa4c4c30b5dab17ba24d7b550cfa5b2e0a09718fa1` | yes | 70,506 | 124 | 23 / 24 / 44 |
| 6 | 32,778,415 | `045fdfd2cb31c2f6b08f09afe892a8d6af2f9961626d99f74c2693d51c0394ac` | yes | 70,518 | 124 | 51 / 49 / 96 |

Each is 64-channel EEG at 250 Hz with finite stored values. As in scans 7–9, the variables `freqtag1` and `freqtag2` are about 8.57 and 6.67 Hz, respectively. Do not assume their numeric order identifies green/red. Each `trialResponse.domResponse` marker had a distinct nearest same-code match among the `latency_s1/s2/s3` arrays: 196/196, 91/91 and 196/196 in scans 4, 5 and 6. The per-trial median offset between the two event-time representations ranges from about −4.7 to −38.8 ms in these scans. That is not an independently calibrated physical onset or reaction time.

TR markers are EEG events, not counts of available fMRI volumes. These checks neither settle the 129-versus-121 volume discrepancy nor identify the scan conditions. The detailed non-identifying summaries are [scan 4](verification/roy_s09_scan4_inspection.json), [scan 5](verification/roy_s09_scan5_inspection.json) and [scan 6](verification/roy_s09_scan6_inspection.json). Per-file SHA-256 and the separately computed Dropbox content hash verify local bytes against the Dropbox listing, not against the original Zenodo ZIP checksum.

## 2. Report coverage in all six inspected scans

Using the same event-carry-forward reconstruction and assumed 42-second trial durations as the [previous coverage analysis](ROY_S09_REPORT_COVERAGE_AND_DECODER_FLOOR.md), each scan has five trials and 210 seconds on the full denominator. Before the first report in a trial is unknown; code 3 is mixed. Both count as unresolved **only for the specified conservative binary score**.

| Scan | Unknown (s) | Mixed (s) | Unknown or mixed, full trial time | Conditional union with `bad_epoch` |
| --- | ---: | ---: | ---: | ---: |
| 4 | 4.252 | 37.360 | **19.815%** | 20.632% |
| 5 | 4.164 | 45.140 | **23.478%** | 25.301% |
| 6 | 3.528 | 39.108 | **20.303%** | 22.838% |
| 7 | 3.672 | 21.748 | **12.105%** | 13.861% |
| 8 | 3.380 | 11.228 | **6.956%** | 8.941% |
| 9 | 3.376 | 4.492 | **3.747%** | 12.781% |

A binary score that counts every unresolved report as disagreement has a per-scan floor equal to the fourth column. The union is a further floor **only if the decoder abstains on each `bad_epoch` sample**, and overlapping samples are not double counted. Neither floor is a decoder's measured error, a report-to-experience error, or evidence that a mixed report is wrong. Different scan conditions, trial presentations or reporting contexts could explain the variation; without independently verified conditions, do not infer a rivalry/replay difference. The 10% threshold in the previous random-probe motion assay is not a preregistered threshold for these data.

The additional scan coverage output is [here](verification/roy_s09_scans4_to6_report_coverage.json); the 7–9 numbers are from the already saved [earlier output](verification/roy_s09_report_coverage.json). They were produced in separate runs of the same script, not by a new analysis of all six raw files in this turn.

## 3. A post-hoc timing match that matters for validation

For trial 4, reconstruct the event series relative to its own recorded trial trigger in each of scans 4 and 6. Each contains 37 report events. Pairing events by ordinal position:

- **18/37** have identical recorded codes; **37/37** match if 1 and 2 are exchanged while 3 is unchanged.
- The scan 4 minus scan 6 event-time offsets have median **16 ms**, RMS **73.3 ms**, and range **−200 to +184 ms**.
- On the **33.244 seconds** where both reconstructed states are pure, the swapped codes agree for **100%** of samples, and the unswapped codes agree for **0%**. This excludes time when either is unknown or mixed. Over all 42 seconds, the swapped pure agreement is **79.152%** when any nonpure interval is conservatively treated as disagreement.

The assumed trial window and carry-forward interpretation are the same as in the coverage analysis; these numbers are **report-to-report**, with no EEG features involved. The pair, trial and swap were found after examining the data. They are not a prespecified generalization test, no p-value is warranted here, and they do not establish that the conditions, stimuli, percepts or neural processes are identical. Replay, shared timing, counterbalancing and other explanations need original stimulus records; no particular cause is established.

Nevertheless, the observation directly changes a proposed analysis design: if report patterns or physical replay schedules recur across runs, a classifier with access to trial-relative time or a stimulus-linked proxy could appear to generalize across runs without independently tracking spontaneous experience. Cross-run separation remains necessary but may not by itself defeat this failure mode. In addition, swapping labels **after looking at the test report**, as done for this exploration, is test leakage and cannot be used as a successful held-out decoder score.

## 4. Revised test gate

Before training a task-labeled decoder, resolve the scan conditions and trial-level stimulus/eye mappings from the original S09 records. Then:

1. Group trials with shared or replayed source sequences in the **same split**, using independently documented stimulus lineage, not observed test outcomes. If lineage is unavailable, report the limitation and use a genuinely independent participant or newly generated stimulus sequences for confirmation.
2. Freeze mapping, spatial filters, lag, features, thresholds, artifact handling and splits using development data. No test-label-based flip or selection.
3. Compare EEG predictions with a frozen **time-only / replay-schedule baseline** using only information actually available before a held-out test; the specific data-selected swap above is not such a baseline. Also consider motor/report artifacts and whether earlier preprocessing used information across train/test runs.
4. Report pure-conditional performance, full-denominator disagreement with unresolved outputs, excluded coverage, and participant-level uncertainty separately. Good agreement with reports remains different from accuracy against felt experience and does not establish a physical–phenomenal law.

None of these steps supplies the independent report-to-experience bound or physical-intervention gate required for the existing framework's stronger claims. Nor does this scan-level observation test C/M subject constitution.

## 5. Reproduction

With `numpy==2.2.6` and `scipy==1.15.3`, run the existing `verification/roy_s09_scan_inspection.py` separately on each authorized `.mat` and `verification/roy_s09_report_coverage.py` on scans 4–6. Reproduce the exploratory trial comparison with:

```
PYTHONPATH=/your/dependency/dir python verification/roy_s09_repeated_report_pattern.py \
  /path/to/S09_scan4_filtered_gac_cbc.mat \
  /path/to/S09_scan6_filtered_gac_cbc.mat --trial 4
PYTHONPATH=/your/dependency/dir python verification/roy_s09_repeated_report_pattern_test.py
```

The [comparison JSON](verification/roy_s09_repeated_report_pattern.json) contains aggregate results and file hashes, not event sequences, EEG or DICOM fields. Synthetic tests check the code's swap, denominator and unequal-count stop, not the real data's stimulus lineage or behavioral interpretation. Respect the [release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1)'s research/noncommercial terms and cite Roy and Jamison as requested.
