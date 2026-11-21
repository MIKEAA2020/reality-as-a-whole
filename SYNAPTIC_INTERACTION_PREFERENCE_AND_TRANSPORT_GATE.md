# A concrete synaptic calibration—and why it does not yet reach experience

**Decision: develop the physical calibration in a controlled preparation, but stop before a human `q`–unpleasantness comparison.** A directed neuron-to-neuron connection gives a more specific target than a pair of EEG channels. Paired recordings can probe such connections, but an evoked effect is not automatically a selective measurement of that synapse, an equilibrium preference, or the same interaction during a person's report. The test below is a conditional design and invented-probability control, not a new experiment, established neural `q`, or clinical protocol.

The [fixed plan](SYNAPTIC_PREFERENCE_CALIBRATION_FIXED_PLAN.md) predates the calculation. The existing published rTMS outcomes and literature were already known; no new individual data or recordings were examined. This is not a preregistered analysis of those published studies.

## 1. One specified target

Consider a pair of identified cells in a consented, clinically resected human cortical slice: A is presynaptic and B postsynaptic, and their candidate connection is characterized with paired electrophysiology. Let `a=+1` denote an A spike in a prespecified input window and `a=−1` no A spike there; `b=+1` denotes a B spike in a **subsequent** fixed window and `b=−1` no B spike. Fix actual window lengths, cell selection, baseline state, background inputs, repeated-stimulation history, spike-detection criteria and reference frame in an approved laboratory protocol before seeing the calibration. These bin values describe firing, not positive/negative feelings.

In a specified context, randomize an instruction or validated intervention to set A's input-window spike versus no spike. For each pathway-gate condition `g`, define

```text
p(g,a) = P(B spikes in its window | intervention sets A=a, g, fixed context)
D_g = logit p(g,+1) − logit p(g,−1).
```

The target is the **contribution `K` of the designated A→B pathway** to `D_on`, not simply the observed association of their spontaneous spikes. A narrowly defined gate is hypothesized to attenuate that contribution, and a remaining contrast is denoted `R_g`:

```text
D_on = K + R_on,   D_off = (1−λ)K + R_off,
Δ = D_on − D_off = λK + δ,   δ = R_on − R_off.
```

The additive decomposition on this log-odds scale is a substantive assumption; neither randomization nor a drug, stimulus, sham or circuit label establishes it. In particular, an intervention on A can affect other routes, and changing a synaptic pathway can alter network state and other influences. `K` is an effective causal contrast under these specific preparations, not automatically an isolated receptor conductance, universal synaptic sign, energy or equilibrium coupling. If `λ>0` and a defensible independent bound `|δ|≤c` holds, a confidence interval `[L,U]` for Δ gives a positive sign certificate if `L>c` and a negative one if `U<−c`. If neither condition holds, the sign is unresolved under this certificate. For a finite magnitude interval also require an independently justified lower attenuation bound. All such bounds must apply to the **same physical pair, state and measurement**.

### Why this is not yet the project's `q`

A conditional binary logit can be written `P(b|do(a)) ∝ exp[h b + J a b]`, with `D=4J`, for a fixed context. This is an algebraic representation of a binary response, not proof that the joint neuronal system has physical energy `−Jab`, is in equilibrium, or has the pair preference needed by E-L. In particular, a positive evoked effect does not establish that **joint silence** is physically preferred when A is silent. The normalized conditional also contains an `a`-dependent normalizer; treating this conditional as a symmetric joint physical energy requires an independently validated physical model and admissible interventions. Further, the variables here are **lagged**, whereas the earlier E-L bit was defined on a current pair. Any lagged version needs its own justified physical and experiential bridge.

Only if this pair-potential interpretation, component separation, state transport and nonzero sign have been independently established may the proposed operational extension use `τ=sign(K)` and `q=(1−τab)/2`. For `K>0`, the encoding would call both `(a,b)=(+,+)` and `(−,−)` matched; for `K<0`, the mixed pairs would be matched. The first-person quality mapping remains a separate hypothesis. No q is assigned to actual recordings here.

