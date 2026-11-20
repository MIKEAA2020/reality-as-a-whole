# Higher-order causality and the subject-selection problem

## Main result

A selector that sees only **single-variable intervention effects on single-variable outputs** can miss a real collective dependence even if it has perfect access to every such effect. In the finite example below, the one- and two-output distributions agree exactly under every fully fixed input, and hence under every one of 27 partial-clamp protocols we test. Yet the complete three-output distribution changes under a single controlled input flip. The two proposed dynamical kernels are therefore not equivalent.

A subsequent [common-cause gate](COLLECTIVE_CAUSAL_RESPONSE_AND_COMMON_CAUSE_GATE.md) shows the converse limitation: even this complete higher-order channel admits a distributed local implementation with shared randomness, so its collective response does not itself establish an integrated physical mechanism.

This matters for the project's earlier four-spin subject rules: their pairwise-influence graph can be useful **within its stated model**, but is not a generally complete description of causal organization. A proposed subject criterion based only on that graph needs an independently justified restriction excluding relevant higher-order dependencies, or must be extended to a richer intervention/response structure. Conversely, finding such a dependence does not demonstrate a subject or phenomenal unity.

This is a new **application and exact check for our selector problem**, not a new discovery of XOR, higher-order causality, information decomposition, or an empirical result. No literature-wide novelty claim is made.

## 1. Established literature and access

