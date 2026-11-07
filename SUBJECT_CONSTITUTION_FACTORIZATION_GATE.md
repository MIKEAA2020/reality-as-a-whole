# Subject constitution: factorization, representation and symmetry

**Status: finite mathematical gate and explicit rival hypotheses; not a discovery of subjects or a completed v2 framework.** This extends the existing [ties, persistence and redescription gate](SUBJECT_TIES_PERSISTENCE_REDESCRIPTION_GATE.md), rather than replacing it. The goal is to identify what a subject-constitution proposal must supply before it can ground the framework's subject measure or its empirical claims.

## 1. The step forward

A rule that counts subjects by looking at the *written coordinates* of a model can change its answer when exactly the same system is redescribed. Instead, a proposed rule should operate on physically meaningful observables and operations, carried across the redescription. But that requirement alone does not always select a unique decomposition: the fully symmetric finite system below has three equally eligible decompositions even when the complete state-transition kernel and a rich family of interventions are specified.

There is also a positive result. A concrete **factorization gate**, defined below, identifies one decomposition in an asymmetric model and follows it correctly through a nontrivial mixing of coordinates. The selected factors are candidates for a constitution rule, **not themselves a proof of subjects**. A distinct experiential premise and independently anchored tests are still required.

Prior work already recognizes the dependence of subsystems on observables and operations. Zanardi's [Virtual Quantum Subsystems](https://doi.org/10.1103/PhysRevLett.87.077901) analyzes operationally induced subsystem structure in quantum theory; the finite example below is classical and is not a derivation of that result. [Massidda et al.](https://proceedings.mlr.press/v213/massidda23a/massidda23a.pdf) study state and intervention maps in causal abstraction, including hard and soft interventions. We use a simpler explicit **invertible** transformation, without claiming to reproduce their framework or its theorems. [IIT 4.0](https://doi.org/10.1371/journal.pcbi.1011465) has its own intrinsic-causal and exclusion postulates; recent [intrinsic-unit work](https://www.biorxiv.org/content/10.1101/2024.04.12.589163v2.full) addresses grain selection. Our factorization gate is neither IIT nor a test of IIT.

## 2. Input, candidates and a precise diagnostic

Let the complete state space be `Ω={00,01,10,11}`. An input consists of a transition kernel `K(s,t)` and a specified family of admissible state operations and readouts. This is an internal ordered-step model, not an external clock or a model of the entire universe.

A binary observable is a map `f: Ω→{0,1}`. Here consider **balanced** observables: two states yield each value. Swapping the output labels does not change the observable's partition of the states. There are exactly three such partitions:

```
X: x                  Y: y                  Z: x XOR y.
```

Any distinct pair, `XY`, `XZ`, or `YZ`, gives a bijection from `Ω` to two bits; call such a pair a **complete binary factorization**. The restriction to exactly two balanced binary factors is a deliberately chosen test domain, not a theory of what factors or subjects must be.

### Candidate gate G: independent local factors

For a complete pair of observables `(f,g)`, accept its factorization if, for every initial state `s` and final state `t`,

```
K(s,t) = K_f(f(s), f(t)) K_g(g(s), g(t)),
```

where `K_f` and `K_g` are stochastic binary kernels. This requires both (i) conditionally independent next-factor values and (ii) each factor's transition law depending only on its own current value. The verifier obtains the two marginals and checks both conditions exactly. It enumerates **all** three eligible factorizations, rather than assuming the coordinate axes are privileged.

The gate tests a dynamically autonomous product structure. It is not a direct test for experiential unity: an independent factor may be unconscious, and an interacting, integrated subject need not factorize internally. A candidate extension might use autonomous factors to separate noninteracting regions and then apply a different, independently justified *within-factor* constitution rule. It must also specify how the subsystem candidate space and physically admissible operations are chosen, how coupling and external context affect the rule, and how the rule handles time grain, persistence and phenomenal content.

## 3. A constructive redescription check

Let `x` and `y` undergo independent binary flips, with probabilities `p=1/4` and `q=1/3` respectively:

```
x' = x XOR E_x,     y' = y XOR E_y,
P(E_x=1)=1/4,       P(E_y=1)=1/3,
E_x and E_y independent.
```

The kernel satisfies G for `XY` and for **neither** of `XZ` or `YZ`. Thus G selects the single decomposition `XY` in this finite model. It does not follow that the factors are subjects, or that this is the unique correct selection criterion.

Now make the bijective change of description

```
u = x,        v = x XOR y,        so x=u, y=u XOR v.
```

The physical transition kernel is transported through this bijection. In the new notation the same selected factors are **`u` and `u XOR v`**, not the two written coordinate axes `u` and `v`. Indeed, conditional on the starting state, the new-coordinate flip indicators satisfy

```
P(Δu=1, Δv=1) = 1/6,
P(Δu=1) P(Δv=1) = (1/4)(5/12) = 5/48.
```

