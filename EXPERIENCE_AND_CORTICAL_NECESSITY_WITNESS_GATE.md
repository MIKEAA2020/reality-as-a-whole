# A joint witness gate for cortical necessity

## Purpose and status

The [Shewmon case analysis](SHEWMON_FOUR_CHILDREN_CLINICAL_EVIDENCE_AND_CONSTITUTION_GATE.md) and [Merker analysis](MERKER_SUBCORTICAL_CONSCIOUSNESS_AND_PERSPECTIVE_AUDIT.md) leave an important inference unresolved: what would have to be established, jointly, before one could rule out a proposed cortical necessity claim? Here is a sharp finite-set accounting rule and a concrete research contract. **It is conditional mathematics, not a new statistical theorem or a result about any actual child.**

The counting idea is the established inclusion–exclusion/union bound; see [Bonferroni's inequalities](https://math.iisc.ac.in/~gadgil/MA261/notes/chapter-8.html). The project-specific contribution is to apply it to two simultaneously uncertain claims—presence of a specified experience and absence of a specified functional cortical substrate—and to separate a counterexample to necessity from proof of subcortical sufficiency. It complements, rather than replaces, [the existing intervention and assay bound](ROBUST_EXPERIENTIAL_CONTRAST.md).

## 1. Define the claim before assessing evidence

Fix a domain `D` of individuals, developmental histories, conditions and time windows, and fix the kind of conscious experience `E` being discussed. Let `C=1` mean the precise **functional** cortical condition that the candidate theory says is necessary is present in that window; `C=0` means it is absent. The universal claim is

```text
N: for every case in D, E = 1 implies C = 1.
```

A single case in `D` with `E=1, C=0` contradicts N. This is a claim about the specified theory and domain, not a claim that all cognitive functions, all contents or all possible substrates have the same prerequisites. A thin cortex, small tissue volume, abnormal EEG or reduced task response is **not by itself** equivalent to `C=0`; conversely, seeing remnant tissue on a scan is not by itself proof that the specified functional condition is present. Specify the distinction between anatomical presence, physiological activity, relevant connectivity and the theoretical condition before using the inference.

First-person experience is an accepted datum in this project, not something to explain away. For a non-reporting person a behavioral or physiological indicator can supply evidence, but the truth of `E` in a particular window is not automatically identical to the indicator. Uncertainty about an indicator gives no permission to treat a person as incapable of feeling or undeserving of care.

## 2. A sharp finite witness count

Consider `m` **distinct preselected case-windows** in which both a chosen experience indicator and a chosen cortical-absence indicator are positive. A case-window may instead be an individual if its evidence and timing are defined at the individual level; repeated windows from the same person are not independent people.

Let:

- `F` be the subset where the experience-positive indicator is wrong for the specified `E`;
- `G` be the subset where the cortical-absence indicator is wrong for the specified `C=0`;
- independently justified **deterministic counts for this selected set** satisfy `|F| <= a`, `|G| <= b`, and optionally `|F ∩ G| >= j`.

Take integer `0 <= a,b <= m` and `0 <= j <= min(a,b)`. The actual number of joint witnesses is

```text
W = m - |F ∪ G| = m - |F| - |G| + |F ∩ G|.
```

Exactly the following integer range is compatible with only these constraints:

```text
max(0, m - a - b + j) <= W <= m - j.
```

The lower bound follows from inclusion–exclusion and cannot go below zero; the upper bound follows because at least `j` selected case-windows have both indicators wrong. Both endpoints and every integer between can be realized by choosing the two error sets appropriately, so the interval is sharp **given only these set constraints**. For example, put `j` errors in both sets, then distribute remaining errors over separate windows as far as the budgets and set size allow. Additional independently known features or actual individual measurements may narrow this interval.

If no overlap information is available, set `j=0`: `W >= max(0,m-a-b)`. No independence of mistakes is assumed. The combined uncertainties are not interchangeable: a positive experience indicator without a valid absence classification, or a valid absence classification without an experience-linked indicator, is not a joint witness.

**Synthetic examples, not estimates from the four children:**

| Selected windows `m` | At most experience-indicator errors `a` | At most absence-indicator errors `b` | At least common errors `j` | Sharp `W` range |
| --- | --- | --- | --- | --- |
| 4 | 1 | 2 | 0 | 1–4 |
| 4 | 1 | 3 | 0 | 0–4 |
| 4 | 1 | 3 | 1 | 1–3 |

In the first row at least one witness exists even when all errors are arranged adversarially. In the second, the error sets can cover all four selected windows, so these premises alone cannot guarantee any witness. In the third, the separately established overlap prevents the two error sets from covering all four; this stronger assumption should never be invented merely to obtain the desired answer. These hypothetical error cases are bookkeeping alternatives, not claims that any of the four children lacked experience.

For `j=0`, these assumptions **guarantee** that N is contradicted exactly when the guaranteed lower bound is positive, i.e. `a+b < m`. When the lower bound is zero, the constraints allow both a no-witness assignment and, except in degenerate cases, assignments containing witnesses; N could still be false, but these bounds do not establish that. This is failure of the proposed proof, not evidence for N or against experience. With independently justified `j>0`, the corresponding guarantee condition is `a+b-j < m`.

## 3. Why the existing cases do not instantiate the bound

The Shewmon paper reports substantial selective behavior and some cortical remnants in each of four children. It does not establish calibrated bounds on the number of experience-indicator errors or on the number of false functional-absence classifications for any particular definition of `C`; in fact it did not perform the proposed PET or functional MRI localization. No observed `m`, `a`, `b` or `j` from that series is asserted here. Merker's related interpretation remains an experience-respecting hypothesis; the absence of a numerical witness certificate does not decide the children's experiences. The original sources and reading limits are in the two linked audits.

This gate also does **not** create an experience assay. To use it, one would need separately defensible grounds for both selected-set error bounds, especially calibration under the actual person's sensory, motor, communicative and developmental conditions, and a sufficiently sensitive assessment of the precise functional condition. Transport from verbal adults or from a typical anatomy requires its own justification. Accuracy in a different condition or a generic probability that a test works is not a deterministic count bound for these selected windows.

If `a`, `b`, or `j` are instead estimated with confidence, distinguish a statement such as “all three inequalities hold jointly with at least 95% confidence” from the inequalities themselves. With separate bounds, account for their simultaneous coverage, selection and repeated measures; if the bounds depend on counterfactual or unobservable phenomenal truths they may not be independently calibratable. No such confidence claim or study power calculation is made here.

## 4. A witness is not a complete constitution account

A validated `E=1, C=0` witness would refute N for the defined `D`. It would **not**, without more:

1. prove that a proposed brainstem arrangement `B` is sufficient for all experience in other situations;
2. show that `B` is necessary, or that no other residual system participates;
3. identify the causal effect of removing cortex, a developmental history, or its unrealized counterfactual outcome;
4. determine the quality of the experience, establish one or more subject boundaries, or transport an assay to another organism or substrate.

For a concrete logical example, in a hypothetical actual case let `B=D=1`, `C=0`, and `E=1`. Both proposed rules `E=B` and `E=B AND D` fit that case; they disagree where `B=1, D=0`. This is a logical illustration, not evidence that `D` is a real brain mechanism or that the unobserved configuration can occur. Neither a common structure nor the counterexample to one necessity rule identifies the remaining experiential constitution.

The project's target is **full structural and experiential intelligibility**, jointly with C1–C7. This gate can sharpen one empirical obstacle for the preferred relational, intrinsic-experience and plural-subject program, but cannot prove the ground self-sufficient, derive subjective quality or settle subject incidence. No universal subject, external creator or temporal mechanism that actualizes possibilities is assumed.

## 5. Verification and next evidence

Run [the finite checker](verification/experiential_anatomical_witness_gate.py). It exhaustively enumerates pairs of error sets for all feasible budgets with `m <= 6`, checks the full attainable witness-count interval, and writes the [receipt](verification/experiential_anatomical_witness_gate.json). It does not verify clinical premises or generalize to an experiential law.

A prospective, ethical research route is to specify an experience target and functional necessity claim in advance, then use independent complementary assessments, condition-matched evidence about experiential validity, careful subject-level reporting and imaging appropriate to each patient. Include potentially uninformative assessments and do not substitute repeated windows for people. Spontaneous clinical contrasts or ethically indicated observations are preferable to harmful experimental lesions; individualized care must not be withheld for theory testing. If adequate calibration or structural sensitivity is unavailable, report the joint witness as **unresolved**, not as a forced binary verdict.
