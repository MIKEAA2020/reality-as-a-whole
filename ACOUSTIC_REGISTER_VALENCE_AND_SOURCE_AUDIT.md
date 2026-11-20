# Acoustic mismatch, reported consonance and the experiential bridge

## Result and scope

An independently computed **external stimulus** mismatch proxy makes a sharp but limited test possible. In the public Eerola–Lahdelma register experiment, a deliberately restrictive theory says that a listener's expected consonance is a nonincreasing function of the published symbolic roughness value alone. It predicts higher or equal consonance in the high registers than in the middle registers for each of the four chords. In our eligible 59-person subset, the observed high-minus-middle mean is **−0.250** on a 0–10 consonance scale; a paired participant-bootstrap 95% interval is **[−0.763, 0.288]**. Thus this analysis is **inconclusive about the population inequality**, even though the sample means go against it. The result is not a demonstration that string vibration misalignment is unpleasantness or that it is not.

The contribution is a fixed, inspectable inequality linking an external acoustic feature to a real first-person report and preserving the participant as the resampling unit. The results are retrospective and the underlying register effect and roughness/sharpness modeling are **already published**. This is neither discovery of that effect nor independent replication. We had read the article and predictor table before fixing the [analysis plan](ACOUSTIC_ROUGHNESS_REGISTER_FIXED_ANALYSIS_PLAN.md), so it is not prospective preregistration. The script's historical `heldout` filename does **not** mean the analysis uses a held-out cohort.

## Source and operational distinction

