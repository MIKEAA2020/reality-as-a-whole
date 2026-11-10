# S09: public condition labels and motion regressors

## What the new sources resolve

The user supplied the original dataset README and the Roy paper, and pointed to [Lyu's reanalysis repository](https://github.com/Aubrey-Lyu/BR-project/tree/b8ca204024a4f7151645c6c2e908eb564203ac66). This was a useful lead: **the README does document S09's scan-type order**, and the reanalysis provides S09 motion files. My prior statement that no scan-condition mapping had been verified was too cautious about what was in the README: I had relied on a text extraction that misplaced headings. The attached PDF's actual page-2 layout resolves that particular extraction problem.

| S09 scan | README condition | MRI volumes | Public motion rows × columns |
| --- | --- | ---: | --- |
| 1 | Rivalry | 141 | 141 × 6 |
| 2 | Rivalry | 141 | 141 × 6 |
| 3 | Rivalry | 129 | 129 × 6 |
| 4 | Smooth replay | 129 | 129 × 6 |
| 5 | Rivalry | 129 | 129 × 6 |
| 6 | Smooth replay | 129 | 129 × 6 |
| 7 | Rivalry | 129 | 129 × 6 |
| 8 | Instantaneous replay | 129 | 129 × 6 |
| 9 | Instantaneous replay | 129 | 129 × 6 |

The labels are stated in the S09 block on page 2 of the attached README, and reproduced in the pinned [condition script](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m) and the accompanying rivalry/smooth index `.mat` files. Lyu's [GLM script](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/Analysis-2_fMRI/BR_GLM1_bhv_activation.m) builds sessions in numerical scan order and uses those indices in its rivalry and smooth-replay contrast vectors. Agreement is useful corroboration of the documented mapping, **not an independent check of the actual stimulus/acquisition records**: the code may have copied the README. Trial-level eye assignments and replay lineage remain unverified. In particular, scans 4 and 6 are *both documented as smooth replay*; their earlier post-hoc similar report-timing pattern does not establish whether they replay the same source trial.

The two attachments were read locally. The three-page README SHA-256 is `119e6f1de2089b305ce5a28a98b4f7dc0f9a9fba9c75a4413c896188c56a8003`; the 37-page Roy PDF SHA-256 is `2f6c115f2e3b0ce6b8396981b8f2c6674e9d9d994943754decb09321be98548c`. The Roy PDF states a *typical* first-level GLM with 121 volumes per run (page 17), not an actual S09 included-volume list. The PDFs and image-bearing data are not copied into this public repository.

## Motion: concrete progress, not yet a valid nuisance model

I fetched all **nine** S09 text motion files and their nine mask `.mat` files, selected from the [pinned motion tree](https://github.com/Aubrey-Lyu/BR-project/tree/b8ca204024a4f7151645c6c2e908eb564203ac66/data/rivalry_fMRI_head_motion_files/S09). All 18 downloaded Git blobs match the pinned tree's Git SHA-1 and reported sizes. Each motion matrix has six finite numeric columns and exactly as many rows as the corresponding supplied MRI inventory. The series number in each motion filename matches the respective MRI/EEG series number, and its filename identifies first frame 1. The adjacent `mask` arrays have matching lengths and contain all ones; their coding and treatment must be checked before interpreting those ones as keep, discard, or absence of motion. The [machine-readable audit](verification/roy_s09_public_support_audit.json) records hashes and dimensions without publishing raw motion series or original filenames.

These checks are **strong consistency evidence** that these are useful S09 motion resources. They do not prove that row *i* is the particular supplied image frame *i*, settle preprocessing transformations, establish censor semantics, or give an EEG-to-image origin. Do not simply add these regressors to an EEG-informed GLM until their frame correspondence, conventions and any trimming are checked. The reanalysis is [Lyu et al., 2022](https://doi.org/10.1038/s41467-022-34410-6), not Roy's original 2017 GLM, and the two analyses cannot be treated as identical.

## Timing and implementation audit

The user is right that `latency_trial`, `latency_tr` and report times inside the EEG files are directly useful: they fix event timing **relative to the EEG recording**. They do not, by themselves, specify which processed MRI volume is simultaneous with an EEG marker. The new per-run motion row counts match MRI counts, not EEG marker counts, so they do not supply that missing temporal anchor. The conditional candidate offsets remain as described in the [nine-scan inventory](ROY_S09_NINE_FMRI_SCANS_AND_STRUCTURAL.md).

The pinned reanalysis GLM code loads behavioral `time_trial` and `time_tr` files, selects motion per scan, and uses run-specific regressors. It warns when `time_tr` length is not 129, but this is not a proof of an EEG/MRI offset. In that script a comment says to discard the first five scans, yet the immediately following active line constructs a list of **all selected files**, without a `6:end` slice; another section that would drop the first **11** native images and corresponding motion/CSF/WM entries is **commented out**. We have not executed the original script or inspected its actual input selections or generated SPM designs. Therefore neither comment establishes the correct trimming for our files, nor the original Roy GLM. Use an independently recorded anchor rather than choosing a trim by arithmetic or model fit.

The full original `S09.zip` was **not inspected internally**: the accessible Dropbox connector rejected that 606 MB archive under its 100 MiB per-file limit, and the extracted MRI ZIPs contain only their image pairs. A recursive scan of the pinned *reanalysis Git tree* found no `SPM.mat` or separate `time_tr`/`time_trial` MAT files, but says nothing about the contents of the full Dryad subject ZIP or what the authors hold. The user's suggested archive inspection remains worthwhile if a private file manifest or the extra non-image files can be supplied; don't assume that the raw archive contains or lacks any particular log.

## What can already be analyzed

The documented labels permit a **post-hoc, descriptive** regrouping of the report-coverage summaries already computed from the nine EEG files. The same assumed five 42-second trial windows and carry-forward report convention are used; unknown before the first response and code-3 mixed reports are treated as unresolved for a binary coverage measure.

| Documented condition | Scans | Trial seconds | Unknown + mixed | Fraction of trial time |
| --- | --- | ---: | ---: | ---: |
| Rivalry | 1, 2, 3, 5, 7 | 1,050 | 245.932 s | 23.422% |
| Smooth replay | 4, 6 | 420 | 84.248 s | 20.059% |
| Instantaneous replay | 8, 9 | 420 | 22.476 s | 5.351% |

This [calculation](verification/roy_s09_condition_coverage.json) is not a prespecified contrast, decoder error, evidence that mixed percepts are wrong, group-level finding, or causal effect of condition. It concerns one participant, with few potentially dependent runs and different stimuli/report demands. No p-value or population conclusion is justified. EEG/report-based work can continue without an MRI anchor, but the report–experience error remains independently unknown.

## Reproduction and next decision

The bounded [fetch helper](verification/roy_s09_fetch_public_support.py) uses `gh` to download the pinned repository tree and only 21 selected small support blobs into a **private cache** (the tree can contain identifying-looking filenames). The [audit](verification/roy_s09_public_support_audit.py) uses the locally supplied README PDF, the existing nine-scan aggregate and the cache; [condition coverage](verification/roy_s09_condition_coverage.py) uses already committed safe aggregates. With `numpy==2.2.6`, `scipy==1.15.3`, `pymupdf==1.26.7`:

```sh
python verification/roy_s09_fetch_public_support.py /private/cache/roy_support
PYTHONPATH=/your/deps python verification/roy_s09_public_support_audit.py /path/to/readme.pdf /private/cache/roy_support verification/roy_s09_nine_scan_mri_summary.json /private/cache/roy_support/tree.json /private/cache/roy_support/motion
python verification/roy_s09_condition_coverage.py
PYTHONPATH=/your/deps python verification/roy_s09_public_support_audit_test.py
python verification/roy_s09_fetch_public_support_test.py
python verification/roy_s09_condition_coverage_test.py
```

Tests cover synthetic labels, PDF layout, dimensions, Git blob handling and coverage arithmetic, not actual acquisition truth. **Next:** inspect an S09 ZIP manifest or any non-image extras if available; request an explicit volume-to-EEG anchor, actual preprocessing/GLM volume selections and replay lineage if absent. In parallel, a frozen single-person EEG/report feasibility analysis can use the documented labels, with care for the 4/6 replay similarity and no claim of independent held-out participants. MRI-based contrasts should wait for the anchor and motion-row correspondence; broader population/experience claims require independent participants and a separately justified report-to-experience bound.
