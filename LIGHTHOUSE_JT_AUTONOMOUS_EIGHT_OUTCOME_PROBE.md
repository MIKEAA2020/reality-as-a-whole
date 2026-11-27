# Lighthouse WP0: an autonomous model probe for the same eight-outcome event

## Result and scope

The [previous York/scalar calculation](LIGHTHOUSE_JT_COMMON_EVENT_AND_CLOCK_SWITCH.md) specified an eight-outcome Lüders instrument but did not realize it dynamically. Here a **time-independent enlarged constraint** adds one massive cursor, a four-state clock pointer and a two-state qubit pointer. Its bounded interaction is a York-dressed function of the **original, uncompressed** four clock-bin effects and qubit event. In the ideal chiral-cursor comparator it realizes exactly the same eight Kraus operators and retains the old scalar, qubit and any reference. For a specified finite-mass cursor packet and finite crossing time, the full recorded-output channel is within

```text
(1/2) || C_massive - C_ideal ||_diamond < 0.000745
```

on the old input and arbitrary untouched references, with the new cursor and pointers fixed in their stated ready preparations. This is an analytical bound in the declared model. The no-reading/outside outcome is retained. The numerical control uses a separate compressed finite cyclic clock, not the continuum JT system.

The achievement is **not** a local or engineered detector: the assumed interaction is an explicitly constructed, generally nonlocal operator involving the complete time-bin effects, their square roots, a polar isometry and a gravitational/York dressing. It is a changed constraint with extra apparatus and a carefully synchronized initial packet. Its positivity offset and finite cursor kinetic energy are not a bound on the scalar's or the full apparatus's final energy. It does not establish the original JT/CFT zero-mode realization, locality, gravitational algebra or entropy comparisons, nor an autonomous final observer.

Crucially, the new constraint includes the apparatus; the previous scalar-frame map applies directly to the **old-model ideal or effective channel after a declared York-slice/instrument-data identification**, not automatically to the full interacting constraint. No full physical clock-switch theorem for the enlarged apparatus is asserted.

## 1. Preserve the previous instrument exactly

Let the old physical data space be `K = K_clock ⊗ C²`, including variable `B`, positive scalar energy and the qubit. Set

```text
H0 = E + h,       h = Δ|1><1|,
F_0 = F_outside,  F_1,F_2,F_3 = three original scalar-time bins,
Pi_± = (I ± X)/2,
A_(b,m) = sqrt(F_b) ⊗ Pi_m,    b=0,1,2,3,  m=±.
```

The `F_b` are the **full positive-energy covariant time effects**, including their `B`-controlled representation, not band compressions. They need not commute. `ΣF_b=I` and each is a positive contraction. We do not replace `sqrt(F_b)` by `sqrt(P F_b P)`: those can have different retained clock outputs even on a band-supported input.

The intended old-model instrument is `rho ↦ A_(b,m) rho A_(b,m)†`. With a fixed pointer register, its ideal recorded channel in the old York-data picture is

```text
C_ideal(rho) = Σ_(b,m) |b,m><b,m| ⊗ A_(b,m) rho A_(b,m)†.
```

## 2. A bounded gate for noncommuting clock effects

Introduce a clock pointer `D_c=C⁴` with ready state `|0>`, where outcome 0 denotes outside. Write `J:xi↦xi⊗|0>` and

```text
W_perp xi = Σ_(b=1)^3 sqrt(F_b) xi ⊗ |b>,
H_hit = Σ_(b=1)^3 F_b = I-F_0,
W_perp = V sqrt(H_hit)                     [polar decomposition],
Theta = arcsin sqrt(H_hit),
K_c = i( V Theta J† - J Theta V† ).
```

`V` is the polar partial isometry: `V†V` is the support projection of `H_hit`, its range is orthogonal to `J`, and no unbounded inverse at zero is assumed. `K_c` is bounded and self-adjoint with `||K_c||≤π/2`. On the support it is the usual two-subspace rotation, and on the kernel it acts trivially. Therefore

```text
exp(-i K_c) J xi
 = J sqrt(F_0) xi + Σ_(b=1)^3 sqrt(F_b) xi⊗|b>.
```

This is exact for noncommuting effects and realizes the **specified square-root poststates**, not merely the same probabilities.

Add a qubit pointer `D_s=C²` in `|0>` and define

```text
K_s = (π/2) Pi_- ⊗ sigma_y^(D_s).
```

