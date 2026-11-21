# A conditional physical mismatch measurement in the four-spin sector

## Result and limits

The previous [assay-error gate](HISTORY_MISMATCH_FIRST_PERSON_ASSAY_ERROR_GATE.md) requires an independently justified physical-history error bound `ρ`, but did not say how to obtain one. Here we construct a **complete, explicitly conditional measurement model** for the existing four-spin system. It specifies a way to learn the pair's preferred sign without using any affect reports, accounts for noisy spin readout and the common calibration error, and computes the conditional error in the critical observed `11` cell.

Under the exact toy equilibrium law, 19 independent, perfectly read calibration states select the wrong pair orientation with probability **0.00890**. If each of the four spin readings in a subsequent two-time episode has independent 5% error, the resulting physical-history error **conditional on observed `11`** is about **0.1704**, including calibration failure. These are model predictions with invented sensor parameters, not an experiment or a real calibration. The numerical answer averages over repeated calibration datasets; it is not automatically a valid bound conditional on a single realized calibration.

The positive result depends on identifying the **net** edge preference as the target. A concrete opposite-preference *parallel-channel* model has exactly the same entire four-spin equilibrium distribution and heat-bath kernel. It changes the preferred sign of one separately specified target channel while preserving the net interaction. A genuinely selective channel-removal experiment would distinguish these specific constructions, but selectivity has not been established in a real system. Thus the proposed physical measurement is conditional on substantive physical modeling, not a definition that solves the experiential bridge.

## 1. What is being measured

Reuse the [integrated candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) at middle coupling `t=1/4`, the same ordered one-step transition kernel and equilibrium distribution. Write `x=s₀s₁`, and let the preferred product be `τ∈{−1,+1}`. For a chosen physical interaction,

```text
q = (1 − τ x)/2.          C = (q⁰,q¹).
```

The existing candidate's **net outer-edge** convention sets `τ=+1`, so `q=1` for opposite signs. Here suppose that, as a separate experimental task, τ is not yet known to a physical observer and has to be learned. The spin encoding, the rule that a sign refers to this *net edge interaction*, the stationary model and the class of allowed systems must be specified independently of the target reports. A change of sign convention at one node must transport both x and τ, leaving q unchanged. Independent identification of physical variables is not accomplished by choosing a coding that looks like the answers.

For the unmodified chain the equilibrium probability is

```text
π(s) = (1/16)(1 + (1/2)s₀s₁)(1 + (1/4)s₁s₂)(1 + (1/2)s₂s₃).
```

Therefore `P(x=+1)=3/4` and `P(x=−1)=1/4`. Even conditioning on fixed external values `(s₂,s₃)`, the cross-product odds ratio of the four `(s₀,s₁)` states is

```text
[π(+,+,s₂,s₃) π(−,−,s₂,s₃)] /
[π(+,−,s₂,s₃) π(−,+,s₂,s₃)] = 9.
```

The factors depending only on `s₁,s₂,s₃` cancel. In a known pairwise Gibbs model with no hidden common causes or unmodeled pair terms, this conditional association has the sign of the **net pair coupling**, even with arbitrary finite one-site terms that cancel in the same cross ratio. It does not identify a separately hidden channel, establish causal intervention response, or show that an arbitrary brain signal is in equilibrium. Its magnitude is dimensionless; converting it into a physical energy needs a valid equilibrium model and energy scale.

## 2. A possible report-independent calibration

In the stated symmetric two-orientation model, choose an odd number n of independently sampled, perfectly measured equilibrium states, and let `τ̂` be the majority observed product `s₀s₁`. When the true preference is +, each product is positive with probability 3/4, so the wrong-orientation probability is exactly

```text
d_n = Σ_(k=0 to (n−1)/2) C(n,k) (3/4)^k (1/4)^(n−k).
```

By symmetry, the corresponding result holds when the model's preferred sign is − and the model is transported consistently. For these known probabilities, the smallest **odd** calibration sizes reaching each error target are:

| Failure target | Odd n | Exact wrong-orientation probability | Approx. |
|---:|---:|---:|---:|
| 5% | 9 | `6413/131072` | 0.04893 |
| 1% | 19 | `611828695/68719476736` | 0.00890 |
| 0.1% | 33 | `35084231326971293/36893488147419103232` | 0.000951 |

