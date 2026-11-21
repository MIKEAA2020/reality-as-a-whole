# PAINgen condition means: a published response-time rule explains most discrepancies

## Result and scope

The [published Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC11255344/) of Botvinik-Nezer et al. (2024, DOI [10.1038/s41467-024-50103-8](https://doi.org/10.1038/s41467-024-50103-8)) say that individual stimulus trials were excluded when the pain-**intensity** rating response time was **below 0.02 s or above 5.01 s**. Our previous provisional average did not apply that rule. Applying it to the BIDS intensity-rating event's `response_time` field as a **candidate** for the authors' timing variable makes **585 of the 620 previously mismatching paired condition means match** the authors' export, without making any previous paired match fail. The other **35 remain mismatched**.

This is strong retrospective evidence that the published exclusion rule is relevant to the discrepancies, not independent proof that we recovered the original processing pipeline. The paper does not identify the precise CSV-generating code or establish that the BIDS field is the exact original variable. The BIDS event sidecar we inspected documents the two ratings and stimulus levels but does **not** define `response_time` or its units; seconds here are the interpretation used to test the paper's rule, not an independently validated mapping. The event files and condition export are related releases from the same study, not independent evidence of participant experience or hardware delivery.

The [analysis plan](PAINGEN_RESPONSE_TIME_RECONSTRUCTION_PLAN.md) was written before sample-wide RT screening. It specifies inclusive retention at the two boundaries, shared deletion of both ratings, no cutoff tuning, unresolved missing RT and aggregate-only reporting. The follow-up missing-export diagnostic was explicitly added **after** the first results. The selection of the source and the question were already informed by prior analyses, so this is not a prospective preregistration or independent replication.

## Fixed paired-mean comparison

We used the same hash- and Git-blob-verified v1.0.0 input, accepted event grammar and condition join as the [trial provenance audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md) and [subset diagnostic](PAINGEN_CONDITION_MEAN_SUBSET_PROVENANCE_DIAGNOSTIC.md). Each paired mean is considered a match only if **both** dimensions agree to `10⁻¹⁰`. The 4,400 eligible overlapping keys have finite exported ratings for both outcomes; all had enough candidate-screened data to compare.

| All accepted trials | Candidate RT-screened pair matches | Candidate RT-screened pair mismatches | Total |
|---|---:|---:|---:|
| Pair matched export | 3,780 | 0 | 3,780 |
| Pair mismatched export | 585 | 35 | 620 |
| Total | 4,365 | 35 | 4,400 |

There were **zero unresolved** eligible cells from unavailable RT or no retained trial. The rule changed membership in 603 eligible cells, removing 704 and retaining 11,022 paired trials in these cells. A membership change need not change a mean, and an average match need not uniquely identify a trial set. On intensity alone, 575 of 610 mismatches became matches, leaving 35; on unpleasantness, 575 of 608 became matches, leaving 33. Neither outcome had match-to-mismatch regressions. The different marginal counts cannot be added to obtain the paired result.

The paired mismatch-to-match / mismatch-to-mismatch counts were **246 / 14** mechanical and **339 / 21** thermal; by treatment they were **365 / 24** control and **220 / 11** placebo. These are overlapping descriptive groupings, not tests of between-group differences. For full transitions and trial counts see the [aggregate receipt](verification/paingen_response_time_reconstruction.json).

The earlier exhaustive calculation found exactly these numbers of mismatches had a proper-subset witness (585) or lacked *any* common nonempty subset witness (35). The present RT-selected pairs match all 585 cases and none of the 35. By construction, deleting trials from the same set cannot resolve a no-subset case; this cross-check is not independent confirmation of either the original selection or the source of the remaining mismatches. Other exclusions, missing or rejected runs, condition construction or transformations are possible explanations; their relative importance has not been established.

## Event counts and missing exports

Among **12,528 episodes** in the 1,566 accepted runs, the candidate intensity-event field was finite and in range for **11,022**, below the lower bound for **140**, and above the upper bound for **1,366**. There were zero unavailable values and zero exact-boundary values in these accepted episodes. Seven event files failed the earlier row-count rule and one failed schema; these files are not interpreted as necessarily invalid experimental trials. The earlier onset-sort amendment is important: it followed inspection, not a blinded preregistration.

There were 4,707 overlapping condition keys, two export-only keys and 307 overlapping keys with missing exported outcomes. The **post-result** diagnostic found both exported ratings missing in all 307; all **802 recorded accepted trial pairs** in those cells had out-of-range candidate RT (44 below, 758 above). This is consistent with the RT rule leaving no retained accepted trial for those keys. It does not prove why the author export is missing, or exclude unaccepted/missing runs or other selection mechanisms. We do not impute values. The accounting is 704 removed eligible pairs + 802 pairs in missing-export cells + 11,022 eligible retained pairs = 12,528.

## What changes, and what does not

The earlier statement that the source of most discrepancies was wholly unexplained should now be read in light of this result: the documented RT rule supplies a concrete, quantitatively successful **candidate reconstruction**, though 35 finite paired means still cannot be reproduced by selecting a subset of our accepted events. Prior held-out analyses remain calculations of the authors' exported means; they are not independent trial-replications. The finding does not diagnose author error or provide an independent physical mismatch `q`, a channel preference, a first-person constitution, or a physical-to-experiential law.

For a next empirical route, the existing [pain/aversion dataset readiness assessment](PAIN_AVERSION_CROSS_MODALITY_EXPERIENTIAL_READINESS_GATE.md) is a better candidate for same-person continuous ratings and EEG across modalities, but its signal and rating annexes remain uninspected, its task constructs differ, and the protocol's fixed sequence creates schedule confounding. No validated intervention-based channel-preference measurement is presently identified there. Observed EEG phase lags are not automatically preferred interactions: the [phase-lag gate](OBSERVED_PHASE_LAGS_VERSUS_PHYSICAL_FRUSTRATION_GATE.md) gives explicit counterexamples. Do not relabel a correlation as `q` or as an experiential bridge. B4–B5/F2, B9/F3, B10 and C3 remain open.

## Reproduction and limitations

Fetch the pinned [recursive tree](https://api.github.com/repos/OpenNeuroDatasets/ds004746/git/trees/8a38ee30b870373547676bf0d0638e16160472a1?recursive=1) and [archive](https://codeload.github.com/OpenNeuroDatasets/ds004746/tar.gz/8a38ee30b870373547676bf0d0638e16160472a1), then run:

```sh
PYTHONPATH=verification python -m unittest -v paingen_response_time_reconstruction_test
PYTHONPATH=verification python verification/paingen_response_time_reconstruction.py --tree TREE --archive ARCHIVE
```

The [script](verification/paingen_response_time_reconstruction.py) retrieves the pinned author CSV unless a `--behavior` path is supplied; it verifies its byte length and SHA-256, the tree and archive SHA-256, and all 1,574 target Git blob hashes. It checks prior screen and join counts, rating-field agreement, the prior paired and per-dimension match totals and exhaustive-subset counts, and trial accounting. Tests cover bounds, paired deletion, missing RT, no retained trial, a regression and missing-export categorization. No IDs, trial data or individual-level results are written to the receipt. These checks apply to the specified released files and accepted event grammar only; they cannot establish the experiment's unobserved processing history.
