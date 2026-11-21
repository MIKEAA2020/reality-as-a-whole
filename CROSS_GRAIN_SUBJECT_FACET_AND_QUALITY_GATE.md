# Subject boundaries and qualitative facets across grains

## The question and result

The existing E-L candidate uses a local mismatch bit as a **stipulated** unpleasant/neutral contrast for each of two selected pairs. A different, nine-update version of its selector instead selects the whole four-node sector. The [previous cross-scale gate](INTEGRATED_CROSS_SCALE_SUBJECT_QUALITY_GATE.md) offered two whole-quality extensions, a binary scalar and a graded scalar, while leaving subject incidence and experience postulated.

A further question matters for **full structural and experiential intelligibility**: if the two localized contrasts are to remain individually available as facets of that whole, does either scalar carry enough information to specify them? In this model, **neither does**. A small structured completion can preserve both facets and the chosen aggregate scalar, but it is only an informational construction: it neither identifies a real subject nor explains why any state is felt. This is a conditional advance about compatibility and information loss, not a solution of the subject-combination or quality problems.

The test is laid out in the [fixed plan](CROSS_GRAIN_FELT_FACET_IDENTIFIABILITY_PLAN.md), with an exact [verifier](verification/cross_grain_facet_identifiability.py), [tests](verification/cross_grain_facet_identifiability_test.py), and [receipt](verification/cross_grain_facet_identifiability.json). The plan was written before these calculations, although the underlying model and its properties were already known; no empirical study is preregistered here.

## The premise that does the work

Retain the exact four-spin physical sector with outer pair mismatches `qL,qR` and middle mismatch `m`, each 0 or 1. At one update, L selects the two outer pairs; at nine updates, the related selector selects the whole. These are **different causal queries on one kernel**, not observed successive moments, not a physical fusion and not an identity relation between subjects. No local update is an external clock or an actualization of a previously unactualized possibility.

Consider a strengthened *facet-transport* proposal:

1. Both pair-quality contrasts are independently anchored, and the nine-update whole has corresponding distinguishable, simultaneously accessible qualitative facets with the same binary values.
2. Their left/right designation refers to a physically or phenomenally grounded reference, transported under redescription. The arbitrary written names `L` and `R` themselves carry no intrinsic privilege.
3. A proposed **complete** whole-quality code uniquely determines both facets and the declared aggregate unpleasantness. It need not determine every physical variable.

These are substantive, currently unestablished assumptions. A subject may have contextual masking, a different quality scale, no such facets, or a different ownership relation. In particular, two subjects each having an experience does not imply a third subject jointly experiences their contents. A model may also treat the scalar as **one** aspect of a richer experience, rather than the complete code. None of those responses is contradicted by the calculation. We are not assuming that all parts of an experiential ground are subjects or that the whole is a universal subject.

## Same sector, three representational proposals

The exact equilibrium distribution over edge mismatches is the product of outer probabilities `Pr(q=1)=1/4` and middle `Pr(m=1)=3/8`. This is a probability distribution of a stipulated model, not an experiential measure over all actuality.

The earlier whole-subject quality extensions use:

```text
binary:  B = 1 if any of qL, m, qR is 1; otherwise 0

graded:  D = [ln(3)(qL+qR) + ln(5/3)m] / [2 ln(3) + ln(5/3)]
```

Both obey the previously postulated pair contrast when restricted to the selected pair. B and D are alternative aggregate **quality postulates**; the spin model does not establish that either is unpleasantness. Now compare:

| Complete code, if claimed | Number of possible values | Can recover each marked facet? | Minimum model-weighted error for either facet |
|---|---:|---|---:|
| `B` alone | 2 | No | `1/4` |
| `D` alone | 6 | No | `3/16` |
| Structured `(B,qL,qR)` | 5 | Yes | 0 |
| Structured `(D,qL,qR)` | 8 | Yes | 0 |

The error column is the exact best possible 0/1 classification error for **one specified facet at a time**, when the predictor knows the model distribution and the labels. It is an oracle in-sample/model bound, not a confidence interval, human prediction error, or evidence that a brain is wrong. The two structured codes preserve their respective scalar as well as the two facets. Five and eight values each require at least three fixed-length binary digits, and a three-digit code suffices; this is a cardinality bound, not a neural-bit or consciousness capacity measurement. The binary structured code does not recover the middle mismatch in every state, and nothing here requires it to.

The graded scalar takes six distinct values, represented exactly by `(qL+qR,m)`. To see this without numerical rounding, if two such pairs gave the same D, then an integer multiple of `ln 3` would equal an integer multiple of `ln(5/3)`. Exponentiation and unique factorization of 3 and 5 force both integer differences to be zero. This is a straightforward application of unique factorization, not a new information-theoretic theorem.

## Why the scalar-only codes lose facets

Two explicit positive-probability configurations are enough for each failure. Write triples as `(qL,m,qR)`.

- For `B`, `(0,0,1)` and `(1,0,1)` both have `B=1`, but their left facet is 0 and 1 respectively. Their model probabilities are `15/128` and `5/128`.
- For `D`, `(0,0,1)` and `(1,0,0)` give the same aggregate value because `qL+qR=1` and `m=0`, but their left facets differ. Each has probability `15/128`. The same holds for `m=1`, each with probability `9/128`.

