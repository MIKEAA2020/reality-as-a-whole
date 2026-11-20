# Correlation clustering: full-paper audit and an asymmetric error certificate

## What was read

The user supplied the published paper by Nikhil Bansal, Avrim Blum and Shuchi Chawla, [*Correlation Clustering*](https://doi.org/10.1023/B:MACH.0000033116.57574.95), also preserved as the [supplied PDF](sources/uploads/B_MACH.0000033116.57574.95.pdf). SHA-256: `2b43328e9799c4712a63329072369f5ee62ed1d5c887dfdd171a7d478386abec`.

Text was extracted and read from **all 25 pages** (journal pages 89–113), including proofs, the random-noise section, extensions, subsequent-work section, notes and references. Figure 1 and selected formula-bearing pages were visually inspected. Some mathematical symbols were imperfect in text extraction, and the long approximation and hardness proofs were **not independently verified line by line**; their stated results are attributed to the authors, not claimed as our own proofs. Cited predecessor and subsequent papers were not independently read. In particular, the paper's discussion of later work is historical, not a survey of the current state of the art.

## 1. What the paper actually contributes

The authors study partitions of vertices given positive and negative pair labels. A positive pair assigned to different clusters or a negative pair assigned to the same cluster is a disagreement. In their main complete, unweighted graph setting, they report that optimal clustering is NP-hard; they give a constant-factor approximation for **minimizing** disagreements and a polynomial-time approximation scheme for **maximizing** agreements. Those are related objectives but their multiplicative approximation guarantees are not interchangeable. See abstract and §§1, 3–5.

The paper explicitly observes the `++−` triangle already used in the [phenomenal-unity gate](PHENOMENAL_UNITY_AND_PLURAL_SUBJECT_IDENTIFICATION_GATE.md): no partition can satisfy all three relations (§1, p. 90). More generally, its Lemma 3 (§4, p. 94) gives a lower bound on total disagreements from a **fractional packing** of such triangles: assign nonnegative weights to conflict triangles so the total weight through any edge is at most one. The sum of triangle weights is a lower bound on the number of disagreements in every partition. The proof counts a disagreement in each triangle without overcounting an edge beyond its capacity. Figure 1 illustrates constructions used in the paper's approximation argument; the whole long argument has not been independently audited.

Section 6 assumes an actual underlying partition and **independently flipped edge labels** at a common rate below one half, and describes consequences for recovery in particular size regimes. This is a useful statistical model, but it does not establish that phenomenal-unity indicators have independent errors, an underlying exclusive partition, or a known noise rate. The paper itself points to prior work on planted partitions and noise; neither this project nor the authors should be credited with inventing those general ideas.

Section 7 treats two distinct weighted objectives. With linear costs, a zero-weight edge contributes a constant `1/2` regardless of the clustering. With *weighted disagreement* costs, a zero edge contributes zero and can be treated as missing. Section 8.1 already records improvements by others after the initial work; the paper's earlier approximation ratios and open questions are not necessarily the best or open today.

## 2. Why a best score does not identify a subject count

The paper optimizes the total number of pair disagreements. The project's question is different: **what counts remain compatible with separately justified false-positive and false-negative bounds?** The distinction matters even for the paper's complete graph.

Consider positive `AB`, `BC` and negative `AC`. Every partition has at least one disagreement. A one-block partition `{ABC}` makes one negative disagreement. Either `{AB}|{C}` or `{A}|{BC}` makes one positive disagreement. All three are globally optimal with one disagreement, yet their block counts are **one or two**. An algorithm that returns a single optimum need not identify a unique count, and an optimal score cannot choose which kind of error occurred without an additional premise.

Approximation widens the issue. In an all-positive complete graph, the zero-error optimum is one block. Separating a single vertex gives two blocks and `n−1` disagreements, but an agreement fraction `1−2/n`, arbitrarily close to perfect as `n` increases. Thus high agreement alone cannot certify the exact number of clusters. This is not a criticism of the paper's algorithms: they were designed for their explicitly stated objective, not for certifying a subject count or consciousness.

The [earlier subject gate](PHENOMENAL_UNITY_AND_PLURAL_SUBJECT_IDENTIFICATION_GATE.md) accordingly retains **all** partitions meeting stated error budgets. The supplied paper strengthens the prior-art attribution: the conflict triangle and fractional-packing technique are already explicitly present, not original discoveries here.

## 3. Extending the paper's packing idea to two error budgets

The following is a small **application of weighted counting**, not a claim of a new optimization method. Let a declared set of positive and negative pair records be available; omitted pairs are unknown. A candidate partition has `FP` positive records cut between blocks and `FN` negative records placed inside blocks. Assume separately justified budgets `FP≤a` and `FN≤b`. As in the earlier gate, interpreting a block as a subject-occurrence requires additional exclusivity, unity, occurrence and calibration premises.

Let `T` be any set of observed `++−` conflict triangles, with nonnegative weights `r_t`. For some `λ≥0`, require

```text
Σ(t contains e) r_t ≤ 1     for each observed positive edge e,
Σ(t contains e) r_t ≤ λ     for each observed negative edge e.
```

Every partition must disagree with at least one edge of each conflict triangle. Counting the chosen triangle weights through the partition's disagreeing edges gives

```text
Σ_t r_t ≤ FP + λ FN ≤ a + λ b.
```

Consequently, if `Σ_t r_t > a + λ b`, **no** exclusive partition can satisfy the stated budgets. This is a one-sided infeasibility certificate: if it does not fire, feasibility is not established. `λ=1` gives the paper's standard edge-capacity style of lower bound; allowing a distinct negative-edge capacity uses the project's separate error accounting. One could search for weights and λ using an appropriate optimization method, but no new efficient general-purpose solver is supplied here.

### Worked case: three conflicts sharing one negative edge

Let the only negative recorded pair be `AB`, and let the six positive pairs be `AXᵢ` and `BXᵢ` for `i=1,2,3`. The three `ABXᵢ` triangles all share `AB`, while their positive edges are distinct. Other pairs are unmeasured.

- An ordinary packing with capacity 1 on every edge has total weight at most 1, because every conflict uses the same negative edge. This does not reject the combined-error budget `a+b=2`.
- Set each triangle's weight to 1 and `λ=3`. Positive-edge load is 1 and negative-edge load is 3. The certificate is `3≤a+3b`; with `a=2,b=0` it is violated, so no permitted partition exists.
- With `a=3,b=0`, put A in one block and B together with all X's in another: exactly three positive records are wrong and the negative is correct. With `a=0,b=1`, put everything in one block: only AB is wrong. Thus neither of those budgets can be rejected in this example.

The conclusion is **not** that anyone has zero, one, or several subjects. It is that the idealized partition assumption and the specified observation/error premises cannot all be true under the rejected budget. A flawed pair indicator, dependence or drift, misidentified aspects, an invalid error bound, or a nonexclusive unity ontology could each account for the conflict.

### What triangles cannot see

The observed positive path `A−B−C−D`, together with the observed negative pair `AD` and no other observed pairs, is inconsistent with an error-free partition: transitivity of the positive links forces A and D together. But it contains **no fully observed conflict triangle**. A triangle-only packing returns no certificate, despite infeasibility. The prior positive-component check detects this case. More generally one can reason with positive-path/negative-edge conflicts, but neither sparse observed conflicts nor a successful partition alone establishes experiential truth.

## 4. A useful interpretation detail about zero edges

On p. 109 the authors say that under weighted disagreement, zero-weight edges can be regarded as missing. On p. 110 they describe finding a perfect clustering by removing negative edges and taking connected components. This is correct when “graph” means the graph **with zero edges omitted**, as their preceding discussion permits; it is not correct if a literal complete graph retains zero edges during that deletion.

For instance, with `AB=+1`, `BC=−1`, `AC=0`, the perfect partition is `{A,B}|{C}`. If zero edges are retained when deleting BC, `AC` connects A to C and all three are wrongly merged. The project's implementation correctly takes components of the **positive-edge graph**, treating unknowns as absent. We flag the interpretive ambiguity rather than claiming a substantive error in the paper, because the paper explicitly licenses treating zero edges as missing.

## 5. Implications for the experiential whole

The added certificate can rule out a particular combination of **exclusive-field model, fixed experiential aspects, pair readings, and error budgets** without having to enumerate all partitions. This gives the proposed framework a sharper way to say which assumptions are in tension. It does not decide *which* premise failed, and the bound is useful only if the pair labels and joint target-domain error budgets are independently warranted.

Actual first-person experience is an accepted datum, not a clustering output. No physical correlation, controller, shared information, fitted graph or algorithm supplies the experiential bridge. Nontransitive or shared experience may require a different ontology from the partition model, and the paper says nothing about whether such alternatives describe real subjects. The certificate does not establish experience, subject plurality, qualitative character, self-subsistence, physics, or **full structural and experiential intelligibility**. No universal subject or external temporal actualization is assumed.

## Verification

Run `python verification/correlation_clustering_asymmetric_certificate.py`. The [receipt](verification/correlation_clustering_asymmetric_certificate.json) checks the triangle inequality against 3,720 partition cases drawn from all 760 signed partial graphs through four vertices, the five-vertex shared-negative example, the longer-path limitation, the tied optimum and zero-edge example. The general certificate follows by the explicit weighted-counting argument, not by enumeration. The checker uses no biological or phenomenal observations.
