# A second quantum clock for the same autonomous record

**Continuation:** [the retained-clock instrument analysis](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md) constructs an explicit normalized clock-neutral instrument on the enlarged physical space and demonstrates that the same clock-neutral effects can have different retained poststates. It does not identify a unique physical realization or complete the clock switch.

## Result

The preceding [cursor instrument](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md) was formulated relative to a scalar clock φ. Here we add a **distinct physical quantum clock R** to that same instrument, extend the constraint explicitly, and compare the same memory outcome against its R reading. The R clock has a semibounded Hamiltonian and a finite-resolution covariant POVM; it is not a second name for φ.

For one specified clock state and one finite reading bin, we construct a normalized, clock-neutral **joint memory/clock effect**. Its memory probabilities are exactly those of the same scalar-clock instrument averaged with a calculated clock-resolution kernel. No time-dependent switch, flat normalized prior over an infinite clock, or dropped outside-window outcomes is used in that probability identity.

A separately specified reduced-output convention gives a complete two-outcome instrument for the same kernel. For that convention, the full recorded channel differs from the earlier ideal support instrument at the bin center by less than **0.0394 in half-diamond norm**, including a bound for clock tails and the earlier cursor/flag backaction. This is conditional on the model and the chosen preparation; it is not a proof that all independently constructed clock quantizations are equivalent or that this reduced-output convention is a canonical quantum reference-frame switch.

The construction is a meaningful two-clock **comparison**, but not the full gate in the [research plan](PROBLEM_OF_TIME_DIVIDE_AND_CONQUER_PLAN.md): R is an additional noninteracting ideal clock, its preparation and POVM are supplied, and a physical measurement realization and general transformation of retained clock/φ/cursor poststates remain open. It does not solve the problem of time. [Checks](verification/zero_two_window_second_clock_test.py).

## 1. One changed constraint containing both clocks and the same apparatus

Let H be the **actual positive Hamiltonian of the prior massive-cursor, flag, memory and two-window system**, including both h sectors. Add

```text
H_R = L²([0,∞), dk),         K_R ψ(k)=k ψ(k),
H_tot = H ⊗ I_R + I ⊗ K_R,
C_new = [p_φ² − H_tot²]/2,       positive-frequency branch p_φ=H_tot.
```

H and K_R act on separate factors, strongly commute, are self-adjoint and bounded below; H remains positive as proved previously. Thus the positive-frequency root and scalar-φ evolution exist on their natural spectral domains. This is a **further changed constraint** with an extra clock, not an assertion that the original Hamiltonian already contained R. The decoupled addition preserves the old apparatus's H evolution at fixed φ but adds a new prepared degree of freedom, its energy spectrum and a measurement. Its physical realization and gravitational energy accounting are not derived.

The R clock has positive frequencies k and a covariant time POVM E_R on the real line, defined weakly by

```text
⟨ψ|E_R(dr)|ψ⟩ = |∫₀∞ e^(−ikr) ψ(k) dk|² dr/(2π).
```

Plancherel gives `∫_R E_R(dr)=I`. This is a POVM on a semibounded frequency space, **not** a self-adjoint canonical time operator or a sharp position PVM on all real times. For `U_R(t)=exp(iK_R t)` its distribution translates: a state β has density `w(r−t)` after scalar evolution t. A Naimark dilation can mathematically implement this POVM; a local physical implementation or an apparatus energy budget is not supplied.

## 2. One genuine shared event and an exact clock-neutral effect

Write Π_m for the **same** previously defined record-memory projector, and let `U_H(t)=exp(iHt)` and `U_R(t)=exp(iK_Rt)`. Fix a reading bin `B=[r−ℓ/2,r+ℓ/2]`, with `ℓ>0`, and define the weak operator integral on the selected physical initial-data Hilbert space

```text
F_(m,B) = (1/ℓ) ∫_R dt [U_H(t)† Π_m U_H(t)]
                              ⊗ [U_R(t)† E_R(B) U_R(t)].
```

This is not an integration over distinct experimental interventions: it is the specified invariant relational effect for asking **what the same memory reads when R is in B**. It is positive, and the clock covariance identity

```text
(1/ℓ) ∫ dt U_R(t)† E_R(B) U_R(t) = I_R
```

