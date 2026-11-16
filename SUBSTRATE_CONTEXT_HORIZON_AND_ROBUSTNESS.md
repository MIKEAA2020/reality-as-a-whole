# Substrate, context and the time horizon of an organizational match

## Result in brief

The follow-up [hidden-edge and imperfect-intervention analysis](SUBJECT_ROBUSTNESS_HIDDEN_EDGES_AND_INTERVENTION_ERROR.md) relaxes the fixed-zero-nonedge assumption, proves a sharp four-node margin, and states a separate conditional measurement budget.

The [previous context gate](SUBSTRATE_INDEPENDENCE_CONTEXT_AND_SUBJECTS.md) showed that an arbitrarily weak connection can change the verdict of a simplistic exact-connectivity subject rule. The present question is different: **even when we do not use that all-or-nothing rule, how much can a weak physical difference matter over the span of an experience or a subject's persistence?**

A one-step match does not, by itself, establish a long-horizon match. In a finite example with maximum one-step total-variation discrepancy `ε=1/10,000`, the probability laws of the **entire local output history** have distance about `0.632` after 10,001 updates. In a different, contracting example, the difference between **endpoint distributions** stays below `0.02` for every number of steps. These are deliberately specified stochastic toys, not simulations of human subjects.

The practical refinement is that proposed material substrate-independence needs a declared **context, relevant observables and operations, time grain, and horizon**, together with evidence for the claimed match. It remains a thesis about experience, not merely the mathematical closeness of records. A sufficiently close physical match establishes neither identical phenomenal quality nor the same continuing subject without further principles.

## 1. General finite-horizon comparison: a known result applied here

Let `K` and `L` be finite-state transition kernels describing two candidate implementations in a **common, already justified representation**, with the same initial distribution. Suppose for every state and every specified allowed action,

```
TV(K_a(s,·), L_a(s,·)) ≤ ε,     0 ≤ ε ≤ 1.
```

The two records are produced by the same declared observation map; operations and state labels must be transported when the descriptions differ. For any fixed sequence of actions, or the same action policy applied to matched histories, the laws of full state histories through `n` local steps obey

```
TV(full history under K, full history under L)
    ≤ 1 − (1−ε)^n  ≤ nε.
```

To see the first inequality, maximally couple the next states while their histories agree: the probability of continuing to agree is at least `1−ε` each step. Once the histories differ, couple the two evolutions in any way preserving their respective laws. The probability of any disagreement is at most `1−(1−ε)^n`; total variation cannot exceed the disagreement probability of a coupling. The deterministic local-record map cannot increase the distance. If action policies are not the same on matching histories, or relevant initial distributions differ, this bound does not apply as stated. An arbitrary coordinate relabeling does not automatically transport interventions, costs or locality.

