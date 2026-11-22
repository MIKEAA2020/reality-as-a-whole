# A stronger subject-boundary candidate fails a many-weak-links test

## Result

The [previous boundary test](REAL_CASE_WITNESS_AND_MAXIMAL_RULE_BOUNDARY_TEST.md) exposed the weakness of merging everything connected by any positive path. The repository already had a more discerning alternative: the **overlap-local minimum-cut selector L** in the [competing-rules analysis](COMPETING_SUBJECT_CONSTITUTION_AND_LOCALITY_GATE.md). It keeps two strongly connected pairs separate when they are joined by a single weak edge.

That repair does **not** generalize automatically. In an exact family of graphs with two large, internally cohesive blocks, L selects the whole as one field even as **every individual cross-block link and the total cross-block strength relative to within-block strength tend to zero**. Many weak links can collectively outweigh a minimum cut. This is a mathematical stress test of the project's existing rule—not a finding about brains or communicating people.

A simple size-normalized score avoids this specific failure and still merges a uniform graph. But it has a previously identified symmetry/tie problem and remains dependent on the chosen units, causal graph and time horizon. **Verdict:** neither rule is ready to serve as the framework's subject-constitution principle. The useful advance is a more demanding, explicit boundary requirement and a concrete candidate repair, not a discovery of consciousness.

## 1. Reuse the actual existing rule

For a finite undirected graph with nonnegative, symmetric edge weights, define the cohesion score `c(S)` for a candidate subset `S` of at least two nodes as the **sum of edge weights across the least-weight nontrivial cut inside S**. Compare a positive-scoring S with *every other positive-scoring subset that overlaps it*:

- S is a **strict winner** if its score exceeds each overlapping rival's score.
- If no rival scores higher, but an overlapping rival ties, retain S as **unresolved**, not as a definite subject.
- A candidate beaten by any overlapping rival is not selected. Strict winners cannot overlap.

In the earlier project model, associating each winner with one experience is an **extra phenomenal postulate**. We do not assume it here. The score is an unnormalized, undirected minimum cut, **not IIT**, not a directed neural influence measure and not a known measure of conscious unity. The eligibility of nodes, their units, the weights, their interventions, and the time horizon are assumed supplied. No physical or experiential calibration is claimed.

L previously handled two unequal pairs connected by one weak link. That was an important but narrow example. The following construction tests whether its behavior depends on the **number** of weak links.

## 2. Two cohesive blocks, increasingly many weak links

For any integer `m≥3`, take two blocks A and B of `m` nodes each:

```text
within each block: every pair has weight 1
between blocks: every pair has weight ε ≥ 0
```

All candidate subsets are considered; the selector is **not** given A and B as privileged labels. They are distinguished for the analysis by the input weights. We make no claim that such a graph accurately represents people, brains, or the operational influence construction in the earlier spin model. In particular, the edge weights are invented; we have not shown that this entire family is realized by a common biological transition kernel.

| Cross weight | Original L: unnormalized cut | Alternative: cut divided by subset size |
|---|---|---|
| `ε=1/(2m)` | A and B are separate strict winners | A and B are separate strict winners |
| `ε=1/m` | The **whole** `A∪B` is the only strict winner | A and B are separate strict winners |
| `ε=1` | The whole is the only strict winner | The whole is the only strict winner |

At `ε=1/m`, a cross edge has only `1/m` of the weight of a within-block edge. There are `m²` cross edges, however. Total cross weight is `m`, versus combined within-block weight `m(m−1)`; the ratio is `1/(m−1)`. Both the **individual** and the **aggregate relative** cross strengths go to zero as m increases, while the unnormalized selector continues to choose the whole. Cross strength is not absolutely vanishing: its sum is `m`, and each node has total cross weight `1`.

For a numerical illustration with `m=4`, each core's minimum-cut score is `3`. At `ε=1/8` the whole's score is `2`, so the original L keeps the cores. At `ε=1/4`, its whole score is `4`, exceeding either core, so L selects the whole. These are exact invented weights, not empirical estimates or a suggested subject-fusion threshold.

### Why the original rule changes its answer

For a mixed subset containing `a` nodes from A and `b` from B, the cut separating its A and B nodes has weight `abε`, so its minimum-cut score is at most `abε`.

- At `ε=1/(2m)`, every mixed subset scores at most `m/2`, strictly less than either full core's `m−1`. Every proper subset within a core scores less than that core. Thus the two full cores are the strict overlap-local winners.
- At `ε=1/m`, the whole's minimum cut is exactly `m`. If a cut splits both cliques, its within-block contribution is at least `2(m−1)`; if it splits one, the within-block contribution is at least `m−1` and the crossing links contribute at least `1`; if it separates the whole cliques, the crossing contribution is `m`. A singleton cut attains `m`.
- Every node has whole-graph weighted degree `m`. A proper subset omits at least one neighbor connected by at least `1/m`, so a singleton cut inside that subset has weight at most `m−1/m`. Every proper subset therefore scores strictly below the whole, which overlaps all candidates and is the unique L winner.

