# S09 scan 1: fMRI access and two-volume sample

## Status: not all files inspected

The user reports uploading **282 scan-1 files** to Dropbox and requested that all be read. This remains **unfinished**. The Dropbox connector exposes individual files but not a bulk-folder download or server-side ZIP creation. Reading the entire set individually would require hundreds of separate connector calls; in light of the user's budget constraint, that has not been done. Only **two `.hdr`/`.img` pairs—four files—were downloaded and inspected**. The 606.6 MB subject ZIP was not downloaded.

A sequential whole-series inspection program and synthetic regression have been prepared below. The practical next input is a ZIP containing only the scan-1 `.hdr` and `.img` files; based on the sampled sizes, if the reported 282 files are 141 such pairs, the uncompressed pair content would be approximately **43.36 MB**, under the connector's 100 MiB per-file limit. That size and pairing count have not been verified for the entire upload. Zipping them does not require putting patient data in the public Git repository. Once that ZIP is accessible, the prepared program reads every header and image in it and reports exact counts and missing frame numbers.

## 1. What was actually checked

Dropbox searches located a scan-1-series header and image for frame index 1 and another pair for frame index 141. They match the Dropbox-provided content hashes. The files are NIfTI-1 separate header/image pairs (`ni1`), each with a 348-byte header and a 307,188-byte image payload. Both inspected images are readable with NiBabel as finite-valued 3D volumes with shape **53 × 63 × 46**, `uint16` on-disk data and 3 mm isotropic voxel spacing. Both headers are byte-identical; both use the same finite affine. The payload size equals `53 × 63 × 46 × 2` bytes. The [machine-readable sample result](verification/roy_s09_scan1_two_volume_sample.json) contains checksums and aggregate voxel QC only, not original filenames, images, header strings or DICOM details.

In a separate local inspection of the previously supplied S09 EEG scan-1 MATLAB file, its embedded MRI metadata reported series number 7 and 2,200 ms repetition time. The two sampled fMRI filenames also carry series number 7. This is consistent with the user's scan-1 identification, **not independent confirmation of stimulus condition, temporal alignment or every file in the series**. The separate three-dimensional image header does not establish the complete time series or its start time. Potentially identifying fields in the MATLAB and image metadata have not been published; the raw files stay outside Git.

## 2. Volume-count issue: still open

The record describes 129 MRI image pairs per run after its stated preprocessing and the paper describes a typical GLM of 121 volumes; the scan-1 EEG file contains 124 TR markers. The observed existence of image indices 1 and 141 is a new fact, but **does not demonstrate that every intermediate index exists**, that the user-uploaded set consists only of those pairs, or how any images were retained in the authors' GLM. The sample JSON labels the 139 unexamined intervening indices as absent **from this two-pair sample**; that is not a claim they are absent from Dropbox.

If, as a hypothetical, all indices 1–141 represent consecutively timed 2.2-second acquisitions, the first-to-last onset span would be `140 × 2.2 = 308` seconds, compared with approximately 282.016 seconds spanned by scan-1 EEG samples. This is conditional on unverified index ordering, continuity and same-run correspondence. It does not establish which volumes overlap EEG or explain the published 121/129 numbers. Actual sample counts, first/last acquisition times, dropped-volume history, marker origin and authors' SPM design are required.

## 3. Prepared sequential whole-series audit

[The audit script](verification/roy_mri_pair_inventory.py) accepts a local directory or ZIP, requires complete `.hdr`/`.img` pairs, checks series and index consistency, reads each pair's entire bytes, validates 3D geometry and finite values, and emits non-identifying aggregate QC and checksums. It processes one volume at a time and does not extract archive paths supplied by a ZIP. It rejects unexpectedly large members and limits total pair bytes to 100 MiB. Passing it does not validate the scan condition, EEG/fMRI alignment, experimental timing, or a BOLD contrast.

The [synthetic regression](verification/roy_mri_pair_inventory_test.py) passed directory/ZIP equivalence, missing-index reporting and the stop on unpaired files. The script also completed the two-pair **real sample**. It has not been run on the user's full 282-file upload.

To process a scan-only ZIP after it is made available locally:

```
PYTHONPATH=/your/dependency/dir python verification/roy_mri_pair_inventory.py /path/to/scan1_fmri.zip
```

The dependencies used are `numpy==2.2.6` and `nibabel==5.3.2`. If the complete data really contain 141 pairs, `--expect-volumes 141` can enforce that count; do not set it as an assumed finding. The final output may contain source image hashes and aggregate voxel values, so review privacy and the [dataset's research/noncommercial terms](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) before publishing it. No individual images or embedded patient metadata should be committed.
