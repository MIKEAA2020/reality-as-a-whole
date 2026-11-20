# A relational whole with plural unified subjects: a finite constitution model

## 1. The question and the result

Can one relational whole include several genuinely distinct, individually unified subjects without the whole itself being one universal subject? **A finite formal model can represent that combination without contradiction among its stipulated rules.** But the model does not establish that its stipulated experiences or subjects exist, that shared experiences are metaphysically coherent, or that our world has this structure.

The construction distinguishes a whole's relational connectedness from the phenomenal unity of a subject. In the example, the same experienced aspect is shared between two individually unified fields. The resulting structure is connected, but no field contains all its aspects. Individual finite same-subject closure holds even though the existential relation “some subject experiences these two aspects together” is not transitive. Thus the weaker, existential relation cannot replace Bayne and Chalmers' subject-indexed unity principle, and connectedness of the whole does not produce a universal subject.

The strongest useful finding is a **conditional characterization**, not the stipulated example itself. In a finite downward-closed model of actual joint states, if every state is owned, ownership is downward closed, and every subject's states satisfy same-subject subsumptive closure, then every maximal joint state needs an owner. If subjects are identified extensionally by their owned states, the admissible number of subjects ranges from the number of maximal states through the number of nonempty states. Exactly the maximal states are subjects only with an additional *no-nested-subjects* rule. If ownership must instead be exclusive, overlapping maximal states cannot satisfy these assumptions at all. These alternatives expose where a subject-individuation rule enters rather than hiding it in a graph algorithm.

This is a model-relative application of standard finite order and simplicial-complex ideas, **not a claim of a new general mathematical theorem**. The objects are representations of stipulated experiences, not an argument that structure alone produces experiential presence. The project accepts experience as a datum and prefers an intrinsically experiential, timeless relational ground. C3 remains **full structural and experiential intelligibility**, jointly with C1–C7; the construction does not establish C3 or the entire framework.

## 2. Prior work and source scope

