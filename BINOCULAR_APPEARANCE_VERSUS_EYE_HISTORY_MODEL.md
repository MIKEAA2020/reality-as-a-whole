# A testable color-blending model: appearance versus eye-specific history

## Result in brief

Two toy models can give the **same binocular appearance throughout adaptation** yet make different predictions for later eye-specific probes:

* **Appearance-only state:** once the adapting display ends, the future response depends on its observer-level appearance history and the current probe, but not on which eye received which color. Swapping the eye assignments while preserving that appearance makes no difference to the later probe response.
* **Eye-history state:** the appearance is still the same binocular average, but eye-indexed adaptation variables persist. A neutral probe to one eye reveals opposite aftereffects when the adapting colors have been swapped.

In the deliberately invented numerical example below, both histories have appearance `0`; the predicted **eye-by-history interaction** is `0` for the appearance-only model and `1` for the eye-history model. These are exact results for the stated equations, **not measured effect sizes or a new analysis of participants**. The model makes a concrete scientific distinction, but its extra variables are processing states, not extra subjects or demonstrated experiences.

The [preceding source audit](BINOCULAR_COLOR_FUSION_AND_LEWTAS_BLENDING_AUDIT.md) reports that Anstis and Rogers found an analogous qualitative pattern. Their study does not calibrate this model's numerical parameters, and the proposed future experiment below is not a replication already performed. The later [probe-context audit](AFTERIMAGE_PROBE_CONTEXT_AND_IDENTIFICATION_AUDIT.md) examines how test contours can alter afterimage judgments and why response shifts alone cannot uniquely identify the underlying modulation mechanism.

## 1. Set the terms before examining outcomes

Use a signed, abstract one-dimensional color coordinate; positive and negative merely denote opposite directions relative to a neutral test. This is **not** identified with CIE `x,y`, cone excitation, an actual measured color axis, or a complete phenomenal quality. Let `a > 0` denote an effective adaptation input. Compare two equal-duration histories, at the same retinal location:

| History | Left eye | Right eye | Stipulated binocular appearance |
|---|---:|---:|---:|
| A | `+a` | `−a` | `0` |
| B | `−a` | `+a` | `0` |

Within this toy, `z = (left + right)/2` is zero throughout adaptation. A common fade profile could multiply both inputs and preserve that equality at every instant; for simplicity `a` is the resulting effective input. The coordinate `z` is an **observer-level report proxy**, not a claim that both eyes house separate seeing subjects, that actual observers see exactly gray, or that every experiential feature matches.

After adaptation a physically identical neutral test is presented to the selected eye with the other eye seeing black, or to both eyes for a separate control. The same probe eye, delay, background and test geometry must be used when comparing A with B. Let `Y_L` and `Y_R` be signed deviations from an independently defined neutral reference. They are predicted response coordinates, not directly observed sensations. Probe presentations are separate randomized trials, so probing one eye is not assumed to leave adaptation unchanged for a second probe.

## 2. Rival 1: the specified appearance-only state

Let the predicted mean response to a fixed eye-specific probe be

```text
E[Y_e | history] = f_e(z(t) over the adaptation period, probe, delay, fixed context)
```

for `e = L,R`. Probe eye can have its own function and baseline; the claim is only that, **given the same appearance history and same probe/context**, the prior eye assignment supplies no further information. A and B have the same full `z(t)` in this model, so

```text
D_L = E[Y_L | B] − E[Y_L | A] = 0
D_R = E[Y_R | B] − E[Y_R | A] = 0
Δ = D_L − D_R = 0.
```

This is a restrictive, falsifiable candidate—not the claim that all appearance-based theories, all experiential-whole accounts, or all physical models must satisfy it. The fixed state is *the stipulated calibrated appearance variable and its history*, not an arbitrary real number that could secretly encode all eye inputs. Allowing the observer's internal state to store eye history, an unmeasured perceptual distinction, or other adaptation information already goes beyond this candidate. Unequal eye baselines cancel within `D_L` and `D_R`, provided they are stable across randomized A and B trials.

The prediction is about expected responses after controlling context; it is not the assertion that matching reports prove physically or phenomenally identical entire histories. The premise must be tested separately, and is never guaranteed by asking whether both look gray.

## 3. Rival 2: a minimal eye-indexed memory

