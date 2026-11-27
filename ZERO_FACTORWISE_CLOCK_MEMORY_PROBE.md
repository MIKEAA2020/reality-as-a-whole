# A factorwise clock–memory probe with a no-bin outcome

**Continuation:** [the retained-clock obstruction](ZERO_CLOCK_PROBE_POSTSTATE_OBSTRUCTION.md) proves that this probe's conditioned clock poststate cannot equal the earlier orbit-averaged instrument's clock poststate: the latter has strictly positive out-of-band probability while this probe preserves the initial band exactly. [The same probe in an R-time representation](ZERO_SAME_PROBE_CLOCK_REPRESENTATION.md) transports the actual four outcomes and retained cursor isometrically, and establishes a restricted loss of recoverability after an additional classical R reading. The encoding is not an independently quantized gravitational clock switch.

## Result

We replace the previous readout's assumed coupling to the **whole relational effect** `F₁` by two separately specified couplings: one to the existing record memory, the other to the added quantum clock R. A further massive cursor triggers both couplings through a static position profile. The changed positive Hamiltonian gives a complete four-outcome probe instrument: clock-bin hit/no-bin hit and memory record/no-record. It retains the original apparatus, R, and both probe outcomes, and includes measurement backaction.

For one explicit, extreme parameter choice, the resulting full output channel is within **0.000466 half-diamond distance** of a specified instantaneous factorwise comparator, uniformly over the old Hilbert space and arbitrary untouched references, with the *new* cursor and probes in fixed ready states. For the earlier independently prepared bandlimited R clock and corrected old apparatus preparation, the memory distribution **conditioned on a bin hit** is within **0.00781 total variation** of the previous clock-neutral event distribution. The conditional comparison uses a proved positive lower bound on the bin-hit probability and counts the no-bin outcome rather than dropping it silently.

This is a limited but concrete step toward the target in the [plan](PROBLEM_OF_TIME_DIVIDE_AND_CONQUER_PLAN.md). The two couplings are local **in the tensor-factor sense only**; the R coupling still assumes a specially engineered spectral operator, and the old support detector contains a global Q coupling. The fixed cursor is synchronized relative to the scalar clock. The new and earlier operations are different interventions; closeness of their selected memory probabilities is **not** equality of their full poststates or a completed R-relative clock switch. The finite numerical controls are not a continuum simulation. [Checks](verification/zero_factorized_clock_probe_test.py).

## 1. Keep the old event and clock explicit

Use the corrected earlier two-window apparatus Hamiltonian H_A, including its old cursor, flags and memory M. The added clock R has `H_R=L²([0,∞),dk)` and `K_R=k`. Let

```text
H₀ = H_A ⊗ I_R + I_A ⊗ K_R,
U₀(t)=exp(iH₀t),                    Π_m = old memory outcome m.
```

The old positive-frequency constrained branch is the same one as in the [second-clock construction](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md). Its R time POVM E_R has finite-bin effect `E_R(B)` with

```text
B=[r−ℓ/2,r+ℓ/2],     ℓ=10⁻⁴,
r=(T_end+T_ret)/2≈0.023562945.
```

The declared R preparation β is supported in the **finite positive-frequency band**

```text
Λ=[k₀−b_R,k₀+b_R]=[5000,15000],      k₀=10000, b_R=5000,
β(k)=b_R^(−1/2) cos[π(k−k₀)/(2b_R)] on Λ, zero outside.
```

Let P_Λ be the clock spectral projector and define

```text
E = P_Λ E_R(B) P_Λ,          E₁=E,          E₀=I−E.
```

Because `0≤E_R(B)≤I`, E and `I−E` are effects on the **whole** clock space. For any state supported in Λ, the probability of E equals that of the original `E_R(B)`. The operations associated with their square roots need not be equal: `√E` and `√E_R(B)` can produce different poststates, even on band-supported inputs. E₀ includes clock readings outside B **and** all out-of-band states; call it a *no-bin-hit* outcome, not an independently diagnosed hardware failure. Its probability is retained.

