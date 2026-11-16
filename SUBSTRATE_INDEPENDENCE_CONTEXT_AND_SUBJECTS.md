# Substrate-independence, context and the boundaries of subjects

## The advance

The follow-up [horizon and robustness analysis](SUBSTRATE_CONTEXT_HORIZON_AND_ROBUSTNESS.md) tests how weak contextual effects accumulate and gives a fixed-topology stability certificate for the existing four-spin C/L subject-rule comparison.

The user's preferred account combines an intrinsically experiential, self-existent whole with **material substrate-independence** and real plural subjects. The immediate obstacle is not simply whether two materials can implement the same local process. It is **which relations count as part of the organization whose preservation is supposed to preserve an experience**.

This note connects the earlier [substrate-independence interface](SELF_EXISTENT_EXPERIENTIAL_SUBSTRATE_INDEPENDENCE.md) to the existing [causal subject-boundary comparisons](CAUSAL_INFLUENCE_SUBJECT_CONSTITUTION_GATE.md). It gives a conditional incompatibility and an exact weak-coupling/detection example:

> An organization criterion that sees only a subsystem's own input/output and interventions can declare that subsystem unchanged while a context-sensitive boundary rule says it has ceased to be a separate subject. Both cannot determine the same subject verdict in that case.

This is **not** a proof that substrate-independence is false or that context-sensitive subject constitution is correct. It isolates the further choice the framework must make. The candidate can remain substrate-independent while requiring preservation of relations to the relevant surrounding system; it need not choose a privileged material. But specifying which surrounding relations matter is substantive work, not a free solution.

The checks are a finite mathematical illustration. They do not identify subjects, measure consciousness, establish which local systems are genuinely possible or derive physics, time, the self-existent whole, or its experiential nature.

## 1. Candidate principle and the factorization gate

Let `r` be an actual candidate realization **with a specified boundary and context**, not a free-floating abstract computation. Let `O(r)` describe the chosen organization, including the admitted physical operations and observational structure. Let `B(r)` answer whether the indicated boundary is selected as a subject; a richer answer could include qualitative type and incidence, with independently fixed referents.

A candidate material substrate-independence principle is:

```
O(r₁) ≈ O(r₂)  ⇒  B(r₁) = B(r₂),
```

where `≈` preserves the claimed consciousness-relevant organization, state and circumstances, even if the materials differ. This concerns subject **type or boundary verdict**, not numerical identity of two separate people. As in the prior work, neither this principle nor its scope follows automatically from an experiential ground. In particular, it does not say that a mere description creates an experience or that every possible material can implement the same organization.

This is a standard factorization criterion applied to our problem: for a fixed domain of candidates, an unambiguous function `b` with `B = b ∘ O` exists exactly when `B` is constant on every equivalence class of `O`. If two candidates share an organization class but receive different boundary verdicts, no such `b` exists. This is the already-used [factor-through-a-quotient principle](EXPERIENTIAL_FOUNDATION_POSITIVE_CONSTRUCTION.md), not a new general theorem. One can change `O`, change `B`, or reject the principle; which is justified is a philosophical and empirical question.

The converse is important: enlarging `O` until it contains the desired subject label makes factorization trivially true, but explains nothing. Relevant relations must be specified independently of the outcome the rule is meant to explain. Nor can every accidental surrounding feature automatically be treated as subject-constitutive; otherwise substrate-independence risks becoming vacuous.

## 2. A local realization that stays the same as its context changes

Consider two bits `x,y`, local inputs `i,j`, and the local update

```
x' = x XOR i
y' = y XOR j XOR (x AND N),     N ~ Bernoulli(ε), independently each step.
```

Here `0 ≤ ε ≤ 1`. The prime denotes a local mathematical ordering, **not** an external clock or a fundamental temporal creation. Each configuration and each hard clamp is a stipulated test case. In particular, these toy states and intervention alternatives are not declarations that every formal counterfactual is a genuinely possible unrealized world. A physical application would need actual realizations or independently justified physical intervention models.

