# Constructive step 11: one finite process, four compatible presentations

## What has actually been built

The integration programme now has a concrete common construction rather than only an architecture diagram. A two-output quantum process is represented simultaneously through:

1. quantum states and channels;
2. a finite local net of observable algebras;
3. an operational causal-order diagram;
4. a presheaf of measurement-context characters and compatible probability distributions.

The connections are explicit and executable. They also expose two important non-identifications:

- a channel's observable translation need not preserve multiplication;
- a global quantum state need not supply a global deterministic valuation of observables.

**30 new tests pass. All 276 tests across the eleven research folders pass.**

This is a finite common mathematical model. It is not a full AQFT, a quantum-gravity construction, an integration of every named framework, or evidence that its simulated variables are conscious. No new physical or phenomenal measurements were collected.

## Step 1. Specify the resource, rather than hide it

Begin with one input qubit in state ρ and an ancillary qubit supplied in state |0><0|. Apply a controlled-NOT unitary and label the outputs B and C.

Equivalently, define the isometry

\[
V|0\rangle=|00\rangle,\qquad V|1\rangle=|11\rangle,
\qquad V^\dagger V=1.
\]

The output channel is

\[
\Phi(\rho)=V\rho V^\dagger.
\]

Its unitary dilation is explicitly checked:

\[
\Phi(\rho)=U_{\rm CNOT}(\rho\otimes|0\rangle\langle0|)U_{\rm CNOT}^\dagger.
\]

The extra output degree of freedom is therefore not silently created by a formula. Its ancilla and initial state are supplied physical-model inputs. Their existence and preparation are not explained ultimately by this construction.

## Step 2. Represent causal precedence without inventing a spacetime metric

Use three process-event labels:

\[
a\prec b,\qquad a\prec c,
\]

with b and c incomparable. Event a represents preparation/interaction; b and c represent operations on the separated outputs.

This is a finite strict partial order and an operational common-cause diagram. It is not a recovered continuum geometry, a demonstrated manifoldlike causal-set approximation, or a proof of relativistic dynamics. No temporal order between the two output operations is imposed by the diagram.

In particular, the causal-event poset and the output-region inclusion poset below are **different typed objects**. Giving both an order does not identify them.

## Step 3. Build the output observable net

On the final output slice define:

\[
\mathcal A(\varnothing)=\mathbb C1,
\]

\[
\mathcal A(B)=M_2(\mathbb C)\otimes1,
\qquad
\mathcal A(C)=1\otimes M_2(\mathbb C),
\]

\[
\mathcal A(BC)=M_4(\mathbb C).
\]

The Pauli basis dimensions are respectively 1, 4, 4, and 16.

The net obeys isotony: region inclusion gives algebra inclusion. The separate output algebras commute elementwise:

\[
(a\otimes1)(1\otimes b)=a\otimes b=(1\otimes b)(a\otimes1).
\]

These are genuine finite algebraic locality properties. They are not all the axioms and structures of a relativistic field theory.

We deliberately do not attach an independently tensor-factored copy of the input algebra to the same output slice. An input occurrence and its later outputs are connected by a channel, not assumed to be three independent simultaneous systems.

## Step 4. Prove agreement between state and observable descriptions

The observable pullback is:

\[
\Phi^*(a)=V^\dagger aV.
\]

For every input state and output observable in the mathematical model:

\[
\operatorname{Tr}(\Phi(\rho)a)
=\operatorname{Tr}(\rho\Phi^*(a)).
\]

This follows from trace cyclicity. Since V is an isometry, the channel is trace-preserving and the pullback is unital. The single-Kraus form supplies complete positivity; the tests check the specified finite instances rather than claiming to enumerate all positive matrices.

This is the first exact integration bridge: the state-side and observable-side calculations represent the same process and predictions.

## Step 5. Do not mistake every translation for an algebra isomorphism

The pullback is not multiplicative. Let X_B=X⊗1 and X_C=1⊗X. Then:

\[
\Phi^*(X_B)=0,\qquad\Phi^*(X_C)=0,
\qquad\Phi^*(X_BX_C)=X.
\]

Hence:

\[
\Phi^*(X_BX_C)\ne\Phi^*(X_B)\Phi^*(X_C).
\]

This is not an inconsistency. The bridge is a unital completely positive map, not a claimed *-homomorphism.

**Integration lesson:** assigning every connecting arrow the name “structure-preserving” is insufficient. One must state which structure is preserved and which is not.

The phase information that neither output alone retains can remain accessible jointly.

## Step 6. Distinguish basis copying from arbitrary quantum cloning

For input basis states, the process produces:

\[
|0\rangle\mapsto|00\rangle,
\qquad |1\rangle\mapsto|11\rangle.
\]

For input |+>, it produces a Bell state:

\[
|+\rangle\mapsto|\Phi^+\rangle
=(|00\rangle+|11\rangle)/\sqrt2,
\]

