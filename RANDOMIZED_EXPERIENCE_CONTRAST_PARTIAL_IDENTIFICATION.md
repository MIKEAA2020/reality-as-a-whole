# Can a randomized intervention identify an experiential change?

## Result in brief

Randomization can identify the effect of an intervention on **observed reports**. It does not, on its own, establish the effect on a particular experienced content: the intervention may also change how that content is reported or measured. A positive result is nevertheless possible under explicit, target-valid calibration assumptions.

In an invented example, positive reports occur in 50% of control windows and 70% of intervention windows. If both arms share a sensitivity between 75% and 90% and a false-positive rate between 5% and 20%, the corresponding experiential prevalence contrast is between **4/17 and 4/11**, or about **23.5 to 36.4 percentage points**. Both endpoints are attainable under those assumptions. If the measurement channel is allowed to change between arms, exactly the same report rates are compatible with **no change in experience for anyone**. These numbers are stipulations, not measurements or established error bounds.

Even when the experiential prevalence contrast is fixed, it does not uniquely tell us which individuals would change or whether anyone would change in the opposite direction. The results below concern one prespecified content contrast in already identified hypothetical subjects, not whether a system is conscious or how subjects are constituted.

## 1. What the experiment would need to mean

Imagine a consenting, eligible human population and an ethically acceptable intervention `A∈{0,1}`. For a defined time window, target and coding protocol, `E(a)=1` means the participant would have a particular experienced content under arm `a`; `E(a)=0` means that particular content is absent, **not** that all experience or the person is absent. `Y(a)=1` means the standardized observed response would be positive. Let `p_a=P(E(a)=1)` and `q_a=P(Y(a)=1)` over the same eligible population.

This model assumes the target is well defined and comparable across arms; the subject is identifiable across the relevant conditions; each participant has well-defined potential outcomes for both arms; treatment assignment is randomized; consistency holds for the assigned arm; and interference, nonadherence, exclusions and missing data are absent or validly handled. Observed arm frequencies estimate `q_a` only under the relevant design and sampling assumptions. The sample rates are **population values** here, not finite-sample estimates, and no actual intervention or trial has been conducted. A within-person design would require additional assumptions about carryover, order, time and whether the two windows remain comparable.

The participant's own experience is an anchor, not something to be redefined away as an external report. For an external analysis, `Y` is a fallible communication or measurement channel: its sensitivity and false-positive rate relative to the *actual defined content* require justification. Reliable testimony is important evidence, but repeated agreement between imperfect channels does not automatically establish their error against the experiential target. No observer directly reads another participant's private experience simply by assigning a latent variable.

## 2. Identification under a shared calibrated channel

Assume, for this specific target and both arms,

```text
s = P(Y(a)=1 | E(a)=1),       f = P(Y(a)=1 | E(a)=0),
```

with the same `s,f` in each arm and `s>f`. These are population-average conditional rates; they need not be constant for every person and the equations do not assume independent errors. For each arm the law of total probability gives

```text
q_a = s p_a + f(1-p_a) = f + (s-f)p_a,
ΔE = p_1 - p_0 = (q_1-q_0)/(s-f).
```

Thus an exactly known positive report contrast implies a positive *average* experiential contrast if this particular stable, positively oriented channel applies. If `s` and `f` are known exactly, the experiential prevalence in each arm and its contrast are point identified within the model. If not, use only defensible bounds and the probability feasibility conditions `f≤q_a≤s`. Shared rates and positive orientation are substantial **experiential bridge premises**, not consequences of randomization.

For the stipulated `q₀=1/2`, `q₁=7/10`, and the rectangular rate set `s∈[3/4,9/10]`, `f∈[1/20,1/5]`, every pair is feasible. The denominator `s−f` lies between `11/20` and `17/20`, so

```text
4/17 ≤ ΔE ≤ 4/11.
```

These bounds are sharp for the specified rectangle and exact report rates: at `(s,f)=(9/10,1/20)` the arm prevalences are `(9/17,13/17)`; at `(3/4,1/5)` they are `(6/11,10/11)`. Both pairs lie in `[0,1]`, and simple Bernoulli channels realize them. A smaller interval is not warranted from those assumptions alone. If rate uncertainty is correlated, if the rectangle contains infeasible pairs, or if reports have sampling uncertainty, optimize over the **joint feasible set** instead of mechanically applying these endpoints. A confidence interval for the reported contrast and simultaneous uncertainty in calibration must be propagated; a population interval is not a confidence interval.

## 3. Same observed reports, no change in experience

A different possible model has `E(0)=E(1)` for every participant, with `P(E=1)=1/2`. The rates are

| Arm | Sensitivity | False-positive rate | Positive-report probability |
|---|---:|---:|---:|
| Control | `9/10` | `1/10` | `1/2` |
| Intervention | `9/10` | `1/2` | `7/10` |

