# Timeless whole, local time and a quantum world

## The two articles and reading scope

[Tim Maudlin, “Einstein didn't think time was an illusion”](https://iai.tv/articles/tim-maudlin-einstein-didnt-think-time-was-an-illusion-auid-2317?_auid=2020) argues that relativity retains objective temporal relations and that invoking Einstein's condolence letter does not establish that time or its direction is unreal. His specific historical interpretation of Einstein's intentions is an argument, not something established by that letter alone.

[Vlatko Vedral in conversation with Ozbir Kip, “Everything is quantum, including you”](https://iai.tv/articles/everything-is-quantum-including-you-auid-3715?_auid=2020) advocates a universally quantum description, including observers and instruments, rather than a fundamental quantum/classical split. He regards his picture as close to many-worlds, while preferring to speak of one universe with quantum properties. He proposes experiments and acknowledges that his preferred account could be wrong. His suggestion that even integers might ultimately follow from quantum physics is presented as speculative.

Both supplied pages returned their full article/interview prose through their conclusions, although they also display subscription prompts. Vedral's book *Portals to a New Reality: Five Experiments to Unlock the Future of Physics* was **not read**. Neither interview statements nor broad popular summaries are substitutes for the technical experiments or complete interpretive arguments.

## 1. Maudlin's challenge to the timeless absolute

We should not say “relativity proves time is an illusion.” In relativity there is no general inertial-frame-independent simultaneity for spacelike-separated events. Timelike-related events nevertheless have an invariant temporal order once a time orientation is chosen; physically measured proper time along a clock's worldline is not abolished by relativity. General relativity admits a range of spacetime geometries; special cosmological models can have a useful preferred cosmic time without providing an external universal clock for every spacetime or for the absolute.

Separate the following questions:

- **Temporal geometry and order:** what clocks measure, whether a pair of events is timelike-related, and in what order along an oriented timelike worldline.
- **Thermodynamic and record arrows:** why, in appropriate circumstances, records, memories and entropy gradients exhibit a shared orientation.
- **Objective present or passage:** whether there is an additional metaphysically privileged present or “flow,” beyond temporal relations and physical processes. Maudlin argues for objective direction, while what counts as a further flow is debated; an ordered structure need not by itself settle that debate.
- **Fundamentality:** whether temporal structure belongs to the deepest level or is constituted by relations in a more basic, timeless account.

Our proposal addresses the fourth question. It does **not** deny the first three as mere mistakes: observable clock behavior, real local changes, records and experienced succession are targets of explanation. The claim that the absolute is timeless is neither a consequence of Einstein's letter nor established by relativity. Conversely, real relativistic temporal structure alone does not prove that time must be metaphysically fundamental. It places substantive recovery requirements on any timeless proposal.

In particular, Maudlin's insistence on order is a challenge: the whole must contain sufficient asymmetric physical relationships to recover local clock readings and records, not just an undirected collection of possible events. It must also explain why experience has its locally ordered character; a clock variable or the assertion of experience as intrinsic does not yet do that.

## 2. Vedral's challenge to a classical observer outside quantum theory

Ordinary measurement devices and brains are made of matter for which quantum theory is extraordinarily successful. Quantum behavior has also been demonstrated in diverse macroscopic degrees of freedom. This supports modelling an observer and measuring instrument as quantum systems when appropriate; it does not show that a whole brain maintains accessible, functionally decisive macroscopic coherence or that consciousness requires it. The microscopic origin of matter, robustness of an effective classical description, and evidence for a specific brain mechanism are different claims.

Unitary measurement plus environmental entanglement can suppress interference in an accessible reduced description and yield robust correlated records in a suitable regime. This is the established decoherence programme; see [Schlosshauer, “Decoherence, the measurement problem, and interpretations of quantum mechanics,” DOI 10.1103/RevModPhys.76.1267](https://doi.org/10.1103/RevModPhys.76.1267). Its uploaded paper was previously text-extracted and assessed in [the source audit](SCHLOSSHAUER_DECOHERENCE_RECORD_AND_SUBJECT_GATE.md). Suppression in a subsystem is not, by itself, a proof that one outcome alone exists, nor a derivation of subjective experience or the Born rule. Vedral's statement that the entanglement is sufficient to explain experienced individual outcomes is his interpretive position, not a settled experiment-independent consequence accepted by every interpretation.

Keep distinct: the universality of the quantum formalism, global unitarity versus collapse, the ontology of branches, and the existence and identity of subjects. A single whole is compatible with various interpretations, but it does not automatically settle any of these. Plural experiences are not established merely because a state has multiple components.

Nor is “Q numbers” a license to conflate different formalisms. In the usual Schrödinger representation, state-vector amplitudes are complex numbers; observables are operators. In quantum field theory fields can be operator-valued distributions. An operator-valued field amplitude is not the same as every quantum wavefunction coefficient. The interview's “everything is a Q-number wave” is a particular way of presenting physics, not a reason to erase these distinctions.

## 3. A precise compatibility gate, not a derivation of reality

Page and Wootters' established [“Evolution without evolution: Dynamics described by stationary observables,” DOI 10.1103/PhysRevD.27.2885](https://doi.org/10.1103/PhysRevD.27.2885), illustrates how a constrained stationary state can encode conditional evolution. Its bibliographic record was checked here, not the complete original paper. The following two-level instance is a teaching example of that existing mechanism, not a new discovery.

Let `C` be a clock qubit and `S` a system qubit. Set `ℏ=1` and choose

```text
H_C = ω |1⟩⟨1|,   H_S = −ω |1⟩⟨1|,
|Ψ⟩ = (|0⟩_C|0⟩_S + |1⟩_C|1⟩_S)/√2,
|t⟩_C = (|0⟩ + e^(−iωt)|1⟩)/√2.
```

The given state obeys `(H_C + H_S)|Ψ⟩ = 0`. Conditioning on the stated clock reading and normalizing gives

```text
|ψ(t)⟩_S = (|0⟩ + e^(+iωt)|1⟩)/√2,
P(+X | t) = (1 + cos(ωt))/2,
P(+Y | t) = (1 + sin(ωt))/2.
```

Thus a stationary global constraint is **compatible with** changing local conditional predictions; no external clock for the whole appears in this equation. The parameter labels the chosen clock states, and an experiment still needs a physical clock POVM, preparation and readout. This is a deliberately constructed constraint, not a proof that our universe is stationary in this sense. The negative system energy is harmless in this finite bounded toy model but is not justified here as a physical gravitational Hamiltonian.

The example also shows what the construction fails to establish:

- The pure conditional system state has zero von Neumann entropy for all `t`; changing conditional probabilities alone do not generate a thermodynamic arrow or durable memory.
- The two-level clock repeats after `2π/ω`; its states at different labels need not be orthogonal. It is not a globally reliable clock or a continuum of independently distinguishable readings.
- Choosing the opposite clock orientation reverses the parameterization; interpreting one direction as the past-to-future record direction needs additional structure and boundary conditions, not just the equation.
- There is no gravitational constraint algebra, emergent Lorentzian geometry, interacting quantum field theory, subject-constitution rule, or experiential quality in this finite model. It cannot solve those problems by analogy.

The [earlier audit](TIME_SOLUTION_EVIDENCE_AUDIT.md) records why relational clocks, modular time and the existing toy models do not solve the general problem of time. In particular, [Barontini, “Testing the problem of time with cold atoms”](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md) supplies a relevant internal-clock laboratory analogue; the setup is not an entire universe or evidence that the cosmos is globally stationary. Its experimental protocols employ ordinary external laboratory preparation and measurement, and a demonstrably useful internal time does not imply that a universal external clock exists. The measured entropy proxy involves coarse-grained position distributions and is not a direct measurement of entanglement entropy; further limitations and the released-data comparison are in the linked audit.

## 4. What the combined challenge requires

The proposed relational, experiential whole must provide—not merely name—the following interfaces:

1. **Quantum structure:** an explicit class of permissible physical states, operations and correlations, with recovered tested quantum predictions and clearly stated interpretation.
2. **Local temporal structure:** an internal-clock construction with a controlled regime, quantified accuracy and limitations, and ultimately recovery of causal order and proper times in appropriate relativistic circumstances.
3. **Record arrow:** a concrete account of stable records, asymmetry and boundary conditions, not the equation of any increasing variable with the whole arrow of time.
4. **Plural experience:** a rule connecting actual physical organization to distinct subjects and qualities, tested against rival rules and independent reports; merely labelling a branch or an instrument “observer” does not supply it.
5. **Actuality and self-sufficiency:** an argument why the whole is self-sufficient and why genuine possibility is actuality within it, rather than a temporal process by which a world comes into being. None of the quantum or clock models here establishes those claims.

The constructive result is a separation of tasks: Maudlin's real local temporal order and Vedral's quantum observers are **not automatically incompatible** with a timeless ground, but each imposes independent obligations. We have not established that these obligations can all be met in a single physical theory, nor derived a complete account of experience, emergent spacetime or necessary plenitude.