This band-limited binary effect is not a sharp canonical time operator, and the spectral projection and square-root interaction are assumed resources. The construction is not a proof of a local detector in spacetime or of a universal covariant clock instrument for all bins.

## 2. An autonomous, factorwise interaction

Introduce two fresh qubit probes D_R,D_M and a fresh cursor `x,p=−i∂x`, independent and initially prepared below. Define

```text
Θ_R = arcsin(√E),                     Θ_M = (π/2) Π₁,
G = Θ_R ⊗ σ_y^(D_R) + Θ_M ⊗ σ_y^(D_M),
H_new = H₀ + p²/(2M) + B₀ + v f_b(x) G.
```

The R term acts on R and D_R, the memory term only on old M and D_M. They commute with each other at a fixed time because their tensor factors are disjoint. Neither term is a function of the joint relational effect F₁. The smooth compact profile is the earlier normalized `f_b(x)=15(1−(x/b)²)²/(16b)` for `|x|≤b` and zero outside. Since `||G||≤π`, choose

```text
B₀ = 1 + π v ||f_b||∞ = 1 + 15πv/(16b).
```

H_new is self-adjoint on the free tensor-sum domain because its interaction is bounded, and `H_new≥H₀+1>0`. The further changed constraint `C_new=(p_φ²−H_new²)/2` with positive branch `p_φ=H_new` is well-defined by spectral calculus. This is a **new constraint and extra apparatus**, not a passive change of clock coordinates.

Initialize both probes in `|0⟩`, and initialize the new cursor in

```text
ψ(x)=exp(−iMvx) ψ_a(x+vr),
ψ_a(z)=√[315/(256a)](1−(z/a)²)² for |z|≤a, zero outside.
```

With `exp(+iHt)`, the carrier moves the packet rightward. Its initial center is synchronized so the passage is centered at the scalar reading r; the interaction Hamiltonian itself is not time-dependent. This synchronization and the fixed profile remain supplied inputs. Read the two probe qubits after the passage at a chosen scalar output slice; autonomous initiation is not a demonstration of an autonomous final observer or a permanent record.

## 3. The complete comparison instrument

If the interaction were an instantaneous gate at r, then with `c,m∈{0,1}` its Kraus operators at that slice would be

```text
A_(c,m) = √E_c ⊗ Π_m,       Σ_(c,m) A_(c,m)†A_(c,m)=I.
```

The probe sign for c=1 and/or m=1 is irrelevant to its CP operation. At a later scalar output T, the comparator channel, with the two classical outcomes retained and all old degrees of freedom and R retained, is

```text
C_inst(ρ) = Σ_(c,m) |c,m⟩⟨c,m| ⊗ V_(c,m) ρ V_(c,m)†,
V_(c,m) = U₀(T−r) A_(c,m) U₀(r).
```

The outcomes `(0,0),(0,1),(1,0),(1,1)` are all included. The actual autonomous cursor interaction produces a channel `C_probe` on the same retained output, after reading its probes and tracing the new cursor. The clock and memory gates perturb their respective subsystems: the effects alone do not fix a unique update, and this comparator uses exactly the displayed square roots.

For a product clock β and any state of the original system/reference with the corrected old ready ancillas, R and A evolve independently before r. Thus in the **instantaneous comparator**,

```text
p_inst(c=1,m) = q_hit p_m(r),
q_hit = ⟨U_R(r)β|E|U_R(r)β⟩,
p_m(r) = old apparatus memory probability at r.
```

This factorization is not asserted for R correlated with A or an interacting R Hamiltonian. It concerns this particular fresh-probe intervention; the old relational F_m was defined by an orbit-average, not by a finite-probability bin hit at a particular prepared scalar slice.

## 4. Controlled continuum comparison

