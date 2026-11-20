# Timeless ground, located totality and experiential actuality

## Result

A fundamental reality can be non-spatiotemporal while its derivative contents are spatiotemporally located, **but the word “whole” must not conceal two different entities**. On a common inheritance principle for location, a whole with a located part is itself weakly located. Therefore the following four claims cannot all hold in the same sense of part and location:

1. A fundamental ground is not spatiotemporally located, even weakly.
2. There is a spatiotemporally located derivative entity.
3. That derivative entity is a part of the fundamental ground.
4. A whole inherits weak location from any exactly located part.

This is a conditional metaphysical incompatibility, not a physics theorem. A candidate resolution is to distinguish **the ground**, which is non-spatiotemporal, from **the totality of what exists**, which includes both the ground and the located derivative entities. The totality can inherit their location while the ground does not. Located derivative entities must depend on the ground by something other than parthood *in the relevant sense*. Neither dependence nor the emergence of spacetime is thereby explained.

The distinction adapts a published proposal by Baron and Pohlmann, cited below; it is not presented as a novel derivation. The project-specific advance is to combine that constraint with the framework's **necessary actuality and experiential plurality**, then test whether it closes the experiential-ground gap. It does not: even a necessary, non-spatiotemporal ground whose totality includes real experiences need not itself have an experiential intrinsic nature without an additional bridge.

## 1. Separate the commitments

Call the non-spatiotemporal basic reality `B`, the all-inclusive totality `W`, and a derivative located object `s`. Let `P(x,y)` mean x is a mereological part of y; `L(x,r)` means exact location at region r; `WL(x,r)` means weak location at r. The relevant inheritance assumption is

```text
P(x,y) and L(x,r)  ->  WL(y,r).
```

Assume `L(s,r)` and no weak spacetime location at all for `B`. If `P(s,B)`, inheritance gives `WL(B,r)`, contradicting the assumed non-location of `B`. The contradiction does **not** follow if `P(s,W)` but not `P(s,B)`. The totality `W` may be weakly located, while `B` remains unlocated. Being weakly located in derivative spacetime is **not** the same as being contained in an external spacetime, evolving in external time, or having fundamental spacetime. Nor does it imply that all of W is exactly located at r.

This choice is not forced: one can question the inheritance principle, the claim that fundamental entities lack even derivative locative properties, the existence of located derivative objects, or the mereological interpretation. A blanket statement that a timeless whole cannot have any locative properties already adopts a controversial premise. Equally, a declaration that its located contents are literally its parts imports the inheritance problem if that principle is accepted. Fundamental timelessness here means no *fundamental or external* time; whether the all-inclusive totality bears derived temporal or locative predicates is a separate question.

## 2. A tiny consistency model

Treat `b` and `s` as distinct atoms and `w` as their fusion: the only parthood relationships are reflexive ones and `b P w`, `s P w`. Use a single region and a Boolean proxy for weak location. Set `b` unlocated and `s` located. Inheritance then forces `w` located; all premises are consistent. Add `s P b` with the same inheritance rule and the model becomes inconsistent. The executable check [timeless_whole_location_gate.py](verification/timeless_whole_location_gate.py) exhausts all eight location assignments for this three-object proxy.

The proxy does not implement exact locations, nontrivial spacetime geometry, observers, quantum gravity, or a theory of emergence. The abstract conditional proof above uses exact and weak location separately. In particular, this Boolean example demonstrates only that the stripped-down commitments are logically compatible when stipulated; it does not show that the proposed entities exist or that the priority direction is correct.

A proponent may call `B` the “fundamental whole” and `W` the “total whole”, but must state which is meant in each claim. `B` may have non-spatiotemporal parts and need not be simple. This bookkeeping does **not** introduce an external creator or a universal subject. If the framework instead insists that “the whole” means all of reality and is itself fundamental, it must either revise the literal parthood/location package or make clear why it does not apply. Saying “within” need not mean literal parthood; using it that way requires an explicit alternative relation.

## 3. Necessity and concreteness: a further project-specific constraint

Under the project's stipulated global principle, actual global propositions are necessary when the principle also applies to their negations; [the prior self-presence gate](SELF_PRESENCE_AND_NO_NOTHINGNESS_UNIFICATION.md) shows the relevant inference. Thus real experience and concrete actuality can both be necessary on that scope without a creator or temporal actualization. This says nothing by itself about whether the fundamental basis is experiential.

The distinction also matters for a suggested definition of concreteness. Baron and Pohlmann's footnote 14 proposes, as a way to exclude necessary abstract entities from their universal mereological world, defining concrete things as **contingent parts** of it. Their solution is explicitly conditional on the relevant abstract entities being necessary. It is **not usable unchanged** for this project if the actual ground is necessarily existent and intended to be concrete: it would classify `B` as non-concrete. If the global principle extends to the existence of each particular actual part, it also excludes those necessarily existing particulars, not merely the ground. That further result depends on the scope and identity conditions of the modal principle; necessary existence of the whole alone does not entail necessary existence of every part.

This is not a refutation of the authors' theory: they do not adopt this project's modal assumptions, and their footnote offers a possible modification, not their only definition. It is a compatibility constraint on *borrowing* that modification. Calling the totality “concrete” by universal parthood, on the other hand, risks counting mathematical objects as concrete if they are admitted to that same universal fusion; restricting the domain to concrete entities presupposes a workable classification. No solution follows just by changing the label.