This is an application of **standard maximal-coupling and total-variation inequalities**, not a new theorem or a proof that the two systems are conscious. See the [coupling lecture notes](https://courses.cs.duke.edu/spring13/compsci590.2/slides/lec5.pdf) and [work on Markov-chain perturbation bounds](https://dukespace.lib.duke.edu/server/api/core/bitstreams/c7a0f94a-93d5-4e3d-9a97-daaeb651a23f/content). A real comparison must justify its state space, mapping, operational repertoire, stationarity or time dependence, and uniform error bound; matching a few sampled trajectories is not enough.

For a specified local record, the bound says every record event's probability differs by at most `1−(1−ε)^n`. It does **not** say that two subjects or qualities are identical, or that subjective differences are bounded by physical total variation. That inference requires an independently justified phenomenal bridge. In particular, two ontology/subject packages can assign different experiences while using the same physical record law; the existing [subject interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) exhibits this type of underdetermination by construction.

## 2. A delayed contextual effect that accumulates

Let `x,y∈{0,1}`, start from `(0,0)`, and set

```
x_(t+1) = x_t XOR y_t
y_(t+1) = y_t OR N_t,      N_t independently Bernoulli(ε).
```

Compare `ε=0` to `ε>0`. The local update rule for `x` is unchanged: given the same local input `y_t`, both systems apply the same XOR. The difference is a weak activation process in the surrounding `y` context. Once activated, `y` remains active. For `y=0` the full-state one-step kernels differ by `ε` in total variation; for `y=1` they agree. Thus the uniform full-state discrepancy is exactly `ε`.

At one step, `x` is certainly `0` in both systems. Under `ε=0` the entire output history remains zero. Under positive `ε`, an activation in the first `n−1` updates produces a nonzero `x` within the `n`-step history. Hence, **for this model and this starting state**,

```
TV(law of x_0,...,x_n at ε=0, law at ε>0)
    = 1 − (1−ε)^(n−1),     n ≥ 1.
```

This exact equality is for the **whole observed local history**, not necessarily for the final `x_n` alone. The full-history distance can be large even when a selected endpoint hides earlier differences.

| Updates `n` | Exact local-history TV when `ε=1/10,000` |
|---:|---:|
| 1 | `0` |
| 2 | `0.0001` |
| 1,001 | about `0.0952` |
| 10,001 | about `0.6321` |
| 29,957 | about `0.9500` |

The environmental bit and noise are formal model variables, not an identified neuronal process or a subject. The two parameter settings are mathematical comparisons; we do not assert they are both genuinely possible realities or have actually been implemented. The local step is an internal ordered relation of the toy, not a universal clock or a transition from nonexistence to existence.

The result does not contradict the preceding paper's exact local invariance example. That example had **no `y→x` influence**; here `y` affects `x`, and a weak environmental activation eventually changes `y`. Different assumptions, different conclusion. It does show why naming a coupling “tiny” without specifying the feedback, memory and horizon cannot establish that it is irrelevant to an extended record.

## 3. A control: contraction can keep endpoints close

Not every weak difference accumulates indefinitely. Suppose `K` is a finite-state kernel with Dobrushin coefficient

```
α = sup_(s,t) TV(K(s,·), K(t,·)) < 1,
```

and `sup_s TV(K(s,·),L(s,·)) ≤ ε`. For the same initial law, let `d_n=TV(μK^n, μL^n)`. Standard total-variation contraction gives

```
d_(n+1) ≤ α d_n + ε,
d_n ≤ ε(1−α^n)/(1−α).
```

If the bound exceeds `1`, it can of course be capped at `1`. This is an **endpoint-law** result, not a bound uniform in length on full path histories. It applies to fixed comparable kernels; a state-dependent adaptive intervention policy can change the effective contraction and needs separate analysis. See the prior [Dobrushin-coefficient discussion](https://arxiv.org/html/1912.06845).

For a concrete two-state control, set `P_K(x'=1|x)=1/4+x/2` and `P_L(x'=1|x)=1/4+δ+x/2`, with `δ=1/100`. Both are valid kernels, their maximum row difference is `δ`, and `α=1/2`. Starting from `x=0`, the endpoint TV is exactly

```
δ(1−(1/2)^n)/(1−1/2) = (1/50)(1−2^−n) < 1/50.
```

This saturates the stated bound for this example and tends to `0.02`. It does not imply that long records, memories, or phenomenal qualities are close. The growing full-history bound and the bounded endpoint result concern **different targets** and are compatible.

## 4. A robustness certificate for the existing subject-rule comparison

We can now apply a concrete stability requirement to the **existing** four-spin interface, rather than proposing another untested selector. At its weak-coupling setting the earlier interventional calculation gives a chain with symmetric edge weights

```
w_01 = 10/21,     w_12 = 4/21,     w_23 = 10/21.
```

The two stipulated rules compared there are C, positive connected components, and L, strict local cohesion maxima among overlapping candidate subsets. Assume the graph has the **same fixed chain topology**—in particular, the three nonedge weights remain exactly zero—and each of the three listed weights changes by at most `η`. Then, for **every** such weight assignment with

```
η < (10/21 − 4/21)/2 = 1/7,
```

C still selects `{0,1,2,3}`, while L still selects `{0,1}` and `{2,3}` with no unresolved ties. The proof uses the original gap `2/7`: both outer edges remain strictly stronger than the middle edge, and all three remain positive. For an induced connected interval in a positive weighted chain, the minimum-cut score used by L is its weakest edge; a disconnected subset has score zero. Any candidate that overlaps an outer pair and extends beyond it must include the weaker middle edge, so it cannot tie or beat that pair. The two outer pairs are disjoint, so they do not compete with each other.

This strengthens the earlier [physical influence ordering bound](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md): it carries the margin through the **actual C and L selection rules** in the fixed interface. The verifier checks 27 endpoint/interior perturbation combinations at `η=1/8` in addition to the general argument. At the boundary `η=1/7`, both outer weights can be reduced and the middle weight raised to `1/3`; L then has six overlapping tied candidates, so the strict inequality matters.

The certificate is for uncertainty in **abstract edge weights at one specified local update**, with fixed zero nonedges. It does not show that every perturbed graph comes from the original physical spin model, bound accumulated multi-step kernel error, or validate an experiential readout. Hidden additional edges, changed intervention backgrounds, biased or dependent measurements, other time grains, and uncertainty in the topology require separate bounds. Most importantly, stability of the competing labels does not establish that either label denotes a real subject. The existing hypothetical assay remains uncalibrated.

## 5. A non-circular robustness requirement for the framework

For any proposed pair of materially different realizations, the subject/experience account should explicitly declare:

1. **Target:** which physical records, qualitative contrasts, joint-experience claims and identity/persistence questions are being compared. These are distinct targets; a current-state match need not be a lifetime match.
2. **Organization and context:** the candidate variables, intrinsic relations, physical encoding, boundary, surrounding connections, admissible operations and readouts. Preserve these under representation changes. Do not encode the desired subject verdict as an input.
3. **Scale:** the internal update grain and a relevant local horizon. An ideal infinite horizon is a further assumption, not something implied by a timeless whole. If available, specify independent contraction or memory-retention bounds rather than relying on a raw coupling threshold.
4. **Error:** exact equality or a justified tolerance with uncertainty, for the specified operations and states. A finite observed trace, or small average error, does not automatically establish the required uniform bound.
5. **Phenomenal bridge:** a separately defended rule linking the declared organization to subject incidence and anchored experiential quality, plus a treatment of overlap, ties, and continuity of identity. Operational closeness alone does not supply this bridge, and no empirical data in the present calculation calibrate it.

On this basis, material substrate-independence may mean that distinct material realizations with an equivalent **relevant contextual organization** support the same experiential type. It does not mean that every approximate behavioral duplicate has an identical experience, or that copying a description makes a subject. The open question is what organization is genuinely sufficient and why. Strong possibility=actuality does not fill that gap: it concerns genuine possibilities and actual realization, not whether every formal state, hypothetical model or approximation is a genuine possibility. It also does not supply a measure over subject occurrences.

## 6. Status and next work

The result gives an actionable *screen* for a proposed implementation comparison: choose the target and horizon first; check whether the physical approximation supports the desired operational claim; then separately assess subject and quality constitution. For the existing four-spin C/L comparison, the fixed-topology certificate now carries an explicit influence margin through both selection rules. It does not select the correct substrate-independent subject rule, derive experiential properties from kernels, establish a universal subject, or solve emergent physical time and gravity. The self-existent experiential whole remains the intended candidate, without an external creator or an actualization process, not a theorem of these probability calculations. The [frozen framework battery](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) remains incomplete, including B1–B2, subjects and quality, physics/time, measure and empirical discrimination.

Next, extend the four-spin certificate to a defensible operational model of imperfect interventions, potentially nonzero hidden edges, and a chosen local horizon, rather than assuming static weights are the entire organization. A real empirical step would additionally need a calibrated experiential target, not just longer physical data. This gate supplies neither that calibration nor new Roy evidence.

## Reproduction

Run `python verification/context_horizon_robustness.py`. Its [receipt](verification/context_horizon_robustness.json) checks all four full-state kernel rows, computes exact finite output-history distributions for 12 small horizons, evaluates the large-horizon closed form, verifies 20 exact endpoint identities for the contracting control, checks 27 four-spin weight perturbations and the tie at the radius boundary. It checks the stipulated models, not the general coupling or contraction theorems or any phenomenological claims. The preceding context and subject-interface scripts also passed. All 21 selected framework regression scripts exited successfully after installing the pinned NumPy dependency into a temporary cache; the initial battery attempt lacked NumPy. These are bounded regressions, not a pass of the substantive framework.
