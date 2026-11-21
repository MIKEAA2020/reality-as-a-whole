# Integrated subject and quality across two query horizons

## Result and boundary of the result

The [integrated E-L candidate](INTEGRATED_EXPERIENTIAL_MISALIGNMENT_CANDIDATE.md) previously specified a binary unpleasant/neutral postulate for its two selected pairs but had no quality output when its own nine-update query selects the four-node whole. We now give **two explicit, experience-respecting, same-domain extensions** that agree with every original pair output yet give different predictions for that whole. The comparison is an additional constraint on the proposed bridge, not a derived bridge or a pass of B4–B5/F2. The [calculation plan](INTEGRATED_CANDIDATE_CROSS_SCALE_COMPLETION_PLAN.md) fixes the assumptions and contrast; the [implementation](verification/integrated_cross_scale_quality.py), [tests](verification/integrated_cross_scale_quality_test.py), and [receipt](verification/integrated_cross_scale_quality.json) preserve the calculation.

C3 remains **full structural and experiential intelligibility**, jointly with C1–C7; experience is accepted as a datum. Neither candidate denies experience. We have not shown that either formal description is a genuinely possible world or that this spin system describes a subject. Their disagreement shows that **the previously stipulated pair law and the finite physical sector do not, by themselves, determine the new whole-subject quality law**. It does not prove that all experience is unknowable or that no independently justified bridge exists.

## One physical sector, two query scales

Retain `t=1/4`, the distribution `P_t`, single-site heat-bath kernel, eligibility and the original L rule, without replacing its one-update definition. The [horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md) showed that the original one-update rule selects `{0,1}` and `{2,3}`; the otherwise specified nine-update variant selects `{0,1,2,3}`. The latter is a **different query** to the same physical kernel, not the original rule and not evidence that two subjects literally merge in time. No physical/experiential principle yet selects one horizon. At `t=1/2` the original one-step rule leaves six tied competitors unresolved, so neither extension assigns a quality to an L-selected subject there.

Let each physical chain edge have preferred alignment and `q_ij=(1−s_i s_j)/2`. Its model weight is `(1+c_ij s_i s_j)` with outer couplings `c=1/2` and middle coupling `c=1/4`. The aligned-to-misaligned factor ratio gives the nonnegative, dimensionless edge cost `a_ij=ln[(1+c_ij)/(1−c_ij)]`: `a_outer=ln 3`, `a_middle=ln(5/3)`. Thus, for any connected selected subset here,

```text
D(S,s) = sum over internal edges of a_ij q_ij / sum over internal edges of a_ij.
```

This is current energy excess over this particular aligned chain's zero-cost ground state, normalized by maximum edge cost. Temperature and logarithmic energy are properties of this stipulated statistical model, not demonstrated physics of a brain or strings. It is **not** minimum frustration, dissipation, a measured affective quantity, or a proof of phenomenal intensity. On each outer pair `D=q`, hence it exactly preserves the original pair law.

## Same-domain quality rivals

Both descriptions retain the identical physical model, subject selector at the queried horizon, and one normalized negative-valence reference scale:

* **Graded E-L+:** postulate that each L-selected subject's comparative unpleasantness is `U(S,s)=D(S,s)`; 0 is the neutral reference.
* **Binary E-L+:** postulate instead `U(S,s)=1` whenever `D(S,s)>0`, and 0 otherwise.

Both preserve the original qualitative pair contrast, and neither follows from the equations. The common 0–1 interpersonal and cross-horizon scale, numerical intensity, subject incidence and experience/quality interpretation are further assumptions, not consequences of the original binary postulate. This is not the earlier neutral-ground rival: both here respect the experiential-ground hypothesis. Nor do they provide independently defensible constitution laws simply by being explicit. A different extension could assign pleasant rather than unpleasant qualities or depend on context; these examples do not exhaust the options.

At the nine-update query, write `k=q_01+q_23` and `m=q_12`. The model's exact equilibrium weights and stipulated qualities are:

| k | m | physical probability | graded U | binary U |
|---:|---:|---:|---:|---:|
| 0 | 0 | 45/128 | 0 | 0 |
| 0 | 1 | 27/128 | 0.188632 | 1 |
| 1 | 0 | 15/64 | 0.405684 | 1 |
| 1 | 1 | 9/64 | 0.594316 | 1 |
| 2 | 0 | 5/128 | 0.811368 | 1 |
| 2 | 1 | 3/128 | 1 | 1 |

