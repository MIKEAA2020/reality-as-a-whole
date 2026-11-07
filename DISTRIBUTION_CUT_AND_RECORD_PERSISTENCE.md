# Cutting a distribution channel is not erasing its records

## Decision

A more practical *in-principle* substitute for recording every downstream consumer is to certify a complete bottleneck: bound the content-dependent signal crossing it **together with any content already available on the consumer side**. Under a stated causal factorization, this bounds the entire downstream system, even parts not individually recorded. The price is a strong, independently justified boundary assumption. For the human extrastriate–frontal candidate, that assumption has not been established.

Applying this idea to the **existing** realized-workspace implementation reveals a concrete complication: turning off its distribution gate does not erase consumer memory written before the cut. If the direct report is enabled, it also continues to transmit current content despite the gate being off. Both are straightforward consequences of the actual implementation, not new neuroscience. Their significance depends on which consumers the frozen P4 hypothesis specifies; they do not refute the restricted comparison that explicitly excludes the report.

## 1. A sufficient boundary certificate

This uses standard data-processing and total-variation contraction, not a novel theorem; see [Polyanskiy and Wu, *Strong data-processing inequalities for channels and Bayesian networks*](https://arxiv.org/abs/1508.06025). The following application makes the necessary assumptions explicit.

Compare two **fully specified preparation/intervention regimes** `c=0,1` over a declared interval. They may correspond to randomized earlier stimulus conditions, or to a validated intervention on a source. Let:

- `E` be the consumer-side initial state and other shared resources or background variables relevant over the interval, including any prior content records or side information;
- `B` be the complete content-bearing boundary transcript allowed into the nominated downstream system during the interval;
- `D` be the **joint downstream state or output** whose dependence on the contrast is to be bounded, including interactions between consumers.

Assume the two regime distributions have the same downstream stochastic kernel `L`:

```
P_c(E,B,D) = μ_c(E) K_c(B | E) L(D | B,E),    c = 0,1.
```

This is a physical causal/coverage assumption, not a consequence of observing a few sensors. The transcript must cover all relevant incoming routes; E must include relevant initial records, shared noise and accessible side information. In a recurrent system B must be an adequate *whole-interval transcript* and the common-kernel factorization must actually be justified: conditioning on a partial or feedback-contaminated transcript does not establish it. Including independent downstream random seeds in E is one possible way of specifying a model, not a guarantee that the necessary variables are observable.

Write `η = TV(μ_0, μ_1)` and `δ = E_{E ~ μ_0}[TV(K_0(.|E), K_1(.|E))]`; on a zero-probability conditioning row choose a valid conditional version. Then

```
TV(P_0^D, P_1^D) ≤ TV(P_0^{E,B}, P_1^{E,B}) ≤ min(1, η + δ).
```

The first inequality is the ordinary contraction of TV through the common kernel L; the second follows by inserting `μ_0(E) K_1(B|E)` and using the triangle inequality. Consequently, a scientifically justified `η + δ ≤ ε` bounds the complete nominated joint downstream effect by ε **without separately measuring every member of D**. This is sufficient, not necessary, and it is no stronger than the evidence for the factorization and the two upper bounds. For finite samples, the bounds must include uncertainty and any simultaneous coverage requirement.

Why both terms? An unread message B can have zero *marginal* content dependence while being completely informative given an available key E, as in the [consumer-coverage counterexample](CONSUMER_COVERAGE_IDENTIFIABILITY.md). There δ=1 in the fully retained channel even though the marginal B effect is zero. Conversely, a perfect boundary cut has δ=0 but if an old downstream record depends on the target, η can be 1. The bound does not assume either problem away.

This is a criterion for the **specified contrast**. Bounding two content values does not bound all other contents, all hidden forms of representation, or the consumer's full physical powers. Extending it requires a declared set of interventions, intervals and suprema. It is also not a phenomenal test and cannot establish P3 or P6.

## 2. Test the actual workspace model

The [existing workspace](research/realized_workspace/model.py) has a `distribute` gate, consumer memory, action and comparison, and a direct report. Under `distribute=False`, the current workspace is not sent through the gated consumer route, but the `step` function explicitly retains the old memory when no content is available. The report instead reads current workspace content directly when `report=True`.

The [verifier](verification/boundary_cut_workspace.py) uses the actual implementation, not a replacement model:

1. **Fixed previous consumer state, report off:** for both visual and auditory bit values, all five possible prior memory states, three feedback settings, two task rules and two targets (120 cases), force current bit 0 versus 1 with distribution disabled. The checked consumer signature—memory, action, comparison and report—is identical. This establishes no instantaneous dependence on the current forced bit in those *specific model outputs and cases*.
2. **Same previous state, report on:** the two current bits produce different direct reports in every case. Thus a boundary claiming to include that report cannot treat the distribution gate as the only exit. If H_D1 concerns memory/action/comparison rather than direct report, excluding report is a legitimate narrower contrast, but one must still address whether it constitutes an equivalent additional distribution under the stated P4 scope and whether P6 is valid.
3. **Prior record retained:** first write visual bit 0 or 1 into consumer memory through the enabled gate; then disable distribution and report. In both cases the memory retains the respective bit. There is no new action or comparison, yet the old consumer record distinguishes the prior contents perfectly. Cutting present transmission is not the same as removing a pre-existing distributed record.
4. **Current-source intervention:** after writing bit 0, forcing the current workspace to bit 1 leaves memory at 0. Therefore the old record is not evidence of a *new* current source-to-memory causal influence in the cut interval; it is evidence that the prior content persists downstream. Which of these P4 requires depends on the frozen target, history and interval.

Cases 1–4 are distinct from the maintained-disclosure comparison's reduced feedback replacement. The test above does not implement or validate that replacement, establish preservation of the complete C dynamics, or show that a saved bit is an experience. Nor does it assert that human report and prior memory always behave like this toy system.

## 3. A necessary correction to the experimental shorthand

The earlier [specific pathway note](SPECIFIC_VISUAL_PATHWAY_GATE_TEST.md) described P4 in terms of source-to-consumer influence and residual routes. That is a useful **subtest**, but causal influence alone is not the whole frozen P4 requirement. P4 also requires that the specified distribution be absent and not replaced or retained as an equivalent distributed organization. A zero effect of a new source perturbation can coexist with an old consumer copy, as the implemented workspace shows. We therefore cannot count a channel-effect bound alone as a P4 pass.

To compare two histories rather than only newly imposed source values, the regimes in the boundary certificate must include the relevant content preparation and prior records in `μ_c`. Resetting memory to a common state may make η small **for those prepared trials**, but reset, loss of memory or altered feedback may itself disturb C, experience or the intervention's meaning. P3 and P6 must be re-evaluated in those same conditions. Treating previously stored content as irrelevant needs an independent argument tied to the specified target and time window.

## 4. What would make this useful in a real experiment?

For the extrastriate–frontal proposal, a researcher would have to (i) define the entire consumer set and time interval, (ii) identify a complete physical/causal interface including recurrent and alternate routes, (iii) bound all pertinent prior records and side information, (iv) validate the boundary transcript and its conditional dependence under the relevant preparation/intervention, and (v) independently test P3 and P6 on the same experimental condition. A narrow interface and a task-specific result may be useful, but does not certify an unrestricted multi-consumer absence.

Offline cTBS plus BOLD does not provide a verified complete boundary or an upper bound on pre-existing content records, and its delayed measurements cannot establish this certificate. A more localized peripheral or engineered system could make a complete boundary more plausible, but might not independently warrant the target conscious experience. Whether an ethically feasible human protocol can establish all obligations remains open. No numerical neuroscience bound is claimed here.

## 5. Verification and global role

Run `python verification/boundary_cut_workspace.py`. The [saved output](verification/boundary_cut_workspace.json) checks 11,664 finite channel/factorization cases and the 120 fixed-environment workspace cases above. The general inequality is proved from known contraction, not inferred from enumeration.

This narrows the M4 task: rather than assuming unrecorded consumers are empty, identify a justifiable boundary **and** budget old records. It does not solve phenomenal unity, establish the user’s universal-consciousness commitment, or close the separate physics dependencies L3/L4.
