# When could the maintained-disclosure contrast be identifiable?

## 1. A concrete result

The [frozen H_M1/H_D1 contrast](MAINTAINED_DISCLOSURE_CANDIDATE.md) has different conditional experiential consequences but no independently warranted observation relation in the existing model. This report derives an explicit criterion for when an assay would separate them.

> **For deterministic rival predictions about one precisely defined target, if the assay's false-positive probability is at most alpha and its false-negative probability is at most beta in the intervention condition, the permitted observation-probability intervals are disjoint exactly when alpha + beta < 1.**

This is a bounded identification result under stated premises, not an empirical calibration, a consciousness test, or a derivation of a psychophysical identity. It turns the generic demand for “reliable evidence” into a concrete requirement that can fail. The [robust experiential contrast](ROBUST_EXPERIENTIAL_CONTRAST.md) extends the calculation to trial-wise failures of the shared physical prerequisites and shows the sharp separation criterion under explicit bounds; it does not establish those bounds empirically.

The complete absolute and finite-disclosure framework remain unchanged. Local observations concern limited evidence within the one actuality, not an external observer selecting a world or manufacturing a perspective.

## 2. Freeze the target before the assay

Let E mean that **the nominated, independently anchored qualitative/incidence organization is preserved** under the proposed intervention, relative to the declared baseline equivalence. This is not a binary definition of consciousness in general. Different episodes may preserve the nominated organization without being numerically identical tokens.

Let Y be a binary assay judgment intended to distinguish E from not-E. For example, a judgment about an anchored quality contrast could be considered only if it actually targets that contrast. A generic “I saw something” response is not automatically evidence for a particular orientation, co-presentation, or subject boundary.

If the target changes from content to unity, the assay's calibration must change accordingly. An assay cannot identify a finer target merely because it predicts a coarser report.

All probabilities below concern a declared population/model and intervention condition. A trial-wise target may have a model-based propensity or a frequency across admissible repetitions; this notation does not establish fundamental randomness, a population of universes, or an observer measure.

## 3. Shared physical premises come first

The contrast discriminates the constitutive claims only if:

- the proposed maintaining basis is independently specified and genuinely preserved in its claimed relevant respects;
- the additional distribution feature is genuinely removed, not relocated into the replacement route;
- the baseline target is independently warranted;
- the scope, interval, and target equivalence are fixed before assessing the outcome.

There is an important qualification to the word “full”: the hypotheses do **not** require the entire physical process to remain identical while a physical feature changes. That would be impossible by construction. They require preservation of the **declared maintenance basis** while the rival's extra feature changes. What must be fully audited is that declared basis and its relevant counterfactual powers—not every omitted variable of the whole system.

The basis must be specified without assuming its phenomenal sufficiency. Its scope may be contested, but a theory cannot enlarge it after each adverse result without recording a revision. The existing equality of C = (workspace, feedback) is an exact reduced result; it does not establish that this particular C captures the proposed intrinsic maintenance powers.

## 4. Derivation of the observation relation

For the intervention condition z, write:

    theta_z = Pr(E | z)
    s_z     = Pr(Y=1 | E, z)       [sensitivity]
    f_z     = Pr(Y=1 | not E, z)   [false-positive probability]
    q_z     = Pr(Y=1 | z).

On the declared event partition, the law of total probability gives:

    q_z = s_z theta_z + f_z (1-theta_z)
        = f_z + (s_z-f_z) theta_z.

No phenomenal identity follows from this probability identity. Sensitivity and false-positive rates need independent warrant for the target and condition. If one event has zero probability, its conditional kernel needs a justified counterfactual or broader calibration model; the equation does not magically supply it from that condition's data.

### Unrestricted assay: no discrimination

If s and f can be chosen freely for each rival, then for any observed q:

- theta = 1 can fit by taking s = q;
- theta = 0 can fit by taking f = q.

Thus the observation probability alone cannot choose between the deterministic experiential predictions. This is a nuisance-parameter identification failure, not proof that experiential evidence is impossible or that every report is unreliable.

If s = f, q does not depend on theta. If s and f are independently known with s != f, then theta = (q-f)/(s-f), provided the result lies in [0,1] and the model is warranted. The informative orientation s > f is used below; a known reversed assay can be recoded.

## 5. Bounded errors: exact separating criterion

Suppose the intervention-condition calibration warrants:

    f <= alpha,
    1-s <= beta,
    0 <= alpha,beta <= 1.

Under H_M1 with the shared preservation/removal premises and deterministic target preservation, theta = 1, so:

    q_M is in [1-beta, 1].

Under the frozen H_D1 consequence of target nonpreservation, theta = 0, so:

    q_D is in [0, alpha].

These closed intervals are disjoint iff:

    1-beta > alpha,
    equivalently alpha+beta < 1.

