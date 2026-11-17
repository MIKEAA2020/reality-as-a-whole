# State mismatch: a bounded contrast and a falsification gate

## The advance

The prior [selective-channel certificate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) bounded **minimum structural frustration**. The integrated experiential candidate instead uses a **state-dependent excess over a minimum**. These are different quantities, and the difference matters for the proposed link to discomfort.

Here is a conditional bridge between them: when the *same* physical cost landscape applies to two states, its unknown minimum cancels in the difference of state excesses. A calibrated subset of channels can therefore bound part of that difference without solving the global optimization. However, the total difference is not identified unless the contributions of omitted channels are also bounded. An explicit pair of toy systems reverses the total ranking while retaining the same target-channel contrast and the same endpoint forces.

This is a mathematical design gate, **not a measurement in a brain**. It gives neither a new theory of neural oscillations nor proof that discomfort is mismatch. It identifies exactly what must be measured before one version of the idea can be tested against experience.

## 1. Definitions and the cancellation

Fix one finite, experimentally justified local system and one time window. In a simplified first-harmonic potential model, write

```text
E(z) = Σ_e k_e [1 − cos(x_e(z) − a_e)] + E_other(z),
F = inf_z E(z),                    D(z) = E(z) − F.
```

Here `z` is the state, `x_e` is the oriented phase difference, `a_e` its preferred offset, and `k_e≥0`. `E_other` represents any other modeled costs, including channels not individually measured. The infimum is over the **same admissible state space** in both comparisons; require finite costs and finite F. E is a stipulated mismatch cost, not automatically thermodynamic energy or dissipated heat.

For two states `A` and `B` in that same fixed landscape,

```text
D(A) − D(B) = E(A) − E(B).                       (1)
```

The unknown F cancels exactly. This applies to arbitrary additional fixed terms, even if F cannot be computed. It does **not** say the difference is known without observing those terms. The equation fails as a direct cancellation if the treatment changes the admissible space, weights, preferred offsets, remaining costs, system boundary, or other part of the landscape: then `F_A` and `F_B` may differ. A current response cannot establish those invariances by definition. A different account would be needed for non-potential, history-dependent or time-varying dynamics.

## 2. Bounding an identified channel in both states

Assume an independently selective, phase-independent attenuation of a target channel produces the prior gate's contrast `y(x)=λ k sin(x−a)`. Measure the gate contrast at phase differences `0` and `π/2`, obtaining `ŷ₀, ŷ₁`, each with a jointly valid absolute error bound `ε`. Assume the *same* λ in those two calibration settings, a stable original channel, and independently justified bounds `0 < λ_min ≤ λ ≤ λ_max`. Let

```text
ρ = √2 ε,                   R = hypot(ŷ₀, ŷ₁),
â = atan2(−ŷ₀, ŷ₁),        δa = asin(ρ/R),
k_lo = (R−ρ)/λ_max,         k_hi = (R+ρ)/λ_min,       when R>ρ.
```

The first three bounds extend the prior result with an upper weight bound. The derivation is the triangle inequality on the two-component response, together with its angular uncertainty; the positive lower bound on attenuation is essential for `k_hi`. If `R≤ρ`, the offset is unresolved and these angle formulas must not be used. If λ can be arbitrarily small, `k_hi` is not finite from these data: with the exact same response magnitude 1, `λ=1, .1, .01, …` permits `k=1, 10, 100, …`. The measured response only identifies `λk`, not k itself.

For condition `t=A,B`, suppose the measured current phase difference `x̂_t` has an independent, simultaneous circular error bound `δx_t`—independent of the report being predicted, not necessarily statistically independent of other errors. Define

```text
d_t = dist_circle(x̂_t, â),       η_t = δx_t + δa,
f_t^lo = 1 − cos(max(0, d_t − η_t)),
f_t^hi = 1 − cos(min(π, d_t + η_t)).
```

The circular triangle inequality and monotonicity of `1−cos(d)` on `[0,π]` imply the true factor `1−cos(x_t−a)` lies between these limits. If the target channel's **same** positive k and a apply in both states, its true contribution to `E(A)−E(B)` lies in

```text
z_lo = f_A^lo − f_B^hi,        z_hi = f_A^hi − f_B^lo,
[L_e, U_e] = [min S, max S],
S = {k_lo z_lo, k_lo z_hi, k_hi z_lo, k_hi z_hi}.  (2)
```

