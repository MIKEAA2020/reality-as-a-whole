# Plenitude, symmetry and the measure of plural perspectives

## Result

The thesis that every genuinely possible local reality is actual does **not**, on its own, say how much weight any subject or record should receive. Symmetry can narrow that freedom, but only when the relevant symmetry and its connection to probability are independently justified.

In an explicit plenitude toy with two distinguished kinds of local center and every infinite binary record present:

- If the measure is invariant under every finite reversal of record bits **within each kind**, its conditional record law is uniquely fair, even without separately assuming independence.
- That symmetry still leaves the **relative weight of the two kinds** completely open. A further symmetry that truly exchanges the kinds, plus measure invariance under that exchange, forces equal weights.
- The same set of actual records also supports biased probability laws if those record-bit reversals are not required to preserve the measure. Different laws can give **mutually singular** typicality judgments despite agreeing that every finite record is present.

This is a conditional construction and application of known probability mathematics—not a derivation of the Born rule, the real whole's self-subsistence, or the existence of any subject. It sharpens the missing bridge between the user's actuality thesis, plural perspectives, and empirical probabilities.

## 1. The scope: one whole, local distinctions, no creator

The working proposal is a self-sufficient, timeless whole with experiential intrinsic nature and genuinely plural subjects or perspectives. The user's strong thesis is that what is genuinely possible is actual **within that whole**; what is not actual was not genuinely possible. This is not a temporal process in which possibilities wait to become real, and it does not posit an external simulator, creator, universal agent, or a world selected from outside.

We will use `H={0,1}^N`, the mathematical space of infinite binary records, and two distinguished local types `A,B`. The formal center space is

```text
C = {A,B} × H.
```

As a **stipulation of this toy**, let every center `(type,h)` be realized in the same formal whole; and separately suppose that centers have the intended local experiential incidence. This grants rather than derives actuality and experience. A history is not automatically a subject, a single center is not necessarily a whole subject, and this model does not justify the incidence stipulation. It does not show that every mathematically possible binary history is genuinely possible in reality. Incompatible records belong to different indexed occurrences, not to the same event in the same respect.

The coordinate n is only a declared internal order in each illustrative record. Its shared indexing is a mathematical convenience, not a derived local time or a fundamental external universal clock. The construction does not derive spacetime, physical dynamics, or subject persistence; nor does a set-theoretic union by itself establish the real whole's self-sufficiency.

## 2. When symmetry does determine a fair record law

Take a normalized, countably additive measure `μ` on the **Borel** sets of C. It represents a proposed weighting of centers or records; its normative or physical relevance is an additional premise, not something created by the formal space. Let `C_{a,w}` denote centers of type `a∈{A,B}` whose record starts with a word `w` of length n. Set `α=μ({A}×H)`.

For each finite set of positions S, consider the active transformation `T_S` that flips those bits in every history, without changing the type. Assume **as a substantive symmetry principle**

```text
μ(T_S E) = μ(E) for every Borel E and finite S.   (invariance)
```

For fixed type and n, finite flips map each length-n cylinder to any other. Invariance gives equal weight to all `2^n` such cylinders; they partition the type sector. Therefore

```text
μ(C_{A,w}) = α / 2^n,
μ(C_{B,w}) = (1−α) / 2^n.                         (1)
```

