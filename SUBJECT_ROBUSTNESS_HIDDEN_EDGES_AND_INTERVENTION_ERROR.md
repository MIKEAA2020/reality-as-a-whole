# Subject-rule robustness with hidden edges and imperfect interventions

## Result

The earlier [four-spin certificate](SUBSTRATE_CONTEXT_HORIZON_AND_ROBUSTNESS.md) assumed all non-neighbor connections were exactly zero. Removing that assumption gives a tighter, **sharp** graph-level result for the existing stipulated C and L rules:

> If every one of the six nonnegative pair weights differs from the reference graph by at most `η`, including the three originally zero weights, then **for `η < 2/35`** C still selects the whole four-spin component and L still selects the two outer pairs with no ties. At `η = 2/35`, a permitted graph produces overlapping L ties, so the strict radius cannot be enlarged for this claim.

This is an exact theorem for the specified finite graph/rules, not evidence that the spins are subjects, that every permitted graph comes from an actual physical spin system, or that the user’s framework is complete. Its point is to carry **bounded uncertainty, including small previously absent edges**, through the existing comparison rather than assuming away precisely the features that could change it.

A separate illustrative calibration budget accounts for imperfect clamps, readouts and sampling. Under its explicit idealized assumptions, the sample-size bound is **15,260 trials per cell for 24 cells**, a very conservative toy calculation—not an experimental proposal for a person or an observed result. A separate full-kernel assumption is needed to extend the comparison over a local history. None of these bounds calibrates an experience assay.

## 1. The fixed reference and what the rules mean

The reference is the existing [interventional influence model](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md), at `t=1/4`, with four nodes and symmetric nonnegative weights

```
w*01 = 10/21,   w*12 = 4/21,   w*23 = 10/21,
w*02 = w*03 = w*13 = 0.
```

C selects the positive-graph connected component `{0,1,2,3}`. L assigns each candidate subset of at least two nodes its minimum total weight crossing any nontrivial internal cut, and selects strict local maxima among **overlapping** subsets. L selects `{0,1}` and `{2,3}`. These are *stipulated subject labels*, and the pair of rules is the one in the [fixed interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md). Neither is IIT 4.0 or a validated consciousness model.

The present extension allows all six weights to vary, including the three zero reference weights. It remains a four-node model: an entirely unobserved fifth node, a different factorization, changing backgrounds, negative-weight semantics, or altered time grain is not covered. Nonnegative weights are part of the input definition; below we say exactly how clipping can produce them.

## 2. Graph-level bound, including a sharp boundary witness

Let `w` be any nonnegative symmetric four-node graph with

```
max_(i<j) |w_ij − w*_ij| ≤ η.
```

For a candidate set `S`, its score is the minimum of its internal cut sums. A cut of a four-node set crosses at most four pairs, so changing every pair by at most `η` changes any candidate score by at most `4η`. Each outer pair has only one internal edge, so its score changes by at most `η`.

At the reference graph, each outer pair scores `10/21`; all **nine other** subsets of size two through four score at most `4/21`. Thus each outer pair exceeds every other candidate's score by at least

```
(10/21 − η) − (4/21 + 4η) = 2/7 − 5η.
```

For `η < 2/35`, this is strictly positive. The two outer pairs are disjoint, so L's overlapping-rival rule selects each; all other size-at-least-two candidates overlap one of them and are strictly dominated. C still selects all four nodes because the original three path edges remain positive. This proves the claim for **all** nonnegative graphs in the specified radius, not just the finite test grid.

The radius is sharp for that exact claim. At `η=2/35`, decrease `w01` and `w23` by `η`, increase `w12` by `η`, and increase all three previously zero weights to `η`. The two outer pairs and the whole set then all score `44/105`. The two pairs and the whole are overlapping tied L candidates, so L no longer returns the original two strict winners. C still selects the whole. This witness establishes failure of the guarantee at the boundary; it does not say the reference physical model actually has those changed weights. The [verifier](verification/four_spin_hidden_edge_robustness.py) additionally checks 729 illustrative perturbation combinations at `η=1/20`.

The bound is smaller than the earlier fixed-chain value `1/7`: extra edges can contribute simultaneously to a cut. This is exactly why treating uncertain zeros as fixed structural facts can give an overconfident certificate.

## 3. From imperfect interventions to an edge-error budget

For every ordered pair `j→i`, specify two intervention cells, clamping `j` to `+1` and `−1`, with the other two nodes randomized according to a **fixed declared background distribution** and a binary readout of `i`. There are 12 directions and **24 cells**. Let each ideal cell probability be `p`, and define the signed directional influence as the difference of its two cell probabilities. Define a symmetric nonnegative weight by

```
w_ij = max(0, min(d[i→j], d[j→i])).
```

At the reference model this agrees with the earlier weights. Clipping is an explicit convention, not a claim that it is the unique correct treatment of inhibitory effects. If each estimated cell probability differs from its ideal target by at most `e`, then each estimated directional difference is within `2e`. The minimum and clipping maps are 1-Lipschitz in the maximum norm, so every estimated pair weight is within `2e` of its target. This accounts for all six pair weights, not just the originally present edges.