The arithmetic assumes **independent** equilibrium samples with the known 3/4 advantage and perfectly read spins. Consecutive states of the heat-bath chain are correlated and cannot simply be counted as independent calibrations; unknown preference strength, drifting interactions, selection and spin errors need separate uncertainty analysis. At zero or near-zero coupling, finite data may not determine the preference. The numbers are theoretical error rates for a fixed rule, not a sample-size recommendation or confidence claim for human data.

Crucially, the majority rule identifies a *net statistical preference only within this restricted model*. A stable 3/4 majority may be caused by other terms outside the model. Calibrating against experience itself, or selecting τ to fit target unpleasantness, would be circular for the present physical–experiential test.

## 3. Physical readout error in the actual disagreement cell

Assume, solely for the illustration, that for the two subsequent spin states each of the four recorded spin signs independently flips with probability `p=1/20`, independently of the true spin process and the separate calibration data. The physical classifier uses the same `τ̂` at both times. With correct orientation, a mismatch bit is wrong precisely when one of the two spin readings flips:

```text
e = P(noisy q ≠ q | τ̂=τ) = 2p(1−p) = 19/200.
```

For the exact equilibrium one-update distribution, the four true-history masses are `(295,41,41,71)/448` for `00,01,10,11`. Define `H` by applying τ̂ to both noisy recorded states. With perfectly known orientation,

```text
P(H=11) = 678631/4480000 ≈ 0.15148,
P(C≠11 | H=11) = 388493/2714524 ≈ 0.14312.
```

Thus 9.5% error on each marginal q readout does **not** translate into 9.5% posterior error in the selected two-time cell. It depends on both times and on the underlying cell frequencies. Two errors in a single episode are not the same as a single spin error.

Now include independent 19-state calibration and average over whether its majority selected the wrong sign. Wrong orientation complements **both** noisy q bits, so its mistakes are shared across the history. With `d=d₁₉`, the exact model gives

```text
P(H=11) = 373009915633097/2405181685760000 ≈ 0.15509,
P(C≠11 | H=11) = 2034055896400553/11936317300259104 ≈ 0.17041.
```

The [verifier](verification/four_spin_mismatch_measurement_gate.py) calculates these numbers from the original stationary law and transition kernel; an independent [test](verification/four_spin_mismatch_measurement_gate_test.py) enumerates the four spin-readout errors and the calibration outcome directly. This `ρ` is a **population probability averaged over repeated independent calibrations**, not an error guarantee conditional on the actual calibration dataset or a bound for each person. One wrong calibration may affect all trials, so repeated trials do not independently average it away. For a realized study, construct a justified confidence or posterior set for preference and sensor errors, propagate their uncertainty conditional on the calibration actually observed, and account for shared errors and participant/session clustering. Our 5% sensor error and perfect training readout are invented.

If, in addition, an *independently justified* target report error bound were `η≤0.10`, the prior gate's unrestricted bound would give `η+ρ≈0.2704<1/2` in this hypothetical repeated-calibration population. This would separate the two specified report-rate ranges under all the other assumptions. It does **not** establish the requisite experiential error, physically valid q, subject identity, or experimental test. Altering the balance of histories, sensor conditions, selection or calibration protocol changes the posterior and requires a fresh calculation.

### Correlated errors and reference-frame control

The independent flip model is not generic. If at one time a common sign reversal affects **both** spin measurements, their product and q are unchanged. If only one channel is systematically flipped, q is systematically reversed. An unrecognized orientation mistake flips both history bits. Reference artifacts, correlated channel errors, missed states and state-dependent sensor quality can therefore produce a substantially different `ρ` despite the same marginal per-spin error rate. No finite noise number should be transported without evidence that its error model and selection apply to the target cell.

## 4. The physical non-identification control

The net coupling can be fixed by the stipulated equilibrium distribution while a **particular component** remains unidentified. Let the unnormalized baseline factor for the original outer interaction be `1+(1/2)x`.

