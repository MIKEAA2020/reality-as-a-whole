# Constructive step 4: can compatible presentations be glued into one experience?

## Decision

The previous round isolated overlap-amalgamation as a sufficient condition for finite maximal episode supports to form a partition. The next question is whether an independently defensible gluing principle supplies that condition.

**The answer from the tested constructions is no—not from compatibility alone.** Four different achievements must remain separate:

1. agreement of local descriptions on overlaps;
2. existence of an admissible global description;
3. uniqueness of that description;
4. one actual experiential occurrence realizing it.

The work gives exact counterexamples to collapsing these stages and a constructive characterization of one missing higher-order parameter.

It also motivates a productive change in the local research method: **anchor a known actual episode first and reconstruct its concrete organization, rather than try to manufacture episode unity by gluing independently described contents.** That changes the starting evidence, not the demand that unity eventually be explained.

**24 new tests pass; 102 tests now pass across four research rounds.** These are mathematical and bookkeeping checks, not empirical consciousness experiments.

---

## 1. Exact gluing is real—but what does it establish?

Suppose local sections assign values to overlapping sets of content coordinates:

\[
s_{ab}:\{a,b\}\to V,
\qquad
s_{bc}:\{b,c\}\to V.
\]

If both assign the same value to \(b\), their union is a well-defined function on \(\{a,b,c\}\). On that covered domain, the function is unique.

That elementary gluing result is valid. But its inputs already include:

- which coordinate in one section is the same coordinate in another;
- what counts as value agreement;
- the domains that are being covered;
- and the admissible global structure.

If the coordinates are merely repeated content types, gluing does not establish shared occurrence identity. If they are genuine occurrence-tokens, that identification must be justified before the theorem is applied.

Moreover, the union is a **description**. Its existence as a function is not the actual occurrence of a joint experience.

A crucial distinction follows:

> Exact mathematical compatibility can establish a unique union of descriptions without establishing that the union is an admissible, actual, or phenomenally unified realization.

## 2. Compatible and individually admissible patches can fail globally

Consider binary coordinates \(x,y,z\) and a globally admitted state set consisting of odd-parity triples:

\[
x\oplus y\oplus z=1.
\]

Take two patches:

\[
(x,y)=(0,0),\qquad(y,z)=(0,0).
\]

They agree on their overlap. Each separately extends to an allowed global state:

- the first extends to \(001\);
- the second extends to \(100\).

Their union, however, is \(000\), which violates the global constraint.

Thus local admissibility and overlap agreement are insufficient to prove global admissibility when the global theory has additional constraints.

This is not an argument that actual experiences obey a parity constraint. It is an exact test of the attempted inference from local compatibility to a joint realization. The lesson is that a gluing principle needs its domain and global extension conditions justified.

## 3. Statistical overlap agreement is even weaker

A second example uses pairwise probability models. Give each of \((x,y),(x,z),(y,z)\) a perfectly anticorrelated distribution:

\[
P(0,1)=P(1,0)=1/2.
\]

Every single-coordinate marginal is uniform, so the pair models agree on their overlaps.

But no three-bit assignment makes all three pairs unequal. Every deterministic triple satisfies at most two of the three anticorrelation requirements. Any global probability distribution is a mixture of such assignments and cannot give all three requirements probability one.

Therefore the pair models have no common global joint distribution.

This is a classical marginal-consistency example. It is not a derivation of quantum contextuality from experience, a claim that phenomenal privacy is no-broadcasting, or a metaphysical impossibility theorem. Its role is narrower: **statistical consistency on overlaps need not supply a global model at all**.

## 4. When global extensions exist, local data may leave a continuous family

Now specify all three pairwise marginals as uniform:

\[
P(x,y)=P(x,z)=P(y,z)=1/4
\]

for every pair outcome.

All compatible three-bit distributions are

\[
p_t(x,y,z)=\frac{1+t(-1)^{x+y+z}}8,
\qquad -1\leq t\leq1.
\]

Their pairwise and single-coordinate marginals agree. Their triple correlations differ:

\[
\mathbb E_{p_t}[(-1)^{x+y+z}]=t.
\]

Special cases are:

- \(t=1\): uniform distribution over even-parity triples;
- \(t=-1\): uniform distribution over odd-parity triples;
- \(t=0\): independent uniform bits.