The increments are correlated, even though the original `x` and `y` factors evolve independently. A coordinate-axis-only rule would miss the original factorization after the change; G recovers the transported factors. The verifier also checks G's equivariance under **all 24** bijections of the four-state space for this model.

### Interventions must be transported too

A change in notation does not make a new independent control operation available. Write an original clamp as `x→a` and/or `y→b`, with unclamped values left unchanged. In `(u,v)` notation, decode `x=u, y=u XOR v`, perform the original clamp, then re-encode. For example:

```
do(x=a), leave y unchanged:   (u,v) → (a, a XOR u XOR v)
do(y=b), leave x unchanged:   (u,v) → (u, u XOR b).
```

Neither should be silently replaced by a native single-coordinate clamp in the new representation. All nine combinations of unclamped, zero and one for the original two coordinates and all four starting states are checked, along with the transported transition probabilities. The general lesson is conditional: if a proposed bijection preserves the actual observables and interventions *with their meanings*, equivalent descriptions must agree. A mixing that fails to preserve physically relevant locality, intervention costs or a distinguished observable algebra need not be a physical equivalence at all.

## 4. Approximate recovery under an explicit error budget

Exact factorization is too brittle to apply directly to noisy data. For each candidate factorization `F=(f,g)`, define a defect `D_K(F)` as the larger of:

- the maximum, over starting states, of the total variation distance between the next-state distribution and the product of its `f` and `g` marginals; and
- the largest total variation difference between `f` marginals at two starting states with the same `f` value, or between `g` marginals at two starting states with the same `g` value.

Thus `D=0` exactly when G holds in this finite domain. The exact defects for the asymmetric example are:

| Factorization | Defect |
|---|---:|
| `XY` | `0` |
| `XZ` | `1/8` |
| `YZ` | `2/9` |

Suppose an estimated kernel `K̂` is within `ε` of the true kernel in total variation **for every starting state**. Marginalization cannot increase total variation, and the distance between two product measures is at most the sum of the distances of their factors. It follows by the triangle inequality that the product defect changes by at most `3ε`; the locality defect changes by at most `2ε`. Consequently `|D_K̂(F)−D_K(F)| ≤ 3ε` for each fixed candidate. The smallest-defect rule therefore still picks `XY` uniquely whenever `ε<1/48`: its estimated defect is at most `3ε`, while either rival's is at least `1/8−3ε`.

An illustrative **sampling-only** bound makes the assumptions explicit. If each of the four starting states can be prepared exactly and gives `n` independent draws from its row of the kernel, simultaneously estimate the 16 transition probabilities by their frequencies. Hoeffding's inequality and a union bound give all entrywise errors at most `1/192` with probability at least 95% when `n≥119,098` **per starting state**. Then each row is within TV `1/96`, which is below `1/48`, so the true factorization is selected with at least that confidence under the ideal model. This is a deliberately conservative sufficient bound, not a human sample size, observed data, or a claim of optimality. It excludes preparation error, hidden variables, nonstationarity, serial dependence and intervention disturbance; any such effects must be included separately in a real error budget. The inequalities use standard [Hoeffding bounds](https://doi.org/10.1080/01621459.1963.10500830), not a new concentration theorem.

This quantitative margin shows what would make **this model's physical factorization** recoverable under bounded error. It does not turn factorization into consciousness, and a model with closer defects may require much stronger evidence or be exactly ambiguous. The code checks the exact defects and their invariance under all 24 state permutations; the analytic error and sampling bounds are separate arguments.

## 5. The symmetry obstruction: a finite no-go

Set `p=q=1/2`. Then `K(s,t)=1/4` for every pair of states. G accepts **all three** complete binary factorizations. Give the system all 256 deterministic state-to-state operations as admissible interventions, with complete state readout, but supply no additional privileged labels, costs, locality or intervention classes. On changing state labels by a permutation `π`, transport every operation `a` to `π∘a∘π⁻¹`, and transport readout labels accordingly. This is a symmetry of the entire stipulated input; the code checks all `24 × 256 = 6,144` permutation–operation pairs and all state/outcome cases.

The 24 state permutations act transitively on the three factorization candidates. Suppose a rule:

1. receives only this specified unlabeled kernel, operation family and readout structure;
2. must output exactly **one** of the three complete binary factorizations;
3. is deterministic and equivariant under all input automorphisms.

No such rule exists. An automorphism of the input must leave its output fixed, but the three factorizations form a single orbit and none is fixed by every automorphism. If the output is instead a **set** of eligible factorizations, the only invariant possibilities are the empty set or all three. Returning all three transparently represents ambiguity; it does not assert that six subjects exist.

This is a finite obstruction to *that exact combination of inputs and demands*. It does **not** prove that physical subject boundaries are in general unidentifiable, that real brains have this symmetry, or that a universe has no additional subject-making facts. The exact uniform kernel is also memoryless; it is used to expose a structural ambiguity, not as a plausible experiencer.

