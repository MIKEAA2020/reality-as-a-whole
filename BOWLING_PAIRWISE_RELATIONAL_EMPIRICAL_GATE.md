# An empirical gate for relational and pairwise musical predictions

## Question and verdict

The user's idea is that a relational form of alignment or conflict might matter for experience. Before attempting to associate neural frustration with discomfort, a useful empirical question is: **how much can simpler relations between the sounds already predict about listeners' ratings?**

I analyzed a small public aggregate dataset of actual consonance judgments from [Bowling, Purves and Gill (2018)](https://doi.org/10.1073/pnas.1713206115), using source tables pinned below. This is an exploratory secondary analysis, not a prospectively registered test, a replication in new listeners, a neural experiment, or the Marjieh et al. data. It assesses **musical attractiveness**, not physical pain or internal oscillator frustration.

Two simple candidate rules are made to agree exactly on the original two-note data: predict a larger chord's rating by either (i) averaging its constituent interval ratings or (ii) taking their minimum. Both show substantial descriptive correlation with the study's chord means, but neither reproduces the full data. Crucially, **two chords can have the same collection of symbolic pairwise intervals while receiving different average ratings**. Any rule depending only on that collection predicts them identically. This is a restriction on that particular stimulus representation, not evidence that all pairwise physical explanations fail.

The useful conceptual gain is a concrete **hierarchy of null models**: the experiential programme must beat—not rename—interval-only, context-aware psychoacoustic and other established predictors, and must separately identify internal interactions before invoking subject-internal frustration.

## 1. Data and provenance

Bowling et al. studied 30 people: 15 music students and 15 nonmusicians. They rated 12 dyads, 66 triads and 220 tetrads, each chord on a four-point consonance scale. The analysis table provides the **average** rating for each chord, not individual trials. The original [paper](https://www.pnas.org/doi/10.1073/pnas.1713206115) states that the stimuli used just intonation, a synthesized piano tone and approximately controlled average fundamental frequency.

We use the 298-row [DCMLab consonance table](https://github.com/DCMLab/consonance/tree/a13bcb0a52ac41cff9647e8b6406aed32a8250c6) (commit `a13bcb0a52ac41cff9647e8b6406aed32a8250c6`), and separately cross-match every relative pitch-class set and supplied rating to [Harrison's inconData transcription](https://github.com/pmcharrison/inconData/tree/b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe) (commit `b95b4db27356a04241ed1a2e38ffc8f5e1f68bbe`). All 298 match within `10⁻⁸`. DCMLab identifies inconData as a source, so this is a processing check on **shared provenance**, not two independent studies or a complete audit of the primary supplementary files.

Both tables, their providers' stated license metadata, hashes and attribution are recorded in [external source provenance](sources/external/README.md); the [verifier](verification/bowling_pairwise_transfer_audit.py) checks input hashes and the match. The files contain aggregate ratings and not listener identities. The two data providers supply symbolic interval representations, and the inconData tables also record frequencies and previously calculated harmonic-similarity scores. We have not inspected the original audio or participant-level responses.

The related [Marjieh et al. 2024](https://doi.org/10.1038/s41467-024-45812-z) experiment's own [OSF archive](https://osf.io/83w2b/) lists a 215.5 MB data ZIP and a 591.1 MB code ZIP, plus GitLab and a browser-based data explorer. We read the published data-availability statements and browsed repository listings; **we did not download or analyze those large archives**. The result below is Bowling's different experiment and must not be attributed to Marjieh's participants.

## 2. Direct transfer: two competing rules that agree on dyads

For each integer symbolic interval `d=1,…,12`, let `r_d` be that dyad's observed group-average rating in this dataset. For each triad or tetrad, list every unordered pair of notes and its semitone separation `d_ij`. Compute

```text
M_mean(chord) = mean over note pairs of r_(d_ij)
M_min(chord)  = min  over note pairs of r_(d_ij).
```

On every two-note chord both rules equal the dyad rating, by construction. So the two-note data alone do not choose between these two specified aggregation rules. For larger chords, the outputs are compared directly with the existing chord-level averages, with **no triad or tetrad coefficients fitted in the direct comparison**. We do not claim independence: the dyad and larger-chord averages come from the same study and listeners, and the source data were already available and inspected. The dyad ratings are behavioral inputs, not independently specified physical interaction forces. Integer pitch labels also discard real tuning, frequency, timbre and temporal-envelope information.

| Chords | n | Mean-of-dyads: correlation / RMSE | Minimum-dyad: correlation / RMSE |
|---|---:|---:|---:|
| Triads | 66 | 0.823 / 0.533 | 0.865 / 0.545 |
| Tetrads | 220 | 0.767 / 0.545 | 0.722 / 0.698 |

Correlations are Pearson's r across **chord-level means**, not across independent listeners. RMSE is in the original 1–4 rating-scale units. On triads the minimum has higher correlation but the mean has slightly lower direct RMSE; on tetrads the mean has both higher correlation and lower direct RMSE. These are descriptive results for the specified candidates, not evidence that either captures a feeling's physical constitution. Because larger chords are generally rated lower than the unadjusted mean rule predicts, calibration matters; choosing a metric or model after seeing results would bias selection.

To expose calibration sensitivity rather than hide it, we also fit a separate intercept and slope for each chord size, holding out **every chord with the same multiset of symbolic intervals** as the test chord. The group-held-out RMSE is 0.435/0.385 for mean/min on triads and 0.381/0.410 for tetrads. These calibrations use ratings of other chords of the **same size** from the same listener sample; they are not dyad-only prediction, participant-held-out validation or an external replication. Results and all descriptive metrics are in the [receipt](verification/bowling_pairwise_transfer_audit.json).

Pairwise interval models are not novel: [Hall, Tamir and Rohrmeier (2025)](https://doi.org/10.5334/tismir.243) already optimize and compare interval-based models on these and other datasets, citing earlier work. Our calculation is a narrower exploratory **dyad-agreement/aggregation and representation-collision gate**, not a superior model or priority claim. We did not run their optimized model here.

## 3. A concrete collision: same symbolic pairs, different ratings

Consider these two triads in the processed table:

| Symbolic pitches | Pairwise separations, semitones | Mean rating | Reported frequencies, Hz | Published harmonic-similarity score |
|---|---|---:|---|---:|
| 56, 58, 64 | 2, 6, 8 | 1.767 | 210.71, 237.05, 337.13 | 0.057 |
| 55, 61, 63 | 2, 6, 8 | 2.633 | 196.22, 274.71, 313.96 | 0.400 |

Their group means differ by approximately **0.867** on the 1–4 scale. A deterministic rule that takes only the *unordered multiset of integer semitone distances* as input must give the same prediction for both: it receives exactly the same input. This is a mathematical limitation of that representation for matching the two **observed means**; the example was selected after inspecting the data and no significance test is claimed.

It is **not** a controlled demonstration that the physical pairs are the same. The reported frequency ratios are approximately `(1.1250, 1.4222, 1.6000)` for the first and `(1.1429, 1.4000, 1.6000)` for the second. Register and just tuning differ, and complete sound spectra need not be equal. The supplied harmonic-similarity scores also differ markedly. They are an existing stimulus-based alternative worthy of assessment, not our independently calculated or validated explanation of this particular contrast. A pairwise physical model using exact frequency, register and spectral partials could distinguish these stimuli; so could some non-pairwise models. No inference to specifically neural or experiential holism follows.

### A finite-sample representation floor

Group all 66 triads by their multisets of integer pair distances: 36 groups result, 30 containing multiple chords. Even an **oracle** that sees all observed chord means and assigns each group its own best in-sample constant cannot reduce RMSE below `0.185` on these particular observed triad means; its residual sum of squares is `6.32%` of the total observed sum of squares around the overall mean. The analogous tetrad figures are 125 groups, RMSE `0.153` and `6.83%`.

This is an algebraic fit floor for this supplied finite table: using the group mean is optimal by squared-error minimization. The oracle uses the target values and **is not a predictive model**. Its floor includes rating noise and effects of tuning, register, timbre, listeners and context; it is not the fraction of experience that is irreducibly holistic, nor a population confidence bound. Individual participants rated multiple chords, so the chord rows should not be treated as independent people.

## 4. What this changes for the misalignment hypothesis

This result favors a **more demanding test**, not a different metaphysical starting point:

- **External acoustics versus internal organization:** an auditory interval, an acoustic roughness model, an internal phase-coupling model and felt unpleasantness are separate variables. Here only symbolic external notes and their reported attractiveness are available.
- **Predictive hierarchy:** first compare established pairwise and spectral models; then a prespecified internal-channel candidate must show added value under independently measured conditions. Its potential benefit cannot be inferred from a shortfall of an impoverished symbolic baseline. The existing [selective-channel gate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) specifies why the physical channel identification itself is difficult.
- **Avoid reverse inference:** an unexplained chord-rating gap is not evidence of neural frustration, fundamental strings, suffering, a novel subject boundary, or intrinsic experiential identity. Subject-internal F was not measured; neither was pain.
- **Preserve plurality and time constraints:** this concerns human local reports and does not posit one universal consciousness, an external creator, or an absolute clock. It leaves self-existence, global actuality and emergent physics open.

## 5. Next empirical decision

For auditory experience, a meaningful next comparison would need individual trial-level data, exact audio/spectra, listener and context information, and held-out listeners and timbre conditions. It should compare published roughness, harmonicity, familiarity and other appropriate models with independently specified neural predictors. The original 2024 timbre study and later models are relevant baselines; re-fitting the same group's ratings is not independent validation. Any attempt to identify preferred neural interaction offsets also needs data and interventions capable of supporting the [channel-identifiability conditions](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md). Those channels cannot be inferred from the Bowling table.

If available data lack these measurements, the result for the experiential-frustration conjecture is **not identified**. A new controlled experiment would require ethics review, consent and safe sound levels; nothing here recommends inducing pain. The core gap remains the link between a specified physical organization, its subject and its intrinsic felt quality.

## Reproduction

Run `python verification/bowling_pairwise_transfer_audit.py`. It requires only Python's standard library and the pinned source files already included. It checks the SHA-256 hashes, cross-matches all 298 source chord types and averages, computes the two direct and grouped-calibration results, and checks the multiset collision. The [JSON output](verification/bowling_pairwise_transfer_audit.json) contains exact inputs and results. This code does not perform population-level uncertainty inference or recreate the experiment.