Let `d=(a+b)/v` and `T=r+d`. The new cursor's chiral comparison traverses the whole pulse in `[r−d,r+d]`. In the H₀ interaction picture the coupling at time t differs from its value at r by at most `|t−r|` times the sum of the following bounded commutator norms.

For the old memory coupling, only its old reader term `κv_old f_old(x_old) F_flag σ_y^M` fails to commute with Π₁. With the earlier `κ=π/2`, `v_old=1` and old width `10⁻⁶`,

```text
||[H_A,Θ_M]|| ≤ (π/2) κ v_old ||f_old||∞
                = (π/2)² 15/(16×10⁻⁶) ≈ 2,313,188.54.
```

For R, Θ_R is supported in Λ, commutes with P_Λ and vanishes outside it. As K_R differs from k₀ by at most b_R on that band,

```text
||[K_R,Θ_R]|| ≤ 2b_R||Θ_R|| ≤ π b_R ≈ 15,707.97.
```

These are bounded commutators on the appropriate domains, extended by continuity. Duhamel comparison over a normalized pulse gives the finite-duration error

```text
ε_pulse ≤ d [ (π/2)² 15/(16×10⁻⁶) + π b_R ].
```

For the massive cursor, conjugate away its negative-momentum carrier and compare `−vp+p²/(2M)` with `−vp`. The z-derivative estimates use `||G||≤π`; an arbitrary old state or reference only sees bounded internal unitaries. Set

```text
A₁ = π 15/(8b),
A₂ = π 10/(√3 b²) + A₁²,
K₂ = √(63/2)/a² + 2(√3/a) A₁ + A₂,
ε_disp(T) = T K₂/(2M).
```

The normalized compact cursor envelope has the derivatives used in K₂. Duhamel and density of the H₀ domain give a state-vector bound `ε_pulse+ε_disp`, uniformly on the old space and arbitrary references. Reading the probes and discarding the new cursor are contractive. Hence

```text
(1/2)||C_probe − C_inst||_diamond ≤ δ := ε_pulse+ε_disp(T),
```

for the specified new cursor/probe preparation. This statement controls the **whole four-outcome, retained-old-space instrument**, not just the probability of a click. It does not assume a fixed old input or R preparation; the separate probability comparison below does.

Choose dimensionless parameters

```text
a=b=10⁻¹⁰,     v=1,     M=10³⁰,     T=r+2×10⁻¹⁰,
ε_pulse ≈ 0.000465779299,     ε_disp ≈ 0.0000000000929,
δ ≈ 0.000465779392 < 0.000466.
```

The new cursor's mean kinetic energy is approximately `5×10²⁹` in model units, and `B₀≈2.945×10¹⁰`. These deliberately extreme parameters, the old cursor's resources, preparation synchronization and implementation of Θ_R are not claimed physically practical. No actual energy cost follows from the positivity shift alone.

## 5. Comparison with the earlier clock-neutral memory probabilities

In the earlier clock-neutral prescription, for this fixed R β and old ready state,

```text
p_F(m) = ∫_R dt q_B(t) p_m(t),
q_B(t)=w_B(r−t),        ∫ q_B(t)dt=1.
```

The clock tail outside `[T_end,T_ret]` is below `τ_B=0.0000177`. The corrected old cursor's *chiral comparator* memory probability is constant throughout this window: after its cursor has passed, the remaining old Hamiltonian commutes with the memory projector. The actual massive old cursor differs from that comparison by at most `t K_old/(2m_old)` in state norm for the fixed old cursor packet. Therefore, uniformly on original-system inputs and untouched references,

```text
TV(p_F, p(r)) ≤ τ_B + (r+T_ret) K_old/(2m_old) < 0.000110.
```

For two memory outcomes, TV is the absolute difference of their m=1 probabilities. This uses the **same old autonomous memory dynamics** in both quantities. It does not assert that an instantaneous measurement and an orbit-averaged instrument are the same physical operation or have equal poststates. Times outside the retention window contribute their full worst-case probability to the bound; none are silently discarded.

