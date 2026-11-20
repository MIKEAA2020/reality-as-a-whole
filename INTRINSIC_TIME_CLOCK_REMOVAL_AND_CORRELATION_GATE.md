# Timelessness, intrinsic time and the cost of removing a clock

## Main result

A globally stationary quantum state can encode different locally conditioned descriptions without invoking an external universal clock. However, **discarding the physical relation that carries the conditioning can erase observable information**. In the exact finite example below, two orthogonal stationary states have identical reduced system states and the same coherent sum of conditional system kets, yet a constraint-commuting relational observable distinguishes them perfectly.

This is a concrete information-preservation test for attempts to replace a clock–world description by an intrinsic-world description. It does **not** show that intrinsic time is impossible, or refute a continuum construction by a finite example. An intrinsic formulation may preserve the relevant degree of freedom or observables within the world; it must demonstrate that it does. The model is not a solution of quantum gravity or the phenomenal experience of time.

The preferred framework remains a timeless, self-sufficient relational whole with genuine plural subjects, not a universal subject or an outside creator. Experience is valid data; C3 is **full structural and experiential intelligibility**, jointly with the other six criteria. Our previously identified time, subject, quality and measure gates remain open.

## The literature and what is genuinely new here

O. C. Stoica's [*The preferred-time problem in the conditional interpretation of time*](https://arxiv.org/html/2608.16732v1) argues that even after selecting a clock subsystem, multiple candidate clock observables can yield different conditional decompositions; it proposes replacing a separate clock with an intrinsic world time observable built from macroscopic pointer observables. I read the **entire available HTML text, all eight chunks including references**. I did not independently prove its claims about continuum operator domains, inspect a PDF rendering of equations or independently audit its cited proofs. It is a preprint, and its conclusions are contested arguments, not an established universal no-go theorem.

Stoica's concern is real: specifying a tensor decomposition and constraint does not automatically establish a uniquely meaningful physical time observable. The proposed intrinsic pointer has to be selected and interpreted too. But the inference from this to the impossibility of every clock-conditioned approach is not established merely by presenting multiple formal observables. Some can be distinguished by independently specified physical couplings, records or admissible measurements; whether those can be derived without circularly assuming temporal structure is a further question. Such input need not be an external time.

Importantly, Stoica's paper proposes both (i) a formal expression consisting of a coherent integral over world kets and (ii) a reinterpretation in which a time degree of freedom is **retained within the world**. These are not automatically the same operation. The comparison below tests the loss of the clock label by a naive coherent sum or partial trace; it is **not a proof** that his more elaborate intrinsic degree-of-freedom proposal loses information. He assumes the existence and sufficient resolving power of an intrinsic time observable; he does not construct or calibrate that observable in the paper.

The central Page–Wootters and relational-observable mathematics is existing work, not our invention. Our contribution is the explicit, reproducible contrast between conditional correlations, tracing out a clock, and coherent summation, connected to the project's existing [stationary relational-constraint construction](RELATIONAL_TIME_CONSTRUCTION.md) and [subsystem-symmetry gate](QUANTUM_MEREOLOGY_STATE_STABILIZER_GATE.md).

## One fixed constraint and two stationary states

Take two two-level sectors `C` (candidate clock) and `S` (system), with basis `|0⟩,|1⟩`. In units with `ℏ=1`, set

```text
H_C = −|1⟩⟨1|,     H_S = |1⟩⟨1|,
C = H_C⊗I + I⊗H_S,
|Ψ±⟩ = (|00⟩ ± |11⟩)/√2.
```

Both states satisfy `C|Ψ±⟩=0`; the zero in the constraint is not an external time coordinate. The negative clock energy is a modeling choice, not a realistic energy spectrum or a derived gravitational law. The two states are orthogonal. Their clock and system reductions are both `I/2`, although their joint correlations differ. This sector has a finite periodic clock and cannot have an exact canonical `[T,H_C]=iI` relation: it is **not** the ideal noncompact clock assumed in some continuum arguments.

Define four phase readings `t∈{0,π/2,π,3π/2}` using

```text
|t⟩_C = (|0⟩+e^(it)|1⟩)/√2,    E_t = (1/2)|t⟩⟨t|.
```

The four effects are positive and sum to `I`. They form an overcomplete **POVM**, not four mutually orthogonal clock states or a projective clock. This is one specified set of possible clock readouts, not a proof that it is uniquely selected. For either stationary state each outcome has probability `1/4`. With these phase conventions the normalized conditional system kets are

```text
|ψ±(t)⟩ = (|0⟩ ± e^(−it)|1⟩)/√2.
```

They give the following expected values of the system Pauli `X`:

| Clock phase | 0 | π/2 | π | 3π/2 |
|---|---:|---:|---:|---:|
| `Ψ+` | +1 | 0 | −1 | 0 |
| `Ψ−` | −1 | 0 | +1 | 0 |

Thus different clock conditions yield different system predictions in a global stationary state. This is a standard relational result, not evidence that any of these quantum systems is conscious. The four effects themselves do not commute with C, so treating a raw clock projector as a physical Dirac observable would be unjustified. On the zero-constraint sector, define the relative operator

```text
R_t = e^(it)|00⟩⟨11| + e^(−it)|11⟩⟨00|.
```

It commutes with C and has exactly the same expectation values in the table. It is a physical-sector observable *for this model*, not an independently built clock-measurement apparatus. The [prior constraint construction](RELATIONAL_TIME_CONSTRUCTION.md) likewise exhibits relational observables reproducing conditional predictions for a specified flat finite history; it does not settle their physical selection or quantum-gravity implementation.

## Three different operations, three different results