The cylinder sets generate the Borel σ-algebra; standard extension/uniqueness results therefore give the **only** measure for each α satisfying the stated condition. Conditional on a type with positive weight, all finite coordinates are fair and independent: independence is a consequence of the full finite-flip invariance here, not an extra premise. This is an application of standard product-measure theory; see the [MIT construction](https://ocw.mit.edu/courses/6-436j-fundamentals-of-probability-fall-2018/03cb805c752a7e89e52878e8e6270e34_MIT6_436JF18_lec02.pdf). This is a probability model over already stipulated centers, not a random production of realities.

**What it does not determine:** every `α∈[0,1]` is consistent with (1). For example `α=1/4` and `α=3/4` both respect all the stated bit flips. If one separately requires both type sectors to have positive weight, every `0<α<1` remains possible. Actuality and positive probability are different: excluding α=0 or 1 is an added measure assumption, not a consequence of saying both types are actual.

If there is a further active symmetry `S(A,h)=(B,h)` and the measure is invariant under it, `α=1−α`, hence `α=1/2`. But **do not presume this exchange** when A and B differ in intrinsically relevant experiential or physical structure. A graphical relabeling, a mathematical permutation of symbols, or a change of material description does not by itself establish that their associated subject occurrences are physically or phenomenally interchangeable. Whether a type swap is an actual symmetry and whether rational or physical weighting must respect it are separate obligations.

Also distinguish active invariance from passive redescription: changing coordinate labels while transporting both events and measures is a consistency requirement for any law. It does **not** force `μ(T E)=μ(E)` for an active physical transformation that swaps outcomes while the original meaning is held fixed. If the probability law is itself taken as part of the whole's structure, a transformation that changes it is not a symmetry of that *enriched* structure; identifying the correct enriched structure is exactly the unresolved task.

## 3. What plenitude allows without the extra symmetry

For any `0<p<1`, the standard Bernoulli product measure on H gives a length-n word with k ones the weight

```text
μ_p([w]) = p^k (1−p)^(n−k).
```

Every finite cylinder has positive weight for both `p=1/4` and `p=3/4`, and all infinite histories remain elements of the same stipulated H. The two measures disagree, however, on their relative weights. For example the four-bit all-zero cylinder has weight `81/256` at `p=1/4` and `1/256` at `p=3/4`. These measures are not invariant under arbitrary bit flips. Mere exchangeability under permutations of coordinate positions is weaker: every iid Bernoulli-p law has that property, whatever p. Interchanging positions is also not automatically a real symmetry of an experienced temporal process.

By the standard strong law, the set of histories whose limiting fraction of ones is p has `μ_p`-measure 1 and `μ_q`-measure 0 for `q≠p`. The two measures are therefore **mutually singular**, despite having full topological support: every nonempty finite cylinder has positive measure under both. This standard fact is discussed in [work on Bernoulli-like measures](https://www.sciencedirect.com/science/article/pii/S0022247X18301148). Mutual singularity is a property of the assigned measures, not evidence that the excluded histories are unreal or impossible. Each individual infinite record has measure zero for both p values while, by stipulation, each is actual in the toy. Measure-zero does not mean nonexistence.

The finite [verifier](verification/plenitude_symmetry_measure_gate.py) computes total-variation distances between the `p=3/4` and `p=1/4` laws at 1, 4, 8 and 20 coordinates: `1/2`, `11/16`, `1759/2048`, and `33747909673/34359738368`. These checks are finite; the infinite singularity is a theorem under the stated product assumptions, not something verified by 20 coordinates.

## 4. A quantum check: which swap is actually a symmetry?

The following uses ordinary quantum mechanics as a comparison, **not** a derivation of it from the experiential whole or an assumption that literal simulations occur. Consider a normalized two-qubit Schmidt state

```text
|Ψ⟩ = (√3/2)|0_A0_B⟩ + (1/2)|1_A1_B⟩.
```

The reduced density operator on A has diagonal `(3/4,1/4)` in the displayed basis. An active local swap of A's 0 and 1 changes that diagonal to `(1/4,3/4)`. Its trace distance from the original reduced state is `1/2`. No unitary acting only on B can undo that change to A's reduced state, because a B-only unitary leaves A's reduced density operator unchanged. Thus this particular unequal-weight local swap is not an environment-compensable symmetry of the given state. By contrast, for `( |00⟩+|11⟩ )/√2`, an A swap followed by a B swap restores the state.

The standard Born rule, if supplied for this example, gives the unequal outcome probabilities `3/4` and `1/4`. Requiring invariance of their probabilities under an active outcome swap **while holding this unequal state fixed** would instead force equality. Therefore the assumption in §2 cannot simply be imposed on every quantum measurement: whether the transformation preserves the **full state and physically relevant structure** matters. A passive change of labels swaps both the state description and the outcome descriptions and does not create a contradiction.

This does not claim that all symmetry-based Born-rule programs make that mistake. Zurek's envariance, Deutsch–Wallace decision theory, and self-location approaches use additional physical and/or rationality premises; see [Sebens and Carroll](https://www.journals.uchicago.edu/doi/10.1093/bjps/axw004), [Wallace's analysis](https://arxiv.org/html/quant-ph/0303050), and the [SEP review](https://plato.stanford.edu/entries/qm-manyworlds/). Their conclusions, premises and criticisms are not replaced by this toy. We have neither justified those premises for this whole-account nor derived Hilbert space, the amplitudes, decoherence, or a self-location rule.

## 5. Fine-graining needs a physical and subject rule

If four **stipulated equally weighted fine centers** map to two outcomes, with three centers assigned outcome 0 and one assigned outcome 1, additivity gives weights `3/4` and `1/4`. If two equally weighted fine centers map one each, the weights are `1/2,1/2`. Both constructions include both coarse outcomes, yet their raw counts differ. The finite checker also records a `9:1` example.

This is not an objection to every fine-graining argument. The two toy refinements are not automatically the same complete physical state; in genuine quantum arguments fine-grained amplitudes, environmental symmetries, availability of transformations and invariance principles do work that arbitrary branch-counting omits. The issue for this project is to specify **which** fine structures correspond to physically distinct subject occurrences and which differences are merely environmental, representational or irrelevant. If adding a hidden record creates a new subject, counting may change; if it is merely an alternative description of the same subject, it should not silently double the subject. Neither alternative is fixed by plenitude alone. A refined model must defend that distinction before a counting rule can be used as an explanation.

## 6. Consequences for the research programme

1. **Positive conditional result:** exact finite-outcome symmetry plus a justified invariant center measure determines equal cylinder weights in the stated domain. It gives an explicit route from relational structure to a probability rule when its assumptions really apply.
2. **Residual plurality gap:** symmetry within each type does not set relative weight across inequivalent types. A principle for constitution, token counting and measure remains necessary even if every type is actual.
3. **Physics gap:** the relevant symmetry must preserve the full physical and experiential state; a generic outcome flip need not. Recovering quantum amplitudes and their empirical weights is an independent task, not a consequence of the existence of all outcomes.
4. **Foundation gap:** the example stipulates both the formal structure and experiential incidence. It does not explain why the real whole is self-sufficient or intrinsically experiential, or establish `possible ⇔ actual`; the user's point that a self-sufficient whole needs no external cause is respected. The question is why that constitution is true, not what caused a self-sufficient whole.
5. **Empirical gap:** an actual subject-location measure must connect to finite observations, observer identity and calibrated reports. A predictive or quantum formal result alone does not establish that the whole is one subject, that strings are subjects, or that a given physical mismatch is unpleasant.

This extends, rather than replaces, [the earlier actual-history and measure analysis](RELATIONAL_PLENITUDE_HISTORY_AND_MEASURE.md): full actual support, measure, invariance, subject incidence and physics are distinct requirements. The substantive framework battery remains open.

## Reproduction

Run `python verification/plenitude_symmetry_measure_gate.py`; the [aggregate receipt](verification/plenitude_symmetry_measure_gate.json) records **349,520 finite bit-flip checks**, two unequal type-weight choices, finite-law distances, fine-count examples and the two-qubit reduced-state comparison. The infinite uniqueness and singularity results follow from the cited measure theory and stated premises, not finite enumeration. The verifier does not test the metaphysical theses or establish real subjects.
