# How accurate must a first-person mismatch test be?

## Result and scope

The follow-up [physical mismatch measurement gate](FOUR_SPIN_PHYSICAL_MISMATCH_MEASUREMENT_GATE.md) derives an explicit toy-model `ρ` under independently stipulated calibration and spin-readout assumptions, and shows why passive data cannot identify every possible target-channel preference. Its sensor and calibration inputs are hypothetical, not real validation.

The prior [current-level versus onset comparison](CURRENT_MISMATCH_VERSUS_HISTORY_EXPERIENTIAL_GATE.md) identified the one physical history where the proposed binary assignments disagree. This gate quantifies what must be known to make that disagreement visible through an imperfect, potentially history-dependent report and an imperfect physical classifier.

For episodes *classified* as persistent mismatch `H=11`, suppose independently justified conditional bounds are `η` on report disagreement with the designated experienced contrast and `ρ` on physical-history misclassification. Even if the two errors are dependent and history-specific, the predicted positive-report rate is at least `max(0,1−η−ρ)` under the strict level package and at most `min(1,η+ρ)` under the strict onset package. With only these bounds, **η+ρ<1/2 is sufficient for nonoverlapping population predictions**; the bounds are sharp in the unrestricted finite model. At or above 1/2 the predictions can overlap. Actual calibrated values are not supplied, and a valid real-world discrimination has not been achieved.

If the *whole conditional distribution* of the true physical history given `H=11` is known, the sharper separation depends on its actual `P(C=11|H=11)`, not on a generic error bound. This result does not deny the authority of first-person experience: `η` concerns an external binary coding of a communicated or recorded target, not the existence of experience. The bounds apply only if that target and the reference used to evaluate it are adequately specified and justified.

## 1. The objects, without circular calibration

For a declared episode and subject, let the true physical history be `C=(q⁰,q¹)`, the independently measured/classified history `H=(h⁰,h¹)`, and `U` the designated unpleasant-versus-neutral experiential contrast. `Y=1` is a recorded positive response for that contrast after a prespecified, anchored coding procedure; `Y=0` is its negative response. The onset and level models posit, respectively,

```text
level: U = q¹;          onset: U = 1{q⁰=0 and q¹=1}.
```

They retain the same physical domain and assume a real subject and target episode; both mapping and persistence remain open. `U` is not asserted to exhaust a subject's experience, amount of suffering, or all possible mixed feelings. A binary response requires a declared target, timing and neutral reference; if experiences do not fit that dichotomy, either enlarge the model or stop. A person's report can itself be central first-person evidence. The additional `Y≠U` hypothesis is a **measurement model**, not a claim that reported pain is false or that only an outside observer can know it.

Fix the observed `H=11` group and assume it has positive probability. For each candidate package let the following *conditional, target-population* statements be independently warranted, not fitted to whichever model is favored:

```text
P(Y ≠ U | H=11) ≤ η,          P(C ≠ H | H=11) ≤ ρ.
```

The first is the coding/communication error for precisely this contrast and episode; the second is the **posterior error in the entire two-bit history** among cases called `11`. Neither follows from generic agreement, repeatability or the models themselves. No independence is assumed, including independence of the two errors, the physical state, or the report. Bias may differ arbitrarily across histories provided these declared conditional upper bounds still hold. Conditional on `H=11`, the level and onset rules predict `1` and `0` respectively *if* the physical label is correct. Therefore

```text
P(Y ≠ predicted_U(H) | H=11)
    ≤ P(Y ≠ U | H=11) + P(C ≠ H | H=11)
    ≤ η + ρ.
```

The first step is a union bound, not a novel statistical theorem. It can be conservative, because not every wrong physical cell changes a particular model's predicted U, and physical and report errors can overlap. It does not require a stable common sensitivity and specificity. It **does** require the indicated per-package experiential calibration: if the bound is known only by presupposing which quality law is true, the comparison is circular.

## 2. The sharp discrimination threshold

Let `r=P(Y=1|H=11)` and `b=η+ρ`. Under the stated assumptions:

| Package | Permitted `r` |
|---|---|
| strict level | `[max(0,1−b), 1]` |
| strict onset | `[0, min(1,b)]` |

