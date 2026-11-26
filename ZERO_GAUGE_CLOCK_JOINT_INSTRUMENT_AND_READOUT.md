# A finite clock and chirality–holonomy joint instrument

## Result

The [previous pass](ZERO_THREE_FRAME_GAUGE_CHIRALITY_AND_NONCYCLIC_CLOCK.md) found a gauge-invariant chirality–holonomy correlation and a noncyclic approximate history, but left their joint readout unspecified. This pass supplies a **finite, explicitly defined global instrument** for that model and computes both its statistics and its disturbance of the clock constraint.

For a specified 40-reading sine-window history, a noisy early/late clock sensor, an unsharp loop sensor and the existing chirality memory:

- the model predicts a measurable correlation between the two recorded signs, with an exact finite-shot confidence bound under stated calibration and independent-copy assumptions;
- the coherent clock readout changes the constraint residual from **0.07661 to 0.17347** in the worked example; conditioning on the late outcome gives **0.14868**;
- a general one-step conditional-drift bound is approximately **0.804**, much larger than the model signal of approximately **0.0141**. Thus the small initial residual alone does not certify the desired clock-neutral comparison at this precision.

The instrument is invariant under the specified independent **frame** gauge transformations. It is not shown to be spatially local, autonomously switched, energetically free or invariant under the noncyclic clock constraint. The sensor, preparation, model family, calibration and independent copies are supplied inputs. This is a simulation and a conditional statistical calculation, not observed experimental data.

Code: [joint instrument](verification/zero_gauge_clock_joint_instrument.py), [six focused tests](verification/zero_gauge_clock_joint_instrument_test.py).

## 1. Carriers and what the instrument is meant to distinguish

Use the three-frame loop model: the tree directions give the invariant chirality `t`, the third comparison link gives holonomy H, and `χ=tr H`. The previous pass specified

```text
ρ_ε = 1 + ε tχ/3,       |ε|<1,
E_ε[tχ] = 2ε/27.
```

The entire tree-direction marginal and entire H marginal coincide with the `ε=0` product reference state. Therefore a test of either marginal alone cannot detect this family’s correlation. We assume the old echo’s original uniform directional norm density, the given Haar loop measure, the `ρ_ε` family and the same old-system initialization as previously specified; this is **not** a claim that real preparations must belong to that family.

The qutrit chirality memory M is blank before the `9→10` write and, afterwards, has sign `B=±1` with `E[B|t]=λt`; define B=0 when it is blank. For a normalized N-reading sine-window history, the old echo and the recorded memory state are transported by the noncyclic clock-controlled shift. The 40-reading example here uses `n=0,…,39`.

## 2. A coherent finite-resolution clock sensor

Add a clock-sensor qubit initially in `|early⟩`. At each clock reading n apply a controlled rotation whose outcome `Y=late` has probability

```text
r_n = α       for n<10,
      1−β     for n≥10.
```

Here α is a false-late probability and β a false-early probability. The same constants for all readings, their independence from the angular/loop variables and their stability across copies are **assumptions**. A valid controlled 2×2 unitary has first column `(√(1−r_n),√r_n)`. Measuring the sensor yields the genuine instrument with Kraus multipliers

```text
K_late  = Σ_n √r_n |n⟩⟨n|,
K_early = Σ_n √(1−r_n) |n⟩⟨n|,
K_late†K_late + K_early†K_early = I.
```

It is not merely a post-hoc relabeling: the controlled unitary correlates the sensor with the clock, and measurement dephases clock coherences. A blank M is assumed to be distinguished perfectly from its two written signs; symmetric sign-report errors are introduced separately below.

Let `f_n=√[2/(N+1)] sin[π(n+1)/(N+1)]`, `p_post=Σ_(n≥10)|f_n|²`. Then

```text
p_late = α(1−p_post) + (1−β)p_post,
w = P(written | Y=late) = (1−β)p_post / p_late.
```

For `N=40`, `α=0.05`, `β=0.10`:

```text
p_post=0.90309632,   p_late=0.81763188,   w=0.99407413.
```

These are probabilities in this particular normalized window state and instrument. A late report is not a proof that the memory was written: a small false-late blank fraction remains.

## 3. A gauge-invariant loop sensor and the joint record

Introduce a second qubit, initially ready, with two outcomes `C=±1`. Since `χ∈[−1,3]`, for `0≤κ≤1` the effects

