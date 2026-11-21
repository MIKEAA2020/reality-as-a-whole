# PAINgen recorded prompt order, RT selection and timing: retrospective audit

## Finding and scope

In 12,528 episodes from 1,566 accepted complete BIDS runs, the candidate intensity-response-time screen retains **86.31%** when intensity is recorded first and **89.62%** when unpleasantness is recorded first. These are unadjusted descriptive differences in recorded metadata, not a causal effect of order or an effect on pain. For each rating type and recorded order, BIDS `duration − response_time` is uniformly 0.5 in stored numerical values, to floating-point precision. This is consistent with, but does **not** establish, a relationship to the 0.5-second post-response freeze in the candidate task code; field semantics and the historical conversion remain unverified.

The [fixed retrospective plan](PAINGEN_ORDER_RT_SELECTION_FIXED_PLAN.md) was written before these new stratified comparisons. Earlier results and overall order/RT counts were already known; this is not blinded or independent replication. We did not analyze pain-report values, the author condition-mean table, original MAT records or MRI here. The event files are parsed in memory but only aggregate results are saved.

## 1. What was counted

The same pinned ds004746 v1.0.0 tree and event archive as the [prior trial-order audit](PAINGEN_BIDS_TRIAL_ORDER_AND_MEAN_PROVENANCE_AUDIT.md) supply 1,574 verified event blobs. The established onset-sorted grammar accepts 1,566 complete runs (eight episodes each); seven files have a different row count and one lacks required schema. No partial-run recovery is applied in this analysis. Recorded order is inferred from sorted event onsets, not verified random assignment; the [candidate source analysis](PAINGEN_TASK_SOURCE_AND_PROMPT_ORDER_AUDIT.md) describes a constrained shuffle, but does not establish that it was the deployed implementation.

The candidate screen defines in range as **0.02–5.01 inclusive**, below and above as strict inequalities, and missing/nonfinite as unavailable. The published rule concerns intensity; applying the same thresholds to unpleasantness is an exploratory metadata comparison, not a claim that the authors used that screen for unpleasantness. The BIDS sidecar does not independently establish the `response_time` field's units or equivalence to the paper's timing variable. Table thresholds are applied to stored numbers; the paper's candidate rule uses seconds.

| Recorded first prompt | Episodes | Intensity RT below / in range / above / unavailable | Intensity in range | Unpleasantness RT below / in range / above / unavailable | Unpleasantness in range |
|---|---:|---:|---:|---:|---:|
| Intensity | 6,200 | 44 / 5,351 / 805 / 0 | 86.31% | 97 / 5,582 / 521 / 0 | 90.03% |
| Unpleasantness | 6,328 | 96 / 5,671 / 561 / 0 | 89.62% | 41 / 5,483 / 804 / 0 | 86.65% |

The pooled intensity-first minus unpleasantness-first intensity retention difference is **−3.31 percentage points**. Both rating types show lower in-range proportions when they are first, but this pattern is not evidence on why: design, recording, timeouts, participant differences and other variables are not separated. Episodes are not independent, families may be correlated and no standard error or significance test is asserted.

The full cross-tabulation, independent of order, is:

| Intensity status ↓ / unpleasantness status → | Below | In range | Above | Unavailable | Total |
|---|---:|---:|---:|---:|---:|
| Below | 84 | 48 | 8 | 0 | 140 |
| In range | 41 | 10,640 | 341 | 0 | 11,022 |
| Above | 13 | 377 | 976 | 0 | 1,366 |
| Unavailable | 0 | 0 | 0 | 0 | 0 |
| **Total** | **138** | **11,065** | **1,325** | **0** | **12,528** |

Among 394 people represented in both orders, the intensity in-range proportion is higher in intensity-first episodes for **68**, higher in unpleasantness-first episodes for **163**, and equal for **163**. Their unweighted mean within-person rate difference, intensity-first minus unpleasantness-first, is **−0.03246** (exactly −22805791/702486240). Each person's rate uses *all* their accepted episodes in that order in the denominator; no eligible person has unavailable intensity RT. This is a clustering-aware descriptive summary, not a causal estimate: observations within people and families remain dependent, and order is not verified as independently randomized.

## 2. Internal timing consistency

