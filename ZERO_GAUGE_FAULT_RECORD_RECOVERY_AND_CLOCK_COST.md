# A concrete calibration rival, fault recovery and clock cost

## Result

The [last pass](ZERO_GAUGE_CALIBRATION_CAUSES_AND_TRANSFER_BOUND.md) identified source–reference transfer as a missing premise. This pass specifies a finite unitary mechanism that realizes the problem on the existing chirality and loop-sign records, then tests a possible repair:

- A hidden environment qubit coupled only to the B record and a fault qubit reproduces the earlier false correlation. All four reference tables, the environment's marginal and its correlations with either sign separately look correct; the missing information is its correlation with the **joint** sign context.
- If the fault qubit is supplied in a known ready state and remains accessible, a specified coherent correction removes **this particular interaction's** B error for every written B–C state, including states entangled with the environment. It makes the example's correlated and uncorrelated sources distinguishable by their reported sign correlation again.
- The correction does not restore blank–written coherence. Keeping the fault record in the actual coherent clock-sensor history raises its one-step constraint residual from **0.173474** to **0.174998** in the example. This is an exact model calculation, not a general clock-frame comparison.

The mechanism and correction are stipulated finite gates, not an autonomous spatially local apparatus or an experiment. They expose what a transfer guarantee and its physical resources would require; they do not derive those inputs from the whole. [Code](verification/zero_gauge_fault_transfer_recovery.py) and [tests](verification/zero_gauge_fault_transfer_recovery_test.py).

## 1. The actual records and an explicit additional interaction

Use the preceding clocked chirality memory `B∈{blank,+,−}` and loop-sensor sign record `C∈{+,−}`. They are scalar under the stated frame-gauge action. Add a hidden environment qubit E and a fault qubit A. Prepare A in `|0⟩`; its initialization is a supplied resource. Let

```text
X_B = |+⟩⟨−| + |−⟩⟨+|,       P_E = |1⟩⟨1|,
U = exp[−i θ X_B ⊗ I_C ⊗ P_E ⊗ X_A].
```

`X_B` annihilates the blank. Thus E=`0` leaves B and A unchanged, whereas E=`1` coherently correlates a B flip with A. Tracing A makes the B flip probability `q=sin²θ` in E=`1`. There is no direct B–C coupling in U. Because the added carriers and controls are taken to be frame scalars, U is invariant under the declared independent frame transformations; this does not prove spatial locality or invariance under the clock constraint.

After U, apply separately stipulated independent **classical reporting** flips: B at rate `p_0`, C at rate `p_C`; blank remains recognized. For a written joint-sign context `(b,c)` and conditional environment occupation `t_bc=P(E=1|b,c)`, the final B error and product mean are

```text
p_eff(b,c) = p_0 + (1−2p_0) q t_bc,
h_bc = (1−2p_0)(1−2p_C) bc [1−2q t_bc].
```

The output effects for this specified gate with A initially ready and traced are diagonal in the B sign and E occupation. Thus these formulas apply to their joint diagonal probabilities even if an input has coherences; they do **not** imply that other measurements, state coherence or the entire previous history are unchanged. The comparison below fixes the sign and clock-output statistics, not all observables.

A sign reference can be prepared mathematically by a permutation taking blank B to the required sign and a bit flip setting C, with E in `diag(1−t_ref,t_ref)` and A in `|0⟩`. All four controls, E preparation, isolation and reset are specified, not derived. In particular, calibrating post-record B and C signs does not validate the earlier chirality-write or loop-sensor preparation.

## 2. Why the same calibration can hide a false correlation

Choose

```text
q=.04, θ=arcsin(.2), p_0=.03125, p_C=.1, t_ref=.5.
```

Each of the four reference tables is exactly the independent-channel table with B error `.05` and C error `.1`; its product gain is `.72`. The environment marginal is `P(E=1)=.5`.

Compare two written-source models:

1. **Target:** the true sign distribution is `P(b,c)=[1+bc z]/4` with `z=2(.8)/81≈.0197531`, and `t_bc=.5`. This is the recorded-sign distribution predicted by the earlier `ε=.8, λ=κ=1` family, under its specified sign instruments.
2. **Rival:** true signs are independent and fair, but E is correlated with their joint context:

```text
t_bc = .5 + t_1 bc,      t_1 = −.237037037… .
```

