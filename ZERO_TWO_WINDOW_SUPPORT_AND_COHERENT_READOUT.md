# Better-conditioned clock readout—with a support flag and a cost

**Continuation:** [imperfect support-flag root](ZERO_TWO_WINDOW_IMPERFECT_SUPPORT_FLAG_ROOT.md) allows missed and false flags, derives a conditional finite-shot bound, and constructs an outside state missed by an apparatus that passes another outside calibration.

## Result

The [previous test](ZERO_TWO_WINDOW_COHERENCE_AND_CALIBRATION_TEST.md) found that the original 32-outcome clock-record instrument is informationally complete on a chosen two-packet span but weakly sensitive to one coherent direction. This is **not a universal obstruction**: a different explicitly defined five-outcome instrument on the same regulated physical space has balanced sensitivity to all three qubit directions and an outcome for being outside that span.

The improvement comes from a new, highly structured apparatus. It must coherently address the prescribed incident/receding packet modes and implement a projection onto their exact span and its complement. We do not derive a local detector Hamiltonian, an autonomous clock-triggered interaction, the required reference preparations, or its resource cost. It is a valid abstract quantum instrument, not a passive change of clock description or a free upgrade to the earlier detector.

With this instrument, a finite-shot calibration and an ideal support flag give a conditional bound for predicting the original clock-record outcomes on **separate copies**. Simulated leakage is included, including coherent leakage. On the copies actually subjected to the new instrument, later records change substantially. Code: [verification/zero_two_window_support_eraser_test.py](verification/zero_two_window_support_eraser_test.py).

## 1. An explicit alternative instrument

Use the same N=40 regulated two-window model and the same orthonormal incident/receding basis `B=(e₀,e₁)` as in the preceding report. Define `P=BB†` on the geometry–D–M₁–M₂ physical factor and `Q=I−P`. Both are tensored with the identity on the logical h factor. For the inference below, assume that the initial logical h state is the **same fixed state, uncorrelated with the geometry–apparatus factor**, including any component outside P. Without this assumption the projected state may remain entangled with h and a two-component qubit estimate need not predict h-dependent later dynamics.

Let `n_j`, j=1,…,4, be the four unit tetrahedron directions `(±1,±1,±1)/√3` with an even number of minus signs. On the packet qubit put

```text
E_j = (I₂ + n_j·σ)/4,          Σ_j E_j=I₂.
```

For a concrete imperfect readout, take four **inside effects**

```text
F_j = (1−ε)E_j + (ε/3) Σ_(k≠j) E_k,    ε=0.05,
G_j = B F_j B†,            G_out=Q.
```

These are positive and sum to the full identity. Use the explicitly specified Lüders operations `K_j=√G_j=B√F_j B†` and `K_out=Q`. Stacking the five K operators gives an isometry; in the finite regulator it can be extended to a unitary with a five-outcome memory. The `F_j` have the same outcome probabilities as a 5% symmetric classical relabeling of ideal tetrahedral outcomes, but **their Lüders instrument is not the same postmeasurement operation** as measuring the ideal effects and then relabeling. The disturbance calculation below uses the stated `√F_j` operations. The outside flag is assumed perfect and is never confused with an inside outcome.

For an input supported on P, `(p₁,…,p₄)=c+Lr` with c=(1/4,…,1/4). The four singular values of this 4×3 map consist of three equal values

```text
σ₁=σ₂=σ₃=(1−4ε/3)/(2√3)=0.269430.
```

The original 32-outcome protocol at N=40 had singular values `(0.407353, 0.003254, 0.001432)` on the same span, so the new map's smallest singular value is about **188 times** larger in the respective unweighted Euclidean frequency norms. These are different outcome spaces and different noise assumptions; the ratio is a conditioning comparison, not an optimal Fisher-information or fundamental sample-complexity theorem.

The abstract operators contain the full wavefunctions of both prepared modes. Implementing them requires coherent access to their relative phase and a reliable test of membership in their specified span. The packets are far apart in the selected geometry representation, and these are global mode operations, not the localized geometry-window couplings already constructed. Their mathematical existence does not establish that a physical internal observer can carry them out.

## 2. Calibrating and bounding outside support

Prepare independent reference batches in `z+`, `z−`, `x+`, `y+` of the packet basis, plus an unknown-state batch. Use the same five-outcome instrument in each. The four reference batches are assumed to lie exactly in P; an outside flag from one causes this protocol to abort rather than silently recalibrate. The unknown can be any density operator on the geometry–apparatus factor, including coherent superpositions between P and Q. Let

```text
λ = Tr(Qρ),       ρ_P = PρP/(1−λ)   if λ<1.
```

Each unknown shot yields either the outside flag or one of the four inside outcomes. Conditioned on an inside result, its label has the tetrahedral distribution of ρ_P; conditional on the observed number of inside shots, the labels are i.i.d. if the original copies are i.i.d. If no inside shots occur, the procedure aborts.

