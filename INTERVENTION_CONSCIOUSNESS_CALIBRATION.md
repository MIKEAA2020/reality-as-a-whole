# Can the maintained-disclosure contrast be tested in a real intervention?

## Decision

I examined an actual matched report/eye-movement study, a causal prefrontal perturbation study, and the no-report/EEG study already cited in the [one-whole access test](ONE_WHOLE_FINITE_ACCESS.md). **None of the three, as inspected, establishes all three conditions of our frozen H_M1/H_D1 comparison:** preservation of the candidate maintenance basis (P3), removal of the specified distribution (P4), and an intervention-valid assay for the same phenomenal target (P6). This is an assessment of a short list, not an exhaustive systematic review or a proof that no existing experiment works.

A useful positive development is that a real paired-report-and-eye-movement dataset **does exist**, rather than being merely hypothetical. But its published agreement does not by itself yield the condition-specific phenomenal error bounds our comparison requires. A finite-sample check below also shows why a high average agreement and many repeated trials can mislead in different ways.

The global purpose is M4 of the [whole-account plan](GLOBAL_COHERENCE_AND_DECISION_PLAN.md): test a candidate for how limited experience is organized within the same actual process. Nothing here decides whether that experience belongs ultimately to one universal consciousness. The two local rivals and P3/P4/P6 are frozen in [Maintained Disclosure](MAINTAINED_DISCLOSURE_CANDIDATE.md), and the existing population-level identification condition is in the [observation audit](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md).

## 1. A real candidate assay: paired fixation and reports

