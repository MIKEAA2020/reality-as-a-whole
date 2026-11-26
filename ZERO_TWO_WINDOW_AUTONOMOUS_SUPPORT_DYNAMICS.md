# A time-independent support interaction and its limits

## Result

The [imperfect-flag analysis](ZERO_TWO_WINDOW_IMPERFECT_SUPPORT_FLAG_ROOT.md) required a uniform detector-error bound but did not supply detector dynamics. Here is one explicitly specified, **scalar-clock-independent** support coupling added to the same two-window model. Under its exact operator assumptions it gives a state-uniform continuum bound on missed and false flags, despite noncommutation with the original evolution. The altered positive-frequency constraint has a strictly positive root.

The certified bound is weak: with the chosen coupling it allows error probability up to **0.678**. Regulated calculations give much smaller worst-case errors, about **0.00584**, but they do not by themselves certify the continuum value. The flag is also **not a durable record**: because the interaction keeps running, an outside packet that is flagged at the selected reading is almost unflagged at twice that reading in the numerical control.

This is a stipulated global-mode Hamiltonian inside a changed constraint, not a derived local apparatus. Its readout still refers to a selected ideal scalar-clock reading. A fixed norm bound on implementation error improves the logical status of the flag guarantee, but that norm bound is itself a physical assumption. [Verification](verification/zero_two_window_autonomous_support_dynamics_test.py) checks the finite model; the continuum inequalities below are analytic.

## 1. An interaction inside a changed constraint

Let the old model have `Ω_h=√Θ_h`, h=0,1, and physical scalar evolution `exp(iΩ_h φ)`. Let P project onto the previous incident/receding packet span in the geometry–D–M₁–M₂ factor, and Q=I−P. P and Q act identically on both h sectors. Add a fresh flag qubit A initialized in z=0 and stipulate the time-independent operator

```text
H_h = Ω_h ⊗ I_A + g Q ⊗ σ_y^A,
Θ'_h = H_h²,                         g=1.2,
C'_h = (p_φ² − Θ'_h)/2.
```

The selected positive-frequency branch has `p_φ=H_h` and evolution `exp(iH_h φ)` because H_h is strictly positive, as shown next. This is a **different constraint and physical interaction** from the original autonomous records model, not a representation change. Q depends on the specified global packet modes and all the old apparatus factors. The new flag and its initialization are assumed, not derived from zero.

For each of the old band-compressed window effects, positivity and trace class give `||E_a||≤tr(E_a)=2/π`. With the original couplings λ=0.5 and κ₁=κ₂=0.65 and momentum band `p∈(−7,−6)`,

```text
6−2h−7.2/π ≤ Θ_h ≤ 49/6−2h+7.2/π.
```

Consequently, writing these positive bounds' square roots as a_h and b_h,

```text
a₀≈1.925661,  b₀≈3.233960;
a₁≈1.306969,  b₁≈2.908350;
H_h ≥ (a_h−g) I ≥ 0.106969 I.
```

The argument includes the full continuum Hilbert space in the declared band, not a finite-mesh eigenvalue count. It uses only the stated model and specified bounded coupling. It does not establish a spatially local implementation of Q, a physical energy budget, full gravity or an autonomous mechanism that stops the flag.

## 2. A uniform bound with the original evolution left on

At the scalar reading

```text
τ = π/(2g) ≈ 1.308997,
```

measure the flag A in the z basis. If Ω_h commuted with Q, the added interaction would rotate A from 0 to 1 on Q and leave it at 0 on P. In the actual model Q generally does **not** commute with Ω_h, so that ideal comparison cannot simply be asserted.

Set `c_h=||[Ω_h,Q]||`. In the interaction picture, `||Q(s)−Q||≤s c_h`. Duhamel's formula therefore bounds the difference between the actual evolution and the ordered ideal comparator `exp(iΩ_h τ)exp(ig Q σ_y τ)` by

```text
D_h ≤ g c_h τ²/2 = π² c_h/(8g).
```

The ordered comparator is only a mathematical comparison; it is not claimed to be an implemented second apparatus. For any normalized state initially in Q, the actual no-flag probability is at most `D_h²`; for any state initially in P, the actual false-flag probability is at most `D_h²`.

The spectral interval gives a completely state-independent continuum estimate:

```text
c_h = ||Q Ω_h P|| ≤ (b_h−a_h)/2,
D = max_h D_h ≤ 0.823177,
miss probability ≤ D² ≈ 0.677620,
false-flag probability ≤ D² ≈ 0.677620.
```

The first identity uses the off-diagonal blocks of the commutator with a projection. The estimate holds for arbitrary P/Q states and arbitrary h correlations because the old evolution and Q preserve the h blocks. It supplies a nontrivial uniform bound under the exact Hamiltonian, but 0.678 is far too large to claim a precise support detector.

