# Afterimage hue: when a sign-reversal toy stops being a color prediction

## Finding in brief

The earlier [eye-history model](BINOCULAR_APPEARANCE_VERSUS_EYE_HISTORY_MODEL.md) uses an **abstract one-dimensional signed coordinate**. Its minus sign stipulates an idealized aftereffect; it never specifies real cone excitations, a color space or a 180° hue. Witzel's 2025 results therefore **do not directly falsify that scalar toy**. They do challenge a stronger extension that assumes a fixed, exactly opposite hue is a reliable quantitative prediction across colors and experimental conditions.

A limited check of the author's released aggregate data reproduces the eight reported experiment 1a t statistics to their printed precision and the finding that **six of eight** meet the paper's Bonferroni significance threshold. This is a retrospective calculation on the **same participants and author-produced aggregates**—not independent replication, raw-trial reanalysis or a general law of afterimages. An exact invented cone-coordinate example shows mathematically how nonlinear componentwise contrast can produce a direction different from linear reversal, but does not itself predict perceived color.

## 1. What the evidence says

[Witzel, *The non-opponent nature of colour afterimages* (2025)](https://doi.org/10.1038/s44271-025-00331-5) contrasts a specified cone-adaptation/Weber-contrast model with several specified opponent and color-appearance predictions. In experiment 1a, 31 observers matched static afterimages among nine comparison hues, spanning ±40° around the specified opposite-hue prediction; the task also allowed skips. Six of eight inducer conditions differed significantly from that prediction after correction. Experiment 1b sampled 24 inducer hues in 52 participants.

Experiment 2a used a dynamic chaser-like display, 72 sampled colors and ten participants, including the author. The reported pooled correlations with model predictions were `r = .88` for hue deviations and `.90` for chroma across **colors**, not 72 independent people. Neighboring hues and repeated observations create dependencies that a simple independent-point interpretation can miss. The article's smoothing-based `sR²` is a noise-reduced descriptive fit measure, not an out-of-sample proportion of variance explained. Experiment 2b has two observers; experiment 3 has five including the author. Neither the high correlations nor model comparisons alone uniquely identify the physiological locus.

The paper's results depend on the defined color spaces, standard-observer cone functions, displays, comparisons and tasks. Its real-color matching control is useful, but cannot exclude every response or context effect specific to matching a fading afterimage. Its cone-model adaptation strength was set using comparison chroma for experiment 1 and measured grand-average afterimage chroma for experiment 2; statements of “no free parameters” should not be confused with a prospective prediction independent of all observed afterimage magnitudes. The paper discusses context dependence and uncertainty about physiological implementation. It reports no preregistration. These qualifications do not negate the finding; they constrain its use.

For a distinct empirical route to retinal mechanisms, [Zaidi et al. (2012)](https://doi.org/10.1016/j.cub.2011.12.021) combine time-varying afterimage psychophysics and primate retinal ganglion-cell recordings. Their retinal interpretation is not established merely by Witzel's behavioral model fit, nor does it rule out further visual processing or contextual modulation.

## 2. Recheck of reported experiment 1a statistics

We retrieved the author's [`aggdata.mat` at pinned GitHub commit `8901e132…`](https://github.com/christophWit/The-Non-Opponent-Nature-of-Colour-Afterimages/blob/8901e132b6536a5b1333e7f8ba02bf14925e3a94/aggdata.mat). Its Git blob SHA-1 is `1a10e123ee6a6aad33f18029918d9038b67d6904`, SHA-256 `9d380d2f0e7795f9755fa54e8660d084dde3672dfe583979aab284920202cd45`, and MD5 `76e7398d76b828d6215b6c107510306d`, matching the listed file in the [Zenodo release](https://zenodo.org/records/13328099). GitHub is the actual source retrieved, not a separate dataset. The author's [README](https://github.com/christophWit/The-Non-Opponent-Nature-of-Colour-Afterimages/blob/8901e132b6536a5b1333e7f8ba02bf14925e3a94/README.md) explains that this is prepared data generated from preprocessed raw data by their aggregation script.

The recheck reads the 31 × 8 `AGG1a.afteri.indi` participant-level hue medians and the 8 × 9 × 3 comparison array. The author code identifies comparison slot 5 as the target. We subtract that central comparison's hue on the shortest signed arc, then conduct a two-sided one-sample t test across participants for each inducer. Every column has 31 finite participant medians. Participant medians and the target are taken from the released aggregate; the original trial-to-median computation and DKL transformation were **not independently reconstructed**. Confidence intervals below are ordinary two-sided 95% intervals, **not simultaneous Bonferroni intervals**.

| Inducer | Mean deviation (°) | t(30) | 95% CI (°) | p | p < .00625? |
|---|---:|---:|---:|---:|:---:|
| Red | 11.29 | 5.35 | [6.98, 15.60] | .0000088 | yes |
| Orange | 19.03 | 10.00 | [15.14, 22.92] | < .000001 | yes |
| Yellow | 2.42 | 1.98 | [−0.08, 4.92] | .0574 | no |
| Green | −16.13 | −7.15 | [−20.74, −11.52] | < .000001 | yes |
| Turquoise | 0.97 | 0.63 | [−2.19, 4.12] | .536 | no |
| Blue | −22.26 | −8.52 | [−27.59, −16.92] | < .000001 | yes |
| Purple | 12.10 | 4.69 | [6.83, 17.37] | .0000559 | yes |
| Magenta | 6.29 | 4.00 | [3.08, 9.50] | .000381 | yes |

The eight t values agree with [article table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC12579601/table/Tab1/) to its reported two-decimal precision; the CIs and effect sizes also agree after rounding. Failure to reject for yellow or turquoise is **not** proof of equality. The ±40° response grid restricts these data: four blue-condition participant medians and two green-condition medians lie on an endpoint, among others. This may constrain estimates; medians at an endpoint are not counts of all endpoint trials. A conventional t test assumes the participant-level sampling model, not independence of repeated trials or hues. No new hypothesis test was preregistered.

**Reproduction.** The external MAT file is not committed. Given GitHub CLI authentication, retrieve and verify it, then run with Python, NumPy and SciPy:

```sh
mkdir -p .arena/witzel
gh api -H 'Accept: application/vnd.github.raw+json' repos/christophWit/The-Non-Opponent-Nature-of-Colour-Afterimages/git/blobs/1a10e123ee6a6aad33f18029918d9038b67d6904 > .arena/witzel/aggdata.mat
python verification/witzel_2025_exp1a_aggregate_recheck.py .arena/witzel/aggdata.mat
python -m unittest discover -s verification -p 'witzel_2025_exp1a_aggregate_recheck_test.py'
```

The script verifies both the SHA-256 and Git blob identifier before reading. Full precision, exact p values, software versions, endpoint counts and source hashes are in the [receipt](verification/witzel_2025_exp1a_aggregate_recheck.json). SciPy decodes the necessary numeric fields; MATLAB table objects elsewhere in this file are opaque to this recheck. This is not a rerun of the author's full MATLAB pipeline, and it does not check experiment 2 model fits.

## 3. An exact, invented counterexample to automatic collinearity

Let positive background cone-coordinate vector `b`, inducer `i = b(1 + δ)` componentwise, and `δ_j > −1`. Compare two **defined** normalized vectors:

```text
linear reversal             r_j = (b_j − i_j)/b_j = −δ_j
componentwise Weber vector  w_j = (b_j − i_j)/i_j = −δ_j/(1+δ_j)
w_j − r_j = δ_j²/(1+δ_j).
```

The componentwise difference is second order as `δ → 0`, so `w = −δ + O(||δ||²)` when components stay away from `−1`. For nonzero projected first-order vector the angular disagreement tends to zero for small scaled increments; it need not vanish at finite contrast, and relative-direction claims fail when the projection itself is zero. Componentwise multiplication by unequal denominators need not preserve direction.

Take invented `b=(1,1,1)` and `δ=(1/2,1/4,0)`, so `i=(3/2,5/4,1)`. Define an explicitly arbitrary two-dimensional projection `P(L,M,S)=(L−S,M−S)`. Then:

```text
P(r) = (−1/2, −1/4)
P(w) = (−1/3, −1/5)
det(P(r),P(w)) = 1/60 ≠ 0.
```

The projected arrows are not collinear, so no single scalar gain turns one into the other. This is an algebraic possibility, **not** a calibrated human LMS stimulus, DKL conversion, hue-angle measurement or empirical fit. Real color predictions require the actual background, cone fundamentals, display calibration, luminance constraint, readout and mapping into the chosen perceptual space. Other projections or increments can be collinear. Exact arithmetic and tests are in [`afterimage_cone_contrast_geometry.py`](verification/afterimage_cone_contrast_geometry.py) and its [receipt](verification/afterimage_cone_contrast_geometry.json).

## 4. Consequences for the existing model and a better test

* The earlier `−kh_e` remains a **stipulated scalar response**, not an asserted universal hue law. Its comparison `Δ=4ka` is valid within its own equations. Mapping arbitrary real colors and probes onto that scalar, however, needs independent calibration; it cannot be assumed across hue, chroma, background or viewing context. Witzel's study used different viewing and matching tasks from the dichoptic Anstis–Rogers study, so its quantitative shifts cannot simply be transplanted.
* A future eye-swapping study should calibrate both eye-specific input and observer-level appearance across selected hues and chroma. Prespecify whether it tests only the scalar eye-history interaction or quantitative directional predictions. For the latter, formulate competing models in a common measured output space with individual/display cone calibration, a prespecified readout, and matched gain fitting. Hold out hues, chroma or participants for prediction; account for repeated measures and angular wraparound. Test practical equivalence with explicit bounds where needed; nonsignificance alone is not an equivalence result.
* Test geometry and criteria must be controlled: the [probe-context audit](AFTERIMAGE_PROBE_CONTEXT_AND_IDENTIFICATION_AUDIT.md) shows that an observed shifted response can be compatible with different gain and criterion accounts. Hue-model fit does not remove that identification problem. A direct sensory or neural measure, independently constrained criterion, or additional manipulations could narrow alternatives, but no single option is assumed decisive.
* Eye-indexed processing and hue shifts do not tell us how many experiencing subjects exist. They neither establish private eye-bound experiences nor settle whether or how particular experiences compose into a whole. The required experiential constitution remains open.