These are valid probabilities: `t_+=.26296296` and `t_−=.73703704`. The rival's effective B error is `.05−.00888889 bc`, precisely the earlier contextual-error example. Hence both models have the same written reported-sign table and mean **0.01422222**. If both use the same sign-independent clock sensor, same written fraction and blank handling, their coarse selected `(late,B,C)` tables also coincide. The rival is an alternative joint state of records and environment; it is not evidence for an actual fault and it is not asserted to match the full coherent source state, arbitrary observables or all future dynamics.

In the rival, the E marginal is still `.5` and `P(E=1|b)=P(E=1|c)=.5`. Checking E or either sign alone misses the common dependence. A common-past variable can establish it without any instantaneous C-to-B signal. Conversely, a validated joint-context environment monitor would expose it—but it must identify true joint labels, not merely the already faulty output labels, and its own backaction and transfer need justification.

For this particular interaction the general transfer uncertainty can be tightened. If the same `q,p_0,p_C` apply to reference and source and `|t_src,bc−t_ref,bc|≤d` in each selected context, then

```text
|h_src,bc−h_ref,bc| ≤ τ_gate = 2(1−2p_0)(1−2p_C) q d.
```

If the source's q differs from the reference by at most `Δq`, a valid bound is `2(1−2p_0)(1−2p_C)(q_src d+Δq)`, capped at 2, where `q_src` is itself bounded. If reporting gains or the controlled interaction differ, their errors also need inclusion. In the rival, `d=|t_1|` and `τ_gate=.01422222`: the bound is **saturated**, at the same scale as the entire target signal. Calibrating the mean environment population does not justify a smaller d.

## 3. A repair: keep and coherently correct the fault

Define the unitary B permutation `F_B=|blank⟩⟨blank|+X_B` and the feedback gate

```text
W = I_B ⊗ |0⟩⟨0|_A + F_B ⊗ |1⟩⟨1|_A.
```

It acts trivially on C and E. Apply W after U, retaining A. On **any written state**, including an arbitrary joint B–C–E state, with A initially `|0⟩`, the combined action factors as identity on B,C and an isometry on E,A:

```text
E=0: |0⟩_E|0⟩_A → |0⟩_E|0⟩_A,
E=1: |1⟩_E|0⟩_A → |1⟩_E(cosθ|0⟩_A − i sinθ|1⟩_A).
```

The identity follows because W flips B exactly when the coherent fault branch has flipped it. It does not require E to be independent of B or C, nor a classical mixture of written signs. Tracing E,A therefore leaves the written B–C density operator unchanged. The code checks random entangled written states as well as the exact sign tables. This is a gate-level statement for the declared fault channel—not correction of arbitrary environmental couplings.

In the two source examples, the uncorrelated rival now gives reported written product mean 0, while the target gives

```text
(1−2p_0)(1−2p_C) z = .75 × (1.6/81) ≈ .01481481.
```

With the prior late-selection model, the target accepted mean is approximately `.01472702` because `w≈.99407413`; the rival remains zero. The gain is now `.75`, not the old `.72`: the altered instrument needs its own calibration. The independent reporting flips and sign-independent clock selection remain assumptions. Correcting this fault does not by itself establish the original source family or exclude other channels.

**Why does the repair work?** It has access to a physical record of precisely the error branch and reverses the corresponding conditional B operation. **Why is the record trustworthy?** It must start in `|0⟩`, remain accessible, be coupled by the declared gate and drive an accurate W. For instance, if A is actually `|1⟩` with E=`0`, U causes no fault but W flips B anyway. If E=`1` and A starts `|1⟩`, both coherent branches likewise leave B flipped: the residual flip probability is 1. The correction moves the calibration burden to a ready state, fault coupling and feedback, rather than eliminating the need for justified physical premises.

The same gate algebra gives a useful imperfect-ready bound. On the written sector, `WU = V_EA W`, where `V_EA=exp(−iθ P_E X_A)` acts only on E,A. If the initially wrong-ready population `P(A=1)` is at most `e_A` in the relevant written ensemble, even allowing arbitrary correlations and coherences with B,C,E, tracing E,A after WU changes the B–C state by trace distance at most `e_A`. Under the separately stipulated reporting flips, the reported product mean changes by at most

```text
2 (1−2p_0)(1−2p_C) e_A.
```

For these gains and `e_A=.001`, the bound is `.0015`. To use it in the previous finite-shot error budget, e_A must be independently bounded **in the accepted source ensemble**; an average reference reset check does not automatically give that bound. In the four-context formula, a per-context bound can contribute `2×.75×e_A` to D relative to ideal corrected gain `.75`. Uncertainty in that bound requires a confidence allocation of its own. This covers this exact U and W, not imperfect feedback or other faults.