A more cautious project interface is to treat `Concrete(x)` as a primitive classificatory predicate, allowing a non-spatiotemporal and necessary `B`, and separately state whether mathematical objects exist and whether they are members or parts of `W`. This is **a placeholder**, not an independent account of what makes `B` concrete. A successful account must provide a non-circular criterion that distinguishes actual experience from an uninstantiated mathematical description without making spacetime, contingency or an external observer necessary for concreteness. One can also reject universal mereological fusion entirely and construe totality as a domain or structured plurality; that requires its own account of inclusion and dependence.

## 4. The experiential-ground bridge remains open

Consider two formal interpretations with the same `B`, `W`, located derivative `s`, the same public relational and record predicates, and actual experience attributed to a derivative occurrence:

- **Experiential-base label:** `B` is intrinsically experiential, with plural experiences dependent on it.
- **Neutral-base label:** `B` is not itself experiential, while real experience depends on it.

Both can be assigned the same singleton global modal frame, so every actual global proposition, including “there is experience”, is necessary. The verifier checks this limited labelling consistency and that the shared public predicates do not select the intrinsic label. It does **not** construct a neutral mechanism producing experience or an experiential mechanism constituting plural subjects; nor does logical relabelling prove either a genuinely possible metaphysical world. The example isolates precisely what the current premises fail to specify.

The project therefore still needs a positive, independently motivated constitution linking (i) the intrinsic nature of `B`, (ii) the differentiated experiences and boundaries of multiple subjects, and (iii) effective spacetime and the physical records those subjects can access. Requiring all three is not the same as making the whole one subject. It also makes clear why necessity of experience, and a non-spatiotemporal ground, do not settle experiential fundamentality or self-explanation.

## 5. Work needed next

1. Give an explicit, domain-limited definition of inclusion and dependence; decide whether `W` is a mereological fusion or a non-mereological totality. State exactly which location predicates the ground and the totality can have.
2. Make the scope of possibility–actuality precise for global claims, indexed local claims and identity across descriptions; do not infer that all local alternatives hold in the same context.
3. Construct competing experiential and neutral dependency accounts with the **same real experiential data**, not merely a zombie rival. Identify a non-question-begging discriminator, including how a phenomenal constitution rule avoids simply stipulating its answers.
4. Derive candidate local records, geometry and temporal order from a specified non-spatiotemporal structure, with controlled limits and observational links. The present model is not such a derivation. Respect the separate constraints on quantum records, subject count, and self-location in the [battery dossier](CURRENT_FRAMEWORK_BATTERY_DOSSIER.md).
5. Supply a non-circular reason for actual self-sufficiency and necessity; naming `B` a ground or labelling it experiential does not show that its existence or character is self-explanatory.

## Source and scope

- Sam Baron and Jessica Pohlmann, [“Priority monism and the emergence of spacetime”](https://doi.org/10.1007/s11229-024-04859-7): all 14 HTML text chunks read, including notes and references. Their figures were described in the text but not independently inspected. They distinguish world and cosmos, propose non-mereological dependence, and discuss several alternatives; the paper itself does not establish the project's phenomenal ground or actual quantum gravity. Its claim that fundamental entities lack spatiotemporal location is a premise associated with the models considered, not an experimentally established universal fact.
- David Chalmers, [“Phenomenal Concepts and the Explanatory Gap”](https://consc.net/papers/pceg.html): chunk 0 of 12 read; the remaining available text was not read. The initial section presents a contested argument concerning the explanatory gap, not an established resolution.
- Matt Duncan, [“Subjectivity as Self-Acquaintance”](https://philarchive.org/archive/DUNSAS-5): chunk 0 of 9 read; remaining available text unread. Its account is presented as neutral about reductionism and physicalism.
- Anna Giustina, [“An Acquaintance Alternative to Self-Representationalism”](https://philarchive.org/archive/GIUAAA): chunk 0 of 14 read; remaining available text unread. Its conditional case does not establish an experiential foundation.
- François Kammerer, [“The illusion of conscious experience”](https://doi.org/10.1007/s11229-018-02071-y): publisher abstract and preview only; main article was subscription-restricted at the accessed page. The paper challenges the project's experiential datum; the present gate does not purport to refute it.
- Thomas Oberle, [“Metaphysical Foundationalism and the Principle of Sufficient Reason”](https://www.cambridge.org/core/journals/dialogue-canadian-philosophical-review-revue-canadienne-de-philosophie/article/metaphysical-foundationalism-and-the-principle-of-sufficient-reason/7E67DFE251072B0B97BAB6E20CC0D0B2): chunk 0 of 14 and search excerpts only; the available remainder was not read. Claims about how grounding and sufficient reason interact remain contested.
- [“Metaphysical foundationalism”](https://doi.org/10.1007/s11098-025-02444-3): chunk 0 of 9 and search excerpts only; the open-access remainder was not read. It distinguishes strong well-foundedness from weaker foundational requirements.
- Matteo Morganti, [“Ontological Priority, Fundamentality and Monism”](https://philarchive.org/archive/MOROPF): chunk 0 of 8 and search excerpts only; remainder available but unread. It questions priority monism and the foundationalist assumption.

Source reading does not imply endorsement of the authors' ontologies or the project's stronger necessity claims.