```text
F_c(H) = [1 + c κχ(H)/3]/2,       c=±1,
```

are positive and sum to identity. A controlled qubit rotation with first column `(√F_+,√F_−)` implements these effects, so `E[C|H]=κχ/3`. Both F and its unitary depend only on the conjugacy-invariant trace and thus commute with the independent frame-gauge action. This is a loop observable of the stated finite graph, not a calculated Wilson-loop correlator in a dynamical Yang–Mills theory.

Measure `(Y,B,C)` after the specified history. The clock sensor, qutrit sign projectors and loop-sensor effects act on commuting carriers/multiplication observables, so their joint POVM is well defined. This does **not** make the instrument nondisturbing: the loop sensor can attenuate coherences between different χ values if its result is ignored, and the clock sensor changes clock coherences. A locally implemented interaction around the loop, its path, switching, control and resource accounting are not constructed.

Assume the recorded signs B and C are independently flipped after the quantum instruments, with probabilities `p_B,p_C≤1/2`; a blank B remains correctly recognized as blank. Define `η_B=1−2p_B`, `η_C=1−2p_C`, and `X=B_observed C_observed`, including X=0 for a blank memory. Then

```text
μ_ε = E[X | Y=late] = w λκ η_Bη_C (2ε/81).
```

The extra factor of 1/3 compared with `E[Bχ]` is the finite loop sensor’s normalization. In the selected ensemble,

```text
P(X=0)=1−w,
P(X=+1)=w(1+μ_post)/2,
P(X=−1)=w(1−μ_post)/2,
μ_post=λκ η_Bη_C (2ε/81).
```

The individual B and C means remain zero in this model, both for `ε=0` and for nonzero ε. The correlation, not either individual marginal, is the discriminator. These identities include the coarse clock-selection error because blank is an explicit outcome. They do not establish the required source family, calibration or independence.

## 4. A finite-shot illustration—not an experiment

For the above N=40 clock, use the illustrative choices

```text
ε=0.8, λ=κ=1, p_B=0.05, p_C=0.10, α=0.05, β=0.10.
```

Then `μ_ε≈0.01413794` and the conditional X probabilities, ordered `+1,0,−1`, are approximately

```text
(0.50410603, 0.00592587, 0.48996809).
```

Collect `M` independently prepared **accepted** `Y=late` records. Under iid copies and stable calibration, Hoeffding’s inequality for `X∈[−1,1]` gives

```text
P(|X̄−μ_ε| ≤ r_M) ≥ 1−δ,
r_M = √[2 log(2/δ)/M].
```

If `g=w λκ η_Bη_C·2/81` is known and positive, the same event gives the model-dependent confidence interval

```text
ε ∈ [(X̄−r_M)/g, (X̄+r_M)/g] ∩ [−1,1].
```

Zero gain cannot identify ε. A confidence interval with an empty intersection is a model/calibration warning, not a valid estimate. The interval is a repeated-sampling statement, not a posterior probability and not evidence for the assumed preparation family.

For a reproducible **simulated** seed and `M=100,000`, `δ=0.05`, the three counts are `(50594,581,48825)`, giving `X̄=0.01769`, radius `0.00859` and the clipped interval approximately `[0.515,1]`. This is one favorable simulated realization; other samples vary. If independent copies are prepared until 100,000 pass the late selection, the expected number of total preparations under this model is `100000/p_late≈122304`. A fixed-budget protocol with a random accepted count needs the corresponding handling; no experimental data or resource-cost estimate is claimed.

Calibration and model errors are not included in the radius. For example, if the actual accepted X distribution is independently known to be within total-variation distance ζ of the specified model, the mean can differ by up to `2ζ`. The sign conclusion from the shown simulated mean survives this additional worst-case uncertainty only if `ζ<(0.01769−0.00859)/2≈0.00455`. If λ, κ, w, or the readout-flip rates are estimated rather than known, their calibration errors must also be propagated.

## 5. Reading the clock changes the constraint residual

Let `W_∞` be the earlier bilateral clock shift and `|Ω_N⟩` its sine-window history. Its bare residual is

```text
δ_N² = ||(W_∞−I)|Ω_N⟩||² = 2−2cos[π/(N+1)].
```

Keep the clock sensor coherently, without yet measuring it. Its sensor state at reading n is

```text
|s_n⟩=√(1−r_n)|early⟩+√r_n|late⟩.
```

The old history slices are related by the specified unitary step. At every adjacent pair except `9,10`, the sensor state is the same; at the boundary its overlap is

