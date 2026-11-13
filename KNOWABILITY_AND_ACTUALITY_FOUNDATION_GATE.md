# Knowability and actuality: a foundation gate

## Decision

The immediate bottleneck is still **B1–B2**: why must concrete experience exist, and why should strongest genuine possibility coincide with actuality? We have not passed those gates. This note tests a candidate bridge rather than adding another assumption silently: **truth is in principle knowable by an experiencer**.

A significant constraint emerges when this bridge is combined with the user's strong possibility–actuality thesis. If the global principle `◇φ → φ` applies to the proposition “someone knows p,” then *even a knowability principle restricted to one proposition p* implies that, whenever p is true, someone actually knows p. Restricting knowability to basic truths does not avoid this consequence unless the scope of the actuality schema is also restricted. This does not refute the user's thesis; it shows exactly what the combination commits it to.

This is a **conditional application** of standard epistemic and modal reasoning, not a claim to have discovered the knowability paradox. Fitch's established result and its restrictions are surveyed in the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/fitch-paradox/). The present application distinguishes that result from the separate effect of the project's own global modal schema. No literal simulator, creator, external clock, or transition from possibility to actuality is assumed.

## 1. Candidate and premise ledger

Use propositions about the whole, with any local subject or event explicitly indexed. Let `E` mean “there is at least one concrete experience in the whole.” Let `Kp` mean “at least one subject in the whole genuinely knows p”; it is not merely a formal label, an unconscious computation or an external observer. Assume, for this candidate, that propositional knowledge entails a subject with actual experience: `Kp → E`. This is a **substantive bridge**, not an established consequence of information processing. A subject may know something at a particular local time, but all statements below are global existential claims about the timeless whole; they do not require simultaneous knowledge or a universal present.

Compare the following independent commitments:

- **C — strong global actuality:** for propositions φ in a specified domain, `◇φ → φ`. Under the usual reflexive semantics the converse holds, but this note uses only the displayed direction. This is the user's intended strong thesis *under this precise global formalization*, not a theorem already established. Other sector-realization readings require separate treatment.
- **N — epistemic bridge:** for a declared class of true propositions p, `p → ◇Kp`. This says a truth is knowable, not that its being true is caused by or constituted by a knower. An argument from truthmaking or intelligibility to N would be a further step.
- **H — phenomenal knowledge:** `Kp → E`. This applies only if K means knowledge by an experiencing subject; abstract semantic entailment is not K.
- **F — knowledge conditions:** factivity `Kp → p`, and knowing a conjunction implies knowing each conjunct. These enter the Fitch control below, but are not needed for the main three-line C+N result.

The important extra assumption is N. C does not by itself imply it; actual experience also does not show that every truth, or even a given truth, is knowable. H likewise needs defense. Accepting a bridge explicitly can be a coherent research hypothesis, but it cannot be credited as a derived foundation merely because it is called intelligibility.

## 2. The direct interaction: knowability becomes knowledge

For any particular p in N's domain, if C applies to `Kp`, then

```text
p → ◇Kp          N for p
◇Kp → Kp         C for the global proposition Kp
therefore p → Kp.
```

If p is a true tautology and N includes it, H gives `E`. If C also applies to `¬E`, classical contraposition and `□E := ¬◇¬E` yield `E → □E`; hence `□E`. This is a **valid conditional derivation** of necessary occurrence of some experience. It does not show that C, N or H is true or explain why they hold. Moreover, actual experience was already a datum in the framework: on this global reading C plus that datum alone already gave `□E`. The new route is therefore **not an independent proof of C**, nor an explanation of experience's intrinsic nature.

The dependence is particularly sharp: C must cover `Kp`, including its subject/time indexing and epistemic content. A view that applies the strong thesis only to a narrower class of global propositions, or interprets possibility as realization somewhere in an actual sector, cannot simply inherit this deduction. It must state the relevant relation and truth conditions. Conversely, excluding `Kp` or weakening N solely to escape the conclusion would be a new scope restriction needing its own justification.

The conclusion is **collective coverage of truth**, not a single all-knowing cosmic mind: different p could be known by different subjects at different local times. It does not establish that the whole is a universal subject or agent. It would nevertheless be an extremely strong claim about the totality of actual subjects and their knowledge. Their finitude does not by itself prove it false, nor does the desired elegance make it true. Whether available subjects, physical bounds and truth-domain can support it is open.

## 3. Contrast with Fitch's established result

