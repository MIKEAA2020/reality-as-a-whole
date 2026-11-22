# Afterimages: the probe changes what is reported

## Main result

A later test can do more than passively reveal a fixed stored color. Published studies report that **luminance contours presented after adaptation change afterimage judgments**, and that their effects can be greater for afterimages than for appearance-matched physical color patches. This matters for the [eye-history model](BINOCULAR_APPEARANCE_VERSUS_EYE_HISTORY_MODEL.md): its fixed probe was an explicit simplification, not a context-independent measurement of a hidden experience.

I also constructed a small identification check. A change in the color needed to null an afterimage rules out a particular **common-gain-only** model, but it does not by itself distinguish a selectively amplified adaptation signal from an adaptation-dependent decision criterion. The two latter constructions can predict exactly the same responses. Their equivalence is a deliberately constructed example, not a claim about the actual mechanism.

The studies below concern binocular viewing or spatial-contour effects, not the specific dichoptic eye-history experiment proposed previously. They motivate controls; they do not establish a numerical contour effect in that proposed experiment, identify any subject, or solve qualitative blending. This is a literature and finite-model audit, not a reanalysis of original participants.

## 1. Same adaptor, different later contours

[Anstis, Vergeer and Van Lier (2012)](https://jov.arvojournals.org/article.aspx?articleid=2193772), *Journal of Vision* 12(10):2, [DOI](https://doi.org/10.1167/12.10.2), experiment 1, used a four-color plaid made by superimposing orthogonal color gratings. Five color-screened college students viewed a repeating cycle of one second of adapting plaid, one second of a horizontal-line test, the plaid again, and one second of a vertical-line test. They adjusted colored bars to match the afterimages. A separate naming exercise involved six naïve observers; these are not automatically an independent replication of the quantitative sample.

The authors report different afterimage patterns with the two test orientations and matching settings approximately complementary to the component gratings rather than the four plaid colors. They interpret this as spatial averaging constrained by the test contours. The repeated adaptation and sequential testing are relevant: this is **not** a comparison of two simultaneous observations of one identical microscopic brain state. Fixation, test order, response settings and the repeated top-ups can matter. Nor does the hidden mathematical decomposition of a plaid prove that participants experienced its component gratings during adaptation.

[Kim and Francis (2011)](https://jov.arvojournals.org/article.aspx?articleid=2191780), *Journal of Vision* 11(3):23, [DOI](https://doi.org/10.1167/11.3.23), tested a specific contour-based filling-in model with both simulations and human reports. In experiment 1, 20 students viewed a colored star for 1,200 ms, then successive test contours and a mask; they reported color at the points or center. The paper reports that an appropriately placed inner contour could block the central afterimage, but other boundary positions did not behave as a simple universal trap would predict. In experiments 3a and 3b, 20 main-experiment participants in each reported afterimage boundaries relative to test contours of varied sizes. The reported boundary more closely followed the inducer than the contour in those conditions, contrary to the tested model's prediction. These are response-based comparisons with their own display and task limitations; they show the value of a model that can be *challenged*, not proof that all filling-in models fail.

## 2. A nulling experiment tests more than visibility

[Powell, Bompas and Sumner (2012)](https://jov.arvojournals.org/article.aspx?articleid=2193769), *Journal of Vision* 12(10):17, [DOI](https://doi.org/10.1167/12.10.17), studied contour effects with binocular viewing and eye tracking:

* In experiment 1, **eight observers** (seven naïve, one author) compared afterimage saturation against physical patches. The reference patch in a separate physical-stimulus stage was set individually from the no-contour afterimage match. The authors report a contour-by-stimulus-type interaction, `F(1,7)=11.66, p<0.01`: the reported saturation shift was greater for afterimages than for similar physical stimuli. A match on selected attributes is not identity of whole experiences or of all underlying visual representations.
* In experiment 2, **four observers** adapted for 1.5 seconds to a pink or green circle. A 700-ms test patch, with or without a contour, varied across seven color levels; observers made pinkish/greenish judgments. The point of perceived gray was estimated from those judgments. The authors report that the contour moved the null away from physical gray for all four (`t(3)=6.51, p<0.01`). Their account is that more physical color was needed to cancel the afterimage with a contour.
* Experiment 3 compared sharp and blurred luminance pedestals in the same four observers; the authors report larger mean null shifts for sharp than for blurry/no pedestal. Their edge-blur control addressed one alternative, although the blur profile initially used for physical patches came from a pilot in one observer. These are small studies, with repeated trials nested in participants; the reported tests are the authors' analyses, not our independent replication.

The contrast is stronger than simply noting that observers see a contour. A common multiplicative boost to both the afterimage and the physical nulling signal would improve their joint strength but **would not change their balance point**, under that model's assumptions. A shift challenges that particular account. It does not automatically prove that a contour changed a perceptual representation rather than another history-dependent part of the response process.

The study proposes that afterimages may be especially ambiguous and susceptible to object-consistent context. That is an interpretation, not a direct observation of the brain's uncertainty calculation. A later study by [Witzel (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12579601/) reports afterimage color measurements across several stimulus sets and favors a cone-adaptation account over specified opponent-color predictions. The paper makes broad mechanistic claims; for our purposes it is an additional warning **not to treat the toy's sign reversal as a universal color law**. Different stimuli and readouts need separate tests, and these psychophysical observations alone do not locate every relevant process.

## 3. An exact counterexample: gain versus criterion

Let `h` be a signed adaptation-dependent state, `p` a calibrated physical nulling input, and `g>0` a contour-dependent coefficient. Define the binary response using a decision margin `m`; positive and negative values favor opposite responses. We compare three **stipulated** models:

| Model | Decision margin | Null `p*` where `m=0` |
|---|---|---|
| Common gain, fixed criterion | `g(p − h)` | `h` |
| Selective adaptation gain | `p − gh` | `gh` |
| Fixed adaptation plus shifted criterion | `(p − h) − (g−1)h` | `gh` |

In the second model the contour multiplies the adaptation contribution. In the third it leaves the adaptation term fixed but changes the decision criterion by `(g−1)h`. That criterion depends on **both** adaptation history and contour; it is not a mere fixed response bias. The two margins are algebraically identical for every `p,h,g`, so the same response link and noise distribution yield identical psychometric choice probabilities, slopes and nulls. The third model is a constructed rival, not evidence that the participants actually used such a criterion.

For invented values `h=1`, `g=1` without and `g=2` with a contour, the common-gain nulls are `(1,1)`; both alternatives predict `(1,2)`. A shifted null therefore rejects the common-gain-only package if its other assumptions are justified, but cannot distinguish these two alternatives. If `h=0`, the two alternatives also give the same unadapted control under both contexts: a no-adaptation control alone cannot rule out the history-dependent criterion. Increasing trials, testing additional `p` values, or varying `h` and `g` within this same observation family does not separate models whose response functions remain identical. That does **not** mean every conceivable independent physiological or behavioral measurement would fail to distinguish them.

The [exact-fraction script](verification/afterimage_probe_context_gate.py) verifies the example over **30** invented conditions, and the [tests](verification/afterimage_probe_context_gate_test.py) also check values outside that grid. The general equality follows algebraically, not from the finite enumeration. Its probability link is invented and bounded for the checked inputs; no fit, clinical measurement or estimate of probability in humans is implied.

## 4. Consequences for the earlier eye-history test

The previous model's `Δ=4ka` assumed identical probe context and a fixed readout. If contour condition `c` selectively scales the history term by `g_c`, the same stipulated eye-history equations instead give

```text
Δ_c = 4 k a g_c.
```

The originally calculated value remains valid only for the stipulated fixed context with `g_c=1`; it was never an empirically calibrated constant. Different measured `Δ_c` values would show an eye-history-by-context **response interaction**, not by themselves establish where the modulation occurred. A suitable history-dependent criterion can reproduce the same binary responses. The two models both retain information about history; the criterion counterexample does **not** erase evidence of input-dependent processing or restore the restrictive appearance-only candidate.

For a future study, use the original randomized A/B eye swap at **each** probe context. Prespecify `Δ_c` and their difference, keep delay and test geometry comparable, and include no-adaptation, eye-swap, physical-reference and contour-without-color controls. Independent pilot trials should calibrate appearance equivalence, response scale and any proposed gain; carryover, optical leakage, fixation and context effects need assessment. PSEs, nulls, response slopes and confidence should not be treated as interchangeable or as direct recordings of latent experience. Context conditions can also change the physical probe itself, so compare A/B within the *same* context before comparing contexts.

To discriminate selective signal modulation from a history-dependent criterion, one needs an **additional, independently justified constraint or measurement** that responds differently to the two candidate processes. A possible research route is a separately calibrated criterion-sensitive manipulation or physiological measurement with a frozen linking model and validated error bounds for this exact task. It is not enough to rename another report, assume the criterion is fixed, or claim that a measure is independent simply because it is indirect. If the independent premise cannot be defended, the two mechanisms remain unresolved.

## 5. What this contributes to the framework

The experiments make visual organization and context empirically important: an afterimage response is not merely the adaptor's color copied forward. The finite gate separates an observable null shift from one particular mechanistic explanation. Neither the eye-indexed memory, the contour-gating story, nor a response criterion demonstrates that a hidden local experience or separate subject persisted. Conversely, not reporting a color does not demonstrate its experiential absence. Lewtas's question—what selects, constitutes and owns felt qualities—remains open even if the operational response is predicted exactly.

In a timeless whole, the adapting and probe stages may be represented as locally ordered relations; making that representation does not by itself derive the experiential state, its subject, or a color-quality composition law. The [fusion/private-copy identification gate](LEWTAS_FUSION_PRIVATE_COPY_IDENTIFICATION_GATE.md) therefore retains its requirement for an independently defended subject-identity assay.

**Reproduce:** `python verification/afterimage_probe_context_gate_test.py` and `python verification/afterimage_probe_context_gate.py`; the [receipt](verification/afterimage_probe_context_gate.json) contains the invented example. No new participant data or intervention was used.
