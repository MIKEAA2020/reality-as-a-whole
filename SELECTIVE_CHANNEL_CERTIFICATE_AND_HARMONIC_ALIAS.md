# Can selective interventions identify relational frustration?

## Result and scope

The later [four-spin imperfect-intervention gate](FOUR_SPIN_IMPERFECT_SELECTIVE_INTERVENTION_GATE.md) develops a related, discrete-spin sign certificate using conditional odds and a bounded change in residual coupling. It does not establish that any real intervention is selective.

This is the next step from [the hidden-channel gate](FRUSTRATION_CYCLE_IDENTIFIABILITY_GATE.md). It addresses a specific problem: equal opposing phase channels can cancel in the net dynamics, leaving their channel-level frustration unidentified by phase-only observations and phase-setting interventions.

A **selective channel intervention**, if independently calibrated and sufficiently well isolated, can break that ambiguity. Under a specified reciprocal first-harmonic phase model, two phase settings per channel produce conditional bounds on its preferred offset and coupling strength; those bounds feed directly into the earlier cycle-frustration certificate. Surprisingly, the gate need not remove a known fraction of the channel: an unknown, phase-independent fraction between zero and one still yields a valid lower bound on the original strength.

But two settings **cannot validate the assumed first-harmonic law**. An explicit third-harmonic counterexample reproduces all of those ideal measurements, while changing the triangle's true minimum frustration from `3/2` to `0`. Both the possible advance and its model-dependence are demonstrated below. The work is a measurement-identifiability construction in a finite classical toy model, not a human study, discovery of a neural pain circuit, proof of experience, or solution of quantum physics.

## 1. What is already known, and what is added here

