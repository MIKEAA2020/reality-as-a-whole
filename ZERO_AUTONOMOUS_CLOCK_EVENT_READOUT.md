# An autonomous readout of the clock-neutral event—and a cursor-sign correction

## Result and correction

We construct a time-independent, positive-Hamiltonian **model readout** of the [previous clock-neutral effect](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md) F₁. A new moving cursor triggers a pointer coupling. For a specified cursor preparation and finite duration, the pointer instrument approximates the **relational Lüders instrument** `ρ↦√F_m ρ√F_m`, including the full old apparatus and R clock in the output, with half-diamond error below **0.000318** on arbitrary old-system inputs and untouched references. Both m=0 and m=1 are retained. This is a conditional mathematical construction, not an engineered or local detector.

**Correction to earlier work:** with `p=−i∂x` and the stated evolution `exp(+iHφ)`, the earlier written packet `exp(+imvx) ψ_a(x+vt₀)` moves **left**, away from the reader at x=0. The earlier chiral numerical simulations and bound arguments instead assumed a right-moving packet. We have corrected the [original construction](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) to `exp(−imvx) ψ_a(x+vt₀)` and its chiral comparator to `−vp`. Then the packet moves right, as assumed by the simulations and bounds. The dependent earlier claims apply to this **corrected** preparation, not to the originally written opposite-moving one. The old simulations did not detect this because they evolve prescribed chiral trajectories rather than the massive packet. The new verifier checks both directions.

The new readout is a different operation from the earlier time-label-discarding instrument T: it realizes a chosen **Lüders instrument L with the same effects**, not the same poststate as T. Its static interaction is a highly nonlocal function of the already specified relational event F₁. This is not a local R-clock detector, a readout of a separately displayed clock value, or a general solution of time. [Tests](verification/zero_autonomous_clock_event_readout_test.py).

## 1. Fix the event and select a concrete instrument

Let `H₀=H_A+K_R` be the earlier self-adjoint, positive root on `H_old=H_A⊗H_R`. A contains the actual two-window system, its old massive cursor, flags and record memory; R is the semibounded independent clock. The earlier normalized effects satisfy

```text
F₀+F₁=I,     0≤F_m≤I,     [F_m,H₀]=0
```

in the strong spectral sense. The last equality follows from the invariant weak orbit integral and functional calculus. F₁ represents the previously specified **joint memory outcome relative to a finite R-clock bin**. It need not be a projection. Define the bounded self-adjoint operator

```text
Θ = arcsin(√F₁),      0≤Θ≤π/2,
cos Θ = √F₀,          sin Θ = √F₁,
[Θ,H₀]=0.
```

Choose the already proposed but previously abstract operations

```text
L_m(ρ) = √F_m ρ √F_m.
```

They are complete and have exactly the prior F_m outcome probabilities for **all** old-space input states, not just the original product preparation. Their output states generally differ from the previous T_m operations with those effects. Choosing L is a substantive choice of intervention; effect agreement alone does not identify the operations.

## 2. A changed, positive autonomous constraint

Add a **new** cursor `x,p=−i∂x` and a fresh two-state pointer D with Pauli operator σ_y. All old factors are retained. Set

```text
H_new = H₀ + p²/(2M) + B + v f_b(x) Θ σ_y^D,
C_new = [p_φ² − H_new²]/2,       selected branch p_φ=H_new.
```

Use a real fixed profile

```text
f_b(x)=15(1−(x/b)²)²/(16b)  for |x|≤b, and 0 otherwise,
∫ f_b(x)dx=1.
```

The pointer starts in `|0⟩`. H₀ and the new free kinetic operator are self-adjoint on their tensor-sum domain; the interaction is bounded and self-adjoint. Hence H_new is self-adjoint on that domain. Since `||Θ||≤π/2`, choose

```text
B = 1 + (π/2)v ||f_b||∞ = 1 + 15πv/(32b).
```

Then `H_new≥H₀+1>0`; its positive square and selected constraint branch are well-defined by spectral calculus. This is another **explicitly changed model/constraint**. B provides a lower bound, not automatically a measured energy expenditure or an assertion of cosmic zero. The interaction is static in scalar φ, but its highly nonlocal operator Θ is assumed to be available; we have not decomposed it into a local clock, old-memory and geometry interaction. It is constructed from the complete relational effect itself and therefore does not explain how an observer could build such a coupling from elementary local operations.