Kořenek, Sanda and Hlinka, [*Higher order definition of causality by optimally conditioned transfer entropy*](https://arxiv.org/html/2409.08295v2), explicitly discuss XOR, hypergraphs, conditioning and the dependence of their information measures on the input distribution. All five HTML chunks of the revised preprint, including the conclusion and references, were read; figures were not visually audited and the [published article](https://doi.org/10.1103/PhysRevE.111.L042302) was not compared line by line. The authors also analyze a **biophysical simulation** of dendritic computation. We did not run their code or independently verify their measures, significance tests or biophysical fit. Their proposed causality definition is not the same as a general interventionist definition, and we do not use it as a theorem that a manipulated input has no causal effect in every sense.

Yang, Wang and Zhang, [*Partial Effective Information Decomposition for Synergistic Causality*](https://arxiv.org/abs/2605.03267), connect higher-order causal analysis, intervention distributions and hypergraphs. Abstract, introduction and selected application/discussion passages were read, not its full 19-chunk preprint, figures, proof or code. The authors themselves caution that their air-quality example characterizes interventions on a learned predictor; translating those to atmospheric causation requires additional assumptions. Our example does **not** calculate or validate their PEID.

Gidon and colleagues, [*Dendritic action potentials and computation in human layer 2/3 cortical neurons*](https://doi.org/10.1126/science.aax6239), report ex-vivo human neuronal findings relevant to nonlinear computation. Only the abstract and editorial summary were available in the retrieved main page; full article access is behind a registration/access step and the listed supplement was not inspected. Those findings are not evidence that the toy system or individual neurons are conscious.

The point also connects to our earlier [pairwise-marginal retina audit](RETINAL_MAXENT_READING_AND_MARGINAL_LIMITS.md), [joint-input leakage example](JOINT_ACCESS_COMMON_SOURCE_DECISION_GATE.md), and [factorization/redescription gate](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md). The present example adds a **strictly positive, interventional transition law whose entire pair-output data are unchanged**, with an explicit transformed coordinate representation and a finite distinguishability calculation.

## 2. Two explicit causal channels

Let the controlled input and observed output each be a triple of bits, `x,y∈{0,1}³`. For an ideal intervention setting the entire input to `x`, specify

```text
Kκ(y | do(x)) = [1 + κ (−1)^(x₁⊕x₂⊕x₃⊕y₁⊕y₂⊕y₃)] / 8,
0 ≤ κ ≤ 1.
```

Compare `κ=0` with `κ=1/5`. Both are normalized and **strictly positive** for every input and output: this is not an artifact of impossible output configurations. The all-input intervention is part of the toy's definition; treating an observational conditional probability as this intervention law would require extra causal assumptions. Partial clamps below randomize unspecified inputs independently and uniformly.

For every fully fixed input `x`, each individual output is fair and every two-output marginal is uniform in both models:

```text
Pκ(Yi=a | do(x)) = 1/2,
Pκ(Yi=a,Yj=b | do(x)) = 1/4   (i≠j).
```

These statements hold even when **all other inputs are held fixed**, not just when they are averaged out. Therefore every input-to-single-output contrast is zero, including the `i=j` cases, and all two-output marginals are identical under any mixture of fully fixed input settings. The checker explicitly verifies all `3³=27` partial-clamp specifications and the single- and pair-output distributions in each.

Nevertheless the complete outputs respond collectively. When the input parity is even,

```text
Pκ(output parity even | do(x)) = (1+κ)/2;
```

when it is odd, the probability is `(1−κ)/2`. At `κ=1/5`, flipping any one input while holding the other two fixed changes that probability by `1/5`. For each fixed input the total-variation distance between the full output distributions of the `κ=0` and `κ=1/5` models is `1/10`. A physically accessible joint parity readout can therefore distinguish the channels, although all their single- and two-output marginal laws coincide.

Under uniform independent interventions on the full input, the **mutual information between the entire input and entire output** is

```text
I(X;Y) = 1 − h₂((1−κ)/2) bits.
```

At `κ=1/5`, this is approximately `0.02905` bits, versus zero at `κ=0`. It is an information quantity for a stipulated intervention distribution and channel, not a direct measure of consciousness or IIT's integrated information. In particular, it does not locate where in the system a physical mechanism occurs. An explicit implementation draws independent fair bits `U,V` and a noise bit `N` with `P(N=0)=(1+κ)/2`, and sets `Y=(U,V,U⊕V⊕parity(x)⊕N)`. The checker verifies its full kernel. This same controller could be located inside the declared system boundary or outside it, provided it receives the inputs and sends the three outputs; input–output data alone would not tell those physical arrangements apart. Whether the controller is inside or outside, and whether the relevant mechanisms really have been observed, requires separate evidence.

## 3. A concrete failure of a simplistic selector

Suppose a candidate subject rule says: construct a directed graph with an edge for every nonzero single-input-to-single-output effect under the specified interventions; assign subject candidates using only that graph and its labels. Both kernels yield the **same empty graph**. Thus any deterministic rule using only that graph must produce the same subject assignment for them. This is a mathematical information-loss statement: if the correct experiential constitution were sensitive to the difference between these complete channels, such a selector could not capture it.

The hypothetical “if” is essential. We do **not** know whether experience or subject count is sensitive to that collective dependence. Nor does the example establish that a full channel is sufficient to select subjects. Adding hyperedges or a high-order score can repair this particular information loss but still needs a constitution rule, handling of common causes, overlapping candidates, persistence, qualitative character, and an independently anchored assay. The earlier [four-spin comparison](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) remains valid for its declared spin kernel and interventions; this is not a counterexample to its exact local calculations or to IIT.

### Same channel, different coordinates

Define an invertible re-description of both input and output:

```text
z=(x₁,x₂,x₁⊕x₂⊕x₃),
w=(y₁,y₂,y₁⊕y₂⊕y₃).
```

In these coordinates the same kernel reads

```text
Kκ(w|z) = [1+κ(−1)^(z₃⊕w₃)]/8.
```

The single-coordinate influence `z₃→w₃` is now `1/5`, although all input-to-output single-coordinate effects were zero in the original variables. The map is bijective: no physical information was added. But the parity coordinate is a **joint observable** of three original bits; a readout of it requires access to those bits or a physical equivalent. A clamp in the new coordinates also has to be transported back through the inverse map. For instance, changing `z₁` while holding `z₂,z₃` fixed changes both `x₁` and `x₃`; it is not the same operation as changing only `x₁`. This is why a node-by-node edge rule cannot be declared substrate-independent merely by renaming nodes.

Not every invertible re-encoding is a physically innocent factorization for every theory: local addressability, locality and mechanism may distinguish physical subsystem choices. The requirement is to preserve conclusions **when two descriptions really are equivalent and interventions, records, and candidate subject claims have been mapped**, not to erase physically meaningful boundaries.

## 4. Testing cost in the declared toy model

For a fixed input `x`, record `R=+1` when the output parity agrees with the input parity and `−1` otherwise. Under `κ=0`, `P(R=+1)=1/2`; under `κ=1/5`, it is `3/5`. With 100 independent trials and equal prior odds for the two fully specified kernels, the exact optimal likelihood-ratio decision has average error approximately **0.1573**. This is not a population estimate or a general sample-size guarantee.

For a conservative illustrative guarantee, threshold the sample mean of `R` halfway between the two means, at `1/10`. Hoeffding's inequality for independent `R∈[−1,1]` gives each model's probability of a wrong-side decision at most `exp(−nκ²/8)`; `n=738` makes that upper bound at most `0.025`. This assumes independently prepared trials, fixed exactly known kernels, faithful joint readout and no drift. It does not account for multiple tested subsets, estimating `κ`, dependence, instrumental errors, or the much larger burden of identifying a mechanism in a real system. Conditional on those ideal assumptions, it illustrates why exact nonzero sensitivity is not the same as practical identification.

## 5. What a replacement subject rule must supply

A serious candidate should do all of the following before being treated as a physical–experiential explanation:

1. **Specify the physical domain:** identify actual subsystem boundaries, admissible interventions, joint readouts, time or history grain and environmental channels. A list of correlations is not yet a mechanism.
2. **Specify the full dependence used:** if it uses only pairwise edges, justify the restricted model class; otherwise say what multivariate effects, conditioning and uncertainty are retained. Unbounded enumeration can be combinatorially expensive.
3. **Transport descriptions:** map states, allowed interventions, outputs and proposed subject events between genuinely equivalent encodings, rather than applying the same coordinate-counting rule to different axes.
4. **Give an incidence and quality law:** say what constitutes a subject, its experiences, overlap and persistence. Neither a connected graph nor an information value supplies this law by itself.
5. **Connect to evidence:** identify first-person anchors, condition-specific report accuracy, plausible common drivers and prespecified physical rival predictions. Failure to calibrate these leaves subject constitution open; it is not a reason to dismiss a person's own experience.

This work fits a fundamentally timeless whole by treating inputs and outputs as a model of **local ordered records and interventions**, not a clock external to reality. It introduces neither a universal subject nor a temporal process that turns possibilities into actuality. It does not explain why the whole is self-existent, derive quantum mechanics, settle actual subject boundaries or determine a measure on experiences.

## Reproduction

Run `python verification/higher_order_subject_selector_gate.py`. The [script](verification/higher_order_subject_selector_gate.py) checks exact rational kernels, all relevant fixed-input output marginals, 27 partial-clamp patterns, permutation invariance, the parity-coordinate bijection and the two-hypothesis binomial error; the [receipt](verification/higher_order_subject_selector_gate.json) records the results. The calculations test this finite model and chosen readout, not real brains, experimental hardware or a general theory of experience.
