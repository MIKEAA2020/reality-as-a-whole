# Matched-stimulus valence stress test: analysis plan

## Purpose and limitations

Test a sharply restricted shortcut to the experiential misalignment proposal: **within a participant and fixed stimulus modality and level, the unpleasantness prediction is determined by that external stimulus alone**, with no effect of treatment context. The proposal may have person-specific, modality-specific and level-specific calibrations; it may fit a different value for each matched pair. It cannot vary across control and placebo within a pair. This is not the integrated candidate's actual internal `q`: no physical neural mismatch is observed in the available file. A result against the shortcut cannot falsify the broader hypothesis that an independently defined, context-sensitive internal mismatch is unpleasant.

Plan written before running this specific analysis, but **not prospective preregistration**: the same published data and placebo effect have already been examined in this project and in the source paper. This is an exploratory reanalysis using known data, not discovery, replication, a causal mediation analysis or a test of an experiential-ground ontology.

## Source and sample

Use the exact pinned, digest-checked pain-evoked brain-measures CSV and existing ingestion function in `verification/paingen_unpleasantness_baselines.py`. Study: Botvinik-Nezer et al., [*Placebo treatment affects brain systems related to affective and cognitive processes, but not nociceptive pain*](https://doi.org/10.1038/s41467-024-50103-8). Input: author GitHub repository commit `da46f2f9739ad2e9eeb9658711582be6357c1026`, file `pain_evoked_brain_measures.csv`, 3,728,915 bytes, SHA-256 `0eda58e9f8f83ec5294e92c907babfc771c0172ef22706e0be52c7182dbe8f56`.

Use `participant_ID`, `family_ID`, `heat`, `stimLvl`, `prodicaine` and `Yunp`; do not require fMRI signature availability or intensity report availability. Verify exact source size and hash, condition codes and unique person/condition keys, and fixed family membership. Include only participant × modality × stimulus-level cells with valid unpleasantness means in **both** control (`prodicaine=-0.5`) and placebo (`+0.5`). Count all rows, missing outcomes, usable and excluded incomplete matched cells, people and families. Distinguish these condition-averaged observations from original trial records. Do not print or write identifiers or individual outcomes.

## Fixed targets

Let `d_i = control unpleasantness − placebo unpleasantness` for each complete matched cell. Report, overall and separately for thermal and mechanical conditions:

- count of matched cells, unique participants and families;
- unweighted mean of `d`, mean absolute difference, root mean square difference, counts and proportions of positive, negative and exactly equal differences, and the within-person contrast direction;
- an exact descriptive **oracle lower bound** `sqrt(mean(d²))/2` on the row-level RMSE of any predictor constrained to produce identical values for the two observations in each pair. This allows an unattainable oracle to know both outcomes and pick a separate midpoint for every pair; practical models cannot do better on these same complete observations under the equal-output constraint. It is a mathematical fit floor, **not** held-out model performance and not a calibrated uncertainty bound on felt experience.

Values use the source numeric unpleasantness scale. Differences, averaging and RMSE are conditional on treating this scale as numeric; signs and ties are more weakly scale-dependent, but still depend on the instrument and reporting. Effect estimates are descriptive, not evidence that units are cardinal measures of subjective suffering. Individual cells, including repeated levels and modalities, are not independent.

## Cluster uncertainty

For the overall and two modality mean contrasts, produce 95% percentile intervals with 5,000 bootstrap resamples of **families**, sampled with replacement, fixed pseudorandom seed `202`. Each sampled family contributes all its matched cells, with its repeated sampled copies counted. Recompute the pair-weighted mean in each resample; this targets the pair-weighted distribution represented in this dataset, not an equal-family estimand. Use a local, deterministic random generator and check that each resample has a denominator. Bounds are exploratory and conditional on sampling assumptions, complete-cell selection and the published study; this is not an exact randomized test or independent replication. Families are clusters; within-family dependence is preserved. No threshold or post hoc favorable model selection is specified.

## Valid interpretation

The externally delivered stimulus was held fixed *within the coded condition pair*, but treatment instructions, conditioning, order and neural/bodily responses can differ. If the mean difference is nonzero, a strict stimulus-only mapping of **observed reports** fails to account for it. This leaves open internal mismatch, a report criterion, other psychological/physiological factors or combinations; changes in report do not establish that actual experience has changed, though self-report is evidence of experience and experience is not dismissed. Do not claim a selective neural intervention, identify `q`, infer a single physical mediator, assert an independently replicated experimental effect, or say a noisy mean difference proves an exact phenomenal identity.

A worthwhile later positive test would prespecify a separately measured internal `q` and compare it with independently defined sensory, contextual and physical rivals on held-out data. Current data do not supply that measurement. Failure to obtain it is an inconclusive test of the stronger experiential identity.
