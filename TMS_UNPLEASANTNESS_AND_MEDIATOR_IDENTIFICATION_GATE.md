# rTMS, unpleasantness and mediator identification

**Decision: stop the proposed physical `q` comparison.** The Jin et al. experiment is closer to the desired design than a mood-only dataset: randomized real/sham stimulation, EEG and distinct first-person pain intensity and unpleasantness ratings. But the paper does not establish an independently calibrated preference for a designated physical interaction, nor does randomizing stimulation identify which post-treatment process caused any change. Its published results are already known; this is not a preregistered replication and no participant-level data were analyzed here. The exact synthetic control below clarifies the logical gap rather than modeling the study.

## What the study actually gives us

[Jin et al. (2026), *Prefrontal rTMS modulates dynamic expectancy processes to shape subsequent pain experience*](https://pmc.ncbi.nlm.nih.gov/articles/PMC13738117/) report a randomized, double-blind real/sham crossover with 36 recruited and 33 analyzed healthy young adults, sessions separated by seven days. Stimulation targeted F3 as a DLPFC proxy, not an individually neuronavigated site. EEG was recorded during pre- and post-stimulation expectation tasks; individually calibrated laser pulses were followed by separate ratings of intensity and unpleasantness. Each task had 60 trials divided among certain pain, uncertain pain and uncertain no-pain conditions. The figure caption specifies ratings following painful trials; the general text's wording around no-pain trials is less explicit, so their rating/event linkage needs clarification before an analysis.

The authors report greater real-minus-sham pre/post reduction in intensity (`F(1,32)=4.22`, FDR-adjusted `p=.048`) and unpleasantness (`F=5.46`, FDR `p=.048`). This is their randomized treatment comparison, conditional on the crossover design's assumptions (including adequate control of period, order and carryover and exclusions). It concerns the effect of the *whole stimulation protocol*, not a particular neural connection. Expected pain had raw `p=.026` but FDR `p=.078` in Table 3; the abstract's shorthand should not be read as FDR-significant for that outcome. In particular, contextual P2 and laser N1 treatment-by-context interactions had adjusted `p=.116` and `.076`, respectively; they do not establish context-specific effects at 0.05. These are published statistics, not our computations.

Expected pain, fear and anxiety were rated **retrospectively after the task**, whereas EEG features during cues precede the laser and stimulation precedes both. A later retrospective rating can summarize prior expectation but is not a direct contemporaneous, trial-by-trial mediator measurement; preceding pain and recall can affect it. The paper's serial analysis also uses a mean of intensity and unpleasantness in a pain outcome, which is not specific to unpleasantness. It is reasonable to regard its indirect effects as statistical associations under its model, not definitive causal pathways: the authors explicitly acknowledge this limitation. A randomized treatment does not randomize the mediator, and EEG's timing alone does not remove mediator–outcome confounding or treatment-induced confounding. Assumptions such as consistency, well-defined interventions, appropriate positivity, and no relevant mediator–outcome confounding (including treatment-induced confounding for standard natural effects), plus the applicable cross-world assumptions, require independent justification; stronger or alternative experimental designs may identify different interventional effects.

Pain intensity, unpleasantness, anxiety, expected pain, mood and valence are related but noninterchangeable. EEG components and their lags are not automatically the physical interaction preference `τ` or `q`. F3 stimulation is broad and may change multiple neural and peripheral processes, not selectively remove the designated channel.

## Exact control: identical randomized observations, different mediation

The [fixed plan](TMS_UNPLEASANTNESS_MEDIATOR_IDENTIFICATION_FIXED_PLAN.md) was written after the published Jin results were read and before this calculation. Let `U` be uniform on 0–3, `E` independent Bernoulli(1/4), and randomized binary `T` independent of both. Take `M0=1[U=0]`, `M1=1[U!=3]`, and observed `M=M_T`. Model A has `Y(t,m)=m XOR E`; model B has `Y(t,m)=M_t XOR E`, ignoring an intervention on `m`. Both have observed `Y=M XOR E`. All counterfactuals share the same latent `U,E` within a unit.

Exact probabilities of `(M,Y)` **conditional on each randomized treatment arm** are identical in both models, and all cells are positive:

| `T` | `(0,0)` | `(0,1)` | `(1,0)` | `(1,1)` |
|---|---:|---:|---:|---:|
| 0 | 9/16 | 3/16 | 1/16 | 3/16 |
| 1 | 3/16 | 1/16 | 3/16 | 9/16 |

| Exact estimand | A: mediator causes Y | B: mediator intervention has no effect |
|---|---:|---:|
| `E[Y(0,M0)]` | 3/8 | 3/8 |
| `E[Y(1,M1)]` | 5/8 | 5/8 |
| Total effect | 1/4 | 1/4 |
| Total natural indirect: `E[Y(1,M1)-Y(1,M0)]` | 1/4 | 0 |
| Pure natural direct: `E[Y(1,M0)-Y(0,M0)]` | 0 | 1/4 |
| `E[Y(1,1)] − E[Y(1,0)]` | 1/2 | 0 |

Thus every observed cell, and the total effect, agree, while the natural decomposition and intervention on the mediator disagree. In B, `U` is shared by mediator and outcome under fixed treatment, so mediator–outcome exchangeability is not guaranteed. Full *observed* cell support does not establish the stronger assumptions required to identify the effects. This shows that randomized treatment and full support alone are insufficient; it does not show that Jin's participants obey either construction or that their mediator cannot have a causal role. A separate, well-defined intervention on the mediator, or justified identification assumptions and appropriate measurements, could change the conclusion.

Reproduce with `python verification/tms_mediator_identification.py` and `python -m unittest discover -s verification -p 'tms_mediator_identification_test.py'`. The code exhaustively sums eight weighted latent states per treatment using rational arithmetic; four tests independently check hand-derived cells, totals, natural effects and controlled mediator intervention. The machine-readable [receipt](verification/tms_mediator_identification.json) records the results.

## Data availability and a useful next lead

For Jin, the PMC article's associated-data section lists a [supplementary DOCX](https://pmc.ncbi.nlm.nih.gov/articles/instance/13738117/bin/mmc1.docx); the inspected main text and associated-data section do not give an individual-data repository or a data-on-request statement. The DOCX was not inspected; targeted searches did not establish an accessible individual dataset. Thus availability is **unverified**, not proven unavailable. No EEG, participant data, supplementary data or individual outcomes were downloaded or analyzed for this study.

A **different** study, [Li et al. (2024)](https://www.nature.com/articles/s42003-024-07129-x), reports randomized M1/DLPFC/sham rTMS, EEG and separate pain intensity and unpleasantness reports on laser trials (120 assigned; 115 in Table 1). It reports no significant group difference in unpleasantness change immediately (`p=.83`) or at 60 minutes (`p=.16`); that is not evidence of equivalence. Its data-availability statement links [OSF project 5JGXY](https://osf.io/5jgxy/) and an article source-data spreadsheet. OSF metadata expose an `EEG` folder containing at least large ZIP files (e.g. `data1.zip`, 3,059,566,205 bytes, SHA-256 `f0879da8e0b67c7ea10096ceab7fa783af38fcdd527e4754ad0c76388d2bc8f3`, as reported by [OSF API](https://api.osf.io/v2/nodes/5jgxy/files/osfstorage/670e6d211b29952574a5e0d2/?page%5Bsize%5D=100)) and [analysis code metadata](https://api.osf.io/v2/nodes/5jgxy/files/osfstorage/670f96116ea8ed9b41b93a96/?page%5Bsize%5D=100). Neither file contents, trial linkage, completeness, downloadability nor license were verified. This is not Jin's data and its published findings were already seen. It is a potential physiological prediction resource, not evidence that `τ` is calibrated.

Another distinct lead, [Zhang et al. (2025)](https://www.nature.com/articles/s42003-025-08304-4), describes real/sham tDCS, capsaicin, block-level ratings including unpleasantness and EEG. Its [OSF project](https://osf.io/7gqwh/) lists a behavior spreadsheet and EEG archives in [metadata](https://api.osf.io/v2/nodes/7gqwh/files/osfstorage/6822b3946b16aa5cb8c4c074/?page%5Bsize%5D=100). Contents and pairing are uninspected. It likewise does not establish interaction preference. These leads are not independent replications of the present project.

## Gate to revisit

The subsequent [synaptic interaction preference and transport gate](SYNAPTIC_INTERACTION_PREFERENCE_AND_TRANSPORT_GATE.md) specifies one candidate neuronal pathway, a selective-gate sensitivity calculation and the remaining same-person transport barrier. It does not assign q to these datasets.

Before opening target outcomes for a new comparison, designate the physical variables and interaction, specify what the binary states mean and why the proposed binary model applies, and obtain a rating-independent calibration of the preferred relation `τ`, with uncertainty and evidence that the intervention distinguishes that interaction from other channels. Independently verify participant, trial/block and timing linkage to separately measured unpleasantness. Then fix the inclusion criteria, preprocessing, leakage controls, participants held out, primary metric and uncertainty procedure, and compare calibrated `q` with stimulus-only and conventional physiological models on the **same held-out cases**. If any prerequisite fails, stop rather than relabel an ERP, phase, microstate or correlation `q`. A predictive advantage alone would not establish phenomenal constitution.

The [prior Rao screen](NEURAL_PERTURBATION_FIRST_PERSON_Q_IDENTIFICATION_GATE.md) and [physical selectivity control](FOUR_SPIN_IMPERFECT_SELECTIVE_INTERVENTION_GATE.md) remain relevant; [PAINgen's 21 remaining discrepancies](PAINGEN_PARTIAL_RUN_AND_REMAINING_MEAN_AUDIT.md) remain unresolved pending original processing records. This work does not resolve C3, B4–B5/F2, B9/F3 or B10.