Under classical logic and suitable factivity and conjunction-elimination rules, the unrestricted schema `p → ◇Kp` itself implies `p → Kp`. Briefly, if `q = p ∧ ¬Kp` is true, unrestricted knowability requires `◇Kq`; but any knower of q would know both p and `¬Kp`, and factivity would make `¬Kp` true while Kp is true. Thus Kq is impossible. This is the established Fitch argument; see the [SEP analysis](https://plato.stanford.edu/entries/fitch-paradox/), including its discussions of semantic, syntactic and intuitionistic restrictions.

For a collective K, conjunction elimination means the subject who knows the conjunction also knows each conjunct; factivity of their knowledge of `¬Kp` conflicts with the existence of *any* knower of p. More general collective or distributed-knowledge operators need separate rules. Rigidification, temporal indexing, nonclassical logic and alternative modal interpretations are substantive choices; the formal argument is not a ruling on every theory of truth.

**The distinction:** a basic-truth restriction can block Fitch's substitution of `p∧¬Kp` into N. But if C applies to `Kp`, the three-line argument still applies to any basic p for which N is assumed. Thus avoiding Fitch's *unrestricted* N is not sufficient to avoid the C+N consequence. Nor does Fitch imply C, or that strong possibility–actuality is false.

## 4. Adversarial controls

The [verifier](verification/knowability_actuality_gate.py) implements finite, extensional relational models with an explicit `knower exists` predicate; it does not identify a formal point with a real experiencer. Epistemic accessibility is reflexive in the factive/Fitch cases. The checks include:

1. **Restricted N without C:** at three formal points, p is true but unknown at point 0, and p is known at an accessible point 1. A tautology is also knowable; there is no knower or experience at point 0 (the model stipulates experience exactly at the knower point). Thus restricted knowability and factivity do not alone imply actual E or actual Kp. The Moore conjunction `p∧¬Kp` is true at point 0 but not knowable, so unrestricted N fails. This is a model of a formal rival, not proof that an experience-free world is genuinely possible.
2. **C without N:** a one-point model with no knowers satisfies the strong schema but has no possible knower of a tautology. C alone does not establish N or E.
3. **Combined C+N:** all 8,192 two-point relation/assignment/event cases are checked; in the 4,720 cases satisfying the two relevant premises, no case violates `p → Kp`. The result is already established by the symbolic implication above; finite checks are regression controls, not proof of the universal argument.
4. **Fitch control:** among 512 designated two-point models with reflexive epistemic accessibility, 64 meet unrestricted knowability at the point, and all of those satisfy the corresponding actual-knowledge condition. The finite model closes over its finite event algebra and validates only this encoded instance.

The three-point countermodel represents knower existence and epistemic access separately, avoiding the artifact that a standard normal knowledge operator automatically “knows” all tautologies even when no subject exists. In an unbounded theory, the interpretation of propositions, modal accessibility, quantification over subjects, and a non-circular notion of phenomenal knowledge still need to be defined.

## 5. What this changes in the battery plan

This bridge is **not ready to pass B1–B2**. It gives a useful decision fork:

| Candidate | What it gains | What it must justify or accepts |
|---|---|---|
| Global C + unrestricted N + H | Some experience necessarily occurs, conditionally; all truths are known somewhere under the assumptions. | A very strong and unproved collective epistemic thesis, a genuine experiential knowledge bridge, and C itself. Does not explain why those premises hold. |
| Global C + restricted N + H | May connect selected truths to experience; even one true knowable proposition gives actual knowledge if C covers Kp. | Must justify the selected class and still explain C and H. Restricting N alone does not undo the C+N consequence. |
| Actual experience + global C | Necessity of some experience, conditionally, with no universal knowability postulate. | C is not derived from experience; the intrinsic nature, subject constitution and specific qualities remain ungrounded. |
| Restricted or non-global C | May avoid the inference to actual Kp. | Must explain exactly how its semantics preserves the user's strongest possibility = actuality, not replace that target unnoticed. |
| Realist truth with no N | Avoids assuming truth is knowable or requires an experiential ground. | Does not itself establish a non-experiential world or a self-sufficient experiential foundation. |

**Next work:** formulate a positive, non-circular defense of one bridge against the realist rival, specifying (i) what makes a proposition true independently of the act of entertaining it, (ii) why that ground must be experiential rather than an abstract or non-experiential ground, (iii) whether the argument derives C or presupposes it, and (iv) how it yields plural subjects without postulating a universal knower. If that defense fails, keep B1–B2 open and compare alternatives rather than relabeling the premise as a proof.

In parallel, B4–B5 require a real subject/quality constitution and independent assay calibration; B6–B8 require common physics, local clock and gravitational recovery; B9 requires a justified reference class and measure; B10–B12 require discriminatory predictions and an explicit comparison with rivals and assumptions. The 21-script [regression runner](verification/framework_battery.py) is a useful consistency check, **not the substantive formal battery**. The independent assessment found the submitted dossier entry-incomplete; neither this note nor an additional green script changes that status. See [the critical path](POST_ROY_FRAMEWORK_CRITICAL_PATH.md), [foundation route comparison](FOUNDATION_NECESSITY_ROUTES_COMPARISON.md), and [truthmaker relevance gate](PLENITUDE_TRUTHMAKER_RELEVANCE_GATE.md).

**Positive candidate and rival:** The [experiential-grounding comparison](EXPERIENTIAL_GROUNDING_RIVAL_BATTERY_GATE.md) develops the direct-experience/parsimony motivation, tests a neutral-base rival with the same actual experiences, and isolates the missing constitution and necessity steps.