### A conditional numerical budget

Assume independently justified bounds on:

- **physical drift:** the true four-node target weights differ from the reference weights by at most `1/100`;
- **clamp bias:** each intended cell's observed mean differs from the ideal target due to imperfect intervention by at most `1/400`;
- **readout bias:** the additional mean error is at most `1/400`;
- **sampling:** the observed sample mean of each cell differs from its actual mean by at most `3/200`.

Then, by the triangle inequality, the estimated graph differs from the reference by at most

```
1/100 + 2(1/400 + 1/400 + 3/200) = 1/20 < 2/35.
```

The true graph is also within the certificate under the assumed physical-drift bound. Thus the two rules give their reference verdicts on both the true and estimated graph whenever all those bounds hold. The drift and bias bounds are **assumptions needing independent calibration**, not facts inferred from this calculation or from the same subject label.

For the sampling term, assume `n` independent, identically distributed bounded outcomes **within each cell**, with a fixed mean. Hoeffding's inequality and a union bound over 24 cells give

```
P(any cell's sampling error > 3/200) ≤ 48 exp[−2n(3/200)²].
```

`n=15,260` gives an upper bound about `0.049997` on this failure, i.e. at least 95% simultaneous sampling coverage **conditional on the preparation, drift and bias assumptions**. That is 366,240 total trials. Independence *between* cells is not required by the union bound, but independence and stable means within each cell are required for the stated Hoeffding step. Systematic dependence, condition-dependent confounds, background mismatch, preparation error beyond the stipulated bounds, and adaptive reuse of the data need their own analysis. See [Hoeffding (1963)](https://doi.org/10.1080/01621459.1963.10500830); neither this numerical illustration nor the theorem supplies the missing calibration.

A clamp-error probability does not automatically yield the stated `1/400` bias under arbitrary confounding. A sufficient **model-specific** condition would be that, within each cell, the observed distribution is a mixture of the intended ideal response and an arbitrary contamination with mixture weight at most `1/400`, with the specified background otherwise controlled. A separately bounded readout-error probability can add at most `1/400` to a binary mean. If these conditions are not justified, the bound cannot be used.

## 4. Time-horizon and phenomenal checks remain separate

The graph calculation concerns interventional scores at a **single specified local update**. It neither implies nor estimates a uniform discrepancy between complete dynamical kernels. If a separate physical analysis establishes that such kernels have the same initial distribution and per-row total-variation discrepancy at most `1/10,000` under all relevant operations, the standard [coupling bound](SUBSTRATE_CONTEXT_HORIZON_AND_ROBUSTNESS.md) bounds the discrepancy of the full 100-step physical path laws by

```
1 − (1 − 1/10,000)^100 ≈ 0.009951.
```

This is a hypothetical **additional premise**, not a consequence of edge stability or its 24 cells. It applies only to the specified representation, actions, starting distribution and physical record mapping. Local steps need not imply a fundamental universal clock.

Even if the physical graph and path bounds are both established, C and L can still attach different subject labels to the same physical history. An ordinary fixed device that calculates C or L is not a subject-unity detector. The existing interface's hypothetical 10%-error experience channel and its independence assumptions would distinguish packages *if calibrated*; no such real channel follows from either bound. A feedback/readout model whose report predictions depend on the selected experiential package is an **additional bridge** and must not be smuggled into the physical-kernel bound.

Consequently this result constrains a **candidate organizational comparison** for substrate-independence, rather than proving experience is multiply realizable or determining its type. Type equivalence, numerical subject identity, persistent memory, and a self-location measure are separate obligations. None requires a literal simulator, an external creator or a universal subject.

## 5. What to do with the result

The earlier fixed-topology comparison is now robust to a specified amount of **unmodeled connection among the four declared units**, and an independently stated toy intervention budget can certify that robustness. This is a mathematical advance within the frozen interface, not a full solution. The next genuinely substantive requirements are:

1. Replace the four-node assumption and stipulated nuisance bounds with a justified physical organization and intervention model, allowing additional units and context; or show a principled reason a coarse-grained four-unit closure is adequate.
2. Specify the relation between dynamical kernel bounds, persistence and a phenomenal target without inserting the disputed experience label into the physical input. Calibrate any experiential assay independently.
3. Derive, rather than stipulate, the selected realization's experiential quality and relation to the self-existent experiential whole; recover physical and local temporal structure and justify subject measure.

The [frozen battery](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) remains incomplete for B1–B2, subjects/quality, physics/time, measure and empirical discrimination. Strong possibility=actuality remains the user's thesis: no hypothetical perturbation, graph state or formal counterexample here is asserted to be a genuinely possible but unrealized world. No Roy data were reused.

## Reproduction

Run `python verification/four_spin_hidden_edge_robustness.py`. The [receipt](verification/four_spin_hidden_edge_robustness.json) contains the 729 grid cases, exact boundary witness, sample-size arithmetic and independently assumed 100-step bound. The strict `2/35` guarantee is the analytical argument above, not inferred merely from the grid; the sample-size calculation does not certify its own premises. The related context and subject-interface checks passed, as did all 21 selected bounded framework regression scripts; those exits do not establish the substantive framework.
