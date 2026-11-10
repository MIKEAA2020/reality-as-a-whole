# Roy S09: first inspection of three EEG scans

## What was done

Three preprocessed EEG files for **one participant**, scans 7–9, were supplied through Dropbox. They were downloaded **one at a time**, inspected locally and verified against Dropbox's per-file content hashes. The 606.6 MB ZIP was not downloaded. This is a genuine analysis of the supplied files, but it is exploratory **data-quality and event-alignment inspection**, not a population study, reproduction of Roy's results, randomized audit, decoder validation or measurement of experience.

The source is [Roy et al. (2017)](https://doi.org/10.1016/j.neuroimage.2017.02.041), using techniques described by [Jamison et al. (2015)](https://doi.org/10.1016/j.jneumeth.2015.01.024); see the [dataset README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1). This inspection follows the stop rules in [the earlier feasibility plan](RIVALRY_EEG_FMRI_FEASIBILITY_AND_REANALYSIS_GATE.md). The released data are described as available for research/noncommercial use, with both papers to be cited.

## File integrity and scope

| Scan | File size, bytes | SHA-256 | Dropbox content hash matches listing? |
| --- | ---: | --- | --- |
| 7 | 33,955,147 | `c024063191583b7c4b75204233cac4e071f213a80b7064237db6475cd89501e8` | yes |
| 8 | 33,038,187 | `cadeee7e70dc1ee09fa1d6b12ab8387ea3a5195618a00fcba963f41b14802027` | yes |
| 9 | 33,311,041 | `2a2b9602b4d0a7ed9d5e98a0b3921b8af125c146e868b47d8dd3f37e2805366d` | yes |

A Dropbox content hash is SHA-256 of the concatenated SHA-256 digests of consecutive 4 MiB blocks; it is **not** the ordinary full-file SHA-256. These checks verify each local file against its Dropbox listing, not against the Zenodo ZIP checksum or independent custody of the original release.

**Privacy:** the MATLAB structures contain DICOM metadata fields that may carry sensitive or identifying information, notwithstanding an EEG field marked deidentified. This report and the code intentionally exclude their values. The raw files are not committed to the public repository. Treat source files and metadata as potentially sensitive; do not redistribute them or treat this notice as a complete privacy audit.

## 1. Structural and timing findings

Each `EEG` struct contains 64 channels at 250 Hz, with all stored sample values finite; each has five trial starts and a `trialResponse` structure. The EEG data length varies slightly by scan.

| Scan | Samples | EEG sample span (s) | Recorded `latency_tr` entries | Response codes 1 / 2 / 3 | `bad_epoch` samples |
| --- | ---: | ---: | ---: | --- | ---: |
| 7 | 70,506 | 282.020 | 126 | 20 / 22 / 39 | 8,954 |
| 8 | 70,519 | 282.072 | 124 | 50 / 53 / 97 | 8,324 |
| 9 | 70,509 | 282.032 | 125 | 22 / 22 / 38 | 11,055 |

Span is `(samples−1)/250`, not a claim about how acquisition duration was defined in the README. **Correction:** the previously reported 551-sample gap in scan 9 was an integer-truncation artifact, not a real observed gap; reinspection with numerical-roundoff handling gives 550 samples throughout. See the [scan-3 and trigger-mismatch audit](ROY_S09_SCAN3_AND_TRIGGER_MISMATCH_AUDIT.md). These are **EEG trigger counts**, not MRI image counts; they cannot settle the README's 129 MRI volumes versus the paper's typical 121 GLM volumes. The variable counts across scans make it particularly unsafe to force a single assumed row count or trimming rule.

All three files have `freqtag1 = 8.57142857 Hz` and `freqtag2 = 6.66666667 Hz`. The release README names green as 6.67 and red as 8.57 Hz; thus **the numbered variables cannot simply be assumed to correspond to green then red**. This finding alone does not establish what the two numbered variables mean, or a color-to-frequency assignment for each trial. The subject's condition, trial-level color/eye assignments and ordering still require verification against actual original documentation or stimulus records. `EEG.condition` is empty in the inspected files. Do not infer scan condition or the target from response count or tag ordering.

## 2. Two representations of button events are close, not identical

The files contain both event-sample arrays `latency_s1`, `latency_s2`, `latency_s3` and, for each trial, two-column `trialResponse.domResponse` arrays. For each response code and trial, this check constructs `trial_start + response_time×250` and matches it to the nearest event of the same code. All response counts in each scan match the corresponding event counts, and the matches are **one-to-one**: 81/81, 200/200 and 82/82 responses in scans 7, 8 and 9 respectively. This supports the interpretation that these arrays refer to corresponding markers; it does not establish the exact physical/perceptual onset.

The event-sample time minus the reconstructed response time has a trial-dependent median:

| Scan | Five trial medians (ms) |
| --- | --- |
| 7 | −18.2, −4.9, −3.0, −5.8, −4.7 |
| 8 | −18.3, −42.0, −39.9, −43.6, −40.7 |
| 9 | −42.8, −42.4, −35.9, −39.0, −39.4 |

Across the three files the individual matched offsets range approximately −45.6 to −2.0 ms. This comparison uses the recorded trial trigger as the response time origin; the MATLAB 1-based convention cancels in the subtraction. The discrepancy could reflect different event definitions, clock alignment, trial-onset timing or quantization; its cause is unknown. It is not a measurement of reaction time or report error, and is not enough to determine which representation is ground truth. A single global fixed correction would be unjustified without additional timing provenance. The period-to-period variability matters for precise temporal alignment, even though it is much smaller than Roy's published average cross-to-button delays.

## 3. An exploratory spectral sanity check

As a data-inspection diagnostic—not the paper's decoder—we used only preselected electrodes Oz and POz. Within each reported trial, we took nonoverlapping 4-second Hann-window periodograms starting 2, 6, …, 38 seconds after the trial trigger; windows with any `bad_epoch` sample were excluded. We averaged the surviving spectra and divided power at the nearest 0.25 Hz Fourier bin to each named tag by the median power at bins 0.5–1 Hz away from that tag.

| Scan | Clean windows (of 50) | Oz: 8.57 / 6.67 | POz: 8.57 / 6.67 |
| --- | ---: | --- | --- |
| 7 | 47 | 1.379 / 1.051 | 1.595 / 1.403 |
| 8 | 47 | 1.402 / 1.241 | 1.439 / 1.569 |
| 9 | 39 | 1.547 / 1.019 | 1.316 / 0.942 |

These local power ratios are descriptive only. The nearest bins are **8.50 and 6.75 Hz**, not the exact tag frequencies; 4-second resolution, leakage, intrinsic alpha activity, the sideband definition, artifact masking and electrode choice influence the ratios. The released EEG is already preprocessed, and this simple diagnostic is not Roy/Jamison's optimized spatial filter or adaptive RLS envelope extraction. It does not establish a detection threshold, decoding performance, color–percept association, causal mechanism or absence of a neural response. In particular, a ratio below one does not prove that a tag is absent.

## 4. Stop gate and next defensible analysis

The three scans have useful EEG and report markers, but **scan conditions and trial-specific stimulus/eye assignments are not yet independently verified**. The extracted README text is ambiguous for some subject scan lists, and the `EEG.condition` fields inspected here are empty. We therefore stop short of fitting or scoring a report decoder, assigning these files to rivalry versus replay, pooling them as one task, or claiming a rivalry–replay difference. The condition labels and exact timing conventions must be resolved from original scan documentation, stimulus logs or author clarification, rather than chosen based on the desired EEG–report result.

Once those labels and mappings are verified, use separate runs for train/test with any spatial filtering, normalization, lag, and thresholds trained only on training runs. Evaluate held-out agreement with pure and mixed-report coverage, report missingness and artifact masks, and treat the result as a **single-person feasibility pilot**. Three runs in one person do not support a population claim. The prospective randomized experience bridge would still require its own data and independently justified report-to-experience bound; this inspection supplies neither.

## 5. Reproduction and data handling

Run `python -m pip install --target /your/dependency/dir numpy==2.2.6 scipy==1.15.3`, then for an authorized local input:

```
PYTHONPATH=/your/dependency/dir python verification/roy_s09_scan_inspection.py /path/to/S09_scan8_filtered_gac_cbc.mat
```

The script writes its non-identifying summary to stdout; use corresponding scan 7/9 files to reproduce the other summaries. Saved results are [scan 7](verification/roy_s09_scan7_inspection.json), [scan 8](verification/roy_s09_scan8_inspection.json), and [scan 9](verification/roy_s09_scan9_inspection.json). The raw files and installation environment are not in Git. Do not share detailed `dcminfo` metadata when reproducing the analysis.
