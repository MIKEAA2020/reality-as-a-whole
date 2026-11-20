# Music valence reports: a keyed dataset and held-out baselines

## Main result

The [MET music-induced EEG dataset](https://doi.org/10.18112/openneuro.ds008701.v1.0.6) offers a more promising alignment interface than the undecoded Daly event files: the pinned table directly keys each reported valence rating to a participant and a song, and all 400 distinct keys have valid 1–9 valence entries. The pinned GitHub tree has matching EEG **paths** for 399 of those keys; all are Git-annex links, and the remaining key has a missing-EEG remark. This is not confirmation that the linked signals are accessible, correctly aligned, usable, or correspond to the intended windows. No EEG samples or stimulus audio were obtained or analyzed.

A fixed-before-full-table-inspection [label-only screen](MET_MUSIC_RATINGS_AND_ALIGNMENT_FIXED_PLAN.md) found that a song's intended affective category predicts reported valence better than a grand mean, including when the test song and person are excluded from the training set. This is an important baseline for a future neural mismatch test, **not evidence for the experiential-misalignment hypothesis**. The dataset calls this a post-listening *self-reported valence*; the exact SAM instructions, including whether participants were explicitly asked about felt versus perceived music emotion, were not available in the inspected metadata. Do not silently equate valence, pleasure, enjoyment, liking, or instantaneous experience.

## 1. Source, interface and provenance

Cheang's [dataset version 1.0.6](https://doi.org/10.18112/openneuro.ds008701.v1.0.6) was inspected via the [pinned public GitHub mirror](https://github.com/OpenNeuroDatasets/ds008701/tree/e2613bff898998734e67a9abe4b431154f1c3ec2). It differs from the earlier version 1.0.3 discussed in the [EEG baseline audit](EEG_BASELINE_DEVIATION_AND_VALENCE_GATE.md); no assertion is made that the signal contents or metadata are unchanged across versions. The version 1.0.6 descriptor says CC0. The README describes 20 people, 20 songs per person, randomized presentation, 120-second listening bracketed by five seconds, and 66 selected EEG channels after preprocessing. It advises an illustrative conservative music window of 6–124 seconds. Treat those timings as **reported design**, not a validated signal alignment.

The [ratings dictionary at the pinned commit](https://github.com/OpenNeuroDatasets/ds008701/blob/e2613bff898998734e67a9abe4b431154f1c3ec2/ratings.json) says valence and arousal are 1–9, and liking and familiarity 1–5, with zero for missing values. Song categories are intended stimulus labels: high/low valence and arousal, plus neutral. The [ratings table](https://github.com/OpenNeuroDatasets/ds008701/blob/e2613bff898998734e67a9abe4b431154f1c3ec2/ratings.tsv) is a plain Git blob, SHA-256 `830c854fa33aff943a6a9c36b343f7d81cf6b01da6b4ed67ff1057831c27cc59`. We did not redistribute the individual table here; the deterministic receipt records aggregate counts and metrics.

Reading one event-file example, `sub-01/ses-t01`, revealed only `bad` event entries rather than an explicitly labeled stimulus-onset trigger. That one sidecar reports 1,000 Hz, 66 EEG channels and approximately 131 seconds, but `EEGReference` is `n/a`; the README specifies Cz as the **online acquisition reference**. This does not establish the reference after preprocessing. The sample event file cannot verify the original stimulus onset, audio timing, final processing reference, or timing of a subject's rating. All 399 EEG file symlinks have not been dereferenced or inspected. Presentation-order information has not been verified, and a filename's nominal session/song label must be validated against the EEG and source records before using it as ground truth.

## 2. Label and path check

The plan was written after seeing the README, dictionary, tree and a truncated partial table preview, but before reading the full table or scores. This is a transparent retrospective screen, **not external preregistration**. The [script](verification/met_label_alignment_screen.py) checks the pinned hash, unique keys, numeric ranges and intended categories; three [synthetic tests](verification/met_label_alignment_screen_test.py) cover missing/range parsing, cross-disjoint splits and baseline arithmetic. The [receipt](verification/met_label_alignment_screen.json) gives exact outputs.

| Check | Result |
|---|---:|
| Unique participant–song rows with valid valence | 400 |
| Participants / distinct songs | 20 / 20 |
| Valid valence rows per participant / per song | 20 / 20 |
| Missing liking / missing familiarity | 1 / 1 |
| Missing valence / arousal | 0 / 0 |
| EEG paths matching rating keys | 399 / 400 |
| Matching EEG paths represented by annex symlinks | 399 / 399 |
| Rows marked missing EEG | 1 |

The one missing EEG remark corresponds to the one unmatched key. These counts concern file paths, not verified physiological data. The missing liking and familiarity scores share a `0 = data missing` remark, but their valence and arousal remain in range. Whether those two ratings should be excluded from a later particular neural analysis is a separate eligibility decision. The script stops on duplicate keys, inconsistent categories per song, malformed IDs, unexpected categories or invalid nonmissing numeric ratings. In this version all 20 song categories are internally consistent across participant rows; this checks labeling consistency, not whether the intended categories are correct or assigned independently of responses.

## 3. The non-neural prediction hurdle

For every valid target row, both the mean and squared error are evaluated over the 400 participant–song outcomes. Every prediction uses training ratings only. Person-held-out models use the other 19 people; the joint holdout also removes **every training row for the test song**. The per-row models share most training data, so the 400 errors are not independent and the table has no confidence intervals or hypothesis test.

| Evaluation | Model | MAE | RMSE |
|---|---|---:|---:|
| New person, known songs | grand mean | 1.75301 | 2.14778 |
| New person, known songs | intended-category mean | 1.32375 | 1.66737 |
| New person, known songs | song mean from other listeners | 1.27842 | 1.59705 |
| New person **and** new song | grand mean | 1.80219 | 2.20187 |
| New person **and** new song | intended-category mean from other songs | 1.38746 | 1.73973 |

No baseline required a missing-category or missing-song fallback. The category comparator uses song metadata, not EEG or music acoustics. Its joint-holdout RMSE is lower than the grand-mean RMSE by about **0.462** rating points in this retrospective sample. We have not quantified uncertainty over new people and new songs, and the groups of songs are small. The category is only usable for genuinely novel music when supplied independently at deployment. The song mean is a valid familiar-song comparator but unavailable for a truly new song. Numeric losses on ordinal scores are useful descriptive benchmarks under an equal-spacing convention, not claims of equal phenomenal intervals.

These five values **cannot** be fairly compared to a later neural model unless the same labels, EEG-eligible rows, folds, target direction and preprocessing are used. Because the baseline includes all 400 labels, it is not the analysis subset for the at-most-399 paths with EEG. Nor does the exercise establish causality: intended categories, musical acoustics and listener reactions can covary. Existing literature on subject-level leakage supports grouping repeated EEG segments by person for a new-person claim; see Brookshire et al., [*Data leakage in deep learning studies of translational EEG*](https://doi.org/10.3389/fnins.2024.1373515), abstract and introduction only. A person-disjoint split does not by itself test a new-song claim. This audit's crossed condition addresses a different target than familiar-song prediction.

## 4. Related music EEG evidence—not a replication

A search preview describes Aditya Koundinya's [*The Song or the Self? A preregistered search for personal musical emotion in scalp EEG*](https://github.com/Koundinya2003/met-eeg-project-push), an independent analysis of MET v1.0.4 that reports person/song decompositions and no support for three specified alpha-band hypotheses. The repository returned HTTP 404 to both the GitHub API and direct page fetch in this environment; only search snippets were accessible. Another [profile preview](https://github.com/Koundinya2003/Koundinya2003) reports different numerical coefficients from the project preview. Their relationship and versions are unverified. Thus we report **no authoritative numerical result**, have not inspected its preregistration, paper, code, derived data or EEG, and cannot confirm the timing or adequacy of the claimed preregistration. Its design is relevant prior work, not a dataset or analysis we have reproduced. Neither a null alpha result nor its opposite would establish that all possible physical mismatch measures fail.

A second dataset, MUSIN-G, has a particularly direct song **enjoyment** question and EEG; its [data descriptor](https://doi.org/10.1016/j.dib.2022.108663) describes 20 listeners and 12 songs. Its scale runs **1 = most enjoyable** to **5 = least enjoyable**, the reverse of a common intuitive ordering. The [OpenNeuro v1.0.2 README](https://openneuro.org/datasets/ds003774/versions/1.0.2) explicitly warns that segmented event timelines are inherited from raw data and must be ignored. The [pinned GitHub mirror](https://github.com/OpenNeuroDatasets/ds003774/tree/fb2a9d7ceb7b215fab7be510cd45cf9b8d7470a7) exposes the behavior and EEG through annex links, not directly as the table and signals; neither was obtained here. Its descriptor says individual ratings exist and gives song/participant presentation order, but its example tables also describe baseline durations inconsistently: the procedure says two minutes while Table 2 says 12 seconds. Do not reconstruct timing from those descriptions without checking the original recordings and conversion.

Singla et al.'s [*EEG-Based Prediction of Music Enjoyment Using Deep Learning with Explainable Temporal Analysis*](https://arxiv.org/abs/2610.20795) reports a participant-wise 15/5 MUSIN-G split and song-level ratings copied to two-second EEG windows. It reports 0.97–0.99 MAE for three models, and a 0.21 correlation for another. The paper's own table uses the same songs across participants, and it does not demonstrate joint person/song holdout. The reported p = 0.056 is not below the conventional 0.05 threshold; the paper's description of it as strong evidence should not be treated as validation. A song-level score assigned to all two-second windows is not a moment-by-moment affect rating: saliency of a model trained on those labels does not establish when enjoyment rose or fell. We did not obtain the code or rerun its models; its reported metrics concern **a different dataset, endpoint and split** and cannot be compared numerically to our table.

## 5. Next admissible step

To move beyond label screening without reinventing existing EEG work:

1. Obtain a bounded sample of the pinned dataset's actual EEG and independently examine the file headers, reference, segment endpoints, artifact handling and claimed song key. Inspect the actual questionnaire and source processing/annotation where available. If sample access remains blocked, treat timing and EEG applicability as unresolved.
2. Define a physical mismatch feature from neural relationships and a separately justified reference or preferred coupling **without using held-out valence labels**. Channel powers, correlations and phase estimates are not by themselves a measured local preferred phase, tension, or phenomenal identity. Prespecify any baseline, reference sensitivity and artifact controls.
3. Compare category, acoustic, familiarity and established neural predictors with that feature on the **same qualifying participant–song trials**, including the simple category and known-song baselines above. Separate post-trial familiarity from information available during listening. Keep the whole song's correlated EEG windows in one fold and use an evaluation matching the intended deployment, including person-and-song disjointness where claimed. Account for uncertainty over both people and songs and acknowledge limited sample size.
4. A successful result would support at most the specified report-prediction association and its transport domain; the user’s experience is a valid datum, but reported valence is not an independently established identity with a physical feature. **Full structural and experiential intelligibility** remains C3, jointly with C1–C7. B4–B5, B10 and the broader battery remain open.

## Reproduction and access limits

With `gh`, Python 3 and GitHub access, fetch only the pinned public metadata and run the standard-library verifier:

```sh
mkdir -p .arena/met
gh api 'repos/OpenNeuroDatasets/ds008701/contents/ratings.tsv?ref=e2613bff898998734e67a9abe4b431154f1c3ec2' --jq .content | base64 -d > .arena/met/ratings.tsv
gh api 'repos/OpenNeuroDatasets/ds008701/git/trees/e2613bff898998734e67a9abe4b431154f1c3ec2?recursive=1' > .arena/met/tree.json
python verification/met_label_alignment_screen_test.py
python verification/met_label_alignment_screen.py
```

The full MET table, metadata README/dictionary, GitHub tree, and one EEG sidecar/event pair were inspected; signals, music audio, exact SAM questionnaire, preprocessing code and original acquisition logs were not. Koundinya's named project above was accessible **only as search previews**, not as a full paper or code. The full HTML text and captions of Miyapuram et al.'s [MUSIN-G descriptor](https://doi.org/10.1016/j.dib.2022.108663) were read, but its figure image, original behavioral tables, EEG, audio and cited beat-frequency paper [*Predicting Dominant Beat Frequency from Brain Responses While Listening to Music*](https://doi.org/10.1109/BIBM52615.2021.9669750) were not inspected. The full HTML text and captions of Singla et al.'s [MUSIN-G preprint](https://arxiv.org/abs/2610.20795) were read; its figure images, code, model outputs and data were not inspected. Brookshire et al.'s [*Data leakage in deep learning studies of translational EEG*](https://doi.org/10.3389/fnins.2024.1373515) was read only in its abstract/introduction, not its full study or figures. The information above is not an independent replication of those external studies.
