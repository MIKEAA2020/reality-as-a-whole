# An autonomous cursor reads the transient support flag

## Result

This pass advances gate 2 of the [problem-of-time plan](PROBLEM_OF_TIME_DIVIDE_AND_CONQUER_PLAN.md). A **time-independent, bounded-below Hamiltonian** adds a massive moving cursor and a memory qubit to the [eight-flag support model](ZERO_TWO_WINDOW_REDUNDANT_FLAG_HOLD.md). A fixed position-dependent interaction lets the cursor read the flag as it passes; no external time-dependent on/off switch appears in that Hamiltonian.

For a specified compact cursor packet and the same continuum P/Q system and commutator certificate as before, we derive a uniform bound through a finite later interval. In illustrative units, for every initial P state and every initial Q state (including arbitrary logical-sector correlations):

```text
P state: probability of false memory record < 0.000343;
Q state: probability of missing the memory record < 0.000343.
```

The bound applies from after the interaction through the time at which the earlier comparator flags have almost returned to blank. It is an analytic error budget, **not a physical measurement**. An independent finite-grid chiral-comparator simulation sees the memory remain set while the flag resets; it does not simulate the full massive cursor.

This is a controlled construction for the **support question Q**, not yet an autonomously triggered geometry-crossing instrument, a clock-switch theorem or a complete solution of time. The reference scalar clock, packet, timing correlation, static interaction profile, flag coupling and memory are still specified resources. The clock-time interval is used for analysis; we have not constructed an independent reader of the memory or established its permanent retention. [Verifier](verification/zero_two_window_autonomous_cursor_reader_test.py).

## 1. The shared model and the new physical degrees of freedom

Keep the existing two-window system, its actual positive roots Ω_h and orthogonal packet projectors `P,Q=I−P`. As in the previous pass,

```text
Ω_h ≥ 1.3 I,       ||[Ω_h,Q]|| < c_* = 0.419/(2×1.3),
S_y = Σ_(j=1)^8 σ_y^(j),       F = I−|0…0⟩⟨0…0|.
```

F is the collective flag effect. The bound on the commutator comes from the [previous exact-rational continuum certificate](ZERO_TWO_WINDOW_CERTIFIED_SUPPORT_COMMUTATOR.md), not from a grid fit. Add a memory qubit M, initially `|0⟩`, and a cursor coordinate `x` with momentum `p=−i∂_x` on `L²(R,dx)`. Let

```text
H_h = Ω_h + B + p²/(2m)
      + g Q S_y + κ v f_b(x) F σ_y^M,
C_h = (p_φ² − H_h²)/2,         selected branch p_φ=H_h.
```

Use `N=8`, `g=100`, `κ=π/2`, `v=1`, `m=10^16`, and the dimensionless width `b=10^−6`. Tensor identities are suppressed. Define a fixed, nonnegative position profile

```text
f_b(x) = (15/(16b))(1−(x/b)²)²   for |x|≤b,
         0                         otherwise.
```

Its integral is 1, its first derivative is continuous, and its weak second derivative is integrable. Set

```text
B = Ng + κ v ||f_b||_∞ + 1
  = 800 + (π/2)×15/(16×10^−6) + 1 ≈ 1,473,422.56.
```

On the free cursor kinetic-energy domain, the remaining terms are bounded, so H_h is self-adjoint. Moreover

```text
H_h ≥ Ω_h + B−Ng−κv||f_b||_∞ ≥ 2.3 I.
```

Thus its positive square is well-defined, and the stated quadratic constraint and selected positive-frequency sector can be defined by spectral calculus. This **changes the constraint again**: the cursor and the reader are now inside it, not appended as an externally prescribed instantaneous measurement. The earlier scalar-clock physical representation is an assumption for this enlarged model; no full inhomogeneous gravity or autonomous measurement of φ is established.

The static profile f_b singles out a specified **relative cursor coordinate and interaction region**. Its mathematical localization in that auxiliary coordinate does not show that Q, the old apparatus or the interaction is local in physical spacetime. Q remains a globally specified packet projector. The offset B establishes positivity but is not automatically a physical energy expenditure; its physical meaning and any clock-momentum redefinition need independent analysis. The packet below has mean kinetic energy of order `mv²/2=5×10^15` in these model units—an extreme, deliberately idealized resource, not a practical detector design.

