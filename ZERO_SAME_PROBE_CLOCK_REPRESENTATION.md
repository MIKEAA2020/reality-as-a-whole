# The same four-outcome probe in an R-time representation

## Result

We now take the **same** [factorwise clock–memory probe](ZERO_FACTORWISE_CLOCK_MEMORY_PROBE.md), its full interacting Hamiltonian, new massive cursor, old apparatus, R clock and both probe records, and explicitly transport its retained state to an R-time representation. This is not the previous comparison of two different instruments.

The full transformation is an isometry into a **constrained subspace** of time-wavefunctions. It transports every one of the four outcome operations and any correctly transported subsequent observable exactly; on the same input and the same operation, their joint probabilities agree. A later finite-bin R-clock POVM can also be represented explicitly, including its outside-bin outcome and unnormalized conditional apparatus states.

There is an important limitation: a **classicalized R reading plus conditional apparatus state is not a complete description of the retained quantum clock**. Even for the same probe and its no-bin branch, two admissible inputs can yield orthogonal full poststates while the R-time reading and every apparatus state conditional on that reading are nearly indistinguishable. Under the stated model bounds, any state-independent reconstruction from that reduced data must have worst-case trace error greater than **0.4955** on this two-state example. Retaining the full encoded R-time coherence avoids this information loss.

This is a bounded mathematical result and a precise negative control. The exact isometry is a representation of **one specified theory**, not equivalence of independently quantized gravity theories or a demonstration that a real observer can implement the additional R-time POVM. It does not turn the semibounded clock into an ideal self-adjoint time operator. [Tests](verification/zero_same_probe_clock_representation_test.py).

## 1. One theory and the same complete instrument

Use exactly the previous positive root H_new. Group all factors except R into X: the old two-window apparatus, the new massive cursor, the two probe qubits, and any untouched reference. Write

```text
H_new = H_X + K_R + V,
H_X = H_A + p_new²/(2M) + B₀,
V = v f_b(x_new)[ Θ_R σ_y^(D_R) + Θ_M σ_y^(D_M) ].
```

Tensor identities and the reference's zero Hamiltonian are suppressed. `K_R=k≥0`, `Θ_R=arcsin√(P_Λ E_R(B) P_Λ)` and `Θ_M=(π/2)Π₁` are exactly the previous operators. V is bounded; H_new is positive and self-adjoint on the free domain. The old and new cursor preparations, the probe-ready state and scalar synchronization remain the specified resources.

At the previous output slice T, let Π_(c,m) project the two probe registers onto c,m∈{0,1}. On the enlarged initial-data space the **actual** four operations are

```text
I_(c,m)(ρ) = Π_(c,m) U_new(T) ρ U_new(T)† Π_(c,m),
U_new(T)=exp(iH_new T),
Σ_(c,m) I_(c,m) is trace preserving.
```

The initial ρ includes the specified new cursor and ready probes; an arbitrary reference may be entangled with the old apparatus and R. Nothing in the transport identity requires the R clock to be initially independent. All four results, including clock no-bin and memory no-record, remain present. The final probe interrogation at T is still an assumed output operation; the model has not derived an autonomous external observer.

Unlike the earlier reduced comparison, **the new cursor is retained here**. Its later trace-out is a separate optional restriction.

## 2. An exact, constrained R-time representation

For the clock use the isometric positive-frequency Fourier map

```text
(F_R ψ)(u) = (1/√(2π)) ∫₀∞ e^(−iku) ψ(k) dk,
F_R†F_R=I_R,           F_R F_R†=1_(i∂u≥0).
```

The integral is understood in the L²/Plancherel sense. Define on the dilation space `L²(R,du;H_X)` the unitary multiplier

```text
(W f)(u)=exp(−iH_Xu) f(u),       D=W(I_X⊗F_R).
```

D is an isometry from the actual R⊗X Hilbert space onto a closed subspace, not onto arbitrary time-wavefunctions. On the natural spectral domain,

```text
D K_R D† = i∂u−H_X,
D(H_X+K_R)D† = i∂u,
range(D) = 1_(i∂u−H_X≥0) L²(R,du;H_X).
```

The last projection is defined by joint functional calculus: `i∂u` and the constant fiber operator H_X strongly commute. For the earlier clock band, the more restrictive encoded projector is

```text
P_Λ^rel = 1_Λ(i∂u−H_X).
```

Thus positive frequency and the finite band become **correlations between the R-time Fourier spectrum and the X energy**. They are not removed by declaring u a classical clock coordinate. In particular, multiplication by a sharp finite-time indicator generally does not preserve the encoded band subspace.

