# Joint quality and ownership reports on the same echo

## Result and scope

The [quality comparison](ZERO_ECHO_QUALITY_BRIDGES_SECTOR_SELECTION_AND_REPORT.md) and [ownership comparison](ZERO_ECHO_JOINT_CANDIDATE_ACCESS_AND_IDENTITY_WITNESS.md) can be made on **the same selected runs**, without assuming that their report errors are independent. With independently justified, matched false-positive bounds, a joint affirmative report gives a conservative lower bound on the proportion of selected reporter-runs that are both neutral in the specified signed-valence sense and owned by the same subject at two distinct checkpoints. This proportion is not a census of all subjects or all experiences.

The existing echo supplies physical records and candidate structural quantities, **not** experiential truth labels. Both witness channels, reference labels, reporter alignment and the persistent/momentary ownership rules below are hypotheses. Our numerical reports and calibration data are synthetic or hypothetical; no experiencer or phenomenal reference state was measured. [Code](verification/zero_echo_quality_ownership_joint.py) and [tests](verification/zero_echo_quality_ownership_joint_test.py).

## 1. Align the questions before joining them

At the anchor of the same recorded echo, H selects its reported negative R sector, H=−. Retain the original equal physical event weights `1/8` and the same candidate scalars:

```text
A = pointer:       v_A = G M,
B = type-symmetric: v_B = G (N+K)/2,  N=MJ, K=MJR.
```

On this support G is positive. A has no zero-valued events; B is zero exactly on R=−. Interpret `D=1` as *neutral signed valence* only under the candidate's stated phenomenal bridge. Neutrality is not the absence of experience, nor does pairwise zero erase negative experience.

Let `O=1` mean the very same specified subject owns the relevant slots at **two distinct, fixed, aligned checkpoints**. In the simple persistent hypothesis P, O is 1 for every selected run. In the simple momentary hypothesis F, those two slots have different owners, so O is 0 for every run. F does not claim that no subject exists, nor are P and F the only possible ownership rules.

For every included run, `Y=1` is an affirmative neutral-quality report and `W=1` is an affirmative same-owner report. Both refer to the **same reporter, target, selected population, checkpoint/window pair and jointly administered protocol**. The protocol must define the quality time within that pair and establish correspondence between the reporter and each claimed slot. A pairing of one subject's neutral report with another subject's identity report does not establish a neutral persistent subject; the tests give a simple counterexample. Joint administration can disturb either report or change selection, so bounds established in isolated protocols do not automatically transfer.

## 2. Four candidate combinations and noisy selection

Let `p_L` bound the preselection frequency of R=− from below; let `e_−` and `e_+` bound the selector's negative-to-positive and positive-to-negative error rates above. As derived in the previous pass, the selected negative-sector fraction is at least

```text
L = p_L(1−e_−) / [p_L(1−e_−) + (1−p_L)e_+],
```

with a conservative zero returned for a degenerate denominator. In the selected, joint-protocol population suppose independently supported bounds

```text
P(Y=1 | D=0) ≤ f_y,    P(Y=0 | D=1) ≤ g_y,
P(W=1 | O=0) ≤ f_w,    P(W=0 | O=1) ≤ g_w.
```

Where a conditioning event has zero probability, its inequality is vacuous. These are population-conditional bounds, not assumptions of independent errors or constant accuracy in every latent sector. Write `q_y=P(Y=1)`, `q_w=P(W=1)`. The candidate-implied **necessary** ranges are:

| Quality candidate | Necessary report bound | Owner candidate | Necessary report bound |
|---|---|---|---|
| A | `q_y ≤ f_y` | P | `q_w ≥ 1−g_w` |
| B | `q_y ≥ L(1−g_y)` | F | `q_w ≤ f_w` |