Eerola and Lahdelma, [*Register impacts perceptual consonance through roughness and sharpness*](https://doi.org/10.3758/s13423-021-02033-5), studied four piano-timbre chords in seven registers. They reported both register dependence and a regression using roughness and sharpness; 55 participants were described as passing all quality checks. Self-reports used a scale of **dissonant to consonant**, not a separately measured unpleasantness scale. Consonance may involve agreeableness or stability, but it cannot simply be relabeled felt valence, suffering or bodily discomfort.

The source roughness is the established Hutchinson–Knopoff model applied to **symbolic MIDI**, not an actual recording of the sound in each listener's ear, not a directly recorded neural frustration variable, and not an independent measurement of the subject's intrinsic state. Sharpness is a Zwicker-model estimate from audio; harmonicity and familiarity are also modeled from symbolic data. The four chords were selected partly using modeled roughness, harmonicity, familiarity and prior consonance information; chord selection was not independent of those concepts. The authors' acoustic modeling and established theories are credited to them, not reinvented as our novel physical law.

Read scope: the open article's abstract, introduction, methods, results, discussion and figure captions were read as rendered HTML; its figures themselves, supplemental materials, OSF preregistration, original audio, audio-feature scripts, model implementations, and cited proofs were not independently inspected. The pinned repository's README, preprocessing, means and acoustic-regression scripts and both CSV inputs were inspected; the complete repository and its analysis environment were not audited or executed. The public CSV contains recruitment identifiers and demographic fields; it is deliberately not copied into this repository. The aggregate receipt contains no participant rows. Independent input provenance and hashes are in the [receipt](verification/register_roughness_heldout_gate.json).

## Comparison and fixed-rule test

For every chord, both R6/R7 modeled roughness values are strictly lower than both R4/R5 values; all four comparisons of sharpness go in the opposite direction. A roughness-only monotone consonance rule predicts a nonnegative high-minus-middle expected difference. This prediction is agnostic about functional form and allows the monotone function to vary by person, but requires both that all other relevant changes have no effect and that report errors are conditionally unbiased. It does **not** test more general multivariable acoustic models or internal mismatch theories.

Our frozen inclusion rule keeps complete, plausible ratings after headphone and repeat-consistency checks but omits the authors' response-dependent negative-correlation exclusion. The raw file contains 77 rows; 10 fail the headphone criterion, 8 subsequently fail the repeat criterion, and 59 remain; no further target-rating exclusions. The mean is participant-weighted and the 10,000 bootstrap resamples are whole participants, preserving repeated-measure dependence. Four chord-specific differences (same people, not independent experiments) are:

| Chord | Middle mean | High mean | High − middle |
|---|---:|---:|---:|
| 3-11B | 7.678 | 7.254 | −0.424 |
| 3-7A | 6.483 | 6.034 | −0.449 |
| 4-20 | 5.797 | 5.068 | −0.729 |
| 4-19A | 3.890 | 4.492 | +0.602 |
| Equal chord average | 5.962 | 5.712 | −0.250 |

37 participants have negative, 1 zero and 21 positive average differences. Individual variation and the last chord's opposite direction caution against a universal simple directional interpretation. The participant-bootstrap interval describes sampling variability under independent participants and this fixed selected stimulus set; it does not quantify stimulus-selection uncertainty. The 0.125 sample-only lower bound for the two cell means' unweighted RMSE follows from their 0.250 inversion: the best ordered pair sets both predictions to their midpoint. It is not a population, held-out, or phenomenal-error bound.

## Source consistency issue worth checking

The article's printed high-versus-middle sentence assigns **5.96 to R6–R7 and 5.71 to R4–R5**, while also asserting a high-register decrease. Our independent reading of the raw column labels gives the reverse assignment (middle 5.962, high 5.712) in the 59-person subset. The numerical match to two decimals suggests a possible swapped label, but we have not reproduced the journal's exact analysis pipeline or ruled out a different data version; the published text should not be silently corrected. The source script constructs long-form `m` from `df` **before** `df <- df[!QC3,]` removes negative-correlation cases, then constructs analysis `m2` from the earlier `m`. At the pinned version this appears to leave the last quality exclusion out of downstream analyses using `m2`, despite the paper's description of 55. We have not run R or audited all downstream scripts, so this is a code-path observation, not proof of the journal analysis sample or an accusation of misconduct. It explains why our 59-person subset, not an alleged replication of the 55-person analysis, deserves explicit labeling. Different uncertainty estimates or model specifications can also change the inference; the participant bootstrap is not a replay of the authors' mixed-model contrast.

## What would advance C3

C3 requires **full structural and experiential intelligibility**, together with all other criteria; treating first-person experience as valid is non-negotiable. A rating is evidence about experience, not an excuse to eliminate it. Neither correlating an acoustic feature with reports nor a monotone constraint explains why a physical state feels unpleasant, selects a subject, or identifies the intrinsic nature of that state with feeling. Conversely, the inconclusive narrow test does not disprove an experience-intrinsic relational ground.

A serious next test should predefine a *subject-internal* measurable mismatch using independently calibrated physiological signals and fixed dynamics, not fit it from the valence reports it is meant to explain. Cross mismatch with other known determinants: match acoustic roughness while varying sharpness, harmonicity and learned familiarity; vary physiological mismatch while controlling stimulus and report context; collect separate pleasantness, tension and consonance ratings, timing, behavior and neural data. Use randomized manipulations when feasible, listener- and stimulus-disjoint tests when the design permits, participant-clustered uncertainty and sensitivity to selection/missingness. Predefine the experiential bridge and its rival report/learning models before seeing results. Even a successfully replicated prediction would only constrain the bridge: an independent account of subject constitution and the reason that the physical organization has that felt character would still be needed. Generalization to pain, other timbres and cultures, fundamental strings, and the timeless whole remains open.

## Reproduction

Retrieve only the two inputs from the source commit into ignored `.arena/register/` (do not publish the participant file), for example:

```sh
mkdir -p .arena/register
for f in data/data.csv roughness_and_sharpness.csv; do
  gh api -H 'Accept: application/vnd.github.raw+json' \
    "repos/tuomaseerola/consonance-register/contents/$f?ref=cdc4fc748e1535d9c0dd197f4c429bee80ff9514" \
    > ".arena/register/$(basename "$f")"
done
python verification/register_roughness_heldout_gate.py
```

The script validates input hashes, rating eligibility, feature-grid completeness and register ordering; it writes the aggregate JSON. It does not acquire the files by itself. The repository advertises an MIT license; provenance and any data-specific rights should be rechecked before redistributing participant data.
