# Constructive step 21: controlled order, measure, and metric completion

## Result and scope

[Step 20](../order_reconstruction/REPORT.md) reconstructed anonymous finite grids but did not justify a continuum. Here a **specified coherent infinite refinement** has an order completion, and additional valuation hypotheses give a compatible Borel measure. Further regularity, stated separately, permits a nondegenerate Lorentzian metric in a chosen smooth chart. A smooth curved example and several failure cases make these distinctions constructive.

This is a conditional completion theorem for one refinement class, not an extrapolation from finitely many observed levels or a continuum limit of the quantum walk. The finite source orders may be anonymously labelled; their coherent embeddings supply the information needed to align the reconstructed factors across levels. The hypotheses themselves remain inputs.

Thirty-two exact finite tests check examples and certificates. Infinite claims below use the stated arguments and standard completion/measure results, not the test count.

## 1. The actual source is an infinite coherent system

At level n take an anonymous order isomorphic to C_(2^n+1) × C_(2^n+1), recognized as in step 20. Supply compatible order embeddings into level n+1 that are products of endpoint-preserving chain embeddings, inserting one new point between each old pair of adjacent factor points. Recovered factor names must be transported coherently; arbitrary unexplained axis changes between levels are not permitted.

After choosing names for the two factors, the embeddings have rank form

\[
(i,j)\longmapsto(2i,2j).
\]

The normalized ranks i/2^n identify the direct-limit factor with the dyadic rationals D in [0,1]. This is a representation of the **refinement order**, not a claim that each inserted point bisects proper length. Biased-volume examples below make that distinction explicit.

Every nonempty order interval in D contains further dyadics, and the endpoints remain fixed. Its Dedekind completion is a closed interval. Taking the product gives an ordered square, represented as [0,1]² with product precedence. Its interior is a two-dimensional topological patch; it is not all of Minkowski space, and the added boundary is not automatically a physical spacetime boundary.

The construction is independent of opaque node names. Other increasing interval coordinates describe the same completed order. A finite prefix alone supplies neither this entire refinement system nor a unique continuation; changing the unobserved tail can change its measure and regularity.

### A raw inverse limit is not already an interval

Nested binary cell addresses form {0,1}^N. With the cylinder topology this is a compact totally disconnected Cantor space, not a connected interval. Binary evaluation

\[
b(\epsilon)=\sum_{r\ge1}\epsilon_r2^{-r}
\]

is a continuous surjection onto [0,1], but not injective. At internal dyadic endpoints, a terminating expansion and an expansion with a tail of ones represent the same point, for example 0.1000… = 0.0111… . Apart from these pairs, expansions are unique: at the first differing digit equality is possible only when the entire remaining tail maximizes the opposite difference.

The interval is the quotient by those endpoint identifications. Equivalently use the direct-limit vertex order and its Dedekind completion. Simply attaching a limit symbol to the finite discrete cell spaces would instead produce the wrong topology. The two-axis construction requires this distinction in both factors.

## 2. Consistent valuations and a sufficient measure-extension condition

Let w_n(i,j)>0 be the supplied mass of each dyadic cell, with finite total mass M>0 and

\[
w_n(i,j)=\sum_{a,b\in\{0,1\}}w_{n+1}(2i+a,2j+b).
\]

A finite cell matrix and its rectangular sums recover the finite interval valuation. For an infinite system, parent additivity alone is not enough to identify these numbers with a measure on the intended half-open interval cells.

Define the largest marginal strip masses

\[
s_n^u=\max_i\sum_jw_n(i,j),\qquad
s_n^v=\max_j\sum_iw_n(i,j).
\]

A useful sufficient additional hypothesis is

\[
s_n^u\longrightarrow0,\qquad s_n^v\longrightarrow0.
\]

This is a non-atomic marginal condition, stronger than merely requiring the largest individual cell mass to tend to zero. It is sufficient for this construction, not asserted necessary for every measure that might contain atoms away from ambiguous endpoints.

### Construction and uniqueness

Consistent normalized cylinder weights w_n/M define a probability measure on pairs of binary address sequences, by the standard finite-alphabet extension theorem. Push it forward by b×b. The strip bounds imply that each fixed coordinate value has zero marginal mass: its one or two compatible prefix cylinders have mass bounded by a vanishing strip maximum. In particular the endpoint-identification fibres have zero mass.

Therefore the pushforward measure assigns exactly w_n(i,j) to the canonical half-open dyadic cells, with the final cell including endpoint 1. No mass is shifted across a boundary by choosing one binary expansion rather than the other. It is a finite Borel measure of mass M. Uniqueness follows because dyadic rectangles generate the Borel sigma-algebra and their values determine a finite measure. Strict positivity of all cells gives full topological support, since every nonempty open rectangle contains a dyadic cell.

This constructs a measured ordered patch. It does not yet imply absolute continuity, differentiability, or a Lorentzian volume form.

