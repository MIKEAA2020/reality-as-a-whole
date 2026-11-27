# The problem of time: what remains, formulated precisely

**New technical frontier:** [rigorous frontier problems](PROBLEM_OF_TIME_RIGOROUS_FRONTIER_PROBLEMS.md) gives explicit F1–F9 inputs, candidate equations, domains, success/failure conditions and a new unregulated oscillator modular–relational partial construction. The operational benchmark in this older document is one independent branch, **not** a prerequisite for every analytical or gravitational result.

**Action plan and first advance:** [divide-and-conquer plan](PROBLEM_OF_TIME_DIVIDE_AND_CONQUER_PLAN.md) sets the dependency gates; [finite-window support record](ZERO_TWO_WINDOW_REDUNDANT_FLAG_HOLD.md) implements the first bounded construction without claiming a durable autonomous reader or a clock switch.

## Direct answer

We have not solved the problem of time. We have established—in several **different, explicitly specified models**—that a vanishing constraint can coexist with real internal relational change, that certain clock choices can be compared, and that some physical-style records can be calculated. We have not shown that the same self-sufficient constitution yields the right **physical clocks, events, records, quantum probabilities, spacetime and experienced succession**, and that its clock-relative descriptions consistently refer to the same events.

The central frontier is not “how can a timeless thing be made to start moving?” That formulation already assumes an external time in which the whole must be animated. The hard question is:

> **What must the whole be, internally, for its actual ordered physical and experiential occurrences to be mutually intelligible, without an external timekeeper—and how do we prove that the different clock descriptions recover the same occurrences where their domains overlap?**

This document separates (i) a sharply testable near-term mathematical problem, (ii) the full physical problem, and (iii) the user's deeper constitutive and experiential demand. It proposes success criteria, not a claim that every viable solution must use one formalism or a universal clock. The repository's historical “closed” claim is explicitly superseded by its [evidence audit](TIME_SOLUTION_EVIDENCE_AUDIT.md) and [root-cause diagnosis](PROBLEM_OF_TIME_ULTIMATE_ROOT_CAUSE_DIAGNOSIS.md).

## 1. What the problem actually is

In ordinary quantum mechanics, a state is normally given as `ρ(t)`, with an external parameter t. In canonical general relativity, the coordinate time label is not generally a physical clock; in a closed, boundaryless constrained formulation the Hamiltonian is built from local constraints. Schematically,

```text
H[N, N^a] = ∫(N H_⊥ + N^a H_a) d³x,
H_⊥ ≈ 0,     H_a ≈ 0.
```

A formal quantum condition `Ĥ_⊥(x)|Ψ⟩=0` is only a schematic expression until operator domains, a physical inner product and the constraint representation are supplied. The constraints being zero is **not**, by itself, a proof that an invariant total cosmic energy is zero. Boundary charges can matter in noncompact or bounded settings.

A constraint generates a redundancy in the coordinate description; it does not entail that all physical correlations are constant when compared to one another. A physical question can instead be “what does field X read when clock T reads τ?” The difficulty is to construct such questions and their probabilities, and determine their relationships and limitations, in the actual theory—including quantum clock fluctuations, repeated crossings, interaction, the metric and measurement.

