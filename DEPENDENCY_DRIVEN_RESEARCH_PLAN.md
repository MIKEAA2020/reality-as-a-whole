# From what we have to what we need: dependency-driven work register

> **Historical endpoint:** The universal-subject formulation below predates the plural-subject reassessment and nonliteral Bostrom clarification. The [current consolidated dossier](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) supersedes conflicting statements; individual dependency gates remain scoped research tasks.

**Purpose:** replace large jumps between demonstrations with small, checkable obligations that can be completed or failed independently. The [global coherence and decision plan](GLOBAL_COHERENCE_AND_DECISION_PLAN.md) explains how these obligations connect to one candidate, its experiential and physical interfaces, empirical constraints, failure criteria, and the intended endpoint. The user's intended endpoint remains a timeless, self-sufficient absolute, no fundamental mass or spacetime, experience as intrinsic nature, possibility/actuality and essence/existence identities, one universal consciousness, and an intelligible account of simulation without requiring an external simulator. These are goals and governing commitments, **not established conclusions**.

This is a work register, not a certificate that the goals are achievable. It distinguishes established mathematics, results already checked in restricted models, claims that still require audit, and open research problems. Numerical checks validate declared computations, not their physical or experiential interpretations. [Earlier unsupported closure claims remain retracted](ZERO_RESIDUE_CLAIM_CORRECTION.md).

## 1. The dependency structure

The project needs several mutually constraining tracks; one must not be used as a substitute for another.

    P: specified ontology / necessity / actuality
    X: experiential incidence, quality, unity and finite perspective
    Q: states, observables, instruments, records and quantum references
    L: local fields, causal dependence, regulators and continuum limits
    G: dynamical gravity, constraints, clock/rod backreaction and refoliation
    E: emergent geometry, matter dynamics and empirical limits
    S: simulation, conditional observer weighting and explanation without an external base

`Q + L` are prerequisites for operational local measurement; `Q + L + G` are required for the chosen gravitational time test. `E` requires appropriate physical structures and recovery maps, not simply a label attached to an order. `P` and `X` have their own logical and empirical burdens; they neither follow automatically from `Q/L/G/E` nor establish them by philosophical stipulation. `S` depends on the actual theory's ontology and, for probabilistic claims, a defensible observer measure. These arrows are research dependencies, **not** a claim that existence is temporally produced in stages.

We will not wait for one entire track to finish before thinking about the others. But every claimed bridge must name its source object, target object, map, assumptions, and what is preserved or lost.

## 2. Shared rules for each small task

For every task below record:

1. **Input:** exact prior result, state, action, event and regime; audit it before reuse.
2. **Claim and domain:** a single mathematical or empirical statement, not a metaphor between frameworks.
3. **Method:** published theorem with its hypotheses, or a new derivation and verifiable calculation. Check close prior art before asserting novelty.
4. **Acceptance:** an equation, bound, complete outcome distribution, reproducible test or evidence threshold; include units and explicit quantifiers.
5. **Adversary:** a counterexample, control, alternative interpretation or failure mode.
6. **Status:** established result / checked special case / conditional argument / untested hypothesis / blocked. A failed task stays visible and changes the next step.

The provisional numerical tolerances below are **engineering test thresholds**, not empirically justified constants or fundamental limits. Change them explicitly, not after looking at results. Never infer a theorem from a finite sample, or a local/physical observable from a coordinate label.

## 3. Immediate critical path: one local record coupled to gravity

### L1. Reproduce the specific cutoff failure — DONE, restricted

- **Input:** [the common cutoff and two-record test](CROSS_FRAMEWORK_CAUSALITY_RECORD_TEST.md), a 1D transverse collective sector, supplied equal slice, specified Gaussian state and triangular smears.
- **Deliverable:** full joint record distributions, overlap, source energy, sine-inclusive control and analytic tails.
- **Acceptance:** exact continuum disjoint-support commutation; finite N result and convergence documented.
- **Result:** N=4 gives ordering TV `0.04960`; this is a projected-operator artifact, not real superluminal communication or nonlinear refoliation.
- **Remaining:** this is not the full 3+1 probe, not the prior 71.67% experiment, and not a state-independent locality bound.

### L2. Select a cutoff from simultaneous probability and energy tolerances — DONE, restricted

This step is new relative to the earlier locality note and turns a qualitative refinement claim into a predeclared acceptance rule.

