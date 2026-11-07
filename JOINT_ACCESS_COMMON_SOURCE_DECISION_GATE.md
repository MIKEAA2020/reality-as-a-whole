# Joint access versus a common source: a decision gate

**Status: proposed, conditional operational test and exact finite counterexamples—not a completed experiment or a subject-count theorem.** This follows the [weak-coupling and partial-observation gate](WEAK_COUPLING_PARTIAL_OBSERVATION_SUBJECT_GATE.md) and the existing [report and experience calibration](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md). Its goal is to make the inference from two reported inputs to a shared experiential subject precise enough to fail.

## 1. The central distinction

A system's report can depend on two independently chosen inputs without those inputs belonging to one subject's experience. Successful comparison establishes a **physical information-access fact under suitable controls**; whether that information was simultaneously experienced by one subject is another claim.

We give:

1. two finite causal models with exactly the same joint input–report statistics in a baseline condition;
2. a test showing that a cue can be invisible to each one-input control yet reveal the entire joint answer;
3. a conditional information lower bound for a successful joint task;
4. an isolation intervention that separates the *specified physical models* only if demanding validity conditions hold; and
5. a separate, explicitly uncalibrated bridge from reports to a genuinely joint experience.

None of the numbers below is a human result. Failing to distinguish these two stipulated models would not establish a universal scientific impossibility, and distinguishing them would not establish phenomenal unity.

## 2. Prior art and empirical context

