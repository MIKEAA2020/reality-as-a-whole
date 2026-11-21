# Post-result plan: conservative partial-run episode recovery

## Why this follow-up

The [run-completeness diagnostic](verification/paingen_remaining_mismatch_runs.json) shows that 14 of the 35 residual mismatch cells have a relevant event file rejected by our whole-run grammar, three have a relevant event file absent, and 18 have both relevant runs accepted. This follow-up was chosen **after** those counts were known; it is retrospective, not preregistered, and cannot be treated as an independent replication. We have not yet inspected the rejected files' event rows for salvage.

The whole-run audit rejects a run if it does not have exactly 32 rows, even if an episode inside it is intact. Test a predetermined alternative **only for rejected files**, without changing the previously accepted 1,566 runs. This is an additional candidate interpretation of incomplete files, not proof of actual stimulus delivery or authors' selection. Do not adapt to export means.

## Fixed recovery procedure

Reuse the exact digest-verified BIDS tree/archive, pinned author export, chronological sort, accepted run parser, candidate intensity RT screen, condition join and comparison tolerance. Verify the existing aggregate 4,400-cell 4,365/35 result before doing augmented comparisons. All operations remain in memory; write only aggregate run/episode/key counts, not identifiers or trial values.

In each rejected file independently:

1. Require columns `onset`, `duration`, `trial_type`, `int_rating`, `unp_rating`, `level` and `response_time`; require nonempty rows, all onsets finite and distinct, then sort by recorded onset. If any requirement fails, classify the entire file unusable, without guessing times or columns.
2. Divide rows into non-overlapping consecutive groups starting at each `warning_cue` and ending just before the next one, or at EOF. Count rows preceding the first cue as orphans; do not attach them to an episode. A group is a candidate only when its **entire** sequence is exactly four rows: warning cue, heat/press stimulus, one intensity event and one unpleasantness event in either order. No candidate subset may be selected from inside a malformed group.
3. A candidate's stimulus-row and rating-event values must both be valid and match for each dimension as in the prior audit; level must satisfy the prior exact modality mapping; the intensity-event `response_time` must be finite. Exclude invalid groups with reason counts. Only episodes passing all checks are added, retaining both ratings if `0.02 ≤ RT ≤ 5.01`, and neither otherwise. No imputation, changing run labels, condition mapping or RT cutoff is permitted. Duplicate person/run or condition source keys remain fatal.
4. Replay this recovery parser on every accepted run as a validation check: require all eight episodes be recovered, no orphans/rejections, and exact agreement with the existing parser's tuples. This does not establish correctness for incomplete files.
5. For each originally eligible cell, compare author means against the original RT-screened mean and the augmented mean with additional candidate pairs. Report the full paired 2×2 transition, marginal outcomes, counts and reasons for unavailable comparisons, and separately the subgroup of original mismatches by relevant-run completeness. Also report added candidate pair counts, rejected reasons, affected keys, and whether the two export-only keys become event-covered and have finite export outcomes. Stop if original result differs or an augmented key lacks a previous in-range trial. Never force a match or select a subset based on its match.

No intervention, full code replay or causation is inferred. A finite observed-mean agreement is compatible with different underlying trial selections; disagreement does not imply author error. Files with schema problems, orphan rows, malformed groups, missing BIDS runs, additional authors' exclusions or nontrivial transformations remain unresolved. The 18 original mismatch cells with two accepted relevant runs should not receive new episodes under the fixed join; if they change, stop on a logic error. If remaining findings suggest a new hypothesis, explicitly document it before further analysis.

## Post-result extension: formerly export-only means

The first run found that both previously export-only keys are now covered by in-range recovered episodes and have finite export pairs; it did not compare their means. Before computing that new comparison, add a narrowly defined **post-result** check: compare each of these two candidate means against the corresponding existing export pair at the same `10⁻¹⁰` tolerance and report only aggregate pair and marginal agreement counts. Do not seek alternate keys, add trials from other conditions, or combine these two with the original 4,400 denominator. The very small selected sample is a provenance check, not independent validation or evidence about participants.