- **Input:** exactly L1's fixed smears, source amplitude, initial Gaussian, equal-slice two-bit instrument and bit-noise channel; do not change the operation with N.
- **Targets:** ordering TV <= `1e-4` and source-energy error <= `0.1` in the declared dimensionless 1D units.
- **Proof ingredients:** for `d=0.4`, `g=1`, `q=0.1`,

      |kappa_N| <= 16/(3 pi d^4 N^3),
      |E_infinity-E_N| <= 8 g²/(pi d^4 N),
      TV_order <= (1-2q)|g| |kappa_N|.

  The last line follows from the exact Gaussian sign-readout formula, `erf(x)<=2x/sqrt(pi)`, and this state's `V_N>=1/(2pi)`; it is **not** uniform over arbitrary preparations, readout instruments or states.
- **Result:** the probability certificate alone requires `N>=81`; the energy certificate alone requires `N>=995`. Taking `N=995` satisfies both sufficient bounds: TV <= `5.39e-8`, energy error <= `0.09998`. Direct finite sums give approximately `3.80e-11` and `0.03758` respectively. [Verifier](verification/refinement_acceptance_budget.py), [output](verification/refinement_acceptance_budget.json).
- **Adversary:** N=4 fails the selected probability target; the table in L1 is nonmonotone. The bounds are conservative, so this does **not** prove that N<995 is physically inadequate or that 995 is the minimum true cutoff. Numerical evaluations are floating point, not interval certificates.
- **What it buys:** a repeatable *joint* accuracy contract for one source/readout comparison. It is not convergence of the complete quantum channel or stress tensor, a 3+1 QFT result, a physical probe, or a metric-error bound.

### L3. Upgrade one probability to an instrument — PARTIAL; next executable task

- **Depends on:** L1–L2. Retain both record bits and all four outcomes, plus the post-measurement field state, for the same smears and source—not just the single TV number.
- **Substeps:** (a) write both ordered CP instruments on the same algebra and identify their outcome effects; (b) choose a nonselective and a selective comparison separately; (c) choose a physically bounded class of input states or a specified state family; (d) derive an error bound for every outcome and for accessible post-states; (e) include a counterexample showing why one-state probability convergence does not imply diamond-norm convergence in an unbounded field theory.
- **Progress:** [Explicit four-outcome maps, L3(e), and energy-bounded estimates](CUTOFF_INSTRUMENT_UNIFORMITY.md): squeezed inputs distinguish ideal ordered channels nearly perfectly at every nonzero overlap, but require unbounded energy as overlap vanishes. For arbitrary field inputs with retained kinetic energy <=100, including reference entanglement, the unhalved energy-constrained diamond distance between the full two ordered finite-N instruments is <=`.01` for all N>=722, using a conservative bound. This includes retained field and records but **compares two orders at each N**, not either with a continuum instrument. Established channel-norm and analysis methods are cited/not claimed as novel; the local-probe and total-apparatus energy remain missing.
- **New restricted progress:** [Common-Fock-space continuum comparison](CONTINUUM_COMPLETE_INSTRUMENT_CONVERGENCE.md) now gives an all-outcome, retained-field and reference-inclusive bound for both cutoff orders against the continuum instrument in the stated 1D even-cosine free-field model, using a common **normal-ordered oscillator-energy constraint** and an explicit zero-mode regulator. It does not establish convergence for the earlier kinetic-only class or a physical probe; a sharp measurement may have infinite output energy. This is a restricted L3 subproblem result, not full continuum QFT or gravity.
- **Acceptance still outstanding beyond that model:** justify the common energy domain physically and extend to a local 3+1 probe with apparatus costs, and address the earlier kinetic-only class if that class is required. No unrestricted diamond-norm convergence claim. If no appropriate uniform bound is possible, report the exact restricted statement or counterexample.

### L4. Replace instantaneous field operations with a local probe — BLOCKED on L3