Now add the **stipulated** retained variables `h_L` and `h_R`, equal to the effective signed input at the end of adaptation. For a positive gain `k`, set

```text
E[Y_L] = −k h_L       E[Y_R] = −k h_R
E[Y_both] = −k (h_L + h_R)/2.
```

The minus sign defines an idealized complementary aftereffect, not a derived law of color vision. The binocular-control equation assumes equal weights and linearity; actual binocular combination, adaptation and afterimage appearance can be nonlinear and context dependent. These are deliberately testable restrictions.

| History | `h_L` | `h_R` | Left probe | Right probe | Binocular control |
|---|---:|---:|---:|---:|---:|
| A | `a` | `−a` | `−ka` | `+ka` | `0` |
| B | `−a` | `a` | `+ka` | `−ka` | `0` |

Thus `D_L=2ka`, `D_R=−2ka`, and **`Δ=4ka`**. With invented units `a=1` and `k=1/4`, `Δ=1`, while both adaptation appearances and both binocular-control predictions are zero. If `k=0` or `a=0`, the models coincide on this test. If the eye gains differ, the more general same-sign model gives `Δ=2a(k_L+k_R)`; that extension must be calibrated, not silently imposed.

An all-in-one physical or computational system can carry the pair `(h_L,h_R)` as one global vector. No independent eyes, private perspectives, ontological nesting or subject multiplicity are needed to reproduce the table. Conversely, merely stating that colors blend leaves the two models' different future predictions unspecified.

## 4. Approximate matches: a conditional robustness bound

Real judgments are noisy. Failure to reject a difference in appearance is **not** evidence of equivalence. Suppose, as an extra assumption, that for the relevant observer and context the latent scalar appearance histories in A and B differ by at most `ε` under a defined norm. Suppose each response function satisfies an independently justified Lipschitz bound:

```text
|f_L(z_B) − f_L(z_A)| ≤ K_L ε
|f_R(z_B) − f_R(z_A)| ≤ K_R ε.
```

Then the appearance-only candidate obeys **`|Δ| ≤ (K_L+K_R)ε`**, by the triangle inequality. If `K_L=K_R=K`, this is `2Kε`. In a purely illustrative calculation, `ε=1/20` and `K_L=K_R=1` give `|Δ|≤1/10`, below the toy memory prediction `1`. All these numbers are invented, in the same abstract response units; they are neither empirical calibration nor a confidence interval.

This bound is useful only if the proposed appearance measure is appropriate, the history-norm bound really holds for the relevant trials, and the response-sensitivity bounds hold uniformly over the contexts and histories. A color-match equivalence margin by itself does **not** establish any of those conditions. In particular, a different unmeasured feature, adaptation of the response rule, display leakage or a memory for the assignment would defeat the inference. A measured interaction beyond a justified bound challenges the **defined appearance-only package**, not every account in which appearance is important.

Statistical uncertainty is separate: a future study must use uncertainty intervals for both the interaction and the appearance measurements, propagate uncertainty in any calibrated bounds, and account for repeated trials and participants. A point estimate above an invented bound is not a test.

## 5. Relation to the actual evidence

