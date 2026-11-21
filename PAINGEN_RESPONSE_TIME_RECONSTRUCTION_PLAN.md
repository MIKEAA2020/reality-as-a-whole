# PAINgen published response-time rule: retrospective reconstruction plan

## Motivation and source

The [BIDS audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md) and [subset diagnostic](PAINGEN_CONDITION_MEAN_SUBSET_PROVENANCE_DIAGNOSTIC.md) found 620 condition keys where at least one of the two all-trial means differs from the author export. In this follow-up, we revisited Botvinik-Nezer et al.'s [published Methods, Participants](https://pmc.ncbi.nlm.nih.gov/articles/PMC11255344/) (2024, DOI `10.1038/s41467-024-50103-8`). The authors state that individual stimulus trials were excluded when **pain-intensity rating response time was above 5.01 s or below 0.02 s**, and that participants could be dropped after excluding trials or scans if they lacked sufficient complete conditions. This relevant documented rule was not included in our earlier provisional all-trials mean. It is a serious candidate explanation, not yet the verified source CSV pipeline. The paper also describes other exclusions and preprocessing; no inference that this one criterion is complete is justified.

We have inspected the BIDS event schema and one run's distribution of `response_time`, but have not yet calculated the sample-wide response-time screening outcomes, or compared screened trial means against the condition export. The criterion is chosen from the published paper, not by optimizing fit on the export. This remains a retrospective, outcome-aware audit of a study and dataset already analyzed here, not a preregistered or independent replication.

## Source and fixed operational interpretation

Reuse the exact digest-verified v1.0.0 BIDS Git tree and archive and the exact pinned behavioral CSV from the [subset diagnostic](PAINGEN_CONDITION_MEAN_SUBSET_PROVENANCE_DIAGNOSTIC.md). Reuse its accepted runs, strict chronological event grammar, literal person/modality/level/treatment join and `10⁻¹⁰` mean-matching tolerance. Verify each intensity/unpleasantness stimulus-row value against its corresponding rating event; continue only if previous file, episode, key and all-trial comparison counts are reproduced.

For each accepted episode, take the `response_time` field on the `int_rating` event as the **candidate operationalization** of the paper's intensity-rating RT in seconds. This field's exact relationship to the authors' original timing variable has not been independently established; do not infer it from rating-event duration or substitute unpleasantness RT. For finite values, retain a paired episode if `0.02 ≤ RT ≤ 5.01` seconds and exclude **both** ratings if `RT < 0.02` or `RT > 5.01`, matching the paper's strict wording. Distinguish missing/nonfinite RT: do not automatically include or discard it in a way that manufactures a matched mean; flag the entire affected cell's screened reconstruction as unresolved. Count exact boundaries, low, in-range, high and unavailable RT by event, without storing personal records.

This deliberately implements only one published criterion. In particular, we do not reconstruct scan drops, subject exclusions, experimenter decisions, external missing trials, or other transformations. We do not tune RT cutoffs or screen on rating magnitude to improve agreement. An event duration is not an RT unless the data source independently supports that; any association between them is descriptive and is not needed for the rule.

## Fixed comparisons

For all 4,400 overlapping condition keys with both finite exported ratings and at least one prior accepted event pair:

1. Compute the original all-accepted-trial pair of means and the candidate RT-screened pair of means. A key with any unavailable RT or no remaining trial is **unresolved**, not a failed or perfect numerical match.
2. Classify each resolved key by whether **both** its intensity and unpleasantness means agree with the export: all-trial match and screened match; all-trial mismatch then screened match; all-trial match then screened mismatch; mismatch under both. Report the full 2×2 transition, unresolved count, and counts for intensity/unpleasantness individually. No adaptive subset fitting is permitted.
3. Report matched/unmatched counts among the 620 previous paired-mean mismatches, among the 3,780 previous full matches, by modality and by treatment. Mark any row for which the RT rule changed trial membership, and summarize the number of retained and removed trial pairs. Report all 307 export-missing overlapping keys and two export-only keys, but do not convert them into data-quality errors or reconstruct outcome values for publication.
4. If available, compare the resulting screened subsets with the earlier exhaustive proper-subset classification. Count only aggregates: for example whether cases previously lacking **any** common subset can match a screened subset. A no-common-subset key cannot be repaired by deleting only trials from the same declared set, so such a result would indicate a programming inconsistency and must stop the run.

No statistical significance tests, effect estimates, prediction score changes, or claims about causal exclusion bias are planned. Conditions have few repeated trials; matching a mean is not proof of matching the authors' hidden trial set. The shared-export provenance and retrospective nature prevent treating this check as independent biological validation.

## Interpretation and stop rules

If screening reproduces many previously unequal means, the documented rule is a concrete, source-supported candidate for some differences; report both remaining mismatches and regressions. If it does not, report that honestly and retain the possibility that `response_time` is not the authors' original timing variable. Even exact agreement for every cell would not independently confirm the original pipeline, participant exclusions, treatment assignment, raw hardware, pain phenomenology, or physical mismatch `q`.

Stop on input/hash mismatch, absent `response_time` schema, unsupported condition values, duplicate person/run or source keys, unexpected baseline counts, or inconsistent duplicated ratings. Retain aggregate output only, no personal identifiers or trial-level rows. A move to a more direct physical/phenomenal dataset remains necessary because these event and fMRI exports do not identify the project's channel preferences or `q`.

## Post-result extension: missing cells

After the initial screen reproduced all 585 previous proper-subset cases and showed no eligible cell had unavailable RT or zero retained trials, add one descriptive diagnostic that was **not pre-specified**: among the 307 overlapping keys with missing export outcomes, count whether both or only one rating is missing and whether all retained event trials fail the candidate RT rule, some pass it, or any RT is unavailable. Report cell and trial counts without imputing or predicting missing values. This directly checks whether the rule is consistent with missing means but still does not identify the authors' actual selection or all other missingness reasons.
