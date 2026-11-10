# S09: all nine supplied fMRI scans and structural image

## Results

Every file in the supplied scan-4, scan-5 and scan-6 ZIPs was read: **258 files per ZIP, 129 complete MRI header/image pairs per scan**, with indices 1–129, no other files and no gaps within the observed range. The separately supplied structural ZIP contains **two files**, a complete structural header/image pair; both were read in full.

With the six earlier functional ZIPs, **all nine supplied S09 fMRI scan archives have now been inspected: 1,185 MRI volumes in 2,370 pair files**. This describes the supplied ZIPs, not independent verification that the original subject archive contains nothing else. The [nine-scan summary](verification/roy_s09_nine_scan_mri_summary.json) combines the observed inventories and conditional timing gates.

| Scan | MRI volumes | EEG TR markers | MRI series number | Candidate first-trigger frame* |
| --- | ---: | ---: | ---: | --- |
| 1 | 141 | 124 | 7 | 1–18 |
| 2 | 141 | 124 | 9 | 1–18 |
| 3 | 129 | 127 | 10 | 1–3 |
| 4 | 129 | 126 | 11 | 1–4 |
| 5 | 129 | 124 | 12 | 1–6 |
| 6 | 129 | 124 | 13 | 1–6 |
| 7 | 129 | 126 | 16 | 1–4 |
| 8 | 129 | 124 | 17 | 1–6 |
| 9 | 129 | 125 | 18 | 1–5 |

\*These are mathematical candidates only, **assuming** the numbered volumes are temporally ordered at the recorded 2.2-second interval and every stored EEG TR marker matches a consecutive MRI frame. Neither assumption nor any specific candidate is independently established; dropped or reordered images or missing triggers can change the mapping. Matching series numbers are a consistency check, not proof of alignment. All nine EEG series numbers match the corresponding MRI series. For new scans 4, 5 and 6, the first trial's conditional time from MRI frame 1 ranges from 6.472–13.072 s, 1.752–12.752 s and 1.452–12.452 s respectively.

Seven functional ZIPs have 129 volumes and two have 141; their stored EEG marker counts range from 124 to 127. The [release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) describes 129 MRI volumes per scan and skipping five for steady-state BOLD, but this does not establish why scans 1–2 have 141 or how the stored markers map to any run's images. These observations do **not** by themselves imply that the study was flawed, the upload was incomplete, or an additional MRI volume is missing. Original acquisition and preprocessing/drop records, the included-volume list, SPM designs or another independent EEG-to-volume onset anchor remain necessary. Task-condition and replay-lineage records are separately needed for an appropriate condition comparison.

## Functional integrity and provenance

All 774 members of the three new functional ZIPs passed ZIP CRC and NIfTI decoding. Each run contains finite 53 × 63 × 46 `uint16` volumes with 3 mm isotropic spacing and common geometry. Each run has one shared header hash and 129 distinct image payload hashes. No image payload hash overlaps between **any of the 36 pairs** of the nine inspected series. This excludes byte-identical payloads across series, not shared experimental histories or statistical dependence. The new EEG files match the SHA-256 values in the earlier EEG inspections; their 250 Hz marker spacing is 550 samples = 2.2 seconds.

| Supplied ZIP | Bytes | SHA-256 | Dropbox content hash |
| --- | ---: | --- | --- |
| Scan 4 | 28,439,483 | `1052919ea8edb4230d0cbb93471baffd57fac245ff648569b142e5b06901cf38` | `275b1a4235fcf04d1958c9b801a0351a07a288eaed8673883f318b9d459bdab2` |
| Scan 5 | 28,431,164 | `fadc7e84221634774a1406daeb3af78f688f1173b387980a2eefbf0609f620da` | `f3b60d96a1269785bee880cfb12907f49af3b2b1fd8537d777472fe65a241b32` |
| Scan 6 | 28,446,579 | `af4809473b08d42d7597aae7f0b720bb53b92ea41a87263d711f80cfa965a138` | `2d19ee5ef4554aa4ed3236edf6229f84fc7806540f8a4fdffc1097d7e21589e6` |
| Structural | 40,360,288 | `31fe6fce984b1cf050adc77dba704819a76151936b8519c065d5efde551ca302` | `bf4ca5a3a7fe2fff6b002a59322d51fb42559f351ee42fedf8acd67457e708b9` |

