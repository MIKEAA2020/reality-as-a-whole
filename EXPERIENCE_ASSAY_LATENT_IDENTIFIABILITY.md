# Can multiple imperfect measures identify an experience?

## Result

**Sometimes, under explicit assumptions—but agreement among measures does not by itself establish those assumptions or identify a phenomenal state.**

For a particular balanced binary latent-class model, three conditionally independent, better-than-chance probes determine their individual accuracies from pairwise correlations, without a perfect reference test. This is a useful positive result, not a discovery of a new statistical method. However, we also construct two different experience-assignment models with **exactly the same joint distribution of every physical variable in the toy model**, including under three specified changes of condition. One model satisfies conditional independence given the proposed experience; the other does not. They assign different error rates and predict different experiences.

This is a finite *identifiability* result. It does not show that no consciousness experiment can succeed, that reports are invalid, that the two toy assignments are equally plausible accounts of real minds, or that experience is inaccessible to the experiencing subject. The toy variables and values are hypothetical, not neuroscience observations.

## Prior art and connection to our work

[Dawid and Skene (1979)](https://doi.org/10.2307/2346806) developed latent-class estimation of observer error without access to the true category; [Hui and Walter (1980)](https://doi.org/10.2307/2530508) studied diagnostic error estimation without a gold standard under a different multipopulation design. The role and limitations of conditional independence are discussed in [the diagnostic-test identifiability analysis](https://www.math.unm.edu/~fletcher/backup/IdDiagTest_6.pdf). Consciousness-science concerns about report and no-report confounds are discussed in [the exclusionary approach](https://academic.oup.com/nc/article/2023/1/niad022/7291873).

The narrow contribution here is to **apply an exact latent-class reconstruction and an explicit competing causal story to the subject-to-report dependency** left by our [two-report circuit](TWO_REPORTS_CONSENSUS_AND_REVERSAL.md). This also supplies a concrete warning for the error parameters required by [our robust experiential contrast](ROBUST_EXPERIENTIAL_CONTRAST.md): proxy agreement cannot automatically be treated as an independently established phenomenal-assay error rate. There is no claim of literature-wide novelty.

## 1. Two measures are not enough in this model

Let a binary target `Z` and two binary reports `X1,X2` take values `−1,+1`. Suppose, for this section, `Z` is balanced and both measures are conditionally independent given `Z`, with symmetric, better-than-chance error rates. Define

```
βi = 2 P(Xi=Z) − 1.
```

Under these premises, `E[X1 X2]=β1β2`. Thus even an exactly known joint distribution only fixes the **product** of the two accuracies, not each accuracy.

The following two models produce the same report probabilities `P(++ )=P(--)=5/16` and `P(+-)=P(-+)=3/16`:

| Model | Accuracy of X1 | Accuracy of X2 | Report agreement |
|---|---:|---:|---:|
| A | 75% | 75% | 62.5% |
| B | 100% | 62.5% | 62.5% |

Both satisfy the stated conditional-independence and symmetric-error assumptions; B is the boundary case of a perfect X1. Thus this ambiguity is not merely caused by common-source error. These probabilities are exact, not sampling uncertainty.

## 2. Three measures: identification within a restricted model

Add `X3`, and suppose:

1. `Z` is balanced, and each `Xi` is a ±1-valued indicator of the **same fixed target**.
2. Conditional on `Z`, the three indicators are mutually independent.
3. Each has symmetric error and positive bias `βi>0`; these biases are fixed within the tested condition.
4. All relevant pairwise correlations are nonzero. Probabilities are population values; finite estimates have uncertainty.

Then `cij=E[Xi Xj]=βiβj`, so

```
β1 = √(c12 c13 / c23),
β2 = √(c12 c23 / c13),
β3 = √(c13 c23 / c12).
```

For example, `c12=3/10`, `c13=2/5`, `c23=12/25` give `β=(1/2,3/5,4/5)`, hence inferred accuracies `(75%,80%,90%)`. This identification is **within the stipulated model**, not an unconditional guarantee. When correlations approach zero, the formulas become unstable or undefined. Observable distributions may reject some model restrictions, but good fit to them does not prove that the postulated latent variable is the phenomenal target or that conditional independence holds for that target.

The positive-bias convention also orients the latent labels. Without such an orientation, swapping `Z=+1` and `Z=−1` produces a label symmetry; the observed indicators alone do not tell us what a label feels like. More indicators or different populations can add identifying information, but they do not remove the need to justify the model assumptions appropriate to the data.

## 3. Exact countermodel: same physical data, different experience assignment

Let `H,N,X1,X2,X3` be the physical variables in a toy process. `H` and `N` are independent binary variables. In the balanced condition set `P(H=+1)=1/2`, `P(N=+1)=4/5`. Conditional on `H`, the three indicators are independent, with biases `(1/2,3/5,4/5)` relative to `H`. The variable `N` does not affect those channels. All of `H,N,X1,X2,X3` have **exactly the same joint physical law** in the two models:

- **Model A:** call `Z=H` the target experience.
- **Model B:** call `Z=H·N` the target experience.

These are explicit alternative *candidate psychophysical assignments*, not a demonstration that a real experience is generated by a product of two bits. In both models `Z` is a stipulated label; the same physical behavior is generated without using `Z` as an extra causal input. An independently motivated identity or causal law for experience could rule out one of these assignments. The countermodel only establishes that the listed physical distributions alone do not select one.

| Quantity in the balanced condition | Model A | Model B |
|---|---:|---:|
| Actual `P(X1=Z)` | 75% | 65% |
| Actual `P(X2=Z)` | 80% | 68% |
| Actual `P(X3=Z)` | 90% | 74% |
| `P(Z=+1 | X1=X2=X3=+1)` | `108/109 ≈ 99.08%` | `433/545 ≈ 79.45%` |

The displayed posterior conditions only on the three `X` values, not on `H,N`; the **full** `H,N,X1,X2,X3` distributions are also identical between the models. The reconstructed 75%, 80%, 90% accuracies are correct for `Z=H`, but incorrect for `Z=H·N`. In model B, probes remain independent given `H`, yet they are **not independent given `Z`**. For example,

```
Cov(X1,X2 | Z=+1) = 24/125.
```

That makes the failed assumption explicit, rather than merely saying that correlation is not causation. The shared physical source can create convincing indicators of `H` while leaving open whether the experience of interest is `H` or a different function of the physical variables.

### A restricted intervention comparison

Now consider three prespecified settings that change only the distribution of `H`, with `E[H]=−1/2, 0, +1/2`; keep the `N` distribution and all three response channels fixed. In each setting the complete physical distribution of `H,N,X1,X2,X3` remains identical across A and B. For `E[H]=+1/2`, however, A predicts `P(Z=+1)=3/4`, while B predicts `13/20`.

This is **not** a statement about arbitrary interventions. In particular, an intervention that is independently known to target the relevant experience-assignment mechanism, a validated first-person measure, or additional psychophysical premises may separate these models. The example only checks the three defined changes in `H`; it does not simulate a brain experiment or a physically feasible intervention on experience itself.

## 4. First-person data are not discarded

A subject's own experience is valid data for that subject. If `Z` in this example really denotes that subject's experienced contrast and an independent, reliable first-person observation of `Z` is available, the two models make different predictions and can be compared against it. Their equivalence applies to **the listed physical variables**, not to an enriched data set that includes the actual experiential values.

The methodological difficulty is that an external investigator commonly receives a *physical report* of the experience; that report is itself a potentially imperfect channel. Calling one of the `Xi` “the report” does not automatically make its agreement with a latent estimate an independently verified accuracy against `Z`. Nor does this imply that reports should be ignored or routinely disbelieved: well-designed reports supply valuable, often indispensable evidence, and can anchor no-report methods. The point is to state **which experiential observation is used as an anchor, whose data it is, what is directly available, and what extra reliability or transport premises are needed**.

The numerical labels do not capture phenomenal quality, establish the existence of a subject, or decide how many subjects there are. A successful statistical fit to an access/behavior target must not silently become proof of phenomenal constitution.

## 5. A concrete route beyond the ambiguity

A candidate subject/experience test should preregister:

1. **Target and anchor:** one specific experienced content or contrast, its population and time window, and what genuinely first-person evidence is available. Separate that datum from its physical communication to others.
2. **Indicators and common causes:** the physical pathways of the report, behavioral and neural measures, including common input, attention, memory and reporting demands. Mechanistic independence is a hypothesis, not a consequence of different instruments or locations.
3. **Competing psychophysical assignments:** specify at least one live model in which indicators share a non-phenomenal driver, and the intervention conditions under which it predicts differently. Do not discard it solely because it is inconvenient for the latent fit.
4. **Calibration and transport:** use independently justified partial error bounds, intervention-specific calibration and held-out conditions; if these bounds cannot be warranted, carry ranges into the [robust contrast](ROBUST_EXPERIENTIAL_CONTRAST.md) rather than reporting a point accuracy as fact. Neither a known stimulus nor successful task performance is automatically the felt percept.
5. **Subject identity and reports over time:** specify whose episode each indicator concerns, whether the target is preserved across report/no-report contexts and interventions, and what can actually be retained after a proposed reversal.

The desired outcome is not an abstract impossibility claim but a testable narrowing of rivals, respecting both first-person evidence and physical constraints. This gate does not solve consciousness, select the intrinsic quality of discomfort, prove subject plurality or unity, or resolve the user's wider metaphysics.

## Verification

Run [`verification/latent_experience_three_probes.py`](verification/latent_experience_three_probes.py). Its [exact-arithmetic receipt](verification/latent_experience_three_probes.json) checks the two-reporter ambiguity, three-probe reconstruction, the two competing assignments, their common physical distribution in three specified settings, conditional dependence and differing posteriors. The construction is a toy statistical counterexample, not evidence that either assignment is true of actual conscious organisms.