The interval is conservative: it permits combinations of calibration, phase errors and endpoints that might not all be jointly realizable. Using the same k on both sides, rather than allowing separate k values for A and B, is crucial. The formulas concern simultaneous states; for an extended episode, bound the time-averaged cost with justified time-resolved errors and a specified weighting. In general, `mean[1−cos(x−a)]` is **not** `1−cos(mean[x]−a)`, and a mean phase alone does not suffice. A gauge or reference redefinition that adds the same angle to `x_t` and `a` leaves every distance and bound unchanged; this is a limited coordinate-invariance check, not proof of full substrate independence.

Without `λ_min`, a one-sided positive lower bound can still survive if `z_lo>0`, because `k≥k_lo` makes the channel difference at least `k_lo z_lo`. But if `z_lo<0`, the lower bound can be unbounded below without some finite upper bound on k. A gain bound cannot be inferred just from collecting more trials.

## 3. Numerical example and the omitted-channel problem

For the **hypothetical** gate contrast `(ŷ₀,ŷ₁)=(0,−1)`, take `ε=.1`, `λ_min=.5`, `λ_max=1`, phase error `.05` radians for each state, `x̂_A=0`, `x̂_B=π`. The computed bounds are

```text
k ∈ [0.85858, 2.28284],   δa ≈ 0.14190 radians,
E_target(A) − E_target(B) ∈ [1.68564, 4.56569].
```

Thus, if all assumptions hold jointly, this *one channel* costs more in A than B. This number is **not an observation**, not a certified brain quantity, and not yet a bound on total D.

Suppose for the selected set `S` the sum of intervals (2) is `[L_S,U_S]`. Let `H(z) = E(z) − Σ_{e∈S} E_e(z)` be the **entire residual**, including unselected terms in the original sum as well as `E_other`. Assume an independently defensible bound `h` establishes

```text
|H(A) − H(B)| ≤ h.
```

Then equation (1) yields the total conditional bound

```text
D(A) − D(B) ∈ [L_S−h, U_S+h].                     (3)
```

No independence between edge errors is required if their error bounds hold **simultaneously**; if they are statistical confidence intervals, simultaneous coverage—including the residual bound—must be designed and accounted for. A positive certificate of total excess difference requires `L_S>h`. Additional nonnegative costs do not by themselves establish a useful h: two nonnegative terms can differ by arbitrarily much between states. If h cannot be established, report the global contrast as unidentified rather than setting h to zero. The selected channel bounds are only as valid as the declared channels, model, timing, gates, sample, and systematic error control.

### Concrete reversal despite the same selected-channel evidence

Take `x_A=0`, `x_B=π`, with a unit antiphase channel `E_target=1+cos x`. Its exact gated contrast is `−sin x`, so it gives `(0,−1)` at the two calibration settings; it contributes `+2` to the A-minus-B cost difference.

- **Model 1:** no extra phase cost. Total A-minus-B difference is `+2`.
- **Model 2:** add a parallel in-phase cost `2(1−cos x)`. Total A-minus-B difference is `−2`.

The target-channel gate contrasts agree at the two quadratures, and both models' **ungated net forces** vanish at A and B. Nevertheless their total excess rankings reverse, since each model uses its own fixed landscape and F cancels within it. The models are **not** claimed to be indistinguishable under every measurement: their ungated forces at `π/2` differ (−1 versus +1), and measuring the separate on/off forces there could reveal the extra term. Other unmeasured channels and hidden outputs are likewise possible. This exact example shows that the specified *subset of observations* is insufficient, not that all interventions must fail.

The earlier [harmonic-alias counterexample](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) adds another danger: two gate settings cannot establish the first-harmonic law, even with exact readings. A held-out phase rejects the particular alias there, not all functional alternatives. Thus both **channel coverage** and **model adequacy** must be independently checked.

## 4. How this becomes a falsifiable pain hypothesis

Consider a deliberately strong and narrow hypothesis—not a premise adopted by the user. For a prespecified, valid subject boundary, time window, fixed landscape and separately measured unpleasantness U, suppose

```text
U = g(D),  and  g(d₂) − g(d₁) ≥ s(d₂−d₁) for d₂ ≥ d₁,
```

