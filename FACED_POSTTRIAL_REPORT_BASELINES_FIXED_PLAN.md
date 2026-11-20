# Fixed plan: post-video self-report provenance and baselines

## Question and scope

Can an accessible, bounded source improve the target construct over pre-listening song preferences, and how well can **stimulus information alone** predict the resulting post-trial valence reports? This is a readiness and baseline study, not an EEG study. It is exploratory and not externally preregistered. The paper, GitHub README, conversion script and subject 000's event/sidecar structural sample have been inspected before this plan; no other participant event table has been inspected. The paper's already-published aggregate effects and stimulus-validation results are not blinded.

Source: [FACED paper](https://doi.org/10.1038/s41597-023-02650-w) and [NEMAR conversion](https://github.com/nemarDatasets/nm000112/tree/2577b0bbc089b49e828cd98d80445133634b6d34). Participants watched the same 28 videos, reporting 12 subjective items after each; valence is 0 very negative to 7 very positive. Reports summarize the video experience retrospectively; they are not continuous measurements and do not directly identify frustration. The converter says it joins each `After_remark.vid` with video markers to make BIDS events. We have not verified original MATLAB ratings, event files, synchronization or EEG.

## Bounded access and eligibility

Fetch only the pinned GitHub **metadata archive**, not annexed BDF objects. The GitHub tree reports ~2.2 MB of Git blobs in total; cap the compressed archive at 12 MB. Inspect all 123 events TSV and EEG JSON sidecars plus the conversion code and dataset description. Verify archive membership by paths and SHA-256 for receipt; use GitHub's tree object IDs and git-blob hashes to verify each input. Never execute the source repository code. The archive carries symlink pointers, not BDF data. Do not fetch any raw recordings or videos in this screen.

Each subject's eligible event must have video_index in 1–28, one positive-duration, finite, within-recording span for each index without temporal overlap, and finite 0–7 valence. Separately require one consistent emotion category and intended positive/negative/neutral label per video. Fail closed on duplicate or malformed rows, and document missing data instead of imputing. Extract and report `sample`/`onset` timing inconsistencies and `Manufacturer` in JSON vs. paper's hardware description; these are provenance checks, not proof of synchronization. Exclude missing rows only as specified; if a subject has duplicate video indexes, out-of-range rating, missing timing or overlaps, stop before analysis rather than selecting convenient rows. If no complete cases exist, stop. Verify whether the converted table's ratings and original movie-level means agree with independent original data if those original inputs can be accessed, otherwise explicitly leave conversion verification open.

## Fixed comparison

On eligible rows, report counts and per-video dispersion of reported valence. A video has one target label but many independent reports: compare within-video across-person spread with across-video spread, without claiming that variation is measurement error. Report the average of per-video population SDs and the average per-video valence; these are descriptive, not independent observations for statistical testing.

Predict **the continuous self-reported valence**, not the predefined video category. Use fixed nested-free baselines, with training means only, MAE and RMSE on held-out rows:

1. Grand mean of training outcomes.
2. Intended three-way stimulus valence label mean (positive, neutral, negative), falling back to grand mean if missing.
3. For known-video only: video-specific training mean, falling back to grand mean if missing.

(A) Split subjects by numeric subject ID modulo 5: train on other people, test on held-out people, same videos; report all held-out rows once. (B) For a harder crossed split, split people as above, and divide videos **within each intended category** into three folds by sorted video index cycling 0,1,2. For each of 15 subject-fold/video-fold pairs, fit only rows from non-held-out subjects AND non-held-out videos; test their intersection. Aggregate exactly once per subject/video pair. This guarantees no held-out person's or video's outcomes used in its training; only predefined intended category is available for new video. It is a partitioned descriptive test on this fixed set of clips and participants, not an independent replication, and overlapping training folds prevent treating the 15 folds as independent. Report sample sizes and missing-category fallback counts.

Stimulus-label baselines use experimental design information and do not demonstrate causal affect, neural signal, physical frustration or an experiential identity law. These results are not comparable directly to the paper's EEG classification accuracy (different target, splits, metrics); they provide minimum comparators for any future EEG model on the same rows.

## Implementation and tests

Use Python standard library only; store summary counts, aggregate metrics, input hashes and exact source commit, not individual ratings. Unit-test no training subject/video leakage in crossed splits, each eligible observation exactly once, category fallback, true MAE/RMSE and detection of duplicates/overlap. If any fixed schema gate fails, make no silent schema or analysis change; report the failure. Reproducibility is conditional on the source GitHub archive and repository metadata still being obtainable.

**Implementation cap amendment:** The first run stopped at subject 029 because an implementation-only 100,000-byte individual input guard was smaller than four event files in the already-downloaded, bounded archive; the largest is 131,003 bytes. No full-dataset result was produced. We raised that safety cap to 200,000 bytes, still a bounded limit; no eligibility rule, outcome or model changed. Other data/schema failures will still stop the analysis.

**Supplementary cross-check:** After the first complete baseline run, the original paper's [supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fs41597-023-02650-w/MediaObjects/41597_2023_2650_MOESM1_ESM.docx) became readable as text. Its published 28 two-decimal video-mean valence values were added to the code for the planned original-source aggregate cross-check, with a 0.005 tolerance reflecting two-decimal rounding. They were not used to fit, choose, or alter the original baselines. This is an aggregate consistency check using a publication based on the same source study, not independent participant-level validation.