The new coupling commutes with H₀ because Θ does, so H₀ is conserved by the enlarged model. This is a mathematical property of this specially engineered observable, not a general zero-cost measurement theorem. The new cursor kinetic energy, pointer, interaction and preparation are additional resources.

## 3. One pass through the interaction region

Let `v>0`. Prepare the cursor independently of the entire old system and reference X in

```text
ψ_new(x)=exp(−iMvx) ψ_a(x+vt₀),
ψ_a(z)=√[315/(256a)] (1−(z/a)²)²  for |z|≤a, else 0.
```

Use the convention of the earlier model, `exp(+iH_new T)`. After conjugating away the carrier, the kinetic term is `−vp+p²/(2M)` plus the constant `Mv²/2`. In the comparison with `−vp` the cursor shifts toward **positive** x. Each starting position in its compact support crosses the full interaction profile during

```text
T_start=t₀−(a+b)/v,       T_end=t₀+(a+b)/v.
```

Assume `t₀>(a+b)/v`. For `T≥T_end` the full normalized profile has passed each component. Since Θ is constant in the H₀ interaction picture and all pulse terms commute with one another, the chiral comparison has the exact pointer gate

```text
W=exp(i Θ σ_y^D),
⟨0|W|0⟩ = cos Θ = √F₀,
⟨1|W|0⟩ = −sin Θ = −√F₁.
```

The minus sign in the second Kraus operator cancels from its CP operation. The comparison's translated cursor is independent of the old input after the pulse. Thus, after reading pointer D, tracing the new cursor and retaining the old space and an arbitrary untouched reference X, the ideal comparison channel is

```text
C_L,T(ρ) = Σ_m |m⟩⟨m| ⊗ U₀(T) √F_m ρ √F_m U₀(T)†,
U₀(T)=exp(iH₀T).
```

This includes the R clock and the original memory in each output branch. L and U₀ commute but neither need preserve the original memory or R state as an ordinary unperturbed clock readout would.

## 4. Continuum error bound for the massive cursor

The comparison with the positive kinetic Hamiltonian is controlled on the **fixed new-cursor packet**, not on arbitrary cursor inputs. In the chiral solution the pulse depends on initial position z. Duhamel differentiation of its internal unitary gives, uniformly on the old space and any reference,

```text
A₁ = ||Θ|| ||f_b'||₁ ≤ (π/2) 15/(8b),
A₂ = ||Θ|| ||f_b''||₁ + A₁²
   ≤ (π/2) 10/(√3 b²) + A₁²,
K₂ = √(63/2)/a² + 2(√3/a) A₁ + A₂.
```

The profile and envelope have the weak derivatives and L² regularity needed for these expressions. In particular `||ψ_a'||₂=√3/a` and `||ψ_a''||₂=√(63/2)/a²`; `f_b'` is continuous and its weak second derivative is integrable. These estimates imply `||p² Ψ_chiral(t)||≤K₂`. Comparing `−vp+p²/(2M)` with `−vp` by Duhamel gives, up to the common carrier/B phase,

```text
||Ψ_massive(T)−Ψ_chiral(T)|| ≤ ε(T):=T K₂/(2M).
```

First establish this on old states in the H₀ domain, then extend by density: the bound is uniform in the normalized old/reference input and Θ is bounded. Reading/dephasing D and discarding the new cursor are contractive, so

```text
(1/2)||C_new,T−C_L,T||_diamond ≤ min(1, ε(T)),       T≥T_end,
```

where the diamond input is the old space with arbitrary untouched reference, **and the new cursor and pointer are fixed as specified**. This bound includes the R/old-apparatus poststate for L. It does not bound the distance from T_m, from the prior scalar-slice mixture J_m,B, or from an unsupplied physical device.

An example in dimensionless units is

```text
a=b=0.3,    v=1,    t₀=1,    M=10⁶,
T_start=0.4,    T_end=1.6,    T=1.7,
K₂≤372.873,     ε(1.7)<0.000318.
```

B≈5.9087. The new cursor's mean kinetic energy is `Mv²/2 + 3/(2Ma²)≈500000.0000167` in these units. The older cursor's extreme resource assumptions still also apply. There is no asserted unit conversion or practical feasibility.

Since ideal L has effects F_m, the implemented pointer outcome probabilities differ from `Tr(F_mρ)` by at most ε. On the earlier independently prepared R clock and original ready apparatus, the prior probability-only comparison with initial P/Q support therefore yields the illustrative absolute-error bound

```text
|Pr(new pointer m)−Tr(P_m ρ_system)|
   < 0.01849 + 0.0000177 + 0.000318 < 0.01883.
```

