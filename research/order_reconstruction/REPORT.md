# Constructive step 20: reconstructing a finite diamond grid from anonymous order

## Result and scope

[Step 19](../causal_geometry/REPORT.md) distinguished geometric inputs from reconstructed outputs. This step supplies an actual inverse map whose input has **no coordinates**: a finite set of opaque identifiers and a reflexive causal relation. For a precisely characterized class, it reconstructs a product of two finite chains, uniquely up to naming the two factors. Added interval valuations then determine elementary diamond weights, with an exact test for a compatible flat null-grid realization.

The result is deliberately conditional. A finite order determines neither a unique smooth continuum nor whether its cover edges are null. Positive valuations and a null-rectangular interpretation are additional structures. Even flat-compatible coarse valuations permit nonflat refinements and curved continuum completions.

The implementation uses finite combinatorics and exact rational valuation arithmetic. Thirty-two tests verify the reconstruction, its symmetries, rejection controls, valuation inverse, and ambiguity witnesses. The classification proof and continuum qualifications are stated below rather than inferred from a test count.

## 1. Source, target, and equivalence relation

**Order input:** P = (X, ≤), with X a finite nonempty set of distinct opaque identifiers and ≤ a supplied reflexive, antisymmetric, transitively closed relation. Neither a node's name nor its input enumeration is used as a coordinate. The enumeration can select which reconstructed axis is printed first, and nothing geometric is attached to that convention.

**Accepted source class:** finite distributive lattices whose poset J(P) of join-irreducibles is the disjoint union of exactly two nonempty chains.

**Output:** an order isomorphism

\[
\Phi:P\longrightarrow C_r\times C_s,
\]

with rank coordinates in {0,…,r-1} × {0,…,s-1}. The two chains are intrinsically recovered, but naming them u and v is a target convention. Interchanging the factor names transposes the coordinates. Once a factor is selected, its order fixes its rank order; arbitrary permutations of its elements are not permitted.

The integers are ordinal positions, **not physical lengths or times**. Translating them into equally spaced coordinates would be a new assumption. In particular r and s are sampling cardinalities, not a proved continuum spacetime dimension. A larger or different continuum can contain the same finite order.

The source model assumes its causal relation has already been established. We do not extract it from the unlabelled CAR net or prove that a physical experiment determines it without uncertainty.

## 2. An explicit reconstruction algorithm and proof

1. Check the poset axioms; reject malformed relations rather than repairing them.
2. For each pair x,y find their greatest lower bound x∧y and least upper bound x∨y. Reject if either does not exist uniquely.
3. Check distributivity. This excludes nondistributive diamond lattices that can otherwise look superficially grid-like.
4. Recover J(P): the non-bottom elements having exactly one lower cover. In a finite lattice these are precisely the join-irreducibles.
5. Form the comparability graph of J(P). Require exactly two connected components, each totally ordered, with no cross-comparabilities.
6. For each x record the number of elements in each recovered chain that lie below x:

\[
\Phi(x)=\big(|\{j\in J_1:j\le x\}|,\ |\{j\in J_2:j\le x\}|\big).
\]

The code independently checks bijection onto the full product and preservation **and reflection** of the supplied relation. It does not silently add a missing grid point.

### Why this classification works

Every element of a finite lattice is a join of the join-irreducibles below it: use induction, splitting a non-irreducible non-bottom element into a join of smaller elements. In a distributive lattice each join-irreducible j is join-prime. Indeed, j ≤ a∨b gives j=(j∧a)∨(j∧b), so irreducibility implies j≤a or j≤b.

It follows that x is completely determined by its lower join-irreducibles, and every order ideal I of J(P) is obtained from the join of its elements: join-primality prevents unintended irreducibles from entering that lower set. Thus P is the lattice of order ideals of J(P), the familiar finite distributive-lattice representation.

