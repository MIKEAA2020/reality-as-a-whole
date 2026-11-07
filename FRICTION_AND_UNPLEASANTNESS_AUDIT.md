# Can intrinsic friction explain unpleasantness?

## Decision

**Follow-up:** The [vibrational dissonance test](VIBRATIONAL_DISSONANCE_EXPERIENCE_TEST.md) examines physically coupled phases, distinguishes structural frustration from instantaneous mismatch and relaxation, and audits actual pain/EEG research. It does not identify oscillatory frustration with experience or assume literal fundamental strings.

The user's proposal is a serious candidate for a **specific part of experiential character**: perhaps a certain kind of dissonance or friction is intrinsically unpleasant, rather than first being neutral physics and then somehow acquiring unpleasantness. This is not yet an explanation of all experience, all pain qualities, or the existence of a subject.

There is already extensive work on affect, control, homeostasis, predictive processing and pain. The first contribution here is therefore not to announce a new theory, but to make **one particular interpretation of friction mathematically explicit and subject it to a failure test**. Its limitation is sharp: a measure of conflict depends on how a system's regulatory objectives are individuated, and ordinary aggregate action costs alone cannot identify that decomposition. A second limitation is that an unattainable single objective can be severely frustrated while the particular *between-objectives* measure is zero. Both facts constrain any attempt to identify the measure itself with unpleasantness; neither disproves the broader intuitive idea.

## 1. The proposed bridge—and its two levels

- **Phenomenological intuition:** some experienced tension, resistance or frustrated striving seems intimately related to discomfort. This gives the idea a first-person motivation.
- **Empirical/constitutive conjecture:** a physically and dynamically specified form of subject-internal regulatory friction is identical to, or reliably realizes, a particular unpleasant affective character.

These are different claims. A description using words like “bad,” “distressing,” or “what the subject wants to avoid” cannot independently define the physical variable if the goal is to explain bad feeling. Conversely, a fully structural operationalization does not by itself establish what, if anything, it feels like. An identity theorist need not propose a separate causal machine that adds a feeling to physics; they do need an independently warranted, specific identity or constitutive account.

