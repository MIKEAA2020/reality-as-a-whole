# Lighthouse WP0: scalar-clock state, KMS and matched finite readings

## Result and scope

**Follow-up:** [a common event and York/scalar frame switch](LIGHTHOUSE_JT_COMMON_EVENT_AND_CLOCK_SWITCH.md) adds one qubit, a complete eight-outcome instrument and an explicit same-theory reduction map with retained York-energy shifts and a subsequent York/qubit POVM. It remains an engineered truncated model, not a CFT/gravitational-entropy result.

The previous [rolling-scalar gate](LIGHTHOUSE_JT_ROLLING_SCALAR_ADMISSIBILITY_GATE.md) left the zero-mode state and actual clock readings open. This pass obtains three controlled results:

1. A normalizable finite-resolution scalar clock packet cannot simultaneously be a stationary KMS state of its full noncompact zero-mode algebra. A KMS state for the **remaining** matter, however, is compatible with a separately prepared nonstationary scalar packet at the level of a stated product/scaffold. That changes the total matter state; it is not the original full thermal state.
2. The group-average construction extends exactly to an **arbitrary assumed self-adjoint remainder generator**, including signed Liouvillean spectra. This is an abstract constrained-model result, not a construction of the JT/CFT physical representation.
3. For one common, normalized `B,p` physical packet in the homogeneous model, a calibrated scalar-position POVM and the Hamiltonian-covariant time POVM produce normalized four-outcome distributions (three bins plus outside). The rigorous unconditional total-variation difference is below `0.055` for the stated support and all conditional `S`; in the selected packet and `|S|≤4`, both reading probabilities exceed `0.1078`, giving conditional TV `<0.511`. Numerical quadrature at `S=0` gives unconditional TV about `0.000176`, but the outside probability is about `0.796`.

These are **two different readout POVMs for the same scalar subsystem** under the same York-clock conditional state. They are not the same instrument, not a York-frame-versus-scalar-frame proof, not an autonomous detector, and not a gravitational algebra/entropy comparison. The high outside probability is a limitation, not a successful precision clock. Tests: [verification](verification/lighthouse_jt_clock_state_comparison_test.py).

## 1. Zero-mode KMS gate: reference state versus clock packet

Fix `B>0`, set `ħ=1`, and take the noncompact scalar's positive-momentum Hilbert space `L²(R_+,dp)` with `H=p²/(2B)`. The result is equally valid for both momentum signs on the full noncompact line.

A normal state is represented by a positive trace-class density `rho`. If it is stationary under `U(s)=exp(-isH)`, then its Hilbert–Schmidt kernel obeys

```text
exp[-is(E(p)-E(p'))] rho(p,p') = rho(p,p')   for every s.
```

Since `E(p)` is strictly increasing on `p>0`, this forces the kernel to vanish off `p=p'`; that diagonal has two-dimensional measure zero. An `L²` kernel supported there is zero, contradicting trace one. Hence **there is no normal stationary density state** on this factor for the noncompact free scalar. A normal KMS state would be stationary, so none exists on this full represented algebra. This is stronger than merely noting that the formal Gibbs operator is not trace class.

The same point follows operationally for the covariant time POVM `E_t`: a stationary state with a countably additive normalized time-reading distribution would have a translation-invariant probability measure on `R`. No such finite probability measure exists. This does not rule out non-normal KMS states on appropriate algebras, KMS states on a reduced algebra, finite-window approximations, or stationary **global constrained** states with changing conditional states. It states the normality/readout incompatibility for this free zero-mode factor.

A momentum-only commutative algebra can carry a normal probability density in `p`, but its time automorphism is trivial. It does not contain the off-diagonal clock POVM effects, so a thermal momentum distribution alone does not supply a readable clock. Conversely, a localized packet has the required momentum coherence but is nonstationary.

### A viable conditional split, not a full-source pass

Let `A_rest` have a specified β-KMS reference `omega_rest` and an implementing self-adjoint generator `L_rest` in its chosen representation. Assume a normalized implementing vector `Omega_rest` with `L_rest Omega_rest=0`, as in a standard stationary GNS/thermofield realization. Add the scalar as an independent factor, choose our finite packet for it, and take the product vector. Restriction to `A_rest` retains `omega_rest`; the **total** product state is not KMS because its scalar restriction is not stationary. This is a consistent abstract input when the tensor product, dynamics and representation really exist. It does not prove that the source's large-c CFT has this exact zero-mode split, that its bra-ket state equals this product, or that its complete constraints and type-III/type-II algebras survive the addition.

The finite control takes `h=diag(0,0.7)`, `beta=2`, `rho=e^(-beta h)/Z`, and `L=h⊗I-I⊗h`. Its thermal purification is annihilated by `L`; the test verifies KMS for a pair of matrix units. This demonstrates the state/reference distinction, not the CFT construction.

### Compact-target alternative

