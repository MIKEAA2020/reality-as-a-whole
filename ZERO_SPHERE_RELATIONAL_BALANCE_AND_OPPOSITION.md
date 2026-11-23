# Zero, internal relations and the problem of opposites

**Continuation:** [the binary-state and incidence analysis](ZERO_INTERNAL_SPHERE_BINARY_STRUCTURE_AND_INCIDENCE.md) connects a stipulated complex two-level state space to the same projective sphere, distinguishes zero operator trace from actual state-weighted balance, and derives an exact weighted-network criterion. The complex state space and physical–experiential identity remain unproved inputs.

## Main result

There is a way to combine the point–sphere proposal, relativistic frame independence and a nontrivial zero total, **provided additional relational structure is supplied**. The construction also reveals a constraint on a tempting simpler idea:

> On a relativistic sphere of directions there is no observer-independent rule that assigns each direction a distinct, intrinsic opposite using only that sphere's Lorentz symmetry.

Therefore one cannot identify positive and negative experience with opposite points on that bare sphere and claim the pairing follows from relativity. An observer-dependent pairing, or a pairing defined by further physical structure that transforms with the state, remains possible.

The constructive alternative tested here is relational: attach signed contributions to the two ends of an internal relation, rather than to antipodal points. A finite network of such relations can have nonzero local contributions and an exact zero total, with amplitudes built from Lorentz-invariant cross-ratios. This is **a candidate accounting structure**, not an established energy or experiential ontology.

## 1. Why the spherical “opposite” needs more than the sphere

In an observer's round sky, one can say that `n` and `−n` are antipodal. But a boost changes the angular relations between directions, and antipodality in one observer's sky is not generally antipodality in another's.

The issue is sharper than a single counterexample. Assume the internal sphere is the `CP¹` sphere of the [previous construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md), with the proper Lorentz group acting by Möbius transformations. Suppose a map `F` assigns each direction a partner and is invariant in the required equivariant sense:

```text
F(g·z) = g·F(z)   for every direction z and Möbius transformation g.
```

Every translation `g_b(z)=z+b` fixes `∞`. Equivariance therefore says that `F(∞)` must be fixed by **every** translation. The only such point is `∞`, so `F(∞)=∞`. The Möbius group acts transitively on the sphere. For any direction `z`, choose `g` with `g(∞)=z`. Then

```text
F(z) = F(g·∞) = g·F(∞) = g·∞ = z.
```

Thus **the only globally defined single-valued map commuting with every proper Lorentz transformation is the identity**. In particular, there is no nontrivial Lorentz-equivariant antipodal partner map determined by the celestial sphere alone. This conclusion does not require continuity of `F`.

This is not a no-go theorem for the user's zero thesis. It rules out one extra claim: that an observer-independent, distinct opposite for each direction can be extracted from the bare Lorentz action. A chosen timelike observer, material state, relation network, or other covariantly transforming structure may define a pairing, but that further structure must be accounted for.