### Why this is the complete family

The pair-marginal constraint matrix has eight unknown joint probabilities and rank seven. Its nullspace is one-dimensional, spanned by the parity-sign vector \((-1)^{x+y+z}\). The independent uniform distribution supplies one particular solution. Nonnegativity restricts the remaining parameter to \([-1,1]\).

The implementation checks the rank with exact rational elimination, verifies the null direction, and checks normalization, positivity, and marginal agreement for representative rational parameters. The analytic argument establishes the full interval, not merely those samples.

This is a positive result: **the missing information is identified exactly**, rather than described as a vague gap.

### What would resolve it?

A triple-correlation constraint adds an independent row and fixes the parameter. A physical parity readout distinguishes the even and odd endpoint models with certainty, despite the complete equality of their pairwise marginals.

This parallels the previous round's distinction between pairwise and joint presentation. It does not identify physical correlation with phenomenal co-presence. They are different targets with analogous failures of low-order reconstruction.

## 5. Parameter-free preferences do not become derivations

Independence selects \(t=0\). Maximum entropy also selects the independent uniform distribution in this family: its entropy is three bits, while the endpoint parity distributions have entropy two bits.

Those are coherent additional rules. They are not consequences of the pairwise data. The same local data are exactly compatible with the correlated endpoint models.

Maximum entropy may have an epistemic justification in a specified inference problem. But an epistemic selection cannot automatically be promoted to the actual global constitution or the unity of an experience.

Likewise, imposing overlap-amalgamation or taking a maximal clique can force a unique support structure. Being coefficient-free does not establish that the selected structure is phenomenally actual.

The criterion must be justified for the target, not rewarded merely because it returns a point answer.

## 6. Unique gluing still does not give a unique occurrence

Suppose every coordinate value and every higher-order relation is specified so that a joint description is unique.

That same description can be associated with:

- one supplied realization occurrence;
- two numerically distinct realizations with matching structure;
- or different candidate episode-incidence assignments not constrained by the descriptive theory.

The earlier realization result remains in force: structural or behavioral uniqueness is not numerical occurrence identity.

The duplicate-record test makes only a bookkeeping claim. Distinct supplied witnesses remain distinct despite their equal contents. It does not establish that those witnesses are conscious or derive their numerical plurality from a mathematical tuple.

Similarly, a jointly computed output \((x,y,z)\) or a parity bit need not be jointly experienced. A reporter, database, or circuit can assemble values without the present theory specifying any phenomenal membership relation.

A joint distribution is also not a self-location distribution. None of the probabilities in this round weights observers or allocates an ego among them.

## 7. What this means for overlap-amalgamation

The previous candidate law stated:

> Genuinely overlapping episode supports lie within a common episode support.

The gluing results do not independently establish that law. At most they show how a descriptive union can be constructed under additional conditions.

There are three gaps in applying the union to phenomenology:

1. **Token gap:** does a recurring label refer to the same content-occurrence?
2. **Realization gap:** is the union globally admissible and actual?
3. **Unity gap:** does that actual union constitute one experience rather than jointly describe several occurrences?

An argument that already describes each content-token as belonging to a unique maximal presenting act has assumed the partition-like structure it hoped to derive. That may be an intelligible definition within a theory, but it cannot simultaneously serve as an independent proof of the theory's unity claim.

Conversely, the inability of these weak premises to derive amalgamation is not proof that a richer constitutive argument could never establish it.

The result is exact scope control: **compatibility is not the missing constitutive principle**.

## 8. A constructive change of starting point: episode-first anchoring

The attempted path so far has been:

\[
\text{content distinctions}
\longrightarrow\text{joint structural description}
\overset{?}{\longrightarrow}\text{one experience}.
\]

The first arrow can be made mathematical. The second remains unearned.

A more promising local strategy is:

\[
\text{an independently warranted actual episode}
\longrightarrow\text{its differentiated phenomenal structure}
\overset{?}{\longleftrightarrow}\text{its concrete constitutive organization}.
\]

Here unity is a local starting datum to characterize and explain—not a universal axiom applied to every coordinated process. It is not exempt from explanation.

For the subject, an actual field of co-present contents can be an evidential starting point. Its being given does not establish:

- a unique neural realization;
- its necessity or ultimate ground;
- a unique temporal boundary;
- infallible judgments about every aspect of it;
- or how to identify all other subjects.

The benefit is methodological: do not pretend that a global composition of descriptions has generated the first-person unity that supplied the original evidence.

### What would make this more than a reversal of arrows?

A successful paired reconstruction would need to:

1. characterize the episode's actual co-presence and contrasts independently of the candidate physical model;
2. identify physical transformations whose effects on that structure were not used to define the structure;
3. test context, temporal scope, report dependence, and realization provenance;
4. derive or defend a constitutive identity explaining the connection;
5. explain why the actual episode and its constitution obtain, rather than declaring their evidential undeniability a metaphysical explanation.

That last requirement preserves the whole-reality objective. Episode-first investigation is not a new foundational exemption.

## 9. A concrete next validation target

The next bounded target should be **higher-order phenomenal structure under controlled perturbation**, not merely more pairwise data.

A possible design separates:

- an immediate judgment of simultaneous multi-content presentation;
- a sequence of pairwise judgments;
- a later report aggregating remembered contents;
- and a physical task that combines all input signals without asking about their presentation.

The physical model should predict what changes under the perturbation. The phenomenological record should independently constrain whether contents remained jointly presented, were sequentially integrated, or were merely reported together afterward.

A report of a joint field is evidence to assess, not a direct membership oracle. Attentional and memory effects are possible confounds, not automatically part of the target. No-report proxies need independent validation rather than a label identifying them with experience.

The important acceptance test is explanatory asymmetry: a model should predict a contrast between these conditions that a mere shared-report account misses, while surviving held-out tests and the token-provenance audit.

This round has not collected such data or discovered the required neural identity. It specifies the richer evidence and bridge needed, instead of claiming that compatibility has already supplied them.

## 10. Revised dependency structure

The current programme now distinguishes:

| Stage | Conditional achievement | Still required |
|---|---|---|
| Contrast organization | Relational correspondence and calibration tests | Why the relevant occurrence is experiential |
| Contextual scope | Exact adequacy/factorization criterion | Which differences are genuinely experiential and constitutive |
| Joint support | Higher-order incidence tests and conditional partitions | Token identity and justified unity law |
| Gluing | Exact union conditions, extension counterexamples, one-parameter reconstruction | Global admissibility, actuality, and phenomenal realization |
| Episode-first anchoring | A disciplined local evidential starting point | Constitutive identification and explanation, not exemption |

The rows are not five proven metaphysical primitives. They track dependencies that one deeper theory may explain together. Nor does identifying a missing variable prove that nature contains an independently adjustable selector.

The practical decision is to stop treating mathematical gluing as a derivation of unity and redirect the positive construction to a paired reconstruction from an actual episode.

## 11. Reproducibility

Files:

- `model.py`: exact compatible-section gluing, constrained extensions, three-bit marginal models, rational row reduction, and occurrence-record bookkeeping;
- `test_model.py`: 24 tests;
- `results.log`: actual test run.

Run this round:

```bash
cd research/presentation_gluing
python -m unittest -v test_model.py
```

Run all four rounds:

```bash
python research/run_checks.py
```

**Observed result:** 24 new tests passed, exit code 0; all 102 tests across the four rounds passed.

The equal-report and duplicate-record checks explicitly preserve stipulated model interpretations. They do not independently prove their physical realization. All gluing, marginal, and rank claims concern the specified finite mathematical models, not all metaphysical possibilities.

## Final verdict

> Compatibility cannot supply the missing unity law by itself. It can fail to extend globally, can leave a continuous family of joint models, and can uniquely describe a whole without identifying one actual experience. The positive result is a precise account of these dependencies and of the higher-order data needed to resolve one reconstruction problem. The next constructive route is episode-first paired reconstruction: begin from a warranted actual presentation, derive and test its organization, and seek a constitutive identification without exempting that presentation from the ultimate explanatory demand.

## Subsequent paired reconstruction

[Constructive step 5](../episode_reconstruction/REPORT.md) implements three candidate temporal organizations with identical aggregate reports and a conditional intervention double dissociation. It yields an executable episode-first identification design, not a collected phenomenological dataset or a validated physical identity.
