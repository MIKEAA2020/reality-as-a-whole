# Lighthouse WP0: a common event in York and scalar clock descriptions

## Result and limits

In the closed-Milne-inspired homogeneous model, add one two-level event system and construct **one fixed eight-outcome instrument**: a qubit `X` event together with a finite-bin scalar-clock readout, including the outside outcome. There is an explicit unitary between the York-reduced and positive-energy-scalar-reduced physical Hilbert spaces. Transporting the **same** preparation, all eight operations, retained poststates and any later observables gives exactly identical joint probabilities, including for inputs entangled with a reference. The scalar-frame operation necessarily shifts the retained York-clock energy when the qubit changes energy; a naive spin flip at fixed York energy generally leaves the physical sector.

A subsequent joint York-time/qubit POVM yields an explicit interference law, so the transported event can be followed by a nontrivial retained-record comparison. The instrument and POVMs are mathematical, constraint-compatible constructions. **This is an exact same-model frame representation result, not an independently quantized clock-switch theorem, an autonomous apparatus, or a physical gravitational entropy comparison.** Its clock and qubit couplings, ideal York reference, conditioning prescription, Hilbert-space measure, scalar zero mode and state remain assumptions. The full CFT, local gravitational constraints, operational backreaction and crossed-product traces are not constructed.

Continuum calculations are analytic; [nine finite-control tests](verification/lighthouse_jt_common_event_frame_switch_test.py) verify spectral shifts, constraint commutation, all branches and reference/poststate transport, but the discrete periodic control is not a continuum convergence proof. Previous work: [scalar KMS and matched readings](LIGHTHOUSE_JT_SCALAR_CLOCK_KMS_AND_MATCHED_READINGS.md); [source sign and scalar gate](LIGHTHOUSE_JT_ROLLING_SCALAR_ADMISSIBILITY_GATE.md).

## 1. One constrained model and two reductions

Set `ħ=1`. The source-inspired system has York coordinate `S∈R`, `B>0`, a scalar clock with `p>0`, and a qubit. Use the sign following the source's stated earlier canonical definitions, as discussed in the preceding gate:

```text
H_clock(B,p) = p²/(2B),      h = Δ |1><1|,      Δ>0,
C = -i∂_S + H_clock + h = 0.
```

The qubit is an added finite system, not the source's holographic CFT. The momentum branch, `B` measure and direct-product representation are declared. In particular, this is not a proof that all local JT constraints or the source's KMS representation reduce to this model.

Set `E=p²/(2B)>0`, so `dp=(B/p)dE`. A normalized York-reduced physical vector is

```text
psi = (psi_0(B,E), psi_1(B,E)),
||psi||² = ∫_0^∞ dB ∫_0^∞ dE Σ_j |psi_j(B,E)|².
```

The unitary change from the `p` amplitude is `psi_j(B,E)=sqrt(B/p) w_j(B,p)`. On the chosen physical sector the York-conditioned history is `exp[-i S(E+h)]psi`, and the kinematical York momentum `k` satisfies

```text
k = -(E+h_j),        lambda := -k = E+h_j,     h_0=0, h_1=Δ.
```

Reduce instead relative to the **scalar energy/time POVM**. The residual York momentum and qubit are represented on the correlated subspace

```text
K_scalar = { zeta(B,lambda,j): lambda ≥ h_j },
(V psi)_j(B,lambda) = 1_(lambda≥h_j) psi_j(B,lambda-h_j).
```

`V` is unitary **onto this subspace**, not onto the unconstrained product `L²(R_+,dλ)⊗C²`: changing variables `lambda=E+h_j` gives exactly the same norm. The thresholds are essential. They express the support restriction of a semibounded scalar clock and a nonzero system gap.

For the covariant scalar clock generalized ket `<t|E>=exp(iEt)/sqrt(2π)`, its formal conditional slice has a common normalization factor `1/sqrt(2π)`. With the induced physical norm, the normalized frame map at scalar label `t` is

```text
(T_t psi)_j(B,lambda) = exp[i(lambda-h_j)t] (V psi)_j(B,lambda),
T_t = R_t V,        T_t† T_t = I,        T_t T_t† = P,
```

where `P` projects onto `K_scalar`. This follows by restricting `k+E+h_j=0` and contracting the scalar clock ket; its phase convention is stated explicitly. A fixed generalized clock slice is a reduction/conditioning prescription, **not** an operational probability density for obtaining that reading from a normalizable kinematical history. The separate finite-bin POVM below supplies a modeled readout. `T_t` retains the York degree of freedom; it does not discard its record or claim a physical detector selected `t`.