If the actual self-adjoint generator differs by a bounded perturbation `ΔH` with `||ΔH||≤δ`, Duhamel adds at most `τδ` to the amplitude bound. Provided `δ<a₁−g` so positivity is retained, use `min[1,(D+τδ)²]` for the worst-case miss and false flag. This is robust to **all** perturbations within that operator-norm ball, but a finite set of calibration trials does not automatically establish such a worst-case norm bound; the previous hidden-direction objection still applies.

## 3. The actual flag is not the earlier block-diagonal instrument

The original evolution rotates P into Q, so the induced flag effect need not be block diagonal. In the N=24 calculation, `||P E_flag Q||` is about 0.0644 for h=0 and 0.0761 for h=1. The false-positive/miss formula derived for the earlier block-diagonal POVM must **not** be imported unchanged.

There is nevertheless a direct coherent-state support bound. For an arbitrary initial state, including P–Q coherence and h correlations, let `λ=Tr(Qρ)` and q be the actual probability of a flag at τ. Applying the unitary-norm bound to a purification gives

```text
|sqrt(q) − sqrt(λ)| ≤ D,        λ ≤ min[1,(sqrt(q)+D)²].
```

For N independent copies and k flags, a one-sided binomial upper bound q_U may be substituted for q; its own confidence budget must be specified. This estimates the initial support population in the **changed** constraint experiment. It does not automatically supply the earlier tetrahedral tomography instrument or its accepted-label contamination bounds.

For illustration only, a coherent state with λ=0.01 was simulated at N=40, averaged over the previous equal h preparation. Its model flag probability is 0.015565. A seeded 100,000-shot sample gives 1,519 flags and the 95% one-sided bound `q_U=0.019485`; the universal continuum inequality gives only `λ≤0.926915`. The large bound is honest: this run does not establish a small continuum leakage under the universal estimate.

## 4. Regulated dynamics and a sharper target

For g=1.2, the worst-case N=24 numerical rates are

| h | missed flag on Q | false flag on P | `||[Ω_h,Q]||` |
|---|---:|---:|---:|
| 0 | 0.004169 | 0.004169 | 0.077601 |
| 1 | 0.005833 | 0.005833 | 0.091858 |

N=40 changes each displayed worst-case probability by less than 10⁻⁶. At N=40, using the *computed finite-matrix* commutator in the same Duhamel formula would give D≈0.094438 and, for the illustrative count above, `λ≤0.054768`. This is a regulator-specific numerical bound, not a certified continuum bound.

There is a concrete route to tightening the continuum estimate without diagonalizing the full continuum operator. For positive Θ_h≥a_h², the resolvent formula gives

```text
||[√Θ_h,Q]|| ≤ ||[Θ_h,Q]||/(2a_h).
```

Since Θ₁=Θ₀−2I, the commutator of Θ with Q is h-independent. The finite meshes give `||[Θ,Q]||≈0.4112`. **If** an independent continuum analysis established `||[Θ,Q]||≤0.42`, then the same calculation would imply `D≤0.165190` and worst-case flag errors below 0.0273 for both h sectors. The mesh values are motivation for that test, not proof of its premise; no continuum discretization-error bound has been supplied here.

## 5. Why the flag is not yet a history record

The coupling in H_h remains on. At N=24, for one normalized outside packet, the flag probabilities at τ and 2τ are respectively

```text
h=0: 0.999978, 0.000089
h=1: 0.999969, 0.000124.
```

These are two separate unmeasured evolutions followed by a flag measurement; measuring at τ would itself change the later state. They illustrate reversible unflagging, not an irreversible record. Even in the exactly commuting idealization the flag rotates back to 0 at 2τ. To retain a history one must add a stopping/transfer mechanism, further clock-controlled interaction or environment, and then analyze its backaction and resource assumptions. Turning off the coupling at τ by hand would be a different, externally scheduled protocol.

The state of the old clock apparatus after this new interaction is also not generally the state it would have had under the old constraint. Predicting the original histories on separate identically prepared copies is a separate counterfactual protocol, not evidence that the new device leaves those histories unchanged.

## Scope and reproduction

The construction specifies a possible bounded Hamiltonian in the selected band and a mathematical constraint containing it. It does not show that the mode projector, coupling strength, clock, state or stopping mechanism follows from the proposed whole. It does not establish local quantum gravity, arbitrary refoliation, exact crossing counts, subjects or felt succession. The conditional improvement target above is the next numerical/analytic issue; physically implementing and stabilizing the device is a distinct one.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_autonomous_support_dynamics_test -v
```
