# Can the existing records detect the coherent counterexample?

**Continuation:** [support and coherent readout](ZERO_TWO_WINDOW_SUPPORT_AND_COHERENT_READOUT.md) constructs a better-conditioned alternative with an ideal outside-span flag, quantifies finite-shot inference, and measures its disturbance of the original protocol.

## Result

Yes, **within a specified two-dimensional packet span and the finite regulator**, the full 32-outcome instrument already used in the [finite-shot calculation](ZERO_TWO_WINDOW_FINITE_SHOT_CLOCK_CALIBRATION.md) is informationally complete: its outcome probabilities determine every qubit density matrix on that span, including coherent superpositions. The earlier pair with identical first-click rates has different final-memory statistics. No extra detector interaction is required beyond that earlier *three-attempt plus final-memory* protocol; compared with observing only the first click, however, the additional attempts and memory readout are physical interventions and can cause backaction.

The limiting factor is sensitivity. At N=40 the relevant singular values are approximately `(0.407353, 0.003254, 0.001432)`. Thus the weakest direction is about 284 times less visible than the strongest in this Euclidean output norm. A conservative, calibration-aware finite-shot example needs a very large number of copies to certify a useful worst-case bound. This is a feature of the chosen bound and model, **not** a proved lower bound on optimal tomography or a physical resource estimate.

The span, reference-state preparations, stable instrument, scalar-clock checkpoints and detector error model remain assumptions. Full-record tomography inside the span cannot automatically certify that an unknown source has no components outside it, or derive the clock and its laws from zero. [Verification](verification/zero_two_window_coherence_tomography_test.py) is a finite-model calculation, not an experimental demonstration or continuum proof.

## 1. What is being measured

Use the previous constraint and the same reported protocol: yes/no E₀ Lüders operations at φ=30,40,50, then M₁/M₂-z at φ=100. Only the first reported click bit is classically misread, with 3% false positives and 5% false negatives; its true outcome still determines the physical backaction. The later bits and final memories are idealized. The output has 32 mutually exclusive labeled outcomes.

Let `u` be the incident state and `v` the receding state, both with the same initialized D/M registers. Since u and v are slightly nonorthogonal, use Gram–Schmidt to set

```text
e₀=u,     e₁=(v−u⟨u,v⟩)/||v−u⟨u,v⟩||.
```

The restricted input is an arbitrary density matrix on this **complex span**, tensor the same prepared logical h state as in the previous model. It contains the prior incoherent incident/receding line, but also all pure and mixed coherent superpositions. For each reported full-history outcome s, compress its physical effect to this basis, obtaining positive 2×2 matrices `F_s` with `Σ_s F_s=I`. For `ρ=(I+r·σ)/2`,

```text
p_s = Tr(F_s ρ) = c_s + L_s · r,
c_s=Tr(F_s)/2,        (L_s)_j=Tr(F_s σ_j)/2,        ||r||≤1.
```

The 32×3 real matrix L has rank three at N=40, so this modeled POVM is informationally complete **on this span**. The test constructs effects from the actual branch vectors, including both h channels, all original memories and first-bit reporting noise; it checks positivity, normalization and direct complex-state predictions. At N=80 the singular values are approximately `(0.407330, 0.003288, 0.001437)`. These agree qualitatively with N=40 but do not prove continuum rank, a continuum condition number or physical implementation.

The prior equal-first-click coherent pair has the same observed first-bit probability `0.191491`, but final `Pr(M₁=1)` differs: `0.221422` versus `0.206396`. The two full reported-history distributions have TV distance `0.025180`. If these are two **fully specified hypotheses**, their final-M₁ probabilities are exactly known, copies are independent and the device is stable, a midpoint threshold on N full-protocol trials has, by one-sided Hoeffding, error at most `exp(−N Δ²/2)` under either hypothesis, where `Δ≈0.015026`. About **26,538** trials give a 5% upper bound under each hypothesis. This is a sufficient, conservative bound for that binary comparison—not a way to test arbitrary coherent alternatives and not inclusive of calibration or systematic uncertainty.

## 2. Estimating an arbitrary qubit with finite calibration

The following bound uses real detector counts, not complex slice amplitudes. It assumes four known, reproducibly prepared qubit reference states `z+`, `z−`, `x+`, `y+` in the e₀/e₁ basis, plus copies of the unknown state. Apply the **same** full-history instrument to each batch. These coherent reference preparations are extra source controls; their availability is not established by the detector model.

Let the five 32-outcome frequency vectors be `p̂_z+`, `p̂_z−`, `p̂_x+`, `p̂_y+`, and `p̂`. Form

```text
ĉ = (p̂_z+ + p̂_z−)/2,
L̂_z = (p̂_z+ − p̂_z−)/2,
L̂_x = p̂_x+ − ĉ,        L̂_y = p̂_y+ − ĉ.
```

If `L̂` has rank three, take the least-squares estimate `L̂⁺(p̂−ĉ)` and project it onto the unit Bloch ball, obtaining r̂. Otherwise abort with the trivial radius 2. This calibration estimates the *whole instrument*, not merely its first-bit marginal.

For an n-shot multinomial frequency vector from independent identically distributed copies, let

```text
e(n,δ) = [1 + sqrt(log(1/δ))] / sqrt(n).
```