To condition the new probe on `c=1`, its hit probability must be nonzero. With `y=b_R u`, the normalized time density from the earlier cosine packet has

```text
q_hit = ∫_(−b_Rℓ/2)^(b_Rℓ/2) scaled_w(y) dy ≈ 0.12849858,
scaled_w(y)= π cos²(y) / [2((π/2)²−y²)²].
```

Here `b_Rℓ/2=1/4`. For `|y|≤1/4`, the denominator is no larger than its value at zero and `cos²(y)≥cos²(1/4)`. Thus without relying on numerical quadrature,

```text
q_hit ≥ (b_Rℓ) [8/π³] cos²(1/4) ≈ 0.121109837 > 0.121.
```

The complete joint-output TV bound implies the actual hit probability is at least `q_hit−δ>0.1205`. A conservative normalization inequality gives

```text
TV(p_probe(m | c=1), p_inst(m | c=1)) ≤ 2δ/q_hit.
```

Combining the inequalities and using the explicit lower bound,

```text
TV(p_probe(m | c=1), p_F(m)) < 0.00781.
```

This is a **conditional record-statistics bound**, not a bound between full R-relative and scalar-relative output states. Clock no-bin and memory no-record outputs are present in the four-outcome instrument; only the explicitly stated final comparison conditions on c=1. The observed clock hit rate is preparation-specific; R correlations or a different β can change both that rate and the conditional memory state. No reading at c=0 is not identified with the absence of a physical event.

## 6. Controls, what is new and what is not

The [verification module](verification/zero_factorized_clock_probe_test.py) checks the numerical constants, the analytic lower bound and a quadrature value for the cosine-packet bin hit. It constructs Nyström matrix approximations to the band-compressed clock effect, checks both probe outcomes and all four joint outcomes, and verifies convergence of the selected bin probability with increasing clock grid. It integrates separately the two **chiral prescribed-trajectory** probe gates, including a finite Hamiltonian chosen to saturate the memory commutator bound, for several cursor offsets. A separate selected-state calculation checks that the existing two-window finite-grid chiral memory probabilities stay fixed across a sampled smearing window. A changed R preparation supplies a negative control for the hit probability.

These are selected finite calculations; they do not numerically simulate the full old or new massive cursors, establish an operator-norm Nyström continuum limit, measure an actual instrument, or independently prove the analytical diamond bound. The finite matrix clock uses midpoint quadrature, not an exact finite model of every continuum degree of freedom.

**Progress:** unlike the previous `arcsin√F₁` coupling, the new interaction acts separately on the existing memory and R clock; it explicitly includes a finite-bin click/no-bin output, old-memory no-record and full comparator backaction. The numerical agreement with F concerns the record distribution and uses retention stability; it is not obtained by calling two different instruments identical.

**Open:** Θ_R still assumes a nonlocal-in-frequency engineered binary-effect gate. The clock and old Q-support apparatus are not physically local in spacetime. The R clock does not trigger the probe by itself; the extra cursor is synchronized to the scalar time. The instantaneous comparator, the new four-outcome operation and the earlier orbit-averaged instrument do not have proven equivalent retained poststates. No repeat-read or independent device-failure model is supplied; no full gravity or experiential/constitutive conclusion follows. Resource and timing assumptions are extreme.

**Next discriminating target:** construct a gauge-invariant R-relative description of this **same four-outcome instrument**, including its postmeasurement clock/memory states and subsequent operations, or exhibit a concrete retained-observable counterexample on the overlap. In parallel replace Θ_R by an explicit clock–probe interaction or controlled approximation, with calibration and a no-reading model. A successful probability comparison alone is not the full same-event clock-switch theorem.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_factorized_clock_probe_test \
 verification.zero_autonomous_clock_event_readout_test \
 verification.zero_two_window_second_clock_test \
 verification.zero_two_window_autonomous_cursor_reader_test -v
```
