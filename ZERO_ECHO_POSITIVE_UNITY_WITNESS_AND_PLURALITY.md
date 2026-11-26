# Positive unity witnesses on the echo: what they can and cannot establish

## Result and correction

The previous [joint-unity report](ZERO_JOINT_UNITY_REPORT_AND_INCIDENCE_SYMMETRY.md) offered a two-sided illustrative assay with assumed report errors in both directions. That is stronger than needed to challenge a **strict no-joint-experience claim**. The earlier [first-person witness analysis](FIRST_PERSON_POSITIVE_WITNESS_AND_SUBJECT_CENSUS_LIMIT.md) already established the better one-sided route; this pass applies it to the actual echo's two candidate signs rather than treating the stronger assay as mandatory.

A well-supported **positive first-person witness** of the two specified aspects together can challenge a rule saying that no subject in the covered population has that joint experience. It does not require proving that every negative or missing report reliably signals absence. Nor does it establish that there are no additional private subjects.

The new constructive results are:

* Under a stated false-positive bound, an affirmative-report rate gives a **sharp lower bound** on the reporter's joint-experience prevalence. No false-negative bound or independence assumption is needed for this population inequality.
* The four `N,K` physical cells in the echo provide a concrete way to stratify the calculation. In an invented sparse-report example, using justified cell-specific bounds improves the lower bound from `1/9` to `7/36`; the tests reconstruct the underlying cell weights from actual complex echo vectors.
* If one additionally assumes that the reporter's true joint-experience prevalence is invariant under transformations connecting all four cells, the same illustrative data can imply a stronger bound. That symmetry of a physical carrier is **not automatically** a symmetry of the reporter, their experiential incidence or their report channel.
* A reporter-only model and a nested-private-subject model can preserve the **same reporter's genuine positive witness** and the same available physical reports, while differing in the number of represented subject candidates. The witness supports the reported conjunction; it is not a complete subject census.

No report rates or calibration bounds in this document are measured data. The echo is not a model of a human brain or an identified real experiencer. The implementation is [verification/zero_echo_positive_unity_witness.py](verification/zero_echo_positive_unity_witness.py), with [tests](verification/zero_echo_positive_unity_witness_test.py).

## 1. Preserve the datum without making the report an oracle

Fix an actual candidate reporter `r`, a specified local window w and two independently identified experienced aspects A and B. Define

```text
E_r = 1   iff r has the specified A-and-B conjunction in w,
Q   = 1   iff at least one subject in the theory's declared population
               has that conjunction in w,
Y   = 1   iff the recorded response affirmatively reports that conjunction.
```

A subject's own experience is positive first-person data for that subject; it should not be dismissed because a favored structural model fails to predict it. If r directly has the specified conjunction, and r is included in the population covered by a candidate that asserts `Q=0`, that full candidate package is challenged by this case. This logical point does not first require a false-negative rate for every subject in the universe.

Communication, interpretation, memory, temporal alignment and whether A and B are the aspects the theory actually covers still matter. A third party usually receives a physical report rather than the reporter's experience itself. A **numerical** false-positive bound for that communication is an extra premise, not a deduction from first-person presence or from agreement with a physical decoder. The earlier [rivalry random-audit bridge](RIVALRY_RANDOM_AUDIT_EXPERIENCE_BRIDGE.md) similarly separates report agreement from the experiential error premise. Nonresponse, uncertainty and an unscorable answer are treated here as *not affirmative*; they are not declared to be evidence that the conjunction was absent.

The echo's `N` and `K` are physical structural signs. To apply the witness to them, an independently defended bridge must say why these signs correspond to the specific A and B aspects of the reporting experiencer, in the specified window. Neither the parity report `N K=B` nor the physical Born table supplies that identity. A correct physical bit report must not be relabeled as a first-person unity report by definition.

The distinction is also important for existing human evidence. The prior [real-case audit](REAL_CASE_WITNESS_AND_MAXIMAL_RULE_BOUNDARY_TEST.md) preserves DDC's account of bilateral ordinary sight as evidence against a much stronger claim that the verbal reporter never experiences the left side. It does **not** recode that account as a report of two particular briefly presented details experienced together in one trial. This pass relies on that earlier source audit; it does not obtain new clinical data, recalibrate a report channel or infer a patient subject count.

