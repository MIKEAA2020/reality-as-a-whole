# Pleasantness, preceding context and neural harmonicity

## Finding

The proposed link between misalignment and discomfort needs a **subject-internal**, independently measured physical quantity. Two complementary sources now narrow what such a candidate must accommodate:

1. In an existing chord-sequence experiment, participants rated the **pleasantness** of the final chord, not merely its consonance. The final scored chord was held fixed within each musical key while the preceding chord varied. Our participant-paired retrospective reanalysis of 49 people finds a mean high-minus-low modeled-familiarity-category difference of **+0.536** on the 1–7 rating scale, with participant-bootstrap 95% interval **[0.421, 0.658]**. The published study already found this kind of effect; this is not independent replication or a new discovery of contextual influence.
2. In a separate established neural study, a measured frequency-following-response harmonicity index was associated with consonance preference across 19 people, but the reported association was much weaker after adjustment for musical experience. This is a real physiological lead, **not** a measurement of our proposed mismatch or a demonstration of experiential identity.

Together they rule against treating the external final chord alone as a complete predictor of these ratings, and identify a concrete existing neural comparator for a richer model. They do not distinguish lived final-chord pleasure from an appraisal of the whole preceding sequence, as the first study's authors themselves warn. They do not resolve C3, **full structural and experiential intelligibility**, or B4–B5/B10.

## 1. Fixed final chord: analysis and constraints

