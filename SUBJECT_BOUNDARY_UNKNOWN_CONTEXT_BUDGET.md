# Subject-boundary robustness when the rest of the system is unknown

## The question

A subject within a relational whole need not be isolated from everything else. The relevant task is to determine when a **proposed** local boundary remains stable despite connections to a larger context. The earlier [subject comparison](COMPETING_SUBJECT_CONSTITUTION_AND_LOCALITY_GATE.md) introduced a finite-graph diagnostic `L`, and [its hidden-edge analysis](SUBJECT_ROBUSTNESS_HIDDEN_EDGES_AND_INTERVENTION_ERROR.md) bounded uncertainty among four fixed units. The [QFT source analysis](QFT_SOURCE_RECOVERY_LOCALITY_AND_SUBJECT_GATE.md) warns against replacing physically important approximate locality with exact isolation.

Here we extend the *graph-level* question to an arbitrary finite number of additional units. The result is a mathematical property of the existing diagnostic, not a theory or detection of conscious subjects. It does not establish that QFT or brains have this graph, score, or boundary rule.

## The existing diagnostic

Take a finite undirected graph with nonnegative edge weights `w_ij`. Each candidate `S` contains at least two vertices. Its cohesion score is the ordinary weighted minimum cut **inside** `S`:

```text
c(S) = min over nonempty proper A ⊂ S  Σ_(i∈A, j∈S\A) w_ij.
```

The previously defined `L` selects `S` only if `c(S)>0` and it scores **strictly more than every different positive-scoring candidate that overlaps it**. Equal-scoring undefeated overlaps remain unresolved. Disjoint candidates are not competitors. A selected set is a proposed subject only under an additional, unvalidated experiential postulate.