When J(P) is two disjoint chains of lengths r-1 and s-1, its ideals are exactly pairs of initial segments. Their sizes give the desired bijection with C_r×C_s, with meet and join equal to componentwise minimum and maximum. Conversely the join-irreducibles of C_r×C_s are exactly the non-bottom elements on its two axes. This proves the characterization and intrinsic recovery of the factors.

This is a use of standard finite lattice mathematics, not a new theorem about arbitrary causal sets. Three-axis Boolean lattices, antichains, one-dimensional chains, nondistributive lattices, and the tested punctured grid are rejected. Rejection means “outside this reconstruction domain,” not “physically impossible.”

## 3. A finite diamond need not have null edges

Consider four Cartesian points:

- bottom (t,x)=(0,0), top (2,0);
- two middle points (1,-a) and (1,a), with 0<a≤1.

For every such a the induced finite causal order is C₂×C₂. For a=1 its cover edges are null; for a=0.4 those edges are timelike. The order alone does not distinguish them.

Consequently the recovered two-chain factors are **not automatically physical null coordinates**. Calling adjacent rank rectangles “diamonds” is initially combinatorial. A Lorentzian metric interpretation below requires that they realize actual null-coordinate rectangles and that supplied interval values are actual diamond volumes with null boundaries of zero measure. That interpretation is a separate hypothesis that can be checked for compatibility, not manufactured by naming the ranks u,v.

This also prevents reading a Minkowski continuum directly out of an earlier finite circuit's causal order. Different orders can fail the accepted lattice conditions, and even an accepted one retains the embedding ambiguity above.

## 4. Interval valuations give a second, exact inverse

Add rational values V(x,y) for every pair x≤y. Under a null-rectangular volume interpretation require:

- V vanishes on intervals with zero extent in either reconstructed factor;
- the elementary adjacent two-factor diamonds have strictly positive weights wᵢⱼ;
- larger rectangular intervals are additive over their elementary diamonds, with no boundary contribution.

The inverse is simple but noncircular:

\[
w_{ij}=V\big(\Phi^{-1}(i,j),\Phi^{-1}(i+1,j+1)\big),
\]

followed by checking **every supplied interval** against

\[
V(x,y)=\sum_{i=i_x}^{i_y-1}\sum_{j=j_x}^{j_y-1}w_{ij}.
\]

All weights must be positive. The implementation rejects missing/extra interval entries, nonzero null values, zero atoms, and nonadditive large diamonds. Recovered weights are unique under these assumptions. Arbitrary positive weights also define such an abstract valuation; they do not by themselves select a smooth metric.

These values are additional numerical data on anonymous node pairs, not hidden node coordinates. Their calibration is an input. A positive geometric continuum measure would force truly timelike intervals to have nonzero volume, so the null-zero condition is substantive, not implied by finite order.

## 5. Flat null-grid compatibility and its remaining gauge

Assume a realization by null-coordinate vertices u_i,v_j in a flat 1+1 metric ds²=du dv. Set Δu_i=u_{i+1}-u_i>0 and Δv_j=v_{j+1}-v_j>0. Its weights must obey

\[
w_{ij}=\tfrac12\Delta u_i\Delta v_j.
\]

Therefore the positive weight matrix must have rank one. Conversely, if

\[
w_{ij}w_{00}=w_{i0}w_{0j}\quad\text{for every }i,j,
\]

choose Δu₀=1 as a factorization convention and set

\[
\Delta u_i=w_{i0}/w_{00},\qquad \Delta v_j=2w_{0j}.
\]

Cumulative sums yield a flat null-grid realization with exactly the supplied order and valuation. Thus positive rank one is **necessary and sufficient for existence of a flat null-rectangular realization** in this restricted class.

The factorization remains invariant under Δu ↦ cΔu, Δv ↦ Δv/c, c>0. This is the null-coordinate boost freedom, along with coordinate origins and factor interchange. The displayed Δu₀=1 is a gauge choice, not an independently recovered physical unit. Calibrated volumes determine products and, for timelike vertex pairs in a flat realization,