[Bayne and Chalmers, *What Is the Unity of Consciousness?*](https://consc.net/papers/unity.html), sections 2–3, distinguish subject-indexed phenomenal subsumption from access and from merely having a conjunction of mental states. They argue that pairwise unity within one subject gives finite closure under a transitivity premise; they do not prove their unity thesis and leave overlap unresolved. The full linked HTML, notes and references were read in the [three-paper audit](THREE_UNITY_PAPERS_READING_AND_FRAMEWORK_AUDIT.md).

[Schwitzgebel and Nelson, *When Counting Conscious Subjects, the Result Needn’t Always Be a Determinate Whole Number*](https://faculty.ucr.edu/~eschwitz/SchwitzPapers/CountingSubjects-250528.pdf), section 6, discuss how counting overlapping maximal fields can become problematic and why sharp counts need not settle subject individuation. The linked manuscript's argument, notes and captions were read, but the last bibliography pages and figures 2–4 of that manuscript were not fully inspected; see the audit for exact scope.

[Lopez, *A layered unity model of split-brain consciousness*](https://doi.org/10.1007/s11098-025-02339-3), sections 3–4, offers partial unity within split-brain consciousness and considers nontransitivity and duplication. The complete article text, notes, references and captions were read; its nine figure images were not visually inspected. Our model permits overlapping fully unified subjects as **one different interpretation**, not a reinterpretation proven equivalent to Lopez's account of partially unified consciousness.

The basic mathematics is established. Doktorova, [*Constructing Simplicial Complexes over Topological Spaces*](https://digitalcommons.dartmouth.edu/cgi/viewcontent.cgi?article=1019&context=masters_theses), sections 1.2 and 2.1, defines simplicial complexes and warns that a clique complex assumes all pairwise-related items form a higher-order relation. We inspected those introductory and background passages, **not the entire thesis, algorithms, experiments, figures or proofs**. This mathematical source does not claim simplicial complexes are conscious.

## 3. What the finite representation assumes

Fix one locally specified experiential window, not a universal clock or preferred relativistic slice. Let `V` be a finite set of *already stipulated* elementary experiential aspect-tokens. Let `K` be a nonempty family of nonempty subsets of `V`, closed under nonempty subsets. Each `σ∈K` is stipulated to denote one actual phenomenal state whose component aspects are exactly `σ`; inclusion is stipulated to be phenomenal subsumption. Thus `K` is the nonempty part of an abstract simplicial complex, and its inclusion-maximal elements are its **facets**. The terminology does not require a spatial embedding.

These are strong restrictions: an actual phenomenal field need not have a unique atomic decomposition; distinct phenomenal states might have the same aspects, be holistic or context-dependent, or not correspond to sets at all. A face is not merely a combination of stimuli, a correlation, a report or a combinatorially possible set. The model assumes that each face stands for an actual phenomenal state, and does not infer it from physical data. It also does not equate qualitative similarity with numerical identity: a vertex represents the *same stipulated token* wherever it occurs.

Now let a subject `s` own a nonempty family `D_s⊆K`. We make three explicit assumptions:

- **Downward ownership:** if `σ∈D_s` and `∅≠τ⊆σ`, then `τ∈D_s`.
- **Same-subject subsumptive closure:** for every `σ,τ∈D_s` there is `ρ∈D_s` with `σ∪τ⊆ρ`.
- **Coverage:** every state in `K` is owned by at least one subject.

Subsumptive closure concerns the *same subject*, including the encompassing state. It does not say that arbitrary pairs of states sharing different owners can be subsumed by a single subject. Coverage does not say there is a single subject owning all states. The existence and individuation of subjects remain assumptions, not outputs of bare mathematics.

For the counting result only, add **extensional identity**: subjects are identical exactly when their owned-state families are identical. This thin-bundle assumption rules out two numerically distinct subjects with precisely the same owned states. A substantive subject theory may reject it. It also omits experiential details and contexts not encoded in `K`; two actually different perspectives could be collapsed by this coarse model.

## 4. Derivation: what closure does and does not select

Because `K` is finite, `D_s` is finite. Iterating same-subject closure yields a state `F_s∈D_s` that contains every member of `D_s`. Since `F_s` is itself a member, it equals the union of all the aspect sets in `D_s`. By downward ownership,

```text
D_s = { σ ∈ K : σ is a nonempty subset of F_s }.
```

Conversely, every face `F∈K` defines such a closed, downward-owned family. Thus, in this finite model, a completely unified subject can be represented by a single face as its total state. This is a consequence **conditional on the representation and ownership axioms**, not an independent argument that actual subjects are sets.

Let the facets be `M₁,…,M_m`. By coverage, each facet `M_i` is owned by some subject. Its subject's total state `F_s` contains `M_i`; because `M_i` is maximal in `K`, `F_s=M_i`. Therefore all facets must occur as subject supports. Extensional identity means they give at least `m` different represented subjects.

But coverage and closure alone do **not** forbid another subject with a proper subface as its total state. Under extensional identity, any selection of additional nonmaximal faces gives another admissible family of subjects. If `N=|K|`, every count

```text
m, m+1, …, N
```

is attainable: include all facets and choose that many additional distinct nonmaximal faces. This count includes only subjects represented by this finite model, not subjects elsewhere. If extensional identity is dropped, additional distinct subjects with the same owned family can be stipulated; the finite upper bound `N` no longer follows.

**Maximal-field rule.** Add the separate constraint that no subject's total state is properly included in another subject's total state. Coverage then forces exactly the facets as supports and, with extensional identity, exactly `m` subjects. This is a substantive exclusion of nested subjects. It is not supplied by closure, parsimony, or phenomenal unity alone; nor does it answer Schwitzgebel and Nelson's criticism that nearly identical overlapping fields might be a poor subject census.

**Exclusive ownership.** Instead require that no state has more than one owner. If two facets intersect at any vertex, their necessarily existing facet-owners would both own the nonempty intersection by downward ownership. Exclusive ownership is therefore impossible. If the facets are pairwise disjoint, assigning one owner to each facet is valid and is the only covering assignment under these assumptions. This is a formal conflict among the premises, not an empirical proof of overlap or of exclusivity's falsity.

## 5. Worked example: connected whole, two unified fields

Let `V={A,G,B}` and let `K` contain exactly

```text
{A}, {G}, {B}, {A,G}, {G,B}.
```

Assume `A`, `G`, and `B` are numerically distinct stipulated aspect-tokens. `G` is the **same** token in both compound states, not two equal-looking copies. The two facets are `{A,G}` and `{G,B}`; there is no state `{A,B}` or `{A,G,B}`. Postulate two subjects:

```text
D_left  = {{A}, {G}, {A,G}}
D_right = {{G}, {B}, {G,B}}.
```

Each subject has a total state containing all its states and meets the finite same-subject closure rule. The family is connected through `G` and neither subject owns all three aspects. Yet A is jointly experienced with G by the left subject, and G with B by the right subject, while no subject jointly experiences A and B. Existential co-occurrence is therefore nontransitive, without a violation of within-subject closure. The relational whole is not thereby a subject: there is no third total state containing all three, and no such subject is stipulated. This is a possible *formal interpretation*, not evidence for actual shared consciousness or proof that no larger subject exists outside the model.

In the extensional model above, the minimum is two subjects, but the maximum is five: subjects whose total states are `{A}`, `{G}`, or `{B}` can additionally be included. With maximal-field exclusion, the count becomes exactly two. The two facets share `G`, so exclusive ownership is inconsistent with coverage and closure. All these claims depend on taking the listed states as the **complete** `K` for this example.

The structure also has a relabeling symmetry exchanging `A` with `B` and the two facet-subjects. The *family* of both subjects and the count two are invariant even though neither subject is intrinsically designated “the left one” by this symmetric structure alone. This avoids the earlier demand to select one privileged node, but symmetry does not prove that the two formal supports are real subjects. Qualitative features that break the symmetry may legitimately distinguish them if independently present, not invented to select a preferred subject.

## 6. What the same experiential incidence cannot decide

Keep the same five stipulated states and ownership-downward condition, but suppose instead that **one** subject owns every state. That alternative has one partially unified subject: `A` and `B` belong to it, yet no owned state subsumes them together. It therefore **rejects same-subject subsumptive closure**. The two-subject and one-subject descriptions agree on the state incidence `K`, but disagree about the ownership rule and the truth of the unity thesis. They are distinct formal interpretations, not a demonstration that a single partially unified subject is metaphysically coherent or that behavioral records will settle the choice.

An analogous loss occurs even earlier if only pairwise incidence is available. For `V={A,B,C}`, compare a full triangle, including `{A,B,C}`, with the hollow triangle containing all singleton and pair faces but not the triple. They have the same pairwise incidence. Under coverage, closure and extensional identity, their **minimum** counts are respectively one and three. This restates the higher-order incidence problem in standard complex language; it is not a novel mathematical observation. Neither model identifies a real triple experience from pairwise reports.

Thus there are at least three independent questions: which phenomenal conjunctions are real; which subjects own them; and whether subjects may be nested or overlapping. Even perfect knowledge of `K` would not by itself answer the second or third. The [shared-token gate](SHARED_EXPERIENCE_VERSUS_DUPLICATED_TOKENS_GATE.md) gives a separate reason why ordinary reports may not determine whether a putatively shared `G` is one token or two.

## 7. What a full account still owes

1. **Experiential ontology:** explain why the ground is intrinsically experiential and how its occurrences and qualities are individuated without imposing finite atoms or assuming one cosmic subject. Showing that a diagram is consistent is not that explanation.
2. **Constitution and higher-order unity:** derive or independently motivate a relation that fixes real phenomenal joint states and subject ownership; specify whether context can change the character or identity of shared aspects. Explain the choice among maximality, nesting, overlap and partial unity, rather than selecting whichever gives the desired count.
3. **Physical correspondence and substrate independence:** say which physical or relational realizations correspond to these states, what makes distinct realizations equivalent or distinct, and which transformations preserve the *phenomenal* facts. Mere relabeling invariance, causality, and connectivity do not establish this mapping.
4. **Evidence and temporal extent:** anchor particular experiences in first-person evidence while modeling report, attention, access and error. Address window choice, persistence, fission and recombination without assuming fundamental spacetime or an external universal clock.
5. **Whole and necessity:** explain self-existence and why this self-sufficient whole, and how genuine possibilities are actual within it. Do not posit an external creator, a temporal actualization mechanism, a literal simulation or a universal consciousness as a shortcut.

The finite construction reduces a specific ambiguity to explicit commitments. It does not establish the actual plural subjects, the complete qualitative and physical laws, or **full structural and experiential intelligibility**.

## 8. Reproduction

Run [`verification/phenomenal_facet_subject_gate.py`](verification/phenomenal_facet_subject_gate.py); the [receipt](verification/phenomenal_facet_subject_gate.json) checks all 189 nonempty complexes on up to four labeled ambient vertices and all 32,902 covering subject-support families in the model, the counting ranges, exclusivity criterion, symmetry example and filled/hollow triangle. Ambient vertices not appearing in a complex are not treated as experiences. The proof above establishes the finite statements generally; the program checks bounded cases and does not test consciousness or certify the physical or philosophical premises.
