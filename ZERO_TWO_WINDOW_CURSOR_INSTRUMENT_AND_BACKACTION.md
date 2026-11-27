# A complete instrument for the autonomous cursor—and its backaction

**Continuation:** [a second physical clock](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) adds a semibounded quantum reference and constructs a normalized clock-neutral effect for this same memory, plus a finite-resolution reduced-instrument comparison. It does not yet establish the transformation of all retained postmeasurement clock and cursor correlations.

**Cursor-sign correction:** the carrier in the underlying [cursor construction](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) must be `exp(−imvx)` with its stated `exp(iHφ)` evolution; the old written sign sent the packet away from the reader. The bounds here apply to that corrected preparation. See [the sign check](ZERO_AUTONOMOUS_CLOCK_EVENT_READOUT.md).

## Result

The [previous construction](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) gave an autonomous cursor that records whether the initial state lies in the selected P or Q sector. This pass promotes that readout to a **complete two-outcome quantum instrument**, including the conditional postmeasurement states of the original interacting system. It derives a uniform continuum comparison with a specified ideal P/Q projective instrument and checks the comparison on the existing finite-regulator system.

For all original-system inputs, including coherent P/Q superpositions and arbitrary untouched references, and for the previous fixed cursor and ready-ancilla preparation:

```text
half-diamond distance between the actual recorded instrument
and the specified ideal instrument < 0.0662
```

through the specified retention interval. Equivalently, the full diamond-norm difference is below 0.1324. This is a conditional mathematical bound, not an experimentally certified apparatus. It is **weaker** than the previous `0.01849` amplitude bound for record probabilities because it controls the entire postmeasurement state up to the later reading, not just whether the memory is set.

The comparison exposes an essential physical cost: on an equal coherent P/Q superposition, the ideal measurement's reduced poststate differs from the corresponding unmeasured reference state by trace distance 1/2. The actual instrument differs by at least `0.5−0.0662>0.4338` under the stipulated model. A reliable record of the support alternative is therefore **not nondisturbing** for that superposition. This is ordinary quantum measurement backaction in this model, not an entropy arrow or a new universal uncertainty law.

This completes the mathematical instrument **within a specified scalar-clock model**. A genuinely different physical clock, locality, real resources and permanent record retention remain open. [Checks](verification/zero_two_window_cursor_instrument_test.py).

## 1. Specify the experiment and its two operations

Use exactly the previous positive self-adjoint H_h, positive-frequency constraint, `N=8`, `g=100`, massive cursor packet and memory initialization, as specified in [the cursor construction](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md). The physical scalar reading is denoted T, with

```text
T_end ≈ 0.01570996,      T_ret = π/100 ≈ 0.03141593,
T_end ≤ T ≤ T_ret.
```

Let `H_S` denote the **complete prior system**, including the geometry, pointer, old memories and both logical h sectors. P and Q are its two-packet projector and complement, and Ω is the block-diagonal direct sum of Ω_h. A fresh cursor, flags and record memory are initially in the pure state `|anc₀⟩`. For an input state on H_S define the exact isometry

```text
V_T |ψ⟩ = exp(iH T)(|ψ⟩ ⊗ |anc₀⟩).
```

Let Π_m be the memory-z projector for m=0 or 1. The exact recorded output, before discarding cursor/flags/memory, is

```text
J_m(ρ) = Π_m V_T ρ V_T† Π_m.
```

The physical experiment as specified in this pass **retains m but discards the cursor and flags** when describing the original-system output:

```text
I_m(ρ) = Tr_(cursor,flags,memory) J_m(ρ).
```

Each map I_m is completely positive and trace-nonincreasing; their sum is trace-preserving. Thus

```text
p(m)=Tr I_m(ρ),             Σ_m p(m)=1,
ρ_m=I_m(ρ)/p(m)             only when p(m)>0.
```

This includes no-record m=0, the record m=1, and all their postmeasurement disturbances. It neither defines m=0 as a geometry no-crossing event nor claims that the readout happens without a later physical memory interrogation. Conditional results for zero-probability events are undefined; we do not discard and silently renormalize failures. Retaining the other degrees of freedom is also allowed via J_m; tracing them is an explicit restriction, not a claim that they cease to exist.

