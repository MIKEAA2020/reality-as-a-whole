# Music-induced pleasantness and EEG: source and event-alignment audit

## Main finding

A potentially valuable dataset does contain recorded EEG and **individual reports of music-induced pleasantness**, but the accessible event files cannot yet be used safely for the planned EEG–report comparison by the simple decoder specified in our [audit plan](DALY_AFFECTIVE_MUSIC_EVENT_ALIGNMENT_AUDIT_PLAN.md). In all 1,240 music-onset intervals, question codes recur at multiple timestamps and at least one question timestamp lacks exactly one simultaneously recorded answer code. Under that deliberately strict decoder, **zero** intervals have a fully unambiguous eight-question mapping. This does **not** show that the original reports are invalid or missing: repeated display, keypress and answer markers may encode a perfectly recoverable sequence. It means we must establish the conversion and decoding conventions independently before fitting models.

The EEG recordings themselves are represented by git-annex symlinks in the accessible GitHub mirror; their content and the music audio were not obtained. Therefore this is a **metadata audit and reading of existing studies**, not a neural analysis or an independent replication. It does not test the proposed frustration or experiential-identity hypothesis.

## Dataset and design

Daly et al., [*Neural and physiological data from participants listening to affective music*](https://doi.org/10.1038/s41597-020-0507-6), describe the [film-music EEG dataset](https://doi.org/10.18112/openneuro.ds002721.v1.0.1): 31 participants, four experimental runs of ten clips, 19 EEG channels at 1,000 Hz, and eight questions after each 12-second excerpt. One question asks whether the music made the person feel pleasant; others include energetic, tense, angry, afraid, happy, sad and tender. Questions were randomized and used a 1–9 agreement scale. The source calls these reports of **felt**, not merely perceived, affect; the data do not directly identify phenomenal character independently of the report process. Audio features and known clip content are necessary comparators, not interchangeable with the participant's response.

The paper and original [*Neural correlates of emotional responses to music: an EEG study*](https://doi.org/10.1016/j.neulet.2014.05.003) state that the music lasted 12 seconds. The mirror's README says clips lasted 12 seconds but also describes 20-second EEG corresponding to a music clip. All 90,383 rows in the 124 inspected experimental event tables report duration `20` seconds, including question and artifact rows. These are **different descriptions of different things unless the conversion says otherwise**: the uniform event duration cannot be substituted for a 20-second continuous music stimulus. Define EEG windows from independently established recording markers and trial timing, not this column alone.

The mirror's `dataset_description.json` declares CC0; its README identifies the University of Reading as rights holder and declares CC BY 4.0. We have not resolved that discrepancy. The present report attributes and links the source and does not redistribute event records, audio, EEG or the two non-open-license articles. The [pinned GitHub mirror](https://github.com/OpenNeuroDatasets/ds002721/tree/c0b784f902bb3dc6bd674e27feba5693b0fb9506) is described as version 1.0.2 in its dataset description; the article cites 1.0.1. They must not be silently conflated.

## Fixed, conservative structural audit

We fixed the [rules](DALY_AFFECTIVE_MUSIC_EVENT_ALIGNMENT_AUDIT_PLAN.md) after inspecting the article, documentation, codebook and one run's event table, but before aggregate counts. This is **retrospective** and the counts describe structure, not a hypothesis test. The [code](verification/daly_affective_music_event_alignment.py) processes all participant event TSVs for runs 2–5; the [receipt](verification/daly_affective_music_event_alignment.json) contains aggregate counts and a hash of the input-file hash manifest, not participant-level data. The parser has [synthetic checks](verification/daly_affective_music_event_alignment_test.py). The run-2 codebook says `788` is music onset, `786` is fixation, codes `301–360` identify music files, `800–807` denote questions and `901–909` answers. Its descriptions for answer codes 902–909 all incorrectly say 'response of 1' while separately naming different response levels; we do not silently fix this documentation wording or decode the scores.

| Predeclared check | Aggregate result |
|---|---:|
| Participants / experimental run files | 31 / 124 |
| Files with ten `788` starts | 124 / 124 |
| Starts with a `786` in the previous 4 s | 1,240 / 1,240 |
| Starts with exactly one `301–360` code at identical onset | 27 / 1,240 |
| Starts with exactly one `301–360` code within ±0.1 s | 29 / 1,240 |
| Intervals containing all eight question codes at least once | 1,240 / 1,240 |
| Intervals with a repeated question code at different timestamps | 1,240 / 1,240 |
| Intervals where at least one question timestamp lacks exactly one same-time answer | 1,240 / 1,240 |
| Intervals containing an answer timestamp without a same-time question | 1,191 / 1,240 |
| Intervals meeting the complete strict eight-question rule | 0 / 1,240 |

All counts use event rows rather than raw EEG annotations. Identical `(onset, code)` rows were collapsed within the strict check; **112** such duplicates exist across the analyzed files. All event JSON files in this mirror share one byte hash. The counters are not mutually exclusive. Trial intervals start at each observed `788` and end before the next one, or at the run's last row for the final trial; an interval is not independently proven to match the trial's full psychological episode. In 90 intervals, a question or answer appears at exactly the music-start timestamp under this grouping, another reason not to use this partition as verified ground truth.

At 31 music starts an out-of-documented-range `361–399` code occurs at the exact onset, and at 38 a `401–499` code does. Their meaning is **unknown**, not assumed to be a song identity. The original EEG paper describes sampling from 110 excerpts, while the codebook names only 60 identifiers (`301–360`); the relation between that codebook and the full stimulus set requires investigation. The 27 and 29 exact/near coincidences are not proof of correctly matched identities, nor does the absence of such coincidences prove identity is absent. The events contain other possible timing relationships that this conservative audit intentionally does not decode.

## Already-published EEG and acoustic comparisons

The same study has already been analyzed, so any future use must cite rather than rediscover these results.

- In [Daly et al.'s EEG study](https://doi.org/10.1016/j.neulet.2014.05.003), eight ratings were summarized using PCA. PC1 correlates negatively with pleasantness and happiness and positively with fear and anger; its **sign orientation matters** and is not simply a raw pleasantness score. The authors examined frontal asymmetry and magnitude-squared EEG coherence, reporting selected associations. Spectral coherence is not independently measured preferred phase mismatch, and the study did not test the proposed experiential identity. Frequency bands were selected based on observed correlations, so the associations should not be presented as independent prespecified confirmation.
- In [*Music-induced emotions can be predicted from a combination of brain activity and acoustic features*](https://doi.org/10.1016/j.bandc.2015.08.003), the authors used 135 acoustic and 400 EEG features, outcome PCA and cross-fold model fitting. Their table reports mean predicted-versus-observed PC1 correlations of **0.243** for combined features, **0.202** for EEG and **0.028** for acoustic features, in their particular procedure. These are not subject-and-song-disjoint held-out results established here. The paper describes repeated random folds but does not clearly establish in the inspected methods that both subjects and songs are jointly separated or that response PCA is fitted within each training fold; do not claim either leakage or its absence without the code and a replay. The reported ANOVA across repeated random fold sets also does not by itself establish uncertainty for new participants or songs.
- Two source-internal details need caution. The 2014 paper states 360 excluded and 880 retained trials, but also calls the former 31.03%: 360/(360+880) is approximately **29.03%**. The later paper states 800 retained and 31.03% removed. The reasons for the different counts and denominator are not established by this reading; they may involve additional exclusions or reporting errors. The 2015 abstract states `r=0.234` and 'over 20%' of variance; `0.234²≈0.055`, and its table reports `r=0.243` for PC1. Squared correlation is not necessarily the model's held-out coefficient of determination, and we have not established what calculation underlies the abstract's percentage. Do not equate correlation with percent variance explained or silently reconcile these numbers.

These papers provide familiar, physically grounded baselines, not evidence for a unique experiential bridge. The data report is compatible with individual variation, stimulus effects and experience-respecting neural alternatives.

## Next gate and project implications

1. Recover the original EDF and acquisition/conversion records **selectively**, verify annotation codes and compare small hand-audited trial traces against raw samples and known 12-second music onsets. Independently reconcile question-display, answer and keypress markers and confirm which music IDs are mapped to the actual audio. If this cannot be done, keep the test blocked rather than filling gaps with inferred labels.
2. With verified data and rights, lock a subject/clip-disjoint analysis, channel-reference and filtering controls, artifacts, held-out PCA or a directly reported pleasantness endpoint, and models that compare stimulus acoustics, established frontal-power/coherence measures and a separately justified interaction-mismatch candidate. Correct for uncertainty over participants **and** music; the study is small. A temporal EEG feature from the same music period is still observational and may reflect stimulation, attention, movement or arousal.
3. A reproducible physical prediction, even across descriptions, cannot alone derive which subject feels what. Experience remains a valid datum; C3 is **full structural and experiential intelligibility**, jointly with C1–C7. B4–B5 and B10 remain open. A null result for one proxy would not refute experiential ground or all misalignment proposals.

## Reading and reproduction limits

- The full HTML text and captions of the [data descriptor](https://doi.org/10.1038/s41597-020-0507-6) were read; linked table pages, figure images, full datasets, stimulus files and supplementary code were not separately inspected.
- Complete extracted text of the 6-page [2014 EEG study](https://doi.org/10.1016/j.neulet.2014.05.003) and the 11-page [2015 prediction study](https://doi.org/10.1016/j.bandc.2015.08.003) was read from copies in a [third-party project repository](https://github.com/qiqing-li/neurotech-berkeley-fa20-nmep-proj/tree/89106a639da93c47ec0b8cb64f8e3ea5284b9abd). The 2014 page 3 and 2015 pages 1 and 5 were visually checked for the numerical issues; the other graphical figures, supplements, original model code, raw recordings and analysis outputs were not independently inspected. These repository copies have publisher copyright notices; their authorization was not verified, so they are not tracked here.
- The pinned OpenNeuro mirror's README, dataset descriptor, all event TSVs for the four experimental runs, and one event-code JSON were inspected programmatically. EEG files are annex links, and original event conversion code and source logs were not validated.

Reproduce the aggregate metadata audit (standard library plus `curl` and `tar`):

```sh
mkdir -p .arena/daly
curl -LfsS https://codeload.github.com/OpenNeuroDatasets/ds002721/tar.gz/c0b784f902bb3dc6bd674e27feba5693b0fb9506 \
  -o .arena/daly/events.tar.gz
tar -xzf .arena/daly/events.tar.gz -C .arena/daly
python verification/daly_affective_music_event_alignment_test.py
python verification/daly_affective_music_event_alignment.py
```

The script's codebook-based test does not verify the original acquisition or permissions. It is a deliberately limited screening procedure, not a published decoding standard.
