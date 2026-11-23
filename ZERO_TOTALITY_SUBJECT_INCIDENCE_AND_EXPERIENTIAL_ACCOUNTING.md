# A candidate incidence principle for a plural experiential whole

## The proposal

**Relational-time continuation:** [a whole-level experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md) tests a duration-weighted subject-history candidate, including clock reparameterization, overlapping windows, cross-subject calibration and infinite-sum limits.

The [previous analysis](ZERO_TOTALITY_EXPERIENTIAL_EQUIVALENCE_AND_SUBJECT_INCIDENCE.md) showed that a signed zero and its symmetry orbit do not by themselves say which experiences belong to which subjects. Here is a more explicit candidate, building on the project's earlier [relational subject-facet model](RELATIONAL_WHOLE_SUBJECT_FACET_CONSTITUTION.md) rather than replacing it:

> Each actual subject is an intrinsically first-person experiential field-occurrence, constituted by a physically and experientially specified organization. The whole contains these fields and their actual aspects. A global signed quantity is calculated on a separately specified domain; subject-level accounts must preserve that domain's identity and measure rather than create or discard occurrences by relabelling them.

This is a **field-identity and accounting hypothesis**, not a derivation of feeling from a graph. It permits distinct subjects within one whole without assuming a cosmic subject. A real field's qualitative presence is not produced by a second inner observer reading a subject label. The criterion that selects actual fields, their contents and their physical realization remains to be established.

The central result is a precise compatibility condition: if a global quantity counts each actual experiential token once but fields overlap, weights that apportion each token across its owners add back to the same global total. However, these weights are **accounting allocations**, not automatically the intensity of each person's feeling. A different candidate quantity that counts every subject–experience incidence can give a different total. Which domain and quantity are fundamental cannot be resolved by arithmetic alone.

## 1. Actual fields, views and subjects

For a finite illustration, suppose there is an actual collection of field-occurrences `F_s`, one for each thin subject `s`, and a collection of already actual qualitative aspect-tokens `e`. Write `s owns e` if that token belongs to the field. This is a deliberately simple incidence relation: it does not assume every real experience decomposes into independent atoms, that every phenomenal relation is transitive, or that all subjects persist unchanged through time.

The **candidate identity** is `thin subject s = field-occurrence F_s`. This avoids postulating an extra internal observer in addition to an already first-person field. It does **not** show why the field is first-personal, why it exists, or which organization constitutes it. It also does not identify a persisting person with every successive field. A lineage relation among occurrences needs a separate justification.

In particular, a restricted view of one actual field need not be a new field or a new subject. Otherwise a single episode could be multiplied merely by changing the descriptive window. If a theory instead claims two nested fields are genuinely distinct subjects, it must provide a criterion distinguishing them from two views of one occurrence. See the [field-individuation audit](FIRST_PERSONAL_GIVENNESS_AND_FIELD_INDIVIDUATION_AUDIT.md) and [episode-incidence reformulation](EPISODE_INCIDENCE_REFORMULATION.md). Internal windows and lineage are not a preferred external clock.

Overlapping fields are **not** assumed actual. If one token is truly owned by two fields, that is a substantive and contested sharing hypothesis. Overlapping physical support alone is not enough: two fields could instead have numerically distinct, private qualitative tokens of similar type. A single subject can also have mixed or neutral contents. In every case actual suffering remains a real negative experience, not the absence of experience.

## 2. Two different totals

Assume a finite set of actual experiential tokens `E`, a hypothesized signed contribution `q_e` in a common unit, and a set `S(e)` of their subject-owners. Let `k_e=|S(e)|`. Two candidate quantities are:

```text
Token total:       Q_token = sum_(e in E) q_e.
Incidence total:   Q_inc   = sum_(e in E) k_e q_e.
```

The first counts each numerically distinct token once. The second counts each subject–token incidence once. They agree if every token has exactly one owner, but not necessarily if a token is genuinely shared. Either could be a meaningful global candidate under suitable assumptions; neither is automatically the user's intended experiential quantity. In particular, repeated *descriptions* of one token must not be confused with additional actual experiences, while private tokens must not be collapsed just because they have similar content.

If actual subject–token incidences are the intended fundamental domain, an incidence-based sum might be appropriate—but its weights and cross-subject scale still need justification. If the intended domain is actual tokens, the token total is natural—but the theory must explain what a shared token is and why it is counted once. The qualitative extent of a subject's feeling is not settled by choosing a numerical counting convention. More general non-additive accounts remain open.

## 3. A conservation rule for shared tokens

Assume for this subsection that the token total is the independently specified global quantity, and every counted token has at least one owner. For each `s in S(e)`, choose nonnegative accounting allocations `a_(s,e)` satisfying

```text
sum_(s in S(e)) a_(s,e) = 1.
```

Define the **allocated account** for each subject by

```text
A_s = sum_(e owned by s) a_(s,e) q_e.
```

Then, by changing the order of the finite sums,

```text
sum_s A_s = sum_e q_e = Q_token.
```

Thus, if a separately justified constitutional principle gives `Q_token=0`, the allocated accounts also sum to zero without double counting shared tokens. This does not derive the zero or show that `A_s` is the subject's own summed felt valence. In particular, allocating half a shared negative token to each subject **does not claim that either suffers only half the pain**, nor that suffering is compensated by another subject's pleasure. Accounting, first-person intensity and ethics are distinct questions.

If some actual tokens are unowned, the ownership-only accounts do not cover the global domain. They need a separately specified unowned account, or the theory must explain why all counted tokens have an owner; a zero total does not decide this. Similarly, if physical or other non-subject aspects contribute to a quantity meant to apply to the whole, their inclusion must be defined rather than assumed to be experiential.