This is not a new discovery that agreement can arise from a common source: our [two-report analysis](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md) already exhibited shared errors, and conditional latent-class limitations are established by [Dawid and Skene](https://doi.org/10.2307/2346806) and [Hui and Walter](https://doi.org/10.2307/2530508). The information bound below is a standard binary consequence of Fano's inequality, not a new theorem; see [Cover and Thomas, *Elements of Information Theory*](https://doi.org/10.1002/047174882X). The contribution here is the combination of a **joint-input leakage counterexample, explicit physical rival gate and separate experiential error budget** in this project's decision chain.

In [a 2023 split-brain study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10667445/), the authors examined one patient's simultaneous and delayed cross-hemifield tasks, and discussed both their interpretation of conscious integration and the possibility of cross-cueing or timing differences. Those results are important constraints, not a direct implementation of the protocol below or a settled subject count. Residual pathways, visual fixation and changes in task timing can matter. The [COGITATE adversarial collaboration](https://doi.org/10.1038/s41586-025-08888-1) illustrates testing prespecified theory predictions; it did not test our models or settle the issue of joint subjecthood. Do not infer either one or two subjects from callosotomy alone.

## 3. Baseline: two operational rivals, identical reports

Generate two fresh, independent, uniformly random bits `X,Y`; neither bit is known to the device or participant before its generation. The task is to output the parity `T=X XOR Y`. Let two report channels output `P,Q`. The symbols are input and output records, not subject labels.

In an **open condition**, consider:

- **J — internal convergence:** a designated internal processor receives both inputs and outputs `W=T XOR E`, where `P(E=1)=1/4`. Both report channels copy `W`.
- **C — common-source leakage:** an alternative source receives `X` and, with probability `1/2`, also obtains `Y` through an unmonitored pathway. If it gets `Y`, it computes `T` correctly; otherwise it supplies an independent fair guess. Both report channels copy the same resulting `W`.

In both models, for every `x,y`,

```
P(P=Q=T | X=x,Y=y) = 3/4,
P(P=Q≠T | X=x,Y=y) = 1/4.
```

The **entire** joint distribution of `X,Y,P,Q` is identical, not merely the mean accuracy. Reports agree 100% while being correct 75%. The two models are physically distinct as specified, but baseline input–report data alone cannot identify which route produced the result. A sufficiently informative additional recording or intervention could distinguish them. In particular, the two candidate mechanisms might be differently plausible in a real system; observational equality does not assign equal prior probability.

J describes a physical information-convergence mechanism, not one genuine experiencer. C also uses a physical computation and a shared source, not a demonstrated alternative experiential ontology. Neither is a complete human theory.

## 4. The joint-leakage trap

Independent stimulus choices prevent a source that is genuinely independent of the choices from predicting their parity. But they do **not** prevent an unintended channel from carrying a joint function after generation. Let the leaked variable be

```
S = X XOR Y.
```

With independent uniform `X,Y`, `S` is statistically independent of `X` **alone** and independent of `Y` **alone**. Yet `S` is the correct parity on every trial and, together with `X`, determines `Y` exactly:

```
I(S;X)=I(S;Y)=0,       I(S;Y | X)=1 bit.
```

Thus testing only whether a cue correlates with either individual input can miss a perfectly informative joint cue. A physical origin of such leakage is not assumed here; the example is a warning about what the control must exclude. Include a prespecified full `2×2` input analysis and candidate interaction/decoding checks, not merely two separate main-effect tests. A statistically nonsignificant result or finite negative control does not by itself prove that all hidden or high-dimensional joint cues are absent; quantify what leak strength the instruments could have detected and what paths remain unmeasured.

## 5. What successful parity performance actually implies

Let `Z` be the **complete data physically available to the specified reporting mechanism**, including any routed signals, shared source, past information and its output record. Let the report `W` be determined by `X,Z` and any independent private randomness included in `Z`. Assume the test input `Y` remains an independent fair bit conditional on `X` before the relevant pathways operate, and count missing or unresolved parity outputs as failures. Let `A=P(W=X XOR Y)≥1/2`.

Since `W XOR X` estimates `Y`, the binary form of Fano's inequality gives

```
I(Y; Z | X) ≥ 1 − h₂(1−A)  bits,
```

where `h₂` is binary entropy. For example, `A=3/4` implies at least approximately `0.1887` bits. When a report is unresolved, a randomized guess for that trial has error no larger than the conservative counted failure rate, so the same lower bound applies. The bound concerns the full specified accessible transcript `Z`; it does **not** localize the path, prove that a particular brain region contained the information, constrain an unobserved channel's upper capacity, or establish experience. If stimulus randomization, pre-generation secrecy, input delivery or the transcript definition fails, the inference must be revised. Finite accuracy estimates need a one-sided uncertainty bound before substitution.

In particular, no real calibration follows from the illustrative `3/4`: it is the value chosen for the toy models. A credible upper bound on *unwanted* leakage is a different and considerably harder measurement problem than a lower bound on information present in all available outputs.

## 6. A physical route-isolation decision

Suppose a randomized intervention has an **open** condition as above and a **blocked** condition intended to interrupt the specified unwanted C pathway while preserving the nominated J convergence route. On blocked trials, define a model-specific validity event `G` containing all prerequisites needed for that model's prediction. It must include input delivery, lack of unwanted joint cues and preservation of task and reporting ability as relevant; do not define it merely as “no effect detected.”

For this diagnostic, suppose the complete rivals and independently supported gate bounds give:

```
C: P(G_C=0) ≤ η_C, and P(correct | G_C=1) ≤ 1/2;
J: P(G_J=0) ≤ η_J, and P(correct | G_J=1) ≥ 3/4.
```

The C conditional bound requires that `Y` remain fair and unavailable to C given its actually accessible inputs **and the validity selection**. Selecting valid trials in a way correlated with the hidden target can otherwise create bias. The J bound asserts preserved input access, processing and report behavior under the intervention; it is not implied by merely seeing activity in a nominated region. Count missing outcomes as incorrect and analyze all randomized blocked trials.

Writing `q_C,q_J` for their unconditional blocked accuracies, elementary conditioning gives

```
q_C ≤ 1/2 + η_C/2,
q_J ≥ (3/4)(1−η_J).
```

For illustrative `η_C=η_J=1/10`, the two permitted ranges are `q_C≤11/20=0.55` and `q_J≥27/40=0.675`. The verifier constructs endpoint mixtures; the numbers are **not** measured bounds on any actual intervention. If independently supported ranges overlap, this gate does not decide the rivals. If an observation lies outside both ranges, challenge the specified rival models, validity assumptions or measurements rather than declaring a winner by elimination.

For a simplified IID blocked-arm calculation, threshold the accuracy at `49/80=0.6125`, midway between these ranges. With `473` independent trials from one fixed model, Hoeffding bounds the probability of crossing that threshold by less than `0.025` for either specified hypothesis. This is a conservative illustration, not a clinical sample-size recommendation. It ignores the data and multiplicity needed to establish the gate bounds, input delivery, independence, participant effects and chosen model, and does not justify testing a rare patient on hundreds of trials. Real analyses must handle missing trials, participant clustering, temporal dependence, multiple comparisons and simultaneous uncertainty in all calibrated bounds. Randomization and preregistration do not themselves certify the isolation.

### Practical requirements, not a claim of feasibility

A research design should use safe, appropriate manipulations and avoid surgery or invasive procedures performed merely to isolate candidate consciousness pathways. It should:

1. Privately generate independent inputs after any shared pre-trial state, specify timing and use a full factorial design; conceal input bits and the answer from control displays, operators and report prompts until responses are locked.
2. Map the specific **candidate unwanted path**, its possible external and internal alternatives, and the physical intervention that purportedly changes it. Monitor fixation, timing, sensory spillover, motor and acoustic cues, residual neural routes and feedback where appropriate.
3. Assess whether the intervention changes the designated task, sensor, motor or report process. A signal that remains above threshold in a proxy area does not establish that the entire claimed J path and its content survive.
4. Preregister instrument sensitivity, bounded blind spots and a rule for missing/uncertain cases. Treat unknown gate error as unknown; cross-cue controls that do not constrain the joint `X,Y` function are inadequate.
5. Freeze the trial-level target, endpoints and competing predicted intervals before inspection; use held-out data and appropriate uncertainty analysis. If credible gate bounds cannot be justified, stop at **physical underdetermination** rather than treating chance performance as proof of disunity or success as proof of unity.

The “blocked” condition is a formal intervention requirement, **not an identified safe procedure that has already achieved pathway isolation in humans**. Especially in a brain, eliminating every alternate path while preserving the hypothesized joint path may prove infeasible. Noninvasive studies and existing clinical populations are possible sources of constraints, but clinical care, consent and participant burden take precedence over this toy sample calculation.

## 7. A separately stated bridge to joint experience

Let `E_J=1` mean that a specified subject **simultaneously experiences both target contents together in the same episode**, as distinct from inferring a parity answer, sequentially seeing the inputs, or unconscious information combination. A physical parity result is not the value of `E_J`. A standardized prompted report `R_J∈{0,1,⊥}` is evidence communicated by the participant, not an infallible direct readout; `⊥` includes uncertainty or nonresponse. Preserve the subject's first-person testimony while stating the uncertainty in translating it into external data.

Suppose a randomized audit of otherwise equivalent windows can estimate the potential report rate in the **prompt-possible context**, as in the existing [audit protocol](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md). Suppose further—independently of agreement with the parity output—that a same-condition bound

```
P(R_J misstates E_J or is unresolved) ≤ r
```

is warranted. Repeated, confident or mutually agreeing reports alone do not prove this bound; delays, memory, changes induced by intervention, and whether “together” has been understood all matter. No such universal `r` is known from this toy model.

For a *separate* pair of complete experiential hypotheses, suppose on their respective valid trials one predicts `P(E_J=1|G)=at least a` and the other `P(E_J=1|G)=at most b`. If their validity failure bounds are `η₁,η₀` and report-error bounds are `r₁,r₀`, then a binary potential report with unresolved coded conservatively obeys

```
positive hypothesis: P(R_J=1) ≥ (1−η₁)a − r₁;
negative hypothesis: P(R_J=1) ≤ b + η₀(1−b) + r₀.
```

For **illustration only**, `a=.9`, `b=.1`, `η₁=η₀=.1` and `r₁=r₀=.05` yield ranges `P(R_J=1)≥.76` versus `≤.24`. This numerical separation assumes all four premises; neither physical rival J/C above derives these experiential predictions, and no independently validated `r` or valid pathway intervention has been established here. If calibration is unavailable or these ranges overlap, an operational finding may still be valuable but the experiential inference remains open. A joint episode is also not automatically a full rule for subject persistence, overlap, quality or self-location measure.

## 8. Applying the gate to an actual published study

We inspected the published methods and results of [Pinto et al. (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10667445/), not its trial-level data. The article says raw data would be made available by the authors; no such data were retrieved for this analysis. The following distinction between what was reported and what the new gate requires is essential.

| Gate question | Published study | Assessment for this gate |
|---|---|---|
| Participants and condition | One patient with callosal surgery participated; the paper reports the anatomical history and cites clinical imaging sources. | A valuable case, not a randomized pathway-blocking comparison or population estimate. Surgery for clinical treatment is not an intervention to repeat for this project. |
| Simultaneous task | Experiment 1 presented two shapes, either within one hemifield or across fixation; it used randomized conditions, verbal same/different judgments and confidence ratings. | The authors report chance-level across-field matching. Failure to reject chance is not proof of no interhemispheric transfer, no experience or two subjects. |
| Sequential task | Experiment 2 presented a shape, then a question mark or `X`, with four randomized field combinations. On a question-mark trial the patient named the first shape; on an `X` trial he selected `X`. There were four blocks of 48 trials before exclusions. | This is an important conditional response task, but it is **not** the proposed independent-bits parity protocol. The second stimulus was sequential rather than simultaneous, and `X` trials need not use the first shape. |
| Reported performance | The authors report across-hemifield accuracy of **80.8% overall** and **68.7% on question-mark trials**; within-hemifield values were 74.2% and 58.7%, respectively. | The overall and question-mark figures answer different questions and must not be interchanged. We did not recalculate significance or uncertainty without the raw trial records and exact analysis. |
| Fixation and observer controls | Eye tracking monitored fixation; the paper describes exclusions for saccades and missing eye positions during specified stimulus windows. The experimenter could not see the stimulus screen. | These are meaningful controls. They do not alone provide a bound on every residual neural or bodily cue, especially during the interstimulus interval and subsequent response. This is not evidence that an unmeasured cue actually occurred. |
| Path and experience | The authors propose a deliberate route and discuss subcortical pathways and alternative cross-cueing; they report that their verbal-response design cannot distinguish the transferred representation's format. | The article does not establish this gate's `η_C`, `η_J` or numerical report–experience error `r`, nor isolate the nominated routes while preserving the rival. The authors' unity interpretation is a hypothesis, not an independently verified subject count. |

The 2023 finding constrains simple accounts that would predict chance performance in the particular delayed task. It does **not** implement the parity information bound in section 5: its second input is a task instruction, not an independent binary value with the parity response. Nor can one infer a bound on simultaneously experienced joint content from the reported question-mark accuracy or confidence ratings alone. Its authors discuss the timing/cross-cue alternative and consider it unlikely for reasons given in their paper; the present audit does not decide that dispute.

The smallest useful **data-first** follow-up is to obtain the trial-level stimuli, timing and eye-position/exclusion records, plus the complete response and confidence coding if available. First estimate the originally defined contrasts and their uncertainty, including relevant missingness and serial structure. Then inspect what information about timing and alternative routes the records actually contain. Such reanalysis cannot reconstruct an unrecorded channel, establish a report-to-experience error bound or retrospectively preregister a hypothesis. If adequate recording was not done, a prospective, participant-appropriate control would need to measure the specific suspected cue with sufficient sensitivity while preserving the original task. This is a proposal to assess feasibility, not an assurance that it can be done.

## 9. Reproduction and next step

Run `python verification/joint_access_common_source_gate.py`; its [receipt](verification/joint_access_common_source_gate.json) checks the exact baseline joint laws, joint-only leakage, interval endpoint witnesses, illustrative sample-bound arithmetic and hypothetical experience-report intervals. The general information inequality and conditional error bounds are analytic, not exhaustive computational or empirical results. The paper audit is based on the published article, not a replay of its raw data.

A subsequent [deeper source and task audit](SPLIT_BRAIN_DEEP_EVIDENCE_AND_TASK_AUDIT.md) identifies relevant prior work on one-sided strategies and action unity, and computes an idealized 75% one-input benchmark for the query task. This does not reanalyze patient data. The next step is to obtain and audit suitable trial records if available, or design a minimal prospective control for a **specified** candidate leak. Until the physical gate and independently anchored report–experience bridge have credible bounds, leave subject constitution unresolved. The frozen [v1 framework](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) is unchanged.