When `b<1/2`, these intervals are disjoint. For example, with *hypothetical* `η=0.10` and `ρ=0.15`, level allows `[0.75,1]`, onset allows `[0,0.25]`. A population rate in the gap excludes **both completed packages**, assuming the calibration and exact deterministic assignments; it is not evidence that experience is absent. A rate inside one interval is merely compatible with that package, not proof of it. At `b=1/2` the intervals touch at `r=1/2`; above it they overlap.

The intervals are **sharp when only the stated conditional bounds are known**, no further physical constraints are imposed, and all needed true cells are permitted. For the level lower endpoint, assign up to `ρ` of the observed `11` group to true `10`, where level is neutral, and use up to `η` report errors on the remaining group. For the onset upper endpoint, assign up to `ρ` to true `01`, where onset is unpleasant, and use up to `η` errors on the remaining group. Saturate at 0 or 1. These constructions allow different latent physical mixtures in the two packages; they do not establish that both mixtures satisfy an independently known physical joint distribution. If that distribution is known, use the sharper calculation below. The executable [finite check](verification/mismatch_history_assay_gate.py) enumerates all 330 quarter-grid conditional joint tables of true cell and binary report, and tests all 50 rule/budget combinations. The analytic constructions cover the continuous range; enumeration is a bounded arithmetic check, not a proof of an experiential anchor.

A discriminating empirical result must account for uncertainty in `r`, `η`, `ρ`, and their joint estimation. A prespecified simultaneous confidence procedure can reject a package only when the confidence region does not intersect its admissible set; do not substitute point estimates into these boundaries as if known. Repeat observations from one person or session can share errors, so IID binomial intervals require justification. If no confidence-calibrated bound is available, report the raw experience data and say the package test is inconclusive, rather than choosing a numerical η by convenience.

## 3. Stronger physical calibration can sharpen the comparison

Suppose a separate validated physical measurement gives all four probabilities

```text
p_ab = P(C=ab | H=11),   p_00+p_01+p_10+p_11=1.
```

These are the *same physical conditional mixture* for both models, not a mixture selected separately for each. The positive experiential fractions under the two deterministic quality assignments would be

```text
v_level = p_01 + p_11,        v_onset = p_01,
v_level − v_onset = p_11.
```

Given only `P(Y≠U|H=11)≤η`, each report rate may lie anywhere within its respective `[max(0,v−η), min(1,v+η)]`. These intervals are sharp when no further report-channel restrictions are imposed: flip up to η of the appropriate U class. They are disjoint precisely when **`p_11 > 2η`**; at equality they touch. Again, the independently warranted error bound is a premise about the actual contrast, not an independently observed counterfactual U for both models.

For illustration only, take `(p_00,p_01,p_10,p_11)=(1,2,3,14)/20`. Then `v_level=4/5`, `v_onset=1/10`, so with `η=1/10` the allowed report ranges are `[7/10,9/10]` and `[0,1/5]`. The probabilities and error rate are invented, not inferred from the four-spin calculation or a human experiment. The [tests](verification/mismatch_history_assay_gate_test.py) enumerate fixed posterior mixtures on a rational grid and check these endpoints.

This refinement exposes a useful tradeoff: independent physical validation identifies how much of the apparent `11` group is genuinely in the **only disagreement cell**. A high overall physical accuracy does not guarantee high predictive value in a rare classified cell. Sensitivity and specificity are conditional on the true state; `ρ` is conditional on the observed classification and depends on prevalence and possible differential errors. Converting between them requires prevalence and a specified physical measurement model; it cannot be done by relabeling sensitivity as posterior accuracy.

## 4. Why global accuracy may be too weak

Suppose instead that only population-average bounds `P(Y≠U)≤ε`, `P(C≠H)≤φ` are warranted, and let `w=P(H=11)>0`. Without a class-invariance assumption,

```text
η ≤ min(1, ε/w),       ρ ≤ min(1, φ/w).
```

