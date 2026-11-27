# A controlled autonomous flag window in the existing time model

**Continuation:** [an autonomous massive-cursor reader](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) transfers this flag into a memory within a further explicitly changed constraint, with a finite-horizon continuum error bound. It does not prove permanent retention or solve clock switching.

## Result

The [work plan](PROBLEM_OF_TIME_DIVIDE_AND_CONQUER_PLAN.md) starts by addressing a concrete failure: the prior support flag can almost completely unflip after its optimal reading. Here we keep the existing two-window continuum system, its packet support projector and its certified commutator, and **change the constraint explicitly** by adding eight coupled flag qubits. Under the specified assumptions the flags collectively provide a wider, guaranteed finite readout window:

```text
π/400 ≤ φ ≤ 3π/400,
false-flag probability < 0.0013 on every initial P state,
missed-flag probability < 0.0097 on every initial Q state.
```

The bounds hold throughout the entire interval, not merely at sampled endpoints, and include arbitrary superpositions within each sector and both logical h sectors. There is also a coherent-leakage inference formula. The interaction is time-independent with respect to the scalar-clock description: no hand-switched pulse is inserted. But choosing a reading within the window is still an **external protocol assumption** in this pass; no physical reader, autonomous stop, local coupling or durable memory has been supplied.

Indeed the same model guarantees that at the later reading `φ=π/100` the flag is again almost blank for every initial state, so it is not a permanent latch. We prove a general reason exact nontrivial finite-time latching cannot occur in the stated bounded-generator class. This is a restricted result, not an impossibility theorem for asymptotic scattering records, unbounded systems, approximate records or physical dissipation.

The continuum bound uses the previous [exact rational commutator certificate](ZERO_TWO_WINDOW_CERTIFIED_SUPPORT_COMMUTATOR.md); [new checks](verification/zero_two_window_redundant_flag_hold_test.py) include that certificate and finite-regulator evolution, which is a control rather than the continuum proof. No novelty claim is made for repetition coding, Duhamel bounds or analytic no-plateau arguments.

## 1. Reuse the actual prior model, and identify the change

The prior two-window positive-frequency model supplies, for each logical label h=0,1,

```text
Ω_h = √Θ_h,       Ω_h ≥ a_h I,       a_h > 1.3,
P = projector onto the given two-packet span,     Q=I−P.
```

P and Q act on the original geometry–pointer–memory factor and identically in h. The supplied continuum proof gives

```text
||[Θ_h,Q]|| < 0.419,
||[Ω_h,Q]|| ≤ ||[Θ_h,Q]||/(2a_h) < c_* = 0.419/(2×1.3).
```

The second inequality is the positive-square-root commutator bound used in the earlier analysis. Numerically `c_*≈0.161154`. It is a worst-case continuum upper bound, not a fit to a particular state.

Add `N=8` two-level flags, initially all in `|0…0⟩`, and define

```text
S_y = Σ_(j=1)^8 σ_y^(j),     g=100,     B=8g=800,
H_h = Ω_h ⊗ I + B I + g Q ⊗ S_y,
Θ'_h = H_h²,                 C'_h=(p_φ²−Θ'_h)/2.
```

The model uses dimensionless illustrative units and the selected positive-frequency branch `p_φ=H_h`. It is a **new constraint**, not a clock transformation or an unchanged realization of the earlier device. Because `||S_y||=8` and Q is a projection,

```text
H_h ≥ (a_h+B−8g) I = a_h I > 1.3 I.
```

H_h is bounded and self-adjoint on the declared band Hilbert space; the displayed quadratic constraint is self-adjoint on its natural momentum domain. The scalar φ remains the assumed internal clock and the branch choice and physical inner product are supplied as in the parent positive-frequency construction. No claim is made that the added flags, their preparation or the highly nonlocal Q interaction are derived from zero or physically realizable as a local apparatus.