```text
γ = √[(1−α)β] + √[α(1−β)].
```

For the shift extended trivially to the sensor, the **exact** residual after coherent clock readout is therefore

```text
δ_sensor² = δ_N² + 2 f_9 f_10 (1−γ).
```

This is not an assumed generic error model. It is the actual disturbance of this specified controlled sensor and coherent history; α and β are probabilities, not automatically errors in the original old echo. If the sensor is uninformative (`α=1−β`), `γ=1` and it does not add this boundary term.

If the late result is postselected, the normalized conditional state has amplitudes `f_n√r_n/√p_late`, and its exact residual is

```text
δ_late² = 2 − (2/p_late) Σ_(n=0)^(N−2) f_n f_(n+1) √(r_n r_(n+1)).
```

These formulas concern the clock sensor alone; adding the later memory/loop measurements or discarding their outputs requires another channel calculation. For `α=0.05`, `β=0.10`:

| N | bare residual | coherent-sensor residual | late-conditioned residual |
|---:|---:|---:|---:|
| 20 | 0.14946 | 0.33644 | 0.35660 |
| 40 | 0.07661 | 0.17347 | 0.14868 |
| 80 | 0.03878 | 0.07219 | 0.06157 |
| 160 | 0.01951 | 0.02954 | 0.02609 |

The full reduced B/J/echo/sign/reference/clock/qutrit vector with a coherent sensor reproduces the N=40 values in the verifier. The analytical derivation extends to the stated unitary old history and gauge-invariant loop state because the sensor control is a scalar function of n. A measured/conditioned clock is not being silently treated as the unmeasured state.

## 6. What a small residual does—and does not—bound

For a normalized pure state with nonnegative real shift overlap and residual δ, the trace distance from its one-step-shifted state is exactly

```text
d = √(δ²−δ⁴/4) ≤ δ.
```

Thus any *unconditioned* effect probability changes by at most d under that one shift. For a joint selected statistic `X∈[−1,1]`, with original selection probability p and `p>d`, a conservative bound is

```text
|E_shifted[X | Y=late] − E_original[X | Y=late]|
    ≤ min{2, 3d/(p−d)}.
```

The proof uses `|Δp|≤d`, a bound `|ΔE[X·1_late]|≤2d`, and `|E[X·1_late]|≤p`. When `p≤d`, use the trivial bound 2. This is a **one-step drift bound for the same specified effects**, not a distance to an exact stationary state, a guarantee after arbitrarily many shifts, or an equivalence between different clock frames. Conditioning on rare events can make it weak.

For the N=40 coherent-sensor state, `d≈0.17282` and `p_late≈0.81763`, so the bound is approximately `0.80405`. It is much larger than the assumed model signal `≈0.01414`: the bound does not certify the desired comparison at signal resolution. It also does not show the actual drift is that large—the bound is deliberately conservative. A full operational clock comparison must transport preparation, clock instrument, effects and conditioning together.

The bilateral shift has no nonzero normalizable exact stationary state on the declared `ℓ²(Z)` carrier, as previously proved. The instrument above does not change that fact, and a small δ does not by itself construct a rigged physical inner product, solve the problem of time or justify a normalized infinite-anchor twirl. It is likewise separate from the finite cyclic construction, where an invariant twirled comparison was explicitly specified.

## 7. Next checks

- Derive a physical and possibly local implementation of the loop and clock sensors, including switching, geometry, noise calibration, resources and the effects of discarding environments.
- Test the same joint instrument in a properly defined exact constrained/rigged model or transport it between two explicit relational-clock descriptions. Obtain sharper **observable-specific**, conditioning-aware error bounds; the generic drift bound here is not sufficient for the small correlation.
- Challenge the assumed source family with coherent, holonomy-axis and calibration counterexamples. Separate data for the marginals cannot validate `ρ_ε` or rule out other joint states.
- Compare the graph-loop observable with an actual non-Abelian gauge-theory observable only after specifying a connection, dynamics and physical map. No Langlands duality, subjects, felt values or cosmic energy are derived by this instrument.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_gauge_clock_joint_instrument_test -v
```

The implementation checks unitary sensor matrices, frame-gauge invariance, loop/sphere quadrature, the reduced coherent clock state, exact residual formulas and the stated simulation. Finite sampling, numerical quadrature and code do not replace the analytical arguments or validate the physical assumptions.
