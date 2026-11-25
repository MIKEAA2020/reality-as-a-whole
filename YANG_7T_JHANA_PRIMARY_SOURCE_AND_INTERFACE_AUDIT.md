# The uploaded 7T jhāna study: primary-source reading

## Why this paper matters here

The uploaded paper is the primary study behind part of the earlier [Scientific American article analysis](ADVANCED_MEDITATION_SELF_CESSATION_AND_ZERO.md): Winson Fu Zun Yang and colleagues, “Intensive whole-brain 7T MRI case study of volitional control of brain activity in deep absorptive meditation states,” *Cerebral Cortex* 34(1), bhad408, [doi:10.1093/cercor/bhad408](https://doi.org/10.1093/cercor/bhad408). The supplied 16-page PDF is the 2023 online version; the journal issue is dated 2024. Uploaded PDF SHA-256: `debe134f03d48440f697d92a78742308562846bea99098395c344a858e678029`.

Its strongest contribution to our inquiry is **not a proof that consciousness is one or that meditation reveals zero**. It is an unusually detailed paired observation of a trained person's descriptions of altered experience and changes in a measurable aspect of brain organization. It makes the question of how a single physical–experiential reality can sustain different internal organizations more concrete.

The important qualification is that this is an exploratory **one-person** study, with repeated runs, not 27 independent meditators. Its results are hypotheses and observations about that person and protocol, not a universal neural signature or evidence that a specific mathematical pointer is conscious. The analysis below reads the uploaded paper; it does not analyze the raw MRI data, which the paper says may be requested subject to institutional review board approval (PDF p. 14).

## 1. What the participant did and reported

- The participant was a 51-year-old experienced teacher with over 25 years of jhāna experience; the paper estimates approximately **23,110 hours** of practice from stated assumptions (p. 3).
- Over **five consecutive days**, the participant completed **27** eyes-closed jhāna runs, moving in a fixed sequence from access concentration through J1–J8 and afterglow. The average analyzed J1–J6–8 run lasted about **512 seconds** (pp. 3–4).
- Button presses marked transitions through J6. The participant reported that indicating J7 and J8 would disrupt practice, so the study analyzed **J6–J8 together**, not as separately identified MRI intervals (p. 3). This is a direct methodological instance of the report-interface problem: a measurement action may alter what is being measured. It does **not** test or validate the numerical predictions of our finite sign model.
- Immediately after each full run, the participant rated personally developed experiential items on 1–10 scales, including attention, joy-like J2 qualities, mental ease, equanimity, formlessness and early/late narrative thought. For J6–J8, formlessness ratings were averaged to match the pooled imaging interval (pp. 4, 11). These ratings are first-person evidence and an important strength, but they are retrospective and do not by themselves constitute an independent continuous experience monitor.
- The comparison conditions were mental **memory narration** and **counting backwards by five**. Each had two eight-minute runs: one before meditation and one on day four. The participant reported entering meditative states during the first runs of both controls; the authors also analyzed the later control run separately (pp. 3, 5). These controls therefore do not cleanly establish what all non-meditative consciousness looks like.

The qualitative experiences are meaningful in their own right. Reported joy, equanimity, attenuated narrative and formlessness are not interchangeable, and a state described as “nothingness” need not mean the physical whole or all experience has ceased.

## 2. What the MRI number means

The authors used 7T BOLD fMRI: 1.1 mm acquisition voxels and a 2.9-second repetition time, plus physiological recordings and preprocessing (p. 4). They measured **regional homogeneity (ReHo)**, using Kendall's coefficient of concordance across each voxel and its 26 nearest neighbors. Roughly, ReHo captures the similarity of temporal rankings of nearby BOLD signals. They standardized the values, applied 6 mm smoothing, and used a 538-region parcellation (p. 5).

This is a measure of **local BOLD-signal concordance**, not a direct count of neurons firing, total neural activity, physical energy, amount of consciousness, or felt valence. BOLD is an indirect hemodynamic measurement. A higher or lower standardized ReHo value should not simply be translated into more or less subjective experience or a region being universally “switched on/off.” Acquisition voxel size is not the final effective spatial precision after smoothing and other processing; 7T also does not remove the temporal or physiological limits of BOLD imaging.

An exact synthetic control in [`verification/jhana_reho_sequence_and_sampling_identifiability_test.py`](verification/jhana_reho_sequence_and_sampling_identifiability_test.py) constructs 27 rank-ordered voxel time series, changes their positive scales and offsets, and obtains **identical** Kendall concordance despite different numerical signal magnitudes. This illustrates why concordance is not the same statistic as signal magnitude. It is not an analysis or reconstruction of the participant's fMRI, nor does it claim that this transformation occurred in the study.

## 3. What the paper reports

Across the six analyzed stage categories, the authors report region-dependent linear and nonlinear ReHo patterns in cortical, subcortical, brainstem and cerebellar regions (pp. 5–6). They also report differences from the two control tasks, and associations between ReHo and different experiential ratings. For example, higher ratings of J2 joy were associated with higher ReHo in right somatomotor areas and lower ReHo in right temporal areas; other patterns were reported for mental ease, equanimity and formlessness (pp. 10–11). These are within-person associations in the specified data, not established markers that can yet read another person's experience.

For attention and intensity, the paper uses correlations across stages and runs; some of these associations could reflect differences *between* stages, changes *within* a stage across runs, or both. Other analyses, such as the stage-specific J2 joy rating, have a different structure. It would be incorrect to treat the pooled correlation as automatically establishing a within-stage mechanism or to treat all 27 × 6 measurements as unrelated people. Multiple-comparison corrections were applied across the stated regions and tests; those corrections do not by themselves establish generalizability or rule out dependence and model-selection issues (pp. 5–6, 10).

The paper reports **no significant linear trend** in the recorded cardiac or respiratory measures across stages, but it also reports a respiratory difference for **J1 versus counting**, \(t=3.64, p=0.01\) (p. 11). It applied physiological-noise regression. These are useful checks, not proof that physiological effects were absent, that parameters were equivalent across stages, or that all residual physiological influences were removed. In particular, a nonsignificant result is not an equivalence test. The discussion's stronger assertion that brainstem involvement cannot be explained by physiological noise should be read more cautiously than the methods warrant.

## 4. The fixed sequence and pooled deepest states

Every run followed the same J1-to-J8 order. Observed changes across the sequence may reflect stage-related processes, elapsed time, cumulative practice, fatigue, changing physiology, expectations, or combinations of these. Variable stage durations and repeated runs can supply some information to distinguish them; fixed ordering does **not** prove that the real data are completely unidentifiable. But the labels and elapsed-time effects are not cleanly randomized apart, so a causal claim that a stage alone produced a given pattern needs further evidence.

The accompanying synthetic verifier gives a precise counterexample: if every run had the same fixed stage schedule, a stage-driven model and an elapsed-time-driven model could fit every observation identically and disagree on a different schedule. That is a mathematical possibility, **not** an assertion that the participant had fixed dwell times or that elapsed time explains the actual findings.

Likewise, because J6–J8 were not separately marked in the scanning interval, their individual ReHo patterns cannot be recovered from the reported pooled-stage analysis alone. As a simple illustration of the ratings issue, the two different formlessness profiles \((2,5,8)\) and \((5,5,5)\) have the same average. This does not assume that ReHo of a pooled time series equals an arithmetic average of three stage-specific ReHo values.

There is also a control-sampling distinction: each control condition's 16 one-minute segments came from **two** eight-minute runs, not 16 independent sessions or participants (pp. 3–4). For illustration only, the verifier shows that if eight segments in each of two independent runs had equal within-run correlation 0.75, the variance of their mean would correspond to 2.56 independent, equal-variance segments rather than 16. The study's actual segment correlation is unknown here; this calculation is not its estimated effective sample size or a claim that its analyses are invalid.

## 5. What it adds to the one-reality construction

The paper supports a **researchable distinction** between changes in narrative self-model, experiential content, emotional qualities and the physical organization accompanying them. That aligns with the proposed picture of one reality internally differentiated into physical appearances and experiences, without implying that the physical and experiential aspects have been reduced to one another or that matter is eliminated.

It also gives a concrete empirical parallel to the [internal reference and record trade-off](ZERO_INTERNAL_CONTEXTUAL_REFERENCE_AND_RECORD_TRADEOFF.md): the participant reported that marking certain transitions would disrupt the practice, so those distinctions were not separately recorded. Both examples make interface effects important. The parallel is conceptual only—the finite quantum gate, its one-quarter record disturbance, its orientation charge and the participant's brain are **not** identified.

Most importantly, the paper does not establish a signed global experience quantity. J2 joy and J4 equanimity were measured using different positive-strength descriptions, not as positive and negative terms on a common additive physical scale; suffering was not calibrated against compensating experience. Neither ReHo nor a quiet narrative self is zero whole-energy or zero total feeling. The result is compatible with intrinsic experience and extrinsic matter as aspects of one reality, but also with other mind–brain accounts, so it does not by itself establish that metaphysical identity.

## 6. A discriminating successor

A stronger follow-up could preserve the valuable participant-specific phenomenology while separating competing explanations:

1. Recruit multiple experienced practitioners, repeat sessions across days, retain the individual as a unit of inference, and independently validate any subgroup/generalization claim. Preserve individual practice styles rather than assuming one common jhāna phenotype.
2. Preregister stage-specific versus elapsed-time and day/run effects. Where practitioners can do so safely without changing the targeted practice, include counterbalanced entry or dwell-time manipulations and matched time/attention controls. Do not assume a proposed reordered sequence is feasible. Treat transition timestamps as uncertain and compare minimally cued versus uncued periods for disturbance.
3. Estimate associations **within each stage across runs** separately from differences between stage means. Evaluate predefined ReHo signatures on held-out sessions and independently held-out participants; use cluster-aware uncertainty rather than treating every segment as an independent participant.
4. Measure self-boundary, narrative, attention, arousal, pleasantness/unpleasantness and distress separately, alongside physiology. Preregister whether a neural feature predicts within-person reported boundary change beyond attention, arousal and valence, rather than retroactively labeling a brain region “nonduality.” A held-out failure would count against that specific operational prediction, not refute the one-reality ontology; a success would not by itself prove it.

## Reproduce the synthetic checks

```sh
python -m unittest verification.jhana_reho_sequence_and_sampling_identifiability_test -v
```

The verifier uses invented numbers and exact arithmetic. It neither reproduces the study nor infers a participant's phenomenology. The PDF was supplied by the user; no underlying human data have been downloaded or analyzed.
