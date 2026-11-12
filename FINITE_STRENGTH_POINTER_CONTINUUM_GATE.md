# A finite-strength pointer: convergence, energy and a sharp-readout obstruction

## Executive result

Replace the ideal sign measurement of the [common-Fock-space test](CONTINUUM_COMPLETE_INSTRUMENT_CONVERGENCE.md) by a **specified finite-strength qubit pointer** coupled to the same smeared field observable. In the same 1D even-cosine model and under the same oscillator-energy input constraint:

1. The complete cutoff instrument converges to the complete continuum instrument for either order of the source and pointer. The comparison retains the field, pointer, two noisy record bits and arbitrary reference entanglement.
2. Unlike the sharp Lüders instrument, this pointer instrument has a finite, exactly calculable **nonselective field-energy increment**. At coupling `λ=1` it is `5/12 ≈ 0.4167` in the stated model units.
3. At each cutoff, the two complete operation orders differ by at most `2 |sin(λgκ_N)|`, **without any input-energy restriction**. This tends to zero as `O(N⁻³)`. This is a bound on the *order comparison at the same cutoff*, not an unconstrained cutoff-to-continuum convergence theorem.
4. The qubit does **not** approach a sharp sign detector when `|λ|→∞`. Its response is periodic, and for a finite-energy Gaussian state its recorded probabilities tend to an uninformative half even while its field-energy increment diverges. This concrete obstruction rules out treating the finite-strength model as merely the old sign instrument with a benign energy regulator.