## 2. The one-sided bound

For a declared population of comparable reporter-windows, let

```text
p = P(E_r=1),          q = P(Y=1).
```

Suppose a separately justified, target-specific upper bound `f<1` on false affirmative reports holds **in that same population**:

```text
P(Y=1 | E_r=0) ≤ f.
```

Use the equivalent joint-probability inequality when `P(E_r=0)=0`. Since affirmative reports in truly positive windows cannot exceed p,

```text
q ≤ p + f(1−p),
therefore      p ≥ max(0, (q−f)/(1−f)).
```

If `f=1`, this information gives the lower bound zero. The bound is sharp under the stated assumptions: for `q≥f`, set `p=(q−f)/(1−f)`, use sensitivity 1 and false-positive rate f; for `q<f`, set `p=0` and false-positive rate q. It does not need a bound on missed positive experiences. At `q=0`, even `p=1` remains compatible if all positives are missed; no affirmative report is not proof of no experience.

If r is known to be within the theory's declared population in each relevant window, `E_r=1 ⇒ Q=1`, so the same expression is a lower bound on `P(Q=1)`. If r might lie outside that population, the inference does not go through: a local-only candidate could coexist with an unmodeled global reporter unless the candidate also supplies a coverage/exclusion premise. A bound on existential Q is still not a count of all subjects.

The inequality uses population quantities. For estimated rates, a valid **simultaneous lower confidence bound** `q_L` and upper bound `f_U<1` can be substituted, with all sampling and calibration uncertainties accounted for. Neither a physical decoder's agreement with the report nor repeated affirmative answers alone establishes f relative to the actual experience.

## 3. Apply it to the echo's four physical cells

At the tick-10 anchor the two commuting candidate signs have four physical outcomes `(N,K)∈{±1}²`, each with Born weight `1/4` in the specified model. The new tests reproduce those four weights from original complex source histories for three source labels, retaining the saved-J memory and the pointer. These are **physical weights**, not a measure over actual experiencing subjects.

For a conditional test, suppose further that the same eligible reporter population is correctly aligned to those cells and that its trial selection weights are `w_(n,k)=1/4`. This physical-to-reporter sampling assumption is substantive. In each cell let `q_(n,k)` be the affirmative unity-report rate and `f_(n,k)` an independently warranted false-positive bound for that reporter and target. Then

```text
p_(n,k) ≥ ℓ_(n,k) = max(0, (q_(n,k)−f_(n,k))/(1−f_(n,k))),
p_overall ≥ Σ_(n,k) w_(n,k) ℓ_(n,k).
```

A cell with `f=1` has lower bound zero. Equal physical outcome weights do not by themselves determine w, the reporter identity, or any f. The code realizes exact **synthetic** report tables on the physical four-cell distribution; it does not read human reports from the echo.

### An illustrative heterogeneous example

Take a common assumed `f=1/10` and invented report rates, in order `(++),(+−),(−+),(−−)`, of

```text
q = (4/5, 3/5, 1/5, 2/5).
```

The cellwise lower bounds are

```text
ℓ = (7/9, 5/9, 1/9, 1/3),
weighted lower bound = 4/9.
```

Here the aggregate rate is `q=1/2`, so the unstratified formula also gives `4/9`. This is a sensitivity calculation, not an empirical estimate.

Stratification can matter. With invented `q=(4/5,0,0,0)` and the same per-cell bound and weights, the aggregate q is `1/5`. The unstratified bound is `1/9`, while summing the separately truncated cell bounds gives the sharper `7/36`. Both rely on the relevant cellwise false-positive premises; one cannot simply apply a bound calibrated in a different cell or context. Exact constructions in the verifier attain the lower bounds.

## 4. Symmetry can strengthen the bound—but only with a subject bridge

For the first invented q table, suppose in addition that the **true reporter prevalence** is the same constant p across all four sign cells. Then each cell's lower bound applies to that common p, so

```text
p ≥ max(7/9,5/9,1/9,1/3) = 7/9.
```

The code constructs a compatible probability table attaining `p=7/9` while preserving the stated q values and the `f=1/10` upper bound. It does so using report channels that differ by cell. It also constructs an all-positive `p=1` table with exactly the same physical and affirmative-report marginals. Thus, even with this assumed latent symmetry and the error bound, the data do not force an exact prevalence.

