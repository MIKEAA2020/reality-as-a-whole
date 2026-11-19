# From an assumed boundary budget to a conditional intervention test

## Objective and result

The previous [unknown-context gate](SUBJECT_BOUNDARY_UNKNOWN_CONTEXT_BUDGET.md) showed that a candidate pair is selected by the stipulated `L` rule if its internal edge weight exceeds the **sum** of its external weights. That was a graph theorem: it did not say how anyone could measure or bound the sum.

Here is a limited, constructive answer. In a specified finite **ferromagnetic, pairwise-additive heat-bath model**, one can upper-bound that graph sum from collective interventions on all external inputs, even without separately estimating each coupling. We apply it to the existing four-spin model and give a hypothetical finite-sampling calculation. This is an elementary application of an established model, not an established neuroscience method, a new physical law or a subject assay. Crucially, it assumes one can identify and control **every relevant external input**; it does not certify a genuinely unknown or inaccessible environment.

## 1. Why isolated tests are not enough

Suppose an output `Y` depends on `m≥2` external binary controls. Compare two possible physical response rules:

- Rule A always returns `Y=0`.
- Rule B returns `Y=1` only if **every** control is set to `−1`; otherwise it returns `0`.

If the only tested interventions are the all-`+1` baseline and single flips away from that baseline, A and B make exactly the same predictions. They differ maximally for the all-`−1` intervention. Thus those tests alone do not bound an untested collective response. This is a simple higher-order-interaction counterexample, not evidence that such a mechanism occurs in a particular brain. The earlier [parity gate](QUANTUM_POSITION_VERIFICATION_AND_SUBJECT_LOCATION.md) already noted a related limitation of lower-order access.

