# PAINgen condition means: subset diagnostic plan

## Question and scope

The [prior event-provenance audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md) used all accepted stimulus rows in each person × modality × nominal-level × treatment cell; 610 intensity and 608 unpleasantness finite cell means did not match the published author export. We will check whether those export values are **numerically consistent with averaging a common subset of the available trial-rating pairs**. This is a post hoc diagnostic motivated by the already observed discrepancies. No claim of blind hypothesis selection, independent replication, or discovery of the authors' actual selection rules is appropriate.

An exhaustive subset match can show what is arithmetically possible under our current join, not which records were actually used: multiple subsets can tie, equal responses are common, unobserved data or transformations can produce the same mean, and the authors may not have used the event export to create the table. An exact numerical witness is not evidence that discarded trials were erroneous or that the study was biased. Do not change the original models, make a corrected dataset, infer outcome-selective exclusions or a placebo effect, or use a best-matching subset as an independently validated reanalysis.

## Sources and pre-existing inspection

Use precisely the same pinned, digest-checked dataset v1.0.0 tree and archive, author behavioral CSV, conservative sorted-onset episode parser, participant/condition join, run-treatment convention, level mapping and `10⁻¹⁰` comparison tolerance as in the prior audit. Read no participant metadata, MRI, or external participant-level records. Save aggregate counts only. The compressed archive and its Git blobs must be checked against the same pinned hashes. Retained episode values are internally duplicated in stimulus and question events; verify the two agree before use. Do not publish IDs, exact individual subsets or trial values.

Target the **4,400 overlapping condition keys** with finite source means in both rating dimensions and at least one retained paired trial. Include keys whose full trial average matched as well as those that did not; retain counts for missing source outcomes and unjoined keys. A stop on changed counts or dataset inputs prevents presenting a result from a silently altered cohort. Our existing 1,566 accepted runs and their source-row validation are reused; do not change which event files are accepted.

The authors' pinned `evaluate_pain_evoked_measures.m` reads the already-existing behavioral export at its line 23, then applies later analysis filters. We have not found or run the program that initially created the export; the downstream script does not establish its exact trial-selection process. The OpenNeuro Git tree contained no `.m`, `.py`, `.r`, `.R` or `.sh` file by filename inspection. A GitHub search for the exact export filename returned the paper repository's README and downstream analysis file plus other indexes/third-party results; that is not an exhaustive search of all code or inaccessible storage.

## Exact combinatorial comparison

For each eligible cell with `n` paired trial ratings `(I_j,U_j)`, enumerate every **nonempty subset** of the same trial indices, with both component means compared to the two exported means. The subset must be common to both dimensions. Evaluate the following mutually exclusive categories:

1. Full set matches both (regardless of whether other subsets also match).
2. Full set fails, but at least one **proper subset** matches both.
3. No nonempty subset matches both.

For category 2 report (a) number with exactly one versus more than one matching subset; (b) number with at least one matching subset containing every retained trial from exactly one of the two relevant runs and none from the other; and (c) number with exactly one matching subset and that subset a whole single run. A cell can have multiple matching witnesses, so (b) alone does not establish which run was used; (c) is uniqueness only among these retained subsets and this tolerance. Also report the number of retained ratings excluded in the unique-witness case. Require a hard cap of 10 trials per cell, fail otherwise rather than making a partial search.

For comparison, report intensity-only and unpleasantness-only existence of any subset among category 3; matching different subsets for the two dimensions is not a common-pair explanation. Record how many eligible cells have records from both relevant runs, and the distribution of trial counts. Give aggregate counts overall and by modality and treatment; no confidence intervals or hypothesis tests are planned because these are exhaustive descriptive comparisons of the pinned files, not sampling estimates. The condition key's treatment mapping and onset-based parser remain assumptions, not validated ground truth.

## Consequence and stopping rules

If substantial mismatches have exact common proper-subset witnesses, record that the data are consistent with some trial subsets, **not** that any particular exclusion occurred. If no common witness exists, the simple matched-subset explanation fails under the declared inputs and tolerance, but a mapping, rounding, weighting, missing-data or other preprocessing explanation remains possible. If all full sets match or the previous counts cannot be reproduced, stop and investigate implementation rather than treating the prior discrepancy as resolved. Any later attempt to infer actual inclusion requires independently documented inclusion metadata, original logs, processing code or author clarification. Neither result identifies a physical mismatch `q`, causal pain mechanism, an experiential identity or the reasons for missing data.