A fresh ready A for each shot, access to E/A, gated feedback and retention or reset of A are resources. No reset energy, timing, local control path or autonomous preparation is calculated here. An implementation that discards the fault record before feedback cannot perform this W; measuring it first and using its outcome is a different instrument whose costs and disturbance also need analysis.

## 4. Why does correcting the sign still disturb the clock?

On blank B, U and W leave `E=1,A=0` unchanged; on written B they put A in

```text
|f⟩ = cosθ |0⟩ − i sinθ |1⟩.
```

The fault record therefore distinguishes blank from written. For `(|blank⟩+|+⟩)/√2` with E=`1`, after correction and discarding A the off-diagonal blank–written matrix element is `cosθ/2`, rather than `1/2`. The trace distance between these two reduced B states is `(1−cosθ)/2≈.01010205`. This loss does not contradict exact recovery **within** the written sector.

Now retain A coherently in the *actual reduced history* of the prior clock-sensor model, with E fixed to `|1⟩`. Apply U then W to the qutrit and A in each history slice and compare the same one-step bilateral shift extended trivially to sensor, E and A. The sensor states on the two sides of the `9→10` write have overlap

```text
γ = sqrt[(1−α)β] + sqrt[α(1−β)].
```

The fault-record overlap across that boundary is `cosθ`. Hence the exact residual is

```text
δ_recovered² = δ_sensor² + 2 f_9 f_10 γ (1−cosθ).
```

For `N=40, α=.05, β=.1, θ=arcsin(.2)` this gives

```text
δ_sensor = .17347437,      δ_recovered = .17499811.
```

The implementation separately propagates the old system, reference, qutrit, coherent sensor and retained fault record under the original controlled step, and reproduces the formula for multiple chirality fibers and clock parameters. E=`1` is a specified test condition, not the `.5` mixture used in calibration. This is the **full coherent sensor-plus-fault residual before final sign reporting**, not the residual after discarding the environment, postselection or a proof of a physically equivalent clock frame. A small added residual does not guarantee signal-scale operational equivalence for arbitrary effects.

## 5. Continue asking why

1. **Why did calibration fail?** The source's joint-sign context predicted an environmental control bit while references only reproduced its single-system marginal. The apparatus implemented a sign error conditioned on that bit.
2. **Why did the correction succeed?** The stipulated unitary records the complete B-flip branch in a ready, accessible ancilla, and the feedback gate uses it without error. These are stronger premises than observing a small average error rate.
3. **Why is the problem not finished?** Ready-state quality, other fault operators, correlated reporting, controls, clock selection, access, retained records and their resources need actual physical justification. Correction of a classical-looking sign does not restore all coherent history information; a fixed-effect residual is not clock-frame transport.
4. **Why expect this apparatus or the source to exist?** The carrier, gauge-scalar coupling, source–environment state, ready ancilla and gate are supplied formal structure. Gauge invariance admits the construction but does not derive its local mechanism, energy or autonomous operation. The modeled `ρ_ε` correlation remains a conditional candidate, not a result selected by zero.
5. **Why the constitution and its actuality?** The current programme has not non-circularly derived the particular carriers and dynamical law from the purported self-sufficient whole or shown why they are actual. Continuing that constitutive question is necessary; reaching this limit in the present analysis is not proof of ultimate brute bedrock and does not require positing an external temporal cause.

The positive advance is constructive: *if* the fault record and feedback satisfy these premises, a concrete false correlation is corrected on the written sector, and its cost to the previously specified clock history is calculable. The missing physical warrant is now more precise.

## 6. Next work

- Model imperfect ready states and feedback, other error operators, inaccessible fault modes and repeated use; propagate their actual error bounds into the four-context interval rather than assuming exact recovery.
- Compare two explicitly constructed clock descriptions with the **whole** corrected instrument and all controls transported, including the retained A record. The shift calculation here is not that comparison.
- Derive or experimentally constrain the coupling, preparation, selection and resource-reset mechanism; continue the deeper constitution/actuality why-chain rather than accepting a stipulated fault gate as an explanation of the whole.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_gauge_fault_transfer_recovery_test -v
```

The tests verify the chosen finite operators and mathematical examples, not physical locality, implementation, source identity, full chat coverage or foundational necessity.