\[
\tau(x,y)^2=\Big(\sum_i\Delta u_i\Big)\Big(\sum_j\Delta v_j\Big)=2V(x,y).
\]

If valuations are known only up to a common factor λ², lengths remain known only up to λ, separately from the reciprocal boost gauge. This retains step 19's scale distinction.

Nonrankone data exclude a flat **null-rectangular** realization, not every possible flat embedding of the bare finite order. They could reflect curved geometry, measurement error, or failure of the null-grid interpretation. An arbitrarily small rational perturbation can destroy exact rank one; noisy data need a separate statistical tolerance/identification analysis rather than an unannounced rounding rule.

## 6. Refinement and continuum nonuniqueness

Order refinement inserts elements into either chain. The old grid embeds in the refined product by the chosen increasing index maps. Valuation refinement splits each coarse weight into positive subcell weights whose sum is the original weight. Coarsening then recovers all original rectangle valuations exactly.

But coarse flat compatibility need not survive fine resolution. For one coarse weight 4, both refinements

\[
\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}
\]

sum to 4. The first has rank one; the second does not. The entire coarse order/valuation is identical, so the coarse inverse cannot choose between them.

There are also infinitely many smooth continuum completions. On chosen unit null cells, any finite positive weight array can be realized by a positive smooth factor L in g=Ldu dv: start with a sufficiently small positive constant L₀, then add nonnegative smooth bumps supported strictly inside individual cells, with integrals chosen so that (1/2)∫cell L=wᵢⱼ. This preserves positivity and smoothness across cell boundaries. It supplies a compatible completion, not a preferred one.

If such a factor were flat everywhere on the rectangular domain, the curvature equation ∂u∂v log L=0 would force L=f(u)g(v), making all rectangular cell weights rank one. Thus nonrankone weights force curvature somewhere **within this smooth null-rectangular completion class**. Conversely rank-one coarse weights do not prove actual flatness: the sine perturbation in step 19 has identical integer-grid volumes to flat space but nonzero curvature. Both finite-data aliasing and hidden refinement persist.

Obtaining a continuum would require a specified directed refinement system, compatible measures, regularity, and a proof identifying its limit. One successful finite grid does not supply those requirements, select a topology of convergence, or derive a Lorentzian manifold from arbitrary orders.

## 7. Reproducibility and integration ledger

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover anonymous reconstruction, coordinate reflection, meets/joins, relabelling and factor ambiguity, rejection controls, valuation inversion, flat factorization/gauge, scale, refinement, hidden nonflat refinements, null/timelike embedding ambiguity, and exact rank-one sensitivity. Tests compare axes only up to their permitted naming convention; no coordinate truth is passed to `reconstruct`. `enumeration.json` records representative cases and rational values.

**Earned:** a genuine coordinate-free finite-order inverse on a proved source class, an exact valuation inverse, a conditional metric-realization criterion, and explicit refinement/embedding nonuniqueness. This is a concrete order-theoretic/geometric overlap, not just compatible vocabulary.

**Not earned:** extracting this source relation or valuation from an unlabelled quantum net; establishing physical null directions from order alone; a unique continuum, spacetime dimension, scale, law, or actual realization; full causal-set/field unification; twistor/Langlands bridges; phenomenal constitution or ultimate explanation. No lattice element, ideal, interval, or coordinate is thereby an observer token.

**Next obligation:** construct a controlled infinite refinement or completion with specified regularity and equivalence, then ask whether its interval/incidence data recover a continuum order and measure without assuming the answer in coordinate labels. Its conditionality should remain visible rather than be removed by taking a limit symbol.

## Continuation: controlled completion

[Step 21](../refinement_completion/REPORT.md) specifies a coherent refinement system, its order completion and endpoint quotient, sufficient measure-extension conditions, and separate metric-regularity criteria. It includes a smooth curved completion and counterexamples to deriving infinite regularity from a finite prefix. This is not an automatic completion of every finite order.
