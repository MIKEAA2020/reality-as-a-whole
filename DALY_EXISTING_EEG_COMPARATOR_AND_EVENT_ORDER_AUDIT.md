# Music EEG comparator: timing and event-order audit

## Result and relevance

An independent [public music-cognition EEG pipeline](https://github.com/xinlinwang970-lab/music-cognition-eeg-pipeline-ongoing-/tree/634fa01848731ad2d5c88f6b3483b48dc9ba8725) reports that frontal beta power did not show a stable association with pleasantness in the Daly film-music dataset. This is potentially relevant existing work, but **its reported near-zero association is not yet a dependable listening-only comparator for our proposal**. On inspection of the released code and the event metadata:

1. It requests a 20-second EEG feature window from each music marker. The data descriptor specifies 12-second music clips. In **all 1,240 music-onset intervals**, at least one code documented as a question occurs between 16.501 and 16.601 seconds after the marker, hence inside the requested 20-second window. A question marker's presence is not itself proof of its real display time or of a neural artifact; it creates a **specific timing and construct-contamination risk** that requires checking against raw EEG/acquisition records. All requested windows are not proven to have been available in full, because the pipeline clips to EDF boundaries and the recordings were not obtained.
2. Its parser's outputs change markedly when rows with identical timestamps are reversed, even though event times and event-code multisets are unchanged. With the recorded NumPy/pandas versions, **815 of 1,240 trial intervals** change at least one of the three parsed ratings. The alternate tie order is not proven to be correct; the finding is that reliable labels cannot be inferred from event timing alone using this order-sensitive rule without validating original conversion/order semantics.
3. The event metadata contains conflicting-looking `901–909` and `833–841` code families at many same-time question markers. They may have different acquisition meanings; treating either as the correct score without checking the source would be speculation.

This is an exploratory metadata and source-code analysis. **We have not downloaded or replayed the EEG, obtained the author's trial outputs, or recomputed the published correlation.** These findings do not show that the reported association is necessarily wrong, that the target variable has no useful relation to beta, or that the original study's analyses used this pipeline. They identify actionable problems in this particular third-party comparator before its null result is imported into our framework assessment.

## Provenance and experiment

Daly et al., [*Neural and physiological data from participants listening to affective music*](https://doi.org/10.1038/s41597-020-0507-6), describe 31 participants, four music runs of ten trials, 12-second film-music clips, a 0.5-second pause and eight randomized felt-affect questions. See the [earlier detailed audit](DALY_MUSIC_EEG_AND_EVENT_ALIGNMENT_AUDIT.md) for codebook inconsistencies, original published analyses and licensing uncertainty. The question asks whether the music made the listener *feel pleasant*, which is a relevant experiential report but not a direct measurement of a proposed physical–phenomenal identity.

The independent pipeline pins `ds002721` version 1.0.3 and reports 1,240 trial rows and 31 subject-level results. Its [methods](https://github.com/xinlinwang970-lab/music-cognition-eeg-pipeline-ongoing-/blob/634fa01848731ad2d5c88f6b3483b48dc9ba8725/docs/METHODS.md) describe a 15–30 Hz frontal beta log-power feature, one value per trial and within-subject Spearman correlations. Its [summary](https://github.com/xinlinwang970-lab/music-cognition-eeg-pipeline-ongoing-/blob/634fa01848731ad2d5c88f6b3483b48dc9ba8725/docs/RESULTS_SUMMARY.md) reports mean pleasantness/Fz rho **−0.0027** and a bootstrap interval **[−0.0556, 0.0545]**, conditional on that pipeline and its processing. These numbers are **author-reported, not reproduced**, and a small average correlation is not evidence of absence of every neural–affective association. This comparator was intended for transport from engagement, not as a direct test of independently identified interaction frustration.

We downloaded only the small public git-metadata archive at [v1.0.3 commit `3972f19`](https://github.com/OpenNeuroDatasets/ds002721/tree/3972f19d2846be4f283fe21c7fe39a1a11efda99) and the upstream code and documents, not any raw EDF. All 248 run-2–5 event TSV/JSON blobs have the same Git blob hashes as the previously audited v1.0.2 commit `c0b784f`; we independently verified the 124 TSV byte-manifest SHA-256 is `c026a6bee732bf4eea5e8b60ba2a03d526e05a49b2b2b72ec87df1fbc44c22e7`. This is equality of the **event files**, not proof that all EEG files or other materials in the two versions are equal.

## 1. A listening-window check, not an artifact diagnosis

The upstream parser uses event code `788` as onset and takes its `duration` field as the trial duration. The extraction code requests `[onset,onset+duration)`, clips to EDF boundaries, discards clips with less than 10 seconds, and calculates Welch power from the remaining samples. All 1,240 music-onset rows contain `duration=20`; earlier work established that this value appears on every event type, not just music.

Using half-open marker windows and the codebook's question codes `800–807` and answer/response codes `901–909` and `833–841`, the pinned metadata yield:

| Marker screen | Onsets, out of 1,240 |
|---|---:|
| A question marker in `[0,12)` seconds | 0 |
| A question marker in `[0,20)` seconds | 1,240 |
| Answer/response marker in `[0,12)` | 271 |
| Answer/response marker in `(0,12)` | 189 |
| Answer/response marker in `[0,20)` | 1,092 |
| Answer/response marker in `(0,20)` | 1,051 |
| Next music-onset marker strictly before 20 seconds | 0 |

The first **strictly positive** question-marker offset has minimum/median/maximum **16.501 / 16.501 / 16.601 seconds**. The first positive answer/response marker has minimum/median/maximum **0.076 / 16.601 / 41.241 seconds**. Unlike question markers, answer/response markers sometimes occur at or very close to the music start, and our grouping does not show what these refer to. No claim that they are correctly assigned to the current trial or reflect an actual response in the listening period is justified.

If event timing and code meanings accurately reflect the recording, the 20-second window includes post-music and question-period signals, not just music listening. But the descriptor's stated 12-second clip, the codebook, and the converted events still require alignment to the EEG and original task logs. A proposed 12-second window cannot be declared verified merely because this count is zero: filter boundary effects, non-question artifacts, uncertainty in onset, reference and actual playback must also be checked. Missing marks, timing lag and participant response can affect the interpretation. The pipeline itself already acknowledges no full artifact rejection and practical alignment choices; the counts here quantify additional specific risks.

## 2. The label parser depends on ordering equal timestamps

The upstream code sorts by onset, identifies a `800–807` question row, and searches **only subsequent rows in that order** until a *different* question code for `901–909` answers; if none is found, it uses `833–841` response codes. These code families often share timestamps with question markers. A sort by timestamp alone does not establish a physical before/after relationship between same-time codes. The source order might nevertheless encode a convention: that is precisely what needs independent verification.

We executed the exact pinned upstream `TrialSpec` and `parse_events` definitions against all 124 event tables. For the stress test only, the rows at each exactly equal timestamp were reversed before the source's own sort; no time or code was changed. We matched NumPy `2.4.3` and pandas `3.0.1`, as recorded in the pipeline's summary, but used Python `3.11.2` on this platform rather than its reported Python `3.14.3` on Windows. This is not a replay of the original environment or result. The counts below describe **our local execution**, including original-order processing:

| Target | Nonmissing, original order | Changed after tie reversal | Of changes, two different numeric values | Of changes, one missing |
|---|---:|---:|---:|---:|
| Pleasantness | 1,171 | 478 | 409 | 69 |
| Energy | 1,175 | 457 | 392 | 65 |
| Tension | 1,179 | 450 | 389 | 61 |

At least one target changes in 815 intervals; the three change counts overlap. This does not tell us the true labels or numerical effect on an EEG correlation. It does show that temporal coincidence, row order, and fallback behavior have consequences. A synthetic unit test also exhibits one unchanged timestamp group whose pleasantness changes from 4 to missing when the tied rows are reordered.

### Why the fallback is not self-validating

Among unique co-timestamp groups strictly after a music onset and before the next, after identical code duplicates are collapsed, **2,785** groups contain exactly one question code, one `901–909` code, and one `833–841` code. Under the literal numeric mappings `answer−900` and `response−832`, **710** groups agree and **2,075** differ, spanning **597** onset intervals with at least one disagreement. This does not prove either family is wrong or that both are intended to refer to the same answer; the data conversion and original acquisition could attach distinct semantics. It does preclude justifying their unconditional interchangeability from these metadata alone. The codebook's 902–909 descriptions also repeat the wording 'response of 1', despite distinct level labels.

## 3. Stimulus identity is another independent bottleneck

The same parser chooses the latest `300–699` marker at the start or in the preceding 10 seconds; if absent it creates a participant/run/trial-specific fallback. In our original-order execution it assigns **201** intervals a numeric code in the documented `301–360` music range, **856** an outside-range number still between `300–699`, and **183** a fallback. All 1,240 receive some identifier, but the latter two categories do not establish a shared stimulus identity from the inspected codebook. Whether outside-range numbers encode the remaining music excerpts, other event classes, or some mixture requires original acquisition/conversion evidence. None of the IDs changed in the tie-reversal test; this does **not** validate them.

The pipeline uses its IDs to calculate leave-one-subject-out stimulus group ratings. Subject-specific fallback IDs cannot by themselves match a stimulus across different people, and numeric labels are meaningful only if independently validated. Its within-subject primary correlation does not use the stimulus grouping, so this concern should not be conflated with the question/answer and timing problems.

## 4. What is needed before using the comparison

1. **Validate the recording timeline.** Retrieve a bounded EEG run and raw annotations, original presentation or conversion records, and, where lawful, the corresponding stimulus. Check `788` against true playback; distinguish listening, pause, question and response. Compare a prespecified verified listening-only window against the existing 20-second window and report artifact/reference sensitivity. Raw file existence and signal validity remain unverified here.
2. **Validate label semantics.** Reconstruct a few complete trials against original questionnaire logs or another independently supported source. Treat exact-timestamp codes as groups until source semantics justify an ordering; independently explain both response families. Demonstrate agreement and report ambiguities before evaluating all trials. Do not treat our reverse-order output as the correction.
3. **Validate clip IDs.** Recover the documented mapping for codes outside 301–360 and test cross-person identity. Exclude unresolved IDs from stimulus-group comparisons rather than assuming a participant-specific fallback matches someone else's clip. Report all exclusions.
4. **Recompute on the same retained trials.** Compare the reported frontal beta model to stimulus/context baselines and to a separately specified relational statistic, with properly grouped person and clip splits for the intended generalization. A scalar phase index remains descriptive unless channel preferences are independently identified, as shown in the [phase-lag gate](OBSERVED_PHASE_LAGS_VERSUS_PHYSICAL_FRUSTRATION_GATE.md). These are not independent tests merely because the code runs, and the small sample limits uncertainty estimates.
5. **Keep the bridge separate.** A valid report association can constrain competing physical models but does not establish the qualitative identity, subject boundary or intrinsic nature of an experience. First-person experience remains a valid datum; C3 is **full structural and experiential intelligibility**, jointly with C1–C7. B4–B5 and B10 remain open, and no general negative conclusion about experiential ground or misalignment follows.

## Reproduction

The [fixed audit plan](DALY_EXISTING_EEG_COMPARATOR_AUDIT_PLAN.md) was written after prior aggregate audit results, source reading and a one-file preview but before the counts above; it is not a prospective preregistration. The [script](verification/daly_comparator_metadata_audit.py) verifies the event-file manifest and source hash, extracts only the two upstream parser definitions with Python AST, and saves aggregate counts in the [receipt](verification/daly_comparator_metadata_audit.json). The [tests](verification/daly_comparator_metadata_audit_test.py) exercise window boundaries, duplicate collapse, missing values and a synthetic order-sensitive upstream parse. Upstream code is fetched at a fixed commit and verified by SHA-256; do not use this AST execution with arbitrary untrusted source. The Python parser test is skipped if the source has not been fetched.

```sh
mkdir -p .arena/daly103 .arena/music-pipeline
curl -LfsS https://codeload.github.com/OpenNeuroDatasets/ds002721/tar.gz/3972f19d2846be4f283fe21c7fe39a1a11efda99 -o .arena/daly103/events.tar.gz
tar -xzf .arena/daly103/events.tar.gz -C .arena/daly103
gh api 'repos/xinlinwang970-lab/music-cognition-eeg-pipeline-ongoing-/contents/run_ds002721_v2_0.py?ref=634fa01848731ad2d5c88f6b3483b48dc9ba8725' --jq .content | base64 -d > .arena/music-pipeline/run_ds002721_v2_0.py
python -m pip install --target .arena/daly-py 'numpy==2.4.3' 'pandas==3.0.1'
PYTHONPATH=.arena/daly-py python -m unittest discover -s verification -p 'daly_comparator_metadata_audit_test.py' -v
PYTHONPATH=.arena/daly-py python verification/daly_comparator_metadata_audit.py
```

## Scope of reading and access

- [Pipeline README](https://github.com/xinlinwang970-lab/music-cognition-eeg-pipeline-ongoing-/tree/634fa01848731ad2d5c88f6b3483b48dc9ba8725), methods, datasets, limitations, results summary, configuration, feature helper and relevant parser/extraction sections were inspected. Its other scripts, figures, individual EEG features, neural outputs, NMED-E data and complete end-to-end computation were **not** independently inspected or reproduced. No external party's conclusions are corrected silently.
- Daly's [data descriptor](https://doi.org/10.1038/s41597-020-0507-6) HTML prose and captions were previously read; figure images, table pages, original EEG, stimulus audio and original conversion code were not. The [2014 EEG study](https://doi.org/10.1016/j.neulet.2014.05.003) and [2015 EEG/acoustic prediction study](https://doi.org/10.1016/j.bandc.2015.08.003) were read as extracted text with selected pages checked, not all figure images, supplements, source data or model code. They are not the third-party analysis audited here.
- Kaneshiro et al., [*Inter-subject correlation of electroencephalographic and behavioural responses reflects time-varying engagement with natural music*](https://doi.org/10.1111/ejn.16324), the NMED-E study referenced by the pipeline, was consulted only at its opening/abstract and search excerpts; its full text, figures and data were not inspected this turn. Its continuous engagement endpoint is not the same as a post-trial felt-pleasantness rating.
- MET [OpenNeuro dataset v1.0.6](https://doi.org/10.18112/openneuro.ds008701.v1.0.6) EEG remains unavailable through the GitHub mirror as actual bytes. The platform's outbound host restrictions prevent direct OpenNeuro/NEMAR/S3 retrieval here; a direct OpenNeuro connection failed. No large download was attempted. Its ratings-only analysis is in the [MET audit](MET_MUSIC_VALENCE_LABEL_AND_NEURAL_ACCESS_AUDIT.md).
