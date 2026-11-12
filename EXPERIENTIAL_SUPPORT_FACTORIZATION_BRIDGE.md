# A representation-stable support interface—and its limits

## Result

The previous [truthmaker analysis](PLENITUDE_TRUTHMAKER_RELEVANCE_GATE.md) proposed content-sensitive logical support as a diagnostic, while the earlier [subject-factorization analysis](SUBJECT_CONSTITUTION_FACTORIZATION_GATE.md) supplied a physical-factor selection gate. I have now connected those two **existing finite constructions**.

In the specified asymmetric four-state model, the factorization gate selects one pair of factors. Using that pair, the minimal support for a selected truth is preserved under **all 24 bijective redescriptions** of the state space, provided the transition kernel, factors, target and actual state are all transported. In the symmetric model, three equally eligible factorizations give **two different support families** for the same target and state. The procedure therefore identifies support in the first toy case but does not select a unique answer in the second.

This is a bounded mathematical interface, not a derivation of physical laws, experience, subjects, self-existence or metaphysical truthmaking. It makes a previously implicit dependency explicit: **a content-sensitive support rule needs a justified set of factors, not just truth values or written coordinate names.**

## 1. Why the original coordinate rule is not enough

Use formal states `(x,y)∈{0,1}²`, with actual state `(1,1)`, and let the true target be `p: x=1`. With `x,y` as candidate features, the sole subset-minimal support is `{x=1}`.

Now redescribe exactly the same four states by the bijection

```text
u = x XOR y,     v = y,     so x = u XOR v.
```

The actual state is now `(u,v)=(0,1)`. If we **discard the old factors** and take the new written axes `u,v` as the candidate features, then `p` becomes `u XOR v=1`, and its sole minimal support is `{u=0, v=1}`. Its apparent size changed from one to two. That change alone cannot be an intrinsic fact about the original system: the system and target were merely redescribed, but the allowed candidate features were changed.

The correct transported original factor `x` is the observable `u XOR v`; the original factor `y` is `v`. Relative to those transported factors the support remains the single factor-event `{u XOR v=1}`. An operation that changes `x` while holding `y` fixed must also be transported; it is not automatically an independent clamp of the written coordinate `u`. This distinction does not say all bijections are physically admissible symmetries: locality, accessible operations, costs and other structure may exclude particular transformations. It says that *where* two presentations do represent the same physical structure, that structure must be transported.

