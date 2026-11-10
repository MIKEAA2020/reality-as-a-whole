# S09 scan 3 and the MRI–EEG trigger-count mismatch

## Direct answer

The mismatch by itself does **not** show that Roy et al.'s study was flawed, that the user failed to upload something, or that the assistant missed files from the supplied scan-1 and scan-2 ZIPs. I read every member in those two ZIPs and the separately downloaded corresponding EEG `.mat` files. Each ZIP contained 141 complete, consecutively indexed MRI pairs; each EEG file contains 124 stored TR markers. These are different kinds of counts: one counts MRI image files, the other markers present in a processed EEG file. A one-to-one equality is not guaranteed if the recordings cover different intervals or preprocessing retains or removes different volumes or markers. **That is a possible explanation, not an established account of these runs.**

What remains unresolved is why the two supplied MRI series contain 141 pairs when the [dataset README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) describes 129 per scan, and how the 124 markers relate to the images. The ZIPs have no gaps *within their observed indexed ranges*. That does not prove the ZIPs contain every file from the original released subject archive or that no metadata/design/log files exist elsewhere. The transfers match the Dropbox hashes, but no original archive-to-extracted-file manifest has been checked. Earlier searches for logs were limited, not a complete search of the subject archive or Dropbox. Thus missing **additional alignment information** remains possible; the existing evidence does not say that additional MRI files are needed or missing.

The README's 129 images and instruction to skip five yields 124 retained images by arithmetic, but **does not state that those images correspond to the 124 stored EEG markers**. The paper's typical first-level model uses 121 volumes per run; it does not specify that this participant had the typical selection. The reason for the differences is not documented in the records examined. The original SPM design and included-volume list, preprocessing/drop records, or scanner-volume/EEG trigger onset mapping could resolve this; trial timing, condition and motion information are also needed for the intended analysis. The authors synchronized the scanner and EEG clocks ([Roy et al., methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC5531216/)); clock synchronization does not itself establish which preprocessed MRI frame corresponds to a stored EEG marker.

## New complete scan-3 inspection

The newly supplied scan-3 ZIP is **28,435,811 bytes**; SHA-256 `37459dc7096c3dd1050df0ee21857c50751997ecba6fe324ef33bc6782ed19c4`, Dropbox content hash `ecac0c2d65db4ee3cc62e70d911d9984aad4087306ab0cd5e2a34488a8c43a94`, matching Dropbox metadata. This verifies transfer against the supplied object, not identity with the original release.

Every one of its **258 files** was read: **129** `.hdr`/`.img` pairs, indices 1–129, with no other members or gaps inside that range. ZIP CRC checks and NIfTI decoding passed. All 129 images are finite 53 × 63 × 46 `uint16` volumes with 3 mm spacing and identical geometry; all headers share one hash and all image payloads are distinct. No image payload hash is shared with the prior two scanned ZIP inventories. Distinct payloads do not establish statistical or experimental independence. The MRI series number is 10, matching the corresponding scan-3 EEG's embedded series number; this is a consistency check, not an alignment certificate. The [inventory](verification/roy_s09_scan3_full_fmri_inventory.json) contains hashes and summary QC, not raw images or identifying source filenames.

| Supplied scan | MRI pairs read | EEG TR markers | Consecutive-mapping candidate first MRI frames* |
| --- | ---: | ---: | ---: |
| 1 | 141 | 124 | 1–18 |
| 2 | 141 | 124 | 1–18 |
| 3 | 129 | 127 | 1–3 |

\*Only assuming the image numbers represent equally spaced chronological volumes and all stored markers match a consecutive, one-to-one subset. Neither assumption nor physical feasibility has been independently established. Missing markers, dropped or reordered frames, or other acquisition history could invalidate this enumeration. Three candidates does **not** prove that only three alignments are physically possible. For scan 3, marker spacing is 550 samples at 250 Hz = 2.2 seconds, and under the assumptions the first trial occurs 7.220, 9.420 or 11.620 seconds after MRI frame 1, respectively. See [alignment output](verification/roy_s09_scan3_alignment_gate.json).

For continuity with earlier QC, the same illustrative all-voxel global-mean versus five 42-second boxcars convolved with a fixed double-gamma HRF gives correlations of −0.162, −0.146 and −0.139 for the three assumed placements. These values include background, lack drift and motion corrections, do not represent Roy's event-related GLM and cannot identify the correct alignment, condition, neural correlate of awareness or effect. See [sensitivity output](verification/roy_s09_scan3_offset_sensitivity.json). Do not select an alignment based on these correlations.

## Correction: manufactured 551-sample gaps

I initially said during this scan that its trigger spacing was irregular. **That was my code's error, not a finding about the study.** Six early values were stored microscopically below integer sample indices (maximum deviation `4.55 × 10⁻¹³` samples). Casting them directly to integers truncated them, creating a false 551-sample gap. The corrected code rounds only values within `10⁻⁷` samples of an integer and rejects genuinely fractional or non-finite values. Scan 3's 126 intervals are all 550 samples after correction.

I also re-downloaded and rechecked the previously reported scans 5, 6 and 9, whose inspection summaries had the same apparent 551-sample gap. Their floating-point deviations are likewise at most `4.55 × 10⁻¹³` samples and their intervals are all 550 samples after rounding. The previous scan-9 narrative and the four affected JSON summaries have been corrected; the other fields of those JSON summaries were unchanged. Prior report/EEG contrast analyses were not based on these truncated TR interval values. Regression tests now check numerical roundoff, reject genuinely fractional indices and cover the three-candidate count. Neither those tests nor the regular spacing validates real MRI-to-EEG alignment.

## Reproduction and scope

With authorized local files and `numpy==2.2.6`, `nibabel==5.3.2`, `scipy==1.15.3`:

```sh
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory.py /path/to/scan3.zip --expect-volumes 129
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate.py verification/roy_s09_scan3_full_fmri_inventory.json /path/to/S09_scan3_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity.py verification/roy_s09_scan3_full_fmri_inventory.json verification/roy_s09_scan3_alignment_gate.json /path/to/S09_scan3_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate_test.py
```

The scripts accept explicit scan-specific inputs despite their historical `scan1` filenames. The inspection uses bounded local files rather than bulk downloading the whole subject archive; raw MRI and EEG files are not committed because source metadata may be identifying. The [data release](https://zenodo.org/records/5035511) specifies research/noncommercial use and requests citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024). This is one participant, not replication of the 20-person group GLM or an experience calibration.
