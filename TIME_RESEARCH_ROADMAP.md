# A top-down research program for the problem of time

**Status:** a proposed research program with an explicit finite-model benchmark, not a solution of the problem of time and not a claim that its specific route is uniquely necessary. The literature search is targeted and incomplete. The user asks for genuine advances, so a new result must be a precisely stated theorem, counterexample, construction or discriminating prediction that survives comparison with close prior art—not just a synthesis or a passing numerical script.

**Framework clarification:** In the intended zero-residue candidate, the absolute is timeless and spacetime is not fundamental. There is no reason to posit a universal external clock for the whole. Internal clocks are physical correlations or devices, defined only where they are applicable; local time and spacetime must be accounted for as emergent structures. Mathematical timelessness is an analogy, not a proof that mathematical truth and concrete actuality have identical ontology. Timelessness alone does not prove that internal clocks cannot happen to be globally comparable within a particular model; nor does it derive an emergent spacetime or the phenomenal experience of succession.

**Existing workspace baseline:** Before building a new turning-clock example, audit [TURNING_CLOCK_ATLAS.md](TURNING_CLOCK_ATLAS.md) and [CLOCK_CHOICE_EQUIVALENCE.md](CLOCK_CHOICE_EQUIVALENCE.md): they already propose explicit clock charts, record transport and information loss in constrained toy models. Their proofs and literature novelty require independent checking, and they do not establish the full gravitational claim. An earlier [absolute/perspectives synthesis](ABSOLUTE_PERSPECTIVES_SYNTHESIS.md) makes much stronger physical claims; those claims must not be taken as established and are subject to [the time evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md).

## 1. Define the target before choosing the tools

