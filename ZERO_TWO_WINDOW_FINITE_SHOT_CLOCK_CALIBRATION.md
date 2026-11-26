# Finite-shot calibration for a restricted clock-record family

**Continuation:** [coherence and calibration test](ZERO_TWO_WINDOW_COHERENCE_AND_CALIBRATION_TEST.md) shows that the full existing record is informationally complete on the two-packet span in the finite model, and quantifies its weak-direction and support assumptions.

## What this answers

The [previous analysis](ZERO_TWO_WINDOW_RECORDED_HISTORY_AND_FINITE_INTERVAL.md) showed that ideal finite-interval slice data have an unstable inverse on the unrestricted continuum space. Here we ask a narrower, operational question: **can finite detector counts predict the same model's later recorded histories for a restricted preparation family?**

For an incoherent mixture of two specified packets in the existing two-window model, a single early yes/no statistic estimates the mixture weight. With independent endpoint calibration batches, a simple finite-sample bound controls the predicted **complete recorded-history distribution**, not just the early click rate. The bound includes statistical calibration error. It does not include unknown model, continuum-discretization or preparation error unless an independent bound for those errors is supplied.

A matched counterexample demonstrates the cost of the restriction: two coherent packet superpositions outside the mixture family have exactly the same early click probability but different later record distributions. Thus infinitely many early-click samples cannot validate the mixture assumption. The construction is an operational **prediction test**, not yet a demonstration that geometry is a self-contained time coordinate or an autonomously triggered clock.

Code and reproducible simulated data: [verification/zero_two_window_operational_clock_calibration_test.py](verification/zero_two_window_operational_clock_calibration_test.py). All numerical results below use the same N=40 finite regulator unless noted; no experimental data are claimed.

## 1. Preparations, measurement and noise

The constraint, D and M₁/M₂ apparatus, scalar checkpoints and E₀ Lüders instrument are those of the [three-attempt protocol](ZERO_TWO_WINDOW_RECORDED_HISTORY_AND_FINITE_INTERVAL.md). Its true click history is measured at φ=30, 40, 50; the two original memories are read at φ=100. All eight click strings and four memory pairs are retained. Clicks are responses of a finite-width instrument, not exact crossing counts.

Choose the same internal initialization and h superposition in two packets:

* `ρ₁`: the incident packet centered near α=−15;
* `ρ₀`: the receding packet centered near α=+15.

Within each chosen packet, the original internal coherences are retained. The **restriction** is that each unknown preparation belongs to the incoherent family

```text
ρ_w = (1−w)ρ₀ + wρ₁,        0 ≤ w ≤ 1,
```

with the same unknown w for all copies in a batch. This assumes a repeatable source and excludes coherent superpositions between the two packet preparations. The setup does not derive this family from zero or prove it describes a real clock.

For a concrete error control, the first click bit is misreported *after the physical instrument acts*: false-positive probability `f=0.03` and false-negative probability `g=0.05`, independently on each copy. The other two bits and the final M₁/M₂ readout are assumed perfect in this particular example. The physical postmeasurement state depends on the true instrument outcome, not on the later classical reporting error. The observed history distribution Pᵢ, with the noisy first bit, includes all 32 reported outcomes; its first-bit marginal is

```text
q_i = f + (1−f−g) p_i,       i=0,1,
```

where pᵢ is the physical φ=30 yes probability. For N=40:

```text
p₀=0.00041443, p₁=0.35065194;
q₀=0.03038128, q₁=0.35259978;
D = TV(P₁,P₀)=0.75683904.
```

The endpoint calibration below measures q₀ and q₁ directly, so knowing f and g is not required for the statistical inversion. The quoted numerical table D and simulated outcomes, however, assume the stated noise and model. If the observed endpoint gap is zero, inference is aborted rather than divided by zero. If it is small, the confidence radius becomes uninformative.

## 2. Calibration and an explicit confidence bound

Use three separate sets of independently prepared copies: `m₀` known ρ₀ copies, `m₁` known ρ₁ copies, and m copies of unknown ρ_w. Perform the same first readout at φ=30 on each and record observed yes fractions `â`, `b̂` and `ŷ`. Let `Δ̂=b̂−â` and define

```text
ŵ = clip_[0,1]((ŷ−â)/Δ̂),
e(n) = sqrt(log(6/α)/(2n)),
r = min[1, (e(m)+max(e(m₀),e(m₁)))/|Δ̂|].
```

When `Δ̂=0`, report no estimate and use the trivial radius 1. Hoeffding's inequality and a union bound give, **for fixed w and stable independent Bernoulli trials**, probability at least `1−α` that all three empirical fractions are within their respective e(n) of their true probabilities. On that event, since `q_w=(1−w)q₀+wq₁`,

```text
|ŵ−w| ≤ r.
```

Clipping cannot increase distance from a true `w∈[0,1]`. The denominator is the **observed** calibration gap, and the bound remains valid even if its sign is unexpected. A small observed gap simply makes r trivial. The confidence statement is a repeated-sampling guarantee; it is not a posterior probability for w.

If the full reported endpoint history distributions P₀,P₁ are independently known for this same protocol, linearity gives

```text
P_w=(1−w)P₀+wP₁,
TV(P_w, P_ŵ) = |w−ŵ| TV(P₁,P₀) ≤ r D.
```