## 2. One complete physical event instrument

At the York reference slice `S=0`, define the event as the qubit observable `X` with projectors `Pi_m=(I+mX)/2`, `m=±1`. Let `F_b(B)` be the **same** positive scalar-time POVM effect for each of three bins `[-10,-3)`, `[-3,3)`, `[3,10]`, and the complement `outside`. The scalar-time effects are the covariant positive-energy POVM of the preceding report, acting on `L²(R_+,dE)` at each `B`; they sum to identity in the weak sense.

Choose the Lüders instrument, including its poststates:

```text
A_(m,b) = sqrt(F_b) ⊗ Pi_m,
I_(m,b)(rho) = A_(m,b) rho A_(m,b)†,
Σ_(m,b) A_(m,b)† A_(m,b) = I.
```

Each `F_b` is a bounded positive contraction, so its positive square root exists. The direct integral over `B` is understood; the actual `B`-controlled readout is an assumption. This instrument defines one particular event implementation, not the unique instrument with those effects. An abstract pointer isometry `psi ↦ Σ_(m,b) A_(m,b)psi⊗|m,b>` stores all outcomes; it specifies a quantum operation, not its autonomous hardware.

The corresponding bounded kinematical representatives are multiplication in the York coordinate by

```text
A_(m,b)(S) = exp[-i S(H_clock+h)] A_(m,b) exp[+i S(H_clock+h)].
```

They commute with the constraint unitary group: the shift of `S` under `exp(-iaC)` cancels the `H_clock+h` conjugation. This argument holds as a bounded-operator equality without assuming a formal commutator on all unbounded domains. Their action on a constraint history maps its `S=0` physical initial datum by `A_(m,b)`. The `S=0` anchor is a chosen relational event, not a derived clock-selection principle or an externally scheduled laboratory interaction.

## 3. Transport the same event, not merely its probabilities

On the scalar-reduced support, define

```text
A'_(m,b)(t) = T_t A_(m,b) T_t†,
rho'(t) = (T_t⊗I_R) rho (T_t†⊗I_R),
```

where `R` is an arbitrary retained reference. Then each **unnormalized branch**, including its clock/system/reference state, satisfies

```text
(A'_(m,b)(t)⊗I_R) rho'(t) (A'_(m,b)(t)†⊗I_R)
 = (T_t⊗I_R) I_(m,b)⊗id_R(rho) (T_t†⊗I_R).
```

The transformed Kraus operators are complete on `P`, and any later effect or instrument transported by the same `T_t` has the same joint probabilities. This includes all outside outcomes and works for arbitrary normal input/reference states, not just the packet in §5. Conditional distributions agree where the conditioning event has nonzero probability. The equality is exact because both descriptions are of the **same physical instrument**; it does not show that a different scalar-triggered experiment, a classicalized clock, or an independently imposed quantization has the same output.

For the spin-only `X` operation, the transformed action has a concrete energy shift. For `zeta∈K_scalar`,

```text
(V X V† zeta)_j(B,lambda)
  = 1_(lambda≥h_j) zeta_(1-j)(B, lambda-h_j+h_(1-j)),
```

with zero outside the relevant support. A `0→1` transition changes `lambda` by `+Δ` at fixed scalar energy `E`; a `1→0` transition changes it by `-Δ`. A same-`lambda` spin flip fails at the spectral thresholds. For a general finite-bin clock operator, the full `T_t A_(m,b) T_t†` also mixes scalar energies; it must be transported as an operator rather than replaced by this spin-only shift.

As a concrete backreaction **accounting check**, omit the scalar-bin measurement and perform only the nonselective `X` measurement on `|0>`. The scalar energy is unchanged and the qubit's mean energy increases by `Δ/2`; hence the retained York variable `lambda=E+h` increases by `Δ/2`, or `k` decreases by `Δ/2`. This is a constraint-generator ledger for the specified ideal operation, **not** a derivation of a physical energy reservoir or global cosmic-energy balance. For the sharp continuum time-bin instrument, the output energy moments and finite apparatus cost have not been bounded.

## 4. A subsequent York-reading and qubit comparison

This section supplies an explicit common follow-up rather than stopping at the abstract isometry. In the scalar frame, let

```text
<s|lambda> = exp(-i lambda s)/sqrt(2π),
Q_(m')(ds) = P ( |s><s| ⊗ Pi_(m') ) P ds,   m'=±1.
```

