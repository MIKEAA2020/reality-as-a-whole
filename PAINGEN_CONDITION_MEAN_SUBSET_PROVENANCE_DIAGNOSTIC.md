# PAINgen condition means: which discrepancies admit a trial-subset explanation?

## Result

**Later follow-up:** the [published RT-rule reconstruction](PAINGEN_RESPONSE_TIME_RULE_RECONSTRUCTION_AUDIT.md) selects a matching subset in all 585 proper-subset cases, leaves the 35 no-subset cases mismatched, and causes no paired regressions. This is a source-supported candidate, not verified trial-selection history.

The [previous BIDS audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md) found 620 condition keys for which at least one of the published intensity and unpleasantness means differs from a simple average of all retained BIDS trial pairs. Under the same provisional join, **585 of those 620 keys have at least one proper subset of the recorded trial pairs whose two means jointly match the published values** within `10⁻¹⁰`. The remaining **35** have no such nonempty common-subset match.

This narrows an arithmetic question; it does **not** identify the actual trial-selection procedure or establish that the authors excluded those trials. Even a unique matching subset is unique only among the inspected retained trials and the specified tolerance; other data, transformations, weighting, rounding or processing histories could generate the same mean. Nor does an unmatched key prove a data error. We have not found or replayed the code that generated the condition table. The earlier held-out calculations remain calculations on that table, with their event-to-export provenance unresolved.

## 1. Method and provenance

This is a deliberately **post hoc** follow-up to the known discrepancies, not a preregistered or independent replication. Its [fixed diagnostic plan](PAINGEN_CONDITION_MEAN_SUBSET_DIAGNOSTIC_PLAN.md) was written after the previous results but before running this subset search. The [checker](verification/paingen_condition_subset_diagnostic.py), [tests](verification/paingen_condition_subset_diagnostic_test.py), and aggregate [receipt](verification/paingen_condition_subset_diagnostic.json) preserve the calculation. No participant identifiers, individual values or subset masks are written.

