# When does regulating variation actually help?

## Result and place in the framework

Noble's proposal that organisms can harness variation becomes empirically useful only when we specify **which variation, for which task, in which context and compared with what**. This note works out a small, exact comparison with a matched average rate of exposure to an added-noise intervention. Its key result is that the advantage of context-sensitive allocation depends on both the reliability of the context signal and **differences in the intervention's causal effect across contexts**. A noisy or misinterpreted signal can eliminate or reverse the benefit. More subtly, even exact context-specific randomized outcome averages and exact signal rates need not predict the gated policy's outcome: the signal can itself identify another outcome-relevant difference within each context.

This is an application of existing ideas about treatment-effect heterogeneity and resource-constrained policy, not a claim to have invented them. It sharpens the experimental question in the [Noble audit](DENIS_NOBLE_ORDER_DISORDER_EVOLUTION_AND_EXPERIENCE_AUDIT.md); it does **not** supply an empirical biological result, a consciousness detector, a solution to subject constitution, or the project's full structural and experiential intelligibility. The checker uses exact toy probabilities and no participant data.

## 1. Known work and what we add

[McDonnell and Abbott, *What Is Stochastic Resonance? Definitions, Misconceptions, Debates, and Its Relevance to Biology*](https://doi.org/10.1371/journal.pcbi.1000348) discuss ways noise can improve performance under specified conditions and warn that not all observed variability is functionally exploited. The abstract, introduction and beginning of the historical section were read; the rest of the article, equations shown as images and figures were not systematically checked. This note is **not** a derivation of stochastic resonance; it does not posit a threshold detector or establish an optimal noise level.

[Wang and Wilson, *Separating random and deterministic sources of computational noise in explore-exploit decisions*](https://doi.org/10.1371/journal.pcbi.1014026) distinguish variation attributable to repeated stimuli from residual variability in a model of human choices; the residual can also contain unobserved deterministic influences. Only the abstract and introduction were read; the results, methods, figures, supplementary material, linked data and code were not independently analyzed. Their study does not test this note's biological model.

[Sun, Munro, Kalashnov, Du and Wager, *Treatment Allocation under Uncertain Costs*](https://arxiv.org/html/2103.11066v5) address treatment allocation, heterogeneous effects, uncertain costs and policy comparison against uniform assignment. Only the abstract and introductory section were read, not the complete preprint or proofs. Our special two-context, equal-rate calculation is an elementary illustration of the general pre-existing allocation idea, **not** a general allocation theorem, new statistical method or claim of literature-wide novelty. Physical noise and medical treatment have different meanings; this is a formal analogy, not a clinical recommendation.

## 2. One explicit causal comparison

A unit encounters one of two **pre-intervention** states `E=0,1`, with probabilities `w0,w1>0`, `w0+w1=1`. Let `A=0` mean baseline and `A=1` mean a prespecified additional variability intervention: for example an independently calibrated zero-mean fluctuation with a specified distribution and intensity. This is an abstract intervention, not a claim that all noise has the same effect. Let `Y` be a bounded functional outcome, with the same direction and units in both states. Write

```text
μea = E[Y(a) | E=e],        δe = μe1 − μe0.
```

Here `Y(a)` denotes the outcome under the indicated intervention in a defined population and horizon; causal interpretations require consistency, adequate randomization/exchangeability, noninterference and appropriate handling of missing outcomes. Potential-outcome notation is an analytic device; it does not postulate an external simulator, a temporal creation of possibilities, or a probability measure over the whole.

Compare two policies, with `pe=P(A=1|E=e)`:

- **Context-gated:** the high-variation intervention is applied at rate `pe` in state `e`.
- **Uniform-rate:** apply it at the same rate `r=w0 p0+w1 p1` independently of state and its proxy.

Both use the intervention in the same *expected fraction* of units. If the intervention has the same added-noise distribution and variance whenever used, and baseline variance is the same across contexts and policies, the average injected variance is also matched. That is **not** automatic matching of energy, physical resources, harms, intrinsic noise, total variance or trajectories. Exact equality of realized counts in a finite trial is also not guaranteed by equality in expectation.

For the following calculation assume either policy's assignment is independent of the unit's potential outcomes **conditional on E**, so that a gated unit in state `e` has the same mean potential outcomes as the uniform-policy population in that state. This is automatic if the gating randomization uses only E and independent random draws; it is an additional substantive condition when a proxy or other pre-existing signal is used.

Under those conditions the gain in mean functional outcome is exactly

```text
G = E[Y(gated)] − E[Y(uniform)]
  = w0 w1 (p0 − p1)(δ0 − δ1).
```

The expansion is `Σe we(pe−r)δe`; substitution for `r` gives the displayed product. The first factor is population mix, the second differential allocation, and the third effect heterogeneity. It follows that if the added variability has the same causal effect in both states, merely allocating it differently cannot improve this outcome under this model and fixed rate. If the policy favors the state harmed more or helped less, it does worse. The formula says nothing about whether context influences *baseline* outcomes, whether other forms of adaptation help, or which real system satisfies the assumptions.

The identity itself is a standard covariance/effect-modification calculation. Our addition is its explicit use as a falsifiable accounting gate for the project's proposed Noble comparison and the counterexample below; no precedence claim is made.

## 3. Imperfect state information: a transparent numerical case

Set both states equally common and choose the hypothetical potential-outcome means:

| State | Baseline `μe0` | Added variability `μe1` | Effect `δe` |
|---|---:|---:|---:|
| 0 | 1/2 | 1 | +1/2 |
| 1 | 1/2 | 0 | −1/2 |

Suppose the controller uses a pre-intervention proxy that classifies the state incorrectly at rate `ε` **in each state**, and is independent of the potential outcomes given E. It adds variability when the proxy says state 0. Thus `p0=1−ε`, `p1=ε`, and both policies have a high-variation rate `r=1/2`.

| Proxy error `ε` | Uniform outcome | Gated outcome | Gated gain |
|---:|---:|---:|---:|
| 0 | 1/2 | 3/4 | +1/4 |
| 1/4 | 1/2 | 5/8 | +1/8 |
| 1/2 | 1/2 | 1/2 | 0 |
| 3/4 | 1/2 | 3/8 | −1/8 |

In this illustrative case `G=(1−2ε)/4`; a systematically reversed proxy could be relabeled, if its error and the direction of effects are actually known. A real proxy's errors need not be symmetric, invariant across intervention conditions, or independently known. The observable marker might measure task context, prior history or an output-driving latent variable, not a phenomenal state.

Changing the context mix also changes both the matched dose and the gain. With `w0=3/4`, `w1=1/4`, `p0=3/4`, `p1=1/4` and the same means, the new uniform rate is `5/8`, not `1/2`. The gated and newly matched uniform outcomes are `3/4` and `21/32`, giving gain `3/32`. This is a deployment-mixture example, not evidence that any laboratory result transports across populations.

## 4. A counterexample to inferring the gated effect from separate summaries

The conditional-independence premise above is essential and cannot be inferred just from accurate state-specific randomized outcomes. Let states be equally likely and let a measured pre-intervention marker `M=0` occur with probability `3/4` in E=0 and `1/4` in E=1. Consider two different stipulated causal models:

- **E-only model:** `E[Y(0)|E,M]=1/2`; `E[Y(1)|E=0,M]=3/4` and `E[Y(1)|E=1,M]=1/4`, with no remaining marker effect at fixed E.
- **Marker-sensitive model:** `E[Y(0)|E,M]=1/2`; `E[Y(1)|M=0,E]=1` and `E[Y(1)|M=1,E]=0`, with no remaining E effect at fixed M.

Suppose binary outcomes have the indicated means. The two models have the **same** `P(M|E)` and the same `P(Y|do(A),E)`: in each, randomized added variability gives average effects `+1/4` in E=0 and `−1/4` in E=1. These are genuine state-stratified average causal contrasts if A is properly randomized; the point is that the marginal data do not settle whether E, M or another correlated factor is the relevant effect modifier. The models do not claim that E is randomly manipulable or that its own causal effect is known.

Now gate `A=1` exactly when `M=0` and otherwise set `A=0`. Both models have the same `1/2` average added-variation rate and the same uniform-policy mean `1/2`, but their gated means differ:

```text
E-only:             9/16     gain 1/16
Marker-sensitive:   3/4      gain 1/4
```

The first model satisfies conditional independence of the assignment and potential outcomes given E. The second does not: conditional on E, M predicts the effect and also determines the gated assignment. Feeding its marginal `δe` and `pe` into the formula from section 2 would incorrectly predict `9/16` rather than `3/4`. Thus reliable estimates of each separate E-stratified average and marker rate do not suffice; **their joint relationship must be measured or otherwise justified**.

This is not a claim that the two models are indistinguishable under every experiment. A randomized study observing M and Y jointly distinguishes them: at E=0 and `do(A=1)`, `P(M=0,Y=1)` is `9/16` in the E-only model and `3/4` in the marker-sensitive model. A direct randomized comparison of the two actual policies likewise distinguishes their predicted mean outcomes. Keeping only separate summary tables discards this information. Conversely, observing an association with M does not alone tell us whether the marker itself causes the response; it may only track a third variable.

## 5. Test contract and decision rules

For a safe controlled system, define in advance E, M, the noise waveform/distribution, baseline, task and outcome. Record all baseline predictors that drive gating and treatment response. On independent held-out units, randomize assignment between (i) the prespecified context/proxy-gated policy, (ii) the uniform policy with its high-variation rate matched to the deployment mix, and (iii) a no-added-variation baseline. A state-aware comparator with access to the same information and similar resources is needed before calling noise necessary; deterministic perturbations can be included separately if physically feasible. In a sequential task, extend the unit and horizon, specify histories and carry-over, and randomize whole policy assignments or use an appropriate longitudinal causal analysis; the single-step identity does not automatically apply.

Report mean outcomes, prespecified uncertainty intervals, conditional and aggregate contrasts, actual intervention frequencies, signal calibration, nonresponse, off-target changes, relevant physical cost and adverse outcomes. Matching a single average variance is insufficient if higher moments, energy or input information differ. Test the gating model against joint `(E,M,A,Y)` distributions in independently randomized calibration data, not only marginal E tables; the gold-standard state, if unobserved, introduces further identification assumptions. Observe positivity: any effect to be estimated within a relevant stratum must have nonzero assignment probability for both interventions, and report when sampling is too sparse.

A held-out gated-minus-uniform effect whose interval excludes a prespecified meaningful advantage would count against that particular claimed advantage **for this protocol, outcome and population**; an imprecise interval is inconclusive. A positive result supports a context-dependent functional advantage, not necessarily the mechanism described by Noble, an advantage for every environment, or a conscious experience. A policy can also improve a performance metric while worsening safety, welfare or experienced quality; these require their own endpoints. No experiment here has been conducted and no human or animal intervention is recommended.

## 6. The experience and plurality gap

Experience is a valid datum, not something dismissed as an illusion: the subject's experience itself is first-person evidence, distinct from its physical report. Reports provide meaningful evidence for an investigator, but report transport and accuracy in altered states remain questions for calibration. Replacing `Y` with a performance score, or adding a mathematical reward to the toy, does not automatically measure felt pleasure or pain. A valence study needs a separately specified experiential anchor and target-valid report assumptions; the existing [assay-identifiability analysis](EXPERIENCE_ASSAY_LATENT_IDENTIFIABILITY.md) and [mismatch-calibration gate](EXPERIENTIAL_MISMATCH_CALIBRATION_TRANSPORT_GATE.md) spell out why a proxy agreement is not enough.

Similarly, units, signals and adaptive loops are not thereby subjects. Whether a relational organization constitutes one subject, several subjects or none is unresolved. Nor does demonstrating adaptive dynamics establish the intrinsic experiential nature or necessity of a timeless self-sufficient whole. Such local dynamics, if eventually recovered, would be relations within the whole, not an external clock or a mechanism turning possibilities into actuality. These gaps remain alongside the recovery of physics and the other jointly required C1–C7 obligations.

## Verification

Run `python verification/context_gated_variability_gate.py` for the [exact receipt](verification/context_gated_variability_gate.json). It checks the algebra on 78,125 finite combinations, the sensor-error and mixture examples, and selected exact quantities in the marker-sensitive counterexample. The general identity is established by the displayed algebra, not by finite enumeration. The script is an arithmetic regression check only; it is neither an independent proof of real-world assumptions nor a test of experiential ontology.