For every initial state and input, `x'=x XOR i`. Thus the subsystem `x` has **exactly the same** input/state/update/readout and response to changes of `y` for `ε=0` and any `ε>0`. It may still influence `y`: setting `y=i=j=0`, the difference between the probability of `y'=1` under `do(x=1)` and `do(x=0)` is precisely `ε`. There is no corresponding `y→x` effect in this toy.

The joint kernels are close in a precise sense: at each specified state and input, their total-variation distance from the `ε=0` kernel is `0` if `x=0`, and `ε` if `x=1`. Consequently their maximal conditional distance is exactly `ε`. This holds for arbitrarily small positive `ε`; small is not the same as zero.

Now **stipulate**, for the sake of a candidate comparison, the following boundary rule:

- Draw a directed edge for a positive interventional influence. Form **weakly connected components**, ignoring the arrow direction, and select one subject boundary per component.
- At `ε=0` there are two selected boundaries `{x}` and `{y}`.
- At any `ε>0` there is a single selected boundary `{x,y}`. The singleton `{x}` is no longer selected by this rule.

This is a deliberately simple **weak-connectivity rule**, not IIT, and not quite the prior reciprocal-influence rule: the previous gate used a minimum of the two directional effects, which is zero for this one-way link. The present rule's tendency to merge systems under even an arbitrarily weak one-way connection is a serious reason to question it, not evidence that the two bits ever form one experience. The example tests a rule, not a person.

### The precise conflict

Let `O_local` record only the full input/state/intervention organization and output of `x`, as above. The `ε=0` and `ε>0` cases agree on `O_local`, but the stipulated connectivity rule assigns different singleton verdicts. Therefore the boundary verdict **cannot** be a function of `O_local` alone on any candidate domain containing both cases. If the actual world does not contain both kinds of realization, this is a conditional constraint on a proposal, not evidence that both cases are physically or metaphysically possible.

Three live routes remain:

1. **Boundary-local invariance:** accept that the full `x` organization suffices, and reject the context-sensitive verdict in this case. One must then defend a positive subject/quality criterion and say whether a larger subject can coexist with `x`.
2. **Context-complete invariance:** include independently specified relevant connections, reciprocal structure, environment and operations in `O`; apply invariance only when *that* enlarged organization is preserved. The two cases no longer count as equivalent. This retains material substrate-independence, but owes a noncircular account of which context is relevant and what else can vary.
3. **Weaker multiple realizability:** require some rather than all sufficiently matched organizations to have multiple material realizations, and leave further boundary sensitivity open. This accommodates the preference but supplies less predictive power.

None follows from the toy alone. In particular, retaining a local subject **and** a larger subject is not logically excluded; it would require a positive account of overlapping boundaries, incidence and the ownership or sharing of episodes. Disallowing overlap is itself a premise. The [episode-incidence analysis](EPISODE_INCIDENCE_REFORMULATION.md) sets out that separate issue.

## 3. Arbitrarily weak links and finite evidence

The stipulated connectivity selector changes its boundary discontinuously at `ε=0`: any positive influence, however small, merges the components. This makes its cost clear. A sharp subject transition is not logically impossible merely because the physical change is small, but a theory that relies on exact zero should justify why this distinction is constitutive and how it could be supported by evidence. Small physical changes do not prove small phenomenal changes without an additional continuity principle.

Under an idealized experiment, fix `x=1, y=i=j=0` at every independently prepared trial and observe `y'`. Compare the *known* models `ε=0` and `ε=1/10,000` with perfect preparation and readout:

| Quantity | Result |
|---|---:|
| Probability of no positive outcomes in 1,000 trials under `ε=1/10,000` | about **0.9048** |
| Minimum average decision error with equal priors, 1,000 trials | about **0.4524** |
| Minimum worst-case error for the two known models, allowing randomized decisions | about **0.4750** |
| Trials for at least 95% chance of detecting one positive outcome if `ε=1/10,000` | **29,956** |

