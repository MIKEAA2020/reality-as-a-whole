# Step 39 — Non-additivity and macro-causal relevance do not select a qualitative identification

## Finding

The [non-additive constitution argument](../../NONADDITIVE_CONSTITUTION_ARGUMENT.md) constrains the causal placement of experience under substantive premises. It does not by itself identify which physical state is which experience.

A finite realization audit makes the gap explicit. Multiple candidate target maps can simultaneously:

- be deterministic macro-coordinates of the actual physical state;
- introduce no independent extra causal agent;
- support well-defined physically implemented contrast interventions;
- preserve all physical dynamics and report predictions;
- satisfy the same partial target calibration.

The audit does **not** establish that a toy register is conscious or that qualitatively inverted worlds are metaphysically possible. It establishes that the listed mathematical/causal conditions fail to select the identification within an explicitly supplied candidate class. Genuine phenomenal efficacy remains a stronger premise than macro-coordinate relevance and is not demonstrated by this model.

## 1. Physical model and candidate identifications

The physical state is X∈{0,1,2,3}, with dynamics and report

\[
T(X)=(X+1)\bmod4,\qquad R=X.
\]

These rules are held fixed. Introduce four hypothetical target contrasts a,b,c,d and consider the 24 bijections

\[
f:\{0,1,2,3\}\longrightarrow\{a,b,c,d\}.
\]

Each candidate proposes E=f(X). E is a macro-coordinate of the physical state, not an independently evolving hidden variable or a second physical causal channel. The target names are assumed to have fixed intended reference when comparing candidate assignments. No actual phenomenal measurements warrant that reference in the toy example; it is supplied as the identification problem to be solved.

If the letters are only freely interchangeable notation, their permutation is a re-description rather than a competing qualitative hypothesis. A supposed inversion cannot be inferred merely from exchanging symbols. This distinction is essential to interpreting the example.

## 2. Non-additivity and physical dynamics are satisfied by every map

For every f, the target-coordinate dynamics is

\[
T_f=f\circ T\circ f^{-1}.
\]

Writing the report in those coordinates gives R=f⁻¹(E), so the resulting physical report remains X. No new physical decoder is inserted; f⁻¹ is a mathematical re-expression of the same report rule. Every candidate therefore gives identical physical histories and intervention predictions.

A target contrast intervention can also be defined operationally **conditional on the candidate**:

\[
\operatorname{do}(E=e)\quad\text{means implement}\quad
\operatorname{do}(X=f^{-1}(e)).
\]

Distinct target coordinates then yield distinct reports. This is macro-causal relevance under declared implementations, not epiphenomenal annotation. But the implementation itself depends on f; it is not an independently supplied phenomenal manipulation. A protocol that already knew how to set the actual experience e could supply precisely the additional identification information that is missing.

Thus causal manipulability in these coordinates is compatible with every bijection. It cannot establish which coordinate actually has a specified qualitative character. Nor can this exercise bootstrap genuine phenomenal efficacy from the fact that a register intervention changes a report.

## 3. Partial calibration does not finish identification

Supply the synthetic anchors

\[
f(0)=a,\qquad f(1)=b.
\]

Exactly two candidates remain:

| Physical state | Candidate A | Candidate B |
|---|---|---|
| 0 | a | a |
| 1 | b | b |
| 2 | c | d |
| 3 | d | c |

They agree on the supplied anchors, have no extra independent cause, and preserve all physical predictions. They disagree on the unanchored target identification and on the target-coordinate succession beyond the anchors.

For example, setting target c requires physical intervention X=2 under A and X=3 under B. This difference is not a new experimentally accessible physical prediction unless the ability to identify or manipulate c independently is warranted. Under the same physical intervention X=2, both predict the same physical report R=2.

A warranted third anchor f(2)=c selects A **within this restricted bijective class**. An independently warranted target-succession or qualitative-relation constraint might also exclude a candidate. Their warrant cannot be replaced by a convention that defines c as whatever X=2 produces and then calls the result an independent discovery.

Two distinct physical states mapped to the same target would reject this bijective class, rather than justify forcing the data to fit. The hypothesis class is a substantive restriction.

## 4. What this says about the causal argument

The conditional causal-exclusion reasoning can still motivate rejection of an independent extra phenomenal agent. This audit does not refute that reasoning.

It shows that its explicitly modeled consequences—physical realization, no extra channel, and interventionally effective macro-coordinates—remain compatible with multiple proposed identifications. They do not select χ. No Γ is introduced or inferred either.

Care is needed about the strength of the conclusion:

- This is not a demonstration that all alternatives satisfy genuine phenomenal efficacy. The model contains no independent phenomenal evidence establishing that premise.
- It is not a proof that a complete causal identity theory cannot identify qualities. Such a theory may impose further substantive constraints not present here.
- It is not an argument that qualitative differences require new physical forces or noncausal substances.
- It is a counterexample to the claim that the listed realization/causal-coordinate conditions alone determine the qualitative map.

The additional premise must therefore concern the specific qualitative identification, not merely repeat that an implemented physical process is causally effective.

## 5. Calibration, identity, and explanation remain distinct achievements

Even if evidence supplied all four target assignments, three different claims would remain:

1. **Identification in this model:** the supplied constraints select a particular f.
2. **Constitutive identity:** the selected physical organization is the qualitative occurrence, rather than a reliable correlate or determining condition.
3. **Ultimate explanation:** why this qualitative-physical constitution and its laws are actual.

Evidence can justify an identity inference by explanatory comparison; it need not take the form of a deduction from physics alone. But the explanatory argument must be stated. Calibration cannot be treated as if it already proved the identity and its foundation.

The relevant positive direction is to seek constraints that jointly explain qualitative relations and physical organization, then test whether they genuinely select an identification rather than merely encode it. The current construction supplies no such completed constraint.

## 6. Verification and integration

`model.py` enumerates the bijections, anchors, conjugated dynamics, implemented target-coordinate interventions, and unchanged physical predictions. Twelve tests verify the exact counts, surviving ambiguity, physical prediction equivalence, intervention dependence on the candidate, and selection/rejection by additional anchors. `enumeration.json` records the surviving maps and witnesses.

The model does not assign actual consciousness to its states. Passing its tests establishes finite combinatorial and causal-coordinate facts, not empirical phenomenal sufficiency or the truth of the philosophical premises.

## Current conclusion

Non-additive realization remains a candidate architectural constraint, not the missing qualitative law. Making a process causally active does not by itself tell us why it is a particular experience. The inquiry now has an explicit, checked demonstration of this insufficiency rather than only a verbal caution. A further noncircular qualitative identification and composition argument is still required.

## Follow-up: genuine target differences or notation?

[The qualitative-equivalence audit](../../QUALITATIVE_EQUIVALENCE_AUDIT.md) develops the reference qualification above and tests whether a proposed equivalence criterion legitimately removes ambiguity or merely assumes the desired identity.
