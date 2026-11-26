# Recorded histories and the finite-interval clock gap

**Continuation:** [finite-shot clock calibration](ZERO_TWO_WINDOW_FINITE_SHOT_CLOCK_CALIBRATION.md) gives an explicit statistical prediction bound on a restricted packet family and an equal-click coherent counterexample outside it.

## Result

The earlier [first-reading instrument](ZERO_INTERACTING_GEOMETRY_FIRST_READING_CLOCK.md) already treated no clicks and repeated clicks in a **single-window** model. Here that idea is applied to the later, noncommuting **two-memory autonomous constraint**, retaining all three new click records and both original memories. The checkpoint readouts are additional, scheduled operations, not autonomous components of that constraint. Their complete history instrument has a normalized continuum definition; its finite-regulator outcomes and branch states agree in momentum and interacting spectral descriptions.

There is also a sharper continuum distinction between ideal reconstruction and operational stability. **Conditional on the existing 13-slice reconstruction theorem**, exact complex data on any nonempty open interval of scalar readings already determine the whole state. Yet the finite-interval data map is compact, so its inverse cannot be uniformly stable in the ordinary raw-data norm on the unrestricted infinite-dimensional physical space. There are orthogonal normalized physical states with arbitrarily close finite-interval signals. This is a mathematical instability, not proof that a chosen observable or restricted family cannot be estimated reliably.

[Verification](verification/zero_two_window_recorded_histories_test.py) tests the particular finite model, not the continuum proof. The mathematical ingredients are the bounded, positive root and the full-state slice result in [the two-window continuum report](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md).

## 1. A prescribed history instrument

Use the same `Θ_h`, scalar evolution `U_h(t)=exp(i√Θ_h t)`, and band-compressed effect E₀ as in the [two-window record model](ZERO_AUTONOMOUS_TWO_GEOMETRY_WINDOW_RECORDS.md). The original detector D and memories M₁,M₂ remain continuously coupled inside Θ. Introduce three *additional* fresh record bits for yes/no measurements at scalar readings 30, 40 and 50. At each reading use

```text
K₁ = sqrt(E₀),       K₀ = sqrt(I−E₀),       K₀†K₀+K₁†K₁=I.
```

For history `s=(s₁,s₂,s₃)`, evolve through all attempts and then to φ=100:

```text
B_s = U(50) K_(s₃) U(10) K_(s₂) U(10) K_(s₁) U(30),
p(s,a,b) = || P_(M₁=a,M₂=b) B_s ψ₀ ||².
```

The operators are bounded on the complete physical space, including its bound and scattering parts; `Σ_s B_s†B_s=I`, and the four final memory projectors resolve the identity. This proves `Σ_(s,a,b) p(s,a,b)=1` without projecting away any sector. The formula also defines the branch completely positive operation `ρ ↦ P_(a,b)B_s ρ B_s†P_(a,b)` for a density operator. h-dependent evolution and relative h coherence remain inside the same physical operation; the numerical table below averages the two h-diagonal contributions for the chosen h superposition.

The ordered first-click probabilities are obtained by summing all strings beginning `1`, `01`, or `001`; `000` is no click. Later measurements have been **performed** in this protocol. Their unconditioned completeness makes these first-click probabilities equal to those of an experiment that stops immediately at the first click, but their final memory states need not be equal: the interventions after a click can disturb them. Multiple clicks mean repeated registrations, **not** multiple geometric crossings. A no-click string is failure to register at these three attempts, not proof of no crossing or no later reading.

A formal reversible recording dilation uses a fresh qubit at each attempt and the block unitary

```text
W = [[K₀, −K₁], [K₁, K₀]].
```

K₀ and K₁ commute because they are functions of E₀; the resulting record states label each history. Tracing the added bits gives the nonselective instrument; retaining them gives distinguishable record labels. This does not supply a local, autonomous Hamiltonian or prove irreversible memory. The three switching times, fresh bits and ideal scalar reference are stipulated rather than derived.

## 2. Incident preparation and controls

Choose the original incident packet, balanced D pointer and M₁=M₂=0, with the original equal-weight logical superposition. At N=80, probabilities for the eight strings, summed over both final original memory bits, are:

| Click string at φ=30,40,50 | Probability |
|---|---:|
| 000 | 0.528276 |
| 001 | 0.012008 |
| 010 | 0.095922 |
| 011 | 0.013265 |
| 100 | 0.298657 |
| 101 | 0.004588 |
| 110 | 0.044002 |
| 111 | 0.003283 |

Thus first click at 30, 40 or 50 has probability 0.350529, 0.109187 or 0.012008; no click has probability 0.528276. Two or more clicks have probability 0.065137. The final M₁–M₂ distribution after the three nonselective attempts is

```text
        M₂=0       M₂=1
M₁=0    0.499448   0.073728
M₁=1    0.076100   0.350724
```

Without the added attempts it is approximately `[[0.509184,0.058104],[0.073726,0.358986]]`. A measurement only at φ=40 has click probability 0.159556; performing and discarding an earlier measurement at φ=30 changes that to 0.156472. These are different interventions, not two predictions for the same question. A receding packet, with all apparatus settings retained, gives probability 0.001071 for at least one click.

The largest entrywise difference in the full 32-outcome table between N=24 and N=40 is below 0.0003; N=40 and N=80 give first-click probabilities `(0.350652, 0.109163, 0.011998, 0.528188)` and `(0.350529, 0.109187, 0.012008, 0.528276)`. These numerical checks are not continuum error bounds. Results depend on the prepared state and chosen effect; no universal clock precision is inferred.