These values follow from `t=(1−ε)^n`: the two full-sample distributions overlap only on the all-zero outcome, so equal-prior optimal error is `t/2`; the optimal randomized minimax error is `t/(1+t)`. The last row uses an “any positive” test with zero false positives in the ideal model. It is not a confidence bound for arbitrary unknown `ε`, an experiment on the brain, or a human-study sample recommendation. Imperfect readout, hidden causes, intervention effects and correlated trials may substantially alter it.

Thus, even in an unusually favorable physical experiment, a finite absence of detected influence does not by itself establish exact independence. More importantly, **perfect knowledge of influence still would not establish a subject boundary**; that requires the disputed constitution and experiential bridge. Detection of weak influence and detection of a new subject are different claims.

## 4. What this means for the developing framework

The best current formulation is **context-qualified, materially substrate-independent experiential constitution**:

- The whole is self-existent and intrinsically experiential as the user's working candidate; there is no assumed external creator, universal subject, or temporal mechanism of actualizing possibilities.
- A finite subject is not defined merely by a change in material. It is constituted by the right actual relational organization, whose boundary, relevant surroundings and qualitative consequences must be justified.
- Different material realizations of the **same complete relevant organization**, if genuinely possible, are actual somewhere in the whole under the user's strong actuality thesis. The thesis alone does not identify the correct organization or require their simultaneous realization in our local universe.
- Preservation of experiential *type* does not entail identity of two occurrence tokens, preservation of a person across a branching/replacement, or a probability measure over copies.
- A candidate must explain why its `O` preserves the pertinent experiential facts without stipulating them as part of `O`; it must also say whether external couplings can alter subject incidence and whether overlaps are possible.

This does not disprove the stronger boundary-local view. It sharpens the question it must answer: *which interactions outside the local computation can be changed without changing who experiences what, and why?* Conversely, merely mentioning “context” cannot settle how much context is necessary or whether the entire whole is one subject.

## 5. Next concrete gates

1. **Nontrivial organization:** define an independently motivated relation on actual candidate realizations, including controlled internal and external interactions, state, grain and permitted changes of material. Prevent arbitrary reinterpretation and unbounded inclusion of irrelevant surroundings; use existing causal-abstraction and factorization work rather than inventing another implementation theory.
2. **Rival subject rules:** apply at least a context-local and a context-sensitive rule to the *same* realizations, including zero, weak and strong couplings, reciprocal and one-way interactions, ties, overlaps and persistence. Neither connectivity nor scalar integration is automatically the correct rule.
3. **Independent phenomenal target:** specify a qualitative or joint-experience target and a report/assay relation that is independently calibrated. The prior [fixed subject interface](SUBJECT_CONSTITUTION_INTERFACE_RESULTS.md) showed how even an idealized assay distinguishes packages only under its added error assumptions; it did not provide a real assay.
4. **Physics, necessity, measure:** recover local physical order and actual organization rather than projecting them as inputs; argue non-circularly for the self-existent experiential constitution; and justify subject occurrence/measure separately from type. None is closed here. The [frozen battery](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md) remains incomplete, including B1–B2, subjects and quality, physics/time, measure and empirical discrimination. No Roy data were reused.

## Reproduction and sources

Run `python verification/subject_context_substrate_gate.py`; the [receipt](verification/subject_context_substrate_gate.json) checks 48 exact transition comparisons, the stated influence and conditional total-variation values, the illustrative component verdicts, and the ideal detection arithmetic. It encodes the model, not the truth of its assumptions. The 21 selected [framework regression scripts](verification/framework_battery.py) also exited successfully with their pinned NumPy dependency; that is not a pass on the frozen framework's substantive gates. The factorization insight is an application of the existing [operational factorization gate](EXPERIENTIAL_FOUNDATION_POSITIVE_CONSTRUCTION.md); the handling of subsystems and interventions also builds on [Zanardi](https://doi.org/10.1103/PhysRevLett.87.077901) and [Massidda et al.](https://proceedings.mlr.press/v213/massidda23a/massidda23a.pdf), not an independent derivation of their results. For the argument motivating organizational invariance, see [Chalmers's précis](https://consc.net/papers/precis.html); none of these sources establishes this toy as a correct consciousness model.
