# Source integration, third pass: Bostrom's self-location structure on the same sphere

## Audit → adapt → implement

The user's [Bostrom-based reconstruction conversation](sources/uploads/Bostrom%27s%20simulation%20hypothesis.md) explicitly asks to preserve the **probabilistic structure**, not merely a simulation narrative, while removing unexplained residues. Its assistant proposes dropping agency, using self-hosting fixed points and a universal prior. Those proposals are not established consequences of Bostrom or of zero: a fixed-point equation does not by itself establish a unique concrete reality, a universal prior depends on its coding choices, and a compact description does not identify actual subject incidences. The [side-by-side source audit](SIMULATION_ZERO_RESIDUE_ATTACHMENT_AUDIT.md) discusses these and other limitations. The user's later correction is decisive: use the self-location structure, **not literal simulation, simulators or Bostrom's ontology**.

The transferable core is a reference class of eligible perspective-incidences and a conditional measure on them: given evidence, what relative weight belongs to one kind of incidence? We should not substitute physical outcome-label counting for that measure. Earlier [incidence-refinement work](ZERO_INCIDENCE_REFINEMENT_AND_BORN_MEASURE.md) already showed this issue in another table. Here we bring it into the **same stationary sphere–echo and the two incidence types** of the [second integration pass](ZERO_SOURCE_INTEGRATION_STATIONARY_SUBJECT_INCIDENCE.md).

**Plan:** take the actual six positive reduced physical outcomes at tick 10; form a fixed disagreement event between `sj` and `sjr`; split selected outcome effects into finer labels without changing their total effects; compare naive label counting to preserved physical weights. Then condition the proposed two-type incidence measure on that same event. This specifies the self-location problem in the common candidate, rather than declaring that a prior conversation's useful ideas are already present somewhere in the repository.

## 1. One physical event, several descriptions

At tick 10 the positive old `(b,z,s)` labels number six. The B-positive cases have two labels of weight `1/4` each. The B-negative cases have four labels of weight `1/8` each. They are the same old physical Born ledger, not established subjects. The two quality candidates disagree exactly when `r=−`, equivalently `b=−` on the ready support, so their physical disagreement weight is `1/2`.

Consider two purely **algebraic** refinements of the given outcome effects:

1. Split each B-positive outcome effect into two equal half-effects. This gives 8 positive fine labels, all of weight `1/8`.
2. Instead split each B-negative outcome effect into two equal half-effects. This gives 10 positive fine labels, with weights `1/4` and `1/16`.

After coarsening, both return exactly the original six effects and all their physical weights. No extra measurement apparatus or experiential occurrence is asserted.

| Description | Positive labels | Labels in disagreement | Naive count fraction | Preserved Born weight |
|---|---:|---:|---:|---:|
| Original | 6 | 4 | 2/3 | 1/2 |
| Split B-positive effects | 8 | 4 | 1/2 | 1/2 |
| Split B-negative effects | 10 | 8 | 4/5 | 1/2 |

The equal-weight refinement happens to make label-counting agree with the physical measure, but choosing the other valid refinement changes the count to `4/5` while the physical effect remains unchanged. This is an **actual calculation on the common model**, not evidence that these labels are subjects, and not a new proof that Born weights are experiential weights.

## 2. Conditional self-location once a candidate incidence measure is specified

Under the second pass's **strong proposed product extension**, the physical history carries two proposed incidence types N and E with weights α and `1−α`. Their physical marginal is fixed and their conditional physical distribution is the same. For the event D that the two candidate signs disagree,

```text
μ(D)=1/2,
μ(N ∩ D)=α/2,
μ(N | D)=α.
```

If, in addition, the **active physical-and-type symmetry** established in the reduced model is required to preserve the actual incidence measure, then its demonstrated consequence is `α=1/2`, including within D. The separate symmetry premise is doing real work: α can otherwise be `1/4`, `1/2` or `3/4` with the same physical marginal and sign balance. This is conditional self-location weighting in a single necessarily specified whole; it does not posit an external draw, fundamental objective chance, multiple ultimate wholes, or a simulator.

Nor does it assume that every refined label is a distinct actual subject. A real record-producing apparatus could create physically different outcomes, and an actual experiential theory would still have to say whether the resulting occurrences are distinct, shared or merely different descriptions. Conversely, the algebraic split itself does not demonstrate a new experience. This distinction is necessary to use Bostrom's reference-class idea without allowing the answer to depend on a convenient encoding.

## 3. What the batch contributes—and its limits

The [executable refinement](verification/zero_stationary_refinement_self_location.py) and [tests](verification/zero_stationary_refinement_self_location_test.py) connect (i) the fixed sphere physical event, (ii) refinement/coarse-graining, (iii) the two typed proposed incidences, and (iv) the earlier conditional symmetry selection. The calculations do not prove which mathematical possibilities are genuinely possible or actual under the user's plenitude thesis, derive the equivalence relation on lived occurrences, establish the physical–experiential bridge, or complete the no-residue battery.

To complete this route, the common constitution—not a stipulated reference-class convention—would need to determine which actual perspectives exist, when an apparent refinement is merely a redescription, whether the relevant incidence symmetry holds, and how resulting weights relate to empirical quantum statistics. Those are positive construction targets, not a weaker permission to leave independent selectors unexplained.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_stationary_refinement_self_location_test \
 verification.zero_stationary_subject_incidence_test \
 verification.zero_stationary_battery_bridge_test -v
```