Each locally computed Dropbox content hash matches its corresponding Dropbox metadata, confirming the transfer relative to the supplied object, not independent identity with the original released S09 archive. The released data are research/noncommercial, and the [README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) requests citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).

- Scan 4: [inventory](verification/roy_s09_scan4_full_fmri_inventory.json), [alignment](verification/roy_s09_scan4_alignment_gate.json), [sensitivity](verification/roy_s09_scan4_offset_sensitivity.json).
- Scan 5: [inventory](verification/roy_s09_scan5_full_fmri_inventory.json), [alignment](verification/roy_s09_scan5_alignment_gate.json), [sensitivity](verification/roy_s09_scan5_offset_sensitivity.json).
- Scan 6: [inventory](verification/roy_s09_scan6_full_fmri_inventory.json), [alignment](verification/roy_s09_scan6_alignment_gate.json), [sensitivity](verification/roy_s09_scan6_offset_sensitivity.json).
- Earlier functional scans: [1–2](ROY_S09_SCAN2_ALL_FMRI_VOLUMES_AND_COMPARISON.md), [3](ROY_S09_SCAN3_AND_TRIGGER_MISMATCH_AUDIT.md), [7–9](ROY_S09_SCANS_7_8_9_ALL_FMRI_VOLUMES.md).

## Structural image

The structural ZIP consists of one matching `.hdr`/`.img` pair. Both files were read completely and passed ZIP CRC and NIfTI-1 pair decoding. The structural volume is **256 × 256 × 176**, on-disk `float64`, with approximately 1 mm voxel spacing; all scaled voxel values are finite. Its oblique affine and both qform/sform codes are included as numeric geometry in the [structural QC output](verification/roy_s09_structural_inventory.json). The observed structural image alone does not establish coregistration to fMRI, successful defacing, diagnostic status, a brain segmentation or a timing anchor. No visual or automated anatomical/registration assessment was performed.

The raw images, source filenames and metadata strings are not included in this public repository. Metadata and imaging may be identifying; the release describes the structural MRI as de-faced, but this inspection does not independently certify that claim. File QC is not a clinical assessment.

## Analysis boundary and next step

The same **illustrative** whole-field mean/42-second boxcar-plus-HRF sensitivity diagnostic used previously gives Pearson r ranges +0.101 to +0.235, −0.234 to −0.114 and −0.221 to −0.100 for scans 4, 5 and 6 respectively across the unverified candidate offsets. These are not condition effects: they include background, have no motion/drift or serial-noise correction, lack verified event alignment, and do not reproduce Roy's event-related GLM. Do not choose an offset using these correlations.

The nine EEG and nine supplied fMRI series plus the structural pair make a more complete single-participant resource, but do not independently supply the missing temporal anchor or establish subjective experience. The previously observed scan-4/6 report-timing resemblance is post hoc and may indicate shared replay structure; it makes cross-run leakage controls important, not a verified condition assignment. A defensible next analysis requires an independently documented frame-to-trigger mapping and condition/replay lineage; use the structural image only after checking its registration and appropriate anatomical processing. One participant cannot reproduce the 20-subject group analysis or calibrate experience.

## Reproduction

With authorized local inputs and `numpy==2.2.6`, `nibabel==5.3.2`, `scipy==1.15.3`, substitute `N` with 4, 5 or 6:

```sh
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory.py /path/to/scanN.zip --expect-volumes 129
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate.py verification/roy_s09_scanN_full_fmri_inventory.json /path/to/S09_scanN_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity.py verification/roy_s09_scanN_full_fmri_inventory.json verification/roy_s09_scanN_alignment_gate.json /path/to/S09_scanN_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_structural_pair_inventory.py /path/to/structural.zip
python verification/roy_s09_mri_multi_scan_summary.py 1 2 3 4 5 6 7 8 9
PYTHONPATH=/your/deps python verification/roy_structural_pair_inventory_test.py
```

The scripts with historical `scan1` names accept the explicit scan inputs. Synthetic tests verify file handling, numerical rounding and summary consistency, not true physiological alignment or phenomenal interpretation.
