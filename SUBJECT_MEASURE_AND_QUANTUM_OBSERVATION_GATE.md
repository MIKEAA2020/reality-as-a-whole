# From quantum weights to plural perspectives: an observation-selection gate

## Result

Even **granting** standard quantum weights, a framework with plural experiential occurrences needs a rule connecting those weights to *which observations receive how much weight*. A finite example makes the extra choice explicit:

- Two outcome sectors have quantum weights `3/4` and `1/4`.
- If there is one eligible observation-occurrence in the first sector and three in the second, a stipulated **occurrence-weighted** rule gives the second sector weight `1/2`.
- A different stipulated rule that normalizes *within each sector* gives it `1/4`.

Both use the same quantum weights and the same counts. Neither rule follows from plenitude alone. The two numbers answer different selection questions; the `1/2` is **not** an ordinary prediction for a fixed laboratory observer measuring a qubit with Born probability `1/4`. The three-observer scenario is hypothetical, not an asserted physical experiment. Nothing here requires actual simulations, an external creator, or one universal conscious subject.

This develops a quantitative interface for the project's unresolved subject measure, including a conditional calibration bound and a check against misleading representation-dependent counting. The subsequent [Kent-like history and observation-recovery analysis](KENT_PLENITUDE_OBSERVATION_SELECTION_RECOVERY.md) extends the same interface to imperfect or indefinite local records, selected-class error bounds, and Bell-context consistency. The underlying observation-selection and quantum-measure problems are **known**, not discoveries claimed by this project.

## 1. Established work and the project's different question

