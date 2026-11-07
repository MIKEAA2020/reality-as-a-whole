# When imperfect interventions can still distinguish two local experience hypotheses

## Result and scope

This is an application of established partial identification and robust-testing ideas to the existing [maintained-disclosure contrast](MAINTAINED_DISCLOSURE_CANDIDATE.md), not a claimed new statistical theory or solution of consciousness. It asks: **if the intervention only satisfies its physical premises on some fraction of trials, and the experience assay is imperfect, can the two local hypotheses still predict different observations?**

Yes, under independently justified bounds. Conversely, if the bounds are too weak, even infinitely many measurements of the nominated binary outcome may not distinguish the hypotheses. This sharpens the earlier exact-premise criterion in [DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md](DISCLOSURE_OBSERVATION_IDENTIFIABILITY.md). It targets a local constitution question that remains after relaxing universal consciousness; it cannot distinguish universal versus plural subjects by itself.

Prior art: [Chen, Gao and Ren](https://doi.org/10.1214/16-EJS1216) study robust testing under Huber contamination, and [Obradović](https://arxiv.org/abs/2204.00180) treats partial identification of diagnostic accuracy with imperfect reference tests. The calculation below is a simple problem-specific mixture bound in that established spirit, not a claim of novelty in robust statistics. For finite-sample concentration use [Hoeffding's classical inequality](https://doi.org/10.1080/01621459.1963.10500830), under its independence conditions.

## 1. Fix the contrast before looking at data

On a prespecified population and intervention condition, take the existing rivals in a stated finite domain:

- **M:** if the relevant content-maintaining basis is preserved and the specified extra distribution removed, the nominated independently anchored experiential organization is preserved.
- **D:** under those same conditions, the nominated organization is not preserved because the specified additional distribution is necessary.

These are the restricted H_M1 and H_D1 claims. They do not exhaust consciousness theories, and D does not say all consciousness must vanish. Their local meanings can be studied without adopting the earlier universal-subject metaphysics. Neither is established by the finite circuit models.

Let `E=1` denote preservation of that exact experiential target, `Y=1` the predeclared assay's positive judgment, and `G=1` the conjunction of all necessary trial-specific prerequisites: a valid baseline target and the required intervention-specific maintenance preservation and distribution removal. Define these properties before the outcome; their full physical content is the existing P1, P3 and P4 contract, not just a convenient surrogate signal. The population and trial-wise interpretation of G must be scientifically justified: a model-level theoretical assumption or a statistical confidence statement cannot simply be renamed a trial failure rate.

Under the hypotheses, on valid trials `G=1`, M predicts `E=1` and D predicts `E=0`. The behavior of E and Y on `G=0` is unrestricted. No rule says all failed trials are conscious or unconscious, and the assay may behave arbitrarily there.

Suppose independently warranted bounds are:

```
M: Pr(G=0) <= eta_M;    Pr(Y=0, G=1) <= beta * Pr(G=1)
D: Pr(G=0) <= eta_D;    Pr(Y=1, G=1) <= alpha * Pr(G=1)
```

`beta` bounds false negatives on valid M trials, and `alpha` bounds false positives on valid D trials. The equations use joint probabilities, so they remain well-defined if `Pr(G=1)=0`. When it is positive they are the corresponding conditional error bounds. They must be **valid in the separating intervention and in the G-valid subset**; baseline test–report agreement alone does not establish this. If G includes unobserved counterfactual causal powers, calibration on the actual G-valid subset is especially difficult.

## 2. Exact sharp separation condition

Write `q_M=Pr(Y=1 | M)` and `q_D=Pr(Y=1 | D)`. From the assumptions,

```
q_M >= L = (1 - eta_M) * (1 - beta)
q_D <= U = alpha + eta_D * (1 - alpha)
```

For the first bound, discard all possible positives on failed trials, and retain at least `1-beta` of the good-trial mass. For the second, allow every failed trial to be positive and at most an `alpha` fraction of good trials to be positive. No independence of assay errors from gate failures is assumed.

**The two sets of admissible Y-probabilities are exactly `[L,1]` for M and `[0,U]` for D.** The endpoints are achieved by putting all allowed assay error on valid trials and selecting extreme Y outcomes on invalid trials; convex mixtures fill each interval. Thus the interval predictions are disjoint **if and only if**

```
(1 - eta_M) * (1 - beta) > alpha + eta_D * (1 - alpha).
```

At equality they touch; otherwise they overlap. When `eta_M=eta_D=0`, the condition reduces to the earlier `alpha+beta < 1` criterion. If it fails, the bounds alone cannot guarantee discrimination from Y alone: an overlapping Bernoulli probability has constructions compatible with both hypotheses. This is not a proof that additional measurements of G, neural variables or other outcomes cannot distinguish them; the constructed joint distributions need not agree on those measurements.

## 3. Illustrations, not neuroscience data

**Separated example.** Let `alpha=beta=0.10` and `eta_M=eta_D=0.12`. Then

```
M: q_M >= 0.792
D: q_D <= 0.208
separation = 0.584.
```

For instance, a union bound would give `eta <= .12` from three separately justified trial-wise failure-rate bounds `.05`, `.05`, `.02`; no independence is needed for that union bound. But the individual bounds, their exact scope, and their validity under each hypothesis would all have to be established. This is not a claim that any existing experiment achieved them.

**Overlap example.** Retain `alpha=beta=.10`, but allow `eta_M=eta_D=.50`. Then M permits `[.45,1]` and D permits `[0,.55]`; `q=.50` is compatible with both. The verifier constructs explicit joint laws for `(G,Y)` in both cases. They agree on the marginal law of Y and have opposite experiential predictions on valid trials, but have different G–Y associations. If G were fully observed, the joint data could discriminate them; it is the stipulated Y-only comparison that is nonidentifying. Additional samples of Y alone cannot resolve this overlap.

## 4. Finite samples: a sensitivity calculation, not a recruitment recommendation

If `L>U` are **known pre-established bounds**, and the `n` Y observations are independent Bernoulli variables (or independent bounded variables with the relevant uniform mean bounds), use threshold `t=(L+U)/2`: choose M if the sample mean is at least t; otherwise choose D. With `Delta=L-U`, Hoeffding gives each worst-case error at most

```
exp(-n * Delta**2 / 2).
```

In the illustrative separated example, `Delta=.584` and `n=22` gives a bound of about `.02348` for **each** error. This is merely the smallest n meeting the selected conservative Hoeffding upper bound of `.025` each, not the actual minimum n for an optimal test, a clinical power calculation, or evidence that 22 participants suffice. Repeated trials from the same person can be dependent; substituting trial count for independent subjects is unjustified. An IID Bernoulli model, representative recruitment and the target's empirical accessibility are strong additional assumptions.

If the calibration and gate bounds are estimated rather than known, reserve separate confidence/error budgets for **all** of them, use simultaneous coverage, and ensure the test data are independent of the data selecting/estimating bounds (or use an otherwise valid joint inference). A simple conservative guarantee adds the probability that any assumed bound fails to the conditional classification error. Confidence that a population bound is correct is different from the population fraction eta; neither can be substituted for the other.

For honest model checking, report the measured uncertainty interval for q against both predicted intervals. If it excludes both, the result challenges the premises, calibration or both rivals; a forced binary decision would hide that possibility. The calculation does not adjudicate a non-exhaustive pair of hypotheses when their shared contract fails.

## 5. What must happen next

1. **Fix a specific target**: for example a prespecified perceptual content contrast and its preservation, not a general binary label for consciousness or subject number.
2. **Freeze physical prerequisites**: characterize the maintenance basis and relevant counterfactual powers; predefine the exact consumer scope and the absence of equivalent distribution. Existing [coverage and complete-boundary analyses](CONSUMER_COVERAGE_IDENTIFIABILITY.md) show why absent monitored effects do not bound all hidden consumers.
3. **Bound the validity rate** using validated physical measurements and an explicit representativeness/transport argument; where G itself is partly counterfactual or cannot be bounded, report the gap as unknown rather than inventing eta.
4. **Independently warrant the phenomenal assay under the separating intervention and G-valid condition**. Agreement with a report or no-report proxy is not automatically an error rate against the felt target. No such credible alpha/beta and eta bounds are supplied here.
5. **Pre-register the competing local hypotheses and the full uncertainty accounting.** If the above separation is not obtained, report the experiment as non-identifying under these bounds rather than as evidence that either ontology wins.

A future valid local test could constrain a consciousness-selection rule. It would not alone establish why a specific qualitative character occurs, whether there is one universal subject, the actual truth of plenitude, or a metaphysical framework's unique empirical likelihood.

## 6. Reproduction

Run `python verification/robust_disclosure_separation.py`. The accompanying [results](verification/robust_disclosure_separation.json) check 625 rational parameter combinations and 19,800 feasible grid witnesses, construct matching-Y overlap witnesses, and calculate the sample-bound illustration. The exact interval proof establishes the general algebra; finite enumeration is a debugging control, not a substitute for that proof or for empirical validation. `python -m py_compile verification/robust_disclosure_separation.py` checks syntax.