The physical model gives non-extreme states total probability `5/8`, where the two assigned values differ; its mean binary-minus-graded score is about `0.374858`. These numbers are **not** subject-reference-class probabilities, observations, or a derivation of Born weights. The contrast is not merely a change of numerical units: for example, the graded law distinguishes the middle-only state from a one-outer-only state, whereas the binary law assigns both the same value. Their full ordering differs even if an unknown strictly increasing remapping of the scale is permitted. This claim still assumes the respective experiences can be identified and compared across these states.

## A conditional discriminating target

Fix in advance the physical event `k=1, m=0`, probability `15/64` in this model. The predicted graded value is `ln(3)/(2 ln(3)+ln(5/3)) ≈ 0.405684`; the binary value is `1`, a gap of about `0.594316`.

Suppose, as an **additional and currently unvalidated assumption**, that (i) the whole at the nine-update query really is one subject, (ii) a single common, externally anchored numerical scale applies, and (iii) a readout of that subject in this event has mean absolute error at most `ε` relative to the actual quality under either hypothesis. For any one distribution of readout `R`, the triangle inequality gives `|1−0.405684| ≤ E|R−0.405684|+E|R−1|`. Hence both hypotheses cannot simultaneously have such an error bound if `ε < 0.297158`. This is a conditional identification inequality, not a statistical confidence interval or a sample-size calculation; equality at the threshold does not discriminate. It assumes the same readout population and event definition for both hypotheses. Using only rank comparisons avoids an arbitrary affine numerical scale but still requires an independent ordinal quality assay and subjects that persist or are otherwise comparable.

No such independently validated readout has been supplied for this synthetic sector. Self-report requires an account of report access and unity, not merely a label attached to the model; existing music/EEG evidence is not a measurement of the specific interaction preferences or subjects here. A real test would additionally require a justified physical realization, event identification and intervention, independently anchored qualitative measurement, precommitted error bounds, and validation against context, attention and report-access confounds. Thus no prediction has yet been empirically tested.

## Subject persistence and invariance are still missing

At the two query horizons both pair sets overlap the whole. This gives a **two-to-one set-overlap relation**, not numerical subject identity, continued ownership of one experience, a theory of fusion, or a proof against overlap. Simply declaring the whole to be either pair would introduce an unsupported selection; simply declaring it a new or additional subject would also be an extra premise. The effect of different queries does not establish any real dynamical change, and neither the equilibrium state nor the heat-bath calculation supplies an intrinsic temporal direction for the timeless whole. [Subject incidence and persistence](PLURAL_EXPERIENTIAL_GROUND_SUBJECT_CONSTITUTION.md) and the [horizon audit](INTEGRATED_SUBJECT_HORIZON_AND_VALENCE_AUDIT.md) remain controlling constraints.

The verifier explicitly transports physical edges, preferred signs, states and already-selected sets through all 24 node permutations and 16 local sign recodings, for all 16 states and all three subsets: 18,432 checks. Both quality outputs are invariant on these transported sets. This checks a representation property of the *quality expression*, not independent invariance of the subject-selection procedure, cross-substrate realization, or persistence. The earlier [candidate verifier](verification/integrated_experiential_misalignment_candidate.py) checks the original finite representation transport. An arbitrary change of the interaction model, intervention scope or horizon is not a harmless relabeling.

## Battery consequences and next necessary step

* **B4/F2 remains open:** no independently justified subject boundaries, unity, persistence, rule for tied cases, or mapping from subjects to these finite sets.
* **B5/F2 remains open:** the new four-node output is stipulated, and same pair data admit inequivalent extensions. No argument establishes why either one is felt or unpleasant. No full phenomenal palette or experiential intelligibility follows.
* **B9/F3 remains open:** physical equilibrium weights do not specify an experiential reference class or self-location measure, even if all genuine possibilities are actual.
* **B10 remains open:** the conditional inequality is not an actual assay or empirical result. All regressions here are checks of specified code and assumptions, not the external battery.

The next decisive dependency is therefore not a more elaborate graph score: it is an independent reason or calibrated observation tying a physical/relational intervention to *which* subject has *which* experience, including persistence and the quality comparison, or a defensible proof of constitution. Until that dependency is met, elegance and formal scale-completeness cannot decide the rivals. No claim is made that a neutral ground is impossible, that a single universal subject exists, or that possibility is converted into actuality in time.
