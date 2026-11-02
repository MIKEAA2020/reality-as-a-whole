# Constructive step 13: consistent finite regions and a quasi-local completion

## Main result

The finite integration now extends to a mathematically well-defined infinite-lattice observable algebra with reversible finite-propagation dynamics.

The crucial bridge is **buffered consistency**: for a fixed local observable and finite number of periods, finite open-boundary models give exactly the same answer once their windows include the full circuit cone. Arbitrary unbuffered finite-window dynamics do not automatically agree.

From this locality result and norm-preserving finite-dimensional embeddings, the algebraic dynamics extends uniquely to the quasi-local C*-completion. The completion argument is given below; finite tests check its explicit symbolic implementation and examples rather than proving the entire infinite theorem by enumeration.

**32 new tests pass; all 340 tests across thirteen research folders pass.**

This is a mathematical spin-lattice model. It is not a demonstration of infinitely many actual physical qubits, a continuum QFT, a relativistic spacetime, or phenomenal constitution.

## 1. Specify the infinite model instead of declaring a limit

Put a qubit at every integer lattice site. For each finite interval I define:

\[
\mathcal A_I=\bigotimes_{i\in I}M_2(\mathbb C).
\]

For I contained in J, embed A by tensoring with identities on the added sites. These embeddings preserve multiplication, adjoints, identity, and operator norm.

The site identifiers remain fixed under the embeddings. Enlarging a model does not create new descriptions of an old site and count them as extra occurrences.

The algebraic local algebra is the directed union:

\[
\mathcal A_{\mathrm{loc}}=\bigcup_I\mathcal A_I.
\]

Every member has finite support. We have not yet assumed that every conceivable infinite-support expression is an element of this algebra or its completion.

## 2. Give the dynamics an explicit local rule

Use two disjoint CNOT layers per period:

- first, gates from 2k to 2k+1;
- second, gates from 2k+1 to 2k+2.

This order describes forward state evolution. Observable pullback applies the conjugations in reverse layer order.

Although a layer contains infinitely many gates, a finite-support observable intersects only finitely many pairs. Its translated observable can therefore be computed using finitely many gate conjugations.

No infinite product of unitary operators on a preselected global Hilbert space is needed for this definition.

The schedule, lattice, local algebra, and gate rule remain supplied structure. Their mathematical coherence is not an explanation of why this would be the actual world's law.

## 3. Use an exact finite-support representation

Represent a Pauli monomial as:

\[
P=i^kX^xZ^z,
\]

where x and z are finite sets of lattice sites and k is taken modulo four.

Multiplication is:

\[
(i^kX^xZ^z)(i^\ell X^{x'}Z^{z'})
=i^{k+\ell+2|z\cap x'|}
X^{x\triangle x'}Z^{z\triangle z'}.
\]

This symbolic representation preserves the phases that would be lost by tracking only support sets. In particular, Y=iXZ and signed contextual products remain correctly represented.

The implementation uses integer phases and finite sets, not floating-point approximations or infinite matrices. For the previous three-site open window, all 64 symbolic Pauli translations are checked against the earlier dense-matrix implementation.

## 4. Expose the boundary problem

Let α be the infinite-lattice one-period pullback. For Z at site 0:

\[
\alpha(Z_0)=Z_{-2}Z_{-1}Z_0.
\]

But the open-boundary window {0,1} omits the gates crossing its left boundary and gives Z₀ instead.

Thus the diagrams

\[
\mathcal A_I\xrightarrow{\alpha_I}\mathcal A_I
\]

cannot simply be asserted to commute with every inclusion I⊂J. Boundary-truncated dynamics really can differ.

This is not fixed by declaring both models to be presentations of one whole. One must show the actual stabilization relation.

## 5. Prove buffered consistency

For a finite region R and integer number of periods n, construct a circuit cone J_n(R) by following the gate pairs backward for positive n and through the inverse schedule for negative n.

If a finite window K contains this full cone, the finite-window translation agrees with the infinite rule on every observable supported in R:

\[
\alpha_K^n(A)=\alpha^n(A),
\qquad A\in\mathcal A_R.
\]

### Why

At each backward layer, gates disjoint from the current support commute with the observable and cancel from its conjugation. Only intersecting gates matter. Including both sites of each such gate adds exactly the required finite neighborhood. Repeating for finitely many layers yields the stated finite cone.

All omitted gates then act outside that cone and cannot change the result. The argument applies to Pauli monomials and hence by linearity to the full finite algebra.

The code checks buffered equality in both time directions, over representative local bases and several periods. It also checks agreement when buffered windows are enlarged further.

## 6. State the exact temporal qualification

The buffer depends on the observable and the time horizon. A sufficient radius bound in this architecture is:

\[
J_n(R)\subseteq
\{j:\operatorname{dist}(j,R)\le2|n|\}.
\]

A finite window sufficient for ten periods need not reproduce every later period. No interchange of an infinite-time limit and an infinite-volume limit is being assumed.

The construction supplies a consistent result for every fixed finite time and local observable. That is enough to define the discrete-time algebraic dynamics; it is not a claim that one finite simulation reproduces the entire infinite model forever.

## 7. Obtain an algebraic *-automorphism

Each finite gate conjugation preserves products, adjoints, identity, and scalar multiplication. Buffered consistency makes the combined map independent of the auxiliary window used to calculate it.

Thus α is a well-defined *-homomorphism on the local algebra.

Reverse the layer order to obtain its inverse. Both compositions act as identity on every finite-support observable. Therefore α is a *-automorphism of the local algebra.

Integer powers satisfy:

\[
\alpha^{n+m}=\alpha^n\circ\alpha^m.
\]

This is reversible discrete dynamics. It is not yet a continuous one-parameter group or a derived Hamiltonian evolution.

## 8. Prove norm preservation and extend to the completion

Choose a buffered finite window K for A. Within that window the translation is ordinary finite-dimensional unitary conjugation. Hence:

\[
\|\alpha(A)\|=\|A\|.
\]

The identity embeddings are also isometric, so the norm does not depend on which sufficiently large finite matrix algebra represents A.

Define the quasi-local algebra by norm completion:

\[
\mathcal A_{\mathrm{ql}}
=\overline{\mathcal A_{\mathrm{loc}}}^{\|\cdot\|}.
\]

For a Cauchy sequence A_m of local observables, α(A_m) is Cauchy because:

\[
\|\alpha(A_m)-\alpha(A_k)\|=\|A_m-A_k\|.
\]

Set α(lim A_m)=lim α(A_m). The same equality makes the definition independent of approximating sequence. Products and adjoints pass to the limit by their norm continuity. The inverse extends by the same argument.

Therefore α extends uniquely to a *-automorphism of the quasi-local C*-algebra.

This is the infinite construction actually earned. The proof uses standard finite-range circuit and C*-completion reasoning; it is not claimed as a new general theorem or as an empirical discovery.

## 9. Obtain controlled locality for quasi-local observables

Strictly local observables have finite cones. A general quasi-local observable can instead have arbitrarily accurate local approximations.

If ||A−A_R||≤δ and a local B lies outside J_n(R), then:

\[
[\alpha^n(A_R),B]=0,
\]

and therefore:

\[
\|[\alpha^n(A),B]\|
\le2\delta\|B\|.
\]

The same approximation bounds expectation errors by δ for normalized states.

This is a justified approximation statement, not an arbitrary interaction cutoff. It does not turn δ into a phenomenal unity threshold or provide a measured δ for a brain.

## 10. Construct compatible states without an infinite density matrix

Choose a product state by assigning one-site states consistently. The implementation supports Z-basis states |0>, |1> and X-basis states |+>, |−>, with finite overrides of a default assignment.

Each finite restriction is a positive normalized density operator, and restrictions agree under identity embeddings. This defines a positive normalized state functional ω on the local algebra. Such a state is bounded with norm one and extends continuously to the completion.

Evolve it through:

\[
\omega_n(A)=\omega(\alpha^n(A)).
\]

The evolved restrictions remain compatible. A single global trace-class density operator on a chosen infinite tensor-product Hilbert space is not required.

This is an important algebraic integration gain: one can specify states and dynamics before choosing a Hilbert-space representation. It does not mean there is no further representation theory, or that representations correspond to conscious perspectives.

## 11. Identify the precise overlap with the previous model

There are two distinct relations to the earlier three-site construction:

1. Restrict the new rule to the **open-boundary window [0,2]**. Its two gates exactly reproduce the previous matrix dynamics. Every Pauli translation in that finite window is checked.
2. In the full lattice, prepare |+> at site 0 and |0> everywhere else. After one period, the reduced state on sites 0,1,2 is the same GHZ state produced previously. All 64 local Pauli expectations agree.

These statements must not be merged. The infinite rule contains gates crossing the three-site boundary and is not the previous closed finite unitary for every possible environmental state. The GHZ overlap uses the declared external |0> preparation.

The finite-window and state-dependent overlaps are explicit, not universalized beyond their assumptions.

## 12. Preserve contextual constraints at arbitrary locations and times

Embed the earlier Mermin–Peres square on any adjacent pair. Since α preserves products, identity, phases, and commutation, its parity contradiction survives every integer period.

The five +1 products and one −1 product remain unchanged under transport, even when the observables acquire larger support.

Thus the contextual description is compatible with the quasi-local dynamics. The transport is not merely a renaming of local sites: a single-site observable can become a three-site product, changing the physical support required to measure it.

The result continues to exclude the stated noncontextual deterministic valuation, not global quantum states or every possible hidden-variable account.

## 13. Do not infer dynamics from an invariant state alone

The all-|0> product state and all-|+> product state are invariant under this gate architecture. The automorphism itself is not identity.

Thus an unchanging family of state predictions can coexist with nontrivial counterfactual dynamics. Informative preparations and interventions matter.

This reinforces the earlier distinction between a law, an observed trajectory, and actual events. A chosen invariant state does not demonstrate absence of causal organization; a nontrivial automorphism does not establish a phenomenal episode.

## 14. The completion does not admit every formal infinite expression

Consider finite parity products:

\[
P_N=\prod_{j=-N}^{N}Z_j.
\]

They do not form a norm-Cauchy sequence:

\[
\|P_{N+1}-P_N\|=2.
\]

The upper bound follows from unitarity. For the lower bound, choose a product state with a single |1> at one newly added endpoint and |0> on the other relevant sites. Its expectations of the two products are +1 and −1.

Therefore their proposed infinite parity product is not obtained as a norm limit of this sequence in the quasi-local algebra. A representation-dependent weaker closure could raise different questions, but is not silently included here.

**Integration lesson:** even after constructing a common mathematical setting, one must specify its topology and admitted objects. “All infinite expressions” is not a legitimate substitute.

## 15. Record the actual symmetries

The two-layer schedule has a two-site unit cell. Translation by two sites commutes with α. Translation by one site generally does not: it changes which layer a bond belongs to.

The tests explicitly verify both claims.

No continuous spatial translation symmetry, Lorentz invariance, preferred physical light speed, or fundamental lattice ontology has been derived. The model has the symmetries of its supplied update rule, not those of every physics one might hope to recover.

## 16. Show why continuous time is not obtained by relabeling the clock

For A=Z₀:

\[
\alpha(A)=Z_{-2}Z_{-1}Z_0,
\qquad
\|\alpha(A)-A\|=2.
\]

A product-state witness supplies the lower bound; the sum-of-unitary-norms bound supplies the upper bound.

If the same fixed α is merely assigned a smaller duration Δt, this difference does not approach zero. The formal difference quotient has norm 2/Δt on that observable.

Hence this relabeling alone does not give a point-norm continuous limit on the fixed local observables or a finite generator there.

This does **not** rule out all continuum or effective limits. A scaling construction might change the family of gates, observables, states, spatial scale, or convergence topology. Those choices and their limits must be supplied and justified. They are additional mathematical work, not consequences of having an infinite lattice.

## 17. What the integration now contains

| Ingredient | Earned connection | Remaining limitation |
|---|---|---|
| Finite local algebras | Isometric directed embeddings | Chosen spin-lattice structure |
| Local dynamics | Buffer-independent maps and inverse | Discrete supplied schedule |
| Infinite observable algebra | Norm-completed quasi-local C*-algebra | Not a continuum field theory |
| Causal propagation | Exact finite cones and controlled tails | Not Lorentzian spacetime |
| States | Consistent positive restrictions and evolution | Chosen preparations, not actual-world state derivation |
| Contexts | Preserved commutation and parity constraints | Not a phenomenal structure by definition |
| Earlier finite model | Exact open-window and qualified state overlaps | Not unrestricted equality across boundaries |

This is now more than a single small final-slice example. It is still not integration of every framework discussed. In particular, no causal-set manifold reconstruction, twistor correspondence, Langlands bridge, or constitutive identity with experience has been established.

## 18. Actuality and the standing explanatory objective

An infinite mathematical model is not evidence that infinitely many physical realizations occurred. Its lattice sites, local algebra embeddings, measurement contexts, and state restrictions are not observer counts.

The construction does not explain why its variables, gates, algebra, state, or laws obtain in concrete reality. Norm completion does not instantiate the completed algebra physically. No subject boundary or phenomenal sufficiency follows from the automorphism.

The full-intelligibility requirement is therefore unchanged. What has been earned is one well-defined infinite algebraic dynamics bridge, not a self-explanatory whole.

## 19. The next discriminating task

The next useful step is a **scaling/continuum audit** with explicit criteria:

1. identify the gate family and physical scaling parameters;
2. specify which observables and states are compared across scales;
3. choose the convergence topology and error criterion;
4. establish the limiting dynamics and causal behavior;
5. state whether the construction extends this exact CNOT rule or introduces a distinct model;
6. identify which extra assumptions are required for continuum field or geometric interpretation.

A successful example would contribute a real discrete/continuous bridge. It must not be advertised as the causal-set/twistor integration merely because a continuum equation appears.

The parallel phenomenal task remains independent: explain independently warranted whole-episode contrasts rather than equating quantum nonfactorization, causal propagation, or contextuality with unity.

## Reproducibility

- `model.py`: exact finite-support Pauli algebra, infinite-layer local rule, inverse, cones, finite windows, embeddings, product states, and contextual products.
- `test_model.py`: 32 tests, including comparison with the earlier dense three-site implementation.
- `enumeration.json`: generated boundary, support, state, and symmetry summaries.
- `results.log`: actual execution output.

```bash
# This round
cd research/quasilocal_limit
python -m unittest -v test_model.py

# All research folders, from repository root
python research/run_checks.py
```

The model uses symbolic phases and finite sets. The completion, positivity-extension, and norm arguments are stated proofs, not inferred from the number of tested examples. The checks verify their concrete finite-support implementation and the selected witnesses.

**Observed verification:** 32 new tests pass; all 340 tests across thirteen research folders pass. No new empirical data were collected.

### Consolidated verdict

A buffered family of finite local quantum models supports a genuine quasi-local algebra and reversible finite-propagation dynamics. Arbitrary boundary truncations and arbitrary infinite expressions do not automatically participate in that construction. This advances the algebraic integration while making the next unpaid bridge precise: a justified scaling limit, not merely a smaller clock label or the assertion that discreteness has become spacetime.

## Subsequent scaling audit

[Constructive step 14](../continuum_scaling/REPORT.md) supplies a distinct scaled quantum-walk family with a bounded-momentum Dirac limit and a quantitative finite-time bound. It explicitly does not identify that family with the CNOT model, and demonstrates the failure of uniform convergence near the momentum-zone boundary.