where `s>0` and the scale and lower slope s are fixed *before* the test using independent calibration. This strong monotonic minimum-slope condition is not a consequence of experience or of the graph model. It is necessary for this particular quantitative decision rule; mere monotonicity would not yield the same margin. If (3) establishes `D(A)−D(B)≥δ>0`, then the hypothesis entails `U_A−U_B≥sδ`.

If independently measured reports `Y_t` satisfy a jointly valid, prespecified absolute readout-error bound `|Y_t−U_t|≤r_t`, the same assumptions entail

```text
Y_A − Y_B ≥ sδ − r_A − r_B.                      (4)
```

A reliably measured difference below that threshold challenges **the conjunction**: fixed landscape, complete error bounds, physical model, calibrated subjective readout, subject boundary, and this particular quantitative bridge. It does not isolate which premise failed, disprove every possible mismatch proposal, or prove the neutral-ground rival. Overlapping intervals are inconclusive. For an actual study, choose adequate margins, reporting and missingness rules, sample sizes and multiple-comparison handling in advance; the deterministic inequality is not a statistical power analysis. Unpleasantness self-report is important first-person evidence but is not assumed to be a noiseless, universal cardinal metric. No currently validated error radii or slope are supplied here.

Prediction should also be compared against prespecified stimulus/context variables and established brain predictors on held-out participants and conditions, as in the [PAINgen benchmark](PAINGEN_UNPLEASANTNESS_BASELINE_AND_MISMATCH_GATE.md). Signatures and outcome may have different measurement modalities and timing; the benchmark did not measure channels and does not already test (4). Predictive improvement, even if genuine, would not by itself establish metaphysical identity or that experience grounds physics.

## 5. Research design and known work

1. **Construct validity first.** Independently specify components, how a channel is localized and gated, its phase reference, state measurement, boundary, potential form and physical units. Measure gate stability and phase coverage; include higher harmonics, amplitude, delay and common-input rivals. Work on phase-response curves and neural synchronization is established, with important weak-coupling and oscillatory assumptions ([Ermentrout et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2894948/)); do not assume that scalp EEG or fMRI resolves selective neural channels.
2. **Bound the unmeasured remainder.** Provide instrumentation and intervention controls capable of bounding its *change*, not merely its absolute nonnegative value. If the landscape can shift under intervention, measure or bound that shift and the change of F rather than applying (1). Prove simultaneous error coverage under repeated observations, family dependence and drift.
3. **Use an independent target and competing predictions.** Fix the mismatch definition without fitting reports on the test set; collect unpleasantness, intensity, affective context and other relevant reports independently. Separate a trial's stimulus-evoked activity from a prestimulus predictor. Include nonpainful aversion, neutral states, pleasant challenge and relief where ethically appropriate; do not infer lack of experience from absence of a report.
4. **Check interventions rather than name them selective.** Randomized, blinded, safely reviewed manipulations need sham and sensory controls, measured fidelity and clear causal assumptions. For example, reported work on [perceived sensorimotor synchrony and pain](https://www.nature.com/articles/s42003-025-09076-7) already explores synchrony and analgesia; perceived behavioral synchrony is not selective identification of our internal channels. Transcranial electrical stimulation can also affect peripheral and retinal pathways, even below the threshold of conscious phosphene report ([Schutter et al.](https://doi.org/10.1016/j.ijpsycho.2025.113285)). Such interventions cannot simply be assumed to isolate a channel or establish a mediation mechanism. No experimental protocol here is a recommendation to induce harm.
5. **Separate empirical and foundational claims.** Even passing a prespecified report prediction and intervention comparison would not by itself select experiential over neutral grounding or derive plurality, necessity, quantum physics, or emergent spacetime. It could constrain a specified physical–phenomenal bridge and prioritize or reject particular operational models. The absolute remains timeless in the framework; local laboratory timing does not posit an external cosmic clock.

## Reproduction

Run `python verification/state_mismatch_contrast_certificate.py`; the [aggregate receipt](verification/state_mismatch_contrast_certificate.json) includes the numerical example, reversal and **20,000 seeded candidate cases** (including unresolved cases), checking numerical interval containment and reference-shift invariance. The reasoning above establishes the stated conditional bounds; random checks exercise the implementation only. No biological data or newly measured experiences are involved.