A subject rule could respond by:

- adding and justifying asymmetry, local mechanism, intervention cost, or a physically distinguished observable structure;
- returning underdetermination where the data have an exact symmetry;
- changing what it means to count or individuate subjects; or
- introducing an independently justified experiential constituent not reducible to this input.

Each is a substantive choice. If the theory assumes a fixed physically privileged factorization at the outset, the no-go does not apply—but neither does it explain why that factorization is privileged. Nor can the theory claim full redescription invariance while comparing different, untransported intervention sets.

## 6. Two rivals on one model

To expose the phenomenal bridge, hold fixed the asymmetric kernel, all stated operations and the same operational readouts, then compare:

- **Factor-subject hypothesis F:** stipulate that each G-selected factor is one subject. Here it says two.
- **Whole-subject hypothesis W:** stipulate that the complete four-state system is one subject. Here it says one.

These are minimal diagnostic rivals, not well-developed theories. In particular, W must defend unity across the stipulated independent dynamics, and F must defend why a single stochastic bit is an experiencer. They make identical physical and readout predictions **by construction**, so their subject counts are not empirically decided by this kernel or by those interventions alone. The general finite adaptive-history equivalence argument and its scope were already established in the [coupled-dynamics gate](COUPLED_DYNAMICS_SUBJECT_BOUNDARY_GATE.md); it is not claimed as a new theorem here.

To become testable, either hypothesis must supply a non-circular link to experience and a distinct operational prediction. A research protocol should:

1. Specify a physically realizable candidate system, available interventions, observables, timescale and relevant factorization **before** inspecting outcomes. Include hidden common causes, measurement and intervention disturbances, interaction with surroundings and finite-sample uncertainty.
2. Have each complete theory state a quantitative prediction for a prespecified jointly experienced content and for separately measured report behavior, including failures, ambiguity and delayed communication. A subject-count label by itself does not imply such a prediction.
3. Independently calibrate the link between reported content and the targeted experience under each intervention; a successful joint information report is not by itself proof of one experiencer. Include the controls and report-error assumptions described in the [causal-influence gate](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md).
4. Test held-out, prespecified data against rivals and explicit uncertainty bounds. If both predict the same outcomes or the experiential bridge is uncalibrated, record **underdetermined**, not a win.

For actual neuroscientific applications, extant controlled studies and ethically appropriate noninvasive perturbations should be evaluated before proposing new experiments. The [COGITATE adversarial collaboration](https://doi.org/10.1038/s41586-025-08888-1) illustrates preregistered competing predictions; it did not test the present factor gate or settle subject number. No human data or sample-size claim is supplied here.

## 7. Acceptance criteria and next dependencies

A proposed successor constitution rule should be presented with:

1. **Domain:** ontic inputs, allowed factor candidates, observable/operation algebra, time grain, boundary with surroundings, and what counts as an equivalent representation.
2. **Algorithm and invariance:** explicit selection or principled ambiguity; transformed candidate outputs under admissible redescriptions; no hidden appeal to coordinate names.
3. **Intervention fidelity:** physical intervention and response maps, including when equivalence is approximate or controls are not available. Changing the intervention family is not just changing notation.
4. **Incidence, overlap and persistence:** an explicit account of which candidates are subjects, whether and how they overlap, and how their identity is treated through local change, splitting or merging. Factorization alone supplies none of these.
5. **Experience and quality:** separately stated grounding/identity claims and empirically constrained links to reported and unreported experience. Do not identify stochastic bits or reports with experience by definition and then count that as evidence.
6. **Predictions and failure:** at least one calibrated contrast that could distinguish the complete proposal from a named rival, with limits on what a null or positive result would show.
7. **Integration and cost:** compatibility with the experiential whole, modal thesis, non-optimality and eventual physics; count new assumptions when assessing elegance. Derive rather than assume a self-location measure once the reference class is justified.

The next technical task is to extend the factor gate beyond the full-state error bound above to **weakly coupled, partially observed dynamics**, with justified physical intervention structures and explicit bounds on how inference degrades. That should be compared against the existing interventional-cohesion and IIT approaches, not confused with a solved consciousness criterion. In parallel, the independent foundation and physical-recovery gaps remain open: solving this gate would not establish self-existence, possibility = actuality, emergent spacetime, or a complete account.

## 8. Reproduction and scope

Run `python verification/subject_factorization_redescription_gate.py`. The standard-library verifier exhausts the finite candidates, all 24 state permutations, all 256 deterministic operations in the symmetric case, the nine original clamp settings, and the stated exact rational probabilities. Its [receipt](verification/subject_factorization_redescription_gate.json) records the counts. These are checks of the specified finite definitions, not measurements, a quantum-gravity derivation or proof of phenomenal identity. The [frozen v1 dossier](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) is unchanged.
