# S09 scans 7–9: complete fMRI inspection and six-scan timing comparison

## Findings

All three supplied ZIPs were downloaded and **every member read**. Each contains **258 files: 129 complete MRI header/image pairs**, consecutively indexed 1–129, with no extra members or gaps in that observed range. The separately downloaded EEG files have 126, 124 and 125 stored TR markers, respectively. Each matching EEG/MRI pair has the same embedded MRI series number, but that does not establish which EEG trigger corresponds to which MRI volume.

Together with the previously inspected scan-1, scan-2 and scan-3 ZIPs, this gives **798 MRI volumes / 1,596 pair files across six scans**. Scans 4–6 MRI archives are not included in this six-scan count; their EEG files were inspected previously.

| S09 scan | MRI volumes | Stored EEG TR markers | Conditional first-trigger MRI frame candidates* | First trial after MRI frame 1 under those candidates |
| --- | ---: | ---: | --- | --- |
| 1 | 141 | 124 | 1–18 | 1.132–38.532 s |
| 2 | 141 | 124 | 1–18 | 1.220–38.620 s |
| 3 | 129 | 127 | 1–3 | 7.220–11.620 s |
| 7 | 129 | 126 | 1–4 | 6.680–13.280 s |
| 8 | 129 | 124 | 1–6 | 2.572–13.572 s |
| 9 | 129 | 125 | 1–5 | 4.556–13.356 s |

\*The enumerations assume chronological MRI frame order at 2.2 s intervals and a consecutive one-to-one mapping of every stored EEG marker to MRI volumes. These assumptions are **not verified**; missing triggers, deleted/reordered images or other preprocessing could invalidate the enumeration. The list is not a count of proven physically feasible alignments. The measured marker spacing is 550 EEG samples at 250 Hz for each scan. The [machine-readable six-scan summary](verification/roy_s09_six_scan_mri_summary.json) and individual gate files contain the candidates.

The [release README](https://zenodo.org/records/5035511/files/rivalry-eeg-fmri-upload-readme-20170225.pdf?download=1) describes 129 MRI pairs per scan and recommends excluding five for steady-state analysis. Four of these six supplied MRI archives match the 129 count, but their EEG trigger counts differ (127, 126, 124 and 125). Thus **129−5 = 124 cannot by itself be a universal explanation of the stored trigger counts or a proof of their mapping**. Scans 1 and 2 still have 141 pairs; why remains undetermined. Neither a flawed study nor a missing user upload follows from these counts. An original volume-selection/design file, acquisition/preprocessing records or independent frame-to-trigger anchor is needed. The full S09 source archive has not been independently matched to these extracted ZIPs, and the Dropbox search was not exhaustive.

## Provenance and inspection

| Scan ZIP | Bytes | SHA-256 | Dropbox content hash |
| --- | ---: | --- | --- |
| 7 | 28,436,144 | `a55d428ec87370404c034df7b32e6973e0cb5b233cceb9af300c5d580fe94c7a` | `b9ce76f08c690d63a7ff01dc999edb65d3b79e2be5540b5571c0ef996fc70972` |
| 8 | 28,439,522 | `ef194410c38ec8de1ca43e3ffbef6bacb3756869bd102da10338ce5b280adad4` | `971236455995ecd50e171fbe9c860005b95586d64a7b10c322111b7591125328` |
| 9 | 28,433,761 | `83b655c4203b6f1d03962734ac684bda6bfb61c4f0fe09f4de25f06248f88878` | `e05672ca72f15d55cd684112702b5cf27fff3b8b19cad7d1712db6653ffe2c21` |

All three computed Dropbox content hashes match the metadata of the supplied Dropbox objects. They verify transfer, not identity against the original Zenodo subject archive. The freshly retrieved EEG files' SHA-256 hashes match the earlier EEG inspection outputs. ZIP CRC and NIfTI decoding passed for every member. All three MRI series have finite 53 × 63 × 46 `uint16` volumes, 3 mm isotropic spacing and the same affine; each series has one shared header hash and 129 distinct image payload hashes. Series numbers are 16, 17 and 18 for scans 7, 8 and 9, respectively, matching the corresponding EEG metadata.

There are **no shared image payload hashes between any two of the six inspected MRI series**. That excludes byte-identical image payloads across the series, but does not establish experimental, physiological or statistical independence. The series checks are file QC, not a check of motion, task validity or timing.

- Scan 7: [inventory](verification/roy_s09_scan7_full_fmri_inventory.json), [alignment gate](verification/roy_s09_scan7_alignment_gate.json), [sensitivity](verification/roy_s09_scan7_offset_sensitivity.json).
- Scan 8: [inventory](verification/roy_s09_scan8_full_fmri_inventory.json), [alignment gate](verification/roy_s09_scan8_alignment_gate.json), [sensitivity](verification/roy_s09_scan8_offset_sensitivity.json).
- Scan 9: [inventory](verification/roy_s09_scan9_full_fmri_inventory.json), [alignment gate](verification/roy_s09_scan9_alignment_gate.json), [sensitivity](verification/roy_s09_scan9_offset_sensitivity.json).
- Previous: [scans 1 and 2](ROY_S09_SCAN2_ALL_FMRI_VOLUMES_AND_COMPARISON.md), [scan 3 and mismatch audit](ROY_S09_SCAN3_AND_TRIGGER_MISMATCH_AUDIT.md).

## Exploratory sensitivity, not an fMRI result

For continuity with the earlier QC, whole-field image means, including background, were correlated with five assumed 42-second boxcars convolved with a fixed double-gamma HRF at each candidate offset. The descriptive Pearson r ranges are **−0.148 to −0.131** for scan 7, **+0.062 to +0.161** for scan 8, and **−0.063 to +0.037** for scan 9. The sign for scan 9 changes under the conditional offsets. This is not a fitted condition contrast: there is no drift or motion correction, serial-noise model, independent inference, established scan-condition mapping or validated alignment. Do not choose an offset by its correlation. These numbers cannot establish a neural correlate of experience or reproduce the study's group GLM.

## Reproduction and safeguards

Using authorized local files and `numpy==2.2.6`, `nibabel==5.3.2`, `scipy==1.15.3`, substitute `N` with 7, 8 or 9:

```sh
PYTHONPATH=/your/deps python verification/roy_mri_pair_inventory.py /path/to/scanN.zip --expect-volumes 129
PYTHONPATH=/your/deps python verification/roy_s09_scan1_alignment_gate.py verification/roy_s09_scanN_full_fmri_inventory.json /path/to/S09_scanN_filtered_gac_cbc.mat
PYTHONPATH=/your/deps python verification/roy_s09_scan1_offset_sensitivity.py verification/roy_s09_scanN_full_fmri_inventory.json verification/roy_s09_scanN_alignment_gate.json /path/to/S09_scanN_filtered_gac_cbc.mat
python verification/roy_s09_mri_multi_scan_summary.py 1 2 3 7 8 9
PYTHONPATH=/your/deps python verification/roy_s09_mri_multi_scan_summary_test.py
```

The historical `scan1` script names do not restrict their explicit scan inputs. Synthetic regressions test code paths and consistency, not true temporal alignment. The raw MRI and EEG remain outside Git because their metadata may contain identifying information. The [data release](https://zenodo.org/records/5035511) specifies research/noncommercial use and requests citation of [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024). These are six scans from one participant, not population replication or experience calibration.