In [Anstis and Rogers (2012), experiment 6](https://www.sciencedirect.com/science/article/pii/S0042698911003889), five observers viewed two locations with opposite green/magenta assignments across the eyes. Colors faded in over 12 seconds, followed by four seconds of adaptation. The authors report gray adapting fields and then pink/green responses to a monocular white test, with the predicted sign at all 80 trials per observer. Their design varied eye and position; it did **not** measure the signed continuous response coordinate or `Δ=1` above, nor establish the stipulated equal-gain linear model. Repeated top-up adaptation, spatial location, probe geometry and categorical response all matter. We did not access or reanalyze original trials. The earlier audit notes inconsistencies in other reported numerical details and a sign error in the paper's displayed extreme chance-probability approximation.

This qualitative pattern is consistent with retained stimulus-dependent processing becoming detectable after the probe changes the viewing condition. It would be inconsistent with a strictly report-only model **if** the relevant appearance histories and all other required contexts were truly equivalent and the report-only model excluded other memory. The published data do not by themselves verify those demanding assumptions. They also do not show the individual eye-input colors were experienced by separately existing subjects during adaptation.

## 6. A possible new experiment—not yet a frozen protocol

A feasibility study could operationalize the comparison without building in the conclusion:

1. **Independently calibrate and blind.** Measure each eye's alignment, stimulus luminance, neutral and test response scales; check optical crosstalk. On separate calibration trials obtain eye-specific signed aftereffect functions and their uncertainty, including whether a monotonic coordinate and gain model are reasonable. Fix the color axis and target retinal location for each observer. Use coded, randomly assigned A/B displays and balance the eye and color orders; do not tell observers the expected afterimage sign.
2. **Verify appearance separately.** Include randomized appearance-check trials across the adaptation period and immediately before the test, with controlled match tasks and a prespecified equivalence margin, plus checks for rivalry, luster, fixation and spatial heterogeneity. Avoid using a report from a trial *after* seeing the probe to select whether that same trial enters the primary analysis. Separate appearance-check and probe trials reduce interference, but then require an explicit generalization assumption between trial types. Matches and confidence constrain selected judgments, not complete experiential identity; if equivalence cannot be supported, record the appearance-only comparison as **unresolved**.
3. **Primary contrast.** Randomize A/B and left/right probe across comparable independent trials, equalizing delay, location, surround, luminance, stimulus geometry and recent adaptation. Prespecify `Δ = (B−A)_L − (B−A)_R` in calibrated response units. Include a neutral/no-adaptation condition, sham probe and the binocular probe as controls; washout or model carryover, and counterbalance trial sequences. Assess individual eye effects as well as the interaction; fixed eye biases alone cancel but eye-specific history-dependent crosstalk or carryover does not.
4. **Freeze alternative predictions.** Before main data, use independent calibration to fix the memory model's gain(s), expected signed interval and tolerable deviations, including noise and between-observer variation. If an independent, justified `(K_L+K_R)ε` bound exists, compare an appropriate confidence interval for `Δ` with that bound. An interaction outside it challenges the restricted appearance-only package; an interval excluding the frozen memory prediction challenges that specific memory model. An interval including both is inconclusive. A near-zero interval can challenge a prespecified nonzero memory prediction but cannot, by itself, prove the appearance-only model. If the requisite appearance or sensitivity calibration fails, do not force either verdict.
5. **Analysis and safety.** Predefine the participant-level estimand, cluster-aware uncertainty, response exclusions and handling of missing trials; do not treat repeated probes as independent participants. A real protocol requires sample-size planning from independent pilot variability, ethical review and safe display exposure. This is a study design sketch, not an approved procedure or evidence that its practical assumptions hold.

The interaction is an operational test of **memory for an input assignment beyond a defined appearance proxy**, not a test for consciousness in an eye. Other processes—including attention, unmeasured appearance, response bias or cross-eye adaptation—can generate an interaction. Add targeted controls and compare richer rival models; do not relabel every nonzero effect “private experience.”

## 7. Implication for the experiential framework

The [spectral-metamer construction](COLOR_METAMER_PHENOMENAL_PHYSICAL_BRIDGE.md) showed that a momentary standard-observer coordinate need not determine the result of a later filter. The present example adds a **memory** contrast: here the earlier inputs differ while current probe settings are held fixed, and past input assignment changes the later response in one explicit model. Both are factorization failures for a restricted proxy. Neither establishes that the full physical system, or the full experiential whole, has identical states in the two cases.

Lewtas's problem is harder: even if the predictive state were measured perfectly, why should a particular organization have a particular felt quality, and which subject or subjects own it? Neither `z`, the aftereffect variables, nor a successful fit answers that. The [fusion/private-copy gate](LEWTAS_FUSION_PRIVATE_COPY_IDENTIFICATION_GATE.md) remains underdetermined because both subject-assignment stories can be paired by stipulation with the same physical and report equations. A subject-identity discriminator still requires independent individuation and calibration; the binocular task supplies neither. The result sharpens the demand on a future qualitative bridge instead of supplying one.

## Reproducibility

Run `python verification/binocular_appearance_memory_gate_test.py` and `python verification/binocular_appearance_memory_gate.py`. The [code](verification/binocular_appearance_memory_gate.py) uses exact fractions; its [receipt](verification/binocular_appearance_memory_gate.json) includes the invented table and mismatch bound. The tests check the stated equations, controls, swap symmetry and invalid inputs—not empirical adequacy, subject identity or consciousness. No participant data, correspondence, or intervention was involved.