[Hesse and Tsao, *eLife* (2020)](https://elifesciences.org/articles/58360) used a binocular-rivalry fixation task with a face and an object. In a behavioral validation, **six human participants** tracked fixation spots while also reporting the apparent percept; the paper reports 86–98% agreement across participants, mean 93%. The neural recording portion used **two macaques** in a related no-voluntary-report task; inferred percepts were based on gaze. The human trials were 2,000 ms, the macaque trials 800 ms. The authors report that activity in IT face patches carried information about both the inferred dominant and suppressed stimuli, and controlled eye-of-origin/color confounds.

This is a valuable existing reference and a better candidate for face/object calibration than combining unrelated face-report and motion-OKN datasets. But it is not an intervention satisfying our contract:

- **P3:** The study does not show that a specified maintaining basis and its causal powers are preserved under an intervention removing distribution. It is a recording/decoding experiment, not that perturbation.
- **P4:** The absence of voluntary percept reporting does not establish absence of the specified multi-consumer distribution. Eye tracking is itself an active task; other distribution and monitoring may remain.
- **P6:** Human gaze/report agreement provides a meaningful baseline surrogate comparison, but it is not an experimentally measured false-positive and false-negative bound against **true phenomenal preservation** in a distribution-removal intervention. The macaques did not provide voluntary percept labels, and applying human calibration to them requires cross-species and task-duration transport. Even within humans, a gaze/report match is not automatically a content-preservation assay or an error bound against experience itself.

The numbers above are source-reported; no raw data were downloaded, no subject-level confusion matrices were reconstructed, and no independent validation was run. The paper's overall accuracy is not a bound on class-conditional errors in another condition. The 86–98% refers to human participant agreement in that task, not to the two macaques or to a TMS condition.

## 2. A real causal intervention: what it changes

[Zanto and colleagues (2011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3083493/) used fMRI-guided repetitive TMS to perturb the right inferior frontal junction before a selective-attention/working-memory task and measured EEG. They reported reductions in posterior visual attentional modulation and later color working-memory accuracy, compared with sham, under their specified conditions. The authors also caution that their data do not directly measure disruption of functional connectivity.

This is an instructive **P3 adversary**: changing a putative downstream control region can alter the putative upstream/posterior basis itself. It does not show the same effect would occur for every region, stimulus, timing or intervention, nor does it show that the particular P4 distribution is removed. Its memory outcome is not the frozen phenomenal preservation target. Combining its TMS effects with Hesse and Tsao's separately obtained eye/report calibration would not produce paired evidence for the required same-subject, same-condition contrast.

[Allen et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/32922860/) also used time-targeted TMS and preregistered comparisons to examine putative feed-forward and recurrent processing. Their reported findings challenge a simple feed-forward/unconscious versus recurrent/conscious division. They do not establish the exact P3/P4 intervention here. Likewise, [Cohen et al. (2020)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7326348/) separated report and no-report conditions and found their P3b contrast strongly task-dependent; a missing P3b is not proof that every targeted distribution pathway vanished, and the no-report experience assessment is indirect.

## 3. Why 93% agreement is not enough

Let `E` denote the nominated phenomenal target, `R` an independently anchored report, and `O` a proposed ocular assay. Define

    alpha = Pr(O=1 | E=0),   beta = Pr(O=0 | E=1).

Our earlier population-level criterion for deterministic, opposing predictions needs `alpha+beta<1` **in the intervention condition**. Overall O–R accuracy alone does not supply it. For example, if `Pr(E=1)=.93`, R always matches E, and O always outputs 1, then O and R agree 93% of the time, but `alpha=1` and `beta=0`. The assay conveys no discrimination of E. This is a constructed example, **not** an assertion about the actual study's class balance or classifier.

There is nevertheless a useful conditional route. By the union bound,

    Pr(O != E) <= Pr(O != R) + Pr(R != E).

Suppose both quantities are separately bounded in the target intervention condition by `delta` and `e_R`, and target prevalence satisfies `epsilon <= Pr(E=1) <= 1-epsilon`. Then

    alpha + beta <= (delta + e_R)/epsilon.

So if `delta+e_R < epsilon`, the required separation follows. For a purely illustrative balanced target, `epsilon=1/2`, `delta<=.1`, and `e_R<=.1` imply `alpha+beta<=.4`. The unequal-prevalence inequality is conservative; no specific class-error estimates, prevalence, reference error, or confidence limits are provided by these hypothetical values. The first error compares two channels; the second requires independent warrant for the report–experience relation. Estimating the first from the unperturbed human mean 93% and silently assuming the second to be zero would not justify applying the result to the macaque, a different target, or a perturbation.

In particular H_M1/H_D1 disagree about preservation of an anchored qualitative/incidence organization, not simply face-versus-object categorization. A method validated for the latter does not automatically classify the former. Baseline and intervention episodes are distinct tokens; any claim of preserved content needs a prespecified equivalence criterion rather than identity of tokens.

## 4. Population separation is not a finite-sample guarantee

Consider only an illustrative, idealized assay: in the separating condition, H_D1 has `Pr(O=1)<=.2` and H_M1 has `Pr(O=1)>=.8`. These bounds require P3/P4/P6 and the hypotheses' deterministic predictions; they are **not estimated** from the papers. For independent identically distributed trials and a majority decision on an odd number of trials, the least favorable distributions occur at `.2` and `.8`. With 9 trials the exact error for each side is

    sum_{k=5}^9 C(9,k)(.2)^k(.8)^(9-k) = 0.01958144.

Seven gives a larger error than `.025`; thus 9 is the smallest **odd majority-rule** sample meeting this illustrative per-side error target under these assumptions. It is not a proposed real study size or an effect estimate.

Now keep the **same one-trial marginal bounds**, but take all repeated O values to be a single shared Bernoulli variable Z: `Pr(Z=1)=.2` under H_D1 and `.8` under H_M1. Every trial looks as accurate marginally, but all repeats are copies. The majority-rule error remains `.2` for every n; under equal priors, `.2` is also the optimal average decision error since only Z is observed. Shared attention, calibration or motor errors could induce dependence; this constructed extreme is not a claim that they do so in a particular study. Marginal assay calibration alone cannot justify binomial confidence or power. Trial clustering, common failure modes and uncertainty in calibration have to be modeled or controlled.

The [standard-library verifier](verification/assay_calibration_dependence.py) and [results](verification/assay_calibration_dependence.json) check these exact numerical illustrations. They validate arithmetic, not biological or phenomenal assumptions.

## 5. A testable contract for a future study

This is a design target for qualified researchers, **not** a claim that the required technology or calibration already exists.

1. Freeze a target content/interval, an independently defined putative maintenance basis C, a concrete distribution channel D, its consumers, and the set of physically allowed probes. Specify the two rival predictions and meaningful approximation tolerances *before* observing outcomes.
2. Randomize or otherwise justify comparisons of intervention and control episodes in the same population, including sham/active controls and clinically appropriate safety oversight. Different episodes are not the same token. Use simultaneous measurements or independently validated measurements that can address both C and D.
3. **P3 operational gate:** define a finite predeclared set of input/perturbation probes and compare the probability laws of measured C responses under control/intervention using equivalence margins and uncertainty bounds. Specify coverage of state, interval and response features; a non-significant difference is not an equivalence proof. Restricted probe equivalence does not establish unmeasured powers or qualitative identity.
4. **P4 operational gate:** independently perturb source features and bound their influence on the identified consumer outputs, allowing for alternate routes. A non-significant coefficient, no-report instruction or missing averaged ERP is not exact removal. A finite probe set can bound only those tested pathways and contrasts.
5. **P6 gate:** predeclare the experiential target and evidence channels; collect paired report/assay calibration and separately justify error/transport bounds under the intervention, including altered motor, attention, mixed-percept and missing-response conditions. Avoid using the candidate neural feature both to construct the label and to validate itself. Explicitly model correlated errors and calibration uncertainty.
6. **Robust-theory gate:** the original rivals state a contrast with ideal preservation/removal. Before treating finite tolerances as decisive, derive or stipulate *revisable robust versions* saying what each predicts when residual differences are within the chosen margins. Record that this is an additional hypothesis. If no robust predictions or adequate error bounds can be justified, the outcome stays inconclusive even if the physical measurements look similar.
7. Compare the observations to **both** predeclared predictions, including the possibility that neither fits. A passing contrast would constrain a local constitution hypothesis; it would still not prove universal consciousness, the nature of the absolute, or that this particular physical model arises from it.

**Current bottleneck:** none of the inspected papers jointly passes P3, P4 and P6 for H_M1/H_D1. The [specific extrastriate–frontal pathway follow-up](SPECIFIC_VISUAL_PATHWAY_GATE_TEST.md) audits an actual cTBS/fMRI candidate, identifies residual decodable goal-relevance information and specifies what remains unmeasured. It does not prove any gate is categorically unachievable. No new participants, data, clinical intervention or experimental finding are claimed.
