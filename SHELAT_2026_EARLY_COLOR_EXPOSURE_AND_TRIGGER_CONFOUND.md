# Early color exposure: a trigger confound and a bounded follow-up

## Bottom line

The simple first-versus-tenth colored-display comparison is **completely confounded by trigger type**: all 100 participants' first RGB displays were fixed-triggered, whereas their tenth displays were fast- or slow-triggered. Accuracy was lower at the tenth display, but this cannot be interpreted as an exposure or learning effect. An additional post-result comparison within each trigger type also does not identify learning: trigger assignment, elapsed time, stimulus category, omissions and response history remain important. Neither comparison establishes whether people used the color contingency.

This is a retrospective exploratory analysis, not the inaccessible experiment-2 registration, a preregistered test, or a replication of the authors' model. The [analysis plan](SHELAT_2026_COLOR_EXPOSURE_FOLLOWUP_PLAN.md) was written after the paper and earlier results were known but before the first comparison; the within-trigger analysis was added **after seeing** its complete trigger confound. It is explicitly post-result and unadjusted for multiple comparisons.

## Definitions and data

The preceding [display audit](SHELAT_2026_COLOR_CONTINGENCY_AND_WEBR_STATUS.md) verified that actual red, green or blue entries occur exclusively on rare-target displays in the recorded files. We ordered each participant's recorded SART rows by numeric block and trial, counting RGB displays regardless of trigger, response, accuracy, or RT. Both experiments have 50 participants with a first and tenth recorded RGB display; all these selected events fell in block 1. That is first and tenth **in this recorded SART dataset**, not necessarily a participant's first-ever encounter with a color: training preceded testing, and instructions or experience could already affect expectations. We do not know that an item was perceived.

We count each selected display's recorded binary accuracy as correct or incorrect; missing accuracy is reported separately. In the RGB events, response, RT and accuracy presence were jointly present or absent. No RT threshold is imposed: across all participants, two first events and no tenth events had RT below 200 ms. Thus these comparisons differ from the earlier published-model reconstruction, which excluded <200 ms responses and fixed triggers. Three-category marginal counts have all 50 or 100 occurrences in the denominator; the percentages among usable responses exclude missing. Paired analyses include only participants with usable accuracy at both events. Missingness may be informative.

## First versus tenth RGB display, regardless of trigger

| Group | First: correct / incorrect / missing | Tenth: correct / incorrect / missing | Paired n | Paired change, percentage points (approx. 95% CI) | Exact McNemar p |
|---|---:|---:|---:|---:|---:|
| Experiment 1 | 44 / 3 / 3 | 33 / 14 / 3 | 44 | −22.7 [−39.9, −5.5] | .0213 |
| Experiment 2 | 37 / 11 / 2 | 29 / 16 / 5 | 43 | −11.6 [−29.7, 6.4] | .3018 |
| Pooled | 81 / 14 / 5 | 62 / 30 / 8 | 87 | −17.2 [−29.5, −5.0] | .0107 |

The paired counts in order (incorrect→incorrect, incorrect→correct, correct→incorrect, correct→correct) are **0, 3, 13, 28** in experiment 1; **5, 5, 10, 23** in experiment 2; and **5, 8, 23, 51** pooled. The estimate is the average of tenth minus first binary accuracy among complete pairs; the approximate paired-t interval uses between-participant variability in those differences. McNemar's exact two-sided p value doubles the smaller binomial tail of discordant pairs. Intervals and p values use different procedures and need not have identical thresholds. Pooled values combine separate participants from both experiments, without adjusting for experiment. All p values are unadjusted, and differences in significance across experiments do not establish a between-experiment difference.

The dominant limitation is visible in the design: for the first event, fixed triggers = **50 and 50**; at the tenth, fast/slow = **30/20 and 37/13**. These are distinct triggering rules, not randomly assigned early and later exposures. The color mix also changes; in pooled first displays reward/selection/novel counts are 34/33/33, at tenth they are 37/27/36. First events are near the beginning of block 1 while tenth events occur later, with intervening trials and possible adaptation or fatigue. The analysis therefore tests a descriptive composite of time, trigger and stimulus context—not whether learning changed accuracy.