Inferring phase coupling from observed oscillations is an established field: [Kralemann and colleagues](https://ar5iv.labs.arxiv.org/html/1102.3064) describe phase-dynamics reconstruction and limits from restricted phase coverage, and [a 2025 study](https://journals.plos.org/complexsystems/article?id=10.1371%2Fjournal.pcsy.0000063) investigates inference under particular oscillator assumptions. The [causal-connectivity literature](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011574) explicitly discusses the confounding produced when a perturbation affects multiple neurons. The conditional calculation below is our application of familiar quadrature estimation and [Hoeffding bounds](https://arxiv.org/html/2010.09686v2) to the preceding frustration and subject-interface problem; it is not a claim to have invented those methods.

## 2. Assumptions: what the intervention must mean

Consider an oriented physical interaction channel `e=(i,j)` in a finite system. In an explicitly chosen local phase reference, let `x=φ_i−φ_j` and let the *original, ungated* channel have cost and signed derivative

```text
E_e(x) = k_e [1 − cos(x − a_e)],      q_e(x) = ∂E_e/∂x = k_e sin(x − a_e),
k_e ≥ 0.
```

A hypothetical on/off intervention, with all relevant phases clamped, changes the measured signed generalized force or appropriately signed clamp-reaction force by

```text
Δ_e(x) = λ_e k_e sin(x − a_e) + b_e(x),               (A)
```

where `0 < λ_e ≤ λ_max` is **the same scalar at both sampled phases**, with `λ_max≤1` if the intervention is known only to attenuate rather than amplify the channel. It may be unknown and different for different edges. The original system corresponds to the on-state. The residual `b_e` absorbs intervention cross-talk, changes in other channels, hidden-state response, mismatch of the clamp, calibration bias and model error **only insofar as an independently justified bound on those terms is valid**. A physically plausible apparatus must supply a consistent phase convention and force calibration, verify that the same underlying on-state channel is being changed, and make this contrast meaningful. Differences in unrelated unknown forces must not be silently called zero.

The gate is *channel-selective*, not merely a phase reset, and it must distinguish the physical channel from parallel channels. No available human experiment has been shown here to meet these conditions; nonselective stimulation need not. The cost is a separately specified phase-model mismatch cost; its existence and baselines are physical assumptions. A local change of phase coordinates requires transporting both target phase settings and the reference for the recovered offset: mere coordinate relabeling cannot change cycle incompatibility.

## 3. Two quadratures and their uncertainty

Suppose the gate contrast is observed at `x=0` and `x=π/2`. With no error,

```text
y_0 = −λ k sin(a),             y_1 = λ k cos(a).
```

Consequently, for nonzero response, the direction of `(y_1, −y_0)` identifies `a mod 2π`, and its length is `λk`. If `λ≤λ_max`, then `k≥hypot(y_0,y_1)/λ_max`. Exact k is not identified without a known λ; phase is not identified at zero strength.

Now let each measured contrast `ŷ_0, ŷ_1` differ from its ideal value by at most `ε`, including all sampling and **independently established** systematic errors. Define

```text
ρ = sqrt(2) ε,    R = hypot(ŷ_0, ŷ_1).
```

When `R>ρ`, the true response vector lies inside a radius-ρ disk centered at the estimated vector, not containing the origin. Elementary tangent geometry and the reverse triangle inequality give

```text
k ≥ (R−ρ)/λ_max,
â = atan2(−ŷ_0, ŷ_1),       dist_circle(a, â) ≤ asin(ρ/R).       (B)
```

This treats rectangular component bounds as a conservative enclosing disk. If `R≤ρ`, the disk contains zero and a nontrivial offset bound is not warranted; mark the edge **unresolved**, rather than choosing an angle. `λ>0`, its phase-independent value over the two settings, and valid error bounds are essential. A phase-dependent or sign-changing gate, changing channel preference, cross-talk or higher-harmonic force can invalidate (B), unless separately included in a valid bias bound.

## 4. Conditional three-channel certificate

For a prespecified oriented triangle, apply (B) to each independently identified channel. Write each lower weight as `k_low,e` and each angle radius as `δ_e`. With

```text
k_low = min_e k_low,e,
d_low = max(0, dist_circle(Σ_e â_e, 0) − Σ_e δ_e),
```

our preceding [cycle bound](FRUSTRATION_CYCLE_IDENTIFIABILITY_GATE.md) gives

```text
F_all ≥ (2 k_low / (3π²)) d_low².                     (C)
```

This is a lower bound for the **on-state** channel model, including arbitrary additional nonnegative mismatch costs, provided the three channels and their costs remain included and unchanged. No complete hidden graph is required, but possible environmental changes of the channels themselves are not covered. The bound is on absolute additive F—not normalized F, current excess D, physiological energy dissipation, a subject or unpleasantness.

### Explicit hypothetical receipt

Let all three measured contrasts be `(ŷ_0,ŷ_1)=(0,−1)`, let each contrast's error be bounded by `ε=0.1`, and let `λ_max=1`. Then each edge has

```text
k ≥ 0.8585786,  |a−π|_circle ≤ 0.1418971 radians.
d_low = π − 3×0.1418971 ≈ 2.7159015,
F_all ≥ 0.4277767.
```

These values are illustrative hypothetical readings, **not observations**. Under the assumptions the certificate is valid even if `λ` is unknown—for example, an exactly 80%-gated channel would have a larger true k than its gated-response magnitude. If λ could exceed one, use a genuinely justified larger `λ_max`; if no finite bound exists, the strength lower bound can vanish.

## 5. Illustrative finite-sample budget—not a validated experiment

There are 12 cells: three channels × two settings × on/off. Fix `n` independent trials per cell with each recorded value bounded in `[-B,B]` and a stable cell mean. For each difference of on/off sample means, allocate sampling error `η`: it suffices for both contributing means to be within `η/2`. By Hoeffding and the union bound, all 12 means meet that condition with probability at least

```text
1 − 24 exp[−n η²/(8B²)].
```

No independence *between* cells is required for the union bound; the concentration assumption is independent observations within each cell and stable means. If a separately justified deterministic bound `β` covers the systematic error of **each difference**, set `ε=η+β`. The same simultaneous event supports all six contrasts and hence the joint certificate. If β is itself uncertain, its joint coverage must also be accounted for; it is not supplied by repeated sampling.

For `B=2`, `η=0.05`, `β=0.05`, and failure probability `α=0.05`, the sufficient bound is

```text
n = ceil[(8B²/η²) ln(24/α)] = 79,025 per cell,
12n = 948,300 trials total;
sampling failure bound ≈ 0.0499979.
```

This is a deliberately conservative, hypothetical distribution-free calculation, not an optimal sample size, experimental recommendation, or guarantee for correlated/reused biological trials. It assumes a meaningful bounded-force scale, stable interventions, independent trials, and independently validated systematic error. A more efficient design could use legitimate variance, pairing, sequential or hierarchical methods, but must establish its own error control. If the admissible model or β cannot be bounded, more trials alone do not yield the certificate. Data-dependent channel selection would require separate multiplicity control or independent discovery data.

## 6. Exact failure test: a different potential fits both quadratures

The two-point identification depends critically on the assumed interaction form. Compare these two genuine nonnegative phase costs, with signed derivatives:

```text
first-harmonic antiphase: E₁(x)=1+cos x,          q₁(x)=−sin x;
third-harmonic:           E₃(x)=(1−cos 3x)/3,    q₃(x)= sin 3x.
```

Both give `q(0)=0` and `q(π/2)=−1`. Thus, with the same hypothetical selective gates, the entire two-quadrature receipt is identical in the two models. Yet for a triangle:

- Three `E₁` channels have minimum `F=3/2`, as shown in the earlier audit.
- Three `E₃` channels have minimum `F=0`: set all node phases equal; each nonnegative `E₃` term vanishes.

At the independent phase `x=π/4`, however, `q₁=−√2/2` and `q₃=+√2/2`, a separation of `√2` in these model units. A genuinely channel-specific probe at that held-out phase, with adequate error control, would discriminate **these two particular rivals**. It would not by itself validate a sinusoid against every possible interaction. Even an arbitrary finite set of tested phases leaves untested functional possibilities unless a restricted interaction family and a bound on model misspecification are separately justified. In particular, agreement with two samples is not independent validation of the first-harmonic law.

This counterexample shows why the apparently positive number `0.4277767` is **conditional**: applying it to third-harmonic data without the first-harmonic assumption would certify a false positive despite perfect measurements at the two chosen phases. It does not show that the user's experiential idea is false; it identifies a concrete way a proposed physical test could mislead us.

## 7. What would count as a real advance toward experience?

Before relating any F to discomfort, a viable empirical programme would need:

1. An independently grounded local system and participant/episode; no global or universal subject is assumed.
2. Physical evidence for identifiable channels and an ethically permissible, calibrated selective intervention—or a different validated identification method. Characterize phase-setting errors, cross-talk, hidden-state reactions, stable units and the model's validity; reject the analysis as unidentified if the bounds cannot be obtained.
3. Prespecified **held-out phase settings** and competing harmonic, non-potential and common-input models. Account for the possibility that an effective phase model misses amplitude or delayed dynamics. Check reciprocal forces and channel baselines rather than inferring a potential from one measured response.
4. A separately collected experiential target and held-out comparison of F, D and conventional stimulus, context, expectation and sensory-intensity predictors. A physical certificate is not itself an assay of an experiencing subject; passing it is neither necessary nor sufficient for a person to be uncomfortable.

No new human data are analyzed here and no pain-inducing intervention is recommended. Any future experiment requires ethical approval, voluntary participation, safety limits and free withdrawal. Empirical prediction could constrain candidates but would not itself prove the metaphysical identity or why experiential ground is self-existent. Nor does local laboratory time imply an external clock for a timeless whole.

## Reproduction

Run `python verification/selective_phase_channel_certificate.py`. The [JSON receipt](verification/selective_phase_channel_certificate.json) records the deterministic calculation, the sample-budget inequality, 15,000 seeded quadrature cases, 10,000 seeded triangle checks and the exact harmonic-alias example. Sampling checks exercise the implementation, not the universal proof, the physical assumptions or the validity of the model in brains.