Use the four reference frequencies to estimate the affine qubit map `ĉ,L̂` exactly as in the [previous calibration theorem](ZERO_TWO_WINDOW_COHERENCE_AND_CALIBRATION_TEST.md), now with four inside outcomes. Let `r̂` be the least-squares Bloch estimate, projected onto the unit ball. Allocate α/6 to each of the four reference batches and the unknown inside labels. For their accepted shot counts, define

```text
e_i = [1+sqrt(log(6/α))]/sqrt(n_i),
e_c=(e_z+ + e_z−)/2,
e_L=sqrt[(e_x+ + e_c)²+(e_y+ + e_c)²+e_c²],
R=min[2, (e_target+e_c+e_L)/σ_min(L̂)].
```

If the measured matrix has no inverse, abort with R=2. The same multinomial concentration and calibration algebra as before gives `||r̂−r_P||≤R`, with failure probability at most `5α/6`.

For the outside count k in N unknown shots, allocate the remaining `α/6` between two one-sided bounds, each with failure probability at most `α/12`:

```text
λ_H = min[1, k/N + sqrt(log(12/α)/(2N))],
λ_0 = 1−(α/12)^(1/N) if k=0, otherwise 1,
λ_U = min(λ_H, λ_0).
```

The zero-count bound follows directly from `(1−λ)^N`; the other uses Hoeffding. Taking the minimum is covered by the allocated union bound. This estimate **requires** a perfect support flag: an unmodeled false negative can hide leakage, and a false positive can invalidate the reference assumption. Finite data never prove λ exactly zero.

On the joint confidence event, which has probability at least `1−α`, the normalized support projection obeys

```text
D_trace(ρ,ρ_P) ≤ sqrt(λ) ≤ sqrt(λ_U),
D_trace(ρ_P,ρ̂) = ||r_P−r̂||/2 ≤ R/2.
```

The first inequality follows by projecting a purification and applying contractivity of trace distance; it also covers P–Q *coherence*, not only classical leakage mixtures. Therefore any fixed subsequent quantum procedure has outcome-distribution error at most

```text
TV ≤ min[1, sqrt(λ_U)+R/2].
```

This applies to the original 32-history procedure on independently prepared copies, assuming the same fixed logical h state and a correctly modeled target procedure. It is not a statement about the actual later history of a copy that has already undergone the new instrument. Unknown preparation, detector, logical-sector or target-dynamics errors need separate bounds; reference uncertainty is not automatically included in shot noise.

## 3. Simulated finite-shot comparison

Take the previous qubit `(0.31,−0.42,0.20)`, no leakage, and 100,000 simulated independent shots in each of the five batches. With seed 9387 and α=0.05:

```text
estimated r = (0.301996, −0.415943, 0.205050)
measured σ_min(L̂) = 0.266296
Bloch radius R = 0.189290
outside count = 0/100000,     λ_U = 0.000054805
bound on original-procedure TV error = 0.102048.
```

The realized Bloch error is about 0.01030, but it is not the 95% guarantee. With the same five batches of 100,000 shots, a separate seeded simulation of the **old** 32-outcome instrument gives the trivial radius R=2 under its previous bound. The two confidence constructions allocate their failure probabilities slightly differently because the new test also bounds leakage. Neither example is an optimized estimator or a proof that the old device intrinsically requires a particular number of shots. The 500,000 shots here are simulated and exclude source, apparatus and detector-calibration costs.

As a leakage control, construct an outside packet orthogonal to the span and a pure state with amplitude `sqrt(0.99)` in the span and `sqrt(0.01)` outside, retaining coherent cross terms. In 100,000 target shots (seed 804), 1,049 outside flags yield `λ_U≈0.015725`; the inside calibration gives `R≈0.187653`. The bound for the original 32-outcome distribution on separate copies is 0.219225, while its actual modeled TV error is about 0.004174 in this realization. The bound is conservative; this is a consistency check, not a coverage proof for the continuum model.

## 4. The additional measurement really changes the experiment

Apply the new instrument nonselectively to the incident preparation, **then** perform the old three-attempt clock-record protocol on that same copy. At N=40 the TV distance between its old-protocol distribution and the distribution without this new intervention is about 0.168672 for ideal old click labels, or 0.161708 after the old first-bit reporting noise. Final `Pr(M₁=1)` changes from 0.426804 to 0.335834. Both histories are normalized and use the same subsequent dynamics. These differences demonstrate backaction, not disagreement between representations.

Thus the improved inference works by deliberately adding an interferometric measurement on an ensemble and predicting a separate matched ensemble; it does not improve the original device for free. The exact support flag also shifts the previous unexplained preparation restriction into a demanding apparatus and its calibration. Whether such a global mode measurement is physically realizable, how to implement it autonomously, and what resources it requires remain open.

## Scope and reproduction

The tetrahedral and support POVMs exist in the regulated Hilbert space and extend formally to the corresponding closed two-dimensional continuum subspace, but the numerical comparison supplies no continuum discretization error or physical locality proof. It uses an ideal scalar clock for the old protocol, assumed modes and logical state, and an ideal support flag. It does not identify exact crossings, solve inhomogeneous quantum gravity, derive the proposed whole from zero, or establish experienced time.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_support_eraser_test -v
```