For a direct example, in one stereographic chart the usual round-sphere antipode is `A(z)=−1/conj(z)`, with `A(0)=∞`. For the Möbius transformation `g(z)=z+1`, `A(g(0))=−1`, but `g(A(0))=∞`. Hence `A(g(0))≠g(A(0))`. The underlying Lorentz–Möbius correspondence is reviewed by [Oblak](https://arxiv.org/abs/1508.00920).

## 2. Replace opposites of points with two sides of a relation

Take four *distinguished* directions on the projective sphere, with labels `1,2,3,4`, and suppose their physical or constitutive organization includes the oriented relations

```text
1 → 2 → 3 → 4 → 1.
```

This is an abstract network, not a claim that causal time literally runs around a closed loop. Its vertices and relations are supplied as additional data; the sphere alone does not select them.

For each relation `e=(i→j)`, assign an amount `q_e`. Its incidence at the tail is `−q_e` and at the head is `+q_e`. Equivalently, with `B` the directed incidence matrix,

```text
s_i = Σ_e B_ie q_e.
```

For the cycle in the stated order,

```text
        e1 e2 e3 e4
B =  [ −1  0  0 +1 ]
     [ +1 −1  0  0 ]
     [  0 +1 −1  0 ]
     [  0  0 +1 −1 ].
```

Since every column contains one `−1` and one `+1`,

```text
Σ_i s_i = Σ_i Σ_e B_ie q_e = 0
```

for **any** `q_e`. This is exact. It does not require a special observer or antipodal directions. It also shows exactly why this particular mathematical total vanishes: every internal relation contributes twice with opposite incidence signs. Such a total is an accounting identity, not yet an independently established objective energy or experiential sum.

## 3. A nonzero zero-balanced example

Four distinct, physically distinguished projective directions have the Lorentz-invariant cross-ratio

```text
X = (z₁−z₂)(z₃−z₄) / [(z₁−z₃)(z₂−z₄)].
```

Take `z=(0,1,2,3)`. Then `X=1/4`. With the selected cycle and

```text
q = (X, 2X, 3X, 4X) = (1/4, 1/2, 3/4, 1),
s = Bq = (3/4, −1/4, −1/4, −1/4),
Σ s_i = 0.
```

The local net signed values are nonzero; their sum is exactly zero. A common proper Lorentz transformation of all four sphere directions changes their coordinates but preserves `X`, and therefore the same assigned `q` and `s`, **assuming the labelled network and chosen amplitude rule are retained**. Neither the preferred labels, the cycle, the coefficients `(1,2,3,4)`, nor the identification of `s_i` with a physical quantity follows from the cross-ratio.

This example shows how zero need not mean an empty internal ledger. It does **not** show that the entries exist physically, that the entries are energy or valence, or that their signs are pleasure and suffering. Those are distinct constitutive questions.

### The self-contained cycle case

If all four relation amounts equal `X`, then

```text
q = (X,X,X,X),   Bq=0,
```

while every edge still has nonzero contributions `−X` and `+X` at its ends. The net at **every vertex is zero**, so the nonzero values in this case belong to individual relation incidences, not to the vertex nets. With `X=1/4`, there are four `+1/4` and four `−1/4` incidences. They are not eight established experiences or subjects.

For a connected finite graph, `dim ker B = edges − vertices + 1`: nonzero divergence-free flows exist precisely when the graph has an underlying cycle. A tree has only the zero flow in `ker B`. This is a graph-theoretic result conditional on the network, not a proof that reality contains a physical closed causal loop. A cycle here can be an abstract pattern of mutual relations or a spatial network; a causally ordered spacetime does not thereby acquire closed timelike curves.

## 4. Why this does not yet prove experiential cancellation

The mathematical two-sidedness of a relation is an important potential clue, but it is **not already felt valence**:

* The same incidence bookkeeping occurs in a wholly non-conscious network. Neither a vertex nor an edge end is automatically a subject.
* Reversing an edge's chosen orientation **and** the sign of its flow gives exactly the same physical incidences. Thus orientation is partly a representational convention, not automatically an intrinsic distinction between pleasure and pain.
* The zero sum is over the particular incidence or vertex accounting measure. It does not imply zero for a different measure of actual subject incidence. For the nonzero-vertex example, weighting vertex 1 by `2` and the others by `1` yields `3/4`, not zero. Equal weights and the relevance of vertex values to experience would need physical justification.
* In the equal-flow example, the four positive and four negative incidence entries are paired by construction. That does not imply equal counts of positive and negative experiences. No intensity, duration, subject unity, or self-location weighting has been derived.
* Mathematical cancellation does not make an individual's suffering unreal. If signed experience is a whole-level additive quantity, real locally negative contributions would remain real even if the correctly defined whole total were zero. Whether valence has that additive physical identity is still to be established.

The two examples deliberately distinguish global cancellation from local conservation: the unequal-flow example has nonzero `s_i` while the equal-flow example has `s_i=0` for each vertex. Neither supplies a dynamical law. If interpreted as transport, nonzero divergence would require a compatible source, storage, or continuity equation; it cannot simply be called conserved local energy.

## 5. What follows for zero's own constitution

The proposed shift is from **two opposite things imposed on zero** to **one internally differentiated relation whose two incidences are signed oppositely**. This makes “nonzero locally, zero as a whole” intelligible within a specific, frame-independent relational representation. The sphere can supply invariant relational information (`X`), while the network supplies internal incidence. The point projection still represents the whole as externally unextended in the proposed picture.

But two tests show that the construction is not a derivation of reality from zero:

1. Holding the graph fixed, `q=0`, `q=(X,X,X,X)` and `q=(X,2X,3X,4X)` all satisfy the same whole zero. The zero identity does not determine that differentiation exists or which differentiated state is actual.
2. The same abstract incidence law permits many graph structures and many amplitude rules. Lorentz invariance constrains possible descriptions; it does not choose a graph, determine the project's `CP¹` structure, provide dimensional physical energy, establish dynamics, or produce a subject.

The next substantive task is to find a constitutive principle that **does not merely impose** the network and its weights but explains their necessity and physical–experiential identity. An adequate candidate must show why its accounting measure coincides with actual subject incidence and what determines locally felt positive and negative valence, while retaining relativistic covariance and real local suffering. It must also establish any whole-level energy or experiential zero rather than equating it with this graph identity by definition. There is no claim here that the required principle is impossible, or that it will automatically follow.

## Verification

`python -m unittest verification.zero_relational_sphere_cycle_test -v` checks exact cross-ratio invariance for an explicit Möbius transformation, the balanced and nonzero-local examples, cycle/tree ranks, weighted-count failure, antipode non-equivariance for one transformation, and the edge-orientation convention. The general no-partner argument is proved in section 1; finite tests cannot prove it. The code does not verify physical or experiential identity.