## 2. The ideal instrument being compared

The intended question is the original **initial-state support** P versus Q, not whether a geometry has crossed a surface. Define

```text
P₀=P,   P₁=Q,   U₀(T)=exp(iΩT),
L_m,T(ρ) = U₀(T) P_m ρ P_m U₀(T)†.
```

This is an ideal Lüders support measurement at the preparation reference, followed by the original Ω evolution. It is **a comparator**, not an extra gate physically applied to the actual system. The original system's output is a full density matrix, not just a click probability. U₀ includes both h sectors and their coherent relative phases.

The comparator does not claim that a Q measurement is local, a clock event, or geometrical first crossing. The added cursor/flag Hamiltonian changes the constraint and state, so the comparison is not a passive coordinate change. The preparation identification and common H_S are specified through the same P, Q and Ω operators.

## 3. A uniform postmeasurement error bound

We make explicit the state-level comparison that the previous report used only to bound memory probabilities.

1. Replace the massive cursor by the chiral comparison. On the fixed normalized cursor preparation, the full state-vector error at T is bounded by `T K₂/(2m)`, with the previous `K₂≈3.35586×10^13`.
2. Replace the evolved Q coupling by fixed Q **through the whole interval to T**. The old commutator certificate and Duhamel give `Ng c_* T²/2`, including after the cursor pulse. This is crucial: stopping this bound at T_end would suffice for the memory probability, but not generally for the **full original-system state** at the later T.
3. Replace the finite pulse by a controlled gate at each cursor-coordinate crossing. The previous bound is `D_pulse≤2κgNb/v`.

The Q-fixed comparator can be written as an isometry whose P input produces a blank memory and whose Q input has a small blank component of norm at most

```text
η = [sin(ga/v)]^N < 10^−31.
```

Its Q-record environmental state is otherwise independent of the original-system input. Normalize that record environmental state and replace the tiny Q/blank component by zero. The resulting isometry has **exactly** the two reduced operations L_m,T. The normalization changes the isometry norm by at most `√2η`. This construction retains the cursor-dependent environmental state rather than assuming the flag or cursor are unaffected.

Combining the bounds for every T in the interval yields

```text
δ(T) = Ng c_* T²/2 + 2κgNb/v + T K₂/(2m) + √2η,
δ(T_ret) ≈ 0.06618698 < 0.0662.
```

The same vector bound holds after tensoring an arbitrary reference: each estimate is uniform on the original-system factor. For pure inputs with a reference, the trace distance between two normalized output states is no larger than their vector-norm distance; mixtures follow by convexity. Dephasing into the classical m register and tracing flags/cursor cannot increase trace distance. Hence the exact recorded instrument channel

```text
C_I(ρ) = Σ_m |m⟩⟨m| ⊗ I_m(ρ)
```

and the corresponding ideal channel C_L satisfy

```text
(1/2) ||C_I−C_L||_diamond ≤ δ(T_ret) < 0.0662.
```

The diamond norm here is over H_S and arbitrary untouched references, **with the cursor and ready ancillas fixed as specified**. It is not a bound over arbitrary cursor states, arbitrary unknown apparatus Hamiltonians or all gravitational theories. It also does not prove the ideal instrument itself is physically local. The common phase from the cursor carrier and B is irrelevant to channel predictions.

For a specified input, write `p_m=Tr I_m(ρ)` and `p_m^0=Tr(P_mρ)`. The same joint-output bound implies `|p_m−p_m^0|≤δ`. If `p_m^0≥κ>δ`, then p_m is nonzero and a conservative conditional-state bound is

```text
D_trace(I_m(ρ)/p_m, L_m,T(ρ)/p_m^0) ≤ min(1, 2δ/κ).
```

Thus rare branches cannot be assumed accurate merely because the unconditioned channel is close. Additional statistical, preparation and implementation errors must be accounted for separately.

### Why the stronger full-state bound is larger