## Post-result comparisons within trigger

For each trigger separately we re-ranked that participant's RGB displays within that trigger and compared its first with its tenth. These are **not** the first and tenth overall RGB displays: other colored and neutral events can intervene. The rule reduces the categorical trigger confound, but fast/slow triggers are tied to response history; exposure rank is not randomized, and context, elapsed time and color can still differ. This analysis was added after the trigger confound became visible and produces nine more unadjusted comparisons. Full occurrence-level counts, including missingness and category mixes, are in the [aggregate JSON](verification/shelat_2026_color_exposure_followup.json).

| RGB trigger | Group | Paired n | Incorrect→correct / correct→incorrect | Tenth minus first, pp (approx. 95% CI) | Exact p |
|---|---|---:|---:|---:|---:|
| Fast | Exp. 1 | 47 | 6 / 10 | −8.5 [−25.6, 8.6] | .4545 |
| Fast | Exp. 2 | 47 | 3 / 11 | −17.0 [−32.4, −1.6] | .0574 |
| Fast | Pooled | 94 | 9 / 21 | −12.8 [−24.1, −1.4] | .0428 |
| Slow | Exp. 1 | 38 | 6 / 9 | −7.9 [−28.7, 12.9] | .6072 |
| Slow | Exp. 2 | 39 | 4 / 8 | −10.3 [−28.2, 7.6] | .3877 |
| Slow | Pooled | 77 | 10 / 17 | −9.1 [−22.5, 4.3] | .2478 |
| Fixed | Exp. 1 | 47 | 2 / 19 | −36.2 [−52.9, −19.5] | .00022 |
| Fixed | Exp. 2 | 44 | 5 / 11 | −13.6 [−31.7, 4.4] | .2101 |
| Fixed | Pooled | 91 | 7 / 30 | −25.3 [−37.5, −13.0] | .00019 |

Within-trigger results span different portions of the task. The pooled tenth fast event fell in block 1 for 85 participants and block 2 for 15; the tenth slow event fell in blocks 1/2/3 for 45/52/2, and one participant lacked it; the tenth fixed event fell in blocks 2/3/4 for 41/55/2, and two lacked it. First fixed events were all block 1; the other first-trigger events were nearly all block 1. Among the selected within-trigger events, four tenth fast events, two first fixed events and one tenth fixed event had RT below 200 ms; no selected slow event did. These are included. Missingness also differs: pooled first/tenth slow events had 16/7 missing accuracy, and the complete-pair count is 77. Any conclusions concern the selected events and response-complete participants, not an intention-to-treat learning effect.

The pooled fast paired-t interval excludes zero while the exact p is .0428; in experiment 2 the paired-t interval excludes zero but the exact p is .0574. This mismatch is expected for distinct approximate and discrete exact procedures, and neither result should be reinterpreted as decisive after the added exploratory analyses. A decline is not evidence *against* an individual learning a color warning: learning could be rapid or offset by other factors, and the task and selection of rare triggers evolve. Equally, an uncertain or null contrast would not prove stable learning or equivalence. More direct evidence would require independently varying RGB–rarity contingency and separating advance cueing from simultaneous visual effects, as proposed in the prior audit.

## Reproducibility and scope

[The script](verification/shelat_2026_color_exposure_followup.py) checks both archive SHA-256 hashes, joins observed data to trial structure, validates actual colors, triggered labels and counterbalanced orientation using the earlier audit's checks, sorts unique subject/block/trial keys, and writes aggregate results only. It does not read surveys or write participant-level records. The [tests](verification/shelat_2026_color_exposure_followup_test.py) check synthetic pair tables, missingness and exact McNemar arithmetic, saved confound counts, and opt-in recomputation from the archived data. All 16 focused tests and 45 selected project regression checks passed; these engineering checks do not establish psychological or philosophical claims. The numerical contrasts do not measure neural recoupling, awareness, phenomenal conjunction, subject identity or subject count.
