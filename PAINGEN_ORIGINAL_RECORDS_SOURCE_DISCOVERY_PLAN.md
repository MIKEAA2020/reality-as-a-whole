# Fixed source-discovery plan: PAINgen processing records

## Scope and prior knowledge

The prior retrospective reconstruction has already identified 21 mismatched condition keys, including 18 with accepted relevant runs and three with a missing event run. The results and authors' exported condition means are known. We seek an independently documented trial-to-condition transformation or original task/behavior records, not a new filter selected to make those means agree. The `canlab/PainGen_DR` repository and `canlab/Paradigms_Public` PAINgen folder surfaced in a new metadata search; their trees and contents were not yet inspected when this plan was written. The previously pinned author analysis and BIDS releases remain the comparison sources.

## Bounded, privacy-preserving discovery

1. Pin current default-branch commit, license and recursive Git tree for each candidate; record truncation and public provenance. Inspect paths, file types, README and study/task descriptions and relevant source code, not individual outcome rows or source-log contents. Do not assume a similarly named project is the same experiment; identify modality, task design, intervention, dates and authorship.
2. For any potential processing code, identify its explicit inputs, exclusions, output names, scale transformations and applicable study/session, and whether it actually generates the pinned `merged_firstlvl_stim_betas_to_share.csv`. A task presentation script can document intended logging semantics without proving which version ran or generating the export. Check release identity and author links where available.
3. Stop prior to reading any individual data or changing the existing reconstruction. If source code points to a plausible original pipeline, first document evidence and separately fix an outcome-blind verification plan for paths, versions, hashes, key mapping, missingness, exact failure handling and aggregation. If no independently supported source exists, report the search boundary, continue to leave all 21 discrepancies unresolved, and specify precise source-record request. Never infer missing files are corrupt or conclude author error.

No new pain outcomes, MRI, behavioral trial rows or sensitive records should be committed. This provenance work does not measure the physical interaction preference or constitute a `q` test.