All allowable errors could concentrate in the critical observed cell. Thus a sufficient (not necessary) condition for the earlier disjoint ranges is `min(1,ε/w)+min(1,φ/w)<1/2`. Uncertainty in w and both global bounds must be propagated. A source-domain global bound does not automatically transport to this target population or conditional cell; the separate [transport gate](EXPERIENTIAL_MISMATCH_CALIBRATION_TRANSPORT_GATE.md) explains the required overlap and stability.

As a numerical stress test, **suppose** the observed cell probability equals the existing toy equilibrium's `71/448` and, independently, hypothetical global bounds are `ε=1/20` and `φ=1/50`. Then the conditional combined bound is at most

```text
(ε+φ)/w = 784/1775 ≈ 0.442 < 1/2,
```

giving a conservative gap of `207/1775 ≈ 0.117` between the two conditional report ranges. The value `71/448` is the toy probability of *true* `11`; it is **not automatically** the observed-cell frequency when a classifier errs. This illustration explicitly assumes the observed frequency coincides with it; the toy model supplies neither the classifier nor either error bound. If the observed cell were less frequent, the same population-average calibration would be less informative. The bound is conservative and not claimed sharp if additional known physical frequencies constrain the errors.

## 5. Calibration and causal interpretation: stop conditions

1. **Define the contrast first.** Identify the same subject and episode, target quality, coding rules, response timing, neutral anchor and handling of mixed/ambiguous/nonresponses. Use independent first-person elicitation and within-person comparisons where appropriate. Multiple questionnaires or behavioral proxies are not automatically independent witnesses or a gold standard.
2. **Do not calibrate U from the theory being tested.** A numerical `η` requires a defensible independent reference or expressly bounded assumptions for the target contrast in the target conditions. No independent infallible observer of another's experience is assumed. Agreement between proxies alone can be produced by shared biases; statistical measurement invariance tests cannot by themselves prove phenomenal identity. If the response itself is operationally taken as the outcome, set `U=Y` only as an explicit *operational definition*; the conclusion then concerns that response, not an independently established phenomenal identity.
3. **Validate q without using held-out target ratings.** The physical relation, preferred reference, two sampling windows, classifier and uncertainty must be specified independently. A measurement of external temperature, pain intensity, EEG amplitude or prediction error is not q without a justified model. Obtain `ρ` or the full posterior mixture in the **observed** target cell, including validation-sample selection and label uncertainty. If validation is impossible, calculate a range over plausible error assumptions and do not claim identification.
4. **Separate inference from intervention.** A randomized history protocol estimates assignment effects under its design, not an unconfounded causal effect of q within a post-treatment selected cell. Test the assignment patterns with appropriate uncertainty, missingness and participant/session dependence; any inference about q's causal role needs additional identification assumptions or convergent interventions. Predefine cell overlap and an inconclusive stopping rule.
5. **Separate model refutation from explanation.** Rejection of a completed assignment means at least one of its physical, experiential or reporting premises fails. Passing a binary assay is not a derivation of why anything feels unpleasant, of subject boundaries, or of an experiential rather than neutral ground. The mathematical model is not a study of pain or an actual toy subject.

## 6. Related evidence and reproducibility

[Edwards et al. (2023)](https://doi.org/10.1097/EDE.0000000000001572) study covariate-dependent outcome misclassification and its consequences for prevalence estimation, including transport between validation and target populations. Their abstract and source snippets were consulted; the complete article, figures and code were not read or replayed. That work concerns an observable epidemiological outcome, not validation of first-person phenomenology or the error bounds derived here. The separate [heat-pain source audit](CURRENT_MISMATCH_VERSUS_HISTORY_EXPERIENTIAL_GATE.md) documents actual reports without asserting q was measured.

Run `PYTHONPATH=verification python verification/mismatch_history_assay_gate.py` and `PYTHONPATH=verification python -m unittest mismatch_history_assay_gate_test`. The [receipt](verification/mismatch_history_assay_gate.json) records exact rational examples; no third-party data or nonstandard packages are needed. No preregistration, real calibration, new empirical result, or substantive battery pass is claimed. B4–B5/F2, B9/F3 and B10 remain open; C3 remains **full structural and experiential intelligibility**, jointly with C1–C7.