[Page (2010)](https://arxiv.org/abs/1003.2419) discusses observation probabilities when multiple observers can occupy different locations and distinguishes weighting by numbers of observations from averaging within a sector. His claim that a particular projection-only formulation of the Born rule is insufficient must not be read as an experimental refutation of quantum mechanics. [Cooperman (2011)](https://doi.org/10.1088/1475-7516/2011/02/014) argues that generalized measurements accommodate Page's examples under a broader Born-rule formulation. Selecting the appropriate observable, conditioning event, and first-person interpretation remains a separate problem.

[Carroll and Sebens](https://arxiv.org/abs/1405.7907v3) use epistemic separability to motivate Born weighting and consider multiple observers; [Friederich and Dawid](https://doi.org/10.1093/bjps/axaa002) dispute whether the quantum version is justified independently of the Born rule. We do not settle that debate. Generalized Gleason-type results such as [Caves, Fuchs, Manne and Renes](https://doi.org/10.1023/B:FOOP.0000019581.00318.a5) fix a trace-form assignment under their stated noncontextuality and normalization assumptions across the relevant POVMs; they do **not** identify which physical effect corresponds to a subject or which conditional event is the correct indexical reference class.

Our target is not a claim that actual simulations exist or that a separate deity runs one. The adopted thesis says all genuinely possible local realities are already actual within a self-sufficient whole. Here `sector` is simply a label for an idealized mutually exclusive record class inside a mathematical model; it is not an external lottery selecting a whole, and it does not establish a specific Everettian branching ontology. Any appeal to probability as subjective credence, physical chance, or a measure of actual occurrences must be specified separately.

## 2. The finite interface

Let `i=0,...,k−1` label disjoint outcome sectors with given nonnegative normalized physical weights `w_i`. Suppose a **separate subject-incidence and reference-class rule** specifies a finite nonnegative total eligible occurrence weight `s_i` per unit sector weight. When `Z = Σ_i w_i s_i > 0`, the proposed occurrence-weighted distribution is

```text
Q_i = w_i s_i / Z.                                      (1)
```

Here `s_i` can be a count **only if** the analysis has separately justified equal weight for each distinct eligible occurrence in that sector. More generally it is a sum of positive occurrence weights. No observer is literally sampled by a cosmic agent; the rule says how a proposed normalized measure or associated self-locating credence is assigned. Existence of a center does not itself guarantee positive weight, nor is a positive weight a proof of phenomenal status.

**Conditional recovery criterion.** If all `w_i` are positive and all `s_i` finite and positive, then `Q_i=w_i` for every i **if and only if** all `s_i` are equal. More generally, equality is needed only on positive-weight sectors. In one direction it follows by cancellation; in the other, `w_i s_i/Z=w_i` implies `s_i=Z` on that support. A constant positive `s` cancels. This elementary algebra provides an explicit audit for any proposed observer-occurrence measure; it is not a new physics theorem.

An alternative valid normalized rule is to preserve each sector's `w_i` and distribute that sector's weight among its eligible centers, instead of giving each center the full sector weight. When each sector has `n_i>0` equally treated centers, each is assigned `w_i/n_i`, summing to `w_i`. This is **sector normalization**, not the occurrence-weighting rule in (1). It can be an appropriate different modeling choice, but it is not established as the uniquely rational one. If a sector has no eligible center, a separate prescription for conditioning and normalization is required.

## 3. Concrete counterexample and what it does—and does not—mean

Use `w_0=3/4`, `w_1=1/4`, `s_0=1`, `s_1=3`. Then

```text
occurrence weighting: Q_1 = (1/4 × 3)/(3/4 × 1 + 1/4 × 3) = 1/2;
sector normalization: Q_1 = 1/4.
```

The centers are stipulated and comparable under an expressly chosen reference class. They need not be separate complete persons; whether subjects, moments, or records should be the reference class is part of what remains open. No claim is made that an outcome physically creates persons, that each branch has a precise, basis-independent number of observers, or that ordinary experiments implement this selection rule.

Suppose instead a **particular fixed observer and laboratory** is specified before the measurement, with normal detector response and no conditioning on an outcome-dependent number of future occurrences. The given qubit's ordinary probability for outcome 1 remains `1/4`. The occurrence-weighted `1/2` describes a different stipulated ensemble of eligible center-occurrences. Mixing these targets would manufacture a contradiction with a law one never applied to the same question.

Conversely, if a real observation protocol selects reports at outcome-dependent rates, its selected sample can differ from the underlying source distribution. Such selection bias is a familiar statistical phenomenon and does not itself establish the existence or multiplication of consciousness. Formula (1) models the weight-to-observation **interface** only; it does not derive it from substrate-independent organization or experiential ground.

## 4. Generalized-measurement consistency check

Represent the two sectors by orthogonal basis states and let `ρ_p=diag(1−p,p)`. Introduce effects

```text
E_0    = diag(1/3, 0),
E_1    = diag(0,   1),
E_fail = diag(2/3, 0),     E_0+E_1+E_fail = I.
```

All are positive; they define a valid three-outcome POVM. The standard trace rule, **conditioned on not obtaining `fail`**, gives

```text
P(1 | not fail) = p / ((1−p)/3+p) = 3p/(1+2p).
```

At `p=1/4` this is `1/2`, exactly matching the stipulated occurrence weighting. This exhibits an operational postselection **representation**; it does not show that a physical device or correct metaphysical selection process implements that POVM.

There is also a useful limitation. With a fixed state-independent, unconditioned POVM effect, `Tr(ρ_p E)` is affine in `p`. The conditional expression `3p/(1+2p)` is not: it equals 0 at `p=0`, 1 at `p=1`, but `1/2`, rather than `1/4`, at `p=1/4`. Thus this *particular rule for all such mixed states* cannot be represented as one fixed unconditioned effect on this two-sector space; adding a failure outcome and conditioning works. This is compatible with standard quantum mechanics and Cooperman's generalized-measurement discussion. Other extensions, effects, states or selection rules can have different representations.

## 5. Quantitative inverse gate

A useful consequence is that, **if** an independently established base weight is trusted and the same occurrence-weighting model applies, agreement with it constrains *relative selection weight*—not subject number alone.

Write `p=w_0`, `r=s_1/s_0>0`, and assume `0<p<1`. Then

```text
Q_0 = p/[p+(1−p)r];
r   = p(1−Q_0)/[(1−p)Q_0].                            (2)
```

For a justified interval `0<L≤Q_0≤U<1`, monotonicity gives the exact conditional bounds

```text
p(1−U)/[(1−p)U]  ≤  r  ≤  p(1−L)/[(1−p)L].              (3)
```

For illustration **only**, if `p=3/4` and an appropriate population-level interval were `[0.74,0.76]`, equation (3) implies `18/19 ≤ r ≤ 39/37`, approximately `[0.9474,1.0541]`. This would exclude the toy's `r=3` under the same model and evidence conditions. The interval is hypothetical, not measured data or a confidence interval calculated from an experiment. If p is uncertain, bound it jointly with Q; intervals must cover the desired joint uncertainty. Near the boundaries the inversion becomes unstable.

Crucially, `s_i` combines **all** factors in the specified eligible-occurrence weighting: constitution, multiplicity, duration/grain, recording, inclusion and any subjective or indexical weights. Even perfect knowledge of r cannot by itself say which factor differs or count subjects. Conversely, a known recording efficiency would let one bound the residual combined factor only with independently justified bounds and an explicit factorization. Standard experimental frequencies do not automatically supply the hypothetical interval for an unknown first-person reference class.

## 6. Substrate and redescription requirement

A substrate-independent rule must at minimum transport the occurrence measure when a representation is changed. For a harmless partition of one center of weight `m` into labels with weights `m_1,...,m_n`, it must satisfy `Σm_j=m` and preserve the projection back to the original event. In the finite checker, splitting weight `2/9` into `2/45` and `8/45` preserves the coarse value `2/9`. Duplicating the full `2/9` onto both mere labels instead changes the normalized event weight to `4/11`: counting descriptions as new subjects silently changes the prediction.

This invariance follows from treating the split as **merely representational**. Whether a physically different configuration contains additional distinct experiential occurrences cannot be decided by declaration; an independently defensible subject and persistence rule is required. The rule must also handle overlaps, time/grain and contexts without assuming that every mathematical decomposition is a separate subject. Uniform treatment of genuinely distinct, symmetric occurrences is a further premise; substrate independence is not equivalent to unweighted token counting.

## 7. What advances, and what remains

The new application is an explicit, auditable **compatibility gate** between: (a) physical sector weights; (b) plural subject/occurrence constitution; (c) a choice of normalization and reference class; and (d) observational calibration. It identifies the exact equal-density condition under which the chosen occurrence-weight rule preserves the given quantum distribution, and shows how discrepancies or agreement constrain only a combined selection ratio. It does **not** derive quantum mechanics, subject constitution, consciousness, strong plenitude or a probability of the whole's existence.

A candidate complete account would need, in order:

1. Specify and justify the relevant local record structure and a subject-occurrence rule, including overlaps, persistence, context and permitted redescriptions.
2. State what the physical weights represent and why they have the observed local quantum form; cite rather than silently replace existing Gleason, decision-theoretic and self-location work. A fixed postselection question is not a substitute for this derivation.
3. State which occurrence/reference-class measure applies and why it is transportable across substrates. Resolve whether and when count- or sector-normalization is appropriate; do not assume either follows from actuality.
4. Provide independent calibration of eligibility and recording/selection, then make a held-out prediction for a clearly defined observable. Merely conditioning ordinary outcome reports or guessing numbers of subjects is not a test of experiential grounding.
5. Extend the rule to infinite domains only with a justified finite normalization or regulator and show whether its predictions converge independently of regulator choices. None is supplied here.

These steps respect the timeless-absolute constraint: this is a relationship between stipulated parts and weights of a single structure, not a universal clock or a temporal act of self-creation. They also preserve the distinction between “self-sufficient means not caused externally” and the unanswered question of **why the proposed experiential constitution is true**.

## Reproduction

Run `python verification/subject_measure_selection_gate.py`. The [receipt](verification/subject_measure_selection_gate.json) records the exact example, POVM and non-affinity witness, mass-preserving and naive refinements, the illustrative inverse interval, **10,000** seeded exact-rational bound/inversion checks, and 125 multi-outcome cases. These check mathematics under the stipulated assumptions, not the empirical truth of those assumptions. The prior [symmetry gate](PLENITUDE_SYMMETRY_AND_SUBJECT_MEASURE.md) remains the separate check on when symmetry constrains probability at all.
