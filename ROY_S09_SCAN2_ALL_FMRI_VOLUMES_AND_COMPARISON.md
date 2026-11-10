# S09 scan 2: complete fMRI series and timing sensitivity

## Result

The supplied scan-2 ZIP was downloaded once and **every one of its 282 files was read**: 141 complete `.hdr`/`.img` pairs with consecutive frame indices 1–141. This matches the *count and geometry* found in the independently supplied [scan-1 archive](ROY_S09_SCAN1_ALL_FMRI_VOLUMES_AND_ALIGNMENT.md), but does not establish that the runs have the same experimental condition, temporal anchor or statistical design.

The matching scan-2 EEG file contains **124** TR markers. Under the same explicit and unverified consecutive one-to-one mapping assumptions used for scan 1, there are **18** candidate placements of those markers among the MRI frames. Neither dataset establishes which placement is correct. We also computed a clearly labeled, noninferential two-scan sensitivity diagnostic: changing those assumed placements can reverse the sign of the difference between crude global-signal correlations. This is **not** a rivalry-versus-replay result or a test of consciousness.

## 1. Provenance and complete file inspection

- `scan2.zip` is 31,077,490 bytes. Its SHA-256 is `8b778b91faa549fab71750c4cb421ceea70747ec9e015133de39f6a43b831a70`. The locally calculated Dropbox content hash `178efb511eb598b3bddc44949abc691089ea3006250853bcecc980a6d969a061` matches the Dropbox metadata. This confirms transfer integrity relative to the supplied Dropbox object, not independent identity with the original Zenodo ZIP.
- All **282 pair files** were read, with no other files in the ZIP and no missing frame indices between 1 and 141. Uncompressed pair data total 43,362,576 bytes. ZIP CRC validation, pair matching and NIfTI decoding completed.
- All 141 volumes were finite and share the same 53 × 63 × 46 geometry, 3 mm voxel spacing, `uint16` on-disk type and affine. All headers have one shared SHA-256; all 141 image payload hashes are distinct. This is integrity/QC, not proof of clean physiology, correct volume order, task validity or suitable statistical assumptions.
- The MRI series number is **9**, matching the series number stored in the separately supplied EEG scan-2 metadata; the EEG SHA-256 matches the previously inspected scan-2 file. This consistency check is not a stimulus-condition or temporal-alignment certificate.
- The scan-1 and scan-2 archives have identical geometry and header hashes, but **no image payload hash is common** between the two supplied series. This rules out byte-for-byte duplication of individual image payloads; it does not establish independent experimental sequences, independent subjects or independent neural processes.

The [full scan-2 inventory](verification/roy_s09_scan2_full_fmri_inventory.json) includes per-frame hashes and aggregate voxel QC, not raw images, original filenames or DICOM strings. Raw files remain outside Git because source metadata may be sensitive and the [release](https://zenodo.org/records/5035511) states research/noncommercial terms and requests citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).

## 2. Scan-2 timing gate

The EEG scan has 70,497 samples at 250 Hz and 124 TR markers spaced exactly 550 samples, or 2.2 s; embedded metadata likewise gives TR 2,200 ms. The first stored EEG trigger occurs 10.776 seconds after the first EEG sample, and the first trial trigger is 1.220 seconds after that EEG TR marker. These are not times relative to MRI frame 1.

Assume for the following **witness**, not as an established fact, that MRI frames 1–141 are temporally ordered at 2.2-second intervals and the 124 EEG triggers correspond one-to-one to a consecutive subset of frames. Without an independently established start anchor, the first trigger may map to any of frames **1 through 18**. The first trial marker consequently has 18 conditional positions from **1.220 to 38.620 seconds** after frame 1. These placements could be excluded by uninspected records; missing triggers or removed images could also invalidate the assumed mapping altogether. The [scan-2 alignment output](verification/roy_s09_scan2_alignment_gate.json) records all candidates.

Both scan archives have 141 pairs, the release README describes 129 image pairs, the paper describes a typical 121-volume GLM run, and each of these EEG files has 124 markers. The arithmetic `141 − 12 − 5 = 124` is **not** proof that those particular images were removed or that the markers map to the last 124 frames. Only actual acquisition/preprocessing records, volume onset correspondence or the original SPM design can settle the association.

## 3. Sensitivity—not a two-condition fMRI contrast

As for scan 1, take the observed whole-field mean of each image (including zero background) and correlate it with an illustrative series of five 42-second trial-onset boxcars convolved with a fixed `Gamma(6,1) − Gamma(16,1)/6` response. Compute this crude correlation at each of the 18 hypothetical placements. No alignment is selected to maximize agreement.

| Quantity | Scan 1 | Scan 2 |
| --- | ---: | ---: |
| Candidate placements | 18 | 18 |
| Range of descriptive Pearson r | −0.168 to +0.392 | +0.119 to +0.561 |

The [scan-2 values and assumptions](verification/roy_s09_scan2_offset_sensitivity.json) are reproduced using the same code as scan 1. These are **not fitted task-specific GLM effects**: there are no motion, drift or nuisance regressors, serial-noise correction, condition labels, independent-sample inference or multiplicity control. The chosen block onsets, duration, double-gamma HRF and 2.2-second image spacing are assumptions. A positive or negative value does not establish a neural correlate of experience.

If the two unknown placements are allowed to vary independently, the difference `r_scan2 − r_scan1` across all **18 × 18 = 324** hypothetical pairs ranges from **−0.273 to +0.729**, with 101 negative and 223 positive. Even imposing the additional unverified assumption that both scans use the *same* offset leaves a range of **−0.191 to +0.287**, with three negative and fifteen positive. The values are differences of raw descriptive correlations, not a tested effect size; the [comparison code and output](verification/roy_s09_two_scan_offset_comparison.json) enumerate rather than select the offsets. This illustrates why a result whose sign depends on unknown temporal alignment cannot be used to choose that alignment or establish a contrast.

## 4. Remaining decision and reproduction

The new archive completes inspection of scan 2 and provides another concrete timing gate; it does **not** supply the scan-condition/stimulus and replay lineage or an independently verified MRI-to-EEG start anchor. An appropriate analysis still needs the relevant acquisition/volume-time and preprocessing records or the original SPM design and included volume list. One participant and two scans cannot reproduce a 20-participant group result, and EEG/report agreement alone cannot supply the separate report-to-experience error bound. The earlier report-pattern similarity remains a warning about training/test leakage, not an inferred replay assignment.

With authorized local files and `numpy==2.2.6`, `nibabel==5.3.2`, `scipy==1.15.3`:

```
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory.py /path/to/scan2.zip --expect-volumes 141
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate.py verification/roy_s09_scan2_full_fmri_inventory.json /path/to/S09_scan2_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity.py verification/roy_s09_scan2_full_fmri_inventory.json verification/roy_s09_scan2_alignment_gate.json /path/to/S09_scan2_filtered_gac_cbc.mat
python verification/roy_s09_two_scan_offset_comparison.py verification/roy_s09_scan1_offset_sensitivity.json verification/roy_s09_scan2_offset_sensitivity.json
```

Despite their `scan1` filenames, the two alignment/sensitivity programs accept the explicitly provided input files and were executed for scan 2 as above. The inventory, candidate enumeration, numerical sensitivity and two-scan grid have synthetic regression tests; those tests validate code paths, not real experimental labels or physical–phenomenal claims.