The minimum strict gap from the whole to any proper candidate is at least `1/m`. If every edge weight changes by at most `η` while staying nonnegative, every cut weight changes by at most `m²η`, and so does each minimum-cut score. Therefore the whole remains the unique original-L winner for

```text
η < 1/(2m³).
```

This is a **sufficient** fixed-node, fixed-candidate, uniform edge-error bound; it is not claimed optimal or applicable to observational uncertainty, hidden nodes, altered interventions, or a different time horizon. The pathology is not just an exact tie, although its guaranteed robustness shrinks with m.

## 3. A constructive repair—and its cost

Now use the **same candidate family and overlap-local comparison**, but define

```text
c_norm(S) = c(S) / |S|.
```

This size-normalized score is already used elsewhere in the project's [tie and persistence analysis](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md); we do not claim to have invented it. At `ε=1/m`, each whole core has normalized score `(m−1)/m > 1/2`. For every mixed subset,

```text
c_norm(S) ≤ ab / [m(a+b)] ≤ (a+b)/(4m) ≤ 1/2.
```

The middle inequality is `4ab≤(a+b)²`. A proper subset of a core has strictly lower normalized score than that full core. Consequently the two cores are the only strict winners. When every edge is `1`, a subset of size `k` scores `(k−1)/k`, strictly increasing in k; the whole uniquely wins. Thus normalization repairs **this** benchmark without merely declaring that interacting systems can never join.

It does not follow that this is the correct boundary rule. In the three-node path `0—1—2` with both edge weights `1`, normalized scores of the two adjacent pairs are `1/2` and the triple's is `1/3`. The overlapping pairs tie for the maximum and reflection exchanges them. Under strict, nonoverlapping, relabeling-invariant local selection, there are no strict winners and both pairs are unresolved. This is the previously documented [symmetry obstruction](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md), not a new discovery. Returning uncertainty avoids an arbitrary label but is not a completed ontology; selecting one, both, or the weaker triple adds a substantive rule. It does **not** follow that there is no experience.

Dividing by the number of written nodes also makes the answer sensitive to how a physical system is partitioned into units. Changing grain can create different candidate subsets and different denominators; a simple node relabeling check is not invariance under coarse-graining or an arbitrary state-coordinate transformation. Nor does either cut account capture directed effects, synergy, delays, state dependence, feedback memory or intervention cost without additional definitions. It would be mistaken to apply it directly to real conversational links and count minds.

## 4. What this requires of a serious realization rule

Before promoting any boundary selector to a constitution principle, it should supply and test:

1. **A realization domain:** which degrees of freedom and admissible interventions are real at the proposed grain, including background, relevant state, physical direction, time horizon and externally coupled variables. A chosen graph is input, not something a score derives.
2. **A scaling principle:** why system size, number of weak channels, shared environments and multiple time steps should or should not alter the verdict. This example shows why one weak-edge check is insufficient. Neither raw sums nor normalization by `|S|` is automatically privileged.
3. **Redescription and boundary transport:** which relabelings preserve the answer, and which changes of coarse-graining or intervention family represent the same system. A lossy coarse-graining is not automatically an equivalent realization; both justified invariance and meaningful sensitivity must be stated.
4. **Ties, overlap and persistence:** an explicit treatment of symmetric overlaps, indefinite cases, nested supports and identity through change. A missing strict winner is not an observation of unconsciousness.
5. **A separately supported experiential bridge:** why a selected realization is a perspective, which contents belong together, why particular qualities have their character, and how the candidate would make defensible first-person or physical predictions. Fitting desirable subject counts alone presupposes rather than establishes those claims.

A prospective real-world application would need independently measured influence and uncertainty, a validated realization mapping and a target-specific report or other justified observation model. We have not established any of them. The relevant two subjects in an interpersonal case are not created by graph labels, and their distinctness is not logically guaranteed merely by observing two bodies or two channels.

## 5. Status and reproduction

The [exact checker](verification/subject_boundary_dense_weak_links.py) enumerates **all candidate subsets** for the symmetric graphs at `m=3,4,6` and all three link regimes, comparing the original L and the normalized variant. The [receipt](verification/subject_boundary_dense_weak_links.json) records supports and scores. The [tests](verification/subject_boundary_dense_weak_links_test.py) compare the new cut calculations and selector to the existing implementation for six nodes, check all subset types for the `m=3…12` strict-gap claim, and verify the three-node tie. The all-m conclusions and robustness radius follow from the proofs above, not from the finite enumeration.

```sh
python verification/subject_boundary_dense_weak_links.py
python -m unittest discover -s verification -p 'subject_boundary_dense_weak_links_test.py'
```

**Bottom line:** the earlier local rule really does improve on raw reachability in its original example, but it is not a general solution to plural subject boundaries. The normalized alternative earns a further test, not acceptance. None of this explains why there is experience, its felt quality, self-existence, or how the framework recovers physics; the central bridge remains open.