**Bound-sector control.** For h=0 at N=80, select all ten numerical eigenvectors lying outside the free grid band's continuum endpoints `[6,49/6]` and call their projector P_ext. This is a regulator spectral projection, not a continuum scattering decomposition. Its weight in the initial state is 0.004278. For the 000 outcome, the full coherent probability is 0.450324, while dephasing between P_ext and `I−P_ext` before the protocol gives 0.455078. The difference −0.004754 is a retained interference term. The complement may include other point modes, and finite-grid exterior eigenvectors are not by themselves a proof of the continuum bound weights or transition rates.

## 3. Continuum transport of the *same* instrument

Let A and B be good 13-tuples in the sense of the existing continuum theorem. `W_A` maps a physical state to its complete complex slice solution, and its image is given the transported physical norm; similarly for B. Define `T = W_B W_A⁻¹` and, for every original operator X,

```text
X_A = W_A X W_A⁻¹,    X_B = W_B X W_B⁻¹ = T X_A T⁻¹.
```

Since W_A and W_B are unitary **onto their respective induced-norm data spaces**, every `U`, `K₀`, `K₁` and final memory projector transports as a bounded operator on those spaces. In particular, `B_(s,B)=T B_(s,A) T⁻¹` and, for the same physical preparation,

```text
||P_(a,b),A B_(s,A) W_A ψ₀||_A²
 = ||P_(a,b),B B_(s,B) W_B ψ₀||_B².
```

This holds for every string and memory outcome, with all bound–scattering and channel coherence retained. It is a general consequence of transporting a fixed instrument through the earlier full-state theorem, not a new proof of that theorem. The φ checkpoints are still scalar-clock operations; using geometry-slice data as an exact state representation does **not** make these operations independently triggered by geometry, or show equivalence of separately quantized clocks. Nor does formal knowledge of W_A⁻¹ establish that a physical observer can implement it.

The numerical check instead works in the finite momentum and full interacting-eigenvector bases, not directly in the continuum slice representation. For every one of the eight branch vectors it checks reconstruction by the eigenvector matrix, and verifies the full 32-outcome joint table. This is an independent regulator-level check of the transport bookkeeping, not a proof of the continuum slice theorem.

## 4. Exact finite intervals: injective, but not stable

Fix h=0 and let `H=L²((-7,−6),dp)⊗C⁸`. Put `Ω=√Θ₀`, so Ω is bounded and `Ω≥ω_min I`, with `ω_min=√0.4`. Let A be a 13-tuple good under the existing full-state theorem. For a finite nonempty open scalar-time interval I, define R by retaining **all eight complex internal components** of

```text
(R_A,I ψ)_j(t) = L_(α_j) (2Ω)^(−1/2) exp(iΩt) ψ,
                                  j=1,…,13, t∈I,
```

where `L_α` is band-limited Fourier evaluation, including the `1/√(2π)` normalization. The order of the two Ω functions is immaterial because they commute. Internal labels and phases are not traced out.

**Exact uniqueness.** Ω is bounded, so `exp(iΩz)` is an entire operator-valued function of complex z. Each output component is therefore an entire scalar function of z. Equal outputs on an open real interval—or equal L² outputs almost everywhere there, using continuity—are equal for all real t by the identity theorem. The assumed full-state theorem for A then implies equal physical states. Thus R is injective on H. Exact values over an open interval contain infinitely precise information; this is not a finite-click reconstruction.

**Instability.** The band has length `L=1`. Each L_α has finite Hilbert–Schmidt norm squared `8L/(2π)`. Composition with the unitary evolution and `(2Ω)^(−1/2)` shows that, as a map `H → L²(I; C^(13×8))`, R is Hilbert–Schmidt, with

```text
||R||²_HS ≤ (13 × 8 × L × |I|)/(4π ω_min).
```

In particular R is compact. An injective compact map from an infinite-dimensional Hilbert space cannot have a bounded inverse on its image with the raw L² norm: otherwise the identity would be compact. More concretely, pick any unit state v and an orthonormal sequence e_n in its orthogonal complement. Compactness gives `||R e_n||→0`, so the orthogonal unit states `(v±e_n)/√2` have raw data distance `√2 ||R e_n||→0`, even though their physical-state distance is √2. The same construction can choose v with nonzero signal. Consequently arbitrarily small raw-data errors can hide an order-one state difference; no uniform state-reconstruction error bound exists on the unrestricted unit sphere.

If `s_k` denotes the decreasing singular values of R, the bound also gives `s_k ≤ ||R||_HS/√k`. This is an upper bound, not the actual singular-value asymptotic or a rate for a particular measurement. The conclusion applies to finite intervals and any finite number of slices; the injectivity part additionally assumes A is good. The physical norm transported to the image makes reconstruction an isometry by definition, but that norm is generally stronger than the raw L² signal norm and does not remove this instability.

This establishes a precise limitation on ideal signal reconstruction, not an impossibility of approximate inference on a compact/restricted preparation family, of measuring particular observables, or of introducing a justified regularization and error model. A complete complex solution signal is itself not a directly measured wavefunction from one apparatus run.

## 5. Remaining work

A genuinely operational geometry-clock comparison must realize or approximate the necessary instruments and conditioning, specify finite-noise and preparation restrictions, and compare errors in the same physical question. Distinguishing actual zero/one/multiple crossings requires a separately justified crossing-history observable; these binary records do not do so. The calculation assumes the scalar clock, couplings and preparation, and proves neither refoliation invariance in full gravity nor actual subjectivity, felt succession, or the point–sphere constitution.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_recorded_histories_test \
  verification.zero_two_window_full_slice_test -v
```