The offset B and large g keep the selected root positive while shortening the control time. They change its frequency spectrum and constraint. An additive identity term might be removable by a suitable clock-phase convention in a different formulation; we do **not** infer a measured energy cost merely by calling B energy. Conversely, the large global coupling and eight prepared flag degrees of freedom are not free proven physical resources. A real gravitational/thermodynamic embedding must account for their operational cost and justify the clock-momentum reference.

## 2. The ideal comparator and its finite window

Let `U(φ)=exp(iH_h φ)`; the sign convention matches the parent model. Compare it—not as another implemented apparatus but as a mathematical bound—with

```text
U_id(φ) = exp[i(Ω_h+B)φ] exp[i g Q S_y φ].
```

When Q=0 all flags remain blank in the comparator. When Q=1 each independently rotates, and the probability that **all** flags remain blank is

```text
cos^(2N)(gφ).
```

The defined readout effect is the OR effect

```text
F = I − |0…0⟩⟨0…0|.
```

Thus the ideal Q-state miss probability is `cos^(16)(gφ)`. For

```text
π/4 ≤ gφ ≤ 3π/4,
```

its maximum is `2^−8=1/256`, while the ideal P-state false-flag probability is zero. The comparator can have substantial changes in the individual flag configurations across the window; the guarantee concerns the **collective OR event**, not a frozen microscopic state.

In the interaction picture, `||Q(s)−Q||≤s ||[Ω_h,Q]||`. Duhamel's formula gives for the actual and ideal full unitaries

```text
||U(φ)−U_id(φ)|| ≤ N g ||[Ω_h,Q]|| φ²/2.
```

The identity offset cancels from this estimate. Throughout the displayed interval,

```text
D(φ) < D_* := 9π² N c_*/(32g)
              < 9(22/7)² N c_*/(32g)
              ≈ 0.035816 < 0.036.
```

The inequality is a continuum norm bound for the stated model, not a finite-grid extrapolation. For every normalized P input, applying the triangle inequality to the flagged output gives `Pr(flag)≤D_*²<0.0013`. For every normalized Q input, applying it to the **blank** output gives

```text
Pr(blank) ≤ (2^(−N/2)+D_*)²
          < (1/16+0.036)² < 0.0097.
```

The same bounds extend to mixed states and arbitrary h correlations by purification/direct-sum norm bounds. These are **individual terminal readouts at a chosen φ**, each performed on a separate preparation if comparing times. They do not assert that continuous monitoring leaves the evolution unchanged.

## 3. A coherent support inference

For an arbitrary initial density operator, including coherence between P and Q and correlations with h, write

```text
λ=Tr(Qρ),       s(φ)=√[1−cos^(16)(100φ)].
```

With flags initially blank, the ideal flag probability is `s(φ)²λ`; the P and Q sectors are orthogonal even if ρ has off-diagonal terms. For the actual model's flag probability q at a chosen φ in the window, the full-unitary bound yields

```text
|√q−s(φ)√λ| ≤ D_*,
λ ≤ min[1, ((√q+D_*)/√(255/256))²].
```

This is a state-uniform continuum statement **conditional on the supplied Hamiltonian, blank flags and interval**, not a claim that the physical world realizes Q. A confidence upper bound `q_U` from independent copies can replace q, with its own sampling and implementation error budget. For illustration only, if a *new experiment using this changed device* produced `q_U=0.019485`, the formula would give `λ<0.0311`; that number must not be imported from the old device as if the same counts had already been obtained here.

This support estimate alone does not reconstruct the state inside P, prove the calibration reference states, or predict the earlier 32-outcome histories. To obtain such a prediction one needs a tomography protocol on matching preparations and a justified map between this changed constraint and the target procedure. The earlier output sensitivity and preparation assumptions remain relevant.

For a bounded implementation perturbation ΔH with `||ΔH||≤δ`, Duhamel adds at most `(3π/400)δ` to the amplitude error within the window. A sufficient positivity condition is `δ<1.3`. Such an operator-norm guarantee itself requires justification; finite calibration of a few test states does not prove it.

## 4. Why this still does not make a durable record