Input and eligibility are unchanged from the previous audit: paper-cited [OpenNeuro ds004746 v1.0.0](https://doi.org/10.18112/openneuro.ds004746.v1.0.0), its [pinned GitHub tree](https://github.com/OpenNeuroDatasets/ds004746/tree/8a38ee30b870373547676bf0d0638e16160472a1), and the [authors' behavioral export](https://github.com/rotemb9/paingen-placebo-fmri-paper/tree/da46f2f9739ad2e9eeb9658711582be6357c1026). All 1,574 event blobs are checked against the nontruncated tree; after the same onset sorting and strict episode grammar, 1,566 runs and 12,528 paired episodes are retained. The duplicated stimulus-row and rating-event values agree in all retained episodes. We use the earlier run-to-treatment and level-code mapping and the same `10⁻¹⁰` absolute tolerance. These are explicit reconstruction assumptions, not author-confirmed pipeline rules.

The prior audit found 4,707 overlapping person × modality × level × treatment keys and two export-only keys. On 307 overlapping keys, at least one export rating is missing; these are **excluded from the numerical subset search**, not set to zero. This leaves **4,400 eligible keys**. A cell has one to six retained trial pairs; 4,199 eligible keys include trials from both relevant runs. A hard search cap of ten trials per cell prevents silently truncating the search.

The authors' pinned [`evaluate_pain_evoked_measures.m`](https://github.com/rotemb9/paingen-placebo-fmri-paper/blob/da46f2f9739ad2e9eeb9658711582be6357c1026/evaluate_pain_evoked_measures.m#L22) reads the behavioral CSV at line 23 and later applies analysis filters; it does not by that fact reveal how the CSV was first generated. A filename scan of the dataset Git tree found no `.m`, `.py`, `.r`, `.R` or `.sh` processing file, and a limited GitHub code search located the paper repository's README and downstream script among other results. Neither search establishes that the earlier processing code does not exist elsewhere.

## 2. Exhaustive paired-subset results

For each eligible cell, enumerate every nonempty subset of the retained trial **pairs** `(intensity, unpleasantness)`. A witness must match *both* exported means using the **same** subset. A different intensity-only and unpleasantness-only selection is not counted as a common witness. The full-set case is counted first even if smaller subsets also happen to match.

| Mutually exclusive result | All | Thermal | Mechanical | Control | Placebo |
|---|---:|---:|---:|---:|---:|
| All retained trial pairs match both means | 3,780 | 1,843 | 1,937 | 1,810 | 1,970 |
| Full set fails; some proper subset matches both | 585 | 339 | 246 | 365 | 220 |
| No nonempty common subset matches both | 35 | 21 | 14 | 24 | 11 |
| **Eligible cells** | **4,400** | **2,203** | **2,197** | **2,199** | **2,201** |

Thus **585/620 ≈ 94.4%** of the previously observed paired-mean mismatches admit a proper-subset arithmetic witness in this bounded reconstruction. This fraction is a description of selected keys, not a population estimate, an estimate of the fraction of actual excluded trials, or a test that the two treatments had different rates of exclusion. The differences by treatment can also reflect the reconstruction assumptions and sample composition.

Among those 585 proper-subset cases:

- **566** have exactly one matching subset among the retained trial pairs; **19** have more than one.
- **330** have at least one witness that includes all retained trials from one recorded run and none from the other, in a cell with both runs represented. For **315**, that whole-run witness is the only matching subset. These figures overlap with the 566 unique cases; they are not additional discrepancies.
- Among the 566 unique witnesses, the complement contains one retained trial in 474 cells, two in 88, and three in four. The complement is not shown to be an actual exclusion.

For the 35 keys with no common witness, **zero** have any subset reproducing the intensity mean alone and two have a subset reproducing the unpleasantness mean alone. Consequently, the simple common-subset explanation fails for these keys under the declared join and tolerance. It does not exclude source rounding, different data, level/run mapping problems, excluded files, weighting or other transformations. Conversely, the 585 arithmetic matches do not establish that a subset rule generated the export, particularly when the possible subsets were exhaustively searched after the mismatch was observed.

## 3. What this changes—and what it does not

**Positive progress:** the discrepancy is no longer just an undifferentiated gap. Most mismatched cells are numerically compatible with a common subset of the recorded two-rating trials, often uniquely within the finite candidate set. That is a useful lead for checking source-level inclusion and preprocessing, and the 35 remaining cells prevent declaring the whole discrepancy resolved by subset selection alone.

**Still needed:** independently obtain or inspect the original first-level behavioral-generation pipeline and any run/trial inclusion record; check version, row and condition mapping, rounding and behavior-to-imaging alignment; reconcile the missing and two export-only keys. Compare the documented inclusion decisions against the subset witnesses **without tuning them to the output**. If those materials cannot be obtained, leave the cross-export provenance unresolved. Do not substitute the witnessed subsets into the previous pain prediction benchmark and call it validated.

**Phenomenal and physical scope:** neither the existence of matching subsets nor absence of one says whether the intensity and unpleasantness experiences are identical or distinct, whether a participant genuinely felt pain, or whether recorded order caused a rating difference. Neither measures the proposed physical `q`, validates subject boundaries, establishes a ground, or decides the philosophical alternatives. Source reports are evidence about experience; an unresolved transformation between recorded exports is not evidence against experience itself.

## 4. Reproduction and status

Obtain the exact tree and archive as in the [BIDS audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md), then run:

```text
PYTHONPATH=verification python -m unittest -v paingen_condition_subset_diagnostic_test
PYTHONPATH=verification python verification/paingen_condition_subset_diagnostic.py --tree TREE --archive ARCHIVE
```

`--behavior PATH` selects the exact pinned local behavioral CSV instead of downloading it. The code verifies the tree/archive digests, all Git blobs, event values, the original selection counts and the 3,780 full-pair matches before producing the receipt. Five synthetic unit tests check common versus separate subsets, ambiguity, full-set priority and the search limit. These are software checks, not validation of the experimental pipeline. No raw EEG/MRI or participant-level data are committed.

The cross-export discrepancy remains open, as do B4–B5/F2, B9/F3 and B10. C3 continues to require full structural **and** experiential intelligibility; this diagnostic makes no substantive battery pass.