- **Substeps:** (a) take a cited, fixed-background field/probe measurement construction, such as [Fewster–Verch](https://arxiv.org/abs/1810.06512); (b) specify compact smooth spacetime switchings and probe initial state; (c) derive the induced effect and complete instrument, including failed/no-click outcomes; (d) establish the causal-separation condition; (e) calculate a nontrivial finite-duration benchmark and check any approximation against a limiting case.
- **Acceptance:** an actual source/probe action and same-event probabilities, with a stated support region and no hidden globally accessible zero-mode memory. A sharp field projector or a gate written by fiat is not sufficient.

### L5. Carry the benchmark to the intended dimension — BLOCKED on L4

- **Substeps:** (a) restore all spatial directions and both sine/cosine modes; (b) define the same physical smears under refinement, with physical volumes and dimensions; (c) redo probability and source-energy bounds; (d) check timelike, spacelike and null-near controls; (e) compare cutoff dependence with known 3+1 detector literature.
- **Acceptance:** a controlled 3+1 fixed-background result with both a causal leakage tolerance and an independently specified source/probe energy criterion. L2's 1D numbers cannot be reused as 3+1 bounds.

### G1. Pick a documented gravitational model and boundaries — OPEN; parallel literature audit

- **Substeps:** (a) compare the prior [smooth Einstein–matter clock](SMOOTH_FIELD_CLOCK.md), the [clock–rod scalar action](RELATIONAL_MATTER_DETECTOR_GRAVITY.md), and established discrete/continuum approaches; (b) independently recheck the reusable action, sign conventions, boundary terms and claimed domains; (c) decide compact torus versus asymptotically flat boundaries with an explicit reason; (d) state what is classical, perturbative, regulated or quantum.
- **Acceptance:** a cited action and complete canonical variables including source, clock, rods, probe, reference and memory. The compact flat torus needs the [integrability obstruction](TORUS_SECOND_ORDER_GRAVITY_MATTER.md); a point particle needs a singular-source prescription. No historical claim is inherited automatically.

### G2. Establish admissible initial data and local constraints — BLOCKED on G1

- **Substeps:** (a) derive all matter momenta and stress sources; (b) construct nontrivial constraint-satisfying data, including detector/clock resources; (c) treat global charges, boundary terms and zero modes; (d) independently check H–H, D–H and D–D brackets, plus mixed terms; (e) test off-shell configurations, not only one solution.
- **Acceptance:** a stated classical theorem or controlled approximation with all three constraint brackets, not just the Abelianized linear constraints. If a discrete regulator has a defect, specify it and the claimed refinement limit.

### G3. Relational event and clock calibration — BLOCKED on G1–G2

- **Substeps:** (a) specify clock and rod fields with finite-resolution effects; (b) identify invertible regions, turning points and branch labels; (c) define one interaction and one readout by values of these fields; (d) prove the same physical event is represented after a coordinate/gauge change; (e) include calibration states and their energy.
- **Acceptance:** no reliance on a globally monotonic clock or a fixed coordinate point; all conditioning events and records are transported. A coordinate order, a global external clock, or matching only marginal clock values fails this gate.

### G4. Control evolution and backreaction — BLOCKED on G2–G3

- **Substeps:** (a) solve or bound the coupled detector, control and gravitational evolution over the actual window; (b) specify the renormalization and state if using quantum stress-energy; (c) control constraint violations and physical metric/clock error on a stated class of states; (d) compare with the fixed-background calculation; (e) include preparation, switching, record persistence and readout costs.
- **Acceptance:** an error bound on observable probabilities or a defensible self-consistent solution, not merely a ratio of bare field energy to a background integral. If backreaction invalidates the protocol, change the protocol rather than claim it is negligible.

### G5. Compare two deformations of the same experiment — BLOCKED on G3–G4 and L5

- **Substeps:** (a) choose two lapse/shift paths with the same relational endpoints and physical boundary data; (b) evolve the same state, source and complete instrument along both; (c) quantify the constraint or discretization defect; (d) compare full joint outcome distributions and accessible conditional post-states; (e) demonstrate refinement or bound a nonzero remainder.
- **Acceptance:** an explicitly controlled same-event comparison. Equal-slice commutation or two different preparations are not a refoliation test. A finite witness is not an anomaly-free operator proof.

### G6. Quantum constraints and time — RESEARCH GATE, not scheduled as routine

- **Substeps:** specify the constraint operator/algebra and domains; construct or justify physical states and observables; examine anomalies and physical inner product; transport instruments between clock descriptions on their common domains; establish a classical limit and compare with prior clock-switching results.
- **Acceptance:** the relevant claim must survive all stated hypotheses and independent scrutiny. Failure here remains an open physics problem; L1–G5 do not automatically resolve it. Barontini's [cold-atom clock](COLD_ATOM_CLOCK_COMPARISON.md) remains a separate experimental comparison, not evidence of gravitational constraint closure.

## 4. Geometry, experience and actuality: small tasks that cannot be skipped

### E1. Geometry from a single common structure — OPEN

1. Declare the candidate's events, causal relation, region inclusion and context category separately.
2. Define order-to-geometry map and calibration/volume data; test relabelling invariance.
3. State refinement maps, limits and regularity; test a non-manifoldlike counterexample.
4. Recover a metric and matter propagation on the same states; test dynamics, not just cone analogy.
5. Compare to GR/QFT and observations in their applicable regimes.

Existing [order reconstruction](research/order_reconstruction/REPORT.md) and [refinement completion](research/refinement_completion/REPORT.md) are conditional examples, not this derivation.

### X1. Experiential incidence and quality — OPEN

1. Fix a specific, independently described physical process and a specific phenomenal contrast; do not start by assigning experience to an algebra.
2. Define competing constitution hypotheses that genuinely differ and a reference/evidence procedure that could separate them.
3. Audit measurement error, report, access and confounds; do not treat an instrument outcome as infallible experience.
4. Test preservation and disruption cases; state when a failure rejects the proposal rather than adding an ad hoc selector.
5. Explain unity, finite ownership and qualitative character, not merely transport of information.

The existing [reference case](REPORTED_CONTENT_REFERENCE_CASE.md), [identifiability audit](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md) and [rival comparison](MAINTAINED_DISCLOSURE_CANDIDATE.md) supply partial inputs, not a demonstrated consciousness law. The [one-whole finite-access test](ONE_WHOLE_FINITE_ACCESS.md) derives operational scope from a declared causal model and audits a real no-report experiment against the frozen contrast; the physical-to-phenomenal and calibration bridges remain open.

### P1. Necessary actuality and modal identity — OPEN

1. State the modal logic and meanings of possibility, actuality, essence and existence without embedding the conclusion as an axiom.
2. Separate the fact of present experience from the stronger necessity of concrete actuality.
3. Build countermodels distinguishing a consistent description, an actual occurrence and a necessary occurrence.
4. Identify the exact additional premise that eliminates each countermodel; justify it independently or mark the inference as conditional.
5. Test whether a single experiential absolute and finite distinctions follow without an unexplained selector. Check the perfection/suffering problem separately.

An inability to speak from an absolute nothing state does not by itself prove that nonbeing is impossible. The [truth-grounding analysis](NOTHINGNESS_TRUTH_AND_EXPERIENTIAL_NECESSITY.md) gives a valid conditional route to necessary experience, identifies its disputed load-bearing premise, and separates necessary experience from a necessary universal subject and sector plenitude. This track must not cite stipulated Boolean flags as evidence.

### S1. Simulation without an external base — OPEN

1. Distinguish a literal simulator hypothesis from a timeless internal-description interpretation.
2. Specify which physical/experiential implementation, if any, makes the description concrete.
3. State what observer population and measure are required for a probabilistic simulation claim; examine infinite-measure and reference-class failures.
4. Compare the hypothesis with a non-simulation account on predictions and explanatory premises.
5. Do not infer actuality, a probability or experience from a short program alone. The [simulation audit](SIMULATION_ZERO_RESIDUE_ATTACHMENT_AUDIT.md) gives the current constraints.

## 5. How to avoid repeating the previous failure

- **Next action:** assess the physical status and limitation of the [new common-space L3 comparison](CONTINUUM_COMPLETE_INSTRUMENT_CONVERGENCE.md), including its changed oscillator-energy constraint and sharp-measurement infinite-energy issue, and pursue an actual local probe before extending to 3+1 and gravity. Four CP maps, an unrestricted-norm counterexample, a fixed-cutoff order bound, and restricted common-space cutoff-to-continuum bounds are now available. In parallel develop M0/M4's candidate-and-rival sheet under the [global plan](GLOBAL_COHERENCE_AND_DECISION_PLAN.md). Do not jump straight to a new gravitational toy model.
- In parallel, G1 can be researched without pretending L3–L5 are finished.
- Every later report must point to the exact task it closes, the task(s) it unlocks, and the assumptions it does not close.
- Periodically re-audit whether these tasks actually serve the endpoint. Passing a long list of isolated checks is not equivalent to a solution, and no timeline or guaranteed completion is asserted.
