# Bryan and Medved: time, causality, records and the zero whole

**Source.** K. L. H. Bryan and A. J. M. Medved, *The problem with ‘The Problem of Time’*, arXiv:1811.09660v1, submitted 8 November 2018, 47 pages [2](https://arxiv.org/abs/1811.09660). I read the linked version's abstract, main text and appendices. It is a theoretical and philosophical proposal, not a reported measurement or an experimental proof. Their reference to an “observer” generally does **not** require consciousness.

**Bottom line for our work.** The paper asks exactly the next question: how do internal clock correlations, physical interactions, memory and causal direction fit together in one isolated whole? It strengthens the demand for a *physical interface*, not just a mathematically ordered list. But some of its strongest necessity claims exceed the arguments given. In particular, isolated-clock correlations need not be inaccessible to every small subsystem, and recording interactions do not by themselves yield a universal thermodynamic arrow. I constructed explicit finite countermodels and connected them to our recent coherent memory echo; the checks are in [the verifier](verification/bryan_medved_relational_time_claims_test.py).

## 1. What the authors argue

The paper distinguishes a capacity for change (“time”) from a compulsion to move through configurations (“causality”). It considers how quantum theory and general relativity might have a common deeper temporal structure, then treats a Wheeler–DeWitt-type constraint `H|Ψ⟩=0` as an isolated-universe model. In the Page–Wootters construction, the stationary whole is partitioned into a clock and the rest; conditional states of the latter depend on the clock reading.

Its distinctive proposals are:

- An isolated clock alone is, in the authors' view, inadequate to supply time to small subsystems; interactions with the clock should maintain usable correlations.
- Recording interactions are taken to be irreversible and heat-producing, giving the emerging relational time a thermodynamic arrow. With cosmological expansion as clock, they propose alignment of cosmological, thermodynamic and psychological arrows.
- Causality, defined in terms of an external influence on the affected subsystem, is the deeper unsolved problem: they do not derive it.
- They regard a purely timeless/block description as unable to account for genuine change, arguing that isolated frames and records provide at most an illusion of passage.

These are the authors' claims, not established results of the paper. In particular, “external” to a **subsystem** need not mean external to the one whole. Conversely, the authors' preference for real becoming is not the same thesis as the user's necessary plenitude.

## 2. First countermodel: an isolated clock can correlate with a small part

The authors argue in §3 and Appendix B.2 that maximal clock–rest entanglement makes the clock and rest roughly equal in size, and that a much smaller subsystem cannot itself have a sufficient clock correlation without an interaction. As a universal mathematical statement, that is too strong.

Take a four-level clock C, a four-level subsystem S, and an eight-level spectator E. Let `ω=2π/4`,

```text
H_C = −ω diag(0,1,2,3),     H_S = +ω diag(0,1,2,3),     H_E = 0,
|Ψ⟩ = (1/2) Σ[k=0..3] |k⟩_C |k⟩_S |0⟩_E.
```

There are **no interaction terms**. The total constraint `(H_C+H_S+H_E)|Ψ⟩=0` holds exactly. C is maximally entangled with the whole rest S+E, yet `dim C=4`, `dim(S+E)=32`. Conditioning on one of four orthogonal Fourier-basis clock readings gives S a matching orthogonal state. A joint clock/S readout has `P(S reading=n | C reading=n)=1` for every n. Unconditionally, the reduced S state is maximally mixed and stationary.

This is a specially prepared finite cyclic model, not a generic interacting universe or evidence of an experienced flow. The counterexample does **not** make a joint readout automatically available to S: it establishes a correlation in the global state. A physical observer must have an allowed interface to compare C with S, or a locally accessible record with the appropriate interpretation. That is where the authors' concern has real force.

### Even local clock entanglement is not necessary for a record correlation

A second four-level construction uses

```text
|Ψ_GHZ⟩ = (1/2) Σ[n=0..3] |n⟩_C |n⟩_S |n⟩_E,
```

where the displayed time bases are opposite-phase Fourier bases for C and for S,E. With clock energy `−ωk` and rest Hamiltonian `H_SE=ω(a+e mod 4)` in their energy bases, the total constraint again annihilates the state. There is no C–rest interaction; the rest Hamiltonian includes an S–E interaction. C is maximally entangled with S+E, but the reduced C–S state is the explicit separable mixture `(1/4)Σ_n |n,n⟩⟨n,n|`. It has **no C–S entanglement**, yet C and S have perfectly correlated readings in that basis and two bits of classical mutual information. This does not assert that all quantum dynamics can be reconstructed from separable C–S correlations; it only refutes a blanket requirement of local entanglement for such a record correlation.

The four readings are periodic, with a fixed chosen factorization, Hamiltonian and state. No claim of an infinite, ideal or autonomous self-reading clock follows. Likewise the finite clock has no exact canonical commutator `[H,T]=iI`: its trace would have to be both zero and nonzero. The existence of discrete time observables or POVMs is not ruled out by that trace argument.

## 3. Second countermodel: interaction does not guarantee an arrow

Use the same four-reading clock, with a two-qubit system and memory in the rest. Set

```text
U = CNOT(S→M),       H_rest = (π/2)(I−U),
|ψ₀⟩ = |+⟩_S |0⟩_M,  |ψ_n⟩ = Uⁿ|ψ₀⟩,
|Ψ⟩ = (1/2) Σ[n=0..3] |n⟩_C |ψ_n⟩.
```

Since `U²=I` and `exp(−iH_rest)=U`, the properly chosen opposite clock Hamiltonian gives `(H_C+H_rest)|Ψ⟩=0`. There is an actual S–M interaction in the rest. The system's **conditional von Neumann entropy** in bits is exactly

```text
clock n:      0    1    2    3
S entropy:    0    1    0    1
```

The first interaction correlates the memory with S; the second uncomputes that correlation. The whole history state remains pure. This exhibits reversible record formation and removal, not a proof about macroscopic thermodynamic entropy. No thermal bath or heat variable has been specified, so the circuit cannot calculate a heat cost. It is sufficient to show that an interaction, or a change in conditional entanglement, **alone** does not mathematically force an everywhere-monotonic arrow.

This is precisely what our independently constructed [coherent memory echo](ZERO_DYNAMIC_SUBJECT_BOUNDARY_AND_MEMORY_ECHO.md) illustrates in a richer constrained history: a write and its inverse cancel if nothing relevant intervenes; if Q changes the record, the attempted inverse instead transports information into a sphere-sign record. Both effects are unitary. Neither makes a thermal reservoir, sustainable low-entropy supply or irreversible experience appear automatically.

The authors also say clock–rest entanglement decreases as interactions proceed. For a single fixed pure stationary state and a fixed C/rest partition, that entanglement is one fixed number. To assert its monotonic change requires an explicitly defined evolving or conditional state, a suitable partition and an ordering parameter; it does not follow merely from `H|Ψ⟩=0`.

## 4. What thermodynamics really adds

The paper's §3 states that every interaction records information and therefore produces heat. That should not be treated as a general theorem. Logical reversibility, record copying into a prepared blank, coarse graining, genuine reset and heat transfer are distinct operations.

A rigorous Landauer statement has identifiable premises. For a memory initially uncorrelated with an initially thermal reservoir, and joint unitary dynamics, Reeb and Wolf relate the memory's entropy reduction to reservoir heat, with extra correlation and relative-entropy terms [1](https://arxiv.org/abs/1306.4352). Under the standard assumptions, resetting an unbiased bit to a definite value has the ideal lower bound `Q ≥ k_B T ln 2`; finite reservoirs and exact reset need care. Initial correlations or additional nonequilibrium resources modify the bookkeeping.

A simple check exposes the resource: swap an initially maximally mixed bit with a pure blank ancilla. The original bit becomes pure, while the ancilla becomes maximally mixed; total von Neumann entropy is unchanged and **one bit is exported to the ancilla**. The ancilla was a low-entropy resource, not a thermal bath whose temperature or heat we have calculated. This neither violates Landauer nor licenses free, indefinitely repeatable resetting.

Consequently a constructive arrow model needs a physically defined coarse graining, low-entropy boundary or equivalent resource, a bath/energy accounting if heat is claimed, and an analysis of recurrence and memory reuse. The fine-grained entropy of a closed unitarily evolving state is constant; coarse-grained and subsystem entropies can increase, decrease or fluctuate. A finite periodic model cannot exhibit strict monotonic increase around its entire cycle. A local arrow is not thereby disproved; it is a further dynamical and boundary-condition problem, not a consequence of every interaction.

## 5. Zero, causal order and the one whole

The paper is congenial to the user's proposal in rejecting an external clock for an isolated whole, and in taking internal relations seriously. But three distinctions matter:

1. **Constraint versus objective energy.** `H|Ψ⟩=0` is a constraint on the modeled state. It is not automatically an invariantly defined total matter-plus-gravity energy or a proof that reality is literally nothing. Nor does closedness alone make every quantum state stationary: a generic isolated state can be a superposition of different energy eigenstates. Shifting an energy origin changes a phase, not generic relative evolution. Our [FLRW constraint example](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md) makes this distinction explicit while showing nonzero local density and relational expansion.
2. **Causality within the whole.** An influence can be outside the affected subsystem yet internal to reality as a whole. A relational intervention model can specify which operations, records and counterfactual comparisons are physically admissible, without introducing a cause outside the whole or a fundamental preferred foliation. But writing a circuit or a causal graph does not derive its operations from zero, nor automatically orient every process.
3. **Change and necessary plenitude.** The authors argue that without a moment selecting one configuration, being in any configuration is tantamount to being in all configurations, which they regard as incompatible with physical existence. That is a philosophical premise, not a logical identity: alternative relational configurations can occupy distinct consistent roles within one structured whole without being asserted simultaneously at the same local interface. This is relevant to the user's actuality/possibility thesis, but neither establishes that every genuine possibility is actual nor derives an incidence measure or experience.

The authors' criticism of frozen frames is still important: a list of snapshots and a story about memories do not by themselves establish an interacting carrier, reliable records, actual temporal experience, or the existence of the other frames. The user's view need not identify experienced change with illusion; equally, the paper has not proved that real relational change requires a fundamental moving present or that all block/relational accounts lack causal structure. Necessity of the whole is not automatically equivalent either to deterministic local dynamics or to irreducible objective chance.

## 6. What to do with the paper

The useful advance is to replace a vague “time emerges” claim with a **three-layer construction**:

- **Constraint and clock:** specify the valid global history, clock choice and correlations, including the finite-clock limits.
- **Causal interface:** specify gauge-admissible interactions and records, and show what each confined subsystem can actually access; do not infer access merely from global correlations.
- **Arrow and experience:** identify the low-entropy/resource conditions under which records persist and interventions have a directed effective description, then separately derive or test the subject and phenomenal bridge.

Our two clock countermodels and prior memory echo establish concrete working examples for the first two layers and rule out some overly strong shortcuts. They do **not** yet derive the third layer, the underlying causal constitution, or the user's zero-whole ontology. The next substantive test is to put a resource-limited, reusable memory inside an actual constrained relational-clock history and calculate conditional record reliability, resource consumption and reversal over many ticks, with no external temporal foliation assumed.

For comparison, Giovannetti, Lloyd and Maccone provide a Page–Wootters treatment of sequential measurements with explicit memories [1](https://arxiv.org/pdf/1504.04215v3). That is a technical development, not a derivation of consciousness or ultimate causation. The paper's separate suggestion that quantum field theories generically lack global symmetries should also not be read as a theorem that all QFT symmetries are anomalous or that Lorentz invariance must fail: the no-global-symmetry argument of Harlow and Ooguri is scoped to bulk quantum gravity with a holographic dual and distinguishes internal from spacetime symmetry [3](https://arxiv.org/pdf/1810.05337).

## Subsequent constructive clock-and-memory test

[The reusable memory in a constrained clock history](ZERO_RELATIONAL_CLOCK_REUSABLE_MEMORY_RESOURCE.md) extends the actual internal-reference history with a closed twelve-tick reversible program, computes finite-memory reliability and resource accounting, and transports the counterpart symmetry through the program. It does not yet add a heat reservoir or an experiential subject.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.bryan_medved_relational_time_claims_test -v
```

Six tests check the finite-clock commutator obstruction, a noninteracting small-subsystem correlation, the separable local-record construction, a constrained reversible entropy cycle, explicit entropy export in reset, and the absence of clock–rest coupling in the first model. They are mathematical toy checks, not experimental tests of cosmology, a universal thermodynamic law or phenomenal consciousness.