The coordinate u is the Naimark time variable for R's covariant POVM. W chooses a natural free-X rotating identification; it does not assume that the full interacting H_new is free or that u is a universal monotonic clock. Other identifications can be chosen but their operators and states must then be transported accordingly.

## 3. Transport the actual probe and its records

Define the full encoded state and branch operators on `range(D)` by

```text
ρ_rel = DρD†,
K_(c,m)^rel = D Π_(c,m) U_new(T) D†,
I_(c,m)^rel(ρ_rel) = K_(c,m)^rel ρ_rel K_(c,m)^rel†.
```

The adjoint D† is the inverse **on the encoded range**. For each branch,

```text
I_(c,m)^rel(DρD†) = D I_(c,m)(ρ) D†,
Σ_(c,m) K_(c,m)^rel† K_(c,m)^rel = D D†.
```

Consequently the complete joint c,m probabilities, clock and apparatus poststates, new-cursor correlations, and any untouched reference are transported exactly. For any subsequent POVM or instrument on the same retained space, transport its Kraus operators/records by D as well; all joint probabilities are identical. The total-variation discrepancy for this **same-theory representation identity** is exactly zero. It is not the `0.00781` comparison between the two different instruments in the earlier report.

This exactness is not an independent physical test: it follows from conjugating the *same* operation and preparation by an isometry. Its value is that the clock, cursor, four outcomes and correlations are now explicit rather than replaced by a new instrument. It does not prove equality of independently quantized reductions, a local measurement mechanism, or agreement after choosing different interventions.

The full interaction remains present. In particular Θ_R is a band-supported integral operator, not generally multiplication by a function of u. If `θ(u,u')` is the time-representation kernel of Θ_R and `χ` is an encoded wavefunction, the R-probe part of the transformed interaction has the form

```text
(V_R^rel χ)(u) = v ∫du' θ(u,u')
   exp(−iH_Xu) [f_b(x_new) σ_y^(D_R)] exp(iH_Xu') χ(u').
```

The memory-probe term is diagonal in u but conjugated by the same free-X rotation. `Θ_R` is Hilbert–Schmidt here: `P_Λ E_R(B) P_Λ` has finite trace and `arcsin(√x)≤(π/2)√x` for x∈[0,1]. Thus the displayed clock kernel is well-defined in L², with the bounded X factor. More generally the transformed interaction is simply `D V D†` on the encoded range. We do **not** replace it by a local-in-u pulse or discard its backaction.

## 4. A later R-time reading and its full joint statistics

After the four-outcome probe, one may add a **separate** ideal R-clock POVM reading. This is an additional operation, not a reinterpretation of the already recorded c bit. For a positive branch state σ, express its encoded operator as `DσD†` and write its diagonal X-valued density as `s(u)`; for general positive trace-class σ this is defined almost everywhere by a pure-state/spectral decomposition. Then

```text
p(c,m; u∈J) = ∫_J du Tr_X s_(c,m)(u),
unnormalized X state for J = ∫_J du s_(c,m)(u).
```

J may be any measurable finite bin, with the complementary outcome `R\J` retained. A point u has a probability **density**, not positive point probability. If a nonzero-probability bin is normalized, divide by its actual probability; no normalized conditional state is assigned to a zero-probability outcome. With all u retained, the four branch densities sum to total probability 1.

Equivalently, in the scalar representation, first apply `F_R`, take its time diagonal and transport X by `exp(−iH_Xu)` at each u. Any later X observable or operation depending on the reading must be conjugated in the opposite direction in the scalar description. This yields exactly the same joint probabilities. R is discarded in this **classical time-reading output**; retaining the full encoded operator `DσD†`, including cross-u coherences, is a different and richer output. A laboratory implementation and its energy/time resources for this extra reading have not been supplied.

## 5. A same-instrument obstruction to reconstruction after classicalizing R

The previous report proves an unconditioned complete-channel comparison with error `δ≈0.0004657794` for the actual factorwise probe and the instantaneous comparator. The same vector-level argument holds **before tracing the new cursor**: both the pulse and massive/chiral comparisons bound the full joint vector, and the ideal chiral cursor ends in a common translated packet independent of the old input. Reading/dephasing the probe registers is contractive. Thus the same δ also bounds the complete channel with the new cursor retained, on its fixed prepared state and arbitrary old/R input and reference.

Consider the probe's clock **no-bin** branch c=0. Its comparator clock effect is `I−E`, `E=P_Λ E_R(B)P_Λ`, and its clock Kraus operator is `A₀=√(I−E)`. Since E is positive and

```text
||E|| ≤ Tr(E) = ℓ|Λ|/(2π) = 1/(2π),
A₀² ≥ [1−1/(2π)] I,
```

