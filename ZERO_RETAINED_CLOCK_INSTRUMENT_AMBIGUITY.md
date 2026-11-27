# Retaining the clock: a complete relational instrument and an ambiguity

**Continuation:** [fiber transport and the lost record](ZERO_CLOCK_FIBER_TRANSPORT_AND_LOST_RECORD.md) derives an exact connection between this particular enlarged instrument's retained dilation and the earlier scalar-smeared reduced map. A later [autonomous readout model](ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md) approximates the distinct L instrument defined below and corrects the original cursor carrier sign. The [clock poststate obstruction](ZERO_CLOCK_PROBE_POSTSTATE_OBSTRUCTION.md) shows that the original T operation has strictly positive clock-band leakage, whereas the subsequent band-compressed factorwise probe has none on the same initial clock packet; probability agreement cannot identify these operations. A later [POVM and smearing recheck](ZERO_SECOND_CLOCK_POVM_TAIL_AND_SMEARING_RIGOR_REVIEW.md) verifies the weak normalization and selected dilation steps, while preserving this effect-versus-instrument distinction. None of these results supplies a physical R-relative frame switch.

## Result

The [previous two-clock construction](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) established a normalized, constraint-invariant **effect** for the same cursor-memory outcome relative to a second quantum clock R. It also defined one reduced-output convention after discarding clock information. This pass keeps the clock and original apparatus in the output and constructs an explicit complete instrument on that enlarged physical initial-data space.

The key result is a **specific obstruction to the next shortcut**: a clock-neutral event effect and its probabilities do not determine the state of the retained clock, cursor and memory after the event. We exhibit multiple complete instruments with exactly the same effects and, in a finite cyclic control, the same certain outcome but retained poststates at trace distance **0.5** or **1**. One instrument preserves clock-time coherence; another discards it; an outcome-dependent clock shift changes the retained output without changing the already recorded event probability.

This does not prove that clock switching is impossible. It says a genuine same-instrument comparison must carry the **measurement operation and its hidden records**, not just the POVM, a conditional probability or an arbitrarily chosen reduced-output convention. The new operations are mathematical instruments, not derived local apparatuses, and the finite control is not a simulation of the full massive-cursor continuum. [Checks](verification/zero_two_window_retained_clock_instrument_test.py).

## 1. The same physical input and event effect

Retain the prior positive-frequency physical initial-data space

```text
H_phys = H_A ⊗ H_R,
H_R = L²([0,∞),dk),        K_R ψ(k)=kψ(k),
H_tot = H_A ⊗ I + I ⊗ K_R,
U(t)=exp(i H_tot t).
```

Here H_A is the **actual** preceding two-window system plus massive cursor, eight flags and record memory, including both h sectors. It is self-adjoint and bounded below. R is the added semibounded independent clock, and E_R(B) is its finite-bin covariant POVM effect for an interval B of length ℓ>0. Let Π_m, m=0,1, be the same existing memory projectors. Both act on the full tensor space with the appropriate identities.

The previous clock-neutral memory effects are

```text
F_m = (1/ℓ) ∫_R dt U(t)† [Π_m ⊗ E_R(B)] U(t),
F_0+F_1=I,       [F_m,H_tot]=0.
```

The integral is weak, and the equalities use the positive-clock POVM covariance and `Σ_m Π_m=I`. Thus F_m are positive contractions and gauge-invariant event effects for the declared branch/representation. The formula does not say that every apparatus capable of producing those effects has the same state update. Nor does adding R derive the clock, its POVM, a real detector or physical gravity from zero.

## 2. A fully specified retained-output instrument

Choose the following **one** clock-neutral measurement protocol. At orbit parameter t use the product Kraus operator

```text
A_m = Π_m ⊗ √E_R(B),
K_m(t) = ℓ^(−1/2) U(t)† A_m U(t).
```

Define the outcome operation on positive trace-class physical initial-data operators by

```text
T_m(ρ) = ∫_R dt K_m(t) ρ K_m(t)†.
```