## 2. Prepared cursor and conditional timing

At `φ=0`, supply the factorized cursor state

```text
ψ(x) = exp(imvx) ψ_a(x+v t₀),
t₀=π/(2g),        a=10^−6,
ψ_a(z) = √[315/(256a)] (1−(z/a)²)² for |z|≤a, else 0.
```

It is normalized and belongs to the cursor H² domain. The original system may otherwise be an arbitrary state, including coherence across P/Q and correlations between h sectors; flags and memory start blank. Factorization of the cursor, its position/momentum and its synchronization relative to φ are **preparation assumptions**.

The comparator cursor of velocity v reaches the support of f_b between

```text
T_start = t₀−(a+b)/v ≈ 0.01570596,
T_end   = t₀+(a+b)/v ≈ 0.01570996.
```

Each point in its initial support crosses the center at `t_c=t₀−z/v`, which lies inside the high-flag window `π/(4g)<t_c<3π/(4g)`. Let `T_ret=π/g≈0.03141593`, the reading at which the old ideal flags return to blank. No assertion of a physical universal unit or a measured duration is implied.

## 3. Comparison A: massive cursor versus translated cursor

Conjugate by the prepared plane-wave phase. Apart from a common constant, the cursor kinetic operator becomes

```text
v p + p²/(2m).
```

Compare it to the *mathematical* chiral cursor with operator `vp`, retaining **the same** Ω_h, gQS_y and position-dependent reader interaction. The chiral comparison has an unbounded-below generator; it is not the physical model or a positive constraint. It is used to bound the actual nonnegative quadratic kinetic-energy evolution.

For a fixed initial cursor coordinate z the chiral cursor translates exactly and sees `f_b(z−vt₀+vφ)`. Its internal evolution `U_z(φ)` includes the full Ω_h and both interactions. Dependence on z enters only through the smooth pulse, so Duhamel differentiation gives the uniform bounds

```text
||∂_z U_z|| ≤ A₁ := κ ||f_b'||₁,
||∂²_z U_z|| ≤ A₂ := κ ||f_b''||₁ + A₁².
```

The integrals are along the cursor's monotone trajectory. For the specified profile,

```text
||f_b'||₁ = 15/(8b),       ||f_b''||₁ = 10/(√3 b²),
||ψ_a'||₂ = √3/a,          ||ψ_a''||₂ = √(63/2)/a².
```

Therefore, for any normalized initial original-system state, including an arbitrarily correlated h sector,

```text
||p² Ψ_chiral(φ)|| ≤ K₂
K₂ = √(63/2)/a² + 2(√3/a) A₁ + A₂.
```

Here p differentiates the *comoving envelope*. Duhamel's formula then bounds the difference between the actual massive cursor state and this chiral state, up to an irrelevant common phase:

```text
||Ψ_massive(T)−Ψ_chiral(T)|| ≤ T K₂/(2m).
```

The initial state lies in the needed domain; f_b has bounded weak first and second derivatives, so the derivative estimates apply to these wave packets. With `T≤T_ret`, `K₂≈3.35586×10^13` and the norm error is below `0.0000528`. This is a state-vector bound for the declared cursor preparation, not a diamond-norm estimate for arbitrary cursor states or arbitrary spatial profile.

## 4. Comparison B: noncommuting flag dynamics and the finite pulse

The original two-window evolution does not commute with Q. In an Ω_h interaction picture, the reader acts only on cursor/flags/memory and commutes with Ω_h. Thus the same certificate controls the error from replacing the evolved Q by Q during the **full reader interaction**:

```text
D_sys ≤ Ng c_* T_end²/2 < 0.01592.
```

This is a norm bound on the state up to T_end, including all flags, memory, cursor and both h sectors. It is not an assertion that Q is exactly conserved in the real model.

For the Q-fixed comparator, the cursor pulse is centered at t_c and has total area κ. Replace its finite-duration action by the mathematical instantaneous unitary

```text
W = exp(iκ F σ_y^M)
```

at t_c. It sends blank M to an orthogonal memory state when F=1, and leaves M blank when F=0. Since `||[gQS_y,F]||≤2gN`, comparing the interaction-picture F at different points of the pulse yields

```text
D_pulse ≤ 2κ gN b/v < 0.002514.
```