Thus, simultaneously for **every event** formed from the 32 recorded outcomes, its predicted probability differs from the true one by at most `rD`, on the same confidence event. This includes any first-click, no-click, repeated-click or final-memory event. It does not claim any individual run or any actual crossing is identified with that accuracy. P₀ and P₁ here are predicted by the finite model, not established by the first-bit calibration.

If instead only modeled endpoint tables `P̃₀,P̃₁` are available, with independently justified total-variation errors `TV(Pᵢ,P̃ᵢ)≤ηᵢ`, the same event gives

```text
TV(P_w, (1−ŵ)P̃₀+ŵP̃₁)
 ≤ (1−w)η₀+wη₁ + r TV(P̃₁,P̃₀)
 ≤ max(η₀,η₁) + r TV(P̃₁,P̃₀).
```

Without such η bounds, the numerical confidence radius is **conditional on the endpoint model**. A grid comparison is not a rigorous η bound. Independently measuring full endpoint tables is another option, but its sampling error, detector calibration and drift must then be included; calibrating only the early bit cannot certify the full tables.

## 3. A finite-shot example and resource trade-off

Set `w=0.37`, use 10,000 independent copies in **each** of the three batches, and simulate with seed 72849. The counts of reported first clicks are

```text
ρ₀ calibration: 309/10000
ρ₁ calibration: 3561/10000
unknown batch:  1504/10000
ŵ=0.367466,    r=0.095152  (α=0.05).
```

Given the exact modeled endpoint distributions, `rD=0.072015` bounds all recorded-history event errors with at least 95% sampling coverage under the assumptions above. In this one simulation the actual total-variation error is 0.001918; this favorable realization is **not** the 95% guarantee. For example, the predicted reported `000` probability is 0.806673, versus the simulated-model truth 0.805554. This is model-based prediction of an ensemble probability, not an observation of a particular trajectory.

Using the *expected* noisy calibration gap about 0.3222 only for planning, equal-sized batches of n=1,000, 10,000 and 100,000 yield approximate rD bounds 0.230, 0.073 and 0.023, respectively. Each requires **3n independent preparations** before any separate validation runs. Actual bounds must use the observed gap, and these estimates exclude apparatus energy, time, preparation cost and systematic errors. False reports reduce the gap; if `f+g=1`, the first reported bit contains no information about w in this independent-error model.

The repeated measurement is a real intervention. At N=40 for the incident preparation, `Pr(M₁=1)` changes from 0.432637 without the extra attempts to 0.426804 with all three; neither is a substitute for the other. The first-click calibration and full-history test must use matched first interventions. Inferring an unmeasured original evolution from a disturbed one would be a different question.

To check a specific predicted history event in an **independent** validation sample of N full-protocol copies, the observed frequency has a Hoeffding radius `sqrt(log(2/β)/(2N))` at confidence `1−β`. Combining it with the calibration guarantee by a union bound gives coverage at least `1−α−β` for the discrepancy bound. For all 32 individual outcome frequencies simultaneously, replace `log(2/β)` by `log(64/β)`; the full-protocol observations must include the same readout noise and interventions. Such checks can falsify assumptions but finite agreement cannot establish that the family is exhaustive.

## 4. Matched coherent counterexample

The restriction to incoherent mixtures is essential. Using the span of the same incident and receding initial states, orthonormalize it and construct two normalized coherent states with equal first-bit expectation, chosen to maximize their difference for the ideal `000` effect subject to that equality. Both have the same early physical click probability `(p₀+p₁)/2=0.17553318` and the same noisy reported first-click probability 0.19149053. Yet their full reported histories differ:

```text
                          state A       state B
reported 000              0.744181      0.752096
final M₁=1                0.221422      0.206396
TV(all 32 reported rows)  0.025180 between A and B
```

Consequently no number of copies measured **only** by this first yes/no test can distinguish these states or justify the mixture-family prediction. The two states are outside the stipulated incoherent line; the example does not refute the finite-shot bound when its premises hold. Their construction uses the ideal model's full operators and is not a claim that an experiment has prepared them.

## 5. What is established and what remains

* The error bound follows analytically from the assumed convex family, Bernoulli concentration and total-variation linearity. The numerical code tests its algebra, a reproducible finite-shot realization, the coherent counterexample, detector-noise bookkeeping and grid refinement; it does not prove the continuum model or detector assumptions.
* N=40 versus N=80 changes the largest entry of each endpoint's 32-outcome table by less than 0.0002 in the tests. This is not a rigorous continuum error estimate, and neither bound/scattering decomposition nor inaccessible physical sectors may be silently discarded.
* Calibration presumes reproducible endpoint states, independent shots, a stable apparatus, the same intervention across batches, and separately justified complete endpoint history distributions. Additional preparations and validations can reveal failures but incur more measurements and backaction.
* The protocol uses an ideal scalar clock to schedule interventions, and finite-resolution yes/no geometry measurements. It estimates an ensemble mixture and predicts records; it has not constructed a physically autonomous geometry clock, a general time observable, a multiple-crossing counter, or a theory of inhomogeneous gravity. Nor does it derive the clock, laws, actual subjects or experience from a self-sufficient point–sphere whole.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_operational_clock_calibration_test -v
```