The integral is over an **unobserved** continuous label in this specified instrument, not a normalized flat probability over t. The positive trace integrals are finite, since

```text
Σ_m ∫ dt K_m(t)†K_m(t) = Σ_m F_m = I.
```

Standard Stinespring construction takes `Vψ` to the function `(m,t)↦K_m(t)ψ` in `C²⊗L²(R,dt;H_phys)`. The displayed completeness makes V an isometry. Keeping m but tracing the t-label supplies T_m; its sum is trace-preserving. The full **R clock, cursor, flags and memory remain in H_phys**; the auxiliary t-label is a mathematical environment/record resource and has not been engineered as an internal physical subsystem.

By construction

```text
Tr[T_m(ρ)] = Tr(ρ F_m).
```

For the previous product R preparation, these are the very same correctly smeared scalar-clock memory probabilities. The instrument is covariant under joint U(s) evolution: shifting t in its integral gives

```text
T_m(U(s)ρU(s)†) = U(s)T_m(ρ)U(s)†.
```

The individual K_m(t) need not commute with H_tot. Covariance of the whole operation is not a demonstration that a physical observer can autonomously implement it or that each unobserved t-label is a gauge-invariant event. `U(t)†` transports the selected operation back to one common anchor in this mathematical representation; it is not a claim that a real device physically reverses the universe.

This gives a complete retained-output instrument, but it **chooses** a Lüders square root for the finite-bin clock effect and discards the t-label. Other dilations and output conventions are possible. In particular, the earlier scalar-slice reduced map was a specified mixture after discarding reference information; its output state has not been proved equal to `Tr_R,cursor,flags T_m(ρ)` under a fully constructed clock-switch map. Equality of their outcome probabilities does not prove equality of those operations. The [subsequent derivation](ZERO_CLOCK_FIBER_TRANSPORT_AND_LOST_RECORD.md) shows exactly how the earlier map follows from the retained dilation **after** a fiber-dependent scalar-slice identification and the specified partial traces; it does not identify it with the raw anchor marginal or establish a physical R-relative switch.

## 3. Two more instruments with the same event probabilities

The physical effects alone also define a coherent square-root instrument

```text
L_m(ρ)=√F_m ρ √F_m.
```

Since `Σ_m F_m=I`, its sum is a channel. The functional calculus gives `[√F_m,H_tot]=0`. This is an abstract **relational Lüders instrument**, not the previously derived microscopic cursor mechanism.

For a fixed nonzero real s, define an outcome-specific R-clock feedback unitary

```text
W_s = exp(i s K_R),
G_0(ρ) = W_s L_0(ρ) W_s†,       G_1(ρ)=L_1(ρ).
```

W_s commutes with H_tot and the selected constraint; its effect is a clock translation in the R POVM. Both L and G are complete CP instruments, and

```text
Tr L_m(ρ) = Tr G_m(ρ) = Tr T_m(ρ) = Tr(ρF_m)
```

for every input and both outcomes. The clock translation is applied **after** the event reading and does not change the already recorded m. It is an explicitly different operation and may require physical resources. Consequently its later clock state, and generally later joint predictions, need not agree.

For the actual continuum R clock this difference is not merely hypothetical. Let an outcome m=0 have nonzero probability and let σ be its normalized poststate under L. R momentum k has absolutely continuous spectrum on `[0,∞)`. By the Riemann–Lebesgue lemma, `W_s→0` weakly as `|s|→∞`: the relevant inner products are Fourier transforms of L¹ functions of k. For any trace-class density σ, choose a finite-rank projector P with `Tr(Pσ)>1−ε`. Weak convergence and trace-class approximation imply

```text
Tr[P W_s σ W_s†] → 0.
```

The two-outcome test P versus I−P therefore makes

```text
D_trace(σ, W_s σ W_s†) → 1  as |s|→∞.
```

