# A concrete subject-to-report hypothesis: randomized audits of rivalry

## Decision

This is a proposed **human perceptual calibration and decision gate**, not an experiment we have run. Its target is a participant's experienced direction of motion during binocular rivalry, not the direction physically presented to an eye, correct guessing, or consciousness in general.

The specific hypothesis to test is:

> **H-audit:** for a preregistered population, rivalry stimulus and time window, a frozen eye-movement decoder and a randomly prompted retrospective report disagree on at most 10% of eligible windows, counting indeterminate/missing outputs as disagreements.

The 10% threshold is an illustrative preregistration choice, **not an observed result**. H-audit is empirically falsifiable using the randomly audited windows. It is only a claim about **decoder–report agreement**. To infer accuracy about the actual experience, a separate report-to-experience error bound is needed. No such bound is established here.

The useful theoretical step is an explicit bridge from those two errors and the physical-intervention validity rate to the existing rival hypotheses. It shows exactly what would have to be calibrated in the **same condition**, and when the data could separate the rivals without assuming the physical gate is directly observed on every trial.

## 1. Existing work—not a new experimental paradigm

In [Frässle et al. (2014)](https://doi.org/10.1523/JNEUROSCI.4403-13.2014), opposing motion stimuli produced rivalry; optokinetic nystagmus (OKN) and pupil measures tracked perceptual reports in active-report conditions, and the authors compared active versus passive viewing. They also found evidence that active reporting affected rivalry dynamics in their pupil-stimulus condition; their OKN-stimulus comparison was not significant. This is not a transferable 90% accuracy certificate for our proposed protocol.

[Naber et al. (2011)](https://doi.org/10.1371/journal.pone.0020910) used reflex measures and graded reports, documenting gradual transitions and effects of reporting on rivalry. [A no-report review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9130851/) discusses attention and other confounds; [Hesse and Tsao](https://elifesciences.org/articles/58360) note that OKN can persist when consciousness is diminished under low-dose ketamine in a cited animal study. Thus an observable eye response is not automatically the phenomenal state.

Randomized experience sampling is also established; for example, [Christoff et al.](https://doi.org/10.1073/pnas.0900234106) used unpredictable thought probes during fMRI. [A 2026 anticipation study](https://doi.org/10.3758/s13414-026-03228-5) reports that explicitly cued probe timing changes mind-wandering and task behavior; random timing may reduce some anticipation but does not remove the expectation of possible prompts. The present proposal applies these existing techniques to a **specific bridge and error budget**. It is not claimed to be the first randomized-probe rivalry experiment.

## 2. Declare the data and target

For each eligible preselected observation window, let:

- `E=1` mean the subject has the prespecified experiential target: for example, an experienced clearly rightward-moving grating in the declared visual region and interval. `E=0` means the target is not present; it does not mean there is no experience at all. These labels encode only a coarse content contrast, not the quality or existence of the subject.
- `Y∈{0,1,⊥}` be the frozen decoder's pre-prompt classification from eye tracking. `⊥` is unresolved or missing. Fix mapping of eye-motion direction to target in advance and counterbalance physical stimulus features across blocks.
- `R*∈{0,1,⊥}` be the report that **would** be elicited by the standardized prompt after that same window. Actual prompted reports provide first-person testimony communicated through a fallible physical channel. Allow “mixed,” “uncertain,” “no relevant percept,” and “I cannot remember”; specify in advance how these map to `0` or `⊥`.
- `G=1` mean all the independently specified prerequisites for the particular rival comparison are satisfied. For the existing orientation-maintenance contrast these include the valid target, preservation of the nominated physical basis, and removal of the specified additional distribution. `G` is not simply the absence of a detected neural difference.

The subject's own experience is valid first-person data; a verbal or motor report communicates evidence about it and can be mistaken, delayed, or incomplete. An eye-movement record is useful physical evidence, not an independent direct reading of phenomenal quality.

This motion-rivalry assay is a **new target**, not automatically the orientation assay or the specific FEF intervention in [the prior orientation gate](ORIENTATION_EXPERIENCE_CONSTITUTION_TEST.md). To use the earlier H_M1/H_D1 structure, its physical basis, competing extra distribution and target-preservation criterion must be reformulated and validated for this particular motion task. No such physical intervention is established here.

## 3. A randomized audit that measures report agreement in its own context

1. Use separate development data to select stimulus parameters, handle artifacts, train the OKN decoder, specify analysis windows and freeze the decoder and eligibility criteria. Include passive physical replay/control stimuli and record fixation/attention proxies; replay stimulus identity is not automatically subjective experience during rivalry.
2. During the test block, let the participant know that a report **might** be requested, but not which eligible window will be audited. At the end of each eligible window, choose audit `A=1` with a known nonzero fixed probability, using private randomization independent of that window's potential outcomes. Compute or lock `Y` from the pre-prompt window. The participant sees no cue identifying the audited window before its end.
3. On audited windows, prompt promptly for the percept **during that specific prior window**, including mixed/uncertain responses and confidence. Record `R`; on unaudited windows, do not request that window's report. The required delay, alignment, possible memory interference and post-window percept changes must be prespecified and analyzed.
4. Count `Y=⊥`, `R=⊥`, and missing requested reports as disagreement for the primary conservative agreement outcome. Do not select favorable windows using a post-prompt report. Pre-window physiological eligibility may still change the target population; report its coverage and exclusions.

Define `d=P(Y≠R* or an output is unresolved)` in this **prompt-possible context**. Under the stated randomization, consistency (`R=R*` when audited), no information about the current audit draw before the window, and correct handling of missingness, the audited-window disagreement estimates `d` for the eligible population. If audit probabilities vary with observed history, use the known probabilities and a prespecified weighted estimator, requiring positivity. Subject clustering, sequential dependence, limited audits and training/test separation matter for uncertainty.

H-audit is an operational claim `d≤0.10`: an appropriate confidence bound lying entirely above 0.10 challenges it; an upper bound below 0.10 supports this **report-agreement** claim in the defined context. Neither result alone measures `P(Y≠E)`.

This is not a pure no-report condition. Expectation of possible prompts and prior prompts can change attention, dominance and neural activity. The inference concerns the prompt-possible block; transport to a block where the participant knows no report will ever be requested is a separate, unvalidated assumption. The report is retrospective: a prompt may influence what is remembered or reconstructed even if it cannot change the earlier recorded `Y`.

## 4. From report agreement to experience: the missing independent premise

Let `r` be an independently warranted upper bound, **in the same eligible population and condition**, on the probability that the potential report fails to convey the target experience:

```
r ≥ P(R*≠E or R* is unresolved or E is outside the target coding).
```

Count a missing/uncertain report as an error for this conservative bound. Define decoder error similarly, treating unresolved outputs as errors. The elementary union bound gives

```
P(Y≠E or Y/E unresolved) ≤ min(1, d+r).
```

No conditional independence between report and decoder errors is required. An independent physical eye-tracking signal can lower uncertainty about reported content, but it does not itself warrant `r`. A person's first-person testimony should be taken seriously; converting it into a uniform numerical bound for all eligible windows, especially after a perturbation and a delay, requires further evidence and assumptions. Repeated reports, confidence, consistency across prompt delays and controls can inform credibility, but agreement among those fallible channels does **not by itself prove** a bound against the felt episode.

The [previous latent-model gate](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md) and the verifier here also demonstrate the opposite extreme: the same observed report–decoder distribution can coexist with a perfect or perfectly inverted hidden experience assignment if nothing constrains the psychophysical bridge. The inverted case is a mathematical countermodel, not a claim that people systematically misreport or that first-person knowledge is unreliable. Additional first-person information or a justified physical–phenomenal law can rule out that countermodel.

## 5. The physical–phenomenal separation gate

Suppose a *particular* physical comparison has been specified before data collection, with two scoped hypotheses:

- `M`: on `G=1` windows, the target experience is present (`E=1`).
- `D`: on `G=1` windows, the target experience is absent (`E=0`).

They need not be exhaustive, and this notation does not by itself instantiate the full [maintenance/distribution candidates](MAINTAINED_DISCLOSURE_CANDIDATE.md). For hypothesis `i`, suppose independently warranted **population** upper bounds are:

```
P(G=0) ≤ ηi;    P(Y≠R* or unresolved) ≤ di;
P(R*≠E or unresolved) ≤ ri.
```

Then, with `q_i=P(Y=1)`:

```
M:  q_M ≥ max[0, 1 − ηM − dM − rM]
D:  q_D ≤ min[1, ηD + dD + rD].
```

The proof is just the union bound: on an M trial, `Y` can fail to be positive only if the physical gate fails, the decoder disagrees with the potential report, or the report fails to convey `E`. On a D trial, a positive decoder output requires at least one of those failures. We do **not** assume the failure events are independent, nor do we substitute a confidence level for a trial failure rate. The result uses unconditional population error bounds, so it avoids requiring that `G` be observable on each individual window—but establishing a credible bound on `P(G=0)` remains essential.

A sufficient separation condition is

```
ηM + dM + rM + ηD + dD + rD < 1.
```

If all four measurement bounds share `d,r`, this is `ηM+ηD+2(d+r)<1`. Failure of this sufficient condition says only that **these bounds do not guarantee separation**, not that a different analysis or richer data cannot do so. The earlier [robust contrast](ROBUST_EXPERIENTIAL_CONTRAST.md) gives sharper interval results under different conditional error assumptions; one must not interchange the two sets of premises.

### Synthetic witness—not data

For each rival, set `η=0.10`, `d=0.08`, `r=0.05`. The bound gives

```
M: q_M ≥ 0.77;   D: q_D ≤ 0.23.
```

The verifier constructs valid finite distributions attaining these endpoints by making the three failure events disjoint. Randomly auditing a quarter of windows recovers `d=0.08` at the population level. These numbers are **not** estimates from the rivalry literature and do not establish that a safe intervention or an `r≤0.05` experiential anchor exists. In real data, use simultaneous confidence bounds for all estimated quantities, account for participant/trial dependence, and test the full predicted intervals; an observation outside both challenges the shared premises or both scoped rivals rather than forcing a winner.

## 6. A falsifiable decision sequence and stopping rule

1. **First decide H-audit.** Collect randomized-audit data and a held-out confidence interval for `d` in the prespecified task. Failure to meet 10% does not refute the participant's experience; it means this decoder/report combination has not met the chosen operational criterion.
2. **Then evaluate the experiential anchor.** State the independent empirical and theoretical support for a particular `r`, including retrospective timing, confidence, mixed percepts and altered conditions. If no defensible bound is available, leave `r` unknown; do not insert H-audit's observed `d` in its place.
3. **Then evaluate the physical gates.** A motion-specific M/D test must provide an intervention with credible bounds on source preservation, relevant distribution removal and valid target rates. The earlier [FEF orientation audit](V4_FEF_ORIENTATION_GATE.md) explains why merely stimulating a prefrontal region and seeing a stable average visual signal does not establish these gates.
4. **Only then compute the separating ranges.** If all bounds are independently supported and the ranges separate, run the prespecified comparison with uncertainty accounting. If any crucial bound is missing, the result may characterize reports or neural dynamics, but it cannot decide the subject/constitution hypotheses.

This is a test of a **specific report bridge and local experiential prediction**, not an experiment to identify subject number, prove a universal consciousness, infer a new physical collapse law, or explain why any phenomenal quality exists.

## Verification

Run [`verification/random_audit_experience_bridge.py`](verification/random_audit_experience_bridge.py). The [receipt](verification/random_audit_experience_bridge.json) checks the elementary inequality including unresolved cases, exact endpoint populations, audit randomization at four probabilities and physically indistinguishable opposite hidden assignments. It does not analyze actual participants or validate the assumed report or physical-gate error rates.
