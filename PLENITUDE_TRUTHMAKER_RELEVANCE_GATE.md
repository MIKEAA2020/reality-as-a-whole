# Strong actuality and the experiential-grounding problem

## Result

There is a specific interaction between the framework's strongest possibility–actuality thesis and its search for an experiential ground of truth:

> **If the global schema `◇φ → φ` applies to every proposition at issue, and classical modal necessitation alone is used to select truthmakers, every actually existing candidate qualifies as a truthmaker for every actual truth.**

That makes the proposed selection rule unable to say *why this experiential occurrence grounds this truth*, rather than an unrelated occurrence grounding it. The result is conditional on that global formalization and on the proposed necessitation-only rule. It does **not** refute strong possibility = actuality, truthmaking, experiential grounding, or the possibility of an intrinsically differentiated whole. It shows that the combination needs a more discriminating account of grounding.

This extends the project's earlier [global modal analysis](PLENITUDE_FOUNDATION_GAPS_AND_SYMMETRY.md) and [truth/experience audit](NOTHINGNESS_TRUTH_AND_EXPERIENTIAL_NECESSITY.md) by combining their assumptions. The general overgeneration problem for necessary truths, as well as alternatives using relevance, essence and grounding, is established prior work, not a new discovery; see [1](https://plato.stanford.edu/entries/truthmakers/) and [2](https://iep.utm.edu/truth-ma/). The calculation below applies it to the present global-collapse formulation, rather than claiming a general no-go theorem for idealism.

## 1. Exact conditional derivation

Let `p` be any **actual global proposition covered by the schema**, and let `X` be any entity that actually exists. No external time, creator or process that converts possibilities into actuality is assumed. Work in classical modal logic, with `□p := ¬◇¬p`.

```text
p                                  actual truth
◇¬p → ¬p                           schema instance for ¬p
p → ¬◇¬p                           classical contraposition
□p                                 definition of □
□(X exists → p)                    consequence of □p
```

If a proposal defines `X` as a truthmaker of `p` **if and only if** `X` actually exists and `□(X exists → p)`, then *every actually existing X* qualifies. Nothing in that definition singles out an experiential X, its specific quality, or its relation to p. Modal necessity may be a **necessary condition** on grounding without being sufficient; this result challenges only the sufficiency claim. It does not show that all truthmaker theorists accept that claim.

The same issue applies when `p` is a factual claim about a **specified local sector, subject and time**, if the global schema is intended to cover that indexed fact. For example, `warm(A)` and `not warm(B)` can both be facts of one whole: they are not the same proposition at the same index. Granting their necessity under the global schema does not eliminate their local difference or require a global clock. If “genuine possibility = actuality” is instead formulated as *realization in some actual sector*, rather than `◇φ → φ` for global propositions, the proof above does **not** automatically apply. The realization relation and its scope would then need their own specification; local compatibility cannot simply be substituted for global possibility.

The [executable check](verification/plenitude_truthmaker_relevance.py) exhausts 256 valuations across four reflexive two-point frames. In the 16 cases where the schema holds at the designated point and two candidates and p are actual, both candidates necessitate p. A control with an accessible `not p` point and one candidate persisting there shows that necessitation can distinguish candidates when the schema fails. This is an elementary regression for the argument, not an empirical discovery or a test that the accessible points are genuine possibilities.

## 2. Does “truth is experiential” solve the problem?

Three different claims must not be conflated:

1. **Epistemic:** a person's grasp or assertion of a truth is experienced. That concerns an actual act of knowing or representing, not automatically what makes the represented claim true. The well-known challenge to arguments from the experience of conceiving to the nature of what is conceived appears in discussions of Berkeley's idealism [3](https://plato.stanford.edu/entries/idealism/). Our target does not require Berkeley's God or an external perceiver.
2. **Witnessed existential:** an actual experience `e` may be a witness to the actual claim `E = there is experience`, on the assumption that `e` is genuinely experiential. This is a promising **specific** connection: the content of E explicitly demands an experiential witness. But identifying a logical witness does not by itself establish an independently specified metaphysical grounding relation; nor does actual E prove `□E` without the separate global schema or another defended bridge.
3. **General foundation:** a particular necessary mathematical or logical truth `τ` is intrinsically grounded in experiential reality. This would require an account of how the proposed ground relates to the *content* of τ, not only `□τ` or the fact that a thinker can grasp it. Bare necessitation makes every existing candidate qualify. The substantive experiential truth-grounding premise remains to be defended against the non-maximalist or non-experiential alternatives [1](https://plato.stanford.edu/entries/truthmakers/), [2](https://iep.utm.edu/truth-ma/).

Thus the strong actuality thesis, combined with actual experience, already **conditionally** gives `□E`; it does not separately prove why E holds or why τ is grounded in E. The conditional implication is real, but it cannot serve as independent evidence for the schema it uses. An experiential constitution could be the answer; naming one without specifying it is not yet that answer.

## 3. A constructive test for a candidate grounding rule

A useful candidate should do more than output `true` for every existing entity/truth pair. The following is a **research contract**, not a completed law or an instruction to posit an external mechanism:

- **Typed inputs:** specify a timeless actual experiential occurrence or whole-aspect `g`, a truthbearer's content `p`, and the relevant subject/sector scope. Distinguish the proposition from a local thinking of it.
- **Content/relevance:** supply a nontrivial condition connecting the specified structure of `g` to what `p` is about. Say which features can be varied in a *formal model* or compared across descriptions; this is a mathematical diagnostic, not a commitment to unactualized genuine possibilities.
- **Truth and occurrence:** establish that the proposed ground is actual and that p is true. If the rule uses `□(g exists → p)` as a necessary condition, show its explanatory content comes from more than that condition.
- **Comparison and economy:** apply the **same rule** to experience-existence, a necessary logical/mathematical truth, a local experiential quality, and a physical relational claim. It should not get the answer by inserting each desired truth as a primitive label. It may use a single intrinsic constitution rather than four extra external laws, but its determinate principles must actually be stated and justified.
- **Adversarial controls:** compare an unrelated actual experiential occurrence, a non-experiential formal competitor, and a differently assigned grounding relation preserving all modal truth values. Explain why the rule admits or rejects each without quietly assuming that everything is experiential.

For a minimal diagnostic, take **two named actual candidate entities and two named actual truths** in one reflexive evaluation point. There are two distinct one-to-one assignments of candidate-to-truth pairs, both respecting existence, modal necessitation and total coverage. The verifier enumerates them. These are just two **stipulated formal enrichments**, not demonstrations that either assignment is an intelligible, genuine grounding relation; they show only that the extensional conditions and one-to-one constraint do not choose between them. Real grounding may be many-to-one or collective; uniqueness is imposed here solely to make the underdetermination obvious, not as a proposed metaphysical law.

Possible routes include a subject-matter-sensitive relevance condition, essential dependence, a hyperintensional relation, or an independently developed intrinsic constitution. These are families of approaches in existing literature [1](https://plato.stanford.edu/entries/truthmakers/), not established solutions here. None is automatically a brute external rule: a successful theory might derive its criterion from the whole's nature. But specifying a primitive relation or allowing counterpossible comparisons still carries explanatory work; a vacuous ordinary material counterfactual is not a demonstration of relevance. The truthmaker literature also notes that defining truthmaking by reference to *truth* makes it unsuitable by itself as a non-circular definition of truth [2](https://iep.utm.edu/truth-ma/).

## 4. First constructive candidate: content-sensitive support

We can go beyond merely demanding relevance by checking a **precise but limited formal rule**. Take two designated Boolean inputs `x` and `y`, both equal to 1. For any true claim `f(x,y)`, define its *support candidates* as the subset-minimal sets of actual input literals that make `f` true for every Boolean completion consistent with those literals. This is the familiar prime-implicant/sufficient-reason idea, not a new theory of explanation; see [4](https://www.ijcai.org/proceedings/2022/0358.pdf).

| True claim at `x=y=1` | Minimal formal support candidates |
| --- | --- |
| `x AND y` | `{x=1, y=1}` |
| `x OR y` | `{x=1}` **and** `{y=1}` |
| `x = y` | `{x=1, y=1}` |
| `x OR NOT x` | empty set |

The same actual values yield different support families because the **contents and declared functions differ**. The rule retains both equally minimal OR supports; choosing only x would arbitrarily break the symmetry. The [toy verifier](verification/experience_ground_support_toy.py) checks these results, a false-claim stop, other assignments and equivariance when x and y are relabeled together. All completions are formal valuations, not claims that nonactual conditions are genuinely possible. This mathematical use of comparison does not insert a possibility-to-actuality process.

This is a constructive advance in the *interface*, not the sought constitution. The Boolean inputs are not established experiences, subjects or physical facts, and the functions are supplied rather than derived. Minimal logical support is neither automatically ontological grounding nor a causal or phenomenal identity. The tautology's empty support also shows that this particular rule does **not** supply an experiential ground for every necessary truth. Replacing the empty support with an experiential one by fiat would assume the disputed claim. The OR tie shows why an account must allow multiple grounds or provide a justified tie rule; this toy does not identify subject boundaries. Real experiential and physical predicates, their appropriate comparison semantics, and an independently justified connection to the whole remain to be supplied.

## 5. Battery effect and what comes next

- **B1 and B2 remain open.** We have exposed a further condition on an experiential-grounding route under one global reading, not justified its crucial premise or established self-existence.
- **B4/B5 remain open.** Nothing here selects subjects or explains qualitative character. In particular, assigning ‘experiential’ as a type in a toy is not a constitution of a subject.
- **B7 and B10 are unchanged.** No claim about physics, temporal emergence or empirical calibration follows from this logical test.

The next constructive task is to specify **one content-sensitive intrinsic constitution** on a small explicit shared model, compute which local experiential and physical claims it grounds, and compare it with a rival constitution on the *same* physical and phenomenological inputs. The strongest test is not whether either can be written down but whether one can be independently justified, remains stable under admissible redescriptions, and connects to empirical and qualitative constraints without already assuming the outcome. If both satisfy the declared constraints, report underdetermination; do not label an arbitrary selection a pass.