## 3. Why positivity, consistency, and vanishing cell masses can still fail

Give the v factor uniform mass. In the u address factor mix uniform mass with an atom of weight ε on the address 0.111… . At level n≥1 the special index is i_n=2^(n-1)-1, and set

\[
w_n(i,j)=\big((1-\epsilon)2^{-n}+\epsilon\,1_{i=i_n}\big)2^{-n},
\qquad0<\epsilon<1.
\]

Every weight is positive, totals and parent sums agree, and the maximum cell mass tends to zero. But the special u strip has mass at least ε for every n. Its canonical coordinate interval is

\[
[1/2-2^{-n},\ 1/2).
\]

These strips decrease to the empty set, while their masses do not tend to zero. This contradicts continuity from above for finite measures. Thus no countably additive measure on those canonical half-open cells can have exactly these values.

There is a perfectly valid measure on address space. Its binary pushforward puts an atom on u=1/2, but then the canonical interval memberships no longer match the original cylinder values. The missing boundary condition is substantive. The tests exhibit both the shrinking cell masses and the persistent strip mass, rather than silently accepting parent consistency as a complete extension theorem.

## 4. Volume density and regularity are further hypotheses

Use the normalized dyadic representation as a provisional coordinate chart. Each cell has Lebesgue coordinate area 4^-n. Put

\[
\rho_n(u,v)=4^n w_n(i,j)\quad\text{inside its cell}.
\]

### Bounded density: a measured, not yet smooth, geometry

Suppose there are constants 0<c_-≤c_+<infinity with

\[
c_-4^{-n}\le w_n(i,j)\le c_+4^{-n}
\quad\text{at every level and cell}.
\]

Strip masses are then at most c_+2^-n, so section 2 applies. The same inequalities extend from dyadic unions to Borel sets. The measure is absolutely continuous relative to coordinate area, with Radon–Nikodym density c_-≤ρ≤c_+ almost everywhere. Its cell averages are exactly ρ_n. This gives a bounded nondegenerate measurable coefficient, not a smooth metric or a classical curvature tensor.

For instance ρ=1 on u<1/2 and ρ=2 on u≥1/2 gives positive consistent bounded densities. From level one onward the cellwise functions already equal this discontinuous step. They are uniformly Cauchy but their limit is not continuous. Uniform convergence of discontinuous approximants alone is not the missing regularity theorem.

### A sufficient continuity certificate

In addition to the bounds, suppose that for every pair of horizontally or vertically adjacent cells at level n,