All four pairs A/P, A/F, B/P and B/F can be examined by intersecting their two necessary marginal conditions with simultaneous confidence intervals. This deliberately conservative screen is not a complete joint-likelihood test: survival does not prove compatibility with all joint frequencies, much less truth, and both quality candidates or both ownership candidates can fail. Sector selection may be correlated with witness errors; the relevant error bounds must already apply after selection in the joint protocol.

## 3. A positive joint report without independent errors

In the matched selected population define `t=P(D=1,O=1)` and `q_11=P(Y=1,W=1)`. On a joint-affirmative run outside D=O=1 at least one affirmative is false. Therefore

```text
q_11 ≤ t + P(Y=1,D=0) + P(W=1,O=0)
     ≤ t + f_y P(D=0) + f_w P(O=0)
     ≤ t + (f_y+f_w)(1−t).
```

Thus for `f_y+f_w<1`,

```text
t ≥ max(0, [q_11−f_y−f_w]/[1−f_y−f_w]);
```

otherwise use the conservative lower bound zero. This uses only false-positive bounds: no missed-report rates, selector bound or independence of report errors is needed for the positive inference itself. The expression is conservative, not asserted to be optimal. It applies to an aligned population, not to mismatched reports or unreported subjects. For example, if `q_11=.77` and both false-positive bounds are `.1`, the lower bound is `.7125` conditional on those premises.

A second bound uses the individual report marginals: `d_L=max(0,(q_y−f_y)/(1−f_y))` and `o_L=max(0,(q_w−f_w)/(1−f_w))`, taking zero if a denominator vanishes. The Fréchet inequality gives `t≥max(0,d_L+o_L−1)`. The implementation reports the larger of this marginal bound and the direct bound when all three rates are available; neither assumes independence. Sampling bounds below replace unknown rates by simultaneous lower confidence bounds and false-positive parameters by upper confidence bounds.

## 4. Finite calibration and data budgets

For N iid selected joint answers let `k_11,k_10,k_01,k_00` count the four `(Y,W)` values. The three empirical rates are `(k_11+k_10)/N`, `(k_11+k_01)/N`, and `k_11/N`. With seven independent-*reference* calibration batches for `p,e_−,e_+,f_y,g_y,f_w,g_w`, allocate total failure probability δ equally to seven one-sided calibration events and three two-sided data-rate events. Each calibration bound has radius

```text
r_cal = sqrt[log(10/δ)/(2 n_cal)],
```

using a lower bound for p and upper bounds for the errors. Each two-sided data interval has radius `sqrt[log(20/δ)/(2N)]`. Clip all probability bounds to [0,1]. A union bound gives simultaneous coverage at least `1−δ` under the specified iid, matching and reference-label premises. **No independence between batches** is required by the union bound; iid trials within each relevant batch, the same source distribution, appropriate joint protocol and validity of experiential/identity labels do matter. A missing required batch is rejected, not assigned a perfect error rate.

A separate positive-only procedure allocates δ/3 to the lower q_11 bound and each of the two false-positive upper bounds. Its one-sided radius is `sqrt[log(3/δ)/(2n)]` for the corresponding batch. This does not require calibration of sensitivity, the selector or the candidate family; it still requires warranted false-positive labels and matched sampling. No generic iid guarantee exists for repeated reports with shared memory, drift, common causes or adaptive selection.

## 5. Correlated controls and hypothetical results

A fully specified synthetic generator uses the same physical echo distribution and H error `.1` in both sectors. Its nominal neutral and identity false-positive and miss rates are `.1`, and it chooses any Fréchet coupling of the two witness outcomes within each latent category. Under B/P, varying that coupling from its lower to upper extreme changes

```text
q_y = .82,  q_w = .90,  while q_11 ranges from .72 to .82.
```

At the midpoint `q_11=.77`. The physical `(i,s,H)` marginal is exactly unchanged across all four bridge/ownership constructions. The new witness outputs are additional modeled channels, not outputs of the original circuit and not evidence of experience. Dependence between them is explicit; the inferential inequalities above do not require even this particular coupling.

