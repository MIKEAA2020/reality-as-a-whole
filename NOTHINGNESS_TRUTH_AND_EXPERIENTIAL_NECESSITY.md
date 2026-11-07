# Can absolute non-existence be incoherent?

## Finding

Yes: there is a valid route from a substantive account of truth to the impossibility of an experience-free reality. But the crucial truth–experience connection is **not yet established**, and even a successful no-nothingness argument would not by itself yield one necessary universal subject or the identity of every possibility with actuality.

This is an extension of the [global plan](GLOBAL_COHERENCE_AND_DECISION_PLAN.md), specifically M0 and M5, and refines the earlier [necessary-occurrence audit](NECESSARY_OCCURRENCE_CANDIDATE.md). It is philosophical analysis, not a new proof of necessary existence or a discovery in physics.

The general strategy is prior art. E. J. Lowe's anti-nihilist argument uses necessary abstract entities and their alleged dependence on concrete entities to argue that some concrete entities necessarily exist; it need not entail that any *particular* concrete entity is necessary. See the [Stanford Encyclopedia discussion](https://plato.stanford.edu/entries/nothingness/) and [Rodríguez-Pereyra's critique of Lowe](https://media.philosophy.ox.ac.uk/assets/pdf_file/0017/5840/Lowe_against_nihilism.pdf). Maximalist and non-maximalist approaches to truthmakers, including the special difficulty of negative existentials, are surveyed in [Truthmakers](https://plato.stanford.edu/archives/fall2021/entries/truthmakers/). These sources do not establish the present experiential conclusion.

## 1. Specify what 'nothing' denies

Let `C` mean that some **concrete occurrence** obtains, and `E` that some experience obtains. 'Concrete' here means actual occurrence, not necessarily an object located in fundamental spacetime; that choice preserves the user's timeless target. A particular account must still explain the term rather than rely on its label.

There are distinct claims:

1. `not C`: no concrete occurrence at all.
2. `C and not E`: something concrete, but no experience.
3. `not E`: no experience, whether or not something else exists.
4. `not Exists x`: nothing of any kind—not even abstract entities or truths—exists.

The target 'intrinsic nature = experience' would rule out case 2 if properly established. Ruling out case 1 does not by itself do so. Case 4 has additional semantic and ontological difficulties about what 'truths' and 'entities' are; calling them abstract or saying they do not exist as objects is a substantive choice, not a mere technicality.

An empty quantum vacuum is not absolute nothing; it already involves structure and laws. Conversely, an abstract mathematical description of `not C` should not be counted as a concrete world that has been shown metaphysically possible. It can test an inference without settling that metaphysics.

## 2. A valid positive argument—and its exact load-bearing premise

Let `tau` be a stipulated necessary truth, for example an instance of excluded middle in a **classical** metalanguage. Let `M_tau` say that there is an actual concrete experiential ground/truthmaker for `tau`, not merely a sentence expressing it. `Box` means metaphysical necessity, with the domain of possibilities and logic explicitly chosen.

    (N)  Box tau.
    (G)  Box (tau -> M_tau).
    (X)  Box (M_tau -> E).
    Therefore Box E.

At each admitted possibility, tau holds; G supplies an experiential truthmaker there; X says its presence entails experience. No creation in time is involved, no external observer is required, and the particular truthmaker may differ across possibilities. N is a **semantic necessity claim**. G is the heavy metaphysical claim that this truth has an *in-world concrete ground* everywhere it is true. X is true if experiential grounds are defined to be actual experiences, but that definition does not establish G.

If one instead uses `Box(tau -> concrete truthmaker)` plus `Box(C -> E)`, one gets the same conclusion in two stages. `C -> E` must say something substantive about the intrinsic nature of all concrete occurrence; calling C 'experiential' is not independent evidence that all concrete occurrence is C.

### Why this is a genuine argument but not yet a proof

- A logical truth being valid in a formal semantics does not automatically establish that a proposition is a separately existing concrete object, or that its validity has an in-world truthmaker. Deflationary or non-maximalist theories deny this inference.
- A truthmaker principle might be proposed on independent grounds. If defensible for tau, it could genuinely ground the result; one must not dismiss it *solely because its conclusion follows*. But when `Box tau` is granted, the **existential implication** `Box(tau -> M_tau)` is logically equivalent to `Box M_tau`. Thus this specific premise already carries the whole necessary-existence burden in modal extension. To be explanatory, its grounding claim needs support that does not merely reassert the desired necessity. A specified grounding relation is stronger than a bare implication and is not established by this equivalence.
- There is an asymmetry between the truth of a proposition and a token of that proposition being thought, uttered, or instantiated as an event. The latter requires an actual thinker or physical inscription; it does not follow merely from truth on every account.
- A **concrete** truthmaker is a further restriction. An abstract truthmaker, even if accepted, does not automatically give concrete or experiential actuality.
- There is also a distinction between a necessarily true sentence in a metalanguage and a necessarily existing proposition or truth-bearer. Rodríguez-Pereyra's critique presses a version of precisely this issue for Lowe.

### The negative-existential variant

Set `p = not E`. A proposed general principle that every truth must have an experiential truthmaker yields, for this particular p,

    p -> experiential truthmaker for p -> E.

In classical logic, `(not E -> E)` is equivalent to `E`; applying it at all possibilities gives `Box E`. So the desired conclusion follows **if** the truthmaker principle applies to the hypothetical absence of experience. Whether it should apply there is precisely contested: negative truths may instead be held true due to the absence of a positive falsemaker, without their own positive truthmaker. A proponent of maximalism can reject that alternative, but must argue for doing so rather than rule it out by definition. This analysis does not claim that maximalism is false or that experience-free reality is really possible.

## 3. Two controlled contrasts

**A. An actual truthmaker is not an all-possibility truthmaker.** In a two-world formal model, let tau be true in both worlds, and let experience and an experiential tau-truthmaker be present only in the actual world. This satisfies `tau` everywhere and an actual-instance truthmaking condition, but not G. The model exhibits a missing premise; it does not prove the second world metaphysically possible. A successful argument must explain why the actual truthmaking relation survives the proposed absence rather than assume it.

**B. Necessary experience is not one necessary experiencer.** Consider two mutually accessible formal possibilities. In one, experiential subject `a` exists and `b` does not; in the other, `b` exists and `a` does not. There is experience in every possibility, but neither individual exists in every possibility:

    Box (exists x: x experiences)  does not entail
    exists x: Box (x exists and experiences).

This distinction is de dicto versus de re necessity. Even a particular necessarily existing experiencer would not automatically be the **only** experiencer or the whole of reality: an additional unity/constitution argument is needed. These are countermodels to the inference, not proof that reality contains multiple subjects. Labels are formal counterparts under the stipulated two-individual semantics, not assumptions about real cross-world identity. The [enumeration](verification/necessity_nonempty_modal_audit.py) finds nine nonempty two-world assignments and two with no subject present in both; [results](verification/necessity_nonempty_modal_audit.json). It is a sanity check, not metaphysical evidence.

### Stronger identity premise: when the user's inference does follow

The preceding countermodel does **not** address a stronger starting premise in which there is already one and the same necessarily existent absolute A, and A's essential intrinsic nature is literally one universal experiential subject U. If A and U are rigidly identified (or their identity holds necessarily wherever A exists), then

    Box(exists A)  and  Box(exists A -> A = U)  imply  Box(exists U).

Thus, under these identity and necessity premises, no separate experience-producing bridge is needed: the same necessary absolute *is* that consciousness. This is an ordinary conditional identity argument, not a derivation that A exists necessarily or that its nature is this subject. Standard modal identity assumptions and what 'the same' means across possibilities should be made explicit; if the view rejects externally distinct possible worlds, its internal modal interpretation must instead be specified.

The user's formulation is **intrinsic nature = experience, plus elegance/parsimony**, not an independent premise of intrinsic nature = identity. On the intended whole-first reading, if A is necessarily actual, and its essential nature is literally experiential, then A is necessarily experiential. If 'universal consciousness' means just this one experiential absolute, the identity is already supplied by the hypothesis: no separate consciousness-generating bridge is needed. The remaining unity question is how all finite experiences and apparent subject boundaries are constituted by that one whole, not an obligation to posit additional subjects.

If the premise says only that all realized entities or aspects share an experiential intrinsic **kind**, without identifying the whole with one subject, its sharing alone does not entail one subject. Likewise, 'the totality of experiences' being one collection or whole does not automatically establish a single subject. Conversely, finite differences or restricted access do **not** prove multiple fundamentally independent subjects; that is also a conclusion needing support. One universal subject can be proposed without each finite perspective having access to every other perspective's contents. Its relation to finite subjectivity and qualitative difference remains to be explained; see the existing [intrinsic-articulation proposal](NECESSARY_ARTICULATED_UNITY.md).

Parsimony can support the identity hypothesis if it eliminates a genuinely independent ontological ingredient without sacrificing explanatory power. It is not a deductive uniqueness or necessity rule: one shared experiential kind can be realized with different subject structures, and a universal-subject theory also owes an account of the finite perspectives and physical constraints. The strength of the simplicity comparison depends on the full rival accounts. This top-down approach has important precedents in [cosmopsychism](https://plato.stanford.edu/entries/panpsychism/), including the problem of how a cosmic subject grounds finite perspectives; it is not claimed as an original framework.

## 4. Possibility = actuality requires a typed interpretation

The simple schema `possibly p -> p` cannot be applied to all unindexed descriptions if incompatible states are both possible. If `p` and `not p` are each possible, it yields both `p` and `not p` at the same context. In an ordinary S5 semantics it eliminates all expressible contingent differences across accessible worlds. That would be one possible modal thesis, not a demonstration of plenitude.

A different plenitude proposal is:

    every admissible local description p is realized in some actual sector s.

Then `p` may be true in one sector and `not p` in another without contradiction. But the realization relation, criteria for sectors and admission, global consistency, and phenomenal incidence are additional obligations. Assigning a label 'actual' to a mathematical sector does not establish concrete instantiation. If the truthmaker/necessity argument only proves that *some* experience exists, it supplies none of these sector-specific claims.

Nor does the existence of two experiential sectors fix an observer measure: even finite sectors can be assigned distinct normalized weights. Therefore it does not by itself yield a simulation probability. This is not an argument against plenitude, only a separation of logical tasks.

## 5. The next test, tied to the whole account

The high-value next question is not to repeat 'nothing is incoherent,' but to compare two precisely stated candidates:

- **Experiential grounding:** the truth of at least one necessary logical claim is intrinsically grounded in concrete experience, without presupposing a finite observer, spacetime or a thinker separate from truth.
- **Truth without experiential grounding:** the claim is valid even in a description with no concrete experiences, without treating the mathematical description as an experienced or physically instantiated universe.

### A concrete rival comparison

Take the same actual experiential and physical history `H`, including the same probability distributions for every experiment expressible in the shared physical model. Compare two extensions:

- `R_ground`: retain H; impose the all-possibility experiential-ground premise G for tau, ruling out an experience-free alternative.
- `R_open`: retain H and its actual experiential truthmaker if desired; do not impose G, and permit the formal `not E` alternative described in section 3A.

By construction, both reproduce the **same stipulated empirical distributions** in H. They differ in modal and grounding claims; data confined to those shared distributions cannot discriminate them without additional bridge assumptions. This is a conditional identifiability result, not a proof that all possible formulations of the rival theories are observationally equivalent or that the `not E` alternative is metaphysically possible. An independent argument for grounding, or a specified physical consequence where the theories diverge, could change the comparison. The quantum-record and clock work cannot be cited as picking `R_ground` merely because they document H.

The decisive next task is to develop and challenge independent support for G: state its account of truth, ground and modality; explain how it handles negative claims and unexperienced mathematical truths; and show how it excludes `R_open` without just assuming the disputed modal constraint. The positive candidate must supply a constitution, not just the sentence `truth = experience`. Then separately test whether its ground is one universal subject and whether its physical organization recovers the empirical interfaces in M1–M4.

This could become a real argument for experiential necessity if the grounding premise is independently justified. At present, the valid conditional is known; its soundness and explanatory adequacy remain open.
