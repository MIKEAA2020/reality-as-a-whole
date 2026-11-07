# Can neural activation duration supply the missing episode clock?

## Direct result

The inspected primary analysis code estimates **stimulus-duration tracking**, not an intrinsic phenomenal episode boundary. Its threshold, smoothing, anatomical selection, and scoring tolerance are explicit analysis choices. Those choices can be legitimate for their intended test, but their existence does not identify the workspace or its phenomenal clock.

A stronger candidate should separate:

    intrinsic process / candidate boundary law
        -> neural signal
        -> recording and analysis transformation
        -> evidence about that boundary.

The positive advance is an explicit measurement requirement, a primary-code audit, and a worked mathematical example of how to correct a measurement-induced timing shift. No participant data or published result has been reproduced.

## 1. The tempting hypothesis to test

Call B0 the proposal:

> The end of a phenomenal episode is the time when a selected neural channel falls below its activation threshold.

B0 is a hypothesis considered here, **not a claim attributed to the COGITATE authors**. Their documented analysis tests sustained activation relative to stimulus duration, with theoretical predictions in view. It does not announce a completed Gamma law.

B0 would be attractive if the threshold identified an independently justified constitutive transition. It is not justified merely because an analysis returns a crossing time.

## 2. Primary materials and scope

Selected sources are pinned to commit

    e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a

of `Cogitate-consortium/cogitate-msp1`. The source tree and exact files were obtained through the GitHub API. Snapshots and SHA256 records are in [the source manifest](sources/external/cogitate_analysis/provenance.json).

Inspected sources:

- [Activation analysis README](https://github.com/Cogitate-consortium/cogitate-msp1/blob/e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a/coglib/ieeg/Experiment1ActivationAnalysis/README.md), all 121 logical lines.
- [Duration tracking master](https://github.com/Cogitate-consortium/cogitate-msp1/blob/e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a/coglib/ieeg/Experiment1ActivationAnalysis/duration_tracking_master.py), all 229 lines.
- [Tracking helper](https://github.com/Cogitate-consortium/cogitate-msp1/blob/e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a/coglib/ieeg/Experiment1ActivationAnalysis/activation_analysis_helper_function.py#L88-L207), specifically its imports, the tracking function, and the smoothing wrapper—not every function in the file.
- [Task-irrelevant face configuration](https://github.com/Cogitate-consortium/cogitate-msp1/blob/e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a/coglib/ieeg/Experiment1ActivationAnalysis/duration_tracking_config/duration_tracking_high_gamma_iit_roi_face_ti.json) and [task-relevant non-target face configuration](https://github.com/Cogitate-consortium/cogitate-msp1/blob/e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a/coglib/ieeg/Experiment1ActivationAnalysis/duration_tracking_config/duration_tracking_high_gamma_iit_roi_face_tr.json), all 100 lines each.

No third-party neural analysis was executed. Dependencies and participant recordings were not downloaded. No primary result paper was inspected. These snapshots do not establish which exact pipeline version underlies every final publication result.

## 3. What these configurations actually specify

Both inspected configurations select:

- a high-gamma signal label;
- an anatomical ROI list under the key `iit`;
- 1000-ms and 1500-ms face trials, with task roles differing between the files;
- a 300-ms moving-average window;
- a threshold calibration condition of 1500-ms trials;
- a baseline window of -0.5 to -0.2 seconds;
- an activation window of 1.2 to 1.5 seconds;
- `fast_track: true`;
- an allowed tracking error of 0.15 seconds;
- 1000 permutations and no configured FDR method.

These are properties of the selected source files, not universal properties of the entire study. Their paths point to phase-2 data. The README's illustrative permutation count is not substituted for the actual configuration value.

A predeclared ROI or threshold is not inherently an error or circular test. It can implement a legitimate theory prediction. But selecting electrodes within a theory-associated ROI does not discover that ROI as the unique boundary of a subject.

## 4. What the implementation computes

The master script loads condition-selected, ROI-selected epochs, optionally smooths them, and calls the helper. It then computes shuffled-label comparisons and writes tracking and statistics files. Those output files were not retrieved or recomputed here.

In the inspected fast-track branch, the helper estimates one threshold for a channel from the baseline and activation-window data of the specified threshold condition. It searches the post-onset time samples for the first value below threshold and compares that sample time with the duration label. The proportion of trials whose error falls within the tolerance becomes the tracking statistic.

The helper also contains a leave-one-trial-out threshold branch, but the selected files enable the fast-track branch. Threshold calibration, held-out validation, and the empirical target should therefore be distinguished before any constitutive inference.

This statistic addresses a relation between neural activity and stimulus duration. It does not, by itself, establish:

- that the channel is the content-realizing process;
- that its amplitude defines phenomenal presence;
- that a crossing ends an episode rather than changes one component;
- that co-active channels belong to one subject;
- that the stimulus duration equals an independently identified phenomenal duration on every trial.

## 5. A source-level edge case, narrowly interpreted

The helper uses `np.argmax(signal < threshold)` without a separately represented no-crossing case in the inspected function. For a nonempty Boolean mask, first-maximum gives index zero both when every entry is false and when the first entry is true.

Thus these observations can share a returned index:

- no below-threshold sample occurs in the observation window;
- the first sample is already below threshold.

They do not denote the same physical transition. The first can require a censored or absent-crossing interpretation rather than an observed drop at time zero.

[The static verification script](verification/cogitate_analysis_audit.py) checks this Boolean-semantic witness without importing or executing the neural analysis. It does **not** show that the edge case occurs in the participant records, affects significance, or invalidates a publication. In these 1-second and 1.5-second conditions, an imputed zero crossing and a properly classified no-tracking event may both fail the duration-tolerance criterion. Their distinction nevertheless matters if one tries to interpret the returned sample as an actual episode endpoint.

## 6. A precise measurement example: apparent clock shifts

Consider an illustrative raw signal

    s(t) = 1 for 0 <= t < D, and 0 otherwise.

This is a mathematical witness, not participant data. Assume D >= w > 0. A trailing moving average of width w is

    a_w(t) = (1/w) integral from t-w to t of s(u) du.

During its falling segment, D <= t <= D+w,

    a_w(t) = 1 - (t-D)/w.

Its half-height time is therefore

    t_half = D + w/2.

The raw signal's endpoint is D. Changing only the downstream smoothing width changes the estimated half-height time, while the source process remains unchanged.

For D=1 second and w=0.3 seconds, the reported crossing would be 1.15 seconds. That is not evidence of an extra 150 ms of experience.

**This is not a claim that the imported COGITATE moving-average routine uses this trailing convention.** Its implementation has not been inspected here. The example establishes the general need for a timing transformation model. A centered convention, another threshold, or another filter can have a different timing relation.

The constructive correction is explicit:

    D = t_half - w/2

under this known observation model. Measurement dependence is therefore not a reason to abandon neural explanation. It is a reason to separate the source property from its measured representation, exactly as the SR analogy requires.

## 7. The improved model form

Let P be the actual process and B(P) its proposed intrinsic boundary structure. Let S(P) be the neural signal and A the downstream acquisition/analysis operator. Then

    y_A = A[S(P)] + observation noise.

An estimator E_A should infer B(P), with its uncertainty, from y_A using a warranted relation between the signal and the boundary. It should not simply define B(P) to equal whichever time E_A returns.

If two passive analysis operators produce different apparent crossing times, their correct measurement transformations should refer back to the same underlying boundary, where that boundary is identifiable. Inverse problems can be nonunique; preserving uncertainty is then required.

For a neural constitutive hypothesis, the new load-bearing work is to identify B from physical organization—such as a proposed change in a content-maintaining causal mode—and justify why that transition is phenomenally significant. No such B is established by the inspected threshold analysis.

## 8. A specific next comparison, not an empirical result

A candidate boundary rule could be calibrated on a predeclared subset and tested on held-out durations, identities, and task roles. Its law parameters should not be freely refitted for every condition merely to track stimulus offset. Actual changes in the neural state are allowed; state-dependent predictions must follow the same declared law.

For example, a rule trained on longer task-irrelevant trials could be evaluated on shorter and task-relevant non-target conditions, with an independently justified phenomenal evidence model. This is a proposed comparison; these source files were not run and do not establish its outcome.

It would help distinguish whether the selected feature tracks:

- sensory input persistence;
- a content-maintaining state;
- task coordination;
- motor/report processes.

Success would still not establish togetherness. It would justify a candidate temporal/content constraint that a broader Gamma–chi theory must accommodate. Joint decoding, anatomical adjacency, or simultaneous threshold crossings cannot substitute for incidence evidence.

## 9. Decision on the candidate

**Do not adopt B0 as the episode law.** The present materials do not identify the analysis threshold with an intrinsic constitutive boundary. This is an insufficiency judgment about the proposed inference, not an empirical refutation of every threshold or neural-transition theory.

Retain the stronger direction: an independently specified causal transition, a calibrated observation model, and held-out phenomenal constraints. Calibration itself is legitimate—SR also requires measured parameters—but cannot be mistaken for an independent identity proof.

This also constrains the current recurrent-access hypothesis: W and its interval cannot be obtained simply by taking whichever ROI and smoothed duration tracker the analysis supplies. They require an intrinsic selection argument and independent phenomenal warrant.

## 10. Verification and current status

The source hashes and configuration values are checked by [the static audit](verification/cogitate_analysis_audit.py); its [diagnostics](verification/cogitate_analysis_audit.json) record the selected fields, function ranges, and edge-case witness. Reading coverage is specified in the source manifest. The original third-party files remain unchanged and their license is retained.

The substantive gain is a clearer measurement model and a concrete primary-code constraint on the proposed episode clock. No full workspace selector, Gamma, chi, empirical result, or necessary-foundation law has been discovered. No new synthetic consciousness model is added, and the established independent research count remains 1,149 tests across 43 folders.

Related: [recurrent-access candidate](WORKSPACE_TOGETHERNESS_CANDIDATE.md), [constitution programme](CONSTITUTION_RESEARCH_PROGRAMME.md), [protocol-independent geometry constraint](research/constitutive_geometry/REPORT.md).
