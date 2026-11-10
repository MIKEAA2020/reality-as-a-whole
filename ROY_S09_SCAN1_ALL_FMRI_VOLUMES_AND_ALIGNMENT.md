# S09 scan 1: all 282 fMRI files read, alignment still unresolved

## Result

The supplied scan-1 ZIP has been downloaded once and **all 282 files read**: 141 `.hdr`/`.img` pairs. The content covers consecutive frame indices 1–141, with no missing indices in that range. All 141 volumes were readable and finite, with identical geometry; the 141 image payloads have distinct SHA-256 hashes. This completes the requested file-level inspection, superseding the earlier [two-volume sample](ROY_S09_SCAN1_FMRI_ACCESS_AND_SAMPLE.md).

This is a real inspection of the complete supplied scan-1 fMRI series, followed by a **conditional alignment sensitivity analysis**. It is not a replay of Roy's published GLM, a rivalry-versus-replay test, or evidence that an observed BOLD signal constitutes experience. The scan condition, original volume/EEG synchronization and first-level model remain unverified.

## 1. Provenance and full-series checks

- The supplied ZIP is 31,072,853 bytes; its ordinary SHA-256 is `3185f8a3e5d4c6d3d6dd3962bd520ed58b936cb08786aabc3b8fa8c0f667f5df`. Its locally calculated Dropbox content hash `ecee91a833151393c77f4e2212436e596e7650f4cbf9ac7111524825c1cd36b5` matches the Dropbox metadata. This establishes transfer integrity relative to that listing, not independent identity with the original Zenodo ZIP.
- The archive contains exactly **282 pair files**, no other files, and 43,362,576 uncompressed pair bytes. Every paired member was read; ZIP CRC validation and NIfTI decoding completed. Frame indices are exactly 1 through 141. The series number in the names is 7.
- Each volume is 53 × 63 × 46, 3 mm isotropic, with a `uint16` on-disk payload and the same finite affine. Each of the 141 headers has the same SHA-256; each image payload has a different SHA-256. All scaled voxel values inspected are finite. This is file integrity/QC, not evidence of valid task design or artifact-free images.
- Frame 1 and frame 141 image/header hashes agree with the independently downloaded two-pair sample from the previous step. The full [machine-readable inventory](verification/roy_s09_scan1_full_fmri_inventory.json) contains per-frame checksums and aggregate QC, not images or original identifying filenames.
- The supplied EEG scan-1 file was separately retrieved and its SHA-256 matches the earlier EEG inspection. Its embedded MRI series number is also 7; this is a consistency check, not a unique mapping proof. The source files may include sensitive metadata, remain outside Git, and are subject to the [release's research/noncommercial terms](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1).

## 2. What the count discrepancy now means

The supplied fMRI archive contains **141** pairs. The release README describes **129** image pairs per EPI scan and recommends skipping five for steady-state analysis. The paper describes a *typical* first-level model with **121** volumes per run. The EEG scan-1 file contains **124** TR markers, spaced exactly 550 samples = 2.2 seconds at 250 Hz. These numbers describe potentially different representations and stages; their differences are not, on their own, evidence that the paper is wrong.

The arithmetic `141 − 12 = 129`, then `129 − 5 = 124`, is tempting, but it is **only one possible accounting hypothesis**. No original record has shown that 12 particular volumes were dropped, or that the 124 EEG markers match the final 124 MRI frames. Likewise the paper's 121-per-run description is typical, not verified as this participant's actual selection. Choosing a trimming rule by arithmetic would silently assume the very alignment to be established.

The retrieved 3D image headers and inspected EEG metadata do not provide an independently established one-to-one volume-to-trigger anchor. The EEG begins 10.864 seconds before its first stored TR marker; its first trial marker follows that TR marker by 1.132 seconds. These are **within-EEG** times, not times relative to MRI frame 1.

## 3. An exact conditional nonuniqueness gate

Assume, solely for this calculation, that all 141 image indices are in temporal order at 2.2-second spacing and that the 124 stored EEG TR markers correspond one-to-one to **consecutive** image frames with no internal omissions. Without an independent start anchor, the first EEG marker could correspond to frame **1, 2, …, or 18**: exactly `141 − 124 + 1 = 18` mathematical placements. This does not assert that all 18 are physically possible; uninspected acquisition records may rule out many or all of them. Nor does it rule out more complex mappings with missing triggers or removed images.

Under those same assumptions, the first trial marker could be positioned from **1.132 s** to **38.532 s** after MRI frame 1, depending on the placement. Thus the sampled files and marker counts alone do not justify a unique fMRI regressor. The [alignment witness](verification/roy_s09_scan1_alignment_gate.json) and [script](verification/roy_s09_scan1_alignment_gate.py) enumerate the alternatives; the synthetic test checks the count and boundary cases.

## 4. How much the offset can matter: a descriptive sensitivity calculation

For a concrete consequence, use the measured whole-field mean of each of the 141 volumes, including zero-valued background. For **each of the 18 assumed placements**, place five illustrative 42-second boxcars at the EEG trial markers, convolve with a fixed double-gamma response `Gamma(6,1) − Gamma(16,1)/6`, sample at 2.2 seconds and correlate the result with the volume means. Across these placements the observed Pearson correlations range from **−0.168 to +0.392**; four are negative and fourteen positive.

This deliberately simple diagnostic demonstrates *sensitivity to an unestablished offset*, not evidence for either sign. It is not the published model: no motion or drift regressors, prewhitening, event-specific reports, spatial ROI, multiplicity correction or inferential p-value are used. The entire 42-second block-onset interpretation is assumed, and the global field mean is not a direct physiological or phenomenal measure. The offset yielding the largest correlation was **not** selected as the real one. In particular, choosing an alignment because it produces the desired result would be circular.

The [sensitivity output](verification/roy_s09_scan1_offset_sensitivity.json) records all 18 values and assumptions, and [the code](verification/roy_s09_scan1_offset_sensitivity.py) is reproducible. A synthetic test checks known-signal correlation and failure for a constant series; it does not validate any real alignment or model.

## 5. Next boundary

A defensible EEG-informed fMRI analysis needs the S09 scan-condition/stimulus log and an **independent volume-to-EEG timing anchor**, or the authors' actual scan-1 SPM design, included volume list, nuisance regressors and preprocessing/drop history. A single 141-volume scan, without that information or independent participants, cannot replicate the group-level mid-cingulate contrast or identify the framework's report–experience error. If those records can be found in the supplied data, inspect them before fitting a condition-labeled GLM; do not guess the offset from the observed BOLD series.

## Reproduction

The raw scan-only ZIP and EEG file are not committed. With authorized local copies and `numpy==2.2.6`, `nibabel==5.3.2`, `scipy==1.15.3`:

```
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory.py /path/to/scan1.zip --expect-volumes 141
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate.py verification/roy_s09_scan1_full_fmri_inventory.json /path/to/S09_scan1_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity.py verification/roy_s09_scan1_full_fmri_inventory.json verification/roy_s09_scan1_alignment_gate.json /path/to/S09_scan1_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory_test.py
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate_test.py
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity_test.py
```

These are reproducibility and illustrative checks, not clinical or metaphysical conclusions. The NIfTI pair reader works sequentially and never commits the raw images or embedded DICOM fields. Cite [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024) as the release requests.