The `lambda` space is `L²(R_+)` with the qubit-dependent support `P`; integrate over `B` as identity. Fourier completeness gives `Σ_m' ∫_R Q_(m')(ds)=P`. Restricting `s` to chosen finite bins and adding the complement gives a normalized finite-outcome joint York-reading/qubit POVM. It is a compressed POVM, not a sharp projective York position on the physical support. A Lüders instrument for its finite effects can be chosen if its poststates are needed. It is a second modeled measurement; no dynamical order or causal localization follows from writing it after the first operation.

Take the first-event input `w(B,E)⊗|0>` and put

```text
f_b(B,E) = [sqrt(F_b) w](B,E),
g_b(B,u) = (1/sqrt(2π)) ∫_0^∞ dE exp(-iEu) f_b(B,E).
```

After the first event with outcome `(m,b)`, transform the full branch using `T_t`. The subsequent joint density for York reading `s` and qubit `m'`, including the first-branch probability, is

```text
p(m,b; s,m' | t)
 = (1 + m m' cos(Δ s))/4 · ∫_0^∞ dB |g_b(B,s-t)|².
```

The Fourier expression is understood in `L²` where needed. Summing `m'` and integrating `s` gives `q_b/2`, with `q_b=∫dB dE |f_b|²`; summing every first and second outcome gives one. The spin/York coherence and the shift `h_1-h_0=Δ` produce the interference factor. Pulling `Q` and the first instrument back using `T_t†` reproduces this **same joint measure** in the York-reduced description, including a finite `s`-outside bin. This is a genuine nontrivial common-task calculation within the declared model, but the equivalence is same-theory transport and does not establish an independently realized pair of physical clocks.

## 5. The previous packet and the no-reading cost

Use the normalized `w(B,p)=b(B)f(p)` of the [preceding comparison](LIGHTHOUSE_JT_SCALAR_CLOCK_KMS_AND_MATCHED_READINGS.md), transform it to `w(B,E)`, and choose the qubit in `|0>`. At York `S=0`, the first instrument's eight probabilities are `p(m,b)=q_b/2`; both signs have the same values:

| Scalar readout | `q_b` (quadrature) | `p(+,b)=p(-,b)` |
|---|---:|---:|
| `[-10,-3)` | 0.07121380 | 0.03560690 |
| `[-3,3)` | 0.06185018 | 0.03092509 |
| `[3,10]` | 0.07121380 | 0.03560690 |
| outside | 0.79572221 | 0.39786111 |

The numeric values use the prior converged quadrature, not a certified interval calculation. The high outside probability is real for this illustrative choice. The frame equality holds for the outside branch too, but that does not make it a high-availability clock. The prior analytic lower bound on the probability of a reading for this preparation is retained; it does not bound the energy cost or physical readout implementation.

## 6. What is and is not achieved

**Achieved:** a single declared constraint, two distinct reduction coordinates, the semibounded support and variable-`B` measure, one complete two-factor event instrument, full retained branch/reference transport, a concrete energy-shift effect, and a subsequent nontrivial York/qubit joint POVM. Exact equality is established for the same mathematical experiment; nine finite controls check its structural consequences, including an equal-effects/different-poststate counterexample.

**Not achieved:** an autonomous local event or detector; a physical scalar-readout realization; independently quantized frames; an actual source CFT/KMS zero-mode construction; inhomogeneous/refoliation constraints; a trace or entropy difference for two gravitational dressed algebras. The induced `T_t` is a representation map, and the event was engineered as a York-anchored relational operation. A proof of empirical clock equivalence must specify physical preparation and readout and control errors, not merely carry an operator through a unitary.

**Next critical step:** bound a physically realized finite-resource measurement of this *same* event and its scalar/York readouts, with both no-reading and retained poststates, while keeping the state and energy/constraint domains controlled. In parallel test whether the actual closed-Milne matter representation admits the scalar zero mode and common event. Only then construct or meaningfully compare its clock-dressed algebras and trace conventions. If an admissible source model or common task fails, report the explicit obstruction rather than treating the present isometry as WP0 completion.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:verification:. \
  python -m unittest verification.lighthouse_jt_common_event_frame_switch_test -v
```

The finite test uses five clock-energy levels, an integer qubit gap, an enlarged York-energy support, a complete two-bin clock POVM with two qubit outcomes, and an entangled reference. Its periodic spectrum and projected effects are a separate control, not the continuum time POVM or a physical JT simulation.