Arthurs, Lahdelma and Eerola, [*The influence of consonance–dissonance contrasts on perceived pleasantness of concluding tonic chords in short chord sequences*](https://doi.org/10.1177/03057356251405848), studied 56 five-chord sequences. Within each of seven keys the sequence was I–vi–IV–[one of eight different chords]–I; the participants were instructed to rate the final chord from 1 (very unpleasant) to 7 (very pleasant). The sequences' presentation order was randomized. The authors' principal result and reported roughness-by-familiarity interaction predate our analysis. We read the article's abstract, introduction, methods, results, discussion, conclusion and figure captions in HTML, plus the source README and R Markdown. We did not inspect the two figure images, original audio, preregistration (if any), individual participants' session histories or all software dependencies. We did not verify that the final audio waveform was bit-identical or free of lingering effects from the prior chord; **the final scored tonic was fixed within key according to the published design**, not independently waveform-matched.

The [fixed retrospective plan](PLEASANTNESS_FIXED_FINAL_CHORD_PLAN.md) was written after seeing the paper, code and variable layout, but before calculating these summaries. It is not prospective registration. From the public SPSS input at pinned repository commit `010777ada95da0044492d14865a162d7bc2874f8`, 56 rows lacked required data and were excluded; the remaining 2,744 ratings form complete 56-question blocks for 49 people. The code validates stimulus-table/question mapping, category codes and ranges. We include the two participants with undisclosed gender; the source R Markdown's principal mixed model filters them out, so this is **not** a replay of that mixed model. Participant data and identifiers are not redistributed; the [receipt](verification/pleasantness_final_chord_context_gate.json) is aggregate only.

The eight penultimate chords were classified by **modeled** roughness (R) and corpus-derived familiarity (F), not by ratings of individual familiarity. The four cells each average two selected chord types across seven keys:

| Prior chord category | Final-chord pleasantness mean |
|---|---:|
| Low R, low F | 5.207 |
| Low R, high F | 5.497 |
| High R, low F | 4.835 |
| High R, high F | 5.618 |

Equal-person contrasts, resampling whole participants 10,000 times:

| Contrast, high − low | Mean | 95% percentile interval |
|---|---:|---:|
| Familiarity category, averaged over roughness categories | +0.536 | [0.421, 0.658] |
| Roughness category, averaged over familiarity categories | −0.125 | [−0.232, −0.026] |
| Roughness category, within low familiarity | −0.372 | [−0.555, −0.200] |
| Roughness category, within high familiarity | +0.121 | [+0.019, +0.226] |

The category contrast reverses direction across the two familiarity groups; this is consistent with the **already published interaction**, not evidence for an independently isolated causal reversal of roughness. Chord identity, relative pitch content, harmonic function, voice leading, modeled familiarity and modeled roughness co-vary: only the choice of prior chord sequence was experimentally varied, not roughness or familiarity in isolation. Treating the rating scale as numerical is a modeling choice. The intervals assume independent participants and reflect sampling uncertainty conditional on these particular selected sequences; they are not confidence statements for the universe of music. Selection after publication and multiple contrasts further limit inference.

A deliberately impoverished model allows an arbitrary fitted score for every person–key pair, but demands the same prediction for the eight preceding-chord contexts. Its optimal in-sample RMSE is **0.962** rating points, or **55.1%** of total sample sum of squares around the grand mean. This oracle uses all target ratings to select its constants. The bound includes ordinary noise and trial-order effects; it is not a held-out error, a population effect-size bound or a lower bound on phenomenal differences. Across-person stimulus means show a within-key context RMSE of **0.436**, which still contains sampling noise. The more direct paired contrast above supplies the stronger descriptive evidence against a zero group difference, under its assumptions.

A candidate that computes internal state from prior input, memory, expectations or other contexts is **not** a final-stimulus-only model and is not refuted here. Conversely, a vague appeal to internal history does not explain what the state is or why it has its felt quality. The observed pattern is informative about the experimental task, not about fundamental string vibrations.

## 2. A real neural measurement already exists

Bones, Hopkins, Krishnan and Plack, [*Phase locked neural activity in the human brainstem predicts preference for musical consonance*](https://doi.org/10.1016/j.neuropsychologia.2014.03.011), examined pleasantness of two-note chords and scalp frequency-following responses (FFRs). They compared presentation of both notes to both ears with separating notes between ears. In their pipeline the harmonic sieve was selected from each stimulus spectrum and then applied to the recorded FFR; a neural consonance index (NCI) was the difference in salience for designated consonant versus dissonant intervals. This is an **existing neural harmonicity measure**, not the framework's frustration F, not a free fit to each participant's pleasantness labels, and not a direct recording of phenomenal quality.

The paper reports 32 people tested behaviorally, four excluded as preference-score outliers, 28 retained, and 19 with both electrophysiology and behavior. Ratings were taken in a separate procedure from the repeated short FFR stimuli; FFRs are stimulus-locked aggregate electrophysiology, not simultaneous single-trial experience readouts. Across those 19, the authors report Spearman `r_s=0.49`, one-tailed Bonferroni-corrected `p=0.02`, between their subtraction-waveform NCI and consonance preference. For other FFR variants, the individual correlations were not significant. After statistical adjustment for musical experience, they report `r_s=0.23`, `p=0.18`; this does not prove musical experience caused or fully explains the association, especially with a small sample, potential selection effects and differing causal roles for the covariate. Correlations across stimulus-averaged intervals are a different analysis from correlations across participants and should not be treated as 19 independent replications across stimuli. Diotic versus dichotic presentation changes how notes enter the ears, not only neural salience, so it does not isolate the neural signal as the cause of pleasantness.

Reading scope: abstract and selected methods, all results and discussion, table text and captions were read in the open HTML; introductory chunks, figures as images, raw signals, MATLAB script and dependent prior derivations were not audited. The paper's interpretation of the FFR as predominantly brainstem-related is used as its own account; scalp FFR source attribution requires additional evidence and is not established by our analysis. Neural harmonics, relative phase synchrony, roughness and **frustration of coupled components** are not interchangeable. The separate [Lahdelma–Eerola article on familiarity, pleasantness and perceived tension](https://doi.org/10.1038/s41598-020-65615-8) reports correlated but distinguishable concepts and context effects; we read its abstract and opening introduction only, not its full text, figures or data.

## 3. A sharper joint empirical bridge

These two datasets are **different experiments and people**. The neural index cannot be joined to the sequence ratings and no incremental prediction by neural mismatch has been demonstrated. A useful joint protocol would:

1. Keep the final waveform and delivery fixed and randomize multiple prior contexts within participant; separately collect final-chord and whole-sequence ratings in counterbalanced blocks, not necessarily together in the same trial. Validate audio and safe playback, while acknowledging that continuous reports themselves change attention.
2. Include a sufficiently large, diverse sample and multiple chord/timbre/context families; record individual musical history and hearing, and deliberately cross roughness, harmonicity, familiarity and tonal expectation as far as physical and musical constraints allow. Predefine unsupported combinations and avoid claiming a pure factor intervention where chord identity co-varies.
3. Prespecify and calibrate a subject-internal candidate mismatch `q` from independent neural channels and separately gathered calibration data, along with artifact controls and uncertainty. Compare it with established stimulus features, prior-context predictors, and an established FFR harmonicity index, not just with an impoverished final-chord-only rule. FFR requires suitable stimuli and long averaging; a trial-level EEG signal cannot simply be called the same FFR. Separate feasible trials and predictions by time window.
4. Predefine participant-held-out and stimulus-family-held-out tests with clustered uncertainty and quantitative smallest meaningful effects. Test whether `q` improves predictions on held-out data and whether randomized perturbations that change `q` while matching major alternatives shift reports as predicted. Training history and attention can be confounders, mediators or selection variables depending on the causal question; don't assume adjustment automatically identifies a direct effect.
5. State exactly what result would disfavor the proposed candidate. For example, reliable calibrated manipulations that change `q` without its predicted report change, in a domain where the model predicts a minimum effect and measurement error is bounded, would challenge that specified law. Failure to detect a weak effect without power or calibration is inconclusive.

Even a successful incremental prediction or mediation result would constrain a physical–report map, not derive why there is experience, determine which organized system is a subject, or establish that `q` **is** felt valence. Those remain distinct requirements; first-person experience remains a valid datum, and an experience-respecting alternative can predict the same reports. The timeless whole need not have an external clock merely because local experiments have ordered stimuli.

## Reproduction

With Python and `pyreadstat==1.3.2` installed, obtain the two inputs from the pinned commit. Keep them in `.arena/` (ignored and not published), since the SPSS file contains participant-level records:

```sh
mkdir -p .arena/penultimate
for f in data/PleDisso1.sav data/stimulusTable.csv; do
  gh api -H 'Accept: application/vnd.github.raw+json' \
    "repos/tuomaseerola/penultimate_chord/contents/$f?ref=010777ada95da0044492d14865a162d7bc2874f8" \
    > ".arena/penultimate/$(basename "$f")"
done
python verification/pleasantness_final_chord_context_gate.py
```

The repository advertises an MIT license; reassess data-specific rights before redistribution. The script checks source hashes and writes only aggregate output. It does not execute or reproduce the authors' R mixed-effects model.