## 4. A concrete overlap and an allocation ambiguity

Take three stipulated tokens `P`, `N` and `C` with

```text
q(P)=+2,  q(N)=-1,  q(C)=-1,  Q_token=0.
```

Assume, for the example only, two actual subject-fields with token incidence

```text
field A: {P,C},     field B: {N,C},
```

where C is **the same token** in both, not two private tokens of the same quality. These are proposed actual fields, not something established by the sets. The token total is zero. Counting each field's unadjusted full token sum instead gives

```text
A full sum = +1,    B full sum = -2,
Q_inc = -1.
```

The difference is the twice-counted shared token. This does not show that token-counting is metaphysically correct or incidence-counting incorrect: they answer different questions. If C were instead two private, distinct `-1` tokens, treating them as one would incorrectly discard an actual occurrence; the stated token domain and its total would change. The existence of shared or private tokens must be decided by the theory, not by selecting whichever makes the answer zero.

For a token-based allocation, write the shared token's A-share as `alpha` and its B-share as `1-alpha`, with `0<=alpha<=1`. Exclusive P and N have their sole owners as recipients. Then

```text
A_A = 2-alpha,     A_B = -2+alpha,
A_A + A_B = 0.
```

Equal allocation `alpha=1/2` gives `(3/2,-3/2)`; `alpha=1/4` gives `(7/4,-7/4)`. Both preserve the global token total. Neither allocation changes what is actually felt or determines how much suffering there is. A subject can have more than one qualitative aspect, so these formal sums also do not by themselves capture a mixed experience's character.

## 5. Does symmetry fix the shares?

An equal-share rule `a_(s,e)=1/k_e` is invariant under renaming the subject labels and requires no named owner. Under the **additional locality/anonymity assumption** that an owner's share depends only on the number of owners and is the same function for all of them, conservation forces that equal share. This is an exact conditional result; it is not a derivation of the locality/anonymity assumption or evidence that equal sharing measures experience.

General relabelling covariance alone is weaker. In the example, A has the exclusive positive token and B the exclusive negative token. Their roles are distinguishable by the full annotated structure. A relabelling-covariant rule could assign `1/4` of C to the owner with the exclusive positive token and `3/4` to the other, or use equal shares. Both rules transport properly when all fields and tokens are renamed. A particular full-structure automorphism that fixes a token and exchanges two owners would force equal shares **if the allocation rule is invariant under that automorphism**, but the annotated example has no such sign-preserving owner exchange.

Therefore a symmetric notation does not on its own select an objective allocation. If competing allocations make no distinct physical or experiential difference, they may be conventions for decomposing the same total, not additional facts to be explained. If they are claimed to be physically or phenomenally real, their independent determination and consequences must be specified. Neither answer follows merely from `Q=0`.

## 6. What would make the incidence proposal more than a table?

A prospective complete constitution needs a coupled physical–experiential law, not just this bookkeeping. It would need to specify:

1. **Eligibility and identity:** what actual organization constitutes an intrinsically first-person field, distinguishes a field from a window-relative description, and determines whether overlapping supports mean shared or private tokens.
2. **Phenomenal unity:** why contents are jointly present within a particular field rather than merely linked by causal paths or represented in the same physical system. Existing [subject-candidate comparisons](SUBJECT_CONSTITUTION_THREE_CANDIDATES_CRITICAL_TEST.md) show why simple connectivity or maximality is not already an established solution.
3. **Actual incidence and persistence:** which fields and contents occur, their contextual boundaries and any internal lineage, with no unsupported universal subject or external time. Reports and interventions can constrain candidates, but behavior alone is not a subject census.
4. **The global quantity:** whether tokens, subject incidences, physical–experiential events, or a non-additive whole constitute its domain; how sign, scale, weights, neutral and mixed character are fixed; and how infinite sums, if needed, are defined.
5. **Balance and physical recovery:** why that very quantity has zero total and how, if at all, it relates to physical energy or a gravitational constraint. Post-hoc allocation does not establish either identity.
6. **No residue:** how the incidence law, local qualities, their determinate organization, and the balance all follow from or are identical with one self-subsistent zero constitution, rather than being independent unexplained rules.

A concrete identity theory might predict different patterns of joint report, information access and behavior under carefully specified, ethically acceptable conditions. Those data cannot by themselves reveal or count every subject; the subjective and physical interpretations, alternative models, measurement limitations and coverage must be stated independently. No clinical test or physical-to-phenomenal law is claimed here.

## Result

This candidate makes subject incidence and accounting **compatible** with a zero-token whole, including a hypothetical shared-token case, without claiming a universal experiencer. It also shows why the same phrase “total experience” could refer to different quantities when incidence overlaps. The rule determining actual fields, their qualitative presence and the correct total is not yet derived from zero's nature. No conclusion of impossibility follows; the strict demand for structural and experiential intelligibility remains the target.

## Verification

`python -m unittest verification.subject_incidence_experiential_accounting_test -v` checks finite conserved allocations, the token/incidence distinction, relabelling covariance and the conditional equal-share rule. These controls are not evidence that shared tokens or the proposed fields occur in reality.

Related: [experiential equivalence and incidence](ZERO_TOTALITY_EXPERIENTIAL_EQUIVALENCE_AND_SUBJECT_INCIDENCE.md), [plural relational subject facets](RELATIONAL_WHOLE_SUBJECT_FACET_CONSTITUTION.md), and [field individuation](FIRST_PERSONAL_GIVENNESS_AND_FIELD_INDIVIDUATION_AUDIT.md).