With probability at least `1−δ`, its Euclidean error is at most e. To see this, the expected Euclidean error is at most `1/√n` by Jensen and the multinomial covariance, and changing one trial changes the norm of the frequency error by at most `√2/n`; McDiarmid's inequality supplies the remaining term. No independence between the 32 components of one multinomial vector is assumed.

Allocate failure probability `α/5` to each of the four reference batches and the target batch. Write their bounds as `e_z+`, `e_z−`, `e_x+`, `e_y+`, `e_t`, and set

```text
e_c = (e_z+ + e_z−)/2,
e_L = sqrt[(e_x+ + e_c)² + (e_y+ + e_c)² + e_c²],
R = min[2, (e_t + e_c + e_L)/σ_min(L̂)].
```

A union bound and the Frobenius bound on the calibration-matrix error give, with probability at least `1−α`,

```text
||r̂−r||₂ ≤ R.
```

The singular value in this bound is the **observed** one; a small value can make the bound trivial even if the point estimate looks precise. Projection onto the Bloch ball cannot increase the distance to the true allowed r. This guarantee assumes the same stable physical instrument and the stated exact reference states, not just independent shot noise.

For any other fixed quantum procedure on independently prepared copies of the same span state, the total-variation distance between its outcome predictions for r̂ and r is at most `R/2`, by the qubit trace-distance bound and data processing. This makes it possible, conditionally, to predict the **unprobed** φ=100 memory distribution from data obtained on separately probed copies. It does not erase the probe's disturbance on the copies actually measured. Any independently justified mismatch between the modeled future procedure and the real one must be added to that error budget.

## 3. Numerical shot and backaction example

With the N=40 model, take an unknown Bloch vector `(0.31,−0.42,0.20)` and simulate independent 32-outcome counts with seed 4820. Use **10 billion copies in each of the five batches**—50 billion total simulated preparations. At α=0.05 the result is

```text
r̂ = (0.309633, −0.418687, 0.200016)
observed σ_min(L̂) = 0.00143173
actual ||r̂−r|| = 0.001364
95% bound R = 0.109866
bound on any other fixed-procedure event error = R/2 = 0.054933.
```

The realized error is smaller than the conservative guarantee; it is not itself a confidence bound. For the separate no-checkpoint-probe procedure, the modeled final `Pr(M₁=1)` is 0.260097 and the estimate predicts 0.260100. The two procedures are deliberately different: the repeated probes prepare the data; autonomous unprobed evolution is the target prediction on other copies. The estimate is valid only insofar as the same input state is reproducibly prepared and the model of that target procedure is correct.

For scale only, using the nominal singular value as though already known, this particular bound suggests roughly `3.6×10⁸` unknown copies to certify Bloch radius 0.1 with exact calibration. With equal-sized **finite** reference and target batches, the five-batch formula suggests about `1.2×10¹⁰` copies *per batch* for that radius. Actual guarantees must use the measured singular value; these figures are not a lower bound, an optimized experimental design, or estimates of thermodynamic cost. The large difference between these shot counts and the earlier two-component mixture fit reflects that arbitrary coherence introduces very weakly visible directions and extra calibration requirements.

## 4. Testing the mixture assumption—and its limit

The original incoherent family is a line segment in the Bloch ball between the actual (slightly nonorthogonal) incident and receding density matrices. Distance to that segment is 1-Lipschitz. If the inferred r̂ lies more than R from the segment, the family is rejected on the same confidence event, **provided the state really lies within the two-packet span and the calibration assumptions hold**. The two earlier coherent witnesses are approximately 0.998 and 1.001 in Bloch distance from the line. Passing such a finite-resolution test does not prove incoherence; nearby coherent states can remain undetected.

More fundamentally, the 32-outcome calculation does not establish the assumed support. Let an outside state be orthogonal to the span, and let an actual preparation be

```text
ρ_actual = (1−λ)ρ_span + λρ_out,     0≤λ≤1.
```

For this same instrument, the difference between its output distribution and that of `ρ_span` has TV at most λ and Euclidean norm at most `√2 λ`. Thus an arbitrarily small nonzero leakage can be hidden below any finite measurement tolerance. The verifier constructs an explicit orthogonal outside packet at the regulator and checks this inequality. This does **not** prove that all outside states are indistinguishable, or that large leakage cannot be detected by the full records.

If an independent argument supplies `λ≤λ₀`, the above statistical derivation can include an extra `√2 λ₀` in the numerator of R, and the TV error for another fixed procedure is at most `λ₀+R/2` (capped at 1). Likewise, bounded preparation or apparatus systematics can be included as additional independently justified residual norms; shot-count confidence alone does not bound them. In this poorly conditioned example even a small unbounded residual can strongly affect the inferred weak direction. The required span, reference controls and systematic bounds are therefore the next substantive assumptions to test, not details solved by inversion.

## Scope and reproduction

These are modeled statistics in a homogeneous, band-projected positive-frequency constraint, with an ideal scalar clock and scheduled geometry operations. They do not establish autonomous geometry-triggered time, true crossing counts, refoliation invariance, actual subjects or experience. All results are conditional on the model and assumed inputs; a whole-level zero does not by itself supply the device, a clock law or the experienced order.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_coherence_tomography_test -v
```
