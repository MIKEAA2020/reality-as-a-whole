# Fixed S09-to-S08 EEG/report transfer: results and archive QC

## Main finding

The fixed S09-trained rule was applied, without S08 fitting or tuning, to the three supplied S08 rivalry EEG runs. On report-pure, artifact-clean windows, its accuracy **tied the time-only baseline when pooled: 48/81 = 59.3% for each**. The S09 training-majority baseline achieved 42/81 = 51.9%. Performance was not consistent across scans:

| S08 scan | Eligible / all windows | EEG rule | S09 majority | S09 time-only | EEG balanced accuracy |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 24 / 105 | 17/24 = 70.8% | 10/24 = 41.7% | 11/24 = 45.8% | 72.1% |
| 3 | 31 / 105 | 19/31 = 61.3% | 20/31 = 64.5% | 25/31 = 80.6% | 65.9% |
| 5 | 26 / 105 | 12/26 = 46.2% | 12/26 = 46.2% | 12/26 = 46.2% | 44.6% |
| Pooled, descriptive | 81 / 315 | 48/81 = 59.3% | 42/81 = 51.9% | 48/81 = 59.3% | 59.6% |

Thus the EEG rule exceeds both baselines in scan 1, falls below both in scan 3, and ties both in scan 5, for **ordinary accuracy**. This is a real participant-held-out feasibility result, not consistent superiority to a timing-only control, proof of general failure of EEG decoding, or an estimate of experience accuracy. The [JSON](verification/roy_s08_fixed_transfer.json) contains every model's confusion matrices, balanced accuracies and denominators.

The model was selected after S09 exploration; the [S08-specific procedure](ROY_S08_FIXED_TRANSFER_PROTOCOL.md) was fixed before these files were supplied and scored. It is retrospective work on a published dataset, not a prospectively preregistered study or an independent cohort. S08 is one new participant, and windows within trials and scans are dependent; pooled percentages are descriptive, not independent-replicate inference. No new tuning or model adaptation was done on S08.

## What the scores do and do not mean

Labels are reconstructed from report events, carrying each code forward within the assumed 42-second trial. Each score selects only two-second windows whose recorded report remains entirely in state 1 or 2 and has no marked artifact. This is **retrospective selection using the reports**, not an operational algorithm for recognizing pure states. It does not establish when experience changed or whether a report was correct.

Out of 315 total windows, 232 are unresolved under this rule and two are otherwise pure but artifact-marked; only 81 enter selected-window accuracy. If all unresolved and artifact windows are conservatively counted as failures, the EEG rule has **267/315 = 84.8% disagreement or unresolved**, with per-scan values 88/105 = 83.8%, 86/105 = 81.9% and 93/105 = 88.6%. This is a deliberately defined full-grid score, **not** evidence that those unresolved experiences were wrongly reported or decoded. The time-only rule has the same pooled full-grid score because it also gets 48 eligible windows correct.

## Input, coding and condition checks

All three EEG files were obtained separately, and their computed Dropbox content hashes matched the supplied Dropbox metadata; SHA-256 identifiers are in the JSON. Those checks establish transfer integrity relative to Dropbox, not independent authenticity of the original research archive. They contain finite 64-channel EEG at 250 Hz, one POz, five trial markers and the two required tag frequencies; expected epoch and event checks passed. Raw files and embedded metadata are not published.

The supplied original [release README](https://zenodo.org/records/5035511) page 1 describes dataset-wide button-press coding green = 1, red = 2 and mixed = 3; page 2 lists S08 scans 1, 3 and 5 as rivalry. The [pinned Lyu reanalysis script](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m) agrees on the condition labels, though the sources may share provenance. For S08, each code's trial-response entries matched a distinct nearest same-code latency event: **121/121, 116/116 and 124/124** across scans 1, 3 and 5. Across these matches latency-event minus trial-relative times ranged approximately **−27.2 to −4.4 ms**; no correction was made. The [audit](verification/roy_s08_report_code_audit.json) provides code counts and offsets. Together these checks substantiate the fixed protocol's coding gate at the documentation and internal-consistency level; they do not independently verify button hardware, trial-by-trial stimulus/eye mapping, color-frequency assignment or subjective experience. `freqtag1` is the higher frequency here; numeric variable order is not assumed to be a color label.

## Supplied fMRI scan ZIPs

All three additionally supplied scan ZIPs were downloaded separately, their Dropbox hashes matched, and **every file in each** was read through the pair QC. Each contained **141 complete header/image pairs**—423 volumes and 846 files in total—with no additional files or internal frame-number gaps. Within each archive the volumes shared a finite affine and consistent 53×63×46 geometry, uint16 storage and 3 mm voxel spacing; all scaled voxel values were finite. Matching EEG and image series identifiers provide consistency, not proof of temporal alignment, correct registration or successful defacing. Details and archive SHA-256s are in [MRI QC JSON](verification/roy_s08_mri_qc.json).

Each EEG file contains 129 TR markers at 550 samples = 2.2 seconds apart. **Conditionally**, if the 141 observed frames are consecutive and ordered, the EEG markers represent 129 consecutive frames, and none are missing, the first marker could correspond to any frame **1–13**. These are possible offsets under assumptions, not an inferred alignment. No EEG–fMRI GLM, stimulus reconstruction or alignment-based result was run. The original README's generic 129-image description does not by itself decide why these supplied scan folders contain 141 pairs. Keep MRI and EEG out of the public repository.

## Reproducibility and next step

The [fixed runner](verification/roy_s08_fixed_transfer.py) uses the earlier S09 model verbatim; the [coding audit](verification/roy_s08_report_code_audit.py) and [MRI QC](verification/roy_s08_mri_qc.py) perform separately labeled checks. The runner's private manifest contains local paths and provenance, not included in the repository. Synthetic tests cover the frozen model, baseline scoring, hash and series stops, and conditional trigger logic; the underlying MRI and EEG extraction also have synthetic tests. They do not validate the empirical or phenomenological assumptions.

To strengthen the empirical inference, freeze a subject-level evaluation across further participants before inspecting their outcomes and preserve replay/source grouping. The user subsequently reported that the authors cannot help with this study, so author clarification should not be treated as an expected next step; original coding and timing records remain unverified where noted. Additional S08 tuning would be exploratory, not a new held-out test. The [post-Roy decision](POST_ROY_FRAMEWORK_CRITICAL_PATH.md) explains why we are moving back to the framework gaps. Even robust report prediction would not settle the experiential nature or self-existence of the proposed whole. The dataset requests research/noncommercial use and citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).