At `φ=π/g=π/100`, the ideal comparator returns **all** flags to blank for both P and Q. Applying the same norm estimate at that time gives

```text
D_return < 16 D_*/9 < 0.06368,
Pr(flag) < D_return² < 0.0041
```

for every normalized initial system state with blank flags. Thus the high flag window is genuinely transient in this model: a later readout will almost certainly miss even an initially outside-support state. The earlier one-flag device already exhibited this failure; redundancy widens a useful window but does not solve retention.

### Exact finite-time plateau obstruction for bounded autonomous generators

Let H be any bounded self-adjoint Hamiltonian, ρ a trace-class initial density operator and `0≤F≤I` a fixed readout effect. Then

```text
p(t)=Tr[ρ exp(−itH) F exp(itH)]
```

is real analytic: the exponential power series converges in operator norm for complex t, and the trace defines an entire extension. If p is constant on any nonempty open interval, the identity theorem makes it constant on the entire real line. Consequently, if an initially blank flag has `p(0)=0`, it cannot become nonzero and then remain **exactly constant on a finite open interval** under such a fixed bounded autonomous Hamiltonian and fixed effect.

This includes the present band-restricted model and any finite-dimensional autonomous extension with a bounded generator. It does not forbid approximate plateaus, a nonconstant record with a high-confidence readout window, a pre-existing record, measurement-conditioned dynamics, unbounded Hamiltonians, environment-assisted processes or an asymptotically conserved scattering observable. The repository's [autonomous stopped-clock construction](AUTONOMOUS_STOP_CLOCK.md), with its unbounded carrier and asymptotic output, is not contradicted. It also does not prove that **every** operational record must have a literal exact probability plateau.

## 5. Independent finite-regulator controls

The verifier uses the existing `system` function to build the original regulated Ω and Q, not a replacement toy geometry. The eight flags begin in a permutation-symmetric state and the coupling preserves that symmetric flag subspace, so it is sufficient for this initialization to represent their collective spin in dimension 9 rather than all 256 basis states. This reduction is a simulation convenience; the continuum proof uses the full flag tensor product.

At grid `N_grid=8`, for one P input and one randomly constructed Q input, the following are illustrative terminal probabilities, not worst-case or continuum estimates:

| h | `gφ/π` | P input: flag | Q input: flag |
|---:|---:|---:|---:|
| 0 | 0.25 | 0.00000016 | 0.996094 |
| 0 | 0.50 | 0.00000056 | 1.000000 |
| 0 | 0.75 | 0.00000097 | 0.996094 |
| 0 | 1.00 | 0.00000118 | 0.00000003 |
| 1 | 0.25 | 0.00000022 | 0.996094 |
| 1 | 0.50 | 0.00000079 | 1.000000 |
| 1 | 0.75 | 0.00000135 | 0.996094 |
| 1 | 1.00 | 0.00000165 | 0.00000005 |

Checks also sample the full window, verify the collective-spin spectrum and comparator formula, and test a coherent 10% Q state against the inference inequality. Finite sampling is not the proof of the continuum uniform bound; nor do these small-grid numbers establish experimental reliability.

## 6. Next gate

Build a **physical, autonomous readout or transfer** in the same changed constraint that registers whether the collective flag is high during the proved interval, with timing uncertainty, no-readout outcomes, backreaction and eventual retention explicitly bounded. Alternatively, establish a controlled link to the existing asymptotic stopped-clock scattering device; its event is not automatically this Q-support flag. Then construct a genuinely distinct second clock for the same complete instrument.

Until then the result is a finite-window information resource with an assumed reading protocol. It is not a solution of time, a global clock, an actual detector, an entropy arrow, a subject, experience or a derivation of physical total energy from zero.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_redundant_flag_hold_test \
 verification.zero_two_window_commutator_certificate_test \
 verification.zero_two_window_autonomous_support_dynamics_test -v
```

The exact-rational threshold, operator inequalities and analytic argument establish the stated bounds under their assumptions; the eigensolver checks and sampled trajectories do not constitute an experimental test or independent continuum proof.