`exp(-i K_s)` maps `xi⊗|0>` to `Pi_+ xi⊗|0> + Pi_- xi⊗|1>`. The two terms act on separate clock/pointer and qubit/pointer factors. Hence

```text
G = K_c + K_s,       ||G||≤π,
exp(-iG)(xi⊗|0>_c⊗|0>_s)
 = Σ_(b,m) A_(b,m)xi ⊗ |b,m>.
```

The `G` gate can act jointly on an arbitrary old state entangled with an untouched reference. `G` is an engineered nonlocal spectral operator; the factorization between the clock and qubit pointers is not a spacetime-locality statement.

## 3. An autonomous enlarged constraint

Let `S` be the York coordinate and `C=-i∂_S+H0` the previous constraint. Define the bounded gravitationally dressed interaction

```text
G_phys(S) = exp(-i H0 S) G exp(+i H0 S).
```

Although this is a function of the **quantum York coordinate**, it is not an externally scheduled function of an auxiliary time. It is constructed to commute with the old constraint's unitary group; equivalently, in the induced York interaction representation it is the fixed operator `G`. This is a very strong assumed nonlocal relational control.

Add cursor coordinate `x`, momentum `p_x=-i∂_x`, mass `M`, velocity parameter `v>0`, and the normalized compact profile

```text
f_b(x) = [15/(16b)] (1-(x/b)²)²   for |x|≤b;  0 otherwise,
∫ f_b(x)dx=1.
```

With the pointer free Hamiltonians chosen zero, take

```text
C_new = -i∂_S + H0 + p_x²/(2M) + B0 + v f_b(x) G_phys(S),
B0 = 1 + π v ||f_b||_infinity = 1 + 15πv/(16b).
```

The free operator is self-adjoint on its standard tensor-sum domain; the dressed interaction is bounded self-adjoint, so `C_new` is self-adjoint there. At every `S`, the conditional Hamiltonian is bounded below by `H0+p_x²/(2M)+1`. The **constraint** itself is not claimed positive: `-i∂_S` has both signs. The positivity offset is an operator lower bound, not an empirical energy-cost calculation.

Let `U0(S)=exp(-iH0 S)` and conjugate the full constraint by multiplication with `U0(S)`. On the transformed representation,

```text
U0† C_new U0 = -i∂_S + H_cursor,
H_cursor = p_x²/(2M) + B0 + v f_b(x) G.
```

Thus this is a static, self-adjoint enlarged constraint with no external switching. The scalar clock and qubit are still perturbed by `G`; they are merely constant in this special interaction picture. Standard group averaging of this linear constraint gives the positive physical York-data space for the enlarged model, as in the previous general self-adjoint-generator construction. The construction assumes a global York coordinate and the engineered dressing; it does not establish source JT/CFT domains or all local constraints.

## 4. Explicit cursor and full-instrument error

Use ordinary evolution `exp(-i H_cursor S)`. Prepare the cursor independently of the old state and all references as

```text
eta(x) = exp(+i M v x) eta_a(x+v S0),
eta_a(z) = sqrt[315/(256a)] (1-(z/a)²)²   for |z|≤a;  0 otherwise.
```

The **positive** carrier is correct in this convention: removing it gives `v p_x + p_x²/(2M)`, whose chiral part `v p_x` moves right. The scalar carrier energy is a common phase. Take `S0>(a+b)/v`. All components of the compact packet traverse the pulse over

```text
S_start = S0-(a+b)/v,       S_end = S0+(a+b)/v.
```

For `S≥S_end` the chiral comparator produces `exp(-iG)` exactly, since the integral of `v f_b` along each crossing is one. Its cursor factor separates from the old system and both pointer outcomes. Read/dephase the pointers, discard the new cursor, and use the old York-data interaction representation at the specified final slice. The ideal channel is exactly `C_ideal` above. In the Schrödinger picture both actual and comparator also carry the same `U0(S)` on the old system; that common unitary does not change the distance.

For the massive cursor, Duhamel compares its carrier-removed Hamiltonian `v p_x+p_x²/(2M)+v f_b G` to the chiral comparator. With `||G||≤π`, the normalized packet has `||eta_a'||₂=√3/a` and `||eta_a''||₂=√(63/2)/a²`. Uniformly over old inputs and arbitrary references, the chiral solution obeys

```text
A1 = π·15/(8b),
A2 = π·10/(sqrt(3)b²) + A1²,
K2 = sqrt(63/2)/a² + 2(√3/a) A1 + A2,
||Psi_massive(S)-Psi_chiral(S)|| ≤ S K2/(2M).
```

