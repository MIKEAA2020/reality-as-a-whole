# Why the clock bound is weak: a causal chain to the model-selection root

## Result and scope

The [preceding instrument](ZERO_GAUGE_CLOCK_JOINT_INSTRUMENT_AND_READOUT.md) gave a generic one-step conditional drift bound of about **0.804** for a correlation of about **0.01414**. Following the chain rather than treating the bound as the problem gives two different answers:

1. In the specified model, shifting the **state** forward one clock step while leaving the sensor memory and readout effects fixed changes this particular correlation by only **0.00002040**. The discrepancy is not an error in the generic bound: the bound controls far more possible effects than this observable.
2. Even a stable measured correlation would not by itself establish the intended source correlation. A stipulated joint-context-dependent sign error can exactly reproduce the same selected output tables from an uncorrelated source while passing average and single-sign error calibrations. Joint-context calibration can expose this rival, but its relevance depends on matched preparations and on a bounded error model.

The deeper question is why the model's admitted source, dynamics, sensors, calibration and rules of interpretation should describe reality. The present construction **supplies** those ingredients; neither gauge invariance nor a zero constraint derives them. This is a concrete explanatory boundary of the present argument, not a proof of ultimate metaphysical bedrock, impossibility of derivation, or an external cause of the whole.

Verification: [calculations](verification/zero_gauge_clock_meta_root.py) and [eight focused tests](verification/zero_gauge_clock_meta_root_test.py). All numbers below are mathematical examples, not experimental measurements.

## 1. Why is the generic bound so much larger than the signal?

The old bound first replaces the chosen observable by a worst-case trace-distance bound over **all** effects, then bounds the selected numerator and denominator separately. It cannot exploit that this instrument's sensor memory is a spectator of the tested shift, that its selection probability is unchanged, or that the only forward-changing part of this particular sign record is the small amplitude crossing the write boundary. Taking a worst-case bound before specifying the observable discards precisely that structure.

Let `f_n` be the sine-window amplitude, `r_n=α` for `n<10` and `r_n=1−β` afterwards, and `p=Σ_n f_n² r_n`. Start from the coherent sensor state in the preceding report. Apply the stipulated bilateral shift `W_∞^k` to the clock and old history, **not** to the sensor memory, and then apply the same late/sign effects as before. The write acts once at the `9→10` crossing, with its inverse on reverse traversal. For integer k,

```text
w_k = (1/p) Σ_(n=0)^(N−1) f_n² r_n 1[n+k ≥ 10],
μ_k = w_k μ_post,
μ_post = λ κ (1−2p_B)(1−2p_C) 2ε/81.
```

The late selection probability stays p because the recorded sensor is carried along unchanged. In particular, the only newly written component for a forward step is the original `n=9` component, whose late probability is α:

```text
μ_1 − μ_0 = μ_post α f_9² / p.
```

For `N=40, α=.05, β=.1, ε=.8, λ=κ=1, p_B=.05, p_C=.1`,

```text
p = 0.81763188,       w_0 = 0.99407413,
μ_post = 0.01422222,  μ_0 = 0.01413794,
μ_1 − μ_0 = 0.00002040019.
```

The reduced **coherent** state is also propagated explicitly, including the old system, reference, qutrit, and clock sensor; at fixed chirality and loop trace it agrees with the formula for shifts `0, 1, 5, 10, −1, −5, −30`. The integrated formula additionally uses the source distribution and sign readout of the prior report. With α=0, forward drift of this statistic vanishes for this history, but the coherent sensor still has nonzero full-state residual and reverse drift remains. For the example, `μ_10=μ_post` whereas `μ_−30=0`: a small one-step change is not a many-step guarantee.

**Why can the state still be disturbed?** The sensor carries an early/late label across the write boundary, so adjacent clock slices have different sensor states. The clock-shift residual measures the resulting full-state mismatch as well as finite-window mismatch, not just this correlation. Other effects can be more sensitive. A small drift of this one statistic neither removes that disturbance nor bounds arbitrary observables.

**Why is this not yet a frame equivalence?** This is an active shift of the state against fixed measurement effects; it is not the simultaneous transport of preparation, instrument, effects and selection. Simultaneous unitary conjugation of both state and effects preserves Born probabilities algebraically, but that tautology alone does not identify two physically realizable clock frames or provide their physical inner product. Showing such an equivalence requires an explicit pair of clock descriptions, their domains, transport of all controls, and operationally comparable effects.