This difficulty is known rather than newly discovered. Schneidman et al., **[“Weak pairwise correlations imply strongly correlated network states in a neural population,” DOI 10.1038/nature04701](https://doi.org/10.1038/nature04701)** report that weak pairwise correlations can coexist with collective activity, and find their pairwise maximum-entropy model useful in the studied retinal and cultured-neuron datasets. The user subsequently supplied the full six-page article, whose text and five main figures we inspected; supplementary figure captions, but not supplementary plots, and neither raw data nor code were inspected. Its fitted interactions can have either sign and are *observational* parameters, not evidence for this note’s positive causal heat-bath couplings. See [the full-source assessment and exact fixed-bin counterexample](FRASER_SCHNEIDMAN_SCALE_DYNAMICS_SOURCE_ASSESSMENT.md). Their correlation result is not itself a test of our intervention or subject rule. Yu et al., **[“Higher-Order Interactions Characterized in Cortical Activity,” DOI 10.1523/JNEUROSCI.3127-11.2011](https://doi.org/10.1523/JNEUROSCI.3127-11.2011)** argue that higher-order descriptions are important for specified cortical dynamics; only the abstract and selected available text were inspected, not the full methods, data or code. Neither source establishes a universal pairwise or non-pairwise brain law.

## 2. Conditional physical model

Use the same type of local heat-bath update as the existing [causal-influence gate](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md). For target spin `i` and fixed input signs `s_j=±1`, let

```text
P(s_i' = +1 | inputs) = σ(2[h_i + Σ_j J_ij s_j]),
σ(x) = 1/(1+e^(−x)),              J_ij = J_ji ≥ 0.
```

Assume a finite set of inputs, stable pairwise couplings, no unmodeled higher-order terms, faithful clamps, and a fixed declared local update. This is a classical toy mechanism, not a model fitted to a brain or QFT. The standard antecedent is Glauber, **[“Time-Dependent Statistics of the Ising Model,” DOI 10.1063/1.1703954](https://doi.org/10.1063/1.1703954)**; the journal abstract, not its full paper, was inspected here.

The graph construction remains the earlier one: `d[j→i]` is the target's probability difference under a two-sign clamp of `j`, averaged over a declared distribution of the other inputs. Set the symmetric edge weight to `w_ij = min(d[j→i], d[i→j])`. In this ferromagnetic model the directed differences are nonnegative.

For any fixed settings of the other inputs, direct calculation gives

```text
0 ≤ P(+ | s_j=+1) − P(+ | s_j=−1) ≤ tanh(J_ij) ≤ J_ij.
```

Averaging over any specified **common** distribution of other inputs preserves this bound. Hence `w_ij ≤ J_ij`. It is important that the same background distribution is used in the two clamped conditions; uncontrolled changes between them invalidate this interpretation.

## 3. Bounding the external sum with two extreme settings

Fix the other members of a proposed core `S` at a declared setting. For each target `i∈S`, let `p_i⁺` be its update probability with **every external input** forced to `+1`, and `p_i⁻` its update probability with every external input forced to `−1`. Define `logit(p)=ln[p/(1−p)]`. The model gives the exact identity

```text
logit(p_i⁺) − logit(p_i⁻) = 4 Σ_(j outside S) J_ij.
```

Therefore the graph's total external weight obeys

```text
D(S) = Σ_(i∈S, j∉S) w_ij
     ≤ ¼ Σ_(i∈S) [logit(p_i⁺) − logit(p_i⁻)] = B(S).
```

For a two-unit candidate with independently established internal weight `w`, the **combined conditional certificate** is

```text
B(S) < w  ⇒  D(S) < w  ⇒  S is an L winner.
```

The first implication uses the additive ferromagnetic update model and complete extreme interventions; the second uses the earlier graph theorem and the declared candidate universe. This does not say that `B` equals the graph sum, that the physical model is correct, or that an `L` winner is a subject. Strong saturation can make logit estimates unstable; low probability differences alone are not a safe substitute for a bound on the logit contrast.

## 4. Worked connection to our four-spin model

For the existing chain at cross coupling `tanh G=1/4` and outer coupling `tanh K=1/2`, consider core `{0,1}`. Its established graph weight is `w=10/21`, and its one external graph edge has weight `4/21`. Hold the other core spin at `+1` during each target's external extreme test. The model gives:

| Target | `p⁺` with external inputs + | `p⁻` with external inputs − |
|---|---:|---:|
| 0 | `3/4` | `3/4` |
| 1 | `5/6` | `9/14` |

Hence

```text
D = 4/21 ≈ 0.19048,
B = atanh(1/4) ≈ 0.25541,
w = 10/21 ≈ 0.47619.
```

So `D ≤ B < w` and the combined certificate succeeds **in this stipulated model**. The bound is deliberately conservative: it uses coupling sums to bound the reciprocal influence score, rather than identifying the two quantities. The same network is the prior exact model; no observations or biological measurements have been added.

### Hypothetical sampling gate

Imagine eight binary-outcome cells: the four extreme-input cells above and four cells estimating the two directed internal influences. The model's internal cell probabilities are `(3/4,1/4)` in one direction and `(31/42,11/42)` in the other, where each pair corresponds to the two core clamps and the declared randomized background.

For illustration, suppose these displayed values were the sample means and each cell's true probability were simultaneously within `r=0.01` of its displayed value. Apply the monotonicity of the logit to get an upper bound `B_U` by replacing each external `p⁺` with `p⁺+r` and each `p⁻` with `p⁻−r`; apply the same probability intervals to the internal differences to get a lower bound `w_L`:

```text
B_U ≈ 0.31136,       w_L = 479/1050 ≈ 0.45619,
B_U < w_L.
```

Both probabilities must remain strictly between zero and one. Under within-cell iid Bernoulli sampling and fixed means, Hoeffding's inequality plus a union bound says `28,842` trials **per cell** suffice for the simultaneous `0.01` error event to fail with probability at most `0.05`:

```text
P(any of the eight mean errors > 0.01) ≤ 16 exp(−2 n · 0.01²).
```

That is `230,736` total hypothetical trials, deliberately conservative and **not a recommendation for human research**. The displayed means are illustrative exact values, not collected data; exact denominators may not match a finite sample of that size. The confidence statement is conditional on the trial model and the structural assumptions above, including valid interventions, not a 95% probability that there is a subject. Cross-cell independence is unnecessary for the union bound, but within-cell independence and stationarity matter. Systematic clamp/readout bias, experimental drift, setting selection and model misspecification need separate calibration and wider bounds.

## 5. The decisive obstacle

The two-extremes trick works only if the actual interaction is additive with known nonnegative signs and if **all relevant external variables are controllable in both extremes**. Hidden variables that cannot be jointly clamped, mixed excitatory/inhibitory signs, context-dependent coefficients, higher-order interactions and unmeasured indirect pathways can invalidate `B≥D`. A successful fit in a small set of conditions does not by itself establish the model or the missing input coverage. If controls can be identified and changed only by invasive procedures, practical feasibility and ethics are independent constraints.

In particular, a procedure that cannot rule out the counterexample in §1 cannot claim a model-free upper bound on collective context influence. The meaningful next empirical task would be to predefine a physically justified class of interventions, validate the response model and input coverage against held-out **multi-input** perturbations, and bound remaining unobserved influence. If that cannot be done, the earlier `D<w` criterion remains conditional rather than an established boundary.

Even a validated physical certificate would select an organizational candidate under the specified graph rule. It would not independently decide whether there is one or several experiences, establish particular qualities, or explain why the experiential whole is self-sufficient. Those are separate gaps, and the positive-connectivity and local-max rules can still attach different subject labels to the same physical history.

## Verification

`python verification/collective_context_leakage_gate.py` checks the reference values, the two-extremes calculation, the hypothetical confidence arithmetic, and finite instances of the collective-interaction counterexample; see the [receipt](verification/collective_context_leakage_gate.json). The general bounds above follow analytically from the explicitly stated model, not from sampling the parameter grid. No patient intervention, experimental data, quantum field theorem or experiential assay is claimed.
