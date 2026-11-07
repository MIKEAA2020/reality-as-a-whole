# Constructive step 10: set-valued boundary identification

## Main result

An exact constitutive boundary must not be inferred by selecting one model when the evidence permits incompatible boundary assignments. This round implements an alternative: carry the **set of compatible exact-core boundaries**, distinguish universally supported links from merely possible links, and retain the unresolved alternatives.

The worked examples establish three results:

1. Finite nondetection does not establish exact zero coupling in the ideal weak-coupling family.
2. Measurement error changes which exact exclusions are licensed.
3. Merging links supported by different alternative models can manufacture a boundary that no compatible model contains.

A fourth result concerns weighting: posterior probability of exact separation depends on whether the prior gave zero coupling positive mass. That choice must not be disguised as a consequence of the observations.

**24 new tests pass; all 246 tests across the ten research rounds pass.** All records below are synthetic illustrations. No actual participants, presentations, or neural boundaries have been measured.

## 1. What is being identified

Retain the preceding effective family:

\[
K_\varepsilon=(1-\varepsilon)I+\varepsilon A,
\qquad A(x,y)=(y,x\oplus y).
\]

The exact-core assignment is:

\[
B(0)=\{\{x\},\{y\}\},
\qquad
B(\varepsilon)=\{\{x,y\}\}\quad(\varepsilon>0).
\]

This is a **physical exact-core assignment within the specified model**, not an established phenomenal boundary law. The previous round withheld the claim that it is sufficient for unity. That limitation remains active throughout this report.

The present question is upstream of that bridge: do the stipulated observations even identify the exact-core boundary?

## 2. An explicit observation model

Begin at a nonfixed source state. Each tick either waits or applies A. On the ideal complete path, a state change identifies an A update. Nonfixed states remain nonfixed, so this interpretation remains valid throughout the path.

Let n be the number of observed ticks and k the number of recorded changes.

For an ordered ideal record its likelihood is:

\[
L(\varepsilon)=\varepsilon^k(1-\varepsilon)^{n-k}.
\]

Using an unordered count adds a common binomial coefficient; it changes neither likelihood support nor the finite-hypothesis posterior ratios used here.

This likelihood assumes independent update choices, a correct family, known opportunities, and faithful classification of changes. It is not a likelihood for consciousness or observer existence.

### Exact positive-likelihood support

| Record | Compatible ε under the ideal model |
|---|---|
| No observations | [0,1] |
| No changes, n>0 | [0,1) |
| Some but not all ticks change | (0,1) |
| Every tick changes, n>0 | (0,1] |

Thus zero changes in 1,000 ticks still permits both exact separation and positive coupling. A detected change excludes exact zero only under the ideal model.

The support is not a confidence interval. A positive-likelihood parameter is logically compatible with the record under this model, even if it makes that record extremely unlikely. The method does not assign equal plausibility to all survivors.

For example, ten nonchanges have likelihood 1 under ε=0 and 1/1024 under ε=1/2, although both lie in the support.

## 3. Noise changes exact exclusions

Pass each ideal change indicator through a binary symmetric error channel with known rate η, where 0≤η≤1/2. Then the recorded change probability is:

\[
p=\eta+(1-2\eta)\varepsilon.
\]

For every η>0 and every finite binary record, the likelihood is positive at every ε∈[0,1]. Consequently a recorded change no longer excludes ε=0 with certainty.

This does not make statistical inference useless. With a known noise model, enough data can favor some parameter ranges strongly and support declared-error confidence procedures. Exact logical exclusion, likelihood comparison, confidence coverage, and posterior probability are different claims.

At η=1/2 the channel erases all parameter information:

\[
L(\varepsilon)=2^{-n}
\]

for every ordered record and every ε.

The code treats η as supplied. It does not infer that a real experimental channel has independent symmetric errors, known error rate, or unchanged reliability under perturbation.

## 4. Combine evidence without inventing calibration

The implementation can intersect the record's likelihood support with an externally supplied calibration interval.