The general issues of subsystem choice, operations and causal abstraction are established prior work, including [Zanardi](https://doi.org/10.1103/PhysRevLett.87.077901) and [Massidda et al.](https://proceedings.mlr.press/v213/massidda23a/massidda23a.pdf). Representation-sensitive logical explanations are also studied in the prime-implicant literature, for example [1](https://www.ijcai.org/proceedings/2022/0358.pdf). The present four-state combination is an application of those kinds of tools to our existing gates, not a claim to have invented them.

## 2. The combined rule

For the finite test, let `Ω={00,01,10,11}` and fix:

1. a transition kernel `K` and its declared allowable factor candidates;
2. a target event `P⊆Ω` and actual state `s∈P`;
3. a factorization `F` consisting of two binary partitions, selected by the earlier gate G: the next-factor probabilities must be independent and each factor's marginal must depend only on its own prior value.

For each factor in `F`, take the partition block containing `s`. A **support** is a subset of these actual blocks whose intersection is contained in `P`; retain all subset-minimal supports. An empty intersection means all of `Ω`, so a tautological target has the empty support. This is a standard formal-sufficiency criterion applied to supplied factors. The other states in `Ω` are **formal comparisons**; they are not asserted to be genuinely possible, unactualized realities or local histories of our universe.

### Conditional covariance

Let `h:Ω→Ω'` be a bijective redescription. Transport the target, actual state and each factor block by `h`, and conjugate `K`. Since bijections preserve intersections, inclusions and strict subset relations, a set of blocks is a minimal support before transport if and only if its image is minimal afterward. Thus support transforms with the input structure. The earlier gate's equivariance under all 24 bijections in this particular kernel has already been checked; the new [combined verifier](verification/ground_support_factorization_gate.py) checks it again together with the support calculation.

The mathematical argument does not require an external clock. The finite transition step is only part of this local toy and is not a proposed fundamental time.

## 3. Worked asymmetric and symmetric cases

### Asymmetric kernel: one factorization

Take the earlier independent-flip kernel, with flip probabilities `1/4` and `1/3` for `x` and `y`. G selects **only `{x,y}`** among the three eligible pairs of balanced binary partitions. For `s=(1,1)` and `P={states with x=1}`, the support family is

```text
{{x=1}}.
```

After *every* bijective redescription, G selects the transported pair and the support family is exactly the transported original family. The implementation tests **24/24** and additionally exhausts 2,304 combinations of factor pairs, target events, satisfying states and redescriptions for the support-covariance rule. It also checks the mixed-coordinate counterexample above: blindly using the new coordinate axes changes support size from one to two; transporting the factorization avoids that error. This is a genuine combined result for this toy, not evidence that the selected factors are conscious or physically fundamental.

### Symmetric kernel: the selection gap remains

Set both flip probabilities to `1/2`; every next state has probability `1/4` from every start. G accepts all three balanced factorizations `{x,y}`, `{x,z}`, `{y,z}`, where `z=x XOR y`.

At the same actual state and target `x=1`, the first two factor pairs yield support `{{x=1}}`; the third yields `{{y=1,z=0}}`. There are **three accepted factor pairs but two distinct support families**. These statements use the same state, kernel and target, and neither solution is selected merely by demanding G. One can retain all admissible factorization/support pairs instead of breaking the tie, but that is a *set of candidate answers*, not an identified ground.

This is a limitation of the declared target-independent factor gate, not a proof that no enriched rule can decide: additional legitimate physical structure, a justified target-sensitive criterion, or a different candidate space may change the result. Those additions must be independently motivated and tested. The earlier full-symmetry factorization no-go does not automatically prohibit all rules that are allowed to use the target as further input.

## 4. What this buys the framework—and what it does not

The result advances a narrow obligation shared by B4 and the truth-grounding work: **do not identify grounds or subjects by an accidental choice of coordinates.** It gives an implementable, covariant finite construction and a failure control, using a previously defined physically motivated gate instead of simply declaring the preferred factors.

However:

- The kernel, factor domain and target are **stipulated**. Factor independence is not a demonstrated subject criterion; integrated experience need not be a product factor, and an independent subsystem need not experience anything.
- Formal minimal support is not automatically an ontological ground, causal dependence or phenomenal identity. The target's content, especially why a particular organization is *this* experience, is not derived.
- A tautology still has empty support. This construction does not establish that necessary truths require an experiential ground, nor does it derive `E → □E` or genuine possibility = actuality.
- Selecting factors or presenting a finite transition model does not derive emergent spacetime, local temporal order in reality, quantum theory, gravity or a subject-weighting measure.
- The symmetric tie may be resolved by actual independent structure, or it may expose a genuine underdetermination; this finite test cannot decide between them in brains or in the whole.

Accordingly B1, B2, B4, B5, B7 and B9 remain **open**. The concrete next step is to test the combined support rule against an independently justified physical/experiential example and an explicit rival rule, with the same input structure, admissible transformations and empirical predictions. A successful finite check alone will not suffice for the full formal battery.

## Reproduction

`python verification/ground_support_factorization_gate.py` checks the combined construction and writes [the aggregate receipt](verification/ground_support_factorization_gate.json). It reuses [the exact factor gate](verification/subject_factorization_redescription_gate.py) and [the formal-support function](verification/experience_ground_support_toy.py). The 24 finite permutation checks validate this model; the stated general covariance follows from bijectivity and set operations, not from treating the 24 examples as an exhaustive proof for all systems.