If the **target** is a circle of radius `R` (not merely the spatial slice), momenta are `p=n/R`, `n∈Z`. The Gibbs state is trace-class at finite `B,R,β`, but the scalar angle is periodic. On the positive branch `n≥1`, `H_n=n²/(2BR²)` and

```text
U(T_B)=I,    T_B=4π B R².
```

Consequently no normalized POVM on the whole real line can be covariant under all real translations: the periodic unitary would make a finite interval and every `T_B` translate have the same effect, incompatible with normalization. A periodic time POVM exists on a circle of period `T_B`, using generalized vectors `|t> = T_B^(-1/2) Σ_(n≥1) exp(-i H_n t)|n>` and the orthogonality of the integer frequencies `n²`. A Gibbs state is diagonal, so both its angular and periodic-time distributions are uniform. The clock is periodic, and any unwrapped winding record is a further physical system.

A positive-branch Gibbs density is KMS on the **restricted** positive-branch algebra, but not automatically on the full algebra with momentum-changing operations. For example `n=+1` and `n=-1` have equal energy; matrix units exchanging them require equal weights by the KMS condition. Zero weight on `-1` and positive weight on `+1` violate it. The branch must be justified as a restriction/superselection, not represented as the unmodified full-circle Gibbs state. With quantum-variable `B`, the period depends on `B`; a global time-circle identification needs a separate controlled construction.

## 2. Positive group average with a general remainder

Let `K` be a declared auxiliary remainder Hilbert space that includes the `B,p` sector and any further degrees of freedom. Assume the total remainder generator `H` is self-adjoint on `K`, with the `B`-dependent scalar part and other interactions/dynamics included in its domain. Consider

```text
H_kin = L²(R_S) ⊗ K,      C = -i∂_S + H.
```

The sign is the convention following the primary source's earlier canonical definitions, as documented in the previous gate. With Fourier variable `k` for `S`, `C=k+H`. For **any** unit `w∈K`, not necessarily an eigenvector of `H`, and normalized `g(c)=(πa²)^(-1/4) exp[-c²/(2a²)]`, define the kinematical vector by

```text
Psi_tilde(k) = g(k+H) w.
```

The spectral theorem and `∫|g(k+lambda)|²dk=1` give `||Psi||=1`, for any spectral values `lambda`, including a Liouvillean's negative values. Its Gaussian-regulated group average is exactly

```text
∫dt exp(-epsilon t²) <Psi,exp(itC)Psi>
  = 2 sqrt(π)/sqrt(a²+4epsilon)
  → 2π |g(0)|² > 0.
```

The Fourier inverse has the form `g_check(S) exp(-iSH)w`; the on-shell physical representative is `w` up to the stated normalization. For suitable test states the spectral on-shell pairing is positive, and null states are quotiented. The exponential does not imply that the physical state evolves in an external time; `S` is the internal conditioning coordinate.

This calculation pays the positivity/nonzero-norm bill **conditional on** a single self-adjoint `H` and the simple linear constraint. It does not derive a matter generator, establish its CFT/KMS domains, resolve the sign conflict in the primary source, prove full JT constraints or anomalies, select the physical measure on `B`, or construct clock-dressed traces. A separate finite spectral-shift test includes negative, zero and positive remainder energies as a check of the shift argument.

## 3. Two readings of one common physical packet

Use the previous truncation with `B∈(0,∞)`, `p>0`, `H=p²/(2B)`, and choose the normalized physical vector

```text
w(B,p) = b(B) f(p),
b(B) = sqrt(2) sin[π(B-7)]     for 7<B<8,  0 otherwise,
f(p) = cos[π(p-p0)/(2δ)]/sqrt(δ)  for |p-p0|<δ,  0 otherwise,
p0=1.5,   δ=0.2,   v0(B)=p0/B.
```

It can be obtained from the group-averaged packet in §2. The conditional state is `psi_S(B,p)=exp[-i S p²/(2B)]w(B,p)`. This uses a state family on `7<B<8`; it does not fix `B` to a number. On each `B` fiber define:

- **Position-calibrated reading:** measure the compressed scalar-position POVM and report `t=q/v0(B)`. This calibration is controlled by `B` and uses the chosen momentum center. It is not an exactly Hamiltonian-covariant clock.
- **Energy-covariant reading:** use the quadratic-generator POVM from the preceding gate, whose generalized time kets have weight `sqrt(p/B)` and phase `exp[-i p²t/(2B)]`.

The required `B`-dependent coupling/readout is assumed; no local apparatus implementing it is supplied. Both are decomposable effects on the same physical `B,p` representation, and the data below average over `|b(B)|²`. B-coherences are not probed by these particular effects. One clock reading cannot be substituted for the other without specifying the measurement; the common numerical labels are a stated calibration.

The respective conditional probability densities are

```text
P_q(t|S,B) = | sqrt(v0)/(sqrt(2π)) ∫dp exp[i p v0 t] psi_S(B,p)/b(B) |²,
P_E(t|S,B) = | 1/sqrt(2π) ∫dp sqrt(p/B) exp[i p²t/(2B)] psi_S(B,p)/b(B) |².
```