Examples:

- A warranted structural constraint ε=0, consistent with the record, yields only the split exact-core assignment.
- A warranted interval bounded strictly above zero yields only the merged exact-core assignment.
- An interval containing zero and positive values leaves both assignments possible.
- An ideal detected change combined with the asserted constraint ε=0 rejects the combined model assumptions.

The interval input is not automatically warranted because software accepts it. It may come from a structural argument or a statistical procedure, and its provenance and error guarantees must be stated. A finite confidence interval is not a guarantee that its endpoints are the exact physical truth.

No confidence procedure or neural calibration is claimed to have been carried out here.

An empty compatibility set means inconsistency or model failure. The implementation refuses to turn an empty set into vacuous “certainty” about every link.

## 5. Preserve a set of boundary alternatives

Given compatible parameter set S, define:

\[
\mathcal B(S)=\{B(\varepsilon):\varepsilon\in S\}.
\]

For the two-feature family, the possible results are:

- split only;
- merged only;
- both;
- or no compatible model.

A set containing both split and merged is an epistemic statement about the evidence and assumptions. It is not evidence of an ontologically indefinite episode, a partial subject, simultaneous realization of both alternatives, or a fractional observer.

Even a singleton result would identify only the exact-core assignment under the physical model. Applying it to actual phenomenal unity requires the independent constitutive bridge that is still missing.

## 6. Must-links and may-links

For each candidate partition, define a relation linking items in the same block.

Across a compatible boundary family:

- a **must-link** occurs in every candidate;
- a **may-link** occurs in at least one candidate.

The must-link relation is an intersection of equivalence relations and is itself an equivalence relation on the common domain. The may-link relation is their union and need not be transitive.

### Why transitive closure is unsound here

Suppose the compatible alternatives are:

\[
P_1=\{\{a,b\},\{c\}\},
\qquad
P_2=\{\{a\},\{b,c\}\}.
\]

Then:

- a–b is possible;
- b–c is possible;
- a–c is not possible in either candidate.

Closing the possible links transitively would add a–c and produce the single block abc. Neither compatible model contains it.

Likewise, the must-link partition is a|b|c, but neither compatible model contains that partition either. It is a lower-bound summary of supported links, not necessarily a candidate world.

Therefore:

> Neither the must-link partition nor the transitive closure of may-links can generally replace the full compatible boundary family.

This is a second, distinct source of false amalgamation. The earlier hypergraph work concerned different witnesses of co-presence. Here the incompatible witnesses are different **alternative models**. They must not be combined as though they all describe the same actual occurrence organization.

These partition examples are controlled mathematical cases. They do not assume that all actual episodes form partitions; a more general overlapping-incidence theory would require a corresponding set-valued hypergraph treatment.

## 7. Boundary probabilities need a prior, including endpoint treatment

Set-valued inference does not produce posterior probabilities. If probabilities are wanted, an explicit inferential framework is required.

Consider only two hypotheses:

\[
H_0:\varepsilon=0,
\qquad H_1:\varepsilon=c>0.
\]

Give H₀ prior mass w. After k=0 nonchanges over n ticks in the ideal model:

\[
P(H_0\mid D)
=\frac{w}{w+(1-w)(1-c)^n}.
\]

For w=1/2, c=1/2, and n=10, this is 1024/1025. That number is conditional on the supplied two-hypothesis prior, not derived from a count of physical systems or a symmetry of realizations.

A prior with w=0 cannot gain positive H₀ mass from nondetection. More generally, under ordinary Bayesian conditioning with finite positive evidence, an absolutely continuous prior over ε gives the exact point ε=0 posterior probability zero because it had prior probability zero. A prior atom at zero changes that conclusion.

This observation does not select the correct prior. It demonstrates why a posterior statement such as “exact separation has probability zero” can reflect endpoint prior design rather than empirical resolution of arbitrarily weak coupling.

With ideal detected changes, H₀ has zero likelihood. With positive measurement error it can retain positive likelihood and posterior mass.