In each arm the response remains positively associated with the target (`s>f`), but the intervention changes the channel. The observed binary-report distribution in each arm is **exactly the same** as in the preceding example; the experiential contrast is zero. This witness violates the shared-rate and stipulated false-positive range assumptions, so it does not refute the conditional bound. It shows why those assumptions matter. The equality concerns the specified arm-level binary reports and randomized assignment, not arbitrary additional neural measurements, confidence responses, or independently validated first-person data; such added evidence could discriminate the models.

The drift model is a mathematical possibility, not a claim that this sort of drift actually occurs, that people systematically misreport, or that reported content is untrustworthy. Altered attention, response criterion, memory, timing, motor output or interpretation are examples of channels one might investigate; the toy itself supplies no evidence of any of them. Observing a strong causal response of the reporting apparatus would not establish which experiential channel is correct without a target-relevant anchor or other justified bridge.

## 4. Population change is not a census of individual changes

Keep the common exact channel `s=9/10, f=1/20` and hence `p₀=9/17, p₁=13/17`. Here are two distributions of paired *potential* target outcomes. A row labels `(E(0),E(1))` for the same individual:

| Potential outcomes | Model A | Model B |
|---|---:|---:|
| `(0,0)` | `4/17` | `0` |
| `(0,1)` gain of the target | `4/17` | `8/17` |
| `(1,0)` loss of the target | `0` | `4/17` |
| `(1,1)` | `9/17` | `5/17` |

They have the same experience prevalence and the same `(E,Y)` distribution within each arm under the stipulated channel, hence also the same observed binary-report distributions. They differ in individual counterfactual changes: A has no losses; B has both gains and losses. “Gain” and “loss” mean only the presence of this specified content, not welfare benefit or harm.

For these fixed prevalences, the sharp probability bounds for gain are `max(0,p₁−p₀) ≤ P(E(0)=0,E(1)=1) ≤ min(p₁,1−p₀)`, namely `4/17` to `8/17`. The corresponding loss bounds are `0` to `4/17`, since gain minus loss equals `p₁−p₀`. The two models attain the endpoints. Randomization identifies arm marginals, not the joint counterfactual pair for each person. Even if a valid experiential anchor supplied the marginals, resolving that coupling requires further design or structural assumptions; repeated observation under changing conditions does not automatically reveal both potential outcomes of the same original window.

## 5. Decision sequence and connections to earlier gates

1. **Define the target and the intervention first:** whose episode, which content, which window, and how uncertain or mixed responses are handled. Ensure consent, safety, independent ethics review as appropriate, and welfare protections. Do not infer subject identity simply from a retained response.
2. **Randomize and measure the operational effect:** lock eligibility and analysis rules, measure missingness and adherence, use suitable controls and report uncertainty. This supports an intervention effect on `Y`, not yet on `E`.
3. **Investigate the bridge in both arms:** support or bound sensitivity and false-positive rates against the same target using the available first-person anchors and relevant controls. Make communication, timing, interpretation and condition-dependent errors explicit. Proxy agreement alone is not a target-valid calibration. Neither statistical repetition nor perfect physical randomization creates a private experiential ground truth for an external observer.
4. **Compute feasible ranges, not a preferred answer:** incorporate arm-specific rates, their dependence and sampling uncertainty. If independently justified bounds permit both positive and zero experiential contrasts, the experiential result is inconclusive even if the report effect is robust. If the bounds genuinely exclude zero, state the model-dependent conclusion and limitations; if observations are incompatible with all prespecified models, revisit the shared assumptions rather than forcing a winner.
5. **Do not transport silently:** applying the same calibration to a nonreporting state, a different population or a nonbiological target requires separate support. Stop short of incidence or substrate claims when that support is unavailable. A result about a coarse content contrast does not establish felt quality, subject count, token identity, persistence or metaphysical constitution.

The [random-audit rivalry gate](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) addresses a different question: how randomized prompts bound decoder–report disagreement, and what additional report-to-experience error and physical-gate bounds would separate scoped rival predictions. Its thresholds are not assumed here. The [latent-assay gate](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md) analyzes multiple probes and conditional independence; this example instead makes the *intervention-dependent measurement channel* and the unidentified individual counterfactual coupling explicit. The [calibration transport gate](EXPERIENTIAL_MISMATCH_CALIBRATION_TRANSPORT_GATE.md) gives a source-to-target worst-case error bound under a stable kernel; equality of the two conditional rates here is a distinct assumption, not an application or replacement of that result. The [feedback bridge audit](FEEDBACK_REALIZATION_AND_PHENOMENAL_BRIDGE_AUDIT.md) remains the broader account of incidence, quality and subject individuation.

## Verification and scope

The [exact arithmetic script](verification/randomized_experience_contrast.py) builds the synthetic arm distributions and writes the [receipt](verification/randomized_experience_contrast.json). The [independent test](verification/randomized_experience_contrast_test.py) checks a rational grid, both potential-outcome couplings, channel drift and the coupling bounds. The sharpness of the full continuous rectangle follows from the displayed denominator extrema and attainable endpoints, not from the grid alone. These checks verify the invented probability calculations; no participants, biological observations or experiential calibration were obtained.
