# Can a minimal quantum description select physical parts and subjects?

## Main result

A nondegenerate Hamiltonian and a specified pure global state do **not always** select a unique two-part tensor decomposition, even when the state is a product in both decompositions and both admit perfectly stable pointer states. The explicit example below has a symmetry that preserves the entire stated input `(H, ρ)` but changes the candidate subsystem algebras in a way that is neither a local change of basis nor a swap of the two factors.

This is a conditional obstruction for a very lean physical starting point, not a universal no-go theorem for quantum mereology or the existence of subjects. If the symmetry is merely a redescription, the two factorizations may represent one physical structure; if the distinction is treated as physical, some additional fact or a different input is needed to pick one. Either way, the example rules out treating the written tensor labels themselves as an independently justified subject boundary.

The construction applies known unitary-covariance and quantum-mereology ideas to the problem exposed by the [Ney audit](NEY_WAVE_FUNCTION_REALISM_AND_RELATIONAL_EXPERIENCE_AUDIT.md). It does not derive consciousness, spacetime, a real brain model, or a measurement outcome. Experience is an accepted datum. Our C3 is **full structural and experiential intelligibility**, jointly with C1–C7, including parsimony; the preferred experiential, timeless whole is not assumed to be a universal subject.

## Prior work and exactly what is being tested

