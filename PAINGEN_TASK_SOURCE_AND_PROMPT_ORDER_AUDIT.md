# PAINgen: public task-source discovery and prompt-order control

## Decision

A newly located public [CANlab task folder](https://github.com/canlab/Paradigms_Public/tree/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms) materially improves our understanding of a **candidate task implementation**: it specifies separate intensity and unpleasantness prompts, their order generator, and named per-prompt response-time fields. But it does **not** establish the code actually run for each participant, the BIDS conversion, or the generation of the authors' condition-mean CSV. The **21 residual discrepancies remain unresolved**. No original behavioral MAT files, participant outcomes, BIDS event rows or MRI were inspected in this follow-up.

The [source-discovery plan](PAINGEN_ORIGINAL_RECORDS_SOURCE_DISCOVERY_PLAN.md) preceded tree and code inspection. The [combinatorial-control plan](PAINGEN_PROMPT_ORDER_SOURCE_CONTROL_PLAN.md) was fixed after inspecting the code and after prior aggregate BIDS order counts were known, but before the new exact calculation. This is retrospective provenance research, not a blinded replication.

## 1. What was found and pinned

The CANlab repository's root README describes folders as public experiment paradigms, and its folder name identifies Botvinik-Nezer, PAINGEN and Nature Communications. Its content resembles the published [thermal/mechanical placebo study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11255344/) and its [pinned author analysis repository](https://github.com/rotemb9/paingen-placebo-fmri-paper/tree/da46f2f9739ad2e9eeb9658711582be6357c1026), but neither naming nor resemblance proves a participant-specific executable version. The default-branch commit inspected was `89ec44cc82d09a6cddced6e7fcf2dd73c8a87281`; its Git root tree is `53433cf1bd3ec0d4c2371ca4b3e2e19aa2aaea8b`. The recursive API response was untruncated, with 18,338 entries; 4,996 blobs are under the candidate folder. The folder's recorded addition is commit `27f79392481511e22ff92581121902388fe9c372` dated 2025-11-03, after the 2024 paper. This is a release date, **not** the date the code was written or run.

The [aggregate receipt](verification/paingen_task_source_metadata.json) records the size, SHA-256 and Git blob identity of six inspected source files. Key links, all pinned to that commit:

- [test sequence generator](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/generate_ts_pain_test.m) — eight paired warning/stimulus slots, `TP` and `PP` modalities, two rating orders;
- [main task function](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/main.m) — records a PAINGEN version string, task timestamps and rating calls;
- [rating function](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/get_overallratings.m) and [prompt parser](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/parse_trial_sequence.m) — distinct labels and measurement logic.

Version ambiguity is concrete, not just theoretical. A separate [runner](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/RUN_cond_and_test.m) calls `generate_ts_pain_only_test`, whose corresponding [file](https://github.com/canlab/Paradigms_Public/blob/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281/2023_Botvinik_Nezer_PAINGEN_paradigms_NatureComms/generate_ts_pain_only_test.m) has a different declared function name and an expectation/intensity sequence rather than the two-prompt test generator. Which launcher, generator, version and local modifications were used for the paper's scanned runs is therefore not established by this folder alone.

A second repository, [canlab/PainGen_DR](https://github.com/canlab/PainGen_DR/tree/975aa6bf481e9d517a8dd8b1fb1531c56bb77130), describes itself as behavioral data for PainGen. Its pinned untruncated tree has eight MAT files; its 2019 commit message describes an upload for one subject. **Only metadata were inspected**, not file contents. The connection of those files to the published fMRI test runs, the 21 disputed keys, authorization for reuse, and their completeness are unverified. Do not assume the files are a solution or conflate them with the exported dataset. The API reports no recognized repository-level license; this does not determine any file's permissions.

## 2. What the candidate source says about responses

The parser contains the distinct prompts “How INTENSE was the pain?” and “How UNPLEASANT was the pain?” The test generator creates alternating warning and stimulus rows; its stimulus rows specify both prompts in an assigned order. In the main function, before each prompt it stores a type-specific timestamp and invokes `get_overallratings`. The latter stores normalized mouse position as a rating, and a type-specific `_RT` as `end_t−start_t`. The start timestamp is set before the rating function's screen/mouse setup; the loop ends on a button press or after its elapsed-time check reaches five seconds, then captures the endpoint **before** a 0.5-second visual freeze. Consequently this source's per-prompt RT is not defined as the later freeze duration, and its start is not simply established as the onset of the visible prompt. The elapsed-time check is in the loop, so its exact endpoint need not be exactly 5.000 s. `main.m` also stores a separate `overall_RT` around the full sequence of prompts and associated operations; it should not be silently substituted for either per-prompt RT.

This is a meaningful description of **these source files**, not verification of actual hardware timing or the BIDS `response_time` field. In particular, we have not found or checked the MAT→BIDS converter, per-run execution log, or original CSV mean/exclusion generator. The paper's published intensity-RT cutoff and the BIDS field's apparent usefulness remain consistent with this source, but that does not prove equality of those timing variables. The original [RT reconstruction](PAINGEN_RESPONSE_TIME_RULE_RECONSTRUCTION_AUDIT.md) is still a candidate reconstruction, and scale/rating fields or equality of means cannot authenticate a historical processing path.

## 3. A design consequence: run-level dependence

The candidate `generate_ts_pain_test.m` does **not** independently flip one fair coin for each of eight painful trials. It creates eight intensity-first and eight unpleasantness-first order vectors, uniformly permutes all 16 under an idealized permutation model, and assigns them to 16 alternating warning/pain rows. The warning rows have empty prompt labels; the eight painful rows have the two prompts. Therefore the count `K` of intensity-first painful rows has, **conditional on a uniform permutation and all eight rows being retained**,

```text
P(K=k) = C(8,k) C(8,8−k) / C(16,8),    k=0,...,8.
```

The exact enumeration of all 12,870 subsets gives:

| K | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Assignments | 1 | 64 | 784 | 3,136 | 4,900 | 3,136 | 784 | 64 | 1 |

`E[K]=4` and `Var(K)=16/15`, while `P(K=4)=490/1287≈0.3807`, `P(3≤K≤5)=1862/2145≈0.8681`, and `P(K=0 or 8)=1/6435≈0.0001554`. For comparison, eight independent fair coins would have variance 2 and all-same probability `1/128≈0.0078125`. The order is balanced **in expectation**, not necessarily exactly four each per run, and painful-trial assignments within a complete run are dependent under this design. The model treats the two categories of labeled vectors as exchangeable and `randperm` as uniform; it does not verify the deployed pseudorandom generator, seeds, omissions or actual assignments.

The earlier BIDS audit reported 6,200 intensity-first and 6,328 unpleasantness-first recorded episodes among accepted runs. Those counts were known before this follow-up; we do not test them against this idealized distribution or use this source to assert randomization in the actual scans. Selective missingness, cue/run exclusions, conditioning stage, differing code and within-person dependence require separate analysis. These facts do not establish that question order causes any difference in experience or ratings.

Run `python verification/paingen_prompt_order_control.py` and `python -m unittest discover -s verification -p 'paingen_prompt_order_control_test.py'`; see the [exact receipt](verification/paingen_prompt_order_control.json). The verifier enumerates position subsets rather than observed people. Three tests check the full hand-derived count table, normalization, symmetry, moments and probabilities.

## 4. Next evidence and reproduction

A targeted request to the study team would ask for: the version/hash and launcher actually used during scanned testing; the original task-data schema defining individual prompt timestamps and RT; the MAT-to-BIDS event conversion; the source code or documented formula producing the shared condition-mean CSV, with exclusion and condition mapping; and, for the three cases without a released relevant run, whether an authorized original run record exists. Ask about the other 18 residual cells without publishing identifiers; use a secure channel and respect consent and sharing restrictions. **No request has been sent.** Do not search for a new participant-specific filter based on the mismatches or treat file names alone as proof of identity.

Source identity can be checked without downloading any participant data: obtain the pinned [recursive tree](https://api.github.com/repos/canlab/Paradigms_Public/git/trees/89ec44cc82d09a6cddced6e7fcf2dd73c8a87281?recursive=1) and the six source blobs listed in the [receipt](verification/paingen_task_source_metadata.json) from the pinned GitHub blob API or commit paths, placing them under their listed basenames in a local directory. Then run `python verification/paingen_task_source_metadata.py --tree TREE --source-dir SOURCE_DIR` and `python -m unittest discover -s verification -p 'paingen_task_source_metadata_test.py'`. It verifies tree identity, untruncated response, sizes, Git SHA-1 blobs and selected source fragments; it is a source-integrity check, not independent verification of execution.

The [prior partial-run result](PAINGEN_PARTIAL_RUN_AND_REMAINING_MEAN_AUDIT.md) remains 4,379 matches and 21 mismatches among 4,400 eligible pairs. No change is made to trial selection or the author's data. This discovery does not identify a neural interaction preference, calibrate physical `q`, or resolve the physical–experiential bridge. C3, B4–B5/F2, B9/F3 and B10 remain open.