The problem of time has several interacting facets, not just the absence of an external parameter; see [Anderson's review](https://arxiv.org/abs/1009.2157). A **strong** quantum-gravity proposal should specify its domain and show, rather than assume, how it addresses:

1. **Physical construction:** a mathematically meaningful state space/observable algebra and quantum constraints, with domains, physical inner product and a controlled constraint algebra. If a candidate uses anomalies or extended boundary degrees of freedom, it must state why these are consistent and physical.
2. **Operational change:** internally specified clock readings, observables and multitime interventions that produce consistent probabilities and account for clock backreaction and finite resolution. A stationary constraint state alone is not a dynamics prescription.
3. **Clock comparison:** for genuinely equivalent descriptions of the *same operational experiment*, identify the map on states, effects, clock records and interventions; prove equality of the corresponding joint probabilities or state exactly where and why equivalence fails. A clock switch need not be a unitary on a naively fixed system factor and one must not equate differently conditioned probabilities without transporting the conditioning event.
4. **Clock domain:** define where each clock works, what happens at turning points/degenerate readings, and whether and how overlapping local descriptions can be patched. A single globally monotonic clock or a single global classical spacetime is not assumed to exist.
5. **Gravity and classical limit:** address the actual constraints of the intended theory, refoliation/foliation dependence and the reconstruction of semiclassical spacetime and local operational predictions. A homogeneous one-constraint toy model cannot establish these.
6. **Discrimination and scope:** show where the proposal agrees with established quantum theory/GR in applicable limits, identify predictions or mathematical properties that distinguish rivals where possible, and state unresolved UV, boundary, state-selection and empirical questions. A complete solution of time is not automatically a UV completion or an explanation of the thermodynamic arrow.

These are evaluation criteria for the present program, not a theorem that any viable framework must take one particular form. A decisive answer could be a no-go theorem showing that an attractive set of requirements cannot all hold, or a restricted constructive theorem with explicit assumptions—not necessarily a single universal clock.

## 2. What is already known—and must not be relabeled as our discovery

- [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580) already relate Dirac observables, Page–Wootters conditioning and quantum deparametrization by frequency sector and discuss clock changes in relativistic models including FRW.
- [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153) already develop a clock-neutral method for switching clocks. Global and multiple-choice issues are not solved in general by the existence of a toy-model switch.
- [Van Neerven and Portal](https://arxiv.org/abs/2306.13774) already construct generalized modular time and unsharp observables for the positive-momentum massless system. The one-branch FRW reduction in this repository is unitarily equivalent to that operator up to scale. Do not claim the clock POVM or the unnormalized modular construction as new.
- [Ahmad, Chemissany, Klinger and Leigh](https://arxiv.org/abs/2410.11029) already study extended phase spaces, crossed products, quantum reference frames and changes of frame. [Klinger and Leigh](https://arxiv.org/abs/2504.00152) propose a quantum-diamond/null-anomaly approach as a *possible* resolution of the problem of time. Neither the proposal nor its general validity is established by our limited source inspection.
- [Baumann and Lock](https://arxiv.org/abs/2603.08845) already analyze interventions and temporal delocalization across clock frames, including incorporating operations into the constraint. A new operational treatment must go beyond their stated setting, not simply repeat it.
- [Finite Quantum Histories](https://arxiv.org/abs/2608.05748) already discusses predictive quotients and irreversible coarse-graining versus exact clock covariance in a finite setting. Basic data-processing and recovery are established quantum-information results; see e.g. [recoverability of quantum processes](https://arxiv.org/abs/2403.12947).
- [Barontini, Testing the problem of time with cold atoms](https://doi.org/10.1103/1h9j-df4k) experimentally constructs a coarse-grained entropic internal-time parameter in a partitioned Bose–Einstein condensate, reporting approximate event ordering through cycles and reproducing measured evolution with an effective equation. We previously examined it in [COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md](COLD_ATOM_ENTROPIC_CLOCK_AUDIT.md) and [COLD_ATOM_CLOCK_COMPARISON.md](COLD_ATOM_CLOCK_COMPARISON.md). Omitting it from the original roadmap and the discussion of universal clocks was an oversight: it is a central experimentally grounded example of relational time, not a test of the absolute or proof that spacetime or time is fundamentally emergent. The experiment uses laboratory timing and an entropy estimator involving whole-cloud images; its constructed clock is internal to the atomic system, not demonstrated to be autonomously readable by the bright sector alone.

These are initial collision checks, not a comprehensive review. The newest sources have only been examined at abstract/selected-section level; their assumptions, full proofs and related literature must be checked before asserting that any specific target is open or new.

## 3. An explicit operational language

For a chosen model, specify: (i) constraints and physical state space/algebra; (ii) an admissible family of physical preparations; (iii) clock effects and actual instruments, including recorded outcomes and unobserved environments; (iv) a set of accessible interventions and final effects; and (v) a common, clock-neutral prescription for the joint probabilities. Each clock description is then a representation of **a specified subset of those experiments**, not merely a relabeling of a Hamiltonian parameter.

A candidate frame-change rule must give a checkable comparison: if a particular physical preparation, interventions, records and conditioning event are represented in frames A and B, calculate the joint probability in each representation. Equality is demanded only for the same physical event with all conditioning transformed, and on the overlap where both descriptions apply. For finite resolution, keep the instrument's record and any accessible memory explicit; if it is discarded, the resulting map may be non-invertible. Conditional/postselected transformations need separate treatment because normalized conditional updates are generally nonlinear and need not be trace-preserving. Distinguish equivalence for all physical observables from equivalence only on an accessible subalgebra.

This language is a proposed test harness. Existing operational QRF and clock-switching frameworks already contain major parts of it. It is not itself a new theory and does not presuppose that all clocks admit CPTP switches, exact global frame changes, or a unique physical time.

## 4. Worked adversarial benchmark: finite-window loss

This is an application of established data-processing facts, **not a novel theorem or a quantum-gravity no-go**. In a two-level test with `H = Δ σ_z / 2`, define the completely positive trace-preserving finite-window channel

    E_T(ρ) = (1/T) ∫[-T/2,T/2] e^(−iHt) ρ e^(iHt) dt.

For the orthogonal states `ρ± = |±x><±x|`, the distinguishability `D(ρ,σ) = (1/2)||ρ−σ||₁` is 1 before averaging and `|sinc(ΔT/2)|` afterward. For **any single CPTP recovery map** R applied without a side record, contraction of trace distance and the triangle inequality imply

    max_± D(ρ±, R(E_T(ρ±))) ≥ [1 − |sinc(ΔT/2)|]/2.

For `0<T≤2π/Δ`, the sinc is nonnegative and the identity recovery attains this bound for this pair, so it is exact. At `T=π/Δ` the optimal worst-case error is `(1−2/π)/2 ≈ 0.18169`; at the full period `T=2π/Δ` it is `0.5`. [verification/time_recovery_benchmark.py](verification/time_recovery_benchmark.py) independently integrates the window and checks the numerical values; it does not prove the data-processing theorem or optimize over all channels numerically.

**Interpretation boundary:** this channel represents discarding a time label in a specified toy model. A change of relational clock is not generally this channel; a retained clock/environment record can restore information, a restricted observable set may not distinguish the two inputs, and postselection or frame-dependent subsystem identification changes the question. The benchmark tells us exactly which unsupported move to avoid: one cannot discard distinguishable information and then assume an exact, deterministic, record-free inverse for this pair. It does not establish a fundamental arrow, rule out clock changes or solve the problem of time.

## 5. Research route: combine approaches only where their interfaces are explicit

### Gate A — existing constructions and collision audit

Read the relevant proofs and hypotheses in the references above, including the 2026 intervention and finite-history papers. Compare what each constructs: physical algebra, state, clock instrument, observable family, constraint, boundary assumptions and switching map. Determine which ingredients are already equivalent, incompatible, or simply use different domains. **Stop:** a rebranding of an existing theorem is not an advance.

### Gate B — one narrow, potentially useful open target

First independently audit the existing clock-choice and turning-clock models, then investigate whether an existing model can be extended to a *specified* finite-resolution, two-clock setting with explicit interventions and operationally recoverable frame changes on a declared family of states and effects. Quantify any irrecoverable information when the reading record is discarded. Compare the answer directly with Baumann–Lock, Höhn et al., and finite-history/recovery results. The neutral theory, clock effects, instruments, conditioning and output algebras must be written before claiming an equivalence. A nonzero distinguishability loss is a counterexample to the specified record-free recovery, not automatically to a less demanding or record-preserving formulation. An exact theorem here would be a **bounded model result**, with novelty still requiring literature comparison.

### Gate C — gravitational progression

Translate any surviving statement into a concretely defined FRW model with multiple sectors or a clock turning point, handling self-adjoint domains, inner products and physical observables. Compare directly against published clock-dependent quantizations, notably [Gielen and Menéndez-Pidal](https://arxiv.org/abs/2109.02660). Then test an inhomogeneous constrained model where foliation issues actually arise. No leap from one branch to full GR.

### Gate D — lateral alternatives and interfaces

If the relational route fails, vary the target rather than declaring time impossible: retain records, restrict observables, alter the clock instrument, or investigate algebraic/crossed-product and quantum-diamond approaches. Conversely, if a modular-time proposal is used, derive the physical state/weight and clock observable and test whether the required modular action follows; do not identify it with relational time by definition. If approaches can be combined, construct explicit maps between their constraints, algebras, states and predictions. Algebraic isomorphism by itself is not operational equivalence.

### Gate E — independent validation

Challenge every claimed proof with explicit counterexamples and domain checks, independently reproduce key numerical and analytical calculations, document assumptions, search the closest literature again, and seek expert scrutiny. Predictions, analogue experiments and empirical comparisons come only after an actual operational model exists. The BEC work is an analogue-data audit, not a direct quantum-gravity test.

## 6. Where we stand

The repository's one-branch FRW mapping, its finite-window mismatch and the finite benchmark above are controlled calculations; the cited ingredients and related obstructions are established, and novelty for the specific examples is unverified. The full constraint algebra, generic clock changes, instruments/backreaction, global patching, refoliation and semiclassical spacetime reconstruction remain open. The research strategy is to reduce those gaps honestly, but neither a roadmap nor an unlimited number of turns guarantees a solution.