These are probabilities over physical hypotheses. They are not self-location probabilities, phenomenal occurrence weights, or an observer measure.

## 8. An executable boundary-audit workflow

The new implementation supports the following disciplined sequence:

1. **Declare the domain.** Supply the token/variable anchors and temporal protocol being compared.
2. **Declare the process family.** Here it is a rare-interaction Markov family, not arbitrary neural dynamics.
3. **Declare the access channel.** Specify ideal observation or a justified error model.
4. **Supply observations.** Record actual observations separately from synthetic fixtures.
5. **State the inference criterion.** Positive-likelihood support, a confidence set, and a posterior are not interchangeable. Only the first and an illustrative finite-prior calculation are implemented here.
6. **Combine separately warranted constraints.** Preserve their provenance and any statistical error qualifications.
7. **Map compatible models to candidate boundaries.** Do not replace alternatives by a graph assembled from possible links.
8. **Report conflict or unresolved alternatives.** Do not infer truth from model rejection or ignorance.
9. **Keep the phenomenal bridge separate.** A physical core assignment does not establish an actual presentation or subject.

This is useful methodological infrastructure, not a new substantive unity law.

## 9. What the standing constitutive task has—and has not—gained

The constructive sequence now supplies increasingly explicit tests of explanatory claims:

- content covariance is not enough without context and temporal scope;
- pairwise compatibility is not global episode unity;
- an aggregate report need not identify presentation history;
- different causal roles need not identify phenomenal constitution;
- a passive copy need not implement the source's intervention organization;
- independent content preparation need not imply independent dynamics;
- exact irreducibility does not independently justify a robust unity boundary;
- a boundary compatible with some model is not a boundary established by the evidence.

These restrictions are not a zero-residue theory. The central positive constitutive claim remains unproved: why and when a concrete organization constitutes a jointly presented qualitative occurrence.

The present work prevents a premature answer from being manufactured by data reduction or statistical conventions. It does not substitute methodological caution for the requested ultimate explanation.

## 10. The next load-bearing target

The next constructive task should test a stronger source of boundary justification than interaction magnitude alone:

> Can a process be identified as the minimal support of an independently warranted **whole episode contrast**, including incidence, rather than merely the minimal support of content values or reports?

This revisits the earlier factorization criterion with the target now enlarged explicitly. A physical projection sufficient for all local content values can still omit a variable relevant to joint presentation. Conversely, a variable affecting report confidence need not alter episode incidence.

The formal target should therefore include:

- a content component;
- an incidence component;
- and access/measurement nuisance variables kept separate.

The key safeguard is that incidence must not be assigned from the very support one is trying to justify. A synthetic exercise can establish conditional identification and expose missing contrasts; it cannot supply the actual incidence facts.

This route may identify what a successful episode-first experiment needs to distinguish. Whether it yields a genuine constitutive explanation will depend on independent target warrant and a non-circular identity argument, not on further test counts.

## Reproducibility

- `model.py`: exact intervals, likelihood support with an explicit error channel, externally supplied calibration intersection, boundary sets, link bounds, and a finite-hypothesis posterior illustration.
- `test_model.py`: 24 tests.
- `audit_examples.json`: generated synthetic inference cases and assumptions.
- `results.log`: actual execution output.

```bash
# This round
cd research/boundary_identifiability
python -m unittest -v test_model.py

# All research rounds, from repository root
python research/run_checks.py
```

**Observed verification:** 24 new tests pass; 246 tests pass across the ten research rounds. They verify this inference machinery and its stated assumptions. They do not establish actual neural boundaries, phenomenal indeterminacy, or an independently justified constitutive identity.

### Final verdict

Carry compatible boundaries as alternatives, not as a single guessed subject. State what is universal, what is merely possible, what the access model can resolve, and what the prior contributes. Exact physical boundary identification and actual phenomenal constitution remain separate achievements; neither is licensed by merging possibilities from different models.