At T_ret, the new dynamical term is approximately `0.063621`; pulse and dispersion terms add about `0.0025133` and `0.0000527`. For memory probability alone the earlier argument stops the noncommutation comparison at T_end because the comparator's memory becomes a spectator after the pulse. That gives the smaller `0.01849` bound. The full original-system state continues to evolve and can accumulate additional Q/Ω mismatch. The two bounds answer different operational questions and must not be substituted for each other.

## 4. Quantified backaction

Choose normalized, orthogonal `|p⟩∈P H_S` and `|q⟩∈Q H_S`, and prepare

```text
|+⟩=(|p⟩+|q⟩)/√2.
```

Without the specified support measurement, the comparator reference state is `U₀|+⟩⟨+|U₀†`. If the ideal record outcome is ignored, the measured state is

```text
U₀ (|p⟩⟨p|+|q⟩⟨q|) U₀† /2.
```

Their trace distance is exactly 1/2. Contractivity of partial trace and the uniform instrument bound imply that the actual nonselective original-system output has trace distance at least

```text
1/2−δ(T_ret) > 0.4338
```

from that no-support-measurement comparator. This is a concrete, state-specific lower bound on disturbance in the **modeled comparison**. It is not a statement that all Q detectors disturb all observables equally, a lower bound on heat, or a proof that irreversibility is fundamental. The full joint evolution is unitary and retains correlations with apparatus degrees of freedom.

By contrast, on an initial state supported entirely in P or entirely in Q, the ideal system output is simply U₀ρU₀†, while the flag outcome has a definite value. The actual joint channel is within δ of that ideal output. Thus the difficulty is especially visible for coherent cross-sector inputs; it is not resolved by testing only the two sector endpoints.

## 5. Finite-regulator checks

The new [test module](verification/zero_two_window_cursor_instrument_test.py) uses the old two-window Ω and Q at grid 4, all nine symmetric-flag basis states, the explicit memory, and a central chiral cursor trajectory. It integrates the actual position-triggered pulse, retains both output branches and traces flags to calculate poststates. It checks completeness/positivity on a two-input span, coherent and mixed inputs, the no-reader negative control and the actual poststate disturbance. The continuum proof above, not the grid, supplies the stated uniform guarantee; the code does **not** simulate the full massive cursor or establish real-world accuracy.

For one equal P/Q superposition at h=0, illustrative finite-grid results are:

```text
record probabilities (m=0,m=1)  ≈ (0.5000024, 0.4999976),
joint-output trace distance to ideal ≈ 0.0010324,
actual reduced-system disturbance  ≈ 0.5000012,
ideal reduced-system disturbance   = 0.5.
```

These selected-state values are much smaller than the uniform comparison bound but do not replace it. The calculation includes the finite pulse and post-pulse evolution; it assumes a single comparator cursor position rather than integrating a physical cursor wavepacket.

## 6. The next frontier: an actual second clock

The instrument now has a complete operational definition and a conditional state/backaction guarantee. The remaining step is not simply to express I_m in a second basis. Construct a **distinct physically specified clock** in the same enlarged constraint, including its measurement or finite-resolution conditioning, and identify the *same* support event and complete instrument. Prove equality or a finite error bound for joint outcome and poststate statistics on their common domain, with no-reading and turning/ambiguity outcomes retained.

The cursor position is a natural candidate but is itself quantum and interacts with the reader. A bare cursor-position projector is not automatically a Dirac observable, and measuring it can disturb the transfer. A proof must define the physical relational event, not reuse the scalar-clock schedule under a different name. The original geometry-window/record instrument is likewise a different experiment until an explicit map is constructed. Physical locality, realistically bounded resources, long-term memory, full gravity, the zero-energy recovery map and lived succession remain separate obligations.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_cursor_instrument_test \
 verification.zero_two_window_autonomous_cursor_reader_test \
 verification.zero_two_window_redundant_flag_hold_test \
 verification.zero_two_window_commutator_certificate_test -v
```

NumPy and SciPy are required. The code checks the finite model and analytic constants; it is not a numerical proof of the full massive-cursor continuum estimate or an experimental validation.
