# Roy S09: a report-coverage floor before decoding

## Result and scope

Using the three available Roy S09 EEG files, I reconstructed report intervals under explicit, provisional timing assumptions. On the **full trial-time denominator**, the fraction that was mixed or preceded the first report event was:

| Scan | Unknown before first report | Mixed report | Combined | Pure code 1 or 2 |
| --- | ---: | ---: | ---: | ---: |
| 7 | 3.672 s | 21.748 s | **12.105%** | 87.895% |
| 8 | 3.380 s | 11.228 s | **6.956%** | 93.044% |
| 9 | 3.376 s | 4.492 s | **3.747%** | 96.253% |

Each denominator is five assumed 42-second trials, or 210 seconds, sampled at 250 Hz. This is a **real, exploratory analysis of one person's three scans**, not an estimate across participants, an EEG decoder evaluation, or a test of experience. Scan conditions remain unverified: no differences here are attributed to rivalry or replay.

The methodological consequence is exact **conditional on this reconstruction and coding**. In the proposed conservative binary score, any unresolved report counts as disagreement, regardless of the decoder output. Therefore the measured full-coverage disagreement for scan 7 cannot be less than **12.105%**, even if the decoder matches perfectly at every pure-report sample. This is a floor created by the score and the report coverage—not evidence that the decoder is wrong or that mixed perception is erroneous.

The previous [random-audit proposal](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) mentioned a 10% threshold for a *different* motion/eye-tracking assay with randomized prompts. These data do **not** test that hypothesis, and the 10% figure is not a preregistered success criterion for these retrospective color reports. The example shows why thresholds, coding and denominators must be reconciled **before** using them in a new experiment.

## 1. Reconstruction and what it assumes

The [release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) describes five 42-second trials and report-event codes 1, 2 and 3 for green, red and mixed. The earlier [three-scan inspection](ROY_S09_THREE_SCAN_EMPIRICAL_INSPECTION.md) established that `latency_s1`, `latency_s2`, `latency_s3` and trial-relative response entries have matching event counts and one-to-one nearest matches, although their times differ slightly and the cause is unknown.

For this diagnostic only:

1. Start a 42-second interval at each recorded `latency_trial` marker. Convert MATLAB 1-based sample indices to 0-based indices.
2. In each trial, label samples **unknown** until the first `latency_s1`, `latency_s2` or `latency_s3` marker. Carry that marker's recorded code forward until the next report marker or the end of that trial. Reset to unknown at the next trial rather than carrying a prior report across the rest interval.
3. Treat code 3 as unresolved for the proposed **binary** green/red comparison, not as a mistaken report. Treat unknown as unresolved too. The state at a sample is reconstructed from event markers; it is not independently verified against button hardware or subjective experience.
4. Include every sample of the assumed trial intervals in the full denominator, including samples marked `bad_epoch`. The binary disagreement floor below concerns this denominator. A separate sensitivity calculation excludes the `bad_epoch` samples.

The 42-second duration follows the published documentation, but the precise physical onset relative to the recorded trigger and the persistence of a reported state to the next marker are assumptions. No attempt is made to use `trialResponse.domResponse` as if it had identical timing: differences between those response times and EEG event markers varied by trial. The summary is not a frozen prospective analysis; the files have already been inspected.

## 2. The bound and its practical effect

Let `R` be the reconstructed report and `Y` any binary or unresolved decoder output. Define `d_full` as the fraction of full-trial samples where `Y` and `R` disagree **or either is unresolved**. Let `u` be the fraction where `R` is mixed or unknown. By the scoring definition, every `R=⊥` sample is included in the disagreement set, regardless of `Y`. Thus

```
d_full ≥ u.
```

This is a counting bound, not a statistical confidence interval, a neural result or a new general statistical theorem. A higher score may arise from actual decoder/report mismatch, decoder abstention, measurement artifact or coding choices. `u` is not an error rate against experience; a mixed report can faithfully describe a mixed percept.