holds weakly. Consequently `Σ_m F_(m,B)=I`. Each positive effect is bounded by I, and shifting the integration variable shows that F_(m,B) commutes with the simultaneous H+K_R evolution. On the selected linear constraint branch this supplies a corresponding constraint-invariant physical effect. The bounded integral is defined via its positive quadratic form; no normalizable uniform distribution on φ is claimed.

Prepare R independently in the specified normalized β, while the previous cursor, flag and memory have their previous ready states. If `p_m(t)` is the **same** scalar-clock memory probability from the original autonomous instrument at φ=t, then

```text
Pr(m | R in B) = ∫_R dt w_B(r−t) p_m(t),
 w_B(u) = (1/ℓ) ∫_(−ℓ/2)^(ℓ/2) w(u+s) ds,
 ∫ w_B(u) du = 1.
```

This follows by evaluating F on that product preparation. It is an exact identity for the **specified POVM and physical state**, including t outside the prior retention window. The integral kernel is a real clock-resolution distribution, not an arbitrary uniform probability of cosmic time. It is not valid unchanged for arbitrary initial correlations between R and the original apparatus.

The two m outcomes include no-record and record. The decomposition of the integral into inside/outside the earlier retention window is used below for a bound; **outside is not asserted to be an observed third outcome**. To label it operationally would require a separate φ-related measurement and its backaction.

## 3. A specified reduced-output instrument—not a free frame switch

The prior scalar description has CP outcome maps I_m,t on the original system, after retaining m and discarding cursor/flags/memory. Define the following R-conditioned reduced-output convention:

```text
J_(m,B)(ρ) = ∫_R dt w_B(r−t) I_m,t(ρ).
```

These maps are CP and their sum is trace-preserving; their outcome probabilities are exactly the F_(m,B) probabilities for the declared product clock state. Mathematically this is the output obtained by using the specified scalar-slice identification for the original-system output, conditioning on the R effect, and discarding the scalar-time label and the added clock. It is a **declared reduction/partial trace**, not a demonstrated unitary transformation between independently quantized clock theories. Retaining φ, R and cursor correlations, or choosing different subsystem identifications, is a different postmeasurement problem. The clock-neutral probability effect above is not by itself a unique specification of every possible measurement backaction.

This distinction matters: R reading is genuinely unsharp, so its reduced poststate is generally a mixture of states at different scalar readings. It cannot simply be declared equal to the sharp scalar-t poststate. The code includes a separate two-level control where the difference is large. The present construction proves equality to the correctly **smeared** scalar description, not equality to an incorrectly matched sharp experiment.

## 4. A finite-resolution clock and error budget

Use the normalized compact frequency packet

```text
β(k) = b^(-1/2) cos[π(k−k₀)/(2b)]  for |k−k₀|≤b, else 0,
k₀=10000,       b=5000.
```

It lies entirely in k>0. Its finite time-resolution density w has mean 0 and variance `π²/(4b²)` by Plancherel and the square-integrable derivative of β. Choose

```text
r = (T_end+T_ret)/2 ≈ 0.023562945,
ℓ = 0.0001,
σ_B² = π²/(4b²) + ℓ²/12,      σ_B ≈ 0.000315483.
```

All numbers are illustrative dimensionless units. A bin effect has nonzero width; individual exact r outcomes are densities, not positive-probability point outcomes.

For the window `I=[T_end,T_ret]`, let `d=min(r−T_end,T_ret−r)` and `Y=b(d−ℓ/2)`. Our choice has `Y≈39.015>π/2`. The packet's Fourier amplitude is proportional to

```text
π cos(y) / [(π/2)²−y²],        y=b u,
```

with removable singularities. Integrating its simple envelope gives the conservative, explicit two-tail bound

```text
Pr_(w_B)(t∉I) ≤ τ_B := π/[3Y³(1−(π/(2Y))²)²] < 0.0000177.
```

This bound does **not** say a particular outside-window event was detected or discarded. All tail contributions remain in J; we bound their worst possible effect by their total probability.

Let `L_m,r(ρ)=e^(iΩr) P_mρP_m e^(−iΩr)` be the earlier ideal support instrument at r and let C_J,C_L be the corresponding classical-record channels. Write the earlier pulse/dispersion constants as

```text
D_pulse = 2κgNb/v,
D_disp(t) = t K₂/(2m),
c_* = 0.419/(2×1.3),       ||Ω|| ≤ ω_* := √(49/6+7.2/π).
```

Inside I the prior full-state comparison gives

