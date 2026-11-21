# PAINgen residual discrepancies: partial-run recovery and its limits

## Result

**Later source follow-up:** the [task-source and prompt-order audit](PAINGEN_TASK_SOURCE_AND_PROMPT_ORDER_AUDIT.md) locates a public candidate PAINgen task implementation and derives its idealized prompt-order distribution. It identifies named per-prompt timing fields but does not verify the executed version, BIDS conversion or original condition-mean export; all 21 discrepancies remain open.

After applying the published response-time rule as a candidate, **35 of 4,400** overlapping finite paired means still differed from the author export. A further retrospective check found:

- **14** had one relevant event run rejected by our strict whole-run grammar. A predeclared *within-this-follow-up* cue-bounded recovery rule finds intact candidate episodes in those rejected files. Adding the in-range recovered pairs makes all 14 match both exported means, with **no regressions** among the 4,365 prior matches.
- **Three** have a relevant run absent from the pinned event-file release and remain mismatched.
- **Eighteen** have both relevant runs accepted and remain mismatched; these 18 keys involve two people. Their cause is not established.

Thus the augmented reconstruction matches **4,379 of the original 4,400** eligible overlapping pairs; **21** remain mismatched. In a separate post-result check, the same recovery also supplies candidates for both previously export-only keys, and both pairs of recovered means agree with the export. They are *not* included in the original 4,400 denominator.

This is encouraging evidence about how the released files and condition export may relate. It is **not** confirmation of the authors' original trial-inclusion decisions, absent runs, timing variable, raw hardware, or original CSV-generation code. Both releases have shared provenance; numerical agreement can have more than one processing history. None of this identifies a physical mismatch `q` or validates an experiential constitution.

## 1. Why inspect rejected runs?

The preceding [RT audit](PAINGEN_RESPONSE_TIME_RULE_RECONSTRUCTION_AUDIT.md) used the paper's intensity-response-time exclusion against a candidate BIDS timing field; it reproduced 585 of 620 originally mismatched pairs, leaving 35. A still earlier conservative grammar rejected any run without exactly 32 event rows, even if it included some intact episodes. The new [run-completeness plan](PAINGEN_REMAINING_MISMATCH_RUN_COMPLETENESS_PLAN.md) was written before its strata were calculated, but after the residual mismatches were known. It defines relevant runs as `01`/`04` for control and `02`/`03` for placebo, using the existing condition mapping.

| Relevant event files under original whole-run screen | Screened paired match | Screened paired mismatch | Total eligible cells |
|---|---:|---:|---:|
| Both accepted | 4,322 | 18 | 4,340 |
| One accepted, one present but rejected | 28 | 14 | 42 |
| One accepted, one absent | 15 | 3 | 18 |
| **Total** | **4,365** | **35** | **4,400** |

These are condition keys, not independent people. The mismatch categories involve respectively two, five and one distinct people; people can contribute to multiple strata, so these counts must not be added. Complete relevant runs do not guarantee correctness of trial-to-condition mapping or the source transformation. An absent file means absent from the pinned event tree, not proven absence of experimental data. Nor does a rejected file imply a bad scan or invalid trial.

## 2. Conservative cue-bounded recovery

After seeing the table above but before inspecting the rejected rows, we wrote the [partial-run recovery plan](PAINGEN_PARTIAL_RUN_EPISODE_SALVAGE_PLAN.md). This is explicitly **post-result and retrospective**. We sort by recorded onset, split into nonoverlapping groups bounded by warning cues, and retain a group only if its *entire* recorded sequence contains the cue, stimulus and two distinct rating events, its stimulus/rating values agree, the prior level mapping is valid, and the intensity-event RT is finite. We do not extract a favorable subsequence from a malformed group. Both ratings are retained only when that RT lies within `0.02–5.01` seconds inclusive.

As a parser check, replaying the new rule on all **1,566 previously accepted runs** reproduces their **12,528** episode tuples exactly; this is an internal check, not validation of rejected-run pairing or real stimulus delivery. Of the eight earlier rejected files, seven fail the original row-count requirement and the eighth lacks required schema. The seven yield **21** intact candidate groups in total: **18** with in-range intensity RT and three above 5.01 seconds. The schema-deficient file yields no candidates. No incomplete, orphan or invalid group was observed under this particular screen; the absence of such a group is not proof the files represent complete runs.