The aggregate binary value is zero only at `(0,0,0)` and is one otherwise. In the `B=1` fiber, the total weight with `qL=1` is `32/128` and with `qL=0` is `51/128`; the best constant prediction makes errors of `32/128=1/4`. For `D`, ambiguity occurs exactly when `qL+qR=1`, whose model weight is `3/8`; symmetry splits that weight equally, yielding the error `3/16`. Analogous statements hold for the right facet.

These results use the established elementary **fiber criterion** already developed in [common constitution closure](COMMON_CONSTITUTION_CLOSURE.md): a target is a function of a code exactly when it is constant on each code fiber. We do not present that criterion or the general source-coding bound as novel derivations. The novel application is to the particular cross-grain extensions and marked facets of this candidate; it has not been validated phenomenologically.

## Relabeling is not qualitative erasure

Reflection exchanges the left and right ends and leaves B, D and the physical probability unchanged. Under that redescription, the structured code's two facets **swap**. It would be wrong to demand a rule choose an absolute intrinsic “left” in the symmetric whole. Conversely, once a side or phenomenal role is independently fixed as part of the target, the symmetric scalar alone cannot reconstruct which designated facet is present. If only the unordered multiset of facets is phenomenally relevant, the graded scalar already determines that multiset; the marked-facet failure would not decide that weaker proposal. Nothing here shows that a sensory field has an objectively preferred absolute side, or that the two subjects have shared experiential tokens.

## What this changes—and what it does not

**Positive construction:** a proposed whole-level model can retain the pair contrast while using a richer, structured target instead of trying to make a single aggregate scalar bear the entire qualitative burden. The structured completions are economical in the restricted combinatorial sense above and equivariant under the simple reflection. This makes the project more precise: a real successor must supply facet incidence, a reference structure and a joint phenomenal field, not merely another value of a discomfort score.

**Precise limitation:** the original extensions expressly propose only a scalar unpleasantness value, not a complete description of experience. Therefore the calculation does **not** refute them as scalar laws; it rejects only an added claim that the scalar alone is a complete code while both marked facets are recoverable. Adding the bits is not a defensible constitution: their grouping and interpretation are stipulated, and the code says nothing about which subject has them. One person may report multiple contents together, but pair or whole reports do not automatically reveal other perspectives, establish numerical token sharing, or distinguish one subject from two.

The model-independent challenge is not merely more bits: a complete theory must justify **why** an appropriate structured relation is intrinsically lived, why these distinctions are its particular qualitative character, and which occurrence owns them. A single scalar can in principle have many values and a formal code can contain arbitrarily much information; neither informational richness nor a relabeling-invariant representation constitutes an experiential explanation. Subject persistence and cases of branching still need a separately defended identity/continuity law. No evidence here chooses an experiential ground over the experience-respecting neutral-ground rival, and the latter also owes a constitution bridge.

Thus B4–B5/F2, B9/F3 and B10 remain open. The target remains a timeless self-sufficient relational whole with genuine plural subjects, not a universal consciousness, and the actuality of genuine possibilities is not a mechanism of temporal conversion. No global subject count, Born weights, physics recovery or necessity of the proposed ground follows.

## Relation to established work and source coverage

[Chalmers, *The Combination Problem for Panpsychism*](sources/uploads/combination.pdf) distinguishes subject, quality, structure, unity and boundary problems; it also stresses that a phenomenal bonding relation must explain both the subject and the palette. Its **structural mismatch** argument concerns a discrepancy between physical and phenomenal structures; this differs from the candidate's proposed physical *misalignment* as unpleasantness. At the time of this facet calculation, the online extract was truncated at the beginning of section 8. The subsequent [full supplied-manuscript audit](CHALMERS_COMBINATION_FULL_PAPER_AND_STRUCTURE_AUDIT.md) reads all 37 pages, including the rest of the structural argument, and distinguishes the manuscript from the uninspected published version. This project does not assert that Chalmers's micro-subject or whole-universe-subject premises are the user's own.

[Albantakis et al., *Integrated information theory (IIT) 4.0*](https://doi.org/10.1371/journal.pcbi.1011465) explicitly proposes a richer cause–effect structure and an explanatory identity, with rules for maximal substrates and ties. The abstract was read here and selected exclusion/tie material was available via search excerpts; full methods, proofs, figures, supplementary files and implementation were **not** re-audited. Our L score and three-bit example are not IIT and the factorization result does not refute IIT's full structure.

[The Combination Problem: Subjects and Unity](https://doi.org/10.1007/s10670-016-9808-8) argues, in its abstract, against treating impossibility of subject combination as established. The publisher supplied an abstract and notes but presented the main text as subscription content; full argument and figure were **not inspected**. That is a live experience-respecting counterpoint, not a solved bridge.

The abstract of [Cogitate Consortium, *Adversarial testing of global neuronal workspace and integrated information theories of consciousness*](https://doi.org/10.1038/s41586-025-08888-1) reports evidence challenging specific predictions of both theories; its full text, figures, supplement, preregistration, code and data were **not read for this gate**. The abstract of [*Open multi-center intracranial electroencephalography dataset with task probing conscious visual perception*](https://doi.org/10.1038/s41597-025-04833-z) describes a 38-patient dataset using suprathreshold stimuli and target detection; its full methods, figures, raw signals and trial-level reports were **not examined here**. Neither abstract establishes a direct co-consciousness, discomfort or subject-boundary assay. Their availability does not justify a bulk data download or new invasive experiments.