A₀ is invertible on the whole clock space and preserves P_Λ. Define normalized, orthogonal clock states

```text
g₁(k)=1_[7000,7100](k)/√100,
g₂(k)=1_[9000,9100](k)/√100.
```

They are translates in k. Their sharp frequency edges give an infinite time variance; they are admissible finite-energy clock states but are **not** the previously calibrated cosine packet. The example therefore does not exclude a switch on a more restrictive calibrated state family. For each i, select an initial R state in Λ which at scalar r is proportional to

```text
A₀^(−1) exp[−iK_R(T−r)] g_i.
```

Both are normalizable and band-supported. The instantaneous comparator's clock state after its c=0 outcome and the remaining free evolution is exactly g_i. Its c=0 probability is at least `1−1/(2π)`. Take the **same** original apparatus and new-cursor preparation for both inputs, independent of R. The comparator's memory probabilities sum to 1, so choose one memory branch m with probability at least 1/2. The same choice works for both inputs, and its joint probability with c=0 is at least

```text
κ=[1−1/(2π)]/2 ≈ 0.4204225.
```

The two ideal conditional outputs have the **same X state** and orthogonal R states g₁,g₂, so their full trace distance is 1. Yet their time wavefunctions differ only by a phase:

```text
(F_R g₂)(u)=exp(−i2000u)(F_R g₁)(u).
```

Consequently their R-time probability densities and their X states conditional on every u are exactly equal, even after the W rotation. This remains true for all finite bins and all reading-dependent later X instruments. The full encoded states remain orthogonal; for example, a suitable subsequent clock-energy question distinguishes their supports. Such a question must be transported along with the state in any other representation.

The result extends quantitatively from the comparator to the **actual same probe**. Let σ_i be its normalized `(c=0,m)` poststate for input i, and let C_time discard the R coherence while retaining the classical u and corresponding X output. The complete-channel bound and the joint ideal branch probability κ imply the actual branch probability is at least `κ−δ>0.4199`, and

```text
D_trace(σ_i,σ_i^ideal) ≤ e:=2δ/κ < 0.002216.
```

Trace-distance contractivity and the triangle inequality give

```text
D_trace(σ₁,σ₂) ≥ 1−2e > 0.9955,
D_trace(C_time(σ₁), C_time(σ₂)) ≤ 2e < 0.00444.
```

For any state-independent quantum recovery channel R acting only on the classicalized time-and-X output, if its maximum reconstruction error on these two states is ε, then

```text
1−2e ≤ D_trace(σ₁,σ₂) ≤ 2ε + 2e,
ε ≥ (1−4e)/2 > 0.4955.
```

This is a **restricted no-go for universal recovery after this specific information discard**, not a no-go for switching clocks. Keeping R quantum, retaining the full encoded cross-u kernel, measuring additional clock observables, or restricting the admissible state family can change the conclusion. The two constructed clock inputs differ from the earlier β packet, so the earlier preparation-specific `0.00781` probability comparison is not applied to them. The comparator δ bound is uniform in the old/R input; all other cursor and apparatus preparation assumptions remain in force.

## 6. Checks and the remaining frontier

The [finite test](verification/zero_same_probe_clock_representation_test.py) uses a periodic eight-level clock and a small X system. It checks isometric transport of the same four operations on a clock–X correlated input, equality of a transported later observable, the transformed band subspace, nonlocality of a compressed interaction in the time basis, and two orthogonal poststates with identical time-conditioned X data. It also checks the continuum packet-phase identity and quantitative constants. The finite clock has a discrete Fourier time basis and is **not** a numerical simulation of the continuum R, old massive cursor, new massive cursor or full constraint.

What is established is a mathematically explicit R-time encoding of the actual fixed probe, with exact transported predictions and a robust loss result if a later R reading is classicalized. What remains is to justify an operational internal clock reading and switching protocol with controlled finite resources, analyze whether a useful **restricted observable algebra/state family** can be reconstructed, and address interacting/turning clocks and gravitational refoliation. A representation identity does not derive the physical clock coupling, the actual universe, lived succession, or a common physical–experiential constitution.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_same_probe_clock_representation_test \
 verification.zero_factorized_clock_probe_test \
 verification.zero_clock_probe_poststate_obstruction_test -v
```

The construction uses standard positive-frequency Fourier/Naimark and isometric transport ideas; it is not a novelty claim over clock-neutral quantum-reference-frame literature such as [Höhn and Vanrietvelde](https://arxiv.org/abs/1810.04153) or [Höhn, Smith and Lock](https://arxiv.org/abs/2007.00580).
