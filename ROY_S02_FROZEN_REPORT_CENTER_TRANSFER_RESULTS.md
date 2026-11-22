# S02 frozen report-center EEG transfer: results

## Bottom line

The six requested S02 EEG files were received and verified against the supplied Dropbox listing. The model trained on S01 and S09 was already fixed in [commit `d8f7645`](https://github.com/MIKEAA2020/reality-as-a-whole/commit/d8f7645), before these S02 files were supplied. It was applied without refitting or adjusting the procedure to S02.

**The S02 result is unfavorable for this candidate.** On clean centers with a known report, the EEG rule matched **42 of 736 mixed-report centers (5.7% recall)**. Of its 367 mixed predictions, **42 matched a mixed center (11.4% precision)**. Overall accuracy was **2,135/5,362 (39.8%)**, below the fixed S01/S09 majority baseline (**2,233/5,362; 41.6%**) and time-only baseline (**2,325/5,362; 43.4%**). Three-class macro recall was **32.2%**, versus **33.3%** and **33.8%** for the respective baselines. These are descriptive, temporally dependent observations from one new participant, not significance tests or a population estimate.

This target is the report code *at a center*, while each EEG feature covers two seconds around it. A mismatch with the center code is not proof of an absence of mixed experience within the EEG window, nor proof that reports measure experience without error. The finding challenges this particular simple frozen report-prediction candidate; it does not rule out other EEG methods, settle the existence or structure of experience, or identify a neural cause of a percept.

## 1. Inputs, provenance and checks

The supplied folder contained exactly the six requested scan files **1, 2, 4, 6, 8, 11**. Every file matched the size and Dropbox content hash independently listed by Dropbox, and its SHA-256 was recorded before the frozen runner opened any report or EEG values. The [integrity receipt](verification/roy_s02_dropbox_integrity_receipt.json) contains only sizes and hashes, not raw data or private links. These checks establish consistency with the **supplied Dropbox files**. The public [S02 ZIP](https://zenodo.org/records/5035511/files/S02.zip?download=1), published MD5 `02f9ab78531e9b9cc5093ed5e3abf767`, was not independently downloaded or checked, so authenticity against that archive has not been established.

The six rivalry conditions were fixed from the [pinned reanalysis condition list](https://github.com/Aubrey-Lyu/BR-project/blob/b8ca204024a4f7151645c6c2e908eb564203ac66/info_scans_conditions.m); this is not an independently verified acquisition log. Each file passed the runner's applicable schema checks: 250 Hz sampling, one POz channel, expected approximately 6.667/8.571 Hz tag frequencies, a binary artifact mask, five trial starts, non-overlapping assumed 42-second trial ranges, in-bounds trial data and no simultaneous report markers. Minimum trial-start spacing was approximately 53.97–54.00 seconds. These checks support code execution; they do not independently validate report onset, perceptual onset, eye assignment or the assumed carry-forward state reconstruction.

The raw MATs are in the ignored private `.arena/roy_s02_input/` cache, not published in Git; they may contain sensitive metadata. The source SHA-256 manifest was prepared *after* matching Dropbox's separate size and content-hash metadata and *before* analysis. The runner checked all six hashes before reading any EEG/report values. No user re-upload or author correspondence was needed.

## 2. Prespecified method and coverage

The [frozen development and S02 protocol](ROY_REPORT_CENTER_MIXED_STATE_DEVELOPMENT_AND_S02_PROTOCOL.md) describes the method and the weak pre-S02 development results. The runner verified hashes of the fixed model receipt and its analysis dependencies; the test runner itself is committed in `d8f7645` (SHA-256 `5e5bd8c4861f98d4aee1992c3691b44c3e028dc98b592c702d0340ad1436c817`). The fitted S01+S09 model, the 0.2-second center grid, two-second POz feature, label conventions, six scans and two baselines were not selected or tuned using S02 outcomes.

For each trial the fixed grid uses 201 centers from 1.0 to 41.0 seconds. Report state is unknown until the first code and then carried forward to the next event; a center is labeled from its exact report-code sample. The feature uses the two-second interval centered on that instant, including one second after it. A window with any artifact-marked sample is excluded from scoring. The model predicts for every clean center regardless of its target, but accuracy is computed only where the reconstructed report is known.

| Coverage category | Centers |
|---|---:|
| All 30 trials | 6,030 |
| Unknown report at center | 15 |
| Artifact in EEG window | 655 |
| Both unknown and artifact | 2 |
| **Known report and clean EEG** | **5,362** |

Thus 88.9% of the grid is scoreable under these rules. Adjacent two-second EEG windows overlap by 90%, so 5,362 centers are not 5,362 independent observations. Exclusion of artifact windows may also change which times and reports are represented.

## 3. Pooled confusion matrices and baselines

Rows are reconstructed center-report codes; columns are model predictions. Code 3 is the release's mixed report. Counts concern only the **5,362 known-report, clean centers**.

```text
EEG rule                  predicted 1    predicted 2    predicted 3
true code 1                    932           1294            167
true code 2                    914           1161            158
true mixed                     301            393             42

Frozen majority baseline  predicted 1    predicted 2    predicted 3
true code 1                      0           2393              0
true code 2                      0           2233              0
true mixed                       0            736              0

Frozen time-only baseline predicted 1    predicted 2    predicted 3
true code 1                    930           1463              0
true code 2                    838           1395              0
true mixed                     269            467              0
```

| Measure | EEG rule | S01/S09 majority | S01/S09 time-only |
|---|---:|---:|---:|
| Accuracy | 2,135/5,362 = 39.8% | 2,233/5,362 = 41.6% | 2,325/5,362 = 43.4% |
| Code 1 recall | 932/2,393 = 38.9% | 0/2,393 = 0% | 930/2,393 = 38.9% |
| Code 2 recall | 1,161/2,233 = 52.0% | 2,233/2,233 = 100% | 1,395/2,233 = 62.5% |
| Mixed recall | 42/736 = **5.7%** | 0/736 = 0% | 0/736 = 0% |
| Three-class macro recall | 32.2% | 33.3% | 33.8% |
| Mixed precision | 42/367 = **11.4%** | Undefined | Undefined |

Baseline mixed precision is undefined because neither baseline predicted mixed. The EEG model's 325 mixed predictions on nonmixed-labeled centers are mistakes relative to this **center-label** convention, not claims about all moments in those two-second windows. Among eligible centers, 736/5,362 (13.7%) had mixed center labels; that prevalence is descriptive context, not an independent probabilistic comparison. The EEG model correctly identified a few mixed centers while the fixed baselines identified none, but its low precision and recall, alongside worse overall accuracy and macro recall than both baselines, do not support it as a useful three-state detector on this participant.

## 4. Per-scan results and segment diagnostic

| Scan | Eligible centers | EEG correct | Majority correct | Time-only correct | EEG mixed recall |
|---|---:|---:|---:|---:|---:|
| 1 | 919 | 360 | 384 | 410 | 4/126 = 3.2% |
| 2 | 978 | 420 | 382 | 410 | 5/64 = 7.8% |
| 4 | 898 | 342 | 348 | 389 | 5/125 = 4.0% |
| 6 | 961 | 405 | 399 | 439 | 9/146 = 6.2% |
| 8 | 851 | 312 | 319 | 325 | 11/163 = 6.7% |
| 11 | 755 | 296 | 401 | 352 | 8/112 = 7.1% |

The individual confusion matrices and all coverage counts are in the [aggregate receipt](verification/roy_s02_frozen_center_transfer.json). Totals in this table and the pooled matrices were independently checked against the six per-scan receipts.

Under the prespecified segment diagnostic, **226 mixed-report segments had at least one eligible center**; the EEG rule predicted mixed at least once in 30/226 of them. The equal-segment mean fraction of eligible centers predicted mixed was **4.3%**. Segments without any eligible center are excluded; repeated and overlapping centers give longer segments more chances to produce at least one hit. These segment counts are not independent trials or a confidence interval.

## 5. What follows

The revised center target fixed the coverage problem—the S02 test included 736 eligible mixed centers—but not the detection problem. It reproduced the low single-digit mixed recall seen in the prior exploratory S01 and S09 comparisons and was below the baselines on aggregate accuracy and macro recall. Those prior comparisons trained on one development participant each, whereas this test used the two-participant pooled model; they are not identical experiments. No p-value or population confidence interval is claimed.

If pursuing this further, a new design should explicitly address report transitions, neighboring pure-state context, tag-signal reliability, artifact selection and timing uncertainty; select and evaluate it on a new held-out participant or, preferably, a separately planned multi-participant study. S02 is now examined and cannot be reused as an untouched test. Even strong report prediction would not by itself validate an experiential or subject-constitution bridge.

The [runner](verification/roy_s02_frozen_center_transfer.py), [fixed model/development receipt](verification/roy_report_center_development.json), [frozen results](verification/roy_s02_frozen_center_transfer.json) and [integrity receipt](verification/roy_s02_dropbox_integrity_receipt.json) are available. The S02 analysis was rerun with NumPy 2.2.6 and SciPy 1.15.3 and reproduced byte-for-byte; the prior synthetic tests passed. These software checks do not independently validate the labels, report timing, or private experience. Public-dataset use and citation remain subject to the [release](https://zenodo.org/records/5035511), including [Roy et al.](https://doi.org/10.1016/j.neuroimage.2017.02.041) and [Jamison et al.](https://doi.org/10.1016/j.jneumeth.2015.01.024).