The covariant density translates exactly as `P_E(t|S,B)=P_E(t-S|0,B)`. The position density does not generally do so, because different momenta have different velocities. Both integrate to one over all `t`. Partition the output into `[-10,-3)`, `[-3,3)`, `[3,10]`, and `outside`; endpoint choices are immaterial for these densities. The outside outcome is retained, not silently postselected.

## 4. Analytic all-state bound and packet-specific lower bound

For any normalized `p`-state supported in `[p0-δ,p0+δ]`, set

```text
v_-=(p0-δ)/B,   v_+=(p0+δ)/B,   v0=p0/B,
c=sqrt(2δ/(2π)),
A_B = c (sqrt(v_+) + sqrt(v0)),
D_B = c [max(sqrt(v0)-sqrt(v_-), sqrt(v_+)-sqrt(v0))
         + sqrt(v0) T δ²/(2B)].
```

For `|t|≤T`, remove the irrelevant phase `exp[i(E0-v0 p0)t]` from the position amplitude, where `E0=p0²/(2B)`. The energy phase differs by exactly `(p-p0)²t/(2B)`. By `|exp(ix)-1|≤|x|` and Cauchy–Schwarz, the amplitude difference is at most `D_B`, while the sum of magnitudes is at most `A_B`. Thus, for **any** partition of `[-T,T]` and its single outside outcome,

```text
TV(P_q,P_E) ≤ ∫_(-T)^T |P_q(t)-P_E(t)|dt
             ≤ 2T sup_(7≤B≤8) A_B D_B < 0.055.
```

This bound is independent of `S` and holds for arbitrary normalized supported states, including mixtures, after integrating over `B`; it concerns outcome probabilities only, not postmeasurement states. A physical reference system may be present, but this bound makes no claim about its retained output.

For the explicit cosine packet, `∫f(p)dp=4sqrt(δ)/π`. For `|S|≤4`, phases relative to `p0` on the entire interval satisfy

```text
position: |phase| ≤ [p0 δ T + (p0 δ + δ²/2)·4]/7 < π/2,
time:     |phase| ≤ (p0 δ + δ²/2)(T+4)/7 < π/2.
```

Using the positive cosine packet and the minimum velocities gives, uniformly over `7≤B≤8`,

```text
Pr_q(|t|≤10 | S) > 0.1297,
Pr_E(|t|≤10 | S) > 0.1078.
```

After conditioning on the reading event, the finite-bin TV is at most `0.055/0.1078 < 0.511`: for a **single outside outcome**, the unnormalized inside L1 difference plus the outside probability difference is twice the full TV. This is a conservative analytic guarantee; it does not claim the apparatus has high availability or accuracy.

### Numerical check for the selected packet

Independent Gauss–Legendre quadratures over `B`, `p` and each finite reading bin yield:

| `S` | POVM | bin 1 | bin 2 | bin 3 | outside |
|---|---|---:|---:|---:|---:|
| 0 | position | 0.07127560 | 0.06190250 | 0.07127560 | 0.79554630 |
| 0 | energy time | 0.07121380 | 0.06185018 | 0.07121380 | 0.79572221 |
| 4 | position | 0.06981557 | 0.06160221 | 0.07205870 | 0.79652352 |
| 4 | energy time | 0.06975299 | 0.06154995 | 0.07199788 | 0.79669919 |

At `S=0`, the unconditional TV is approximately `0.00017592`, and after conditioning on a reading, approximately `0.00000461`. At `S=4` the corresponding values are about `0.00017566` and `0.00001135`. The quadrature stability check is not a rigorous interval-error certificate. These numbers compare different POVMs on the **same selected state**, not different physical frames or poststates.

## 5. Decision and next target

The noncompact branch is viable as a finite prepared clock factor alongside a separate KMS reference for the remainder, but **not** as an ordinary normal thermal state of the whole added scalar factor with a normalized covariant real-line time reading. A compact target gives a thermal state but changes the clock into a periodic one. Neither alternative has yet been matched to the source's large-c CFT algebra or physical trace.

Next construct a **same-event instrument** in this common `B,p` physical Hilbert space and compare its York- and scalar-conditioned descriptions, including calibration, clock backaction, outside/ambiguous outcomes and preparation transport. Then verify whether the source's matter/zero-mode representation and the combined constraints actually admit that setup. Only once the physical algebras, state, trace conventions and common task exist should the WP0 entropy calculation begin. A scalar time-POVM comparison is neither that result nor a proof of clock independence.

## Reproduction

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:verification:. \
  python -m unittest verification.lighthouse_jt_clock_state_comparison_test -v
```

The analytic norm, phase and total-variation bounds are derived above. The finite numerical checks validate selected constants and controls; they do not prove the assumptions of a JT/CFT or cosmological model.