This is a cluster, not one theorem: frozen formalism, observables, the physical inner product, multiple clocks, local versus global time, constraint closure/refoliation, and the semiclassical spacetime limit are related but distinct. The standard review by [Isham](https://arxiv.org/abs/gr-qc/9210011) explains the global and multiple-choice problems. [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153) construct consistent clock switches for a parametrized-particle model through a clock-neutral theory; [Höhn, Smith and Lock](https://arxiv.org/abs/1912.00033) relate three relational formulations under stated assumptions. These are substantive prior results, not complete solutions for generic quantum gravity or evidence that our own models are novel.

## 2. What we already have, in decreasing order of direct relevance

### 2.1 Internal change in one actual constrained model

In the repository's [two-scalar classical FLRW model](ZERO_EXPERIENCE_INTRINSIC_IDENTITY_RELATIONAL_GRAVITY.md), the same assumed action yields

```text
C = −κ p_a²/(12a) + (p_φ²+p_χ²)/(2a³) = 0.
```

For `p_φ≠0`, define the relational observable

```text
χ_φ(τ) = χ + (p_χ/p_φ)(τ−φ).
```

`{χ_φ(τ), C}=0`, including off shell on that domain, because both fields evolve together under the constraint flow. Yet `dχ_φ/dτ = p_χ/p_φ` can be nonzero: constraint invariance and genuine clock-relative change are compatible. The model's positive local matter density and zero constraint are computed from the same action. This does **not** establish objective whole energy zero, a quantum-gravitational solution or a subject.

The meaning of clock overlap can be seen explicitly. If also `p_χ≠0`, the inverse relation on the same classical orbit is

```text
φ_χ(σ) = φ + (p_φ/p_χ)(σ−χ).
```

Set `σ=χ_φ(τ)` and obtain `φ_χ(σ)=τ`: both descriptions identify the **same event**. No external ticking process is added. At `p_φ=0` or `p_χ=0` the respective formula is not defined; extending it there requires different charts or a different description. This is a simple algebraic overlap result for two free scalars—not a quantum clock-switching theorem, nor a derivation of the scalars or initial data.

### 2.2 The project has gone beyond that example—but not yet joined every ingredient

* The [turning-clock atlas](TURNING_CLOCK_ATLAS.md) treats a repeated clock reading and retains orientation; an explicitly coarse-grained readout can lose information. The result is restricted to its fixed periodic constraint.
* The [two-window continuum construction](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md) provides full-state reconstruction from complete complex solution data on almost every **13-tuple of slices** in its stated model. The 13 is sufficient, not known minimal, and a slice signal is not an operational reading. Its [finite-interval analysis](ZERO_TWO_WINDOW_RECORDED_HISTORY_AND_FINITE_INTERVAL.md) proves an injective but compact signal map and hence an unstable inverse on the unrestricted infinite-dimensional state space. This is not a no-go for useful restricted-family estimation.
* On a specified two-packet span, the existing finite-regulator 32-outcome record is informationally complete but weakly conditioned: its smallest singular value is about `0.001432` at N=40. It requires many simulated copies for its conservative calibration bound; this is not an optimal lower bound or a continuum theorem. See [coherence and calibration](ZERO_TWO_WINDOW_COHERENCE_AND_CALIBRATION_TEST.md).
* A separate [continuum support-interaction certificate](ZERO_TWO_WINDOW_CERTIFIED_SUPPORT_COMMUTATOR.md) bounds missed/false flag probabilities below 0.0275 under a specified **changed** constraint and a global-mode coupling. It does not supply the old tomography in that altered experiment, an autonomous stopping mechanism, or a physically local implementation.
* A [classical planar-gravity evolution](ZERO_TOTALITY_NONLINEAR_GRAVITY_CLOCK_EVOLUTION.md) couples gravity, matter and a scalar clock and exhibits convergent monitored constraint residuals in a restricted numerical regime. A constant-lapse redescription check is not an arbitrary-refoliation proof or a quantum theory.
* The recent [chemistry–clock bridge](ZERO_CHEMISTRY_CLOCK_RECORD_INTERNAL_CONNECTION.md) supplies a calibrated molecular snapshot to an existing finite clock record. It uses a **fresh prescribed history per snapshot**; chemical time and the quantum clock are not a coupled time dynamics. It is therefore not the decisive time result.

These are real bounded results. Their **interfaces**—not a shortage of additional analogies—are the immediate problem.

## 3. A rigorous target for the physical facet

A solution could take several forms. Here is a **candidate sufficient benchmark** for a relational approach, not a claim that every successful theory must be Dirac quantization or admit every item globally.

### A. A defined whole and physical probabilities

Specify a physical theory: its state space or observable algebra, allowed states, constraints or equivalent symmetry principle, domains and a positive normalized probability rule for physical events. If constraints have continuous spectrum, provide an actual physical inner product or another well-defined construction; formal solutions alone are insufficient. For boundary systems include physical boundary observables and charges.

For the user's stronger foundational target, this mathematical theory must eventually be recovered from the same self-sufficient constitution rather than introduced as an arbitrary external list. For the nearer physical theorem, one may state the action, sectors and state assumptions explicitly and prove a conditional result.

### B. Clocks, events and records *within* that theory

For each clock i specify its **domain of applicability**, outcomes (including finite resolution, no reading and ambiguity), an event instrument and what information is retained. For a declared preparation ρ and a declared physical sequence of instruments `I₁,…,I_n`, a typical quantum representation should produce

```text
p(s₁,…,s_n) = Tr[I_{n,s_n} ∘ ... ∘ I_{1,s₁}(ρ)],
Σ_(s₁,…,s_n) p(s₁,…,s_n) = 1.
```

The trace/CP-map notation is a convenient benchmark when a Hilbert-space instrument representation exists, not a demand that all approaches use exactly that representation. The operations and their physical ordering must themselves be justified by the model: merely writing the list does not explain how they are triggered without an external schedule. Include the clock, detector, reference, memory and relevant backreaction or quantify an approximation. A no-click outcome cannot be equated to no crossing without an additional crossing theorem.

### C. Same event, different clocks

For two clocks A and B, identify a common domain of states and **the same physical preparation, interventions, records, conditioning event and final event**. The benchmark is equality of their joint probabilities after the full transformation:

```text
p_A(s₁,…,s_n, d) = p_B(transported s₁,…,s_n, transported d).
```

For conditioning on d, the denominator must be nonzero in both descriptions. Different numerical clock readings or different interventions need not have the same probability. The map may act on clock, system, reference and records jointly; it need not be a unitary on a fixed system tensor factor, or even exist outside a stated sector. A pullback of a single given theory proves a consistency property of that representation; it does **not** by itself prove independently quantized reduced theories are equivalent. Conversely, showing two formulations differ with mismatched boundary conditions or different physical experiments does not by itself prove clock-choice inconsistency.

At turning points or repeated readings, state whether orientation, event records or another clock are retained. Define transition rules on overlaps and check their composition around loops where applicable; a nontrivial physical holonomy must not automatically be called an inconsistency. Explicit no-reading/out-of-domain outcomes are better than silently renormalizing them away. A single global monotonic clock is **not required**.

For approximate comparisons the question must say how errors and conditioning interact. For example, if two joint distributions differ in total variation by at most `ε` and both assign conditioning event d probability at least `κ>0`, then their conditional distributions differ by at most `min(1,2ε/κ)`. A rare conditioning event can therefore make a small joint error operationally large. A statement that clock pictures are “close” without a domain and a conditioning bound is not yet a usable equivalence.

### D. Gravity, refoliation and spacetime

In the standard ADM route, the classical normal-deformation brackets include, schematically and with convention-dependent signs,

```text
{H[N], H[M]} = D[q^{ab}(N∂_b M − M∂_b N)].
```

The metric-dependent coefficient is a structure function, not a fixed Lie-algebra constant. To claim canonical general covariance one needs appropriately defined quantum counterparts, domains, regulator removal or controlled approximations, and a demonstration that physically equivalent deformations give consistent predictions. Mere algebraic closure is not automatically enough to reconstruct the standard spacetime geometry, and no particular operator ordering is assumed here. An alternative approach can use other structures, but it must demonstrate an equivalent, empirically adequate account of local covariance and causal structure rather than be rejected for not using ADM.

Derive a semiclassical regime with operational proper-time comparisons, relativistic local dynamics and specified errors; do not assume a background metric and then cite it as emergent. Demonstrate empirical consistency at accessible scales and identify discriminating consequences where available. This is a physical recovery criterion, not necessarily a demand that solving this one facet first prove a complete ultraviolet theory.

### E. Arrow and lived succession

Order, an entropy/record arrow and experienced succession are **different** claims. A clock atlas or stationary correlations can have order without explaining why durable memories predominantly point one way. An arrow account needs explicit state/boundary conditions, coarse-graining and record dynamics; time-reversal-symmetric laws or a bounce alone do not prove it.

For the user's full intelligibility objective there is a further obligation: identify the actual organized occurrence and subject for whom succession is lived, and show how its physical–relational and experiential aspects are the **same occurrence** in the intended noncausal sense. First-person acquaintance is evidence from within reality, not a second substance and not wholly reducible to words. An ordered pointer sequence does not establish a subject, or an experienced present. Conversely, this experiential obligation is not a prerequisite for a narrowly stated mathematical theorem about a quantum clock.

## 4. The strongest specific near-term problem

The most productive next theorem is not “solve full time in one step,” and not “add another detached clock.” It is this **precise open benchmark**, built from the existing two-window model:

> **Operational clock-switch benchmark.** On one explicitly specified interacting constrained theory that includes clock, geometry, physical detector and memory, construct an autonomous finite-resolution event instrument, including no-reading and repeated-reading outcomes, and two genuinely distinct clock descriptions. On a nonempty specified overlap, transport the same preparation, whole instrument and conditioning event, retaining all sectors and records. Prove a uniform bound `TV(p_A,p_B)≤ε_switch` for a declared accessible family and finite resources, or exhibit a concrete pair of descriptions/events for which the stated equivalence fails. Provide a controlled continuum limit and separate statistical, approximation and implementation errors.

To be nontrivial, at least one clock must be more than the same scalar checkpoint written in another basis; the readout must be generated by the specified apparatus, not inserted by an external timetable. The theorem may be local in clock space and may have a no-reading outcome. It need not show equivalence of every possible quantization. An explicit counterexample, if its operational events really match, is progress because it pinpoints the failed premise.

**Why this benchmark is not already complete:** the 13-slice theorem and history transport use ideal complete complex signals and pullbacks of the same prescribed scalar-checkpoint instrument. The certified support flag is instead generated by an altered constraint, requires a global packet projector and is not durable; it cannot simply be substituted into the old instrument. The two results therefore cannot be added as if they described one implemented experiment.

### A quantitative hurdle in the existing ingredients

The certified altered-constraint flag gives, for its declared comparison and `λ=Tr(Qρ)`,

```text
sqrt(λ) ≤ min[1, sqrt(q) + D_*],
D_* = 50699/305760 ≈ 0.1658131,
```

where q is its actual flag probability. A statistical upper bound `q_U` may replace q with its own confidence allocation. For the earlier **illustrative simulated** result `q_U<0.019485`, the certificate gives `λ<0.094`, hence a conservative projection trace-distance bound below about `0.307`. It is not a measured result, a lower bound on actual error, or proof that a better detector cannot exist.

If one could legitimately combine a support bound with a **separately calibrated** qubit-tomography radius R for the same reproducible preparation and fixed logical-sector assumptions, and all target-procedure errors were bounded by η, then the standard trace-distance/data-processing estimate would give, on the joint confidence event,

```text
TV(target actual, target predicted) ≤ min[1, sqrt(λ_U) + R/2 + η].
```

This includes coherent leakage when `λ_U` is justified. However, R must include contamination of tomography data by outside support and calibration uncertainty; the flag and tomography protocols may use separate identically prepared copies, but their differing constraints and preparation/transfer maps must be physically and mathematically justified. No such combined R has been established for the present continuum instruments. Probabilities of successful calibration and support inference require a union-bound confidence budget.

As a **sufficient-certificate** target, even with ideal tomography and no systematic error, the available universal bound has floor `D_*≈0.166` when `q_U→0`. Therefore this particular combination of inequalities cannot certify a worst-case TV error below 0.1. A better bound, detector, prior restriction or entirely different proof could do so; this is **not** an impossibility or a necessary lower bound. The old 32-outcome instrument's weak singular direction makes unbounded support or calibration errors especially costly. Exact analytic invertibility without a stable operational norm does not remove that issue.

A concrete next construction should therefore do at least one of the following, without hiding the other burdens:

1. construct an autonomous switching/stopping/readout mechanism on the **same** altered constraint and prove how it affects support and original records;
2. prove a sharper, state-uniform continuum support/implementation bound on a justified preparation family, accounting for coherent leakage and confidence;
3. construct a real operational geometry-triggered instrument, compare its **same** events in two clock descriptions, and bound all failure outcomes; or
4. prove that the desired specification cannot be met under explicitly stated restrictions and identify the least costly assumption to relax.

A theorem meeting that benchmark would be a significant **bounded** advance. It would still not prove full general relativity, the actual universe, or a unique constitutive explanation.

## 5. The deepest remaining question for this framework

The user asks for the strongest zero–identity account, not an indefinitely extended chain of toy mechanisms. Let `Z` denote the not-yet-specified adequate **physical–experiential constitution of the whole**, not merely the scalar equation `0=0`. A full answer requires a precise claim of this shape:

```text
Z, by its own constitution
   ⇒ a definite physically adequate relational state/observable structure,
   ⇒ applicable clocks, causal/record relations and their mutually consistent descriptions,
   ⇒ actual subjects and their experienced temporal occurrences,
```

with the arrows understood as **constitutive entailment**, not necessarily stages in an external time or separate causes. One must specify exactly what Z is, prove the relevant implications and recover the actual empirical/experiential facts with no extra unexplained selection. The entailment must not be achieved by defining Z to contain every desired conclusion without explaining why that constitution is necessary and actual.

An SR analogy is useful in the precise sense the user emphasized: length contraction follows from a rod's worldtube, Minkowski geometry and simultaneity, without a separate squeezing force. Analogously, a successful theory might show internal order and experience as necessary features of the whole's constitution, not produced by an external clock. The present models demonstrate **possible pieces of that form**; they do not yet provide the corresponding necessity proof for physical time or experience. Mathematical representation, actuality, physical empirical agreement and first-person identity are connected explanatory tasks, but should not be conflated.

In particular, we have not shown that the choice of physical algebra, constraint, initial/physical state, factorization, causal orientation, probability rule, record dynamics or subject-incidence follows uniquely—or follows in an adequately grounded nonunique way—from Z. Nor have we established the physical whole-energy concept to which a necessary zero would apply. Those missing derivations are research targets under the user's full-intelligibility principle, not a proposal to settle for unexplained residues.

## 6. What would change the verdict?

**A bounded result becomes a real advance if:** it specifies a single interacting theory and its domain; constructs the instruments instead of merely naming them; proves or tightly bounds same-event clock agreement, including failures and records; demonstrates stability and continuum control; and survives an adversarial, prior-art and independent mathematical check. A counterexample to those requirements under a precise set of assumptions is also informative.

**A full physical solution** would additionally recover local quantum and gravitational physics, consistent clocks and causality across relevant regimes, and the empirical classical limit. Whether it also needs a full UV completion depends on the claim's scope.

**The user's full solution** additionally needs the noncausal constitutive derivation and the anchored identity of lived succession with the appropriate organized occurrence. An explicit conditional mathematical model is not yet that derivation; nor does its incompleteness show the aim is impossible.

## Checks and source boundaries

The sources linked above are existing model results and selected scientific references, not an exhaustive review of ongoing research. In particular, recent [clock-neutral switching](https://arxiv.org/abs/1810.04153) and [relational dynamics equivalence](https://arxiv.org/abs/1912.00033) precede this formulation; the 2025 [quantum-diamond proposal](https://arxiv.org/abs/2504.00152) explores a different route and is a proposal, not a universally established resolution. No novelty claim is made for the individual criteria, concentration bounds or trace-distance inequalities.

Selected underlying checks can be rerun with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_intrinsic_identity_relational_gravity_test \
 verification.zero_two_window_commutator_certificate_test \
 verification.zero_two_window_coherence_tomography_test \
 verification.zero_two_window_full_slice_test -v
```

The exact-rational certificate is a proof check under its stated operator assumptions; the tomography and full-slice tests include finite-regulator controls and do not by themselves prove their continuum claims or physical implementations. The multi-clock overlap identity in §2.1 is an elementary consequence of the displayed formulas, on the stated nonzero-momentum domain.