The interaction profile's weak derivatives supply `||f_b'||₁=15/(8b)` and `||f_b''||₁=10/(sqrt(3)b²)`. The estimate applies first on a suitable dense domain and extends by uniformity and boundedness. Since pointer dephasing and discarding the cursor are channels, and pure-state trace distance is bounded by the vector error,

```text
(1/2)|| C_massive,S - C_ideal ||_diamond ≤ min(1, S K2/(2M)),
```

for `S≥S_end` and the stated **fixed** new-device preparations. The diamond input is the complete old physical data space with arbitrary references, not arbitrary cursor/pointer inputs. This is a full-output bound including old scalar/qubit poststates and all eight recorded branches; it does not control the discarded cursor or bound the scalar's final energy.

For dimensionless parameters

```text
a=b=0.3, v=1, S0=1, M=10^6, S=1.7,
S_start=0.4, S_end=1.6,
K2≈876.15056,    epsilon≈0.000744728 < 0.000745,
B0≈10.81748,
< p_x²/(2M) > = Mv²/2 + 3/(2Ma²) ≈ 500000.0000167.
```

The large cursor energy, the initial synchronization to York `S`, the four-level memory and the nonlocal effect-dependent dressing are resources/assumptions, not a proposed practical apparatus. The pointer is read at a chosen final slice; permanent retention and autonomous final readout are not established.

## 5. Operational consequences and scope of the switch

For the selected packet in the earlier report, the ideal outside probability is approximately `0.79572221` by numerical quadrature. The implemented outside probability differs by at most `epsilon`, so the model does **not** solve the high no-reading fraction. The earlier analytic reading-probability lower bound at the chosen initial slice is `q>0.135`; the full-channel bound gives an actual reading probability at least `q-epsilon>0.134`. A conservative normalization inequality bounds the conditional recorded-output trace distance by `2 epsilon/q < 0.0111` for that preparation. This is not an error guarantee for arbitrary low-probability branches.

The earlier `T_t` map transports the ideal old-model instrument exactly, including poststates and later effects. By applying it to both **York-data output channels** after the above explicit identification, the same `0.000745` bound holds for their transported mathematical representations. However, in `C_new`, the cursor, pointers and `G_phys(S)` alter the constraint and can mix scalar energy. Tracing out the apparatus does not by itself turn an enlarged-constraint physical state into a physical state of the original closed theory. We have not derived a normalized scalar-time reduction or independent scalar-clock apparatus for this interacting enlarged constraint. Therefore the transported channel bound is **not** a physical full-frame switch of the new apparatus.

The full finite-bin `F_b` have nonzero energy-kernel matrix elements across arbitrarily high energy cutoffs. If `sqrt(F_b)` preserved such a cutoff subspace, its square would preserve it too; hence for each cutoff there is a supported input whose square-root output leaks beyond it. This is not yet a proof that the selected packet has divergent energy. No finite postmeasurement energy expectation, locality, required control complexity or realistic resource cost has been demonstrated. A bounded interaction and a finite initial cursor energy do not settle those questions. Exact finite-bin outcome operations and the stipulated `B`-dependent dressing themselves may be hard to realize.

## 6. Checks and next work

The [eight tests](verification/lighthouse_jt_autonomous_event_readout_test.py) construct a noncommuting four-effect finite clock, verify the polar construction and all eight **same** square-root Kraus operators including an entangled reference, check a zero-support control, check the necessity of dressing when `[H0,G]≠0`, verify constants, and simulate selected massive-cursor eigenchannels on a periodic Fourier grid. The sample grid errors are approximately `5.3×10⁻⁵–6.4×10⁻⁵` versus the analytical continuum budget `0.000745`; they do not simulate continuum JT, certify the nonlocal gate, or prove an energy bound.

The next discriminating steps are: (1) determine whether the original square-root instrument has finite scalar-energy moments on the selected packet, or construct a **specified** finite-band approximation with a measured retained-poststate error to it; (2) build and normalize the scalar-clock reduction of the actual enlarged constraint, retaining cursor and pointer outputs; (3) derive or falsify a physically local implementation of the dressed effect in a specified JT/CFT matter model. Only after these steps can the WP0 dressed-algebra/entropy question be addressed without conflating an ideal representation map with an apparatus.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:verification:. \
 python -m unittest verification.lighthouse_jt_autonomous_event_readout_test -v
```