## 2. Why can the correlation be mistaken for a source property?

The previous inference assumes independent, symmetric B and C sign flips with fixed rates. Challenge exactly that assumption without changing the reported outcomes.

Take the `ε=0` source, so after the write the true signs `b,c∈{−1,+1}` are independent and fair. In a specified angular condition let `q=E[t² | condition]`. Assume independent C flips at rate `p_C`, but let B's flip probability depend on the **joint true-sign context**:

```text
P(B flips | b,c) = p_B + a bc,
a = −(1−2p_B) λκ ε q / 18.
```

Use this only when both `p_B±a` lie in `[0,1]`. For the nonzero-ε target with the original independent error channel, its postwrite reported-sign table in that condition is

```text
P(B_obs=b', C_obs=c') = [1 + b'c' μ_target]/4,
μ_target = (1−2p_B)(1−2p_C) λκ ε q / 9.
```

The null-source rival has the **same entire two-sign output table**, since its reported correlation is `−2a(1−2p_C)=μ_target` and both sign marginals are fair. For the angular parameter `u`, `q=(1−u²)/3`; an adversarial rate allowed to depend on the angular condition reproduces this dependence, too. With the same clock selection, w and blank handling, it matches the selected `(B,C)` table including the blank outcome. This is a restricted operational equivalence, not equality of the two source states or of all possible observations. It explicitly violates the independent B-error assumption and is not evidence that a real apparatus has such an error.

The rival also passes calibration of the *average* B flip rate and calibration conditioned on either true sign alone: averaging over the other fair sign gives `p_B` in both cases. But joint-context-resolved rates differ: `p_B+a` for `bc=+1` and `p_B−a` for `bc=−1`. For the unconditional `q=2/9` and the example parameters, `a=−0.00888889`, giving `.04111111` versus `.05888889`. A suitable joint-context calibration can distinguish them; single-channel averages cannot.

**Why can one set of outputs have two explanations?** The output law is a composition of source and readout channel. The same correlation in that composition can originate in the source or in an error depending on the joint context. Observing the composition alone does not uniquely factor it. In a real quantum implementation, calibration needs suitable trusted joint-sign reference preparations and independent access to the relevant context; presuming those are available merely moves the trust boundary. Contexts, clock acceptance and operating conditions must be matched, not just labeled the same.

## 3. A conditional calibration improvement and its remaining dependence

A concrete protocol for this **particular** rival is to prepare independent matched calibration batches of `m` known-written `bc=+1` and `bc=−1` cases, record B's flips, and estimate

```text
a_hat = (k_+/m − k_−/m)/2,
R_cal = sqrt[log(4/δ_cal)/(2m)].
```

For iid Bernoulli trials within each batch, a two-rate Hoeffding union bound gives `|a−a_hat|≤R_cal` with probability at least `1−δ_cal`, provided the context asymmetry is stable and the calibration matches the accepted data. If C flips independently at known `p_C`, and w is known, the additive shift of accepted mean due to this context effect is `−2w(1−2p_C)a`. Combining with the preceding data bound gives a lower margin for the independent-channel source contribution:

```text
margin = X_bar − sqrt[2 log(2/δ_data)/M]
         − 2w(1−2p_C)(|a_hat|+R_cal).
```

If this margin is positive, then the source contribution is positive on the joint confidence event, with failure probability at most `δ_data+δ_cal`. A further inference to the sign of ε requires the stated source family and positive gain. This is **not** a bound on general correlated errors, uncertain w or p_C, incorrect blank handling, other selection biases, drift, reference-preparation errors, or dependence between trials.

Illustration only: keep the earlier simulated `X_bar=.01769`, `M=100000`, and suppose two additional, separately simulated or hypothetical calibration batches each of 100000 trials yield exactly 5000 B flips. Assign `δ_data=δ_cal=.025`. Then `R_cal≈.00503745`, the data radius is `.00936165`, and the margin is only `.00031620`. This narrow positive value is conditional on all assumptions above; the calibration counts are **hypothetical**, not an observation and not a claimed joint simulation. If the counts instead are 4111 and 5889, as near the rival's expected rates, the conservative margin is negative. Calibration preparation, matching and other uncertainties are not included. Plan samples prospectively and report joint uncertainty rather than choosing a favorable outcome retrospectively.