For each synthetic candidate, seed 204204 produces the following multinomial counts for N=1000, in `(11,10,01,00)` order. Separately suppose seven hypothetical 100,000-trial matched calibration batches: 50,000 negative-sector instances and 10,000 errors in each other batch. With δ=.05, the conservative marginal screen retains only the generating candidate in each example:

| Generated assumption | Synthetic counts | Candidate not rejected |
|---|---|---|
| A/P | (43, 44, 862, 51) | A/P |
| A/F | (43, 44, 51, 862) | A/F |
| B/P | (753, 54, 134, 59) | B/P |
| B/F | (43, 767, 54, 136) | B/F |

For the B/P example, the ten-event procedure gives direct joint-truth lower bound approximately `.6179`, marginal Fréchet lower bound `.5357`, and hence `.6179` combined. Using instead the separate positive-only budget and the same hypothetical false-positive calibration counts gives `.6305`. The different budgets answer related conditional questions and must not be combined as if they shared one unchanged confidence allocation. A synthetic `(250,250,250,250)` data table rejects **all four** candidates under the illustrative parameter bounds; it does not prove that the witness premises are true.

### Physical shortcut control

The very same physical report table generated under the B/P labeling can be relabeled under A/P without changing any observed bit. Its selected neutral-report false-positive rate becomes `.82` under A, rather than `.1`; A has no neutral reference events on this support. If one simply asserts the `.1` calibration under A, the positive formula would incorrectly infer a substantial joint prevalence even though A/P assigns zero true neutral events. This diagnoses the missing premise: a physical sector-driven output can mimic a well-performing B witness, but cannot by itself tell us which experiential labeling is correct. Accurate H measurements and simulated channels do not establish the needed reference labels.

## 6. Follow the causal and constitutive chain

1. **Why might the joint affirmative matter?** If both claims concern the same aligned reporter and each false-positive bound genuinely transfers to the selected joint protocol, a high joint rate cannot be explained entirely by the permitted false affirmatives. The bound gives a proportion of those selected runs, not the number of subjects.
2. **Why is conditioning essential?** H selection, clock choice, shared apparatus and joint administration can change error rates or reporter composition. Separate physical and phenomenal calibration, temporal alignment, disturbance and access have to be established for this protocol rather than inferred from a clean circuit.
3. **Why does a model fit not establish an owner?** The original physical records admit the stipulated P and F extensions; the synthetic witness law was constructed from assumed truths. A separate warranted connection to actual first-person evidence is needed, and neither an unavailable report nor a shared physical record rules out plural or overlapping subjects.
4. **Why not infer all incidence or cancellation?** Trial fractions describe the declared sampling procedure, not an independently derived measure of actual experiential occurrences. Neutral valence is not nonexistence; a formally opposite pair does not cancel a subject's real negative experience.
5. **Why these bridges, selection and laws?** They are consistent candidate relations attached to the same echo, not yet consequences of zero, a subject constitution, actual measure, or the necessity and actuality of the whole. The task remains to derive or independently discriminate those connections and carry the why-chain upstream without assuming an external temporal cause. The present boundary is not shown to be ultimate bedrock.

## Next work

- Specify an independently defensible experiential/identity reference and an actual joint interface, including response disturbance, subject alignment and reference transport across clock descriptions.
- Compare model predictions for the *full joint distribution*, not only necessary marginal screens, under explicitly bounded dependencies and realistic non-iid sampling.
- Connect any warranted selected-run occurrence measure to a candidate subject-individuation and incidence law without suppressing plurality, negative experience or nonreported cases.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_quality_ownership_joint_test -v
```

The checks cover exact synthetic physical marginals and correlated couplings, arbitrary truth/report tables for the lower bounds, calibration bookkeeping, hypothetical candidate outcomes and the physical-shortcut and mismatched-reporter controls. They are not an empirical validation of consciousness, identity or the whole.