not |+>⊗|+>. Each output alone is maximally mixed, not the original |+> state.

Thus the construction does not broadcast arbitrary input states. This concrete failure illustrates why copying a selected classical basis is not arbitrary state duplication. It is not offered as a new general proof of no-broadcasting.

## Step 7. Show exactly what local descriptions omit

Prepare three joint states:

\[
\rho_+=|\Phi^+\rangle\langle\Phi^+|,
\qquad
\rho_-=|\Phi^-\rangle\langle\Phi^-|,
\]

and

\[
\rho_{\rm mix}
=\tfrac12|00\rangle\langle00|+\tfrac12|11\rangle\langle11|.
\]

All have the same reduced states:

\[
\rho_B=\rho_C=\tfrac12 1.
\]

But their XX expectations differ:

\[
\langle X_BX_C\rangle_{\rho_+}=1,
\quad
\langle X_BX_C\rangle_{\rho_-}=-1,
\quad
\langle X_BX_C\rangle_{\rho_{\rm mix}}=0.
\]

Their ZZ expectations are all 1.

So compatible complete single-output states do not uniquely recover the joint state. This is an actual quantum example of the distinction previously exposed by finite marginal constructions.

Commuting regional algebras do not imply uncorrelated regional states.

## Step 8. Recover the joint state from sufficient joint data

The 16 two-qubit Pauli products form an operator basis. Therefore:

\[
\rho=\tfrac14\sum_{P\in\{I,X,Y,Z\}^{\otimes2}}
\operatorname{Tr}(\rho P)P.
\]

The code reconstructs each selected joint state exactly from these expectation values.

This clarifies local tomography: product-observable correlations can determine the joint state even though the separate reduced states cannot. “Local measurements suffice” does not mean “discard all joint correlations.”

This is determination of the selected density operator. It is not determination of a phenomenal profile or of actual occurrence multiplicity.

## Step 9. Build a finite context category

Take the 15 nonidentity positive two-qubit Pauli observables. The selected contexts are:

- the scalar context;
- 15 single-observable contexts;
- 15 maximal commuting Pauli contexts, each with three nonidentity labels.

There are **31 contexts** in total.

Order them by inclusion of their generated commutative algebras. In this selected family, the listed Pauli-support inclusions implement the required inclusions.

Each context is a classical-compatible measurement algebra. The two-qubit theory as a whole is not identified with one such context.

Equal vector-space dimension is not algebra identity: a maximal abelian context of dimension four is not the same algebra as a local noncommutative M₂, also of vector-space dimension four.

## Step 10. Construct the character presheaf explicitly

To each context assign its characters: multiplicative value assignments compatible with its algebraic product relations.

The scalar context has one character, a single-observable context has two, and a maximal context has four.

For commuting Pauli labels P,Q,R with PQ=sR, where s=±1, allowed values obey:

\[
v(P)v(Q)=s\,v(R).
\]

Characters restrict from larger contexts to smaller ones. The code checks that restrictions are valid, preserve identity, and compose correctly.

This is an explicit presheaf on the finite context category. The usual presheaf category provides a mathematical setting in which to study it. The program verifies this particular object and its maps, not every topos axiom by enumeration.

This supplies a concrete connection between operator-algebraic contexts and a contextual/presheaf description. It does not identify internal logic with experience.

## Step 11. Show why a global deterministic valuation fails

Use the following Mermin–Peres square:

| | | |
|---|---|---|
| XI | IX | XX |
| IZ | ZI | ZZ |
| XZ | ZX | YY |

Every row and column consists of commuting observables and is one of the available contexts.

The products of the three rows are all +1. The products of the first two columns are +1 and that of the third column is −1.

Suppose each of the nine observables had one context-independent value ±1 preserving these product relations. Multiplying all six constraints would give:

- +1 on the value side, because every value appears twice;
- −1 on the operator-product side.

Contradiction.

The implementation independently exhausts all 2¹⁵=32,768 assignments to the full selected observable set and finds **zero global valuations**.

This excludes the specified noncontextual deterministic assignments. It is not a proof that every possible hidden-variable theory is impossible, that all logic is nonclassical, or that a global quantum state cannot exist.

## Step 12. Retain a global quantum state and compatible local probabilities

The state ρ assigns context-outcome probabilities by:

\[
p_\rho(\chi\mid C)=\operatorname{Tr}(\rho\Pi_{C,\chi}),
\]

where Π is the corresponding context projector.

These distributions are nonnegative, normalized, and compatible under restriction: summing probabilities of fine outcomes yields the probability of the restricted outcome in the smaller context.

The tests verify this for every inclusion among the 31 contexts and the selected states.

Thus:

> **There is a global quantum state and a compatible family of contextual distributions, but no global deterministic character assignment.**

Compatibility must be stated for the right mathematical object. The absence of one kind of global object does not imply the absence of every global description.

The Born probability rule is **supplied here as part of quantum theory**, not derived from contextuality, self-location, or a demand for intelligibility.