- **A:** the designated target is one alignment-preferring channel with factor `1+(1/2)x`.
- **B:** the designated target is an *opposite*-preferring channel with factor `1−(1/2)x`, while an independently postulated parallel alignment-preferring channel has factor `1+(4/5)x`.

For either `x=±1`,

```text
(1−x/2)(1+4x/5) = (3/5)(1+x/2).
```

The global constant cancels in normalization. With all other factors unchanged, A and B have exactly the same full four-spin equilibrium distribution. The same random-site heat-bath kernel depends only on ratios of those weights, so every finite passive spin-history distribution is also the same when initialized identically. Their **net** outer-edge preference is + in both; their stipulated *target-channel* preferences are opposite. Thus the calibration above correctly identifies the net q in both models, but it cannot identify a q defined by B's opposite target channel from passive observations. These decompositions are substantive physical models, not two gauge redescriptions of one declared target. If only the combined net relation is regarded as real, B does not falsify its identification.

One idealized distinguishing operation would remove only the designated target channel, retain all others and re-equilibrate. In A the outer pair then has `P(x=+1)=1/2`; in B the residual channel gives `P(x=+1)=9/10`. These are conditional predictions for two explicitly constructed models; an actual perturbation might change residual channels, hidden inputs, boundaries or the readout. The two models need not agree under arbitrary interventions. This positive-control logic follows the project's [selective-channel certificate](SELECTIVE_CHANNEL_CERTIFICATE_AND_HARMONIC_ALIAS.md) and [state-mismatch contrast gate](STATE_MISMATCH_CONTRAST_AND_FALSIFICATION_GATE.md); it is not a proposed invasive human intervention.

## 5. What would carry over to an actual experiment?

1. **Choose the target:** net effective interaction or a separately real channel; q cannot refer to both indiscriminately. Specify preferred relation, state variables, physical units/scale, local episode and subject-selection hypothesis without the held-out affect outcomes.
2. **Test the physical model:** assess stationarity, hidden sources, selection, nonstationary fields, interaction form and readout; distinguish observational correlation from selective intervention. A good fit does not prove the assumed Gibbs distribution or a unique decomposition. If channel selectivity and model adequacy are not justified, carry an identified set or stop.
3. **Calibrate physically:** use independent calibration data, allowed preference-strength and sensor-error ranges, and explicit dependence across calibration states and readouts. Estimate the posterior physical confusion **inside the observed history cell**, or bound it jointly with missingness and other uncertainty; training frequency is not itself a target-cell error guarantee.
4. **Anchor experience separately:** declare a defensible first-person unpleasant/neutral contrast and its report channel without setting the contrast equal to q by definition. Treat experience as valid data and recognize that independent quantitative error bounds may be difficult or unavailable. Compare fixed models on held-out participants or sessions and allow for context, intervention side effects and history selection.
5. **Keep the grounding question separate:** accurate physical q and a predictive, even causally supported, report relationship do not themselves explain why this quality is felt or choose experiential over neutral grounding. A failed particular implementation does not rule out every mismatch proposal.

No human signals or ratings are used here. The experimental data discussed in the [pain-history audit](CURRENT_MISMATCH_VERSUS_HISTORY_EXPERIENTIAL_GATE.md) did not measure q. The related [phase-lag gate](OBSERVED_PHASE_LAGS_VERSUS_PHYSICAL_FRUSTRATION_GATE.md) explains why observed EEG phase relations cannot be silently treated as known preferred interactions, and the [equilibrium/coarse-graining gate](EQUILIBRIUM_MISMATCH_AND_COARSE_GRAINING_GATE.md) treats other hidden-state and effective-energy ambiguities. The mathematical calculation neither derives brain physics nor establishes any actual subject.

## Reproduction and status

Run `PYTHONPATH=verification python verification/four_spin_mismatch_measurement_gate.py` and `PYTHONPATH=verification python -m unittest four_spin_mismatch_measurement_gate_test`. The [aggregate receipt](verification/four_spin_mismatch_measurement_gate.json) contains exact rational values. These checks are about the defined finite model and hypothetical measurement model, not the full theory. B4–B5/F2, B9/F3 and B10 remain open; C3 is **full structural and experiential intelligibility**, jointly with C1–C7.
