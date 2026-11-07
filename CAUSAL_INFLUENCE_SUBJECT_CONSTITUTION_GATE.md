# From coupled dynamics to candidate subject boundaries

## 1. Objective and status

The previous [coupled-dynamics gate](COUPLED_DYNAMICS_SUBJECT_BOUNDARY_GATE.md) compared positive connectivity against an arbitrary coupling threshold. Here we take a constructive next step: define a **measurable causal-influence score** and an independently motivated *maximal causal cohesion* subject rule, then compare it with the positive-connectivity rule on the same dynamics.

The score is an elementary, invented diagnostic—not integrated information, an IIT 4.0 calculation, or an established measure of consciousness. The model is a four-spin classical system, not a brain. Attribution of subjects to subsets remains a hypothesis; we do not infer conscious experience from a graph. The underlying [Glauber dynamics](https://doi.org/10.1063/1.1703954) and the strategy of comparing integration across partitions are established prior ideas. [IIT 4.0](https://doi.org/10.1371/journal.pcbi.1011465) contains specific intrinsic-information, state, partition and exclusion definitions that our simple pairwise minimum-cut score does **not** implement. Hoel, Albantakis and Tononi's [causal emergence](https://doi.org/10.1073/pnas.1314922110) is an important warning that results can depend on causal grain.

## 2. Make the structural inputs interventional

Use the earlier four-spin chain `0—1—2—3` with `k=tanh K=1/2` for the outer couplings and `t=tanh G` for the middle coupling. At a selected local heat-bath update of spin `i`, clamp a neighboring spin `j` to `+1` or `−1`; any other neighbors of `i` are independently set to uniform random signs. Define

```
d[j→i] = P(s_i' = +1 | do(s_j=+1), randomized other neighbors)
         − P(s_i' = +1 | do(s_j=−1), randomized other neighbors).
```

The update is the standard conditional Gibbs heat-bath update of the previous model. Other-neighbor randomization defines a particular experimental context; it is **not** necessarily the natural distribution or an intrinsic privileged intervention. With no edge from `j` to `i`, the influence in this one-update model is zero. A different time grain, hidden couplings, nonlocal causes, feedback or interventional context could change the result.

For a symmetric nonnegative candidate cut weight, stipulate

```
w_ij = min(d[i→j], d[j→i]).
```

This favors reciprocal influence, but the minimum and background distribution are methodological choices, not consequences of necessary actuality. Signs are nonnegative in the particular ferromagnetic examples below; the definition needs revision for general inhibitory or nonlinear systems.

At `t=1/4`, exact probabilities give:

| Edge | Directional effects | Symmetric weight |
|---|---|---:|
| `0—1` | `d[0→1]=10/21`, `d[1→0]=1/2` | `10/21` |
| `1—2` | both directions `4/21` | `4/21` |
| `2—3` | `d[2→3]=1/2`, `d[3→2]=10/21` | `10/21` |

For example, `d[0→1]` averages the two settings of spin 2. It is not the same quantity as equilibrium correlation. The weights are exactly calculated from the dynamics and specified interventions; no empirical experiment was conducted.

## 3. Two subject-constitution proposals

For any candidate subset `S` of at least two vertices, define its toy cohesion as the smallest total reciprocal influence crossing any nontrivial split *within that subset*:

```
c(S) = min over ∅≠A⊊S of Σ_{i∈A, j∈S\A} w_ij.
```

We use the induced pairwise graph and an unnormalized cut. A disconnected subset has zero score. A subset need not be isolated from the rest of the network. Candidate rules, applied to the same unclamped interaction system:

- **C — positive connectivity:** one subject per connected component of the positive-influence graph.
- **M — maximal cohesion:** the subsets attaining the highest positive `c(S)` are candidate subjects; a subject's substrate is attributed to each selected subset, subject to an unresolved rule for overlapping ties.

Rule M is motivated by the idea that a unified subject requires strong internal interaction, and that a maximally cohesive subsystem should not automatically be absorbed by weak links to other subsystems. This replaces the old *numerical* cutoff with a comparison across subsets, but it is still an additional constitution rule. Choosing a minimum cut, maximizing it globally, excluding singletons and treating maximizers as subjects are all assumptions, not derived consequences. This simplified global-max rule is **not** IIT's full exclusion procedure.

### Exact comparison

| Cross parameter `t` | Rule C | Rule M candidate maximum | `c` maximum |
|---:|---|---|---:|
| `0` | `{0,1}`, `{2,3}` | `{0,1}`, `{2,3}` | `1/2` |
| `1/4` | `{0,1,2,3}` | `{0,1}`, `{2,3}` | `10/21` |
| `1/2` | `{0,1,2,3}` | six overlapping contiguous subsets of length 2–4 | `2/5` |
| `3/4` | `{0,1,2,3}` | `{1,2}` | `36/55` |

At `t=1/4`, the interventional influence is positive across the middle, so C says one subject; M selects two disjoint maximizers. At `t=3/4`, the maximally cohesive pair is central: M leaves the outer vertices unassigned. This exposes a substantive cost of the rule, not evidence that those vertices lack any experience. At `t=1/2`, M is **indeterminate as a non-overlapping subject partition**: six subsets tie and overlap. Choosing a tie-breaking rule would be a further premise; some principled tie-breaks may be permutation-invariant, but none is supplied here.

All 24 vertex relabelings were checked for each case: the maximizers transform equivariantly. This rules out dependence on vertex names in this toy; it does not imply invariance under coarse-graining, time-grain changes, alternative interventions or descriptions of the underlying physics.

### What has, and has not, been gained

The old arbitrary `3/8` boundary is gone. Each score is calculated from specific intervention probabilities, so the rule can be audited and confronted with measured causal structure **if** that structure is sufficiently identifiable. But the choice of a privileged causal score and its interpretation as a subject remain unexplained. Changing the subset universe, adding singleton subjects, changing how cross-cut influence is aggregated, or changing the intervention distribution can change the selected candidate. No claim of a unique subject decomposition follows from the present calculation.

Nor does the model solve persistence: a change in the maximizer leaves open whether a subject survives, fissions, fuses or disappears. A complete constitution rule must separately specify temporal identity and explain how it fits the user's timeless whole; local update order is not a fundamental external clock.

## 4. Can the influences be measured well enough?

In the ideal weak-coupling model, the *smallest* internal symmetric weight exceeds the cross weight by

```
10/21 − 4/21 = 2/7.
```

For an illustrative finite-data design, estimate all six directed edge influences using two input signs per direction, for **12 independently sampled cells**. Suppose the ideal hard clamps, randomized backgrounds, exact unit definitions and independent identically distributed Bernoulli readouts are genuinely available. Hoeffding's inequality plus a union bound shows that `2,421` trials **per cell** suffice for all 12 underlying response-probability estimates to be within `1/28` simultaneously with probability at least `95%`.

Each estimated directional difference is then within `1/14`. The gap between a true internal and cross influence remains at least

```
2/7 − 2(1/14) = 1/7 > 0.
```

Thus this particular ordering is robust to those bounded sampling errors. This is a conservative **toy** sample bound, not a recommended human sample size, a demonstrated intervention on neurons, or an estimate of any biological effect. The assumed graph and controllable neighbor set are known; realistic hidden nodes, imperfect clamps, intervention artifacts, correlations and model selection require different analysis. It establishes measurement feasibility only under its deliberately ideal conditions. Exact calculations and the bound are checked in [`verification/causal_influence_subject_gate.py`](verification/causal_influence_subject_gate.py); [receipt](verification/causal_influence_subject_gate.json).

## 5. What would make the subject disagreement empirically meaningful?

Even perfect knowledge of the toy interventional kernel does not adjudicate C versus M: they assign different subject boundaries to **the same kernel**. Adding a human report only helps if a separately justified link relates that report to the subjective distinction each theory predicts. The previous [random-audit experience bridge](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) gives a related accounting of report and decoder error; it does not provide a validated universal report-error bound.

For an explicit conditional gate, let `Z` mean that a prespecified genuinely joint experiential content is present, and let `Y` be a binary operational report of that content. Suppose, in a fixed controlled condition:

```
C predicts: P(Z=1) ≥ a       and report error P(Y≠Z) ≤ r_C;
M predicts: P(Z=1) ≤ b       and report error P(Y≠Z) ≤ r_M.
```

Then, by the union bound,

```
C: P(Y=1) ≥ a − r_C;       M: P(Y=1) ≤ b + r_M.
```

The two predictions are separated only if `a−r_C > b+r_M`. For the **hypothetical** values `a=.8`, `b=.2`, `r_C=r_M=.1`, report probabilities are at least `.7` versus at most `.3`. If the trials are independent and identically distributed, a threshold of `.5` on `47` trials gives a Hoeffding upper bound below `.025` on either error. These numerical assumptions are not empirical results and do not follow from C or M by themselves.

The hard part is specifying `Z` without circularly equating it to `Y`, justifying the report-error bounds independently, and deriving each theory's `a` or `b` rather than selecting them after seeing data. If neither theory gives a defensible observable difference, the model remains empirically underdetermined; if it does, a real protocol must account for indirect cueing, report strategy, serial correlation, neural access and ethically appropriate interventions. An information-combining report alone does not prove one experiencer.

The [COGITATE adversarial collaboration](https://doi.org/10.1038/s41586-025-08888-1) provides relevant methodological prior art: theory proponents and independent investigators preregistered competing empirical predictions, and reported results that challenged specified predictions of both IIT and global neuronal workspace theory. That study did **not** test our two toy rules or settle subject identity.

## 6. Position in the larger account

This work focuses on **subject individuation** within the proposed one experiential whole. It introduces no literal simulations and no external agent or possibility-to-actuality operation. The intervention cases are stipulated local mathematical models; constructing them is not a claim that incompatible global realities are genuinely possible.

Causal influence, subjecthood, phenomenal valence and self-location measure remain different questions. Even if M identified a true physical boundary, it would not explain why that subject has its particular experience, why discomfort feels unpleasant, or why the whole is necessarily actual. Nor does the finite Gibbs model derive quantum theory, spacetime, the Born rule, or the observer measure. The next constructive task is to examine whether a principled constitution proposal can meet **all four** constraints at once: causal identifiability, stability under admissible redescriptions/grains, nonarbitrary tie and overlap handling, and independently anchored experiential predictions. If it fails, retain the failure as a constraint rather than treat the maximizer as a discovery.