1. **Keep the clock–system relation.** With the fixed, physically specified relational `R_0`, the two stationary states give `+1` and `−1`. Their joint physical correlations are distinguishable. Under a genuine redescription, state, constraint and observable must all be transformed; the comparison is not based on a convention-dependent sign alone.
2. **Trace out C.** Both global states give the same system density matrix `I/2`. This ordinary partial trace deliberately discards the relative phase correlation. It is not a state-vector sum and is not an invertible removal of a physical subsystem.
3. **Coherently average the four chosen conditional kets.** With the explicit phase convention above,

   `(1/4) Σ_t |ψ+(t)⟩ = (1/4) Σ_t |ψ−(t)⟩ = |0⟩/√2`.

   After normalization both are `|0⟩`. This also erases the distinction, but it is **not the same operation as the partial trace**: the latter yields `I/2`. Summing conditional kets is phase-convention dependent unless one supplies a coherent prescription for their phases. The finite sum illustrates the concern raised by a bare integral of world kets; it does not establish the behavior of Stoica's continuum integral, regularization or physical inner product.

Hence an unlabelled sum of instantaneous vectors and an unconditioned system density matrix do not, in this example, preserve what the anchored relational measurement distinguishes. To establish an equivalent intrinsic account one needs a specified map, its physical inner product and mapped observables, with probabilities and correlations preserved. If a clock-like degree of freedom is retained inside the world, that is a possible way to retain the missing information; then one must still justify its selection and operational meaning.

[`verification/intrinsic_clock_phase_erasure_gate.py`](verification/intrinsic_clock_phase_erasure_gate.py) checks both states, all four POVM outcomes, conditional values, commutators and the erasure distinction. Its numerical entries are exactly representable dyadic/Gaussian-dyadic numbers; [the receipt](verification/intrinsic_clock_phase_erasure_gate.json) records the result. This is a finite model check, not a derivation of the cited continuous theory, a unique time operator or empirical evidence of an experience.

## A way forward without a universal clock

A self-contained relational account should preserve *local* physically anchored correlations, rather than posit one global time observable simply to resolve an ambiguity:

1. **Define the physical domain.** Specify constraints, physical state/inner product, candidate local observable algebras and their admissible redescriptions. Explain whether apparent subsystem symmetries are gauge or represent distinct physical structures; do not count their descriptions as additional subjects.
2. **Specify a candidate clock and its physical record.** Provide a POVM or other observable, preparation and an actual or in-principle interaction/record, with domain, finite precision, backaction and reachable correlations. A formal phase label or a separately named intrinsic pointer is not yet a readable clock. The model above specifies readout effects, not a demonstrated laboratory apparatus.
3. **Show operational equivalence across descriptions.** Map clock, records, allowed interventions and relational observables together; preserve the joint probabilities relevant to a declared experiment. Identical single-time marginals do not by themselves establish multi-time history probabilities, as the [joint-event audit](TIMELESS_CLASS_OPERATORS_DECOHERENCE_AND_JOINT_EVENTS.md) explains.
4. **Handle recurrence and different clocks.** A clock may require additional memory or a branch label to distinguish recurring readings. Distinct local timekeepers need not produce one globally valid coordinate. Barontini's [cold-atom audit](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md) and [five-trace comparison](COLD_ATOM_CLOCK_COMPARISON.md) are empirical constraints on a particular entropic path clock, not an experiment realizing a stationary Wheeler–DeWitt universe.
5. **Bridge physical records to subjects and experience.** Specify which episodes belong to which perspectives and why their character is experienced, including mismatch/valence if that proposal is retained. A correlation or successful clock is not felt passage; no universal consciousness is implied. Self-location weighting and genuinely possible histories require separate justification.

These steps specify what a proposed solution must deliver; they do not presuppose that the whole becomes actual in time. They also do not require one common clock for every perspective. The finite model does not resolve B4/B5, B6–B12, the actual self-existent constitution, or the full general-relativistic problem of time; B3 remains conditional.

## Additional source scope

- Kuypers and Rijavec, [*Measuring time in a timeless universe*](https://arxiv.org/html/2406.14642v3): abstract, introduction, selected finite-interaction timer sections and selected rigged-Hilbert-space appendix passages read. They describe a clock–timer interaction in their chosen model; this does not establish that any clock is readable at zero physical cost. Other sections, complete derivations, figures and supplementary calculations were not fully audited. Their test-function discussion invokes Schwartz behavior; the printed later phrase that all square-integrable functions vanish at infinity should not be used without those stronger hypotheses.
- Höhn, Smith and Lock, [*The Trinity of Relational Quantum Dynamics*](https://doi.org/10.1103/PhysRevD.104.066001): abstract and opening introduction read; full assumptions, proofs, figures and relativistic extensions not inspected. Their claimed equivalence and treatment of conditional transition probabilities are important existing work, not rederived here or presumed to solve all general relativity.
- Loveridge and Miyadera, [*Relative Quantum Time*](https://arxiv.org/html/1905.08078): abstract and introduction/initial clock discussion read; remainder and proofs not checked. They discuss invariant relative observables and the limitations of ideal unbounded clocks.
- Stoica, [*The clock ambiguity problem: extended or extinguished?*](https://arxiv.org/html/2604.21805v2): abstract and introduction only; full claimed theorems and argument for physically meaningful observables not audited. Its claims about records and purely relational approaches should not be adopted without examining its equivalence assumptions.
- Barontini, [*Testing the problem of time with cold atoms*](https://doi.org/10.1103/1h9j-df4k): the source and processed-trace scope is in the linked project audits; raw images and entropy reconstruction were not independently reproduced.

All the partially read full texts above are available through the stated links; partial reading is not an access failure. Stoica's preferred-time paper was read in full HTML, but that does not independently validate its mathematics or its references.