Thus the **same** nonzero event outcome probability can be followed by retained physical states that become arbitrarily distinguishable. This is an existence result for two specified abstract operations; it does not identify which one the actual cursor device implements, show a local clock-shift interaction, or make an arbitrary large shift inexpensive. The limit is stronger than needed to establish nonuniqueness, and it is not a claim that changing clock descriptions itself causes such a shift.

## 4. Explicit finite cyclic counterexample: hidden time versus coherence

The verifier supplies an independent finite control using the **actual prior two-window projector Q**, but it replaces the continuum Ω/cursor dynamics with the following expressly different finite cyclic model. It is not a full-continuum simulation:

```text
H_A,finite = H_old,grid ⊗ C²_memory,     H_R,finite = C⁴,
U_A = P⊗I + Q⊗X,        U=U_A⊗S,
S|r⟩=|r+1 mod 4⟩,       U⁴=I.
```

With clock bin `|0⟩⟨0|`, the four orbit terms Γ_(m,t) are mutually orthogonal projections for fixed m, and

```text
F_m = Σ_(t=0)^3 Γ_(m,t),      Σ_m F_m=I,      [F_m,U]=0.
```

The time-label-discarding instrument is `T_m(ρ)=Σ_t Γ_(m,t)ρΓ_(m,t)`; the coherent Lüders instrument is `L_m(ρ)=F_mρF_m`. Both have effect F_m.

Prepare the actual model's P packet, blank memory, and the coherent R state

```text
(|0⟩+|2⟩)/√2.
```

For both instruments, outcome m=0 has probability **1**. Yet L leaves this clock coherence intact, whereas T dephases the two orbit labels. Their normalized retained-output states have

```text
D_trace(post_L,post_T)=1/2.
```

A clock shift S applied after the same m=0 outcome moves the clock support to the orthogonal span of `|1⟩,|3⟩`, giving

```text
D_trace(post_L,post_feedback)=1.
```

Both operations still report the identical outcome with certainty. The fine-grained operation is idempotent on this particular state; this is a concrete loss of **accessible clock coherence when its orbit label is discarded**, not evidence that all autonomous clocks behave this way or that there is a fundamental thermodynamic arrow.

The finite test checks normalization, covariance, the actual finite Q projector, same effects, both trace distances and a dephasing control. It does not test a semibounded continuous clock, the massive cursor, an experimental clock, or the general analytic limit above.

## 5. What must be done next

The preceding probability identity remains correct under its assumptions. This pass clarifies why it was **not yet** a transformation of the complete event:

1. Pick or derive one physically implementable clock-readout dilation and one explicit treatment of its outcome/hidden environmental records; identify the actual retained output algebra.
2. Starting from the **same** physical preparation and operation, construct its scalar-relative and R-relative descriptions, including the quantum φ/R/cursor correlations. Give an explicit map on the retained output state or show exactly what is inaccessible.
3. Test equality of the full joint statistics of **subsequent** measurements, not only the earlier m outcome. If a reduction has thrown away coherence, a universally invertible state switch is not justified; retaining the environment or restricting the desired observable algebra may instead suffice.
4. Include clock-backaction and finite bin width; analyze an interacting or turning clock. Distinguish its no-reading and repeated-reading outcomes and where clock charts overlap.

Neither the time-label-discarding T, the abstract Lüders L nor the feedback G has been shown to be the actual implementation of our massive-cursor measurement. The Q projector remains global, the clock and state are supplied, and the constrained toy model does not establish full gravity, actual cosmic zero, an entropy arrow or experience. The user's deeper constitutive goal remains the reason for pursuing the physical link, not a conclusion already supplied by these maps.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_retained_clock_instrument_test \
 verification.zero_two_window_second_clock_test \
 verification.zero_two_window_cursor_instrument_test -v
```

The tests check the explicitly defined finite control and earlier clock/instrument calculations. The continuum instrument's completeness and the Riemann–Lebesgue distinguishability argument are operator statements under the assumptions given above, not conclusions obtained solely from the finite test.