## Step 13. Separate local operations from selective conditioning

Reset output B to |0>. The joint state changes, but the reduced state on C does not. The code implements a trace-preserving local reset with two Kraus operators and checks that result.

Now instead measure Z on B and condition on its outcome. For the Bell state:

- outcome 0 has probability 1/2 and conditional C state |0><0|;
- outcome 1 has probability 1/2 and conditional C state |1><1|.

Averaging over outcomes leaves C maximally mixed.

Conditional prediction using a received outcome record is not the same as an unconditioned signal sent to C. The code does not select an actual quantum outcome or solve the measurement problem by computing conditional states.

This gives the operational causal diagram an explicit consistency check without claiming full relativistic causal dynamics.

## Step 14. State what the common construction earns

The four presentations are linked by defined operations:

| Presentation | Object | Explicit connection |
|---|---|---|
| Quantum information | States, isometry, channel and dilation | Observable duality and partial traces |
| Local algebra | Tensor-product regional observable net | Isotony, commutation, state restriction |
| Causal process | Preparation preceding two output operations | Local-operation and conditioning checks |
| Contextual description | 31 contexts, characters and distributions | Restriction maps, projector probabilities, parity obstruction |

They do not merely share a metaphor. Their overlaps yield the same computed quantities, and the non-preserved structures are exposed rather than hidden.

This is what the proposed integrated architecture looks like when one small part is actually constructed.

## Step 15. Do not overclaim the remaining integrations

The common model does **not** yet supply:

- an AQFT over relativistic spacetime;
- a causal-set growth law or manifold reconstruction;
- a twistor reconstruction;
- a Langlands correspondence for this process;
- a renormalization or universality analysis;
- a self-maintaining biological or artificial organization;
- a phenomenal identity or subject boundary;
- an explanation of the supplied state, dynamics, probability rule, or actuality.

A finite causal poset is not already causal-set quantum gravity. A finite contextual presheaf is not already a theory of subjectivity. The finite net is not a proof that all AQFT structures reduce to tensor products of qubits.

The absence of those results is not a proof that they cannot be added. It is the present integration ledger.

## Step 16. Preserve the occurrence-first constraint

Executing the Python model checks an abstract construction. It does not establish that the represented Bell preparation physically occurred in the sandbox, that each context is another execution, or that any modeled system experienced anything.

The 31 contexts are descriptions of compatible measurement settings. The 32,768 assignments are attempted value models. Neither number counts worlds, realizations, or observers.

A global density operator is also not the explanation of why its concrete realization exists. Mathematical compatibility and physical actuality remain different achievements.

## Step 17. Choose the next bridge without changing the goal

The next substantial extension should change one declared scope condition, not simply attach another framework name.

A useful extension is **dynamical locality with a declared spacetime/causal domain**: extend the final-slice net to a process with a justified assignment of operations and observables across regions and times, while preserving the computed channel and contextual restrictions where they overlap.

That is where a causal-order/observable-net relation can become more than a three-event diagram. It will require a justified dynamics and realization interpretation; it must not multiply input and output occurrences merely to make a static tensor-product picture.

The phenomenal line should proceed in parallel using independently warranted whole-episode contrasts. Neither local quantum correlation nor contextuality should be installed as a unity principle by definition.

## Reproducibility and mathematical scope

- `model.py`: the explicit matrices, channel and unitary dilation, output net, context family, character presheaf, distributions, valuation search, and local operations.
- `test_model.py`: 30 tests.
- `enumeration.json`: generated structural and state summaries.
- `results.log`: actual run output.

The selected matrices and operations use small dyadic Gaussian rational entries, exactly representable by the complex-number operations used here. No tolerance-based comparisons or numerical eigensolvers are used. This exactness statement concerns the supplied examples, not arbitrary real/complex input matrices or arbitrary conditioning probabilities.

```bash
# This construction
cd research/framework_overlap
python -m unittest -v test_model.py

# All research folders, from repository root
python research/run_checks.py
```

The parity proof establishes the stated obstruction; the exhaustive search checks the finite implementation independently. The channel identities follow from the specified matrices and ordinary linear algebra, not an empirical experiment or a new unification theorem.

**Observed result:** 30 new tests pass; 276 tests pass across eleven research folders.

### Final verdict

We have moved from “these frameworks might fit” to **one explicit finite construction in which information, observables, causal process structure, and contextual restriction genuinely fit**. The construction also proves that successful integration need not mean making every representation a classical global valuation or every translation an isomorphism. It is a verified partial bridge—not the completed correct account of reality, experience, or all mathematical frameworks.

## Subsequent dynamical extension

[Constructive step 12](../dynamical_locality/REPORT.md) embeds the Bell-preparation example into a three-qubit, three-slice model. It verifies explicit causal cones and cross-time commutation, distinguishes whole-system isomorphisms from reduced-channel maps, and transports the contextual parity obstruction without treating temporal labels as new independent systems.