This instantaneous gate is only a **proof comparator**, not an externally implemented switch. Under the Q-fixed comparator the flags of a Q state at t_c have blank amplitude at most

```text
η_flag = [sin(g a/v)]^N < 10^−31,
```

because t_c lies within `a/v` of the half rotation. P states leave flags blank in this comparator. After the pulse the chiral cursor has passed the interaction region and the memory is a spectator; its measured probability is constant in the chiral comparison, even if the original flag later rotates back.

Combining the three norm errors at any `T_end≤φ≤T_ret`,

```text
ε = D_sys + D_pulse + T_ret K₂/(2m) < 0.01849,
false record on P ≤ ε² < 0.000343,
missed record on Q ≤ (η_flag+ε)² < 0.000343.
```

The bounds apply to a final memory measurement on **one preparation**; comparing different terminal readings requires separate copies. They cover arbitrary h correlations and all original P or Q states, with the fixed blank flags, memory and factorized cursor specified above. A bounded generator mismatch δ adds at most `T_ret δ` to the norm budget if a common comparison and appropriate domains are established; no experimental operator-norm calibration is claimed.

For a coherent general input with `λ=Tr(Qρ)`, the ideal cursor-averaged record probability is `s_eff² λ`, where `s_eff≥√(1−η_flag²)` for the specified packet. The state norm bound therefore gives

```text
|√q_M − s_eff √λ| ≤ ε,
λ ≤ min[1, ((√q_M+ε)/√(1−η_flag²))²].
```

The false/miss statements alone should not be used as if they implied this coherent-state formula; the latter follows from the full-vector comparisons and the orthogonal P/Q comparator sectors. A statistical confidence bound for q_M, preparation errors and real instrument mismatch must be added separately.

Before T_start the chiral comparator has not encountered the pulse, hence its memory remains blank. For the physical massive cursor, an early false record is bounded in amplitude by `T_start K₂/(2m)` under the same ideal preparation. The output memory `0` is a no-record outcome; outside this analysis it must not be equated with a physically demonstrated no-crossing event.

## 5. What the finite check does and does not show

The [verifier](verification/zero_two_window_autonomous_cursor_reader_test.py) checks the exact commutator thresholds and pulse/packet integrals, and evolves the *actual finite-grid Ω and Q* together with the flags and memory for three representative initial cursor positions in the chiral comparison. It verifies the memory probability after the pulse and at `T_ret`, with the reader coupling gone, and tests zero reader coupling as a negative control. Example at grid 4, h=0 and central cursor position:

```text
                        memory after read   memory at T_ret   flag at T_ret
one P input               0.000000371         0.000000371       0.000000886
one Q input               0.999999999         0.999999999       0.000000015
```

These are selected finite-regulator results, not worst-case bounds, physical data, or a numerical simulation of the unbounded massive cursor. The continuum norm estimate above supplies the claimed finite-duration uniform bound under its stated assumptions; the code checks its constants and separate ingredients rather than mechanically proving its functional analysis.

## 6. What is solved, and the next gate

**Progress:** the reader is part of the same explicitly changed constraint, is triggered by an internal cursor position rather than a prescribed function of φ, has a positive self-adjoint generator, treats coherent P/Q states, and stores the support result beyond the flag's return to blank for a proved finite interval. This is stronger than simply measuring the old flag at a hand-selected instant.

**Still supplied:** an ideal scalar clock, exact packet shape and synchronization, very large mass/momentum scale, state-independent static profile, global Q coupling, pure ready ancillas, chosen final memory effect and an analytically bounded implementation. The modeled memory is not proved stable forever; real massive-cursor tails and later recurrences are only controlled to the finite horizon. We have not shown the physical resource cost, thermal behavior, local Q implementation or an entropy arrow.

**Next:** build the complete memory/no-record instrument—including the post-measurement state and cursor/flag backreaction—and determine whether a genuinely distinct physical clock can trigger or describe the **same** event on a common domain. The original geometry-window history protocol is a different instrument and cannot be identified with this Q-support record by naming it “geometry time.” A physical clock-switch result and the user's deeper zero/experience constitution remain open.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_autonomous_cursor_reader_test \
 verification.zero_two_window_redundant_flag_hold_test \
 verification.zero_two_window_commutator_certificate_test -v
```

NumPy and SciPy are required. No full massive-cursor numerical simulation or laboratory experiment is claimed.