At alpha+beta = 1 they touch. Above it they overlap. Disjoint model-probability intervals do not guarantee discrimination by a finite noisy sample; a data-supported interval for q must be narrow enough too.

**Illustrative numbers, not measurements:** alpha = beta = 1/5 gives q_D <= 1/5 and q_M >= 4/5. Alpha = 3/5 and beta = 1/2 permits overlap [1/2, 3/5], so some exact probabilities fit both. The examples demonstrate assumptions' consequences, not the real accuracy of any assay.

This criterion says how good a calibrated channel must be for the stated deterministic comparison. It does not establish that such a channel is available during an intervention that changes access itself.

## 6. Graded predictions and calibration uncertainty

Neither rival need be forced into deterministic predictions in a noisy empirical domain. Suppose a specified version warrants:

    theta_M in [mL,mU], theta_D in [dL,dU],
    s in [sL,sU], f in [fL,fU].

For a rectangular uncertainty set, q = f+(s-f)theta is multiaffine; its extrema occur among the eight endpoint combinations. That fact allows exact interval projection without replacing uncertain calibration by a preferred point estimate. It is an outer identified set if the rectangle relaxes additional constraints.

If 0 <= fL <= fU <= sL <= sU <= 1, the bounds simplify for theta in [a,b]:

    q_min = fL + (sL-fL)a,
    q_max = fU + (sU-fU)b.

The projected probability intervals must be compared. Overlap means some compatible probabilities remain under both; it does not mean every probability fits both or that the full models are equivalent.

Calibration may involve coupled parameters or shared constraints across conditions; do not use a rectangular model to claim an exact set in those cases. The endpoint enumeration is exact for the declared box, not automatically for richer evidence models.

### Observation intervals, not manufactured data

Given an independently justified uncertainty interval J for q, assess its intersection with each rival's projected set:

- intersects both: unresolved on this evidence;
- intersects only one: incompatible with the other within the stated assumptions and uncertainty procedure;
- intersects neither: at least one premise, model, calibration bound, or data analysis needs revision.

An interval excluding a rival is not an assumption-free logical refutation; its inferential guarantee depends on how J was constructed. Repeated observations require justified sampling/dependence assumptions, not an automatic binomial model. No observations or confidence interval have been generated for this report.

## 7. Why ordinary baseline calibration is insufficient

A report may be reliable in the baseline yet change its relation to the target when distribution is removed. Assuming the same s and f is a **transport premise**, not a consequence of matching a reduced state or a report trajectory.

An acceptable calibration proposal must specify:

1. which independent anchors identify E and not-E;
2. what warrants their use under the intervention, including cases where one target state is absent from that condition;
3. which observed channels support the error bounds and how they share failure modes;
4. why the intervention does not destroy or relocate the channel being calibrated;
5. which result would invalidate calibration rather than be reinterpreted to protect a theory.

Multiple channels do not become independent by being separately named. Reports, memory, confidence, and task performance may depend on a common altered pathway. A joint assay requires its own calibration; multiplying unverified likelihoods would overstate discrimination.

For the present one-slot model, Y is computed directly from W. The model specifies its physical report rule, not s or f relative to E. The observed report equality therefore provides no independently established error bounds for the experiential target. Introducing assumed alpha/beta values would manufacture the missing evidence.

## 8. Executable audit and limits

[The identifiability check](verification/disclosure_observation_identifiability.py) uses exact rational arithmetic to verify:

- unrestricted endpoint predictions can share every q on a declared grid;
- the deterministic interval separation criterion across a rational grid, including touching endpoints;
- projection of graded rectangular uncertainty at endpoints and interior witness points;
- evidence intervals compatible with both, one, or neither rival;
- rejection of invalid probability intervals.

[Retained diagnostics](verification/disclosure_observation_identifiability.json) record synthetic mathematical examples only. No neuronal model is changed, no experience is assigned to software, and no primary experiments are reproduced. The established core research test count is unchanged.

## 9. Consequence for the constitution programme

The next empirical design must meet **two independent contracts**:

- **physical contract:** genuinely preserve the frozen candidate basis and remove the rival's specified extra feature;
- **evidential contract:** independently warrant observation bounds under that same intervention that leave discriminating predictions.

Neither contract establishes the other. Complete physical characterization alone does not provide a target-valid assay; ordinary assay reliability alone does not establish constitutive preservation. The result also does not identify chi, Gamma, or the absolute's intrinsic nature.

The current contrast remains unresolved. But the missing evidence is now specified mathematically: a condition-valid, target-specific channel whose projected observation-probability sets separate the frozen claims, with adequate observed precision. If such calibration is unavailable, the responsible action is to redesign the contrast or seek a different constitutive argument—not to classify identical reports as decisive by stipulation.