If an EEG decoder also **abstains on every `bad_epoch` sample**, the fraction in the union of `bad_epoch` and unresolved reports is an additional conditional floor, avoiding double counting overlapping samples:

| Scan | Unknown-or-mixed floor, all trial samples | Conditional floor if decoder abstains on every `bad_epoch` sample | Unknown-or-mixed among samples outside `bad_epoch` |
| --- | ---: | ---: | ---: |
| 7 | 12.105% | 13.861% | 11.932% |
| 8 | 6.956% | 8.941% | 6.695% |
| 9 | 3.747% | 12.781% | 4.061% |

The middle column is conditional: we have not run a decoder or shown that it abstains on those samples. The right column changes the denominator and target population; it is **not** a full-coverage result. Excluding artifact or mixed intervals may be appropriate for a separate conditional analysis, but it must be accompanied by coverage and cannot be relabeled as all-time accuracy.

## 3. Event-pattern check

Among adjacent `pure → mixed → pure` marker triples within a trial, the observed counts were:

| Scan | Code 1 → 1 | 1 → 2 | 2 → 1 | 2 → 2 |
| --- | ---: | ---: | ---: | ---: |
| 7 | 1 | 18 | 17 | 1 |
| 8 | 1 | 47 | 49 | 0 |
| 9 | 0 | 19 | 19 | 0 |

These are counts of a specific pattern in event records, not all perceptual changes or independent samples; incomplete patterns at trial boundaries are excluded. Most observed triples here lead to the opposite pure code, which is consistent with the documented coding of mixed periods as transitions, but does not determine the scan condition. Different counts and durations cannot by themselves identify rivalry versus replay.

## 4. Implication for the experience bridge

This check makes a previously abstract denominator problem concrete: the proposed conservative binary score includes mixed and missing reports as failures, so its threshold can be unattainable in a particular run before neural data are considered. That does not mean the original threshold is refuted, because the original assay targets a different population, signal, task, and randomly sampled context.

A future assay could explicitly use a **three-state report and decoder** (green/red/mixed) plus an unresolved state. That would preserve mixed reports as a legitimate target, but it defines a different operational outcome and requires its own frozen eligibility, time alignment and validation. It still would not establish a numerical report-to-experience error bound. The existing bridge `P(Y wrong or unresolved about E) ≤ min(1,d+r)` remains conditional on a separately justified, same-context `r`; none is established here. Neither this coverage result nor a successful decoder would by itself discriminate subject-constitution rules or establish a causal phenomenal substrate.

## 5. Next and reproduction

The scan conditions and stimulus/eye assignments are still not independently verified, so the earlier stop gate remains: **do not train or score a task-labeled rivalry/replay decoder yet**. The source documentation is available as extracted text, but its layout around subject scan lists is ambiguous. Obtain the original S09 scan-condition/stimulus log or a reliably inspected original document before interpreting differences among these runs. Record timing uncertainty, then evaluate held-out runs and report all-time coverage alongside pure-report conditional performance.

Reproduce from the same authorized local `.mat` files using NumPy 2.2.6 and SciPy 1.15.3:

```
PYTHONPATH=/your/dependency/dir python verification/roy_s09_report_coverage.py \
  /path/to/S09_scan7_filtered_gac_cbc.mat \
  /path/to/S09_scan8_filtered_gac_cbc.mat \
  /path/to/S09_scan9_filtered_gac_cbc.mat
PYTHONPATH=/your/dependency/dir python verification/roy_s09_report_coverage_test.py
```

The [saved aggregate output](verification/roy_s09_report_coverage.json) includes source hashes, counts and assumptions, not raw EEG, event sequences or embedded DICOM metadata. The synthetic regression tests interval construction, overlap-aware union counting and the stop on duplicate event times; passing it does not validate the event semantics. Keep the source files out of the public repository and respect the dataset's research/noncommercial terms.
