# A neural-signal deviation candidate against reported valence

## Result, with provenance warning

I tested a simple, independently defined **EEG-derived deviation** against a table that a third party says was extracted from the DREAMER experiment. In leave-one-person-out prediction on the same films, the training-film-mean baseline had RMSE **0.8627** and adding the deviation gave **0.8630**. The paired change in mean squared error was **+0.00049**, with a fixed-prediction participant-bootstrap interval **[−0.00603, +0.00731]**. This does not demonstrate an improvement.

This is a **provisional computation, not a verified analysis of original DREAMER data**. We have not obtained the original EEG or participant scores or independently confirmed the third-party table. Its source claims 23 people and 18 films and supplies the corresponding 414 rows. Matching the dimensions to the documented study is not a provenance check. The source's earlier project versions reportedly used synthetic labels, although its current README says this table contains real DREAMER self-reports; the original data are needed to verify that claim. We do **not** assert that its current table is synthetic. No individual rows or identifiers are redistributed here.

The tested deviation is a coarse power-spectrum statistic, not measured coupling frustration, not an optimal-state mismatch and not the user's full hypothesis. The negative result is useful for that narrow proxy and evaluation, but cannot settle whether some better-specified relational misalignment is the intrinsic aspect of discomfort.

The later [MET label and neural-access audit](MET_MUSIC_VALENCE_LABEL_AND_NEURAL_ACCESS_AUDIT.md) inspects an explicitly keyed newer dataset version and obtains retrospective stimulus-category baselines without EEG; it does not repair DREAMER provenance or establish MET signal usability.

## 1. What was measured and what was not