## 4. Keep asking why: from the instrument to the explanatory premises

| Why? | Dependency actually established | Deeper question or needed discriminator |
|---|---|---|
| Why the weak numerical bound? | A full-state, arbitrary-effect bound and loose conditioning inequalities ignore the specific write-boundary structure. | Which observable, shift, conditioning, and instrument are physically compared? |
| Why this tiny forward drift? | The late-tagged amplitude at n=9 is α-weighted, and the fixed sensor selection probability is unchanged. | Why trust that clock dynamics, detector response and retained memory describe an actual device over the relevant shifts? |
| Why infer a correlation in the source? | Only given a source family, readout gain, selection model, iid data and independent errors. | Are rival source–detector factorizations excluded by matched, joint-context references and independent apparatus checks? |
| Why assume this source family? | `ρ_ε=1+ε tχ/3` is an allowed, normalized, invariant family selected to exhibit a correlation; `ε=0` is allowed too. Its separate marginals do not fix ε or the complete joint state. | What physical preparation/dynamics produces it, and what measurements distinguish it from other states and channels? |
| Why these carriers and dynamics? | The three frame spheres, loop link, Haar measure, bilateral clock, qutrit, write gate and sensors are explicitly stipulated mathematical structure. Gauge covariance constrains allowed descriptions; it does not supply a Hamiltonian, local coupling, resources, initial state or retained record. | Derive these as consequences of a justified underlying constitution, or make them independently testable physical hypotheses. |
| Why should such a constitution be necessary or actual? | Internal consistency and invariance establish conditional possibilities and relations within the model, not a unique actual world or its explanatory ground. Zero balance permits multiple structures, including trivial and nontrivial ones; a chosen correlation or carrier does not follow simply from the word zero. | Give a non-circular principle that fixes admissible possibilities, physical realization, equivalence and interpretation, then show how the particular structure follows and how alternatives are discriminated. |
| Why expect that principle to be self-sufficient? | This is a question about constitutive/explanatory dependence, not necessarily an earlier temporal event. The existing argument has not established that its premises explain their own necessity or actuality. | Work through the candidate's own nature and modal commitments; do not assume an outside selector, silently rename a postulate as necessity, or declare the present ignorance an ultimate limit. |

The positive result survives: a particular relational and gauge-invariant construction makes an operationally specified correlation possible, and the observable-specific shift can be computed exactly. The stronger claims—physical clock-frame equivalence, actual autonomous and local sensing, and a uniquely necessary self-differentiating whole—do **not** follow from that possibility. Nor does this calculation derive spacetime, Yang–Mills dynamics, Langlands duality, consciousness, or felt value. For the broader method and its prior application, see [the previous meta-level why-chain](ZERO_META_WHY_CHAIN_SYMMETRY_AND_SELF_SUFFICIENCY.md).

## Continuation: calibration and its causal premises

The [next pass](ZERO_GAUGE_CALIBRATION_CAUSES_AND_TRANSFER_BOUND.md) tests shared-cause and clock-selection alternatives and gives a four-context finite-shot bound with explicit reference, transfer, selection and blank uncertainties. Its guarantees depend on independently justified bounds; calibration alone does not establish source–apparatus transfer.

## 5. Next discriminating work

1. Build a joint-context calibration with physically prepared, verified references and a justified bound on context dependence outside the calibration sample, including state preparation, angular bins, clock selection and correlated noise. Quantify uncertainty in w, gains and C errors jointly; test alternative channels, not only this one.
2. Define two explicit relational-clock descriptions and transport their preparations, devices, effects and conditioning on a common physical state space; account for imperfect frame changes and the full sensor/environment dynamics. The fixed-effect shift above is a diagnostic, not that comparison.
3. Derive or constrain an implementable local loop coupling, switching and finite-resource retained record; compare source predictions with alternatives on observables beyond the selected two-sign table.
4. Continue the constitutive why-chain: specify what would make the claimed zero/whole principle select this carrier, dynamics and actuality rather than merely admit them. Identify which steps can be proved, which require empirical discrimination, and which remain philosophical premises without introducing an external temporal cause.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_gauge_clock_meta_root_test -v
```

These tests verify model calculations and numerical examples, not the validity of their physical premises. The historical source tracker remains conservative and does not establish complete survival or review of the original chat.