Our finite target is **momentary unpleasantness during an independently reported painful thermal experience**. Separately measure sensory intensity and other qualities. The target is not tissue damage, motor withdrawal, the whole of pain, all negative emotion, or the number of experiencing subjects. The IASP explicitly distinguishes pain from nociception; see the [revised definition](https://doi.org/10.1097/j.pain.0000000000001939). The rule should respect both subjective reports and independent physical observations, without treating either as infallible.

## 2. Prior art and why the simplest equation is risky

Control-process and predictive accounts of affect already connect appraisal, progress, prediction errors and valence; see the discussion and primary sources in [Affective valence does not reflect progress prediction errors in perceptual decisions](https://doi.org/10.3758/s13415-023-01147-8). In that study, observed affect in the particular perceptual-decision task was better described by additive expected and actual progress than by the examined progress-prediction-error formulation. It does not refute every predictive-processing account or this proposed friction measure. It does warn against equating *any* mismatch with negative affect.

Similarly, pain can be affected by context without tissue damage or noxious input mapping one-to-one onto reported suffering. A useful proposal must distinguish disagreement between objectives, unavoidable bodily deviation, anticipation, time course and individual appraisal—without adding arbitrary terms after looking at outcomes. Pleasant challenge and relief are tests, not examples to dismiss by definition.

## 3. One independently defined structural candidate

This is an **illustrative decomposition-based proxy**, not a demonstrated brain quantity or a new theorem in optimization. For a fixed physical system at a declared time, let:

- `A` be a prespecified finite set of physically feasible control policies over a fixed horizon;
- `l_i(a) ≥ 0` be the independently specified deviation cost for policy `a` relative to regulatory objective `i`;
- `w_i ≥ 0` be fixed weights summing to 1, with objective units, scales and weighting justified before testing.

Define the best joint cost and the sum of the separate optima:

```text
J = min_{a in A} Σ_i w_i l_i(a)
B = Σ_i w_i min_{a in A} l_i(a)
F = J − B ≥ 0.
```

The inequality follows because every policy has cost at least each objective's separate minimum. `F` measures the **additional compromise** required to use a common policy rather than letting each objective independently choose a policy. It is not mechanical friction or an objective measurement of value. A mathematical controller, an ordinary organism and a proposed experiential subject can all be assigned such a number; nothing here asserts that all experience anything.

Operational commitments are demanding: the control policies must be feasible under declared dynamics; costs and weights must be tied to independently characterized regulation rather than calibrated from the very unpleasantness ratings being explained; and the horizon and relevant system boundary must be frozen. The theoretical `min` is an observer's counterfactual optimization—it is not evidence that a nervous system explicitly computes it. Unmeasured bodily processes and failure to observe relevant policies would require uncertainty bounds.

### Exact tests

Take two possible actions `a=0,1`, two equal weights and costs in `[0,1]`:

| Case | Objective costs for actions 0,1 | Aggregate costs | `F` |
|---|---|---|---:|
| Opposed objectives | `(0,1)` and `(1,0)` | `(.5,.5)` | `.5` |
| Aligned objectives | `(0,1)` and `(0,1)` | `(0,1)` | `0` |
| One objective completely blocked | `(1,1)` | `(1,1)` | `0` |
| Opposed objectives merged into one | `(.5,.5)` | `(.5,.5)` | `0` |

These are **formal constructions, not examples of people in pain**. The blocked objective shows that F excludes even complete unavoidable deviation when no second objective is specified; the residual `J` is instead 1 in that example. Thus a rule saying “all frustration is F” is false by construction. Adding `J`, dynamics or other terms could produce a broader candidate, but their contributions and calibration would need independent justification.

The opposed and merged rows have **exactly the same aggregate cost for each action**, yet F changes from `.5` to `0`. Thus aggregate action costs alone do not determine this friction proxy. The two descriptions may correspond to different internal physical implementations; the example does **not** show that two fully identical physical processes have different experience. It shows that selecting an objective decomposition is a substantive extra requirement, not something fixed by the aggregate behavior in this model. A rule that chose the decomposition by looking at unpleasantness would be circular.

A common additional concern is that the sum of losses may itself fail to be identifiable from observed choice: many objective functions can rationalize identical actions. The table makes the stronger limited point that **even if this whole aggregate cost table is supplied**, it is insufficient for F. More detailed physiological measurements and independent causal tests might distinguish genuine regulatory components; the table does not prove they cannot.

The [exact-arithmetic audit](verification/friction_conflict_audit.py) checks all 81 two-action/two-objective tables on a three-value grid. It confirms nonnegativity and that merging objectives keeps all aggregate action costs but sets F to zero; 18 tables on that grid have a positive gap. The algebra, not the finite enumeration, establishes the corresponding general result. Run `python verification/friction_conflict_audit.py`. Neither the verifier nor F assigns pain, utility, phenomenal character, or subjecthood.

## 4. An explicitly risky rival pair

For this small domain, use the following as candidates, **not established laws**:

- **Strict conflict hypothesis H_F:** under a prespecified genuine experiential-subject boundary, with the physical objectives, scales, controls and horizon independently fixed, unpleasantness `U` is an increasing function of this F, and `U=0` when `F=0`. On equal F, it predicts equal U within the declared domain, apart from prespecified measurement error. This deliberately strong version lets data challenge it. It is only one possible sharpening of the user's suggestion, not a commitment they have adopted.
- **Alternative H_R:** unpleasantness varies with some other independently specified bodily/regulatory organization, potentially including `J` or contextual processes, and is not fixed by F alone. A concrete H_R needs its own prespecified variables and predictions; simply saying “something else” is not a quantitatively predictive model.

Possible outcomes: if reliably different U occurs at independently established equal F, or reliably equal U at independently established different F where H_F requires a meaningful difference, the strict rule is challenged. Failure of an equivalence test is not evidence of equality. If F cannot be identified within useful uncertainty, the result is inconclusive about H_F. Neither a positive correlation nor a successful predictor proves the identity of F and felt unpleasantness; simpler rival predictors and held-out conditions must be compared.

`F=0` is not a claim that people cannot be uncomfortable without goal conflict. That would have to be tested in a genuine anchored case; the one-objective row only exposes what the **proposed formula** would say if its strong additional experiential identification were assumed. Nor should a failure of H_F be reported as a refutation of every possible intrinsic-friction view.

## 5. Actual evidence: pain dimensions can be separated, but F has not been measured

**Selective subjective modulation.** [Rainville et al. (1997)](https://doi.org/10.1126/science.277.5328.968) used hypnotic suggestions during noxious heat and reported changed unpleasantness ratings without a corresponding change in perceived intensity, with altered anterior cingulate PET activity. The accompanying [Hofbauer et al. (2001)](https://doi.org/10.1152/jn.2001.86.1.402) study, involving ten volunteers, targeted pain intensity and reported relative sensory/affective modulation. These support treating intensity and unpleasantness separately, not a perfectly isolated neurological switch; a nonsignificant change in another measure is not an equivalence certificate. Suggestions can also alter attention, expectations, reports and multiple brain processes. Neither paper measures the proposed F or independently identifies its regulatory objectives.

**Different interventions and signatures.** [Riegner et al. (2024, issue 2025)](https://doi.org/10.1016/j.biopsych.2024.08.023) combined two randomized trials, assigning 115 healthy participants to mindfulness, placebo cream, sham mindfulness, or book-listening control. With 49°C heat, they report differences in pain ratings and fMRI-based signatures among conditions. In the detailed results, the negative-affect pain signature reduction for mindfulness was significantly greater than placebo and control but **not significantly greater than sham mindfulness** (`p=.30`); this distinction matters because the abstract's more sweeping wording can obscure it. No pre-intervention fMRI was acquired, and the authors caution against generalization to chronic-pain patients. These signatures are statistical patterns, not direct meters of phenomenology or the proposed F. The paper does not establish which independently defined objectives, if any, conflict.

**Avoid a single-area identity.** [Feinstein et al. (2015)](https://doi.org/10.1007/s00429-014-0986-3) describe one patient with extensive bilateral damage to insula, anterior cingulate and amygdala whose emotional experience and expression of pain were preserved. The case is not a universal lesion experiment; residual tissue, individual variation and network reorganization matter. It does show that simply identifying unpleasantness with a named region's ordinary activation is too crude.

No new raw patient data were analyzed here. These published findings motivate and constrain the hypothesis; they do not establish its control variable, mediation, or experiential identity.

## 6. An ethical empirical next step

Before recruiting anyone, search for an existing dataset that includes stimulus delivery, separate intensity and unpleasantness reports, independently measured physical/regulatory signals, candidate action alternatives, and contextual conditions. If no dataset establishes the required controls and counterfactuals, say so; do not compute F by relabeling a pain rating or a pre-trained pain signature.

A future ethics-reviewed design could use calibrated, safely limited thermal stimulation and voluntary participation with immediate withdrawal, measure intensity and unpleasantness separately, and vary a noncoercive task context. Pre-register:

1. the policy set, time horizon, independent physiological interpretation of each objective, scales, and weights; control changes in heat input;
2. independent measurements needed to reconstruct each cost and its uncertainty, including unobserved objectives and the actual feasible policy set;
3. the numerical functional link between F and unpleasantness, and comparison models based on stimulus, sensory intensity, expectations, task context and residual `J`;
4. a held-out subject/condition test, reliability, clustering by person, and error/coverage for both the measured proxy and reported experience;
5. what would count as evidence *against* H_F, not only a positive correlation.

Randomizing a task or instruction by itself does not isolate F: that manipulation can simultaneously change attention, cognition, reporting, context, or the objective set. Conditioning on post-intervention intensity can itself induce selection bias; equal average ratings do not prove equal sensory organization. To claim causal mediation, separately justify identification and all intervention effects; otherwise report predictive associations only. This is an analysis blueprint, **not** a validated protocol, recruitment recommendation, or claim that pain-inducing research is needed. Studies must never prevent withdrawal or withhold clinically indicated pain relief.

## 7. What this changes in the whole-reality programme

The possible bridge is more refined than “everything tends to harmony.” A subject could experience a locally unpleasant conflict within an imperfect world without establishing that the entire absolute is a single universal person. Pleasure, other qualities and subject boundaries need separate treatment. A viable theory may describe frustration as a locally real feature even if the totality is the only genuine actuality; it need not postulate unrealized possibilities waiting to become real. The algebraic `a` alternatives are control-model counterfactuals, **not** a metaphysical claim that nonactual concrete possibilities exist.

The central unresolved question remains: what makes a physically specified regulatory conflict intrinsically unpleasant, rather than merely a conflict whose behavior we can predict? The intuitive identity is a research direction; it is not derived by the optimization and does not yet meet the zero-residue standard. It also does not close the independent problem of emergent time or continuum physics.