Each group—intensity-first and unpleasantness-first, for both rating types—has respectively 6,200 or 6,328 usable duration/RT pairs. In all four groups, **every duration exceeds its corresponding response time by more than 0.001**, with zero within 0.001, zero reversed, and zero unusable. Each group's first quartile, median and third quartile of `duration − response_time` are 0.5; the minimum and maximum across groups are approximately 0.4999999999999949 and 0.5000000000000051 (binary floating-point arithmetic).

The public candidate `get_overallratings.m` records an RT endpoint before a 0.5-second visual freeze. This numerical offset suggests a possible accounting relationship worth checking against actual conversion code and logs, but could arise through a different transformation. It does **not** prove that either BIDS field is identical to an original timestamp, that duration independently measured the freeze, that the candidate source actually ran, or that the CSV generator used either field. A constant difference is not independent measurement or device calibration.

## 3. Exact synthetic selection control

Independently of the participant metadata, suppose `O` and `U` are independent fair bits and each unit has `Y(0)=Y(1)=U`. Let the chance of retention be 3/4 when observed `O=Y`, and 1/4 otherwise. Then the full-population mean is 1/2 in each arm and the individual and average effects of O on Y are zero. Retention is exactly 1/2 in **both** arms, yet the retained means are 1/4 for O=0 and 3/4 for O=1, a selected contrast of **1/2**. The [receipt](verification/paingen_order_rt_selection.json) contains all eight rational joint probabilities and the [test](verification/paingen_order_rt_selection_test.py) checks their sum and the conditional means.

This constructed example shows that even *equal* marginal retention cannot by itself rule out selection bias. It is not a fitted model of these participants, an estimate of the bias here, or evidence that RT selection changes actual pain comparisons. Here the observed candidate intensity retention rates are in fact unequal across the recorded orders.

## 4. Consequences and next evidence gate

The result strengthens the reason to document the candidate RT selection and order as possible dependencies; it does not explain, fit, or resolve the **21 remaining** exported-mean discrepancies in the [partial-run audit](PAINGEN_PARTIAL_RUN_AND_REMAINING_MEAN_AUDIT.md). Those include three cells missing a relevant released run and 18 with both accepted. No specific omitted trials, author error or data-generation rule is identified. Before comparing a credible original pipeline against individual results, write a separate verification plan fixing provenance, data access and comparison rules in advance; prioritize author-provided versioned code, conversion specifications and inclusion records. Do not tune a filter to the discrepancies.

Pain intensity and unpleasantness are distinct reports; fear, anxiety, expectation, mood and valence are not interchangeable with either. The unmeasured physical interaction-preference quantity `q` is a different target. Prediction or metadata consistency would not establish phenomenal constitution or subject boundaries. C3, B4–B5/F2, B9/F3 and B10 remain open.

## 5. Reproduction

The [script](verification/paingen_order_rt_selection.py) verifies the pinned tree and archive SHA-256s and each event blob's Git SHA-1 through the existing ingestion function; it checks expected file, run, order and intensity-status totals and complete category accounting. The [aggregate receipt](verification/paingen_order_rt_selection.json) contains no identifiers or individual rows. Obtain the pinned artifacts and run:

```sh
gh api 'repos/OpenNeuroDatasets/ds004746/git/trees/8a38ee30b870373547676bf0d0638e16160472a1?recursive=1' > /tmp/paingen-v100-tree.json
curl -fsSL 'https://codeload.github.com/OpenNeuroDatasets/ds004746/tar.gz/8a38ee30b870373547676bf0d0638e16160472a1' -o /tmp/paingen-v100.tar.gz
python -m unittest discover -s verification -p 'paingen_order_rt_selection_test.py' -v
python verification/paingen_order_rt_selection.py --tree /tmp/paingen-v100-tree.json --archive /tmp/paingen-v100.tar.gz
```

The expected tree SHA-256 is `4a68281dc147b8436167466550ec5dedb4abb9fc86c27291a5a21fe60769799f`; archive SHA-256 is `b8a04bcc0130edcd65067ccdc98e6f480b403f6165417898f8292f48148a8be7`. A regenerated byte-different GitHub archive or JSON representation fails closed even if contents happen to be equivalent. Passing tests checks the stated computation, not source semantics or scientific interpretation.