Carroll and Singh, [*Quantum Mereology: Factorizing Hilbert Space into Subsystems with Quasi-Classical Dynamics*](https://doi.org/10.1103/PhysRevA.103.022213), propose searching fixed-dimensional tensor factorizations for robust, predictable pointer states. Their stated procedure constructs a candidate pointer observable, computes short-time linear-entanglement and pointer-entropy growth, and minimizes a combined score. They acknowledge the task of choosing subsystem dimensions, iterating the split, stability and computational feasibility as open. They analyze examples, not an experiential selector.

Stoica, [*3D-Space and the preferred basis cannot uniquely emerge from the quantum structure*](https://arxiv.org/html/2102.08620v6), argues that specified distinguishing emergent structures are nonunique for a minimalist Hilbert-space/state/Hamiltonian framework. His conditions and what counts as physical equivalence matter; I have not fully checked the proof or claim its general conclusion here. Our explicit example uses a **state-preserving** symmetry in one finite instance. It illustrates a particular identifiable obstruction, not a verification or refutation of his general theorem or a demonstration that Carroll and Singh's published numerical example fails.

## A four-dimensional physical sector

Let `H` be a Hermitian operator on `C⁴`, and let `ρ` be an actual state:

```text
H = diag(0, 1, 2, 4),       ρ = |00⟩⟨00|.
```

All four energy eigenvalues are distinct. The labels `00,01,10,11` are the basis chosen to display **one** candidate tensor product `A⊗B`; they do not, by themselves, establish physical subsystems. In that factorization, with Pauli matrices `X,Z` and identity `I`,

```text
H = (7/4) I⊗I − (5/4) Z⊗I − (3/4) I⊗Z + (1/4) Z⊗Z.
```

The last term is a genuine interaction relative to this partition. Define

```text
U = diag(1, 1, 1, −1),    U² = I.
```

It commutes with `H` and preserves `ρ`. Now transform the entire proposed factor structure by conjugation with `U`. The original subsystem algebras `A = M₂⊗I`, `B = I⊗M₂` become `A′ = U A U†`, `B′ = U B U†`:

```text
X_A  = X⊗I  →  X_A′ = X⊗Z,     Z_A → Z⊗I,
X_B  = I⊗X  →  X_B′ = Z⊗X,     Z_B → I⊗Z.
```

`A′` and `B′` are again commuting full two-level factor algebras that generate the total matrix algebra. They are not the old algebras in a different basis internal to the factors: `X⊗Z` fails to commute with `I⊗X`, so is not in original `A`; it fails to commute with `Z⊗I`, so is not in original `B` either. Thus even a factor swap does not identify the two decompositions. `U` is an entangling controlled-phase operation relative to the original partition, not a product of local unitaries.

At the same time, `U H U†=H` and `UρU†=ρ`. The original state is `|0⟩_A|0⟩_B`; its image is unchanged, so it is also a product in the primed factorization. The same is true in their respective coordinates for the primed images of candidate product states. **Nondegenerate energy and a given pure global state have not broken this stabilizer.**

## Why the quasi-classicality criteria do not automatically remove this tie

In the original partition, use the `Z_A` eigenstates `|0⟩,|1⟩` with environment ready state `|+⟩`. Because the Hamiltonian is diagonal in the `Z_A` basis, each initial state

```text
|j⟩_A ⊗ |+⟩_B,    j=0,1,
```

remains a product `|j⟩_A ⊗ |e_j(t)⟩_B` under `e^(−iHt)`. The system pointer value stays definite and its reduced linear entropy stays zero. Thus, for these test states, both the linear-entropy and pointer-entropy growths are zero for all model times. The interaction distinguishes the two pointer values through its conditional action on B; the existence of a useful record requires a separate analysis of the environment state and time, not just this conditional coupling.

Since U commutes with H, the U-images of these states have **the same evolution in the primed tensor description**, the same pointer probabilities and zero entropy growth. The entangled-looking original-coordinate vector `U(|1⟩⊗|+⟩)` is nevertheless a product of primed factors. Conjugating a candidate physical system, candidate pointer and all test states together transports any score defined solely from H and those quantities to the same score.

The `Z_A⊗Z_B` product is an admissible zero-commutator candidate pointer for the particular interaction, after normalization. The paper's candidate-pointer minimization can have ties; this calculation chooses one allowed pointer and does **not** rerun the full algorithm or establish what its implementation returns when faced with all ties. Nor do short-time score equality and our simple stationary pointer imply an emergent classical trajectory, a unique macroscopic world, or a viable model of our universe. What is established is narrower: stable product-pointer tests of this form cannot distinguish the two transported decompositions on this input. The exact matrix identities and both pointer initial states are checked by [the standard-library verifier](verification/quantum_mereology_symmetry_gate.py) and [its receipt](verification/quantum_mereology_symmetry_gate.json).

Here `t` is only the parameter of this nonrelativistic comparison model. It is not posited as an external clock for the fundamental whole; a timeless framework would still need to reconstruct appropriate locally ordered dynamics.

## What uniqueness can and cannot mean

Let a proposed deterministic selection map depend only on the input `(H,ρ)` and be equivariant under the unitary redescriptions admitted by the theory. Any unitary that fixes both input objects must take its selected result to itself. In the example, `U` fixes the input but sends the original factorization to a different one. So a selector cannot return **that specific factorization alone** while also being U-equivariant. The same applies to its primed image. This standard stabilizer reasoning does not imply that *no other* factorization is U-invariant, or that every possible quantum input has such a symmetry.

Three principled responses remain:

1. **Treat U as representational equivalence.** Return an orbit or equivalence class. Then there is no physical fact about which representative is selected, unless another invariant relational condition says otherwise. An orbit of subsystem descriptions is not automatically a subject or a collection of subjects.
2. **Keep the alternatives physically distinct.** Supply an independently motivated structure that is not preserved by U—for example, a physical algebra of available operations, an apparatus coupling, a boundary/record relation, or additional laws. The selector must use that fact and transform it under genuine redescriptions. Such structure need not be fundamental spacetime; but it must be justified and its cost counted.
3. **Return multiple or indeterminate candidates.** This is equivariant, but candidates do not automatically correspond one-for-one to actual minds. An invariant probability distribution over options is a mathematical distribution, not an explanation of a realized subject identity or an external actualization mechanism.

For example, if an apparatus physically fixes the observable `X_A=X⊗I` and an independent preparation `|++⟩`, the expectation of this fixed `X_A` is 1 whereas that of `U X_A U†=X⊗Z` is 0. The two operational questions are then distinguishable in that stipulated apparatus model. These added preparation/operation facts are **not** derivable merely from the displayed `(H,ρ)`; the `|++⟩` preparation is not the actual state `ρ` above. If the apparatus and observables are instead transported together with the description, predictions remain equal. Operational distinguishability under extra structure is not automatically a phenomenal distinction.

These distinctions are important for a timeless plenitude: equivalent representations must not be silently counted as different actual possibilities or subjects; conversely, a mathematical symmetry need not be declared a gauge equivalence without argument. The user's strongest possibility–actuality thesis remains an independent premise, not something inferred from this finite example.

## How this changes the route to a subject-and-experience bridge

A useful next candidate must state its **input interface** explicitly, before optimizing a subject criterion:

- **Physical articulation:** the states, laws, observables, admissible local interventions and equivalences; if subsystem algebras are derived, specify the derivation and how its ties are handled. Avoid assuming ordinary spacetime as fundamental.
- **Shared record/operation anchors:** identify whether a physical preparation, interaction or record breaks a stabilizer, and show that the same anchor is present in all compared descriptions. Such an anchor supplies physical distinctions, not experiential ownership.
- **Constitution:** say which actual relational processes form which perspectives, their overlap and persistence. Do not identify a mathematical factor, pointer, record or global wave function with one subject by definition.
- **Character and valence:** independently specify a physical mismatch and law connecting it to quality, as well as a rival experiential mapping and calibrated predictions; symmetry of the physical description alone determines none of these. See the [mismatch bridge gate](AFFECT_PREDICTION_ERROR_AND_MISMATCH_BRIDGE_GATE.md).
- **Measure and parsimony:** decide which descriptions are physically equivalent before weighting occurrences; do not turn a parameterized family of equivalent descriptions into extra subjects. Count any added observables, grounding principles and selection laws in C7, while requiring all of C1–C7.

The result links Ney's representational underdetermination with the earlier [subject factorization](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md), [ties and redescription](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md), and [quantum access](QUANTUM_ACCESS_STRUCTURES_AND_SUBJECT_COUNT_GATE.md) analyses. It is a failure of one shortcut, not a derivation of a positive subject or valence law. B4–B5, B6–B12 and other previously open gates remain open; B3 remains conditional.

## Reading limits

- Carroll and Singh, [*Quantum Mereology*](https://arxiv.org/html/2005.12938v3): abstract, introduction and selected sections on factorization, robustness, pointer criteria, the proposed algorithm, numerical-example discussion and parts of appendices inspected. Other sections, full derivations, all six figure images, numerical code and a full algorithm replay were **not** inspected. The preprint is available; this is a partial reading, not a claim it was inaccessible.
- Stoica, [*3D-Space and the preferred basis cannot uniquely emerge from the quantum structure*](https://arxiv.org/html/2102.08620v6): abstract, opening, selected statements and proof passages of the symmetry/uniqueness arguments and applications inspected. The full argument, all assumptions, figure images, alternative responses and proof chain were **not** audited. Available full text is not the same as fully read.
- Wallace and Timpson, [*Quantum Mechanics on Spacetime I: Spacetime State Realism*](https://arxiv.org/html/0907.5294v1): abstract, introduction and selected sections on region-state assignment and nonseparability inspected; full arguments, relativistic details, notes and figure were **not** audited. Their approach takes spacetime regions/compositional structure as an input; it does not by itself derive emergent spacetime for our project.
- Ney, [*Three arguments for wave function realism*](https://doi.org/10.1007/s13194-023-00554-5): supplied article completely read as described in [our audit](NEY_WAVE_FUNCTION_REALISM_AND_RELATIONAL_EXPERIENCE_AUDIT.md), including the scope of its visual checks.

The symmetry/equivariance observation and quantum-pointer machinery are established concepts; no claim is made to have invented them. The precise matrix example is an application to the project's interface, not a claim of priority over earlier literature.