\[
|\rho_n(c)-\rho_n(c')|\le C2^{-n},
\]

with one C independent of n. Parent consistency makes each parent density the average of its four child densities. A child differs from its parent by at most 2C2^(-(n+1)), using at most two child-neighbor steps. Thus the successive sup-norm differences have a summable bound. The densities converge uniformly, with the safe estimate

\[
\|\rho_n-\rho\|_\infty\le2C2^{-n}.
\]

At level n, a horizontal/vertical path between the cells containing x,y bounds their density difference by C(||x-y||₁+2·2^-n). Passing to the limit proves that ρ is Lipschitz, including across the dyadic boundaries. The limit is the measure density already determined in section 2.

With the interpretation that the two factor directions are null, define

\[
g=2\rho(u,v)du\,dv.
\]

It has the desired volume dμ=ρ du dv and the product causal cones. A positive Lipschitz coefficient is still not enough for ordinary pointwise curvature everywhere.

### A separate smoothness certificate

One sufficient stronger condition is the existence of smooth reconstructions r_n on the interior patch, approximating ρ_n uniformly on compact subsets, with uniform C³ bounds on neighborhoods of those compact sets. Arzelà–Ascoli gives C²-convergent subsequences; uniqueness of the C⁰ limit identifies all subsequential limits with ρ. Hence ρ is C² on the interior and the classical curvature formula applies. Analogous uniform bounds of all derivative orders provide smoothness.

These are extra regularity assumptions, not finite tests that prove themselves. They are relative to a chosen smooth chart; the completed order alone selected an interval topology, not a preferred smooth atlas. Section 6 shows why this chart qualification matters.

## 5. A complete, smooth, curved example

Take the exact cell integrals of

\[
\rho(u,v)=1+u/3+v/2\quad\text{on }[0,1]^2.
\]

Writing h=2^-n, these are

\[
w_n(i,j)=h^2\big(1+(i+1/2)h/3+(j+1/2)h/2\big).
\]

They are positive and parent-consistent. The densities lie between 1 and 11/6; neighboring differences are at most h/2. They converge uniformly to the displayed affine density. Smooth reconstructions can be chosen to be that same affine function, with all the required derivative bounds. The total mass is 17/12.

For g=2ρ du dv, using the curvature convention of step 19,

\[
R=-8(2\rho)^{-1}\partial_u\partial_v\big(\tfrac12\log(2\rho)\big)
=\frac{1/3}{(1+u/3+v/2)^3}.
\]

This is nonzero. The compatible finite weights therefore complete to a smooth curved Lorentzian patch under the stated null-direction and chart interpretation. The construction does not force flat space merely because each finite order is a two-chain grid. It also does not solve Einstein equations or supply a physical stress tensor.

## 6. Singular chart densities and intrinsic product-volume coordinates

Positive weights and the strip condition do not force a smooth density in the normalized rank chart. For independent biased binary digits with probabilities p,q in (0,1), take

\[
w_n(i,j)=p^{s(i)}(1-p)^{n-s(i)}q^{s(j)}(1-q)^{n-s(j)},
\]

where s counts the ones in the n-digit index. These weights are consistent, positive, nonatomic and full-support. Their strip maxima decay exponentially. If p≠1/2, the limiting measure is singular relative to the rank-chart Lebesgue measure: almost every sampled u has digit frequency p, while Lebesgue-almost every u has frequency 1/2, by the independent-digit law of large numbers.

For p=2/3,q=1/3, the largest cell density is (16/9)^n and the smallest is (4/9)^n. The uniform density bounds fail dramatically. This is not a proof that the ordered measured patch admits **no** smooth geometric interpretation in any atlas.

Indeed, for any product measure Mν_u×ν_v with nonatomic, full-support marginals, the marginal cumulative distribution functions U=F_u(u), V=F_v(v) are increasing homeomorphisms onto [0,1]. In those coordinates

\[
d\mu=M\,dU\,dV,\qquad g=2M\,dU\,dV
\]

is a compatible flat Lorentzian realization. Their values on dyadic vertices are already fixed by cumulative finite weights, coherently under refinement. This is the continuum version of step 20's rank-one factorization. Coordinate origins, factor naming, and reciprocal null-coordinate boost normalization remain conventional; uncalibrated total mass retains overall scale freedom.

For the biased example these quantile coordinates are not smooth diffeomorphisms of the normalized rank chart. They transport a different compatible smooth atlas. Thus regularity failure in a chosen chart must not be promoted into coordinate-independent impossibility. Conversely selecting this product-volume atlas is a specified geometric construction, not a theorem that arbitrary measures admit a flat null realization: nonproduct valuations, such as the affine example, obstruct that construction.

The rank midpoint can have U-coordinate 1-p, rather than 1/2. This is why inserting a combinatorial midpoint never by itself justified halving metric length.

## 7. Finite observations do not certify the infinite hypotheses

For any fixed N, choose the first N binary digits uniformly and all later digits with a nonuniform bias. Every observed cell weight through level N agrees exactly with the uniform smooth completion. The unobserved tail still produces a measure singular in the rank chart. Both systems are positive, coherent and have nonatomic marginals.

Thus no finite prefix establishes the all-level density bounds, smoothness, or an independently justified refinement law. One can prove such properties from a supplied generative rule, as in the affine example; one cannot infer them solely because finitely many tests passed. Other tails can also introduce boundary failures. This is an identifiability limit, not a reason to discard conditional completion results.

## 8. Reproducibility and remaining bridges

Run `python -m unittest -v test_model.py` here, or `python research/run_checks.py` from the repository root. The 32 tests cover coherent vertices and order, shrinking cut brackets, binary endpoint ambiguity, exact parent consistency, the boundary-path failure, strip criteria, bounded and neighbor-controlled densities, the curved affine example, singular biased examples, quantile coherence, and indistinguishable finite prefixes. Rational arithmetic is exact. Diagnostic evaluation is intentionally capped at finite levels; infinite proofs are those above. Representative values are in `enumeration.json`.

**Earned:** a controlled completion of a specified infinite order/valuation system; explicit sufficient measure and regularity conditions; a smooth curved example; an intrinsic flat construction for product measures; counterexamples to several tempting automatic-limit inferences.

**Not earned:** extraction of the refinement system or its valuation from the quantum net or empirical data; a proof that its abstract factors are physical null directions; a unique preferred atlas in unrestricted model classes; global spacetime gluing, field dynamics on the reconstructed curved patch, or a matching limit of the previous quantum walk. The order/geometry branch and the CAR/Dirac branch now have explicit compatible pieces, but their common-source identification is still a missing arrow. Physical actuality, all-framework integration, phenomenal constitution, and ultimate explanation remain open; an address, cut, cell, measure, or metric is not an observer token.

**Next bridge:** match a reconstructed nonconstant volume geometry to an explicitly specified local field dynamics, rather than silently reuse the translation-invariant flat Dirac law. A curved-background Dirac operator requires its metric/spin connection, conserved inner product, state conditions, and its own approximation/locality analysis.

## Continuation: curved-background field dynamics

[Step 22](../curved_dirac/REPORT.md) supplies the conformal Dirac spin connection, conserved inner product, and a variable-coin approximation. A separate global static smooth example permits a gapped ground-state construction. The affine nonstatic example is not silently treated as static, and lattice vacuum convergence is not inferred from propagator convergence.