The stronger premise must be justified. The selected two-bin sector has explicitly tested physical operations that flip the two signs separately, but they are not proved symmetries of the complete physical–experiential law, the reporter's identity, or the actual incidence measure. A transformation could carry r to a different reporter. If a theory additionally requires the **report law itself** to be invariant under those transformations, the unequal illustrative q values would violate that stronger hypothesis rather than support it. No such symmetry has been assumed for the q table.

This is the constructive role of the symmetry: it can strengthen an evidential inference when a full subject-level invariance and population correspondence have independently been established. It is not an excuse to infer equal experiences or weights from a symmetric physical state.

## 5. Calibration is the deciding premise, not an automatic consequence

The verifier builds three formal models with the same synthetic physical cell weights and the same per-cell affirmative-report rates:

1. A model attaining the cellwise lower prevalence `4/9` and satisfying `f≤1/10`.
2. A model with the symmetric latent prevalence `7/9`, also satisfying the bound.
3. A model with `p=1`, whose positive experiences are sometimes not affirmatively reported.

It also builds a fourth, **uncalibrated** model with `p=0` and the same physical/report marginals. In that model all affirmative reports are false positives, violating the assumed `f≤1/10` in every cell. This is a mathematical countermodel showing what the independent calibration excludes; it is **not** an assertion that real people systematically misreport their experiences. A genuine first-person observation or a justified experiential law can exclude that countermodel. Physical report agreement alone does not do so.

Under a strict no-joint-experience package covering r, `p=0`. If a justified `f` bound applies and `q>f` is established, the package and those premises cannot all be true. A positive case need not settle which assumption fails: the physical-to-aspect mapping, target window, population coverage, reporting channel, or strict no-joint claim could be wrong. Conversely, a lack of affirmative reports does not reject a joint-experience model without an independently supported sensitivity bound.

For repeated trials the [previous conditional protocol](ZERO_JOINT_UNITY_REPORT_AND_INCIDENCE_SYMMETRY.md) computes an illustrative nine-trial IID tail and gives an exact correlated-error control with the same per-trial error rate. That two-sided design remains mathematically valid under its stronger assumptions. It is **not required** for the one-sided positive inference here, and the actual echo does not supply a calibrated reporter, independent human trials or a durable measurement record.

## 6. A joint witness does not count all subjects

The test builds two formal field assignments with the **same reporter r and the same reporter-level conjunction**:

* `reporter_only`: r is the one represented subject; when `E_r=1`, r's field includes both distinct aspect tokens `N_r` and `K_r`.
* `nested_private`: r has exactly the same field and report, while two additional hypothetical private subjects have their own distinct tokens `N_private` and `K_private`.

They have one and three represented subject candidates, respectively. The private tokens are **not** assumed numerically identical to the reporter's tokens merely because their assigned physical signs match; they are not established by the model at all. Their presence is stipulated as a formal alternative, and the comparison holds only while they have no additional observable reports in the accessible data. Other interventions or genuinely independent private reports could distinguish a fuller theory.

A positive witness for r therefore rules out an exhaustive package that forbids r's conjunction, if coverage and interpretation hold. It does **not** rule out additional private perspectives, establish a global subject, prove the nested alternative, or fix the earlier joint-versus-split incidence weight. This respects both the evidential force of actual lived unity and the user's requirement that genuine plurality remain an open, constructive target.

## 7. Next dependency

The remaining task is not to demand universal negative calibration before taking any positive experience seriously. It is to justify the **specific positive bridge** for a real target: identify the reporter and the two aspects without equating them to structural bits by fiat; establish population coverage and temporal alignment; seek a defensible one-sided report bound or direct first-person witness; and specify permitted intervention and record resources. Separately investigate whether other subjects can coexist or share physical supports, rather than infer an upper census from one reporter.

No such calibrated positive unity witness, physical–experiential identity, actual incidence measure or self-sufficient zero constitution has been obtained in this pass. The calculation makes the pathway and its conditional evidential force explicit.

Reproduce:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_positive_unity_witness_test \
  verification.zero_joint_unity_bridge_test \
  verification.positive_experience_witness_gate_test -v
```