The original [DREAMER article](https://doi.org/10.1109/JBHI.2017.2688239), by Katsigiannis and Ramzan, describes EEG and ECG recorded while 23 participants watched audiovisual films and rated valence, arousal and dominance afterwards. Its PubMed abstract was read; the linked full article returned an HTTP 500, and we did not inspect the full paper, raw recordings or original labels. An independently hosted three-page [DREAMER data description](https://github.com/brainhack-school2020/Biosignal-Emotions-BHS-2020/blob/194885b5fcbd2e4ef20f1a14781cb9319329ae59/docs/DREAMER_info.pdf) was text-extracted and read: its `baseline` is recorded during a **neutral clip before each film**, not necessarily eyes-closed rest or a physiological ideal. We did not visually audit its PDF layout or establish that this particular secondary feature table was generated from that exact release.

The secondary [feature table and extraction code](https://github.com/VarunS05/eeg-ecg-emotion-recognition/tree/4f7da1a235e9f144928d648a4d7a6c541de6bf2b) describe Welch alpha-band power from 14 channels. According to the code, feature `a_i` is `log1p(stimulus alpha power) − log1p(baseline alpha power)`; this is **not** the ordinary log power ratio, and depends on input units. The source README describes a resting baseline; the original data description instead identifies the neutral-clip recording. We read the feature-extraction and table-building code, README and prediction script, but have not executed its extraction on the original signals, verified the cached file's history or independently assessed signal artifacts. No repository license was visible; data terms should be checked separately.

We define, before computing outcome relationships,

```text
q = sqrt(mean_i a_i²),       signed = mean_i a_i,     i = 1,…,14.
```

`q` is the magnitude of a change in **scalp spectral features** between a film and its preceding comparison clip. It is not an independently calibrated cost, normal operating set point, effective interaction energy, phase mismatch, neural frustration, or evidence that a neural state deviates from what it should be. It may include reference, eye movement, facial muscle, attention, arousal, stimulus and preprocessing effects. No interactions, preferred phase offsets, intrinsic subject, or phenomenal property are measured. The signed feature provides a simple existing-style power comparator; it is not an exhaustive neuroscientific baseline. The fitted proxy slopes are unrestricted, so this assesses prediction in either direction, not a prespecified law that increasing mismatch must increase discomfort.

## 2. Results with unseen people

The [retrospective analysis plan](EEG_BASELINE_DEVIATION_VALENCE_ANALYSIS_PLAN.md) fixed the definitions and tests after reading the secondary source and its previously published classifier results but before inspecting feature–valence relationships. It was not a prospective preregistration. The target is the purported 1–5 valence score treated numerically; RMSE and MAE are in those ordinal scale points.

For every held-out person, the models use only other people's rows. The film baseline takes each film's training-person mean; adding a proxy estimates one training-only common slope with film intercepts. It is a strong baseline for familiar film identities, but uses **other people's ratings**, not audio or visual features. It is not available for a genuinely new film and can predict consensus without accessing the tested individual's EEG.

| Model | RMSE | MAE |
|---|---:|---:|
| Overall training mean | 1.3211 | 1.1154 |
| Overall mean + deviation | 1.3174 | 1.1112 |
| Overall mean + signed alpha change | 1.3039 | 1.1025 |
| Film training-person mean | 0.8627 | 0.6853 |
| Film mean + deviation | 0.8630 | 0.6852 |
| Film mean + signed alpha change | 0.8623 | 0.6827 |

Deviation minus film-only mean squared error is +0.00049 [−0.00603, +0.00731]; deviation minus signed-feature model is +0.00121 [−0.00640, +0.00826]. Positive means the deviation model has higher error. These are bootstrap percentiles resampling participants **after** generating the fixed out-of-fold predictions; they do not propagate model fitting uncertainty or random selection of films. Overlapping training sets and a shared stimulus set further limit inference. The intervals crossing zero are not proof of equivalence, and the result does not compare to nonlinear, personalized or anatomically targeted models.

## 3. New people and new films together

To avoid giving the model film identity for films it has never seen, we also divide people into five fixed groups and films into three fixed groups. For each of 15 cells, the model is trained only on other people **and** other films and tested on that crossed held-out cell. Every row is tested once. This is a small, deterministic blocked cross-validation exercise, not an independent dataset or independent deployment. Film-ID means are unavailable in this setting.

| Model | RMSE | MAE |
|---|---:|---:|
| Overall training mean | 1.3629 | 1.1644 |
| Overall mean + deviation | 1.3568 | 1.1575 |
| Overall mean + signed alpha change | 1.3373 | 1.1410 |

Deviation minus overall-mean MSE is **−0.0164** [−0.0407, +0.0063], so the improvement over the weak mean baseline is uncertain by this conditional bootstrap. Deviation minus the signed-alpha model is **+0.0527** [+0.0094, +0.1010]. Because bootstrap resampling is only by person, not by both person and film, and fitting is not repeated, that interval does not support a general claim that one proxy is superior for new film populations. Both splits use the same 18 selected films, 23 claimed participants and same third-party preprocessing; no audio-based context model was evaluated in this double-disjoint test.

## 4. Implications for the framework

This is the first comparison in this thread to use purported neural features and purported self-reported valence from the **same participant–film records**, but the provenance is unverified. It connects a physical signal statistic with reports rather than assuming the reports are physical variables or rejecting first-person experience. It does **not** supply the independently justified internal coupling mismatch requested for the main proposal. It does not provide a new independent validation, neural intervention or account of the phenomenology. Existing EEG emotion-prediction work already compares neural and other features; the particular cross-validated test here is an exploratory project-specific baseline, not a novel derivation of an established EEG method.

The useful next step is to obtain an authorized original dataset with its preprocessing and timing, verify the labels and signals, and compute candidate interaction parameters from independent data rather than substitute synchrony or power for preferred coupling. Use preregistered inference, artifact checks, comparison to content and learned-expectation models, repeated subject/film separations and, ideally, interventions that discriminate the proposed dynamics. A fixed fundamental frustration alone remains constant for a fixed network, while changing state-deviation or coupling/boundary theories require their own independently identified quantities. First-person valence can constrain such hypotheses, but predictive success would still leave the question **why and for whom** a physical organization has the experienced quality. C3 remains **full structural and experiential intelligibility**, jointly with the other criteria; B4–B5 and B10 remain open.

## 5. Other candidate datasets and limitations

A subsequent [audit of Daly et al.'s music EEG dataset](DALY_MUSIC_EEG_AND_EVENT_ALIGNMENT_AUDIT.md) identifies individual trial-level pleasantness questions and existing EEG/acoustic comparators. Its accessible event metadata do not meet our conservative decoding rule; EEG and audio have not been inspected, so no neural reanalysis is claimed.

- [A closed-loop, music-based brain-computer interface for emotion mediation](https://doi.org/10.1371/journal.pone.0213516) and its [data repository](https://github.com/stefan-ehrlich/dataset-affective-music-BCI/tree/f0fb2790def68e74addfc3a787cb81cfc24951d9) contain actual downloadable EEG and mood files. We read the repository README, all text of its three-page BCI-study documentation, and the paper's abstract and selected methods/results via search snippets; we did not read the complete paper, inspect its figures, replay its model or validate all EEG. In its five-person BCI study, mood is assessed at the start of a session, not per feedback trial; online music depends on EEG. It therefore cannot simply provide independent contemporaneous trial-level valence labels for this gate. The separate listening study has ratings but is not the same as those five people's BCI trials.
- The [MET music-induced EEG dataset](https://github.com/OpenNeuroDatasets/ds008701/tree/e2613bff898998734e67a9abe4b431154f1c3ec2) describes music, 20 people and subjective ratings. We inspected the repository listing and README and a sample EEG entry, but the GitHub EEG entry is a DataLad symlink, not the underlying recording. The full EEG, timing and ratings were not analyzed. The [MET analysis repository](https://github.com/Koundinya2003/met-eeg-project-push) appeared in search, but the GitHub API returned 404; only its search snippet was read, and its claims could not be checked. These limitations are access limitations, not evidence that the datasets do not exist.

## 6. Reproduction

The [standard-library verifier](verification/eeg_baseline_deviation_valence_gate.py) checks the source hash, uniqueness and complete person–film grid, validates finite alpha values and all training/test separation, computes the predictions and writes an [aggregate receipt](verification/eeg_baseline_deviation_valence_gate.json). Its [unit tests](verification/eeg_baseline_deviation_valence_gate_test.py) check the fitting formulas. Obtain the table locally without publishing it:

```sh
mkdir -p .arena/dreamer
gh api -H 'Accept: application/vnd.github.raw+json' \
  'repos/VarunS05/eeg-ecg-emotion-recognition/contents/data/dreamer_features.csv?ref=4f7da1a235e9f144928d648a4d7a6c541de6bf2b' \
  > .arena/dreamer/dreamer_features.csv
python verification/eeg_baseline_deviation_valence_gate.py
python verification/eeg_baseline_deviation_valence_gate_test.py
```

The target labels, third-party preprocessing, data provenance and scientific assumptions are not validated by the script.
