# The internal sphere, binary distinction, and actual incidence

**Continuation:** [the closed-plasma incidence gate](ZERO_SPHERE_CLOSED_PLASMA_INCIDENCE_GATE.md) realizes an equatorial sphere orbit in a self-consistent two-fluid–Maxwell model, and exhibits positive state-derived responses with zero and nonzero weighted exchange. The physical–experiential identity, actual subjects and a global zero remain open.

## Constructive result

The point–sphere proposal suggests a more direct physical question than simply finding a sphere already present in relativity: **what minimal kind of internal distinction naturally has a sphere as its space of states?**

A complex two-level quantum system does. Its normalized pure states, with overall complex amplitude treated as irrelevant, form `CP¹`, the same projective sphere used in the [previous Lorentz-cone construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md). Thus one specified two-component structure can connect:

```text
binary quantum alternatives → projective sphere of pure states → null directions of a Lorentz-signature form.
```

No literal spatial sphere or external time is required for this mathematical construction. But the arrows are conditional: complex amplitudes, the quantum interpretation and the relevant normalization are additional structure. Zero itself has not been shown to require them. Nor does a two-level quantum system by itself give an experiencing subject.

The construction also gives a decisive test of any proposed experiential zero: **a signed operator can have zero trace while its actual state-weighted value is nonzero**. The proper incidence weights are essential, not decorative. This matters directly to the user's proposal that local suffering remain real while a suitable whole-level total may be zero.

## 1. Deriving the sphere from a two-level complex state space

Assume a complex two-dimensional vector space with a positive Hermitian inner product. Write a nonzero state vector as

```text
ψ = (α, β),     α,β ∈ C.
```