```text
δ(t) ≤ Ng c_* t²/2 + D_pulse + D_disp(t) + √2η.
```

Changing the **ideal** output time from t to r costs at most `ω_*|t−r|` in half-diamond distance. Convexity, the full tail bound, `E[t²]=r²+σ_B²` and `E|t−r|≤σ_B` give

```text
(1/2)||C_J−C_L(r)||_diamond ≤
  Ng c_*(r²+σ_B²)/2 + D_pulse + K₂(r+σ_B)/(2m)
  + √2η + ω_*σ_B + τ_B
  < 0.0394.
```

The omitted tails are bounded as possible **worst-case channel differences**, not set to zero. The bound applies to the fixed cursor and R-clock preparations, arbitrary original-system states and arbitrary untouched references; it does not apply to arbitrary unprepared clock states. The previous `0.0662` bound is a uniform supremum at the end of the retention interval; this smaller value is an **averaged, different-comparison** bound with new clock assumptions, not an improvement of that original worst-case bound.

For memory probabilities alone, using the preceding `0.01849` bound in I plus the tail gives

```text
|Pr(m|R in B) − Tr(P_mρ)| < 0.01851.
```

This is an absolute event-probability bound, not a guarantee for rare normalized postselected branches. On P-only or Q-only inputs the earlier sector-specific probability bounds can be combined separately with τ_B. Finite calibration errors, clock-state deviations, timing drift, model mismatch, output-trivialization errors and nonlocal implementation are **not** included unless independently bounded.

## 5. Numerical control and what it means

The [test module](verification/zero_two_window_second_clock_test.py) checks the clock-packet norm, variance, tail envelope and error-budget constants. On the actual small-grid two-window Ω and Q it evaluates the **same** chiral-comparator autonomous instrument at nine scalar readings near r and takes a normalized quadrature-weighted mixture. For one coherent equal P/Q input, that selected-state calculation gives record probabilities approximately `(0.5000024,0.4999976)` and a joint-output trace distance about `0.000760` from the ideal comparator.

This finite test uses a truncated, normalized quadrature around r and the central comparator cursor; it does not numerically evaluate the full clock tails, the massive cursor, an experiment or the diamond norm. The analytic bound treats all tails and arbitrary original-system inputs under the fixed preparations. Numerical agreement is a control, not proof of a continuum clock-switch theorem.

A separate qubit control demonstrates why the smearing is not cosmetic: for an energy gap equal to the clock packet bandwidth, the clock-kernel characteristic function is `1/π`, not 1. In that case replacing the R-conditioned mixture by a sharp reading changes the coherence substantially. This control is a different simple system, not an assertion that the present old-system gap is of that size.

## 6. Status and next work

**Accomplished:** one explicit positive-frequency constrained model contains the prior autonomous support instrument and a second semibounded quantum clock; a normalized physical memory/clock effect compares the same event, and its probabilities equal the scalar description with the required kernel. A chosen reduced instrument has a finite complete-channel error bound, with clock tails and backaction retained in the accounting.

**Not accomplished:** the R clock is independent of the old system and is inserted as an additional resource. Its POVM and preparation are assumed; it does not serve as a geometry-triggered device or derive locality. The scalar clock remains an ideal reference; the clock-neutral event construction does not prove equivalence of independently quantized reductions, provide a unique clock-switch map on the retained φ/R/cursor output, or address turning clocks, arbitrary refoliation and full gravity. A different preparation or interactions between R and the apparatus need their own analysis. Nothing here identifies the constraint with actual whole energy or derives a subject, lived succession or the self-sufficient constitution.

**Next discriminating target:** retain R, φ and the cursor through an explicit clock-reading instrument, and construct or bound the actual transformation of the **same** joint postmeasurement state between scalar- and R-relative descriptions. Include clock backaction and failures. In parallel test an interacting or turning clock rather than assuming the added R clock remains a spectator. Only then promote this restricted comparison toward a genuine operational clock switch.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_second_clock_test \
 verification.zero_two_window_cursor_instrument_test \
 verification.zero_two_window_autonomous_cursor_reader_test \
 verification.zero_two_window_commutator_certificate_test -v
```

The prior constraints, clock POVM, positive-frequency inner product, cursor preparation and measurement/trace conventions are explicit assumptions. This document makes no novelty claim for covariant clock POVMs or relational averaging; the cited prior literature and earlier repository clock constructions remain relevant.
