# Smooth switching reveals a zero-mode locality failure—and a restricted repair

## Result and correction

The preceding [finite-strength pointer](FINITE_STRENGTH_POINTER_CONTINUUM_GATE.md) was tested only at one equal-time slice. Extending its **same dynamics** to two smooth interactions at different times reveals a real problem: its special zero-mode oscillator regulator produces a nonzero source–probe commutator even when the prescribed spacetime supports are spacelike separated. In the specified example the continuum integrated commutator is approximately **−0.001826945**, not zero. This is an artifact of that regulator, not a physical superluminal signal.

Replacing that regulator by a **local massive Klein–Gordon field** changes all mode frequencies, not just the zero mode. For that modified model, finite propagation speed makes the source–probe commutator **exactly zero** for the chosen spacelike supports. A smoothly switched, finite-strength qubit instrument then has a finite field-energy increment and energy-constrained cutoff-to-continuum bounds. This is a restricted repair, not proof that the original oscillator regulator was a local field, nor an equivalence of the two physical models.

The qubit is an idealized, degenerate two-level system with an externally prescribed distributed coupling; the source, switching and record operations are externally controlled. We have **not** constructed a relativistic field probe or a physical work budget for that apparatus. For the established covariant field–probe approach and causally ordered instruments, use [Fewster and Verch](https://arxiv.org/abs/1810.06512); for standard finite propagation of Klein–Gordon fields, see [Dereziński and Siemssen](https://arxiv.org/abs/1709.03911), Appendix E. Their results are not novel claims of this project.

## 1. Spatial and temporal setup

Work on a circle of circumference `2π`, with an even-cosine field sector and a fixed background. The parity projection itself is not a fully local field net: a readout centered at `+y` also has its reflected support at `−y`. The separation calculation below includes **both** supports, so the specific pair of smeared operations is spacelike in the underlying circle. It does not establish locality for arbitrary operations in the parity-projected theory.

Let `F_d(x)` be a normalized nonnegative even `C∞` bump supported on `|x|<d`, `d=.4`, proportional there to `exp[−1/(1−(x/d)²)]`. Let the source be centered at 0; the readout is centered at `y=π/2`, with its reflected copy included by the even sector. Let `b_a(t)` be the same kind of normalized even bump with half-width `a=.08`. Source and readout switch with

```text
χ_s(t) = b_a(t),       χ_d(t) = b_a(t−T),       T=.3.
```

The minimum circular spatial separation of the source from either readout support is `y−2d≈.770796`; the maximum time separation is `T+2a=.46`. Thus every pair of points in the source and either readout support is spacelike on the chosen background.

With `e_0=1/√(2π)`, `e_n=cos(nx)/√π` for `n≥1`, define

```text
f_0=h_0=1/√(2π),
f_n=(1/√π)∫ F_d(x) cos(nx) dx,
h_n=f_n cos(ny),
χ̂(ω)=∫ b_a(t) cos(ωt) dt.
```

For field frequencies `ω_n>0`, interaction-picture mode evolution gives

```text
Q_h(t)=Σ h_n [q_n cos(ω_n t) + p_n sin(ω_n t)/ω_n],
P_f(s)=Σ f_n [p_n cos(ω_n s) − ω_n q_n sin(ω_n s)],
[Q_h(t),P_f(s)] = i Σ f_n h_n cos[ω_n(t−s)].
```

This is a free-field, fixed-slice representation, not an absolute or external clock for the framework. The coordinate time only labels the prescribed background calculation.

## 2. The special zero-mode regulator fails the spacetime test

The preceding common-space model used `ω_0=m=.5` but `ω_n=n` for `n≥1`. It is a valid oscillator representation for its equal-slice result. Dynamically, however, the extra zero-mode restoring force is a spatially global term, not the local mass term `m²φ(x)`.

For `|t−s|` below the support separation, ordinary massless propagation on the circle gives

```text
Σ_{n≥1} f_n h_n cos[n(t−s)] = −1/(2π).
```

The left side alone has removed the massless zero-mode contribution. This is an identity for the classical wave kernel and its canonical commutator; it does **not** assume a normalizable massless zero-mode Fock vacuum. Thus the actual regulated commutator is

```text
[Q_h(t),P_f(s)] = i [cos(m(t−s))−1]/(2π).
```

Integrate against the two normalized even switching bumps. Their Fourier transforms are real, so the integrated scalar commutator is exactly

```text
κ_old = [cos(mT) χ̂(m)² − 1]/(2π) ≈ −0.001826945349.
```

It is nonzero despite the spacelike support condition. The [verifier](verification/smooth_switched_locality_gate.py) independently computes the old-mode sum and agrees with this expression. With `g=λ=1`, the old oscillator vacuum and two independently noisy record bits at flip probability `.1`, the resulting order-dependent record total variation is about `0.00085243`. This value is an artifact of the specified 1D model, not a prediction of physical signalling. At equal time the extra term is zero, so the preceding equal-slice convergence and commutator results are not overturned; their extension to finite switching was unjustified.

## 3. Local-mass replacement and exact spacetime commutation

Change the free field to the even sector of a local massive Klein–Gordon field:

```text
ω_n = √(n²+m²),   m=.5,    H_m=Σ_{n≥0} ω_n a_n†a_n.
```

The zero-mode frequency remains `.5`, but **all nonzero frequencies and the reference vacuum change**. Finite propagation for the Klein–Gordon equation makes `[Q_h(t),P_f(s)]=0` at all pairs of points in the specified spacelike supports, including reflected readout support. Hence, writing

```text
A = ∫ χ_s(s) P_f(s) ds,       B = ∫ χ_d(t) Q_h(t) dt,
κ = −i[B,A],
```

we have exactly `κ=0` in the continuum. The analogous cutoff sum `κ_N` generally is nonzero because Fourier truncation spreads the smears. Numerical summation through N=256 gives about `−1.1×10⁻¹⁶`; that is a floating-point **control**, not the proof of exact zero. The proof is the support property of the local Klein–Gordon propagator.

The finite duration source and detector interactions in the interaction picture are

```text
H_s(s)=g χ_s(s) P_f(s),
H_d(t)=λ χ_d(t) Q_h(t) ⊗ σ_y.
```

The qubit has zero free gap and begins in a product `|0_z>` state. Because the self-commutators of the linear field interactions are scalars and `σ_y²=I`, time ordering contributes only irrelevant global phases. Thus the source and detector unitaries are, up to those phases,

```text
U=exp(−igA),      V=exp(−iλB⊗σ_y).
```

They commute for the spacelike pair. Read the detector in the `σ_x` basis and retain it, the field and the same two noisy record bits as before. The complete operations, including each subnormalized outcome, therefore commute in this **specific** model. Reversing the formal order is an algebraic locality control; it is not an experimental reversal of two fixed time windows. This neither proves full relativistic detector realizability nor extends the result to a qubit with an arbitrary noncommuting internal dynamics.

For a cutoff `N`, the same calculation as in the pointer report gives an unrestricted-input fixed-cutoff order bound

```text
||J_N∘Ad(U_N) − Ad(U_N)∘J_N||_⋄ ≤ 2|sin(λgκ_N)|,
κ_N = Σ_{n≤N} f_n h_n χ̂(ω_n)² cos(ω_n T).
```

For the local-mass model, `κ_N→0` by the local continuum result and smooth convergence. A finite mode cutoff is spatially nonlocal, so its residual is regulator leakage. With the old zero-mode regulator, the analogous `κ_N` instead tends to the nonzero `κ_old` above. A bound alone is not a lower bound; the explicit noisy-record vacuum example establishes a nonzero old-model effect.

## 4. Complete continuum convergence and endpoint field energy

Put all cutoffs and the continuum on the common Fock space of `H_m`; cutoff operations act as the identity on modes above N. For `N≥1`, define four actual smooth-tail sums

```text
F_N=Σ_{n>N} f_n²χ̂(ω_n)²,     G_N=Σ_{n>N} ω_n f_n²χ̂(ω_n)²,
A_N=Σ_{n>N} h_n²χ̂(ω_n)²/ω_n²,
T_N=Σ_{n>N} h_n²χ̂(ω_n)²/ω_n,
S_N(E)=min{2, 2|g|[√(2EF_N)+√(G_N/2)]},
L_N(E)=min{2, 2|λ|√(4EA_N+T_N)}.
```

The standard Fock annihilation/creation estimates and `|e^{ix}−1|≤|x|` bound, respectively, the complete source channel and complete pointer instrument cutoff errors by `S_N(E)` and `L_N(E)`, including arbitrary field–reference entanglement. Pointer measurement and record noise are common CPTP postprocessings. Because the spatial and time bump functions are compactly supported and `C∞`, their Fourier coefficients decrease faster than every inverse power; the tails and the displayed bounds tend to zero faster than every inverse power at fixed E, g and λ. This is an analytic rate statement for fixed smooth smear/switch shapes, not a uniform statement in increasingly sharp switching.

The source's vacuum coherent field-energy increment and the detector's nonselective field-energy increment are

```text
E_src = (g²/2) Σ ω_n² f_n²χ̂(ω_n)²,
E_det = (λ²/2) Σ h_n²χ̂(ω_n)².
```

They are finite. `E_src` is the source increment **in the vacuum**; an arbitrary input can have a source cross term, giving the general upper bound `E⁺=(√E+√E_src)²`. In contrast, for any finite-energy input, `E_det` is the exact nonselective detector field-energy increment because the initialized detector has `<σ_y>=0`; pointer readout and unread noisy records do not change the averaged field state. The corresponding cutoff increment is a partial sum, no greater than `E_det`.

Consequently, for complete field–pointer–record outputs and arbitrary reference systems,

```text
||J_N∘Ad(U_N) − J∘Ad(U)||_{⋄,E} ≤ min{2, S_N(E)+L_N(E⁺)},
||Ad(U_N)∘J_N − Ad(U)∘J||_{⋄,E} ≤ min{2, L_N(E)+S_N(E+E_det)}.
```

Individual subnormalized outcomes and the nonselective field marginal inherit the bound. Normalized conditional outputs require a positive outcome-probability lower bound. These estimates do not prove unconstrained cutoff-to-continuum diamond convergence.

For the given numerical example with `g=λ=1`, numerical quadrature gives `E_det≈0.414079` and `E_src≈14.621146` in the changed model's dimensionless units. In the idealized closed field–degenerate-qubit system, endpoint free-field energy change can be attributed to the prescribed external switching work, but this does not include the controller, pointer readout, copying, noise, resetting, or gravitational response. Nor is vacuum source cost a worst-case arbitrary-state cost.

## 5. Controls and next gates

The [script and output](verification/smooth_switched_locality_gate.py) check two quadrature resolutions, the exact old zero-mode expression, finite-N mass and old-mode commutators, a finite-energy vacuum record witness, endpoint energies and a separate two-mode finite-Fock matrix energy control. At N=4 and N=8 the mass-model mode-sum residual is nonmonotone, illustrating why a single small cutoff residual is not a convergence proof. Numerical near-zero is not exact causality and the finite matrices do not establish the continuum estimates.

A subsequent [two-field probe gate](LOCAL_TWO_FIELD_PROBE_AND_CUTOFF_ORDER.md) replaces the qubit's direct system coupling with a smoothly coupled relativistic probe field and derives a complete cutoff-order bound. It still uses a prescribed source and an externally modeled outgoing readout qubit and records; continuum convergence of that interacting instrument is not established. Even the repaired calculation here remains a 1+1 fixed-background even-sector model, with a mass and state chosen by hand. It does not establish the earlier massless/zero-mode dynamics, 3+1 convergence, a gravity/refoliation test, emergent spacetime, experience, or necessary actuality. No framework-level closure follows.