The pointer coupling is a spatially smeared, **instantaneous idealized interaction** on a prescribed slice, not a constructed local spacetime detector or gravity calculation. [Fewster and Verch](https://arxiv.org/abs/1810.06512) already provide a covariant field–probe measurement framework and its causal-factorization theorem; the construction below is a specialized control, not a replacement or rederivation. Spatially extended nonrelativistic detector models can themselves create causality issues; see the review [Recent progress on local measurement theory for quantum fields](https://arxiv.org/abs/2307.08524).

## 1. Precisely specified instrument

Adopt all definitions and the common input/output Fock space in [the preceding report](CONTINUUM_COMPLETE_INSTRUMENT_CONVERGENCE.md), including `d=.4`, source `U_N=exp(−igP_N)`, readout `Q_N`, positive normal-ordered oscillator energy `H`, and the regulated zero mode. The limit operators `U` and `Q` have the same definitions there. No tail is discarded, reset or replaced.

Introduce a qubit `D` in the **fixed product state** `|0_z>` and define

```text
V_N = exp(−i λ Q_N ⊗ σ_y),       V = exp(−i λ Q ⊗ σ_y).
```

Measure the pointer in the `σ_x` basis. Preserve the measured qubit and the classical sign `s=+1 or −1`, then classically replace that sign by two recorded bits, each independently flipped with probability `q` (`q=.1` in the examples). This is an explicit CPTP postprocessing of the field–qubit state. The four outcomes sum to a channel; the two source orders both output the complete field, pointer and noisy bits. Any purifying or otherwise entangled reference is retained and untouched.

If the qubit is subsequently ignored, the field Kraus operators for ideal pointer outcome `s` are

```text
K_s,N = [cos(λQ_N) + s sin(λQ_N)] / √2,
K_s   = [cos(λQ)   + s sin(λQ)]   / √2.
```

Thus the induced effect is `K_s* K_s = [1 + s sin(2λQ)]/2`; the instrument is a bounded, periodic unsharp measurement, not a sign projector. An explicit auxiliary record for the ideal outcome could also be retained; erasing it is the stated noisy-record instrument. Subsequent measurements and bit-copying/noise are idealized operations; their hardware and thermodynamic costs are not modeled.

## 2. Complete-instrument continuum bound

For `N≥1`, use the preceding tail majorants

```text
A_N = 16/(5πd⁴N⁵),     T_N = 4/(πd⁴N⁴),
D_N(E) = 4E A_N + T_N,
S_N(E) = min{2, 2|g|[√(2E·16/(3πd⁴N³)) + √(4/(πd⁴N²))]},
E_src = g²[1/d³ + 1/(16π)],     E⁺ = (√E + √E_src)².
```

For every joint field–reference input vector of field energy at most E,

```text
||(Q−Q_N)ψ|| ≤ √D_N(E).
```

`Q_N` strongly commutes with its tail `Q−Q_N`. Consequently, for the fixed initial qubit and any reference,

```text
||(V−V_N)(ψ⊗|0_z>)|| ≤ |λ|√D_N(E),
||J_N−J||_{⋄,E} ≤ L_N(E),
L_N(E) := min{2, 2|λ|√D_N(E)} = O(N⁻²).
```

The first bound uses `|e^{ix}−1|≤|x|`; the second follows from the pure-state trace-distance bound, purification, and contraction under the common pointer measurement/record postprocessing. Here `J_N` and `J` denote the complete pointer instruments, including the final qubit and records. The source-tail result `S_N` is the previously established all-reference bound.

The source can increase the energy, so it cannot be ignored in telescoping. The field energy after **nonselective pointer measurement** is at most `E + λ²/(6d)` by the exact calculation below, uniformly in N. With source and pointer channels extended trivially to all other outputs,

```text
||J_N ∘ Ad(U_N) − J ∘ Ad(U)||_{⋄,E}
    ≤ min{2, S_N(E) + L_N(E⁺)},
||Ad(U_N) ∘ J_N − Ad(U) ∘ J||_{⋄,E}
    ≤ min{2, L_N(E) + S_N(E + λ²/(6d))}.
```

Both approach zero at fixed finite E, g and λ. The slower source estimate is `O(N⁻¹)`. Individual subnormalized outcomes and the nonselective field marginal inherit the same bounds by postprocessing; normalized conditional outputs need a positive probability lower bound. In the disjoint-smear continuum model `U` commutes with `V` and with the pointer measurement, so the two continuum instruments agree. The construction is an equal-slice operational control, **not** a refoliation test.

For `E=100`, `g=λ=1` and unhalved distance target `.01`, the above conservative inequalities give **N=1,936** for both orders. This is a sufficient cutoff for a **different measurement** than the earlier sharp sign instrument, and the large reduction from its sufficient N is not an improved estimate for the same instrument. Bounds at N−1 and the arithmetic are in the [reproducible output](verification/finite_strength_pointer_continuum.json).

## 3. Finite cutoff order difference without energy restriction

At fixed N, `[Q_N,P_N]=iκ_N`, a scalar, so the Weyl relation gives

```text
U_N† V_N U_N = V_N exp(±iλgκ_N σ_y).
```

The sign depends only on convention and is irrelevant to the norm. Both compared circuits are followed by the same pointer readout and classical postprocessing; the source acts trivially on the pointer and records. Compare their purified pre-readout states. The extra pointer rotation commutes with `V_N` and `U_N`, and the initial pointer has `<σ_y>=0`. Their overlap therefore has magnitude `|cos(λgκ_N)|`, irrespective of field input, reference or field energy. Trace-distance contraction under readout gives

```text
||J_N ∘ Ad(U_N) − Ad(U_N) ∘ J_N||_⋄
   ≤ 2|sin(λgκ_N)|
   ≤ min{2, 2|λgκ_N|}
   ≤ min{2, 32|λg|/(3πd⁴N³)}.
```

The supremum is over unrestricted normalized field–reference inputs, but the detector is always initialized in `|0_z>`. This uniform estimate exists because the pointer has a bounded generator; it contrasts with the sharp-sign order comparison, for which high-energy squeezed states prevent uniform convergence. It does **not** imply uniform convergence of `V_N` to `V`: the tail field generator is still unbounded. Also, the finite-cutoff spatial smear has global tails, so its order discrepancy is regulator leakage, not evidence of signalling between exactly local disjoint operations.

## 4. Field energy and the price of the simplified model

Write `B_N=Σ_{n≤N}h_n²` and `B=Σ_{n≥0}h_n²`. For the two disjoint even-extended triangular readout bumps, Parseval yields

```text
B = 1/(3d) = 5/6,       B_N ≤ B.
```

Conjugating the oscillator annihilation operators by `V_N` shifts each by a multiple of `λh_n σ_y /√(2ω_n)`. The cross term has zero expectation because the initial pointer is the uncorrelated `|0_z>` state with `<σ_y>=0`. For **any finite-energy field–reference input**, after averaging all pointer and record outcomes,

```text
Tr(H ρ_field,out) − Tr(H ρ_field,in) = λ² B_N/2 ≤ λ²/(6d).
```

The continuum expression is exactly `λ²/(6d)`. It remains true if the pointer is kept, because its local measurement and subsequent unread record operations do not change the field's nonselective reduced state. Selective normalized field outputs satisfy the conservative energy bound `(E+λ²B_N/2)/p_s` when the outcome probability `p_s>0`; this may be arbitrarily large as `p_s→0`.

For an illustrative detector Hamiltonian `H_D=Ω(I−σ_z)/2`, the initial detector energy is zero; after the stated ideal `σ_x` measurement its **unconditional** detector energy is `Ω/2`. Thus the change in the displayed free field-plus-detector energy between the declared endpoints is `λ²B_N/2 + Ω/2`. This is not a full work or heat budget: switching/control, the pointer-readout apparatus, record replication, noise, any reset and gravitational stress-energy are absent. It is not a bound on energy at intermediate times for a finite-duration interaction, nor is the instantaneous kick shown to be implementable as a causal spacetime coupling.

## 5. Why larger coupling does not recover a sign measurement

Take the finite-energy state obtained from the Fock vacuum by shifting the zero-mode coordinate so that the readout `Q` has mean `μ=1`; its input energy is `π/4≈0.7854`. The readout is Gaussian with variance `v≈0.26986414`. Then

```text
P_pointer(+; λ) = [1 + exp(−2λ²v) sin(2λμ)]/2,
P_sign(+) = Φ(μ/√v) ≈ 0.9728844.
```

Therefore `P_pointer(+; λ)→1/2` as `|λ|→∞`, not `P_sign(+)`. For two independent record flips with probability `.1`, the record total-variation gap tends to `0.8|0.9728844−0.5|≈0.37831`. The corresponding pointer-induced field-energy increment grows as `λ²/(6d)`. This is a counterexample for the **declared single-qubit sinusoidal instrument**, not a no-go theorem for all approximate sign measurements or for adaptive/multiple-qubit detectors. Alternative pointers and physically switched probe fields must be analyzed rather than inferred from this example.

## 6. Verification and next discriminating step

The [verification script](verification/finite_strength_pointer_continuum.py) independently diagonalizes a two-mode, 24-level-per-mode position matrix, constructs both Kraus operators and verifies four record probabilities and the predicted field-energy change. It also checks finite-M vacuum trace distances against the tail bound, the finite-N Gaussian record-order witness against the unrestricted order bound, Gaussian periodic-aliasing examples, and sufficient-cutoff arithmetic. Its pinned NumPy dependency is listed in `verification/requirements-framework-battery.txt`. These are numerical **controls**, not a proof of the continuum/all-state statements.

The next gate is to instantiate an established **spacetime-local field–probe coupling with smooth switching**, compare the energy and instrument limits for a declared switching family, and test whether temporal spreading, probe dynamics and physical records preserve causal separation. This could change the measurement and energy balance. The fixed background, 1D sector, zero-mode regulator, full source and record costs, 3+1 theory, gravitational constraints and subject/experience foundation remain open.