Weighted min-cut is established graph theory, not a new invention; see Stoer and Wagner, [“A simple min-cut algorithm,” DOI 10.1145/263867.263872](https://doi.org/10.1145/263867.263872) (abstract and bibliographic page inspected, not a full proof audit). `L` is our earlier simplified diagnostic; it is **not** [IIT 4.0](https://doi.org/10.1371/journal.pcbi.1011465), whose cause–effect structure, exclusions and state dependence are different. We inspected the latter paper's abstract and author summary for this comparison, not its full code or proofs. The inequality below is an elementary application to this particular selector; we do not claim literature-wide mathematical novelty.

## Result: a total-leakage certificate

For a candidate core `S`, define its **total external weighted connection** by

```text
D(S) = Σ_(i∈S, j∉S) w_ij.
```

Assume:

1. `S` is a strict winner against all of its eligible proper subsets of size at least two, when its internal edges are considered on their own. For a two-vertex core this condition is automatic.
2. Its internal minimum cut is strictly larger than its total external weight: `c(S) > D(S)`.

Then `S` is a strict `L` winner in the **entire finite graph**, regardless of how many outside vertices there are or how strongly they are connected to one another.

**Reason:** An overlapping competitor is either wholly inside `S`, where condition 1 defeats it, or it includes at least one vertex in `S` and at least one outside it. In the latter case the cut dividing those two portions has weight at most `D(S)`, so the competitor's *minimum* cut cannot exceed `D(S)`, which is less than `c(S)`. Candidates disjoint from `S` do not compete with it. This is an analytic proof for the declared finite graph and selector, not an extrapolation from the code.

For a pair `{a,b}` with internal edge `w>0`, this simplifies to:

```text
w > Σ_(j outside {a,b}) (w_aj + w_bj)    ⇒    {a,b} is a strict L winner.
```

The total matters. Saying that each individual outside connection is small does not bound their sum. Conversely, the condition is sufficient, **not necessary**: if it fails, the pair may still be a winner. Its usefulness depends on an actual justified upper bound for *all* relevant external weights and on the stability of the core's internal score.

## Applied to the existing four-spin case

At the earlier reference point, the two outer pairs have internal score `10/21`. For each, the only original outward edge has weight `4/21`, so the total remaining budget before the sufficient condition ceases to certify that pair is

```text
10/21 − 4/21 = 2/7.
```

If the original weights stay fixed and each pair's **sum** of new connections to any finite set of outside units is strictly below `2/7`, both pairs remain strict `L` winners. The exterior may have arbitrary nonnegative internal edges. This extends the earlier fixed-four-node robustness result in a different direction; its uncertainty radius `2/35` does not automatically apply to infinitely many unobserved units. At equality this certificate no longer guarantees a result. In particular, finite-data estimates cannot simply establish an upper bound on genuinely unmeasured couplings without additional assumptions.

This is a conditional statement about the weights **in the extended graph**. It does not show that adding a physical environment leaves the original interventional weights unchanged. Our original weights depend on interventions and a chosen background distribution, which could change with the larger dynamics. Before using this result physically, one must justify that representation and bound its context-induced changes.

## Why per-edge smallness fails

Let the original pair have weight `1`. Add `k` outside vertices, with every newly added edge—including outside-to-outside edges—equal to `ε=1/k`. Thus each individual new edge can be made arbitrarily small as `k` grows. But the whole `(k+2)`-vertex graph has minimum cut

```text
c(whole) = (k+1)/k > 1 = c(original pair).
```

Every proper candidate has a smaller score, so the whole graph becomes the unique strict `L` winner; the original pair is no longer selected. The original pair's total external weight is `2kε=2`, not small. This construction is deliberately dense, with growing numbers of links and large aggregate resources: it is **not** a realistic claim about biological or quantum systems. It demonstrates why a per-link bound alone is mathematically insufficient in this rule.

The threshold `D<w` is sharp as a **universal sufficient bound for pairs**. A four-node cycle with pair weight `1` and the three other cycle edges each `d` has `D=2d` and full-set score `2d` for `0<d≤1`. For `d<1/2` the pair wins; at `d=1/2` it ties with the whole set; above `1/2` the whole set wins. Thus one cannot replace `D<w` with `D≤w` and still guarantee a strict pair winner for every graph. This does not mean that every graph with `D≥w` fails, or that a sharp physical threshold for subjecthood exists.

## What this does—and does not—contribute

The useful step toward a plural-subject account is **bounded contextual independence rather than absolute separation**: a local candidate can survive a specified amount of external coupling within this explicit rule. This is more precise than saying merely that subjects are separate patterns or that their interactions are weak.

But several bridges remain open:

- **Representation:** the graph assumes declared units, symmetric nonnegative influence weights and admissible subsets. Directed influences, inhibition, different time grains, changing backgrounds and coarse-graining could change the result. This is not a QFT theorem; there is no direct derivation of `D` from field-locality tails or a continuum limit.
- **Physical measurement:** an external leakage budget must be derived or bounded with justified interventions, including latent units and measurement error. Physical correlations do not automatically equal causal influence, nor do pairwise edges capture all higher-order effects.
- **Phenomenal identity:** selecting a robust graph subset does not show that it is one experiencer, which qualities it has, or whether other subjects overlap it. The prior [interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) shows how different subject rules can attach different labels to the same physical and report distributions.
- **Actuality and the whole:** this graph is a local comparative model, not an account of why the whole is self-sufficient or why genuinely possible realities are actual within it. It presupposes neither an external clock nor a universal subject; it proves neither a timeless ground nor emergent spacetime.

## Verification

Run `python verification/subject_boundary_external_budget_gate.py`. Its [receipt](verification/subject_boundary_external_budget_gate.json) records an exact-rational exhaustion of 3,125 four-node graphs, the three threshold examples, the previous four-spin values and complete proper-candidate checks for two dense-context examples. These numerical checks are finite and support implementation correctness; the general certificate is the separate argument above. No new human data, experiential assay, or claim that the substantive framework is complete is involved.