Physical rays identify vectors differing by a nonzero complex factor: `[ψ]=[cψ]`, `c≠0`. Equivalently one may normalize `|α|²+|β|²=1` and identify the remaining overall phase. The set of rays is `CP¹`, homeomorphic to `S²`. This does not mean that the possible states occupy a physical ball or that the universe has expanded from a point. Standard derivations of qubit density matrices and the Bloch sphere are given in these [Durham quantum information notes](https://www.maths.dur.ac.uk/users/kasper.peeters/qcomp/2023/qubit.html).

Using the Pauli matrices `σ=(σx,σy,σz)`, a normalized pure-state projector takes the form

```text
ρ = |ψ⟩⟨ψ| = (I + n·σ)/2,       |n|=1.
```

The three components of `n` give a unit sphere. The important distinction is between **two distinguishable alternatives** and **two exhaustive pure states**: the complex relative amplitude and phase give a continuum of possible pure states even though a specified two-outcome measurement has two results.

As a countercheck, a classical two-alternative system has two pure states and an interval of mixtures, not a sphere of pure states. A two-dimensional real quantum state space gives `RP¹ ≅ S¹`; a two-dimensional complex one gives `CP¹ ≅ S²`; a quaternionic one gives `HP¹ ≅ S⁴`. See [Baez on projective lines and quantum state spaces](https://math.ucr.edu/home/baez/week106.html). Therefore **binary distinction alone does not entail the user's `S²`**. Within this particular class of projective two-level constructions, the two-sphere singles out the complex case; the choice of this class and its physical interpretation remain to be justified.

## 2. The same sphere leads to a causal cone

For a spinor `ψ`, the unnormalized Hermitian matrix `K=ψψ†` has `det K=0`. The matrix is positive semidefinite and nonzero; scaling `ψ` changes only its positive size. Its projective ray is thus a future null direction in the real four-dimensional Hermitian space, whose determinant is the Lorentzian quadratic form. This is the earlier sphere–cone construction, now seen as arising from the same complex two-component structure that also describes qubit rays.

This is a genuine structural link, not a derivation of observed physics: a qubit Bloch sphere and a local celestial sphere have an isomorphic projective geometry under the stated construction. It does **not** identify actual quantum states with actual spacetime events, generate an interacting field theory, or prove that the universe is a qubit. The constructed four real components of a Hermitian matrix are not automatically physical space and time.

There is a crucial qualification about reference frames. Qubit orthogonality and the round Bloch metric depend on a positive Hermitian inner product `h`. General `SL(2,C)` transformations need not preserve a fixed `h`; they act on the projective sphere as Lorentz/Möbius transformations, not as ordinary unitary gates of one fixed qubit Hilbert space. Treating the same nonunitary transformation as a physical filter while holding `h` fixed can change outcome probabilities; it is **not** merely a passive change of description.

A covariant passive change of spinor basis is consistent if all relevant structures transform together:

```text
ψ' = Aψ,                 h' = (A⁻¹)† h A⁻¹.
```

Then `ψ'†h'φ' = ψ†hφ`; state operators and observables transform by similarity, preserving their expectation. This does not select a preferred global frame, but it does require an inner product or equivalent physical structure for probabilities. The constitutive source and physical meaning of that structure have not been derived from zero.

Explicitly, with `h=I`, the vectors `(1,1)` and `(1,−1)` are orthogonal. Under `A=diag(2,1/2)`, their transformed vectors have squared normalized overlap `225/289` if one wrongly holds `h=I` fixed; with the transformed `h'=diag(1/4,4)`, their inner product is again zero. This example separates observer-covariant description from a physical state change.

## 3. A zero trace is not an experiential zero

For a pure state, let

```text
Δ = ρ − I/2 = (n·σ)/2.
```

`Δ` is nonzero, yet `tr Δ=0`; its eigenvalues are `+1/2` and `−1/2`. This realizes a **nonzero, internally differentiated traceless operator**, a useful representation of a zero sum of spectral values. It does not say that `ρ` itself is zero: `tr ρ=1`, and `I/2` is a reference density matrix, not literal nonexistence or the whole's energy.

More importantly, the unweighted sum of eigenvalues and the value actually weighted by a state are different:

```text
tr A                 = sum of eigenvalues of A,
⟨A⟩ρ = tr(ρ A)       = state-weighted expectation.
```

Take `A=σz=diag(1,−1)` and `ρ=diag(1,0)`. Then

```text
tr A = 0,             tr(ρ A) = 1.
```

The negative eigenvalue exists in the spectrum, but in this state its outcome probability is zero. Hence the mathematical availability of positive and negative values does not establish actual balanced incidences. With `ρ=I/2`, the same operator does have expectation zero, but this fact alone neither establishes a conscious subject nor identifies the two measurement outcomes with pleasure and suffering.

Conversely, actual weighted balance does not require equal outcome frequencies or zero unweighted trace. For the assumed observable and state

```text
A = diag(3,−1),       ρ = diag(1/4,3/4),
tr(ρ A) = (1/4)·3 + (3/4)·(−1) = 0,
tr A = 2.
```

The negative outcome has probability `3/4` in this measurement. These are quantum outcome probabilities in a stipulated model, **not** observed suffering frequencies or automatically probabilities of being a subject. The example demonstrates the logical distinction: equal magnitude, equal incidence and weighted zero are different conditions.

If one hypothesized that such outcomes correspond to real experiences, the negative experiences would not become unreal because their weighted sum with positives vanishes. That identification and the relevant probability/subject measure still need an independent constitutive account.

## 4. The exact incidence condition for the relational network

The [previous relational construction](ZERO_SPHERE_RELATIONAL_BALANCE_AND_OPPOSITION.md) assigned signed vertex values `s=Bq` on a graph, where `B` is the oriented incidence matrix. Its unweighted sum is always zero, because each edge has one positive and one negative end. Now suppose, as a *test hypothesis*, that vertices carry the relevant local values and nonnegative weights `w_i` represent how much each counts in the proposed whole total. Then

```text
Q_w = Σ_i w_i s_i
    = wᵀBq
    = Σ_(i→j) (w_j−w_i) q_(i→j).
```

For a given graph and a given `q`, `Q_w=0` exactly when the right-hand side vanishes. Nonuniform weights can satisfy this for a particular `q`; uniformity is not necessary in that case.

There is a stronger exact statement: **if the weighted total is to vanish for every possible assignment of real edge values `q`, it is necessary and sufficient that the weights agree across every edge**. To see necessity, set all edges to zero except one; then its coefficient `w_j−w_i` must vanish. Sufficiency follows term by term. On a connected graph this means all vertex weights are equal. On a disconnected graph they may differ between components.

For example, on the previous four-cycle, `q=(1,2,3,4)` gives `s=(3,−1,−1,−1)`. Uniform weights give `Q=0`, but `w=(2,1,1,1)` gives `Q=3`. The nonuniform weights `w=(1,1,2,0)` give `Q=0` for **this** `q`, while failing for other `q`. This distinction prevents treating a sufficient condition for universal balance as necessary for a specific universe.

This criterion is mathematically necessary and sufficient only **within this specified graph model and linear weighting rule**. It is not a universal theorem about consciousness or energy. The physical work is to establish whether actual subjects, their duration/intensity measure and their valence can be represented by such vertices and weights at all. No proof of that identification is supplied here.

## 5. What has and has not been obtained

The resulting proposal is a single connected chain of conditional structures, rather than a loose analogy:

1. Complex binary rays give the sphere of pure quantum-like states.
2. The same rays give a projective null cone in Hermitian matrix space.
3. Traceless operators and signed network incidences exhibit nonzero constituents with mathematically zero unweighted totals.
4. A state or incidence measure selects which constituents actually contribute, and determines whether the **weighted** total remains zero.

The first three steps are mathematical constructions. The fourth supplies a precise criterion for the graph and explicit quantum controls. None derives complex amplitudes from a zero whole, establishes actual dynamics, turns an observable into felt valence, or establishes a global experiential or energy quantity. The causal-cone identification also does not settle subject plurality, local unity or relational time.

The most direct next constitutive target is therefore **a physical–experiential identity that determines the incidence measure and the sign and magnitude of felt contributions from the same dynamics that produce the physical state**. If that identity makes the actual weighted total vanish, it would be a substantive realization of zero with real experience—not merely the trace of an operator or a balanced bookkeeping convention. It must be derived rather than simply built into the notation.

## Verification

`python -m unittest verification.sphere_qubit_experiential_zero_test -v` checks rational examples of pure Bloch states, traceless versus state-weighted values, unequal-frequency weighted balance, the boost/inner-product distinction and the finite graph-weighting controls. The all-edges graph criterion is proved above; the tests check examples and do not establish physical experience or the existence of a whole-level zero.