This combines the old in-window probability bound, old clock-tail bound and new implementation bound; it is not a full-poststate comparison with the scalar-smeared instrument J. The ideal clock-bin is part of the definition of F_m, so this two-outcome construction does **not** provide an independent clock no-reading/failure outcome or a classical reading of r. Branches with small probability cannot be assigned a uniform normalized poststate error without a probability lower bound.

Before T_start the chiral pointer is blank; the massive model's early-click probability is at most `ε(T)²` for its fixed cursor preparation. After the crossing the chiral pointer is stable; the massive comparison only establishes the stated bound for each chosen finite T. It does not prove permanent retention or prevent eventual cursor spreading and return. Reading the pointer is an additional chosen operation; no general measurement-repeatability or thermodynamic claim follows.

## 5. Sign correction in detail

For `p=−i∂x`,

```text
exp(+i v p t) ψ(x) = ψ(x+vt)    (packet travels left),
exp(−i v p t) ψ(x) = ψ(x−vt)    (packet travels right).
```

Accordingly the earlier carrier `exp(+imvx)` with `exp(+iHt)` and `m>0` gave the first, left-moving behavior. Its center started at `−vt₀`; it could not follow the claimed rightward chiral trajectory. The corrected phase `exp(−imvx)` gives the second behavior. For the old even interaction profile and the real symmetric envelope, the old chiral trajectory `f_b(z−vt₀+vt)` and all its derivative norms and timing estimates are exactly the ones used by the calculations; only the preparation/carrier and sign of the chiral generator required correction. This is not proof that the original incorrectly specified preparation had the advertised record error.

The mistake is not merely notational. In the old *uncorrected* setup the chiral comparator's entire compact packet stays strictly left of the pulse for every `t≥0`. Its memory remains blank, even for a Q-sector input. Along that comparison path, the internal evolution is independent of x, so `||p²Ψ_chiral||=√(63/2)/a²`. Using the old `a=b=10⁻⁶`, `m=10¹⁶`, `t₀=π/200` and `T_ret=π/100`, Duhamel gives

```text
P_uncorrected(memory=1 at T_ret)
  ≤ [T_ret √(63/2)/(2m a²)]² < 7.773×10⁻¹¹.
```

This holds for arbitrary old-system input with the specified blank memory and factorized cursor; in particular, it is incompatible with the old claimed near-certain Q record **for the uncorrected state**. This bound is an analytic comparison for the originally written model, not a finite-grid inference. The verifier checks the constants and a separate moderate-scale wrong-way simulation.

The previous full-instrument and second-clock reports now explicitly point to this correction. Their bounds remain **conditional on the corrected setup**, as well as all their other assumptions. The earlier finite-grid controls were insensitive to the sign because they directly prescribed the crossing trajectory; they should not be described as numerical verification of massive-cursor direction.

## 6. Finite numerical control and limitations

The [test](verification/zero_autonomous_clock_event_readout_test.py) builds an unsharp cyclic event effect using P/Q sectors selected from the actual old two-window grid and checks the square-root pointer gate, positivity and commutation with a cyclic H₀. It also verifies that the coherent Lüders and time-label-discarding operations have the same effects but different poststates for one input. It confirms that plus/minus translation generators move a localized packet in opposite directions. It separately evolves a prepared massive cursor on a finite periodic Fourier grid for several eigenvalues of that finite effect, including unsharp values 0.3 and 0.7, and checks the zero-coupling outcome.

For the sample parameters, selected grid state-vector errors are about `0.000053–0.000056`, below the analytic `0.000317` continuum budget apart from a small explicitly allowed numerical discretization tolerance. This control uses a **different finite cyclic clock and old Hamiltonian**; it does not numerically construct the continuum F₁, simulate the old massive cursor, prove the diamond bound, or establish spatial locality. The operator proof and fixed packet assumptions supply the asserted continuum bound.

**Next target:** replace the nonlocal `arcsin√F₁` interaction with explicit local or controlled approximations acting on the actual memory, R clock and a physical probe, then compare the resulting complete instrument—not just its effect—with the desired same-event operation. Alternatively establish a well-defined R-relative retained-observable algebra and a switch on its common domain. Turning/interacting clocks, physical no-reading, gravity/refoliation, lived succession and a common constitutive derivation remain open.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_autonomous_clock_event_readout_test \
 verification.zero_two_window_autonomous_cursor_reader_test \
 verification.zero_two_window_retained_clock_instrument_test -v
```