| Original RT-screened pair | Augmented pair matches | Augmented pair mismatches | Total |
|---|---:|---:|---:|
| Matched | 4,365 | 0 | 4,365 |
| Mismatched | 14 | 21 | 35 |
| **Total** | **4,379** | **21** | **4,400** |

Exactly 14 originally eligible cells receive an added in-range episode; those are the 14 mismatch-to-match cases. The 18 complete-run mismatches correctly receive none, and the three absent-run mismatches cannot gain an episode from a missing file. The unresolved count for this eligible comparison is zero. For individual dimensions, intensity mismatches fall from 35 to 21 and unpleasantness mismatches from 33 to 20; both dimensions have zero match-to-mismatch transitions. A mean match by itself does not prove which trials the authors used.

Of the 18 added in-range candidate episodes, two cover the two previously export-only keys; a **second post-result extension**, documented in the plan before checking those means, found that both recovered pairs agree with their respective export pairs to `10⁻¹⁰`. The other two in-range candidates need not produce additional originally eligible changed cells; categories are not necessarily one episode per key. The prior 307 export-missing overlapping keys were not imputed or included in the primary comparison. The receipt records counts rather than individual keys.

## 3. What is still needed

This narrows the provenance gap further, but not all of it. For the 21 remaining cells, start with the authors' actual trial-to-condition inclusion record, task logs and code that generated the CSV; check whether the three missing-file cases have usable records elsewhere, and whether the 18 complete-run cases reflect mapping, data versions, missing source trials, transformations, or some other cause. These are alternative explanations, **not findings**. Do not search other participants' records or swap labels until an independently justified source rule is available. No error by the authors is established.

Candidate RT semantics still lack independent validation: the task sidecar does not define that column or its units, and the published paper does not identify the specific CSV-generating code. Partial-run reconstruction is likewise based on the shared event export rather than a separate audit trail. The authors' exported condition-mean prediction results should still be described as such, not as independent physiological or phenomenal replication.

The existing [pain/aversion readiness gate](PAIN_AVERSION_CROSS_MODALITY_EXPERIENTIAL_READINESS_GATE.md) describes a possible continuous-rating/EEG source, but its signals and ratings have not been checked and its fixed schedule and task-specific targets limit inference. More importantly, observed EEG phase lags are not independently identified interaction preferences: the [phase-lag gate](OBSERVED_PHASE_LAGS_VERSUS_PHYSICAL_FRUSTRATION_GATE.md) constructs both false-positive and false-negative controls. A physical `q` assay still needs an independently specified channel model and suitable calibration or interventions. B4–B5/F2, B9/F3, B10 and C3 remain open.

## 4. Reproduction and scope

Reuse the pinned sources and commands in the [RT audit](PAINGEN_RESPONSE_TIME_RULE_RECONSTRUCTION_AUDIT.md). The [run-completeness script](verification/paingen_remaining_mismatch_runs.py), [partial-recovery script](verification/paingen_partial_run_salvage.py), their tests and their aggregate [completeness](verification/paingen_remaining_mismatch_runs.json) and [recovery](verification/paingen_partial_run_salvage.json) receipts include input digests and stop checks. For example:

```sh
PYTHONPATH=verification python -m unittest -v paingen_remaining_mismatch_runs_test paingen_partial_run_salvage_test
PYTHONPATH=verification python verification/paingen_remaining_mismatch_runs.py --tree TREE --archive ARCHIVE
PYTHONPATH=verification python verification/paingen_partial_run_salvage.py --tree TREE --archive ARCHIVE
```

Both scripts read the pinned behavioral export from the authors' repository unless `--behavior PATH` supplies the exact file. The recovery script checks all event blobs, prior counts, pairing agreement and accepted-run replay before reporting. Outputs contain aggregate counts only, not identifiers or trial rows. Software checks do not independently establish the historical experiment or interpretive claims.