## 2. What evidence could justify—or defeat—the calibration?

Paired/multipatch recordings are a real method: [human cortical slice work](https://pmc.ncbi.nlm.nih.gov/articles/PMC13356068/) describes directly probing connections and their properties; [human neocortical work](https://www.nature.com/articles/s41467-024-53901-2) shows synaptic responses can depend on presynaptic membrane state. These sources support feasibility of *some physical measurements*, not the proposed q, within-person transport or pathway selectivity. [Bartram et al.](https://elifesciences.org/reviewed-preprints/86820) explicitly describe how their high-chloride patch solution shifted reversal and made ordinarily GABAergic inputs appear inward under their recording conditions. A current's sign is therefore not a universal spike-effect or preference sign. [Instrumental-variable work](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011574) also illustrates that common input and stimulation of other cells can confound connectivity estimates; its method is not assumed valid here without its own conditions.

A credible validation would require, at minimum:

1. **Stable identity and intervention.** Independently verify the same A, B and directed pathway; randomize A-setting and gate order within controlled, prespecified state strata; check actual A spikes and stimulation leakage. Randomized assignment estimates an assignment effect unless compliance and other intervention assumptions justify a set-spike contrast. Address failed assignments without postselection bias. Verify that the gate changes the designated pathway in the target state, and bound—not merely assume—its attenuation.
2. **Residual and model controls.** Use orthogonal pathway assays and appropriate negative/positive controls, including sham and target-absent controls where available, to bound direct gate effects, alternate routes, hidden inputs, readout shifts and nonlinear interactions **on the relevant log-odds scale**. A target-absent preparation alone need not bound cross-talk in the target-present one. Bound uncertain attenuation, drift and model error jointly; a precise on/off difference does not supply its own `c`. If no justified bound is available, do not certify `τ`.
3. **Temporal and sensor validity.** Validate detection errors, windows, stimulus artefacts, background state, washout, plasticity, stability, and changes caused by patching or the gate. Test the assumed response model on independent calibration blocks; goodness of fit alone cannot establish a unique channel decomposition or an equilibrium law. Use uncertainty methods valid for repeated and clustered recordings; trials are not independent merely because their timestamps differ.
4. **Transport and ethics.** Ex vivo, removed tissue has neither the intact person's contemporaneous network nor a corresponding first-person report. Calibration in a separate slice—even from the same donor—does not identify the same live pathway, state or episode. This is a fundamental design gap, not just a small sample. No new invasive human procedure is recommended. Ethical approval, consent and safety are prerequisites for any actual research; none is proposed here as a clinical procedure.

## 3. Fixed invented-probability control

These probabilities are **invented**, not measured; let `on/off` denote the hypothetical pathway-gate conditions and `−/+` the A intervention states:

| Gate | `P(B spike | do(A=−1))` | `P(B spike | do(A=+1))` | `D_g` |
|---|---:|---:|---:|
| on | 1/5 | 3/5 | `log 6 ≈ 1.79176` |
| off | 3/10 | 1/2 | `log(7/3) ≈ 0.84730` |

`Δ=log(18/7)≈0.94446`; both outcomes have positive probability in each arm. These are idealized interventional probabilities, **not** proof of gate or state-intervention validity.

Suppose, counterfactually, 10,000 independent observations in each of the four arms have exactly those frequencies. For simultaneous nominal 95% coverage of the four probabilities, Hoeffding plus a union bound gives `ε=sqrt(log(8/0.05)/(2×10000))≈0.01593`. Propagating endpoints through the logit and contrasts gives the conservative interval `[0.64095,1.25252]` for Δ. Its coverage assumes the relevant independent, stationary Bernoulli sampling and fixed arms; the numerical interval is not an empirical confidence interval. For independent bounds `1/2≤λ≤1` and `|δ|≤c`:

| Invented systematic bound `c` | Resulting K interval | Decision |
|---:|---:|---|
| 0.3 | `[0.34095, 3.10504]` | positive under the assumptions |
| 1.2 | `[−1.11810, 4.90504]` | sign unresolved |

These bounds are merely sensitivity inputs, not characterized device properties. If the attenuation/drift bounds are themselves statistical estimates, their failure probabilities must be budgeted jointly with the sampling interval; the 95% claim here does not cover them or model validity.

### The same observations can hide opposite channels

With perfect knowledge of all four arm probabilities and `λ=1`, both constructions below yield identical `D_on`, `D_off`, and therefore identical B outcome probabilities for both randomized A states in each gate arm. Their gate-specific one-body intercepts are set to reproduce the given no-spike probabilities.

| Target `K` | `R_on` | `R_off` | `δ` | Compatible with `c=1.2`? |
|---:|---:|---:|---:|---|
| `1` | 0.79176 | 0.84730 | −0.05554 | yes |
| `−1/4` | 2.04176 | 0.84730 | 1.19446 | yes |

Thus even a randomized, fully supported on/off factorial experiment with exactly known outcomes need not determine the designated component's sign. These are alternative formal decompositions, not claims that either is biologically real. They demonstrate why a justified residual bound or a different channel-specific experiment matters. A sign certificate under the narrower assumed bound does not establish the binary-potential bridge.

Reproduce using `python verification/synaptic_preference_calibration.py` and `python -m unittest discover -s verification -p 'synaptic_preference_calibration_test.py'`. The [receipt](verification/synaptic_preference_calibration.json) records the calculations. The tests check the exact odds, all four outcome probabilities in both rival models, interval containment, both sensitivity decisions, fail-closed behavior and `q` invariance under sign relabeling **when τ is transported too**. Those algebraic tests do not validate the neuroscience assumptions.

## 4. Decision for the available pain studies

The [Li rTMS](https://www.nature.com/articles/s42003-024-07129-x) and [Zhang tDCS](https://www.nature.com/articles/s42003-025-08304-4) studies report scalp EEG and separate unpleasantness ratings, not the targeted, calibrated individual A→B pair above. Their public repository metadata were previously located; the archives, event linkage and calibration are uninspected. The Jin study's individual-data availability remains unverified. Neither pairing scalp channels nor applying the slice calibration to those subjects would establish the same physical interaction. **Stop: no target q, held-out fit or empirical q result follows.** This is not proof that a suitable measurement can never be developed.

If a future ethically approved dataset does meet every gate, freeze a new plan *before accessing its target outcomes*. One concrete analysis design is: fixed candidate pair, time bins and subject-incidence rule; report-independent per-pair calibration with joint uncertainty; verified same-person, same-episode state/report linkage; and participant-held-out comparison of (M0) stimulus/context alone, (M1) M0 plus prespecified ordinary physiology, and (M2) M1 plus calibrated q, using the **same eligible cases**. Prespecify an unpleasantness rating as the primary outcome, participant-weighted mean squared prediction error as primary metric and M2−M1 paired difference, participant-cluster uncertainty, nested training/tuning, missingness rules and calibration-error propagation. A fixed protocol should allocate familywise error across physical sign calibration and the predictive comparison, and report unclassified cases rather than silently dropping ambiguous τ. Concurrent pain-intensity ratings, if used, are a distinct post-stimulus report comparator, not a substitute for unpleasantness or an automatic baseline available before the episode. Treatment effects and prediction must not be mislabeled as mediation or proof of phenomenal constitution.

This gate leaves [PAINgen's 21 residual discrepancies](PAINGEN_PARTIAL_RUN_AND_REMAINING_MEAN_AUDIT.md) open pending the original processing records. C3, B4–B5/F2, B9/F3 and B10 remain open. The four-spin example remains a mathematical sector, not a model established in this preparation.
